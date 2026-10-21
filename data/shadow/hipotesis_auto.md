# Hipótesis automáticas — 2026-10-21 10:59 UTC
_Generado por shadow_postmortem.py sobre 992791 resoluciones (PNL=+129596.53€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.255 (n=194)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=628)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.213 (n=881)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.137)

- **PATRÓN** `n_total_lado` > `66.0` → IC=+0.180 (n=279)

  - _Acción_: Kelly boost +0.90€ cuando `n_total_lado` > 66.0 (IC base=+0.137)

- **PATRÓN** `banda_hit_calibrado` > `0.6329` → IC=+0.271 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6329 (IC base=+0.137)

- **PATRÓN** `banda_z` > `9.189` → IC=+0.205 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.189 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=913)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2653.7599` → IC=+0.137 (n=748)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2653.7599 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.151 (n=460)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 98.0 (IC base=+0.137)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.232 (n=678)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.142)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.199 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.142)

- **PATRÓN** `banda_hit_calibrado` > `0.6168` → IC=+0.264 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6168 (IC base=+0.142)

- **PATRÓN** `banda_z` > `9.581` → IC=+0.210 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.581 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.186 (n=256)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.149 (n=814)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.153 (n=422)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 100.0 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `9753.7972` → IC=+0.135 (n=206)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 9753.7972 (IC base=+0.017)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.355` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `py_entrada` < 0.355
  - _Potencial_: sin este filtro IC_bueno=+0.239 (n=109)

- **FILTRO** `banda_hit_calibrado` < `0.8028` → IC=-0.133 (n=47)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.8028
  - _Potencial_: sin este filtro IC_bueno=+0.258 (n=97)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.189 (n=117)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.353 (n=32)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=108)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=107)

- **PATRÓN** `py_entrada` > `0.355` → IC=+0.239 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.355 (IC base=+0.130)

- **PATRÓN** `banda_hit_calibrado` > `0.8028` → IC=+0.258 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8028 (IC base=+0.130)

- **PATRÓN** `banda_z` > `7.17` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `banda_z` > 7.17 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.135 (n=113)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 4.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.140 (n=98)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 14.0 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.189 (n=117)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `911.0736` → IC=+0.173 (n=108)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 911.0736 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 79.0 (IC base=+0.130)

### BALLENAS_CONFIRMADAS_15M#XRP#15min
- **PATRÓN** `n_ballena_banda` > `30.0` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 30.0 (IC base=+0.149)

- **PATRÓN** `n_total_lado` > `43.0` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 43.0 (IC base=+0.149)

- **PATRÓN** `banda_z` > `2.517` → IC=+0.250 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 2.517 (IC base=+0.149)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.719` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `ballenas_wallet_edge_medio` > 0.719 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `2466.3517` → IC=+0.192 (n=37)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2466.3517 (IC base=+0.149)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `142.32` → IC=-0.201 (n=10130)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 142.32
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=30395)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `128.66` → IC=-0.258 (n=1128)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.66
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=3387)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `121.92` → IC=-0.287 (n=1085)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 121.92
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=3256)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `167.27` → IC=-0.202 (n=2676)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 167.27
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=8029)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `133.19` → IC=-0.275 (n=1978)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.19
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=5935)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.48` → IC=-0.224 (n=385)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=385)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.204 (n=174)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=542)

- **FILTRO** `py_entrada` < `0.48` → IC=-0.145 (n=150)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=566)

### CANDIDATA9_BOT_CONSENSO#BTC#5min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.259 (n=164)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=169)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.218 (n=69)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=234)

### CANDIDATA9_BOT_CONSENSO#ETH#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.270 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=156)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.175 (n=78)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=161)

- **FILTRO** `py_entrada` < `0.47` → IC=-0.167 (n=70)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=169)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.213 (n=21911)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.108)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=4350)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `9079.5042` → IC=+0.174 (n=1970)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 9079.5042 (IC base=+0.108)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.130 (n=18546)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.129 (n=33536)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 11.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.227 (n=17386)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.149 (n=7230)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `7056.6369` → IC=+0.158 (n=2794)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 7056.6369 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.199 (n=2032)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.364 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.194 (n=2494)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `16428.8963` → IC=+0.197 (n=647)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 16428.8963 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.189 (n=1787)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 7.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.187 (n=1991)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 17.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.186 (n=2552)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `16197.5868` → IC=+0.194 (n=658)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 16197.5868 (IC base=+0.183)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.169 (n=472)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.61 (IC base=+0.082)

- **PATRÓN** `libro_liquidez` > `6857.6712` → IC=+0.167 (n=124)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 6857.6712 (IC base=+0.082)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.138 (n=1132)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.44 (IC base=+0.083)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=4244)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.161 (n=3608)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 15.0 (IC base=+0.161)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.371 (n=1396)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.225 (n=781)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.347 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.214 (n=2202)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.210)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=1070)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.149 (n=696)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 11.0 (IC base=+0.143)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.261 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=838)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `2201.1634` → IC=+0.161 (n=464)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2201.1634 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.162 (n=152)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.068)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.255 (n=846)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1157)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.151 (n=1292)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.157 (n=681)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 7.0 (IC base=+0.149)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.285 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=857)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.149)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `9.0` → IC=+0.168 (n=320)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 9.0 (IC base=+0.148)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.347 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.135 (n=206)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.135 (n=1135)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 7.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.245 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.123)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `11.0` → IC=-0.297 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=149)

- **FILTRO** `py_entrada` > `0.755` → IC=-0.293 (n=138)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=73)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.206 (n=18507)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.203 (n=15721)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.235 (n=7623)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `8351.1678` → IC=+0.345 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8351.1678 (IC base=+0.201)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.183 (n=2013)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.181 (n=4253)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 18.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.183 (n=4175)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.73 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.181 (n=3485)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.180)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **FILTRO** `libro_liquidez` < `9614.35` → IC=-0.328 (n=56)

  - _Acción_: SKIP cuando `libro_liquidez` < 9614.35
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.224 (n=2194)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.230 (n=1472)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.307 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.222)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=4193)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.184 (n=3570)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 15.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.188 (n=3288)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=3637)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.248)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.362 (n=1176)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.79 (IC base=+0.248)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.248)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min
- **FILTRO** `hora_utc` < `18.0` → IC=-0.217 (n=58)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=20)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.250 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=40)

- **FILTRO** `py_entrada` > `0.755` → IC=-0.267 (n=58)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=4109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=3517)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.194 (n=3033)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.189)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.433 (n=785)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.441 (n=810)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.430 (n=831)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `4200.997` → IC=+0.436 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4200.997 (IC base=+0.426)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.432 (n=307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.442 (n=205)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.447 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.434)

- **PATRÓN** `libro_liquidez` > `20814.5134` → IC=+0.433 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 20814.5134 (IC base=+0.434)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.443 (n=279)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.431)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.434 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.431)

- **PATRÓN** `libro_liquidez` > `4523.4247` → IC=+0.433 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4523.4247 (IC base=+0.431)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.408 (n=140)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.402)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.401 (n=139)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.402)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.416 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.402)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.77` → IC=-0.318 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.77
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=26)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=23970)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=24245)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=11248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.188 (n=7681)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 12.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.201 (n=10765)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.186)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=5000)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.227 (n=4941)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.286 (n=3513)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.191 (n=4107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.212 (n=5487)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.182)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=5038)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.223 (n=3861)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.278 (n=3418)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.204 (n=10311)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.260 (n=3572)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=3987)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=4031)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.244 (n=5025)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=8740)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=8548)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `3.77` → IC=+0.136 (n=10471)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.77 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=4321)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.142 (n=4371)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=5258)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `2.76` → IC=+0.146 (n=3942)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.76 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.189 (n=4419)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.135 (n=4653)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `3.33` → IC=+0.134 (n=5266)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 3.33 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.301 (n=1673)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.293 (n=1647)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.382 (n=575)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.293)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.287 (n=759)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.357 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `5031.5994` → IC=+0.288 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5031.5994 (IC base=+0.279)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.321 (n=539)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.301 (n=792)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.297)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.392 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.297)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.298 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.297)

- **PATRÓN** `libro_liquidez` > `2113.1713` → IC=+0.313 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2113.1713 (IC base=+0.297)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.357 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.352)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.378 (n=80)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.352)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.391 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.352)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.357 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.352)

- **PATRÓN** `libro_liquidez` > `761.0655` → IC=+0.380 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 761.0655 (IC base=+0.352)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.446 (n=774)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.442 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.444 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.442 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.441)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.438 (n=370)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.437 (n=253)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.437 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.438 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.435)

- **PATRÓN** `libro_liquidez` > `5376.2936` → IC=+0.442 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5376.2936 (IC base=+0.435)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.469 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.449)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.452 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.449)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.451 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.449)

- **PATRÓN** `libro_liquidez` > `1979.3729` → IC=+0.468 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1979.3729 (IC base=+0.449)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` > `13.0` → IC=+0.385 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.396)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.409 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.396)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.431 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.396)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `hora_utc` < `5.0` → IC=-0.283 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=95)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.308 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.238 (n=59)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=57)

- **FILTRO** `libro_liquidez` < `1798.9075` → IC=-0.230 (n=87)

  - _Acción_: SKIP cuando `libro_liquidez` < 1798.9075
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=29)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.302 (n=225)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.255)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.379 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.272 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `987.2299` → IC=+0.270 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 987.2299 (IC base=+0.255)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **FILTRO** `hora_utc` < `5.0` → IC=-0.283 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=95)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.308 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.238 (n=59)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=57)

- **FILTRO** `libro_liquidez` < `1798.9075` → IC=-0.230 (n=87)

  - _Acción_: SKIP cuando `libro_liquidez` < 1798.9075
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=29)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.302 (n=225)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.255)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.379 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.272 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `987.2299` → IC=+0.270 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 987.2299 (IC base=+0.255)

### GBM_LATE_15M
- **PATRÓN** `drift_60min` |x|≤ `0.475` → IC=+0.139 (n=13481)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.475 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.125 (n=13618)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.124 (n=9445)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.3793` → IC=+0.166 (n=13483)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.3793 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.7782` → IC=+0.271 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7782 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.904` → IC=+0.192 (n=5104)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 5.904 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.2045` → IC=+0.258 (n=3925)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2045 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6193` → IC=+0.265 (n=3924)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6193 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.3029` → IC=+0.242 (n=1379)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3029 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.3479` → IC=+0.229 (n=4353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3479 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.124 (n=11302)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.6849` → IC=+0.129 (n=18835)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.6849 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` < `0.6964` → IC=+0.185 (n=2841)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6964 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.0507` → IC=+0.182 (n=2927)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.0507 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.233 (n=1613)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.6782` → IC=+0.206 (n=3662)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6782 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.221 (n=10835)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 106.0 (IC base=+0.075)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.210 (n=983)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.3473` → IC=+0.204 (n=2934)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3473 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.212 (n=1423)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.203 (n=1970)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.9802` → IC=+0.279 (n=1330)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9802 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.851` → IC=+0.284 (n=1286)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.851 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2339` → IC=+0.249 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2339 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.4408` → IC=+0.201 (n=2797)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4408 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.214 (n=3151)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `2075.9028` → IC=+0.208 (n=978)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2075.9028 (IC base=+0.200)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.214 (n=2298)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.239 (n=2449)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.0872` → IC=+0.272 (n=817)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0872 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.253 (n=894)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.5313` → IC=+0.258 (n=2449)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5313 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.0944` → IC=+0.238 (n=2197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0944 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2883` → IC=+0.264 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2883 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.4411` → IC=+0.243 (n=771)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4411 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.67` → IC=+0.243 (n=770)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.67 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1625.3772` → IC=+0.247 (n=2188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1625.3772 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.238 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.237)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.237 (n=1063)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.230 (n=1091)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.106` → IC=+0.260 (n=1060)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.106 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.239 (n=2516)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.9489` → IC=+0.278 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9489 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `0.1302` → IC=+0.234 (n=1288)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1302 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.35` → IC=+0.267 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.35 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` < `1.2335` → IC=+0.228 (n=2404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2335 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `0.623` → IC=+0.232 (n=2403)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.623 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2783` → IC=+0.268 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2783 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `2.4448` → IC=+0.257 (n=789)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4448 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.151 (n=2449)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0057 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.169 (n=817)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.153 (n=926)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.725` → IC=+0.176 (n=2449)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.725 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.07` → IC=+0.148 (n=396)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 11.07 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.189` → IC=+0.141 (n=2236)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.189 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `1.2044` → IC=+0.140 (n=2449)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.2044 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.0954` → IC=+0.159 (n=893)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0954 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `2.4537` → IC=+0.144 (n=2329)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4537 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `217.0` → IC=+0.172 (n=995)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 217.0 (IC base=+0.132)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.223 (n=1017)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=3197)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.271 (n=1166)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.268` → IC=+0.276 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.268 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.200 (n=2701)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.3532` → IC=+0.214 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3532 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `2.7012` → IC=+0.213 (n=1341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7012 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.202 (n=3650)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `1970.9487` → IC=+0.200 (n=1383)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1970.9487 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.223 (n=2405)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.1782` → IC=+0.231 (n=1203)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1782 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=1022)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.217 (n=968)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` < `0.0192` → IC=+0.276 (n=911)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0192 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.379` → IC=+0.250 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.379 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.3473` → IC=+0.260 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3473 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `2.7242` → IC=+0.229 (n=1177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7242 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.221 (n=1433)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `2049.2976` → IC=+0.221 (n=911)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2049.2976 (IC base=+0.216)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.220 (n=2262)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.216)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.142 (n=149)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=3688)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.162 (n=543)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0037 (IC base=+0.055)

- **PATRÓN** `ibs_20min` > `0.9538` → IC=+0.229 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9538 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` > `0.1402` → IC=+0.332 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1402 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` < `0.3351` → IC=+0.329 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3351 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.142` → IC=+0.191 (n=1169)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 5.142 (IC base=+0.055)

- **PATRÓN** `volumen_regimen` < `0.8578` → IC=+0.335 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8578 (IC base=+0.055)

- **PATRÓN** `volumen_regimen` > `1.2247` → IC=+0.350 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2247 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` < `0.1669` → IC=+0.328 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1669 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.2985` → IC=+0.348 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2985 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` < `1.4113` → IC=+0.351 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4113 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` > `2.2172` → IC=+0.327 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2172 (IC base=+0.055)

- **PATRÓN** `ballena_activa_n` < `132.0` → IC=+0.337 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 132.0 (IC base=+0.055)

- **PATRÓN** `ibs_20min` < `0.093` → IC=+0.174 (n=961)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.093 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` > `0.3267` → IC=+0.143 (n=460)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.3267 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` < `0.1306` → IC=+0.140 (n=1572)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.1306 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` < `0.8415` → IC=+0.147 (n=1139)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.8415 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` > `1.1677` → IC=+0.143 (n=570)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.1677 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.203 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=+0.036)

- **PATRÓN** `volumen_spike_ratio` < `1.7775` → IC=+0.140 (n=1091)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.7775 (IC base=+0.036)

- **PATRÓN** `volumen_spike_ratio` > `2.155` → IC=+0.150 (n=742)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.155 (IC base=+0.036)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.170 (n=104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=560)

- **FILTRO** `ibs_20min` < `0.2759` → IC=-0.195 (n=165)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2759
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=499)

- **FILTRO** `ibs_20min` > `0.2169` → IC=-0.132 (n=3617)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2169
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=1783)

- **FILTRO** `sigma_ewma_delta_pct` > `8.665` → IC=-0.240 (n=567)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.665
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=4833)

- **PATRÓN** `ibs_20min` > `0.7857` → IC=+0.184 (n=226)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.7857 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` > `1.0126` → IC=+0.279 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0126 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` < `0.4892` → IC=+0.263 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4892 (IC base=+0.032)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.146` → IC=+0.151 (n=210)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 3.146 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` < `0.7536` → IC=+0.262 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7536 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` > `1.0006` → IC=+0.308 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0006 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` < `0.1553` → IC=+0.279 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1553 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` < `2.1989` → IC=+0.291 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1989 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` > `1.5489` → IC=+0.267 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5489 (IC base=+0.032)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.266 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.032)

- **PATRÓN** `ibs_20min` < `0.2169` → IC=+0.146 (n=1783)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.2169 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` > `0.2659` → IC=+0.279 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2659 (IC base=-0.040)

- **PATRÓN** `volumen_regimen` < `0.7052` → IC=+0.304 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7052 (IC base=-0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.0812` → IC=+0.306 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0812 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` < `2.43` → IC=+0.300 (n=673)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.43 (IC base=-0.040)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6099` → IC=-0.179 (n=991)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6099
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=2976)

- **FILTRO** `ibs_20min` < `0.7555` → IC=-0.148 (n=2618)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7555
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=1349)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.161 (n=962)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=3005)

- **FILTRO** `ibs_20min` > `0.75` → IC=-0.204 (n=1424)

  - _Acción_: SKIP cuando `ibs_20min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=4281)

- **PATRÓN** `dist_vwap_pct` > `0.708` → IC=+0.338 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.708 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` < `0.2464` → IC=+0.304 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2464 (IC base=-0.065)

- **PATRÓN** `volumen_regimen` > `0.704` → IC=+0.317 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.704 (IC base=-0.065)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.301 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=-0.065)

- **PATRÓN** `volumen_pendiente_norm` > `0.0729` → IC=+0.306 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0729 (IC base=-0.065)

- **PATRÓN** `volumen_spike_ratio` < `1.4195` → IC=+0.320 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4195 (IC base=-0.065)

- **PATRÓN** `volumen_spike_ratio` > `1.8422` → IC=+0.310 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8422 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` > `0.7982` → IC=+0.276 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7982 (IC base=-0.006)

- **PATRÓN** `volumen_regimen` > `1.0669` → IC=+0.285 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0669 (IC base=-0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.1041` → IC=+0.280 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1041 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` < `2.1851` → IC=+0.262 (n=1268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1851 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` > `1.4295` → IC=+0.266 (n=1441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4295 (IC base=-0.006)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.210 (n=5913)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.3198` → IC=+0.169 (n=17706)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.3198 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.9479` → IC=+0.300 (n=1306)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9479 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.591` → IC=+0.162 (n=7948)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 3.591 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `1.1718` → IC=+0.264 (n=6526)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1718 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `0.6892` → IC=+0.269 (n=5831)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6892 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.2397` → IC=+0.278 (n=1948)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2397 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `1.4596` → IC=+0.262 (n=3472)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4596 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `2.645` → IC=+0.272 (n=3470)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.645 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.296 (n=10003)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.096)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.156 (n=5674)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0093 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.6581` → IC=+0.144 (n=17022)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.6581 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.7051` → IC=+0.262 (n=2362)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7051 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.1951` → IC=+0.265 (n=1788)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1951 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2944` → IC=+0.317 (n=1153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2944 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.5797` → IC=+0.289 (n=3393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5797 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.2668` → IC=+0.283 (n=3495)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2668 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.295 (n=7651)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 77.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.581` → IC=-0.129 (n=2424)

  - _Acción_: SKIP cuando `ibs_20min` < 0.581
  - _Potencial_: sin este filtro IC_bueno=+0.189 (n=2429)

- **FILTRO** `ibs_20min` > `0.7415` → IC=-0.213 (n=1023)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7415
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=3075)

- **FILTRO** `sigma_ewma_delta_pct` > `4.362` → IC=-0.208 (n=900)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.362
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=3198)

- **PATRÓN** `ibs_20min` > `0.9205` → IC=+0.314 (n=1214)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9205 (IC base=+0.031)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.986` → IC=+0.215 (n=859)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.986 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.2292` → IC=+0.302 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2292 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` < `1.4427` → IC=+0.253 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4427 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` > `2.2496` → IC=+0.274 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2496 (IC base=+0.031)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.281 (n=1076)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.031)

- **PATRÓN** `ibs_20min` < `0.1648` → IC=+0.160 (n=1026)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1648 (IC base=-0.030)

- **PATRÓN** `volumen_pendiente_norm` < `0.0733` → IC=+0.411 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0733 (IC base=-0.030)

- **PATRÓN** `volumen_spike_ratio` < `2.5999` → IC=+0.406 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5999 (IC base=-0.030)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.399 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=-0.030)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1149` → IC=+0.214 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1149 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `1.1954` → IC=+0.193 (n=1729)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 1.1954 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `0.6835` → IC=+0.201 (n=1545)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6835 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` < `0.0746` → IC=+0.191 (n=1588)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.0746 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.2762` → IC=+0.230 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2762 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `1.4243` → IC=+0.219 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4243 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` > `2.4876` → IC=+0.193 (n=568)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.4876 (IC base=+0.022)

- **PATRÓN** `ballena_activa_n` < `273.0` → IC=+0.227 (n=1134)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 273.0 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `1.1702` → IC=+0.225 (n=1108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1702 (IC base=-0.004)

- **PATRÓN** `volumen_regimen` > `0.6201` → IC=+0.232 (n=1108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6201 (IC base=-0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2715` → IC=+0.292 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2715 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.5317` → IC=+0.239 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5317 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.1598` → IC=+0.245 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1598 (IC base=-0.004)

- **PATRÓN** `ballena_activa_n` < `201.0` → IC=+0.240 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 201.0 (IC base=-0.004)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.310 (n=860)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.268)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.275 (n=2706)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.268)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.309 (n=1357)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.268)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.693` → IC=+0.301 (n=831)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.693 (IC base=+0.268)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.281 (n=2245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.268)

- **PATRÓN** `volumen_spike_ratio` > `3.2074` → IC=+0.283 (n=831)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2074 (IC base=+0.268)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.279 (n=3069)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.268)

- **PATRÓN** `libro_liquidez` > `2051.6976` → IC=+0.284 (n=860)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2051.6976 (IC base=+0.268)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.283 (n=1561)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.268)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.326 (n=1014)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.1808` → IC=+0.310 (n=983)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1808 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.320 (n=851)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.292)

- **PATRÓN** `ibs_20min` < `0.3704` → IC=+0.295 (n=2234)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3704 (IC base=+0.292)

- **PATRÓN** `ibs_20min` > `0.2609` → IC=+0.299 (n=1013)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2609 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.533` → IC=+0.311 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.533 (IC base=+0.292)

- **PATRÓN** `volumen_pendiente_norm` < `0.1971` → IC=+0.290 (n=2183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1971 (IC base=+0.292)

- **PATRÓN** `volumen_pendiente_norm` > `0.3414` → IC=+0.307 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3414 (IC base=+0.292)

- **PATRÓN** `volumen_spike_ratio` < `1.7293` → IC=+0.296 (n=939)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7293 (IC base=+0.292)

- **PATRÓN** `volumen_spike_ratio` > `2.6617` → IC=+0.301 (n=967)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6617 (IC base=+0.292)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.294 (n=1176)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `2042.1384` → IC=+0.307 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2042.1384 (IC base=+0.292)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.294 (n=1398)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.292)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.737` → IC=-0.188 (n=1072)

  - _Acción_: SKIP cuando `ibs_20min` > 0.737
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=3217)

- **PATRÓN** `ibs_20min` > `0.877` → IC=+0.175 (n=1021)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.877 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` > `0.1544` → IC=+0.236 (n=770)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1544 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.2161` → IC=+0.231 (n=1221)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2161 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` < `1.0082` → IC=+0.244 (n=1262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0082 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` > `0.6704` → IC=+0.233 (n=1281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6704 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` < `0.1639` → IC=+0.237 (n=1520)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1639 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.1029` → IC=+0.248 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1029 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` < `2.4504` → IC=+0.239 (n=1386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4504 (IC base=+0.030)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.266 (n=1239)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 102.0 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.1951` → IC=+0.232 (n=980)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1951 (IC base=-0.002)

- **PATRÓN** `volumen_regimen` < `1.0307` → IC=+0.238 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0307 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` < `0.1017` → IC=+0.249 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1017 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.291 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.7961` → IC=+0.270 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7961 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.4356` → IC=+0.252 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4356 (IC base=-0.002)

- **PATRÓN** `ballena_activa_n` < `109.0` → IC=+0.266 (n=835)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 109.0 (IC base=-0.002)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7606` → IC=-0.214 (n=1864)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7606
  - _Potencial_: sin este filtro IC_bueno=+0.306 (n=1865)

- **FILTRO** `ibs_20min` > `0.6471` → IC=-0.236 (n=907)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6471
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=2726)

- **FILTRO** `sigma_ewma_delta_pct` > `8.508` → IC=-0.246 (n=424)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.508
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=3209)

- **PATRÓN** `ibs_20min` > `0.7606` → IC=+0.306 (n=1865)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7606 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` > `0.2143` → IC=+0.337 (n=827)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2143 (IC base=+0.046)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.495` → IC=+0.185 (n=579)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 9.495 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` < `0.8471` → IC=+0.333 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8471 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` > `0.7033` → IC=+0.326 (n=1250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7033 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` < `0.1593` → IC=+0.323 (n=1446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1593 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.353 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` < `1.4408` → IC=+0.349 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4408 (IC base=+0.046)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.340 (n=1193)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.046)

- **PATRÓN** `ibs_20min` < `0.6471` → IC=+0.121 (n=2726)

  - _Acción_: Kelly boost +0.60€ cuando `ibs_20min` < 0.6471 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` < `0.2058` → IC=+0.252 (n=1118)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2058 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` < `0.7017` → IC=+0.263 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7017 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.0762` → IC=+0.264 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0762 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` < `2.4253` → IC=+0.253 (n=1156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4253 (IC base=+0.032)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.271 (n=1174)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.032)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.346 (n=1757)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.304)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.307 (n=764)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.304)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.314 (n=939)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.304)

- **PATRÓN** `ibs_20min` > `0.66` → IC=+0.336 (n=1966)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.66 (IC base=+0.304)

- **PATRÓN** `dist_vwap_pct` > `0.2066` → IC=+0.329 (n=1110)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2066 (IC base=+0.304)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.802` → IC=+0.325 (n=955)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.802 (IC base=+0.304)

- **PATRÓN** `volumen_regimen` > `0.8621` → IC=+0.321 (n=1310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8621 (IC base=+0.304)

- **PATRÓN** `volumen_pendiente_norm` > `0.2797` → IC=+0.344 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2797 (IC base=+0.304)

- **PATRÓN** `volumen_spike_ratio` > `1.4265` → IC=+0.315 (n=1884)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4265 (IC base=+0.304)

- **PATRÓN** `libro_liquidez` > `2624.5942` → IC=+0.312 (n=1310)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2624.5942 (IC base=+0.304)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.337 (n=1689)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.304)

- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.335 (n=1381)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.304)

- **PATRÓN** `drift_60min` |x|≤ `0.1867` → IC=+0.306 (n=911)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1867 (IC base=+0.304)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.315 (n=802)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.304)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.306 (n=1017)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.304)

- **PATRÓN** `ibs_20min` < `0.3675` → IC=+0.329 (n=2069)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3675 (IC base=+0.304)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.345` → IC=+0.319 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.345 (IC base=+0.304)

- **PATRÓN** `volumen_regimen` < `0.7185` → IC=+0.310 (n=912)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7185 (IC base=+0.304)

- **PATRÓN** `volumen_regimen` > `1.2222` → IC=+0.332 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2222 (IC base=+0.304)

- **PATRÓN** `volumen_pendiente_norm` > `0.2833` → IC=+0.352 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2833 (IC base=+0.304)

- **PATRÓN** `volumen_spike_ratio` < `1.4153` → IC=+0.314 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4153 (IC base=+0.304)

- **PATRÓN** `volumen_spike_ratio` > `2.1353` → IC=+0.306 (n=859)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1353 (IC base=+0.304)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.226 (n=4362)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.0871` → IC=+0.202 (n=4361)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0871 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=13562)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.5581` → IC=+0.234 (n=13078)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5581 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.1642` → IC=+0.208 (n=5288)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1642 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.357` → IC=+0.257 (n=3429)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.357 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.1893` → IC=+0.169 (n=8674)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1893 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` > `0.6248` → IC=+0.164 (n=8673)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.6248 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2935` → IC=+0.206 (n=1912)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2935 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6134` → IC=+0.192 (n=4226)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6134 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `1975.9` → IC=+0.181 (n=11682)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 1975.9 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.198 (n=11992)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 94.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.185 (n=8355)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.007 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.0796` → IC=+0.228 (n=4180)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0796 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=4659)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.236 (n=12528)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.006` → IC=+0.197 (n=2040)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 10.006 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.685` → IC=+0.181 (n=11048)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 2.685 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.1822` → IC=+0.163 (n=8937)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1822 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2941` → IC=+0.224 (n=1856)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2941 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `1.5598` → IC=+0.179 (n=5178)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.5598 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.637` → IC=+0.185 (n=3923)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.637 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.192 (n=11499)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 100.0 (IC base=+0.180)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.233 (n=733)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.3321` → IC=+0.232 (n=2194)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3321 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.227 (n=818)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.220 (n=1486)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `0.9275` → IC=+0.294 (n=1463)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9275 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.924` → IC=+0.331 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.924 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.273 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.8412` → IC=+0.209 (n=1385)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8412 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `1.4375` → IC=+0.215 (n=2076)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4375 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.227 (n=2378)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.215)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.252 (n=1697)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0082 (IC base=+0.250)

- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.261 (n=772)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.250)

- **PATRÓN** `drift_60min` |x|≤ `0.0656` → IC=+0.310 (n=566)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0656 (IC base=+0.250)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.254 (n=1731)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.250)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.253 (n=819)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.250)

- **PATRÓN** `ibs_20min` < `0.2966` → IC=+0.275 (n=1488)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2966 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.252 (n=1476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` > `0.2974` → IC=+0.291 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2974 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` < `1.4328` → IC=+0.272 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4328 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` > `2.6907` → IC=+0.252 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6907 (IC base=+0.250)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.254 (n=1907)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.250)

- **PATRÓN** `libro_liquidez` > `1526.94` → IC=+0.258 (n=1691)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1526.94 (IC base=+0.250)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.253 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.250)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.217 (n=660)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.1597` → IC=+0.181 (n=1316)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.1597 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=2076)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.3323` → IC=+0.222 (n=1974)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3323 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.1362` → IC=+0.212 (n=1176)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1362 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.29` → IC=+0.220 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.29 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.6926` → IC=+0.163 (n=869)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.6926 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.194 (n=318)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `1.4125` → IC=+0.171 (n=645)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.4125 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `2.5032` → IC=+0.166 (n=645)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.5032 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `419.0` → IC=+0.156 (n=1897)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 419.0 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.169 (n=2061)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0058 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.2345` → IC=+0.173 (n=1813)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.2345 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.184 (n=987)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.6154` → IC=+0.205 (n=2059)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6154 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.49` → IC=+0.189 (n=390)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 11.49 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.236` → IC=+0.144 (n=1789)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.236 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.2053` → IC=+0.159 (n=2059)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2053 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.0934` → IC=+0.148 (n=1749)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.0934 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.4989` → IC=+0.152 (n=1939)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4989 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.4236` → IC=+0.145 (n=1939)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4236 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `201.0` → IC=+0.176 (n=625)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 201.0 (IC base=+0.144)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.240 (n=738)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.3992` → IC=+0.224 (n=1946)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3992 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.234 (n=811)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=1144)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.418` → IC=+0.302 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.418 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` < `0.0994` → IC=+0.214 (n=1893)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0994 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.3544` → IC=+0.231 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3544 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `1.7691` → IC=+0.214 (n=943)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7691 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.7129` → IC=+0.228 (n=972)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7129 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=2642)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `1957.7806` → IC=+0.229 (n=1002)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1957.7806 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.0087` → IC=+0.252 (n=1263)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0087 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.5685` → IC=+0.249 (n=1894)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5685 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.280 (n=717)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0099` → IC=+0.300 (n=834)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0099 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.434` → IC=+0.271 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.434 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.3557` → IC=+0.279 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3557 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.7474` → IC=+0.237 (n=796)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7474 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.1533` → IC=+0.237 (n=1206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1533 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2040.8584` → IC=+0.241 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2040.8584 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.235 (n=1211)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.234)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.172 (n=2123)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0074 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.076` → IC=+0.199 (n=708)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.076 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=2199)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.3118` → IC=+0.213 (n=2121)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3118 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1444` → IC=+0.199 (n=1292)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1444 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.82` → IC=+0.198 (n=492)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 9.82 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.0238` → IC=+0.159 (n=1867)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.0238 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1042` → IC=+0.178 (n=871)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1042 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.8232` → IC=+0.151 (n=1386)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.8232 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `2.5084` → IC=+0.171 (n=693)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.5084 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `4607.4199` → IC=+0.184 (n=1414)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 4607.4199 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `138.0` → IC=+0.157 (n=2057)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 138.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.155 (n=2221)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0072 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.395` → IC=+0.145 (n=2220)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.395 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.166 (n=1053)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.684` → IC=+0.187 (n=2220)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.684 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.1534` → IC=+0.157 (n=2215)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1534 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.603` → IC=+0.159 (n=549)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 9.603 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.8554` → IC=+0.156 (n=1480)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8554 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.3001` → IC=+0.192 (n=336)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.3001 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.81` → IC=+0.136 (n=1387)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.81 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.5548` → IC=+0.129 (n=694)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.5548 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `7445.0269` → IC=+0.190 (n=1007)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 7445.0269 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `67.0` → IC=+0.153 (n=896)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 67.0 (IC base=+0.128)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.177 (n=1080)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0104 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.4386` → IC=+0.130 (n=2096)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.4386 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.172 (n=1135)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 15.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `0.4878` → IC=+0.217 (n=2383)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4878 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `0.1961` → IC=+0.190 (n=1387)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1961 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.519` → IC=+0.280 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.519 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `1.175` → IC=+0.143 (n=2382)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.175 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` < `0.1612` → IC=+0.135 (n=2416)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.1612 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.4385` → IC=+0.149 (n=771)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4385 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.131 (n=2498)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `2763.4172` → IC=+0.209 (n=1080)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2763.4172 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.160 (n=733)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 19.0 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.139 (n=2428)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0108 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.108` → IC=+0.172 (n=810)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.108 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=2470)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.219 (n=2433)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.845` → IC=+0.123 (n=372)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` > 8.845 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.469` → IC=+0.132 (n=2148)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 2.469 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.1756` → IC=+0.130 (n=2428)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1756 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1651` → IC=+0.123 (n=2352)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1651 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2757` → IC=+0.147 (n=324)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2757 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4463` → IC=+0.134 (n=755)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.4463 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `2.4253` → IC=+0.134 (n=755)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.4253 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2646.1014` → IC=+0.190 (n=1101)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2646.1014 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.130 (n=1982)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 42.0 (IC base=+0.120)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.245 (n=1965)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0131 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.1286` → IC=+0.240 (n=733)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1286 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.226 (n=2277)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=1977)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.66` → IC=+0.258 (n=2201)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.66 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.1824` → IC=+0.228 (n=1422)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1824 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.606` → IC=+0.250 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.606 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` < `1.1799` → IC=+0.225 (n=2198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1799 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `0.6187` → IC=+0.231 (n=2198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6187 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.2835` → IC=+0.272 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2835 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `2.4722` → IC=+0.227 (n=2139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4722 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `1.8099` → IC=+0.233 (n=1426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8099 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `2843.0726` → IC=+0.226 (n=997)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2843.0726 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.233 (n=983)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.229)

- **PATRÓN** `sigma_h` > `0.0226` → IC=+0.239 (n=1012)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0226 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.0876` → IC=+0.261 (n=744)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0876 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.248 (n=1087)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.229)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.230 (n=999)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` < `0.43` → IC=+0.257 (n=2234)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.43 (IC base=+0.229)

- **PATRÓN** `dist_vwap_pct` > `0.2956` → IC=+0.236 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2956 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.319` → IC=+0.261 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.319 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` > `0.639` → IC=+0.236 (n=2231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.639 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.284 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `1.4386` → IC=+0.232 (n=2076)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4386 (IC base=+0.229)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.208 (n=1479)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.183)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.190 (n=1117)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0089 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.1296` → IC=+0.201 (n=1474)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1296 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.215 (n=1657)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.4878` → IC=+0.217 (n=2992)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4878 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.7901` → IC=+0.202 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7901 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.62` → IC=+0.211 (n=1450)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.62 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.8641` → IC=+0.205 (n=2007)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8641 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.0999` → IC=+0.193 (n=1201)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0999 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` < `1.4312` → IC=+0.196 (n=1085)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4312 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.4896` → IC=+0.188 (n=1085)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.4896 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.189 (n=3784)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.02 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `2674.4599` → IC=+0.189 (n=2992)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2674.4599 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.136 (n=1211)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0038 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.3839` → IC=+0.161 (n=2411)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.3839 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.126 (n=1552)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 27.0 (IC base=+0.088)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.204 (n=410)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.3265` → IC=+0.200 (n=932)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3265 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.206 (n=849)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.6364` → IC=+0.237 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6364 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.3078` → IC=+0.196 (n=278)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.3078 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.079` → IC=+0.196 (n=399)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 3.079 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.041` → IC=+0.179 (n=896)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 4.041 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `0.8759` → IC=+0.203 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8759 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.0712` → IC=+0.184 (n=368)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.0712 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `2.1976` → IC=+0.188 (n=802)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.1976 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `1.4078` → IC=+0.180 (n=912)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4078 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `14694.0598` → IC=+0.184 (n=621)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 14694.0598 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `159.0` → IC=+0.210 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 159.0 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.186 (n=371)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0028 (IC base=+0.114)

- **PATRÓN** `drift_60min` |x|≤ `0.2687` → IC=+0.140 (n=977)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.2687 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.127 (n=1007)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 7.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.6326` → IC=+0.165 (n=977)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.6326 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` > `1.07` → IC=+0.144 (n=503)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.07 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.1608` → IC=+0.163 (n=295)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.1608 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `2.1209` → IC=+0.129 (n=965)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 2.1209 (IC base=+0.114)

- **PATRÓN** `ballena_activa_n` < `221.0` → IC=+0.161 (n=721)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 221.0 (IC base=+0.114)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.248 (n=684)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.0943` → IC=+0.233 (n=343)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0943 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=1073)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.379` → IC=+0.256 (n=916)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.379 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `0.3578` → IC=+0.214 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3578 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` < `0.2075` → IC=+0.219 (n=914)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2075 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.882` → IC=+0.242 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.882 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` < `0.8389` → IC=+0.228 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8389 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `1.1666` → IC=+0.221 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1666 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.2672` → IC=+0.257 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2672 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.4245` → IC=+0.238 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4245 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.4608` → IC=+0.232 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4608 (IC base=+0.213)

- **PATRÓN** `ibs_20min` < `0.104` → IC=+0.168 (n=347)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.104 (IC base=+0.064)

- **PATRÓN** `libro_liquidez` > `6178.6677` → IC=+0.133 (n=692)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 6178.6677 (IC base=+0.064)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.188 (n=280)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0107 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.222 (n=401)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.273 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.9739` → IC=+0.238 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9739 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.092` → IC=+0.236 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.092 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `1.0551` → IC=+0.185 (n=734)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 1.0551 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `0.714` → IC=+0.176 (n=746)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.714 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.1626` → IC=+0.191 (n=228)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1626 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.4446` → IC=+0.185 (n=268)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.4446 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `1.8231` → IC=+0.169 (n=536)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.8231 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.176 (n=865)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.02 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `3024.9723` → IC=+0.189 (n=278)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 3024.9723 (IC base=+0.167)

- **PATRÓN** `ibs_20min` < `0.5455` → IC=+0.137 (n=794)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.5455 (IC base=+0.055)

- **PATRÓN** `libro_liquidez` > `2699.4473` → IC=+0.142 (n=409)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2699.4473 (IC base=+0.055)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0239` → IC=+0.161 (n=219)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0239 (IC base=+0.152)

- **PATRÓN** `sigma_h` > `0.0144` → IC=+0.203 (n=146)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0144 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.2536` → IC=+0.176 (n=146)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2536 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.163 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 16.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.207 (n=97)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.56` → IC=+0.183 (n=197)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.56 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.2021` → IC=+0.167 (n=115)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.2021 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.738` → IC=+0.155 (n=56)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 7.738 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.275` → IC=+0.182 (n=187)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.275 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` > `0.6893` → IC=+0.165 (n=195)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.6893 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` < `0.1109` → IC=+0.169 (n=182)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.1109 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `1.4483` → IC=+0.216 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4483 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `2.5669` → IC=+0.182 (n=64)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.5669 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.177 (n=255)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.03 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `2474.2976` → IC=+0.176 (n=146)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2474.2976 (IC base=+0.152)

- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.146 (n=227)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.0125 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.129 (n=227)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 7.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.614` → IC=+0.128 (n=253)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.614 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `1.1964` → IC=+0.318 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1964 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.225` → IC=+0.176 (n=66)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 5.225 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `0.9016` → IC=+0.134 (n=170)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.9016 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.2396` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2396 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` > `2.3609` → IC=+0.127 (n=108)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 2.3609 (IC base=+0.115)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.130 (n=233)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 19.0 (IC base=+0.115)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0116` → IC=+0.228 (n=5676)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0116 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.193 (n=17726)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.4476` → IC=+0.231 (n=17029)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4476 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.8937` → IC=+0.209 (n=2105)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8937 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.245` → IC=+0.254 (n=4161)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.245 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `1.2224` → IC=+0.169 (n=11416)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.2224 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2405` → IC=+0.206 (n=3086)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2405 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.6152` → IC=+0.197 (n=5521)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6152 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `1789.1119` → IC=+0.184 (n=17028)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1789.1119 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `112.0` → IC=+0.204 (n=15665)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 112.0 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.193 (n=10290)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0074 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.4906` → IC=+0.192 (n=15413)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.4906 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=5725)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.5833` → IC=+0.242 (n=15414)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5833 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.806` → IC=+0.206 (n=2139)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.806 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.557` → IC=+0.190 (n=14903)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 3.557 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `0.7049` → IC=+0.163 (n=4575)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.7049 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.2905` → IC=+0.253 (n=2084)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2905 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.2598` → IC=+0.195 (n=6611)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.2598 (IC base=+0.187)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.216 (n=9661)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.187)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.229 (n=932)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.3482` → IC=+0.229 (n=2779)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3482 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.239 (n=1345)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.227 (n=1875)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.329 (n=1103)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.46` → IC=+0.356 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.46 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2321` → IC=+0.285 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2321 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `1.445` → IC=+0.222 (n=890)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.445 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `2.2907` → IC=+0.237 (n=1210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2907 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.243 (n=2970)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `2075.8376` → IC=+0.231 (n=926)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2075.8376 (IC base=+0.225)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.247 (n=1692)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.266 (n=2361)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.262)

- **PATRÓN** `drift_60min` |x|≤ `0.1192` → IC=+0.286 (n=1038)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1192 (IC base=+0.262)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.268 (n=2159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.262)

- **PATRÓN** `ibs_20min` < `0.5112` → IC=+0.287 (n=2359)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5112 (IC base=+0.262)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.135` → IC=+0.265 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.135 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` < `0.0954` → IC=+0.262 (n=2120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0954 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` > `0.2867` → IC=+0.292 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2867 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` < `1.5578` → IC=+0.266 (n=984)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5578 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` > `2.6411` → IC=+0.270 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6411 (IC base=+0.262)

- **PATRÓN** `libro_liquidez` > `1624.6693` → IC=+0.272 (n=2107)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1624.6693 (IC base=+0.262)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.271 (n=984)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.262)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.197 (n=926)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0028 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1045` → IC=+0.165 (n=1215)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1045 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=2875)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.3668` → IC=+0.222 (n=2466)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3668 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1264` → IC=+0.194 (n=1424)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1264 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.598` → IC=+0.159 (n=585)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 9.598 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.153` → IC=+0.152 (n=2538)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.153 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.6306` → IC=+0.173 (n=922)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6306 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.0718` → IC=+0.152 (n=2461)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.0718 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2719` → IC=+0.184 (n=397)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2719 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1792` → IC=+0.157 (n=2376)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1792 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.5299` → IC=+0.156 (n=2412)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.5299 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `239.0` → IC=+0.185 (n=886)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 239.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.165 (n=2300)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.256` → IC=+0.165 (n=2024)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.256 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=863)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.6944` → IC=+0.197 (n=2299)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.6944 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.222` → IC=+0.153 (n=381)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 11.222 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.454` → IC=+0.144 (n=2316)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 6.454 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.1954` → IC=+0.153 (n=2299)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1954 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2172` → IC=+0.197 (n=430)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2172 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `2.432` → IC=+0.151 (n=2194)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.432 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.7752` → IC=+0.154 (n=1462)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.7752 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=2985)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `274.0` → IC=+0.160 (n=926)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 274.0 (IC base=+0.143)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.260 (n=946)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=2959)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2540)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=1061)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.293` → IC=+0.325 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.293 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` < `0.132` → IC=+0.230 (n=2652)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.132 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `3.1837` → IC=+0.242 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1837 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=3384)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `1819.3955` → IC=+0.234 (n=1889)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1819.3955 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.245 (n=2338)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.1802` → IC=+0.258 (n=1169)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1802 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.262 (n=997)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.241 (n=947)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0333` → IC=+0.308 (n=887)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0333 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.597` → IC=+0.296 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.597 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3451` → IC=+0.300 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3451 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1354` → IC=+0.250 (n=1686)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1354 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.244 (n=1406)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1951.1016` → IC=+0.251 (n=1205)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1951.1016 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.256 (n=1142)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.240)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.205 (n=984)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.4214` → IC=+0.158 (n=2929)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4214 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=3036)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.2458` → IC=+0.194 (n=2929)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.2458 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1424` → IC=+0.172 (n=1555)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1424 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.122` → IC=+0.160 (n=1188)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.122 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.8653` → IC=+0.166 (n=1953)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8653 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.187 (n=381)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.5258` → IC=+0.163 (n=1257)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.5258 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.1755` → IC=+0.157 (n=1296)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.1755 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `5974.0002` → IC=+0.242 (n=1328)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5974.0002 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.169 (n=1235)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 73.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.151 (n=2428)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0075 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.4362` → IC=+0.139 (n=2427)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4362 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.155 (n=883)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.7358` → IC=+0.185 (n=2427)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.7358 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.1485` → IC=+0.145 (n=2209)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1485 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.104` → IC=+0.173 (n=371)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 11.104 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.6971` → IC=+0.144 (n=1068)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6971 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2959` → IC=+0.220 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2959 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `2.2242` → IC=+0.132 (n=2054)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.2242 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `1.4309` → IC=+0.136 (n=2334)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4309 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `7155.388` → IC=+0.211 (n=809)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7155.388 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `130.0` → IC=+0.131 (n=2071)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 130.0 (IC base=+0.129)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.161 (n=1336)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0103 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.180 (n=1082)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.4426` → IC=+0.200 (n=2944)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4426 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `1.0536` → IC=+0.210 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0536 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.709` → IC=+0.263 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.709 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.221` → IC=+0.137 (n=2944)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.221 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1623` → IC=+0.125 (n=3063)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1623 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.132 (n=381)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.8311` → IC=+0.129 (n=1918)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.8311 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.1941` → IC=+0.128 (n=1304)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 2.1941 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.131 (n=3066)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2496.1867` → IC=+0.231 (n=1335)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2496.1867 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.142 (n=936)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 24.0 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.152 (n=2459)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.01 (IC base=+0.116)

- **PATRÓN** `drift_60min` |x|≤ `0.1341` → IC=+0.154 (n=934)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1341 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.129 (n=2880)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.65` → IC=+0.212 (n=2797)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.65 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` < `0.2141` → IC=+0.136 (n=2416)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.2141 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.252` → IC=+0.134 (n=2690)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 3.252 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `0.7108` → IC=+0.139 (n=1231)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.7108 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.2245` → IC=+0.173 (n=475)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2245 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `1.4401` → IC=+0.151 (n=873)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4401 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `2667.8187` → IC=+0.206 (n=932)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2667.8187 (IC base=+0.116)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.131 (n=2312)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 47.0 (IC base=+0.116)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0137` → IC=+0.252 (n=2491)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0137 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.237 (n=2904)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.238 (n=1862)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` > `0.61` → IC=+0.272 (n=2495)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.61 (IC base=+0.232)

- **PATRÓN** `dist_vwap_pct` > `0.1891` → IC=+0.248 (n=1514)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1891 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.721` → IC=+0.273 (n=932)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.721 (IC base=+0.232)

- **PATRÓN** `volumen_regimen` < `1.2312` → IC=+0.238 (n=2785)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2312 (IC base=+0.232)

- **PATRÓN** `volumen_regimen` > `0.6399` → IC=+0.235 (n=2784)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6399 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.2873` → IC=+0.260 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2873 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.505` → IC=+0.254 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.505 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.233 (n=3617)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `2958.7492` → IC=+0.238 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2958.7492 (IC base=+0.232)

- **PATRÓN** `sigma_h` > `0.0255` → IC=+0.251 (n=961)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0255 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.237 (n=2707)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` < `0.5155` → IC=+0.265 (n=2879)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5155 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.196` → IC=+0.268 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.196 (IC base=+0.231)

- **PATRÓN** `volumen_regimen` > `1.2292` → IC=+0.259 (n=960)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2292 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.2821` → IC=+0.298 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2821 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` > `1.4316` → IC=+0.233 (n=2676)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4316 (IC base=+0.231)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.195 (n=5008)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.244 (n=1720)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.5073` → IC=+0.220 (n=5152)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5073 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.227 (n=1867)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.9408` → IC=+0.248 (n=1717)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9408 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` > `0.6983` → IC=+0.212 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6983 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` < `0.4334` → IC=+0.214 (n=3701)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4334 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.983` → IC=+0.220 (n=848)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.983 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.583` → IC=+0.211 (n=4584)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.583 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` < `0.7053` → IC=+0.222 (n=1654)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7053 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` < `0.107` → IC=+0.210 (n=4809)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.107 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.1667` → IC=+0.222 (n=1451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1667 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.4557` → IC=+0.218 (n=1692)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4557 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.8473` → IC=+0.211 (n=3380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8473 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.215 (n=3967)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `3756.9066` → IC=+0.220 (n=3434)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3756.9066 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.241 (n=1259)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.4905` → IC=+0.209 (n=3768)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4905 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=1271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.209 (n=1683)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.734` → IC=+0.200 (n=3768)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.734 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.6719` → IC=+0.203 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6719 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` < `0.1768` → IC=+0.190 (n=3302)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.1768 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.828` → IC=+0.203 (n=3377)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.828 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `1.0967` → IC=+0.202 (n=3146)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0967 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.198 (n=3458)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2228` → IC=+0.195 (n=759)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2228 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `1.533` → IC=+0.198 (n=1634)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.533 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `1.8131` → IC=+0.200 (n=2475)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8131 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.195 (n=5008)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.193)

- **PATRÓN** `ballena_activa_n` < `169.0` → IC=+0.203 (n=3252)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 169.0 (IC base=+0.193)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.275 (n=672)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.260)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.260 (n=684)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.260)

- **PATRÓN** `drift_60min` |x|≤ `0.0853` → IC=+0.294 (n=255)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0853 (IC base=+0.260)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.271 (n=400)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.260)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.260 (n=766)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.260)

- **PATRÓN** `ibs_20min` < `0.4896` → IC=+0.279 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4896 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.054` → IC=+0.274 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.054 (IC base=+0.260)

- **PATRÓN** `volumen_regimen` < `1.2151` → IC=+0.268 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2151 (IC base=+0.260)

- **PATRÓN** `volumen_regimen` > `0.8685` → IC=+0.273 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8685 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.350 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` < `1.8249` → IC=+0.267 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8249 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `16321.2566` → IC=+0.274 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16321.2566 (IC base=+0.260)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.252 (n=583)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.3687` → IC=+0.193 (n=1322)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.3687 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.225 (n=481)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.199 (n=483)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 5.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.207 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1382 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `0.6078` → IC=+0.179 (n=600)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.6078 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.7021` → IC=+0.186 (n=116)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.7021 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.385` → IC=+0.197 (n=1304)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` < 6.385 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `1.2212` → IC=+0.192 (n=1322)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 1.2212 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.2192` → IC=+0.199 (n=267)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2192 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` < `1.4032` → IC=+0.194 (n=439)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4032 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `1.8038` → IC=+0.187 (n=876)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.8038 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `14901.4739` → IC=+0.189 (n=600)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 14901.4739 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `692.0` → IC=+0.189 (n=1276)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 692.0 (IC base=+0.177)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.197 (n=351)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.007 (IC base=+0.193)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.219 (n=361)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.581` → IC=+0.204 (n=793)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.581 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=279)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.7037` → IC=+0.197 (n=529)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.7037 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.242 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.492` → IC=+0.238 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.492 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.211` → IC=+0.242 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.211 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.8783` → IC=+0.209 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8783 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `2493.3465` → IC=+0.229 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2493.3465 (IC base=+0.193)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.197 (n=529)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 10.0 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.229 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.250 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.281 (n=39)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.2121` → IC=+0.263 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2121 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.442` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.442 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `2.4518` → IC=+0.250 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4518 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.861` → IC=+0.250 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.861 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `2407.5596` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2407.5596 (IC base=+0.227)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.008` → IC=+0.214 (n=1378)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.4596` → IC=+0.205 (n=1378)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4596 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=500)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` < `0.5194` → IC=+0.209 (n=919)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5194 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `0.8779` → IC=+0.199 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8779 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` < `0.4062` → IC=+0.211 (n=1375)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4062 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.114` → IC=+0.206 (n=1240)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.114 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `0.8778` → IC=+0.201 (n=919)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8778 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` > `1.2314` → IC=+0.203 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2314 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` < `0.105` → IC=+0.201 (n=1267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.105 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.1638` → IC=+0.197 (n=411)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1638 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `2.4495` → IC=+0.205 (n=1349)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4495 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=1414)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `sigma_h` < `0.008` → IC=+0.205 (n=1130)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.4924` → IC=+0.211 (n=1129)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4924 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.202 (n=441)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.198 (n=755)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 10.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.3984` → IC=+0.194 (n=753)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.3984 (IC base=+0.187)

- **PATRÓN** `ibs_20min` > `0.0867` → IC=+0.190 (n=1129)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.0867 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` > `0.6705` → IC=+0.197 (n=199)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.6705 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` < `0.2251` → IC=+0.189 (n=1090)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.2251 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.36` → IC=+0.194 (n=1028)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 4.36 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `1.2445` → IC=+0.199 (n=1129)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 1.2445 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` > `0.721` → IC=+0.187 (n=1009)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 0.721 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.0742` → IC=+0.208 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0742 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` < `2.1925` → IC=+0.196 (n=973)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.1925 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.5255` → IC=+0.190 (n=369)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.5255 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `6738.937` → IC=+0.197 (n=1129)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6738.937 (IC base=+0.187)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.226 (n=334)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0072 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.205 (n=782)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` > `0.9259` → IC=+0.246 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9259 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` > `0.7398` → IC=+0.239 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7398 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.182` → IC=+0.213 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.182 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` < `0.6978` → IC=+0.229 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6978 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.196 (n=682)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.0788` → IC=+0.191 (n=338)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0788 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` < `1.5661` → IC=+0.196 (n=324)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.5661 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `2.4766` → IC=+0.208 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4766 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.189 (n=885)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.02 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `3102.823` → IC=+0.204 (n=678)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3102.823 (IC base=+0.184)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.199 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.184)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.212 (n=373)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.205)

- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.214 (n=187)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.6042` → IC=+0.226 (n=560)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6042 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.241 (n=384)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` < `0.7304` → IC=+0.227 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7304 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.8163` → IC=+0.216 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8163 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.3056` → IC=+0.206 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3056 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.868` → IC=+0.213 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.868 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `1.1368` → IC=+0.213 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1368 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `0.9368` → IC=+0.212 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9368 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` < `0.1073` → IC=+0.224 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1073 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `2.2063` → IC=+0.239 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2063 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `3008.5906` → IC=+0.224 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3008.5906 (IC base=+0.205)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.236 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.205)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.158 (n=747)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.004 (IC base=+0.072)

- **PATRÓN** `ibs_20min` > `0.3885` → IC=+0.143 (n=1605)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.3885 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` > `0.3558` → IC=+0.161 (n=559)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.3558 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.919` → IC=+0.157 (n=467)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 8.919 (IC base=+0.072)

- **PATRÓN** `volumen_pendiente_norm` > `0.2748` → IC=+0.146 (n=221)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.2748 (IC base=+0.072)

- **PATRÓN** `ibs_20min` < `0.2102` → IC=+0.227 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2102 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.336` → IC=+0.169 (n=143)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 10.336 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.1467` → IC=+0.173 (n=246)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1467 (IC base=+0.055)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.133 (n=562)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0056 (IC base=+0.091)

- **PATRÓN** `ibs_20min` > `0.3558` → IC=+0.168 (n=531)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.3558 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `0.1239` → IC=+0.162 (n=267)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.1239 (IC base=+0.091)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.124 (n=280)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0037 (IC base=+0.071)

- **PATRÓN** `ibs_20min` < `0.0556` → IC=+0.273 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0556 (IC base=+0.071)

- **PATRÓN** `volumen_pendiente_norm` > `0.2135` → IC=+0.201 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2135 (IC base=+0.071)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.131 (n=488)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.006 (IC base=+0.091)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.149 (n=212)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.091)

- **PATRÓN** `ibs_20min` > `0.4203` → IC=+0.175 (n=524)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.4203 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `0.1246` → IC=+0.191 (n=270)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1246 (IC base=+0.091)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.194` → IC=+0.244 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.194 (IC base=+0.091)

- **PATRÓN** `volumen_regimen` < `0.8145` → IC=+0.122 (n=350)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 0.8145 (IC base=+0.091)

- **PATRÓN** `volumen_pendiente_norm` > `0.2871` → IC=+0.171 (n=74)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2871 (IC base=+0.091)

- **PATRÓN** `ibs_20min` < `0.0289` → IC=+0.286 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0289 (IC base=+0.019)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.686` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.686 (IC base=+0.019)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` > `0.16` → IC=-0.204 (n=69)

  - _Acción_: SKIP cuando `ibs_20min` > 0.16
  - _Potencial_: sin este filtro IC_bueno=+0.218 (n=211)

- **PATRÓN** `ibs_20min` > `0.7458` → IC=+0.168 (n=368)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.7458 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` > `0.7321` → IC=+0.150 (n=135)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.7321 (IC base=+0.034)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.303` → IC=+0.158 (n=118)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 9.303 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.2283` → IC=+0.132 (n=104)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.2283 (IC base=+0.034)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.154 (n=241)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0103 (IC base=+0.073)

- **PATRÓN** `ibs_20min` < `0.16` → IC=+0.218 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.16 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.1699` → IC=+0.140 (n=198)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.1699 (IC base=+0.073)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.474` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.474 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` > `1.0818` → IC=+0.194 (n=70)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` > 1.0818 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.1508` → IC=+0.238 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1508 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` < `2.18` → IC=+0.149 (n=166)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.18 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` > `1.4056` → IC=+0.158 (n=188)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.4056 (IC base=+0.073)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.142 (n=185)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.06 (IC base=+0.073)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0068` → IC=-0.221 (n=206)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0068
  - _Potencial_: sin este filtro IC_bueno=-0.164 (n=108)

- **FILTRO** `dist_vwap_pct` > `0.2321` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2321
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=297)

- **FILTRO** `volumen_regimen` < `0.7615` → IC=-0.312 (n=78)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7615
  - _Potencial_: sin este filtro IC_bueno=-0.164 (n=236)

- **FILTRO** `libro_liquidez` < `891.5381` → IC=-0.225 (n=78)

  - _Acción_: SKIP cuando `libro_liquidez` < 891.5381
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=236)

- **FILTRO** `sigma_h` > `0.0052` → IC=-0.338 (n=66)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0052
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=201)

- **FILTRO** `dist_vwap_pct` > `0.4614` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4614
  - _Potencial_: sin este filtro IC_bueno=-0.276 (n=248)

- **FILTRO** `volumen_pendiente_norm` > `0.0453` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0453
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=151)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.271 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=51)

- **FILTRO** `volumen_regimen` < `0.8402` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8402
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=73)

- **FILTRO** `volumen_regimen` < `0.5547` → IC=-0.274 (n=29)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.5547
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=90)

- **FILTRO** `volumen_spike_ratio` > `1.4938` → IC=-0.341 (n=42)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.4938
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=44)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.5786` → IC=-0.464 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5786
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=79)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.375 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=79)

- **FILTRO** `volumen_spike_ratio` > `2.3922` → IC=-0.340 (n=23)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.3922
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=46)

- **FILTRO** `volumen_spike_ratio` < `1.442` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.442
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=52)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.284 (n=86)

- **FILTRO** `libro_liquidez` < `1582.3345` → IC=-0.308 (n=50)

  - _Acción_: SKIP cuando `libro_liquidez` < 1582.3345
  - _Potencial_: sin este filtro IC_bueno=-0.274 (n=51)

- **PATRÓN** `ibs_20min` > `0.941` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.941 (IC base=-0.154)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `drift_60min` |x|> `0.2367` → IC=-0.397 (n=27)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2367
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=84)

- **FILTRO** `volumen_regimen` < `0.7468` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7468
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=84)

- **FILTRO** `volumen_pendiente_norm` > `0.1362` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1362
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=62)

- **FILTRO** `volumen_spike_ratio` > `2.3736` → IC=-0.242 (n=29)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.3736
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=58)

- **FILTRO** `sigma_h` < `0.006` → IC=-0.324 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.006
  - _Potencial_: sin este filtro IC_bueno=-0.294 (n=32)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=32)

- **FILTRO** `dist_vwap_pct` < `0.2328` → IC=-0.352 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.2328
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=22)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.006` → IC=+0.202 (n=243)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=207)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.152 (n=533)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.6842 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.741` → IC=+0.224 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.741 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.077` → IC=+0.124 (n=123)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 11.077 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.6229` → IC=+0.183 (n=178)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6229 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` < `0.1528` → IC=+0.151 (n=436)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.1528 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.415` → IC=+0.178 (n=144)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.415 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.1535` → IC=+0.145 (n=550)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.1535 (IC base=+0.056)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.104` → IC=+0.179 (n=185)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 9.104 (IC base=+0.056)

- **PATRÓN** `libro_liquidez` > `3253.1348` → IC=+0.136 (n=416)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 3253.1348 (IC base=+0.056)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6942` → IC=-0.202 (n=55)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6942
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=165)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.187 (n=97)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0049 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.153 (n=197)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 12.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.149 (n=112)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 6.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.1681` → IC=+0.197 (n=292)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.1681 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.216` → IC=+0.169 (n=125)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 7.216 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.0387` → IC=+0.172 (n=132)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 1.0387 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` < `0.0706` → IC=+0.151 (n=227)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.0706 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2728` → IC=+0.160 (n=48)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2728 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.5202` → IC=+0.172 (n=260)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.5202 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.5491` → IC=+0.145 (n=232)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.5491 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `5387.0239` → IC=+0.148 (n=194)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 5387.0239 (IC base=+0.136)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1261` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1261
  - _Potencial_: sin este filtro IC_bueno=+0.142 (n=174)

- **FILTRO** `ibs_20min` > `0.3277` → IC=-0.162 (n=75)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3277
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=229)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.135 (n=124)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0038 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.196 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.9094` → IC=+0.156 (n=123)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.9094 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` < `0.0908` → IC=+0.135 (n=157)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.0908 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.015` → IC=+0.140 (n=137)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 3.015 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` < `0.6229` → IC=+0.188 (n=62)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.6229 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` < `0.1261` → IC=+0.142 (n=174)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` < 0.1261 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` < `1.7963` → IC=+0.173 (n=105)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.7963 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.957` → IC=+0.232 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.957 (IC base=+0.023)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.4` → IC=-0.278 (n=34)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=106)

- **FILTRO** `dist_vwap_pct` > `0.1699` → IC=-0.150 (n=38)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1699
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=102)

- **FILTRO** `volumen_spike_ratio` > `2.3635` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.3635
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=78)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.315 (n=122)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.255)

- **PATRÓN** `ibs_20min` > `0.6522` → IC=+0.278 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6522 (IC base=+0.255)

- **PATRÓN** `dist_vwap_pct` > `0.6502` → IC=+0.391 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6502 (IC base=+0.255)

- **PATRÓN** `dist_vwap_pct` < `0.224` → IC=+0.260 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.224 (IC base=+0.255)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.331` → IC=+0.320 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.331 (IC base=+0.255)

- **PATRÓN** `volumen_regimen` < `1.1516` → IC=+0.278 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1516 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` > `0.1037` → IC=+0.339 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1037 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` < `1.4833` → IC=+0.398 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4833 (IC base=+0.255)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.321` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.321 (IC base=-0.091)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.331 (n=69)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3447` → IC=+0.325 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3447 (IC base=+0.319)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.389 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.319)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.457 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.319)

- **PATRÓN** `drift_60min` |x|≤ `0.9647` → IC=+0.389 (n=61)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9647 (IC base=+0.319)

- **PATRÓN** `ballena_activa_n` < `1114.0` → IC=+0.370 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1114.0 (IC base=+0.319)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3366` → IC=+0.261 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3366 (IC base=+0.239)

- **PATRÓN** `elapsed_s` > `186.2` → IC=+0.250 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 186.2 (IC base=+0.239)

- **PATRÓN** `elapsed_s` < `202.5` → IC=+0.283 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 202.5 (IC base=+0.239)

- **PATRÓN** `drift_15min` |x|≤ `2.3607` → IC=+0.297 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3607 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.947` → IC=+0.276 (n=65)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.947 (IC base=+0.239)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.331 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.291 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.239)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.331 (n=69)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3447` → IC=+0.325 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3447 (IC base=+0.319)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.389 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.319)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.457 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.319)

- **PATRÓN** `drift_60min` |x|≤ `0.9647` → IC=+0.389 (n=61)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9647 (IC base=+0.319)

- **PATRÓN** `ballena_activa_n` < `1114.0` → IC=+0.370 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1114.0 (IC base=+0.319)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3366` → IC=+0.261 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3366 (IC base=+0.239)

- **PATRÓN** `elapsed_s` > `186.2` → IC=+0.250 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 186.2 (IC base=+0.239)

- **PATRÓN** `elapsed_s` < `202.5` → IC=+0.283 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 202.5 (IC base=+0.239)

- **PATRÓN** `drift_15min` |x|≤ `2.3607` → IC=+0.297 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3607 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.947` → IC=+0.276 (n=65)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.947 (IC base=+0.239)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.331 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.291 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.239)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `libro_liquidez` > `2946.4126` → IC=+0.136 (n=424)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2946.4126 (IC base=+0.103)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2946.4126` → IC=+0.136 (n=424)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2946.4126 (IC base=+0.103)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=195)

- **FILTRO** `libro_liquidez` < `5333.1276` → IC=-0.164 (n=105)

  - _Acción_: SKIP cuando `libro_liquidez` < 5333.1276
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=106)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=314)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `10893.2451` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 10893.2451
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=70)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=37)

- **PATRÓN** `liq_n` > `6.0` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `liq_n` > 6.0 (IC base=-0.008)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `ballena_activa_n` > `63.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 63.0
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=3553)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=104)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=104)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=20)

- **FILTRO** `libro_liquidez` < `15247.5472` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 15247.5472
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

- **FILTRO** `ballena_activa_n` > `558.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 558.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=1318)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=1272)

- **FILTRO** `liq_usd_total` < `12056.79` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `liq_usd_total` < 12056.79
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.292 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

- **FILTRO** `ballena_activa_n` > `118.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 118.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=717)

- **FILTRO** `liq_n` < `11.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `liq_n` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `liq_usd_total` < `13082.51` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `liq_usd_total` < 13082.51
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M#XRP#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=422)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=403)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.145 (n=181)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.495 (IC base=+0.025)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=843)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=843)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.134 (n=260)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=663)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=839)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=839)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=221)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=221)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.132 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=170)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.124 (n=91)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=145)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=239)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=263)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=257)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=350)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=350)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=195)

- **FILTRO** `libro_liquidez` < `625.8426` → IC=-0.138 (n=125)

  - _Acción_: SKIP cuando `libro_liquidez` < 625.8426
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=255)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=260)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.129 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=188)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `py_entrada` > `0.59` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=35)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.145 (n=60)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=35)

- **FILTRO** `py_entrada` > `0.47` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.180 (n=23)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.122 (n=236)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=274)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.178 (n=150)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.46 (IC base=+0.015)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.190 (n=56)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=256)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.141 (n=154)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=175)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` < 0.5 (IC base=+0.053)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.125 (n=315)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=173)

- **FILTRO** `profundidad_ratio` < `57.0` → IC=-0.150 (n=161)

  - _Acción_: SKIP cuando `profundidad_ratio` < 57.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=327)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.139 (n=203)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=228)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `profundidad_ratio` < `21.2` → IC=-0.128 (n=151)

  - _Acción_: SKIP cuando `profundidad_ratio` < 21.2
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=307)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.159 (n=89)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=377)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.154 (n=128)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=469)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=7798)

### MOMENTUM_IBS_15M#BTC#15min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=1058)

- **FILTRO** `libro_liquidez` < `15906.9303` → IC=-0.152 (n=268)

  - _Acción_: SKIP cuando `libro_liquidez` < 15906.9303
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=805)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=2289)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1413)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.47` → IC=-0.163 (n=6093)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=18892)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.177 (n=6191)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=19465)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.193 (n=1116)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=3439)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.173 (n=1060)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=3517)

- **PATRÓN** `py_entrada` > `0.495` → IC=+0.129 (n=3068)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` > 0.495 (IC base=+0.041)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.143 (n=1202)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 1.0 (IC base=+0.041)

- **PATRÓN** `libro_liquidez` > `1292.7766` → IC=+0.136 (n=2278)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 1292.7766 (IC base=+0.041)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.126 (n=2142)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.5 (IC base=+0.011)

- **PATRÓN** `libro_liquidez` > `1485.0` → IC=+0.153 (n=1557)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1485.0 (IC base=+0.011)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.154 (n=846)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=2797)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.176 (n=894)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=2746)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.205 (n=1091)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=3590)

- **PATRÓN** `ibs_20min` > `0.9643` → IC=+0.133 (n=1555)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 0.9643 (IC base=+0.039)

- **PATRÓN** `libro_liquidez` > `1804.3482` → IC=+0.128 (n=1550)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 1804.3482 (IC base=+0.039)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.155 (n=1104)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=3453)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2395)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2319)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2814)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=3554)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=443)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.257 (n=142)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=426)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.234 (n=287)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=888)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `libro_liquidez` < `3613.7014` → IC=-0.152 (n=110)

  - _Acción_: SKIP cuando `libro_liquidez` < 3613.7014
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=224)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.190 (n=143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=298)

- **FILTRO** `drift_20min_pct` |x|> `0.2047` → IC=-0.152 (n=110)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.2047
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=331)

- **FILTRO** `libro_liquidez` < `3728.8927` → IC=-0.167 (n=220)

  - _Acción_: SKIP cuando `libro_liquidez` < 3728.8927
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=221)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=935)

- **FILTRO** `libro_liquidez` < `1782.0417` → IC=-0.167 (n=238)

  - _Acción_: SKIP cuando `libro_liquidez` < 1782.0417
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=716)

- **FILTRO** `ibs_20min` > `0.8947` → IC=-0.136 (n=520)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8947
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=538)

- **FILTRO** `libro_liquidez` < `2089.8344` → IC=-0.170 (n=349)

  - _Acción_: SKIP cuando `libro_liquidez` < 2089.8344
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=709)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=233)

### MOMENTUM_IBS_5M#BNB#5min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=43)

- **FILTRO** `drift_7min_pct` |x|> `0.0725` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0725
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=28)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0331` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_7min_pct` |x|≤ 0.0331 (IC base=-0.026)

### MOMENTUM_IBS_5M#BTC#5min
- **FILTRO** `hora_utc` > `18.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=90)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.200 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.037)

### MOMENTUM_IBS_5M#DOGE#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=39)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=68)

### MOMENTUM_IBS_5M#ETH#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=414)

### MOMENTUM_IBS_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=631)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `8.0` → IC=-0.130 (n=17246)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=38299)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.285 (n=13682)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=41863)

- **FILTRO** `ibs_7min` < `0.2366` → IC=-0.229 (n=13886)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2366
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=41659)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.153 (n=18479)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=37066)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.242 (n=17185)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=52708)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.182 (n=17292)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=52601)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.148 (n=2787)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=6929)

- **FILTRO** `py_entrada` < `0.46` → IC=-0.236 (n=4800)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=4916)

- **FILTRO** `ibs_7min` < `0.7129` → IC=-0.244 (n=3206)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7129
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=6510)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.180 (n=2046)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=7670)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.272 (n=3011)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=9101)

- **FILTRO** `ibs_7min` > `0.7713` → IC=-0.212 (n=3027)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7713
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=9085)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.128 (n=2255)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=7110)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.266 (n=2196)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=7169)

- **FILTRO** `ibs_7min` < `0.7258` → IC=-0.200 (n=2340)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7258
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=7025)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.191 (n=2322)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=7043)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.264 (n=2352)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=7178)

- **FILTRO** `ibs_7min` > `0.2677` → IC=-0.196 (n=2381)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2677
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=7149)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.184 (n=2361)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=7169)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.158 (n=2281)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=6945)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.312 (n=2271)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=6955)

- **FILTRO** `ibs_7min` < `0.2955` → IC=-0.246 (n=3044)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2955
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=6182)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.195 (n=2186)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=7040)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.255 (n=3014)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=9875)

- **FILTRO** `ibs_7min` > `0.7341` → IC=-0.178 (n=3222)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7341
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=9667)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.124 (n=2962)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=6087)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.263 (n=2121)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=6928)

- **FILTRO** `ibs_7min` < `0.7281` → IC=-0.186 (n=2262)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7281
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=6787)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.188 (n=2235)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=6814)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.269 (n=2124)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=7267)

- **FILTRO** `ibs_7min` > `0.2751` → IC=-0.178 (n=2345)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2751
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=7046)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.178 (n=2297)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=7094)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=2186)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=6919)

- **FILTRO** `ibs_7min` < `0.7143` → IC=-0.223 (n=2925)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=6180)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.219 (n=2194)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=6911)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.191 (n=3245)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=10099)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.292 (n=2146)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=6938)

- **FILTRO** `ibs_7min` < `0.2` → IC=-0.223 (n=2258)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=6826)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.198 (n=2265)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=6819)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.218 (n=3095)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=9532)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=120)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.158 (n=299)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=986)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=1270)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.121 (n=209)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=495)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.152 (n=156)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=548)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=851)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.475` → IC=-0.122 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=331)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.143 (n=166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=326)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=443)

- **FILTRO** `libro_liquidez` < `3244.1491` → IC=-0.156 (n=178)

  - _Acción_: SKIP cuando `libro_liquidez` < 3244.1491
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=536)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=387)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.139 (n=1171)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.133 (n=609)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 6.0 (IC base=+0.130)

- **PATRÓN** `total_vol_5m` < `134023.4` → IC=+0.140 (n=1029)

  - _Acción_: Kelly boost +0.70€ cuando `total_vol_5m` < 134023.4 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `3639.8241` → IC=+0.148 (n=530)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3639.8241 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.148 (n=382)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 11.0 (IC base=+0.130)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4377` → IC=+0.145 (n=91)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio` |x|> 0.4377 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.202 (n=132)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.136)

- **PATRÓN** `total_vol_5m` < `375.759` → IC=+0.145 (n=240)

  - _Acción_: Kelly boost +0.72€ cuando `total_vol_5m` < 375.759 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `2571.3862` → IC=+0.199 (n=91)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2571.3862 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.154 (n=102)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 7.0 (IC base=+0.136)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3994` → IC=+0.138 (n=241)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio` |x|> 0.3994 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.135 (n=217)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 14.0 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.129 (n=289)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.04 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2340.1091` → IC=+0.138 (n=161)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2340.1091 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.139 (n=164)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 13.0 (IC base=+0.119)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.416` → IC=+0.175 (n=155)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio` |x|> 0.416 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.188 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 16.0 (IC base=+0.137)

- **PATRÓN** `total_vol_5m` < `384.1453` → IC=+0.211 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 384.1453 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `7706.3933` → IC=+0.143 (n=155)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 7706.3933 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.195 (n=103)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 70.0 (IC base=+0.137)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4324` → IC=+0.250 (n=94)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4324 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.172 (n=190)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 15.0 (IC base=+0.150)

- **PATRÓN** `total_vol_5m` < `4950.202` → IC=+0.186 (n=138)

  - _Acción_: Kelly boost +0.93€ cuando `total_vol_5m` < 4950.202 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `2945.8122` → IC=+0.160 (n=207)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2945.8122 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.162 (n=72)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 27.0 (IC base=+0.150)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.130 (n=198)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 14.0 (IC base=+0.103)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.187 (n=132)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `3591.1308` → IC=+0.163 (n=99)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 3591.1308 (IC base=+0.103)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.9794` → IC=-0.266 (n=45)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.9794
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=139)

- **FILTRO** `sigma_h` > `0.0072` → IC=-0.331 (n=164)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0072
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=494)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.189 (n=165)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0034 (IC base=-0.080)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.340 (n=48)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=147)

- **FILTRO** `T_h` > `87.9952` → IC=-0.260 (n=48)

  - _Acción_: SKIP cuando `T_h` > 87.9952
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=147)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.324 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=-0.028)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0062` → IC=-0.232 (n=39)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=25)

- **FILTRO** `pct_vs_K` |x|> `9.8932` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 9.8932
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=49)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0141` → IC=-0.267 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0141
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=88)

- **FILTRO** `T_h` < `87.9936` → IC=-0.183 (n=58)

  - _Acción_: SKIP cuando `T_h` < 87.9936
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=58)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `pct_vs_K` |x|> `3.6199` → IC=-0.293 (n=153)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.6199
  - _Potencial_: sin este filtro IC_bueno=-0.149 (n=460)

- **FILTRO** `sigma_h` < `0.005` → IC=-0.242 (n=130)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=393)

- **FILTRO** `pct_vs_K` |x|> `3.3065` → IC=-0.432 (n=130)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.3065
  - _Potencial_: sin este filtro IC_bueno=-0.163 (n=393)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0044` → IC=-0.192 (n=50)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0044
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=150)

- **FILTRO** `pct_vs_K` |x|> `2.7876` → IC=-0.363 (n=49)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7876
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=151)

- **FILTRO** `T_h` > `73.6519` → IC=-0.279 (n=138)

  - _Acción_: SKIP cuando `T_h` > 73.6519
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=47)

- **FILTRO** `pct_vs_K` |x|> `2.9891` → IC=-0.436 (n=45)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9891
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=140)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `T_h` < `139.5329` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `T_h` < 139.5329
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `sigma_h` < `0.0078` → IC=-0.262 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0078
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `3.2523` → IC=-0.403 (n=60)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.2523
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=117)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.381 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.116 (n=123)

- **FILTRO** `sigma_h` < `0.005` → IC=-0.214 (n=40)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=123)

- **FILTRO** `T_h` > `57.7851` → IC=-0.275 (n=109)

  - _Acción_: SKIP cuando `T_h` > 57.7851
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=54)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `T_h` < `145.7969` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` < 145.7969
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

- **FILTRO** `sigma_h` < `0.0098` → IC=-0.206 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0098
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.008` → IC=-0.273 (n=42)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.008
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=127)

- **FILTRO** `T_h` > `94.1391` → IC=-0.230 (n=113)

  - _Acción_: SKIP cuando `T_h` > 94.1391
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=56)

- **FILTRO** `sigma_h` > `0.0135` → IC=-0.354 (n=39)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0135
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=77)

- **FILTRO** `sigma_h` < `0.0086` → IC=-0.275 (n=38)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0086
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=78)

- **FILTRO** `T_h` > `46.7258` → IC=-0.310 (n=77)

  - _Acción_: SKIP cuando `T_h` > 46.7258
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=39)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1236` → IC=+0.477 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1236 (IC base=+0.343)

- **PATRÓN** `sigma_h` < `0.0138` → IC=+0.359 (n=97)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0138 (IC base=+0.343)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.394 (n=64)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.343)

- **PATRÓN** `T_h` < `0.3604` → IC=+0.386 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3604 (IC base=+0.343)

- **PATRÓN** `T_h` > `0.7606` → IC=+0.379 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7606 (IC base=+0.343)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.479 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.343)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.359 (n=90)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.343)

- **PATRÓN** `edge` > `0.0992` → IC=+0.442 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.0992 (IC base=+0.416)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.440 (n=149)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.416)

- **PATRÓN** `T_h` < `0.5967` → IC=+0.436 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.5967 (IC base=+0.416)

- **PATRÓN** `T_h` > `1.484` → IC=+0.422 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.484 (IC base=+0.416)

- **PATRÓN** `dist_50` > `0.3772` → IC=+0.456 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3772 (IC base=+0.416)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.478 (n=136)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.416)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1831` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1831 (IC base=+0.186)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.186)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1023` → IC=+0.459 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.420)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.419 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.420)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.423 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.420)

- **PATRÓN** `T_h` < `0.9672` → IC=+0.458 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9672 (IC base=+0.420)

- **PATRÓN** `T_h` > `0.4508` → IC=+0.407 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4508 (IC base=+0.420)

- **PATRÓN** `dist_50` > `0.3792` → IC=+0.459 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3792 (IC base=+0.420)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.431 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.420)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.420)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.1838` → IC=+0.484 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1838 (IC base=+0.440)

- **PATRÓN** `sigma_h` < `0.0163` → IC=+0.468 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0163 (IC base=+0.440)

- **PATRÓN** `T_h` > `0.3968` → IC=+0.452 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.3968 (IC base=+0.440)

- **PATRÓN** `dist_50` > `0.354` → IC=+0.468 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.354 (IC base=+0.440)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.438 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.440)

- **PATRÓN** `edge` > `0.2005` → IC=+0.479 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2005 (IC base=+0.465)

- **PATRÓN** `sigma_h` < `0.0156` → IC=+0.479 (n=140)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0156 (IC base=+0.465)

- **PATRÓN** `T_h` > `1.4874` → IC=+0.480 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4874 (IC base=+0.465)

- **PATRÓN** `dist_50` > `0.4659` → IC=+0.492 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4659 (IC base=+0.465)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.472 (n=143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.465)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=308)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=382)

- **PATRÓN** `streak_estiramiento` < `0.8365` → IC=+0.120 (n=256)

  - _Acción_: Kelly boost +0.60€ cuando `streak_estiramiento` < 0.8365 (IC base=+0.045)

- **PATRÓN** `libro_liquidez` > `2526.423` → IC=+0.136 (n=138)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2526.423 (IC base=+0.045)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=27)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=16)

- **FILTRO** `libro_liquidez` < `2474.7486` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 2474.7486
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=16)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=27)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.000)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `streak_estiramiento` < `0.2566` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `streak_estiramiento` < 0.2566 (IC base=+0.012)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.136 (n=116)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 7.0 (IC base=+0.090)

- **PATRÓN** `streak_estiramiento` < `0.4496` → IC=+0.190 (n=98)

  - _Acción_: Kelly boost +0.95€ cuando `streak_estiramiento` < 0.4496 (IC base=+0.090)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.154 (n=108)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 35.0 (IC base=+0.090)

- **PATRÓN** `libro_liquidez` > `2225.9523` → IC=+0.141 (n=129)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2225.9523 (IC base=+0.090)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=93)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=46)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=31)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=748)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` < `11.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `volumen_racha` > `3677.1957` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `volumen_racha` > 3677.1957
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `libro_liquidez` < `3338.6704` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_liquidez` < 3338.6704
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `streak_estiramiento` > `1.1496` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `streak_estiramiento` > 1.1496
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=43)

### STREAK_FADE_60M#ETH#60min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `hora_utc` > `3.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **FILTRO** `streak_len` > `4.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `streak_len` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### STREAK_FADE_60M#SOL#60min
- **PATRÓN** `regimen_ma_toques` > `4.0` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.056)

- **PATRÓN** `volumen_racha` < `17126.646` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_racha` < 17126.646 (IC base=+0.056)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1006)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1330)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=1153)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=1204)

### STRUCT_NO_15M
- **FILTRO** `hora_utc` < `15.0` → IC=-0.250 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=22)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=4048)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.250 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=22)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=2240)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.198 (n=1222)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0047 (IC base=+0.177)

- **PATRÓN** `sigma_h` > `0.012` → IC=+0.197 (n=1222)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.012 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.1767` → IC=+0.192 (n=3227)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1767 (IC base=+0.177)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1911` → IC=+0.178 (n=1663)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.89€ cuando `delta_ratio_macro` |x|> 0.1911 (IC base=+0.177)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.133` → IC=+0.187 (n=1464)

  - _Acción_: Kelly boost +0.93€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.133 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.185 (n=3383)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 6.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.179 (n=3374)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.177)

- **PATRÓN** `ibs_15` > `0.5488` → IC=+0.253 (n=3664)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5488 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.1289` → IC=+0.170 (n=1755)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1289 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` < `0.3141` → IC=+0.163 (n=2902)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.3141 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.468` → IC=+0.258 (n=947)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.468 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `4653.0512` → IC=+0.194 (n=1222)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 4653.0512 (IC base=+0.177)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1456)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.251 (n=207)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.0585` → IC=+0.270 (n=207)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0585 (IC base=+0.220)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2526` → IC=+0.242 (n=207)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2526 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.239 (n=620)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.220)

- **PATRÓN** `ibs_15` > `0.7199` → IC=+0.285 (n=620)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7199 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `0.1378` → IC=+0.236 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1378 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.96` → IC=+0.306 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.96 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.221 (n=804)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `8753.6365` → IC=+0.233 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8753.6365 (IC base=+0.220)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.189 (n=242)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0035 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.0668` → IC=+0.155 (n=320)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0668 (IC base=+0.144)

- **PATRÓN** `drift_15min` |x|≤ `0.3955` → IC=+0.152 (n=242)

  - _Acción_: Kelly boost +0.76€ cuando `drift_15min` |x|≤ 0.3955 (IC base=+0.144)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1435` → IC=+0.148 (n=484)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio_macro` |x|> 0.1435 (IC base=+0.144)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1283` → IC=+0.157 (n=287)

  - _Acción_: Kelly boost +0.79€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1283 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.153 (n=664)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 6.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.149 (n=756)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 17.0 (IC base=+0.144)

- **PATRÓN** `ibs_15` > `0.5373` → IC=+0.240 (n=726)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5373 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1187` → IC=+0.159 (n=450)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1187 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.577` → IC=+0.266 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.577 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `3217.3698` → IC=+0.151 (n=726)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3217.3698 (IC base=+0.144)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `17.763` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.763
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=343)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.249 (n=281)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.18` → IC=+0.167 (n=160)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 17.18 (IC base=+0.095)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=464)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.095)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0239` → IC=+0.230 (n=279)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0239 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.1298` → IC=+0.225 (n=558)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1298 (IC base=+0.202)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3432` → IC=+0.228 (n=738)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3432 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.213 (n=748)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.202)

- **PATRÓN** `ibs_15` > `0.5328` → IC=+0.279 (n=836)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5328 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.1288` → IC=+0.209 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1288 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.825` → IC=+0.225 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.825 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2960.2036` → IC=+0.294 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2960.2036 (IC base=+0.202)

- **PATRÓN** `ibs_15` < `0.1096` → IC=+0.160 (n=780)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.80€ cuando `ibs_15` < 0.1096 (IC base=+0.067)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.393 (n=212)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1497` → IC=+0.382 (n=422)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1497 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1403` → IC=+0.385 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1403 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.378 (n=638)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.7872` → IC=+0.401 (n=634)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7872 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.1463` → IC=+0.383 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1463 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.239` → IC=+0.386 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.239 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.369 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `10317.9078` → IC=+0.386 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10317.9078 (IC base=+0.365)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.366 (n=290)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.364)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.402 (n=110)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.364)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.366 (n=110)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2147` → IC=+0.387 (n=149)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2147 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1371` → IC=+0.393 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1371 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.382 (n=329)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.8057` → IC=+0.391 (n=329)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8057 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.2485` → IC=+0.392 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2485 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.571` → IC=+0.379 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.571 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `16828.3206` → IC=+0.402 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16828.3206 (IC base=+0.364)

- **PATRÓN** `ballena_activa_n` < `493.0` → IC=+0.408 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 493.0 (IC base=+0.364)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.369 (n=135)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.365)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.387 (n=139)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.380 (n=273)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.298` → IC=+0.382 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.298 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.393 (n=147)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.365)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.373 (n=140)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.7479` → IC=+0.412 (n=306)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7479 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.4536` → IC=+0.382 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4536 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.889` → IC=+0.392 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.889 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.370 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `4001.8474` → IC=+0.394 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4001.8474 (IC base=+0.365)

- **PATRÓN** `ballena_activa_n` < `137.0` → IC=+0.368 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 137.0 (IC base=+0.365)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.176 (n=2186)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=2188)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.213 (n=1709)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=2665)

- **PATRÓN** `ibs_15` > `0.6326` → IC=+0.279 (n=1057)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6326 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` > `0.1113` → IC=+0.205 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1113 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` < `0.2672` → IC=+0.195 (n=902)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.2672 (IC base=-0.069)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2307` → IC=+0.269 (n=1212)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2307 (IC base=-0.013)

- **PATRÓN** `ibs_15` < `0.3605` → IC=+0.283 (n=3633)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3605 (IC base=-0.013)

- **PATRÓN** `dist_vwap_pct` > `0.6551` → IC=+0.274 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6551 (IC base=-0.013)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0341` → IC=-0.224 (n=1920)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0341
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=646)

- **FILTRO** `sigma_ewma_delta_pct` > `23.3` → IC=-0.271 (n=369)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.3
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=2197)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=66)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=2500)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.121 (n=763)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0052 (IC base=+0.095)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2081` → IC=+0.280 (n=157)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2081 (IC base=+0.095)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1079` → IC=+0.272 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1079 (IC base=+0.095)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.134 (n=375)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 15.0 (IC base=+0.095)

- **PATRÓN** `ibs_15` > `0.7572` → IC=+0.330 (n=345)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7572 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.1047` → IC=+0.283 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1047 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` < `0.2443` → IC=+0.277 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2443 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.545` → IC=+0.130 (n=382)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 8.545 (IC base=+0.095)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0659` → IC=+0.210 (n=60)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0659 (IC base=-0.195)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.159` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.159 (IC base=-0.195)

- **PATRÓN** `ibs_15` < `0.618` → IC=+0.290 (n=60)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.618 (IC base=-0.195)

- **PATRÓN** `dist_vwap_pct` < `0.0459` → IC=+0.284 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0459 (IC base=-0.195)

- **PATRÓN** `ballena_activa_n` < `291.0` → IC=+0.360 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 291.0 (IC base=-0.195)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=690)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.159 (n=467)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0058 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.154 (n=354)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0049 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0544` → IC=+0.187 (n=177)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0544 (IC base=+0.147)

- **PATRÓN** `drift_15min` |x|≤ `0.3996` → IC=+0.148 (n=177)

  - _Acción_: Kelly boost +0.74€ cuando `drift_15min` |x|≤ 0.3996 (IC base=+0.147)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3006` → IC=+0.190 (n=407)

  - _Acción_: Kelly boost +0.95€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3006 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.159 (n=534)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.147)

- **PATRÓN** `ibs_15` > `0.5959` → IC=+0.245 (n=531)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5959 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.4658` → IC=+0.164 (n=138)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.4658 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1598` → IC=+0.148 (n=418)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1598 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.387` → IC=+0.240 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.387 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=690)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `5241.237` → IC=+0.152 (n=354)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 5241.237 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.250 (n=1318)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.244)

- **PATRÓN** `drift_15min` |x|≤ `0.7694` → IC=+0.257 (n=1160)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7694 (IC base=+0.244)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2178` → IC=+0.262 (n=598)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2178 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.246 (n=936)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.248 (n=510)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.244)

- **PATRÓN** `ibs_15` < `0.3703` → IC=+0.275 (n=1318)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3703 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` > `0.6016` → IC=+0.259 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6016 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.434` → IC=+0.254 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.434 (IC base=+0.244)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0105` → IC=-0.245 (n=253)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=763)

- **FILTRO** `drift_60min` |x|> `0.173` → IC=-0.254 (n=343)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.173
  - _Potencial_: sin este filtro IC_bueno=-0.161 (n=673)

- **FILTRO** `drift_15min` |x|> `0.89` → IC=-0.284 (n=253)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.89
  - _Potencial_: sin este filtro IC_bueno=-0.161 (n=763)

- **FILTRO** `sigma_ewma_delta_pct` > `6.65` → IC=-0.203 (n=234)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.65
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=782)

- **FILTRO** `sigma_ewma_delta_pct` > `17.96` → IC=-0.149 (n=531)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.96
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4207)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.193)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.193)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.193)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.193)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0814` → IC=+0.236 (n=520)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0814 (IC base=-0.040)

- **PATRÓN** `ibs_15` < `0.3529` → IC=+0.292 (n=585)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3529 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` < `0.2615` → IC=+0.244 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2615 (IC base=-0.040)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0198` → IC=-0.253 (n=600)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0198
  - _Potencial_: sin este filtro IC_bueno=-0.164 (n=602)

- **FILTRO** `drift_15min` |x|> `1.2406` → IC=-0.267 (n=299)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2406
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=903)

- **FILTRO** `sigma_ewma_delta_pct` > `7.41` → IC=-0.211 (n=375)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.41
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=827)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.208)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.208)

- **PATRÓN** `delta_ratio_macro` |x|> `0.069` → IC=+0.274 (n=777)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.069 (IC base=-0.026)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.116` → IC=+0.295 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.116 (IC base=-0.026)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.293 (n=872)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` > `0.7702` → IC=+0.354 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7702 (IC base=-0.026)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.222 (n=16)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.080)

- **PATRÓN** `drift_15min` |x|≤ `0.3927` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3927 (IC base=+0.080)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2386` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2386 (IC base=+0.080)

- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` < `0.1207` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.1207 (IC base=+0.080)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.222 (n=16)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.080)

- **PATRÓN** `drift_15min` |x|≤ `0.3927` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3927 (IC base=+0.080)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2386` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2386 (IC base=+0.080)

- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` < `0.1207` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.1207 (IC base=+0.080)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.297 (n=956)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.0531` → IC=+0.321 (n=362)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0531 (IC base=+0.292)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2427` → IC=+0.308 (n=362)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2427 (IC base=+0.292)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2243` → IC=+0.304 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2243 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.308 (n=1131)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.292)

- **PATRÓN** `ibs_15` > `0.8389` → IC=+0.320 (n=1086)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8389 (IC base=+0.292)

- **PATRÓN** `dist_vwap_pct` > `0.2698` → IC=+0.323 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2698 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.513` → IC=+0.381 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.513 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `12307.7364` → IC=+0.314 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12307.7364 (IC base=+0.292)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.311 (n=257)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.289)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.301 (n=264)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.317 (n=195)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.26` → IC=+0.311 (n=194)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.26 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.307 (n=583)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.83` → IC=+0.315 (n=582)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.83 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.2552` → IC=+0.326 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2552 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.386 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `16196.8854` → IC=+0.332 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16196.8854 (IC base=+0.289)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.304 (n=504)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.0515` → IC=+0.318 (n=168)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0515 (IC base=+0.295)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1464` → IC=+0.299 (n=336)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1464 (IC base=+0.295)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2166` → IC=+0.316 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2166 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.316 (n=486)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.295)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.297 (n=457)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.295)

- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.322 (n=504)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` > `0.2815` → IC=+0.323 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2815 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.513` → IC=+0.367 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.513 (IC base=+0.295)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2656` → IC=-0.140 (n=84)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2656
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=255)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1226` → IC=-0.151 (n=84)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1226
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=255)

- **FILTRO** `ballena_activa_n` > `44.0` → IC=-0.136 (n=229)

  - _Acción_: SKIP cuando `ballena_activa_n` > 44.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=78)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1228` → IC=-0.214 (n=117)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1228
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=362)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.186 (n=119)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=360)

- **FILTRO** `drift_15min` |x|> `0.4407` → IC=-0.152 (n=162)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.4407
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=317)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1334` → IC=-0.147 (n=49)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1334
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=149)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.2412` → IC=-0.128 (n=92)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.2412
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=94)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.0539` → IC=-0.175 (n=38)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0539
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

- **FILTRO** `drift_15min` |x|> `0.3423` → IC=-0.289 (n=17)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3423
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=34)

### UPDOWN_OU_5M#DOGE#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1055` → IC=-0.289 (n=17)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1055
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `sigma_h` > `0.0068` → IC=-0.262 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

- **FILTRO** `drift_60min` |x|> `0.0858` → IC=-0.200 (n=18)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.0858
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `drift_15min` |x|> `0.3434` → IC=-0.184 (n=17)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3434
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2236` → IC=-0.237 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2236
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### UPDOWN_OU_5M#ETH#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1254` → IC=-0.200 (n=18)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1254
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=38)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.3147` → IC=-0.385 (n=24)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.3147
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0611` → IC=-0.259 (n=27)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0611
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.237 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=37)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0905` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0905
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### UPDOWN_OU_5M#XRP#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0898` → IC=-0.227 (n=20)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0898
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **FILTRO** `sigma_h` > `0.0058` → IC=-0.250 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0058
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `87.7391` → IC=+0.190 (n=485)

  - _Acción_: Kelly boost +0.95€ cuando `T_h` > 87.7391 (IC base=+0.188)

- **PATRÓN** `ratio` < `0.973` → IC=+0.407 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.188)

- **PATRÓN** `T_h` > `114.6853` → IC=+0.353 (n=2203)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 114.6853 (IC base=+0.336)

- **PATRÓN** `ratio` > `1.0229` → IC=+0.376 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0229 (IC base=+0.336)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `109.5528` → IC=+0.173 (n=200)

  - _Acción_: Kelly boost +0.87€ cuando `T_h` > 109.5528 (IC base=+0.157)

- **PATRÓN** `ratio` < `0.983` → IC=+0.330 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.983 (IC base=+0.157)

- **PATRÓN** `T_h` > `111.9558` → IC=+0.304 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9558 (IC base=+0.293)

- **PATRÓN** `ratio` > `1.0455` → IC=+0.405 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0455 (IC base=+0.293)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `83.3501` → IC=+0.232 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.228)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.398 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.228)

- **PATRÓN** `T_h` > `111.9882` → IC=+0.353 (n=796)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9882 (IC base=+0.325)

- **PATRÓN** `ratio` > `1.0093` → IC=+0.338 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0093 (IC base=+0.325)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1003` → IC=+0.445 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1003 (IC base=+0.399)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5488 sube el IC de +0.177 a +0.253 en UPDOWN_GBM#15min (n=3664). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7199 sube el IC de +0.220 a +0.285 en UPDOWN_GBM#BTC#15min (n=620). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5373 sube el IC de +0.144 a +0.240 en UPDOWN_GBM#ETH#15min (n=726). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de +0.095 a +0.249 en UPDOWN_GBM#SOL#15min (n=281). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5328 sube el IC de +0.202 a +0.279 en UPDOWN_GBM#XRP#15min (n=836). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1096 sube el IC de +0.067 a +0.160 en UPDOWN_GBM#XRP#15min (n=780). Ya aplicado como kelly_boost=+0.80€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6326 sube el IC de -0.069 a +0.279 en UPDOWN_GBM_15M_TARDIO (n=1057). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3605 sube el IC de -0.013 a +0.283 en UPDOWN_GBM_15M_TARDIO (n=3633). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7572 sube el IC de +0.095 a +0.330 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=345). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.618 sube el IC de -0.195 a +0.290 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=60). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5959 sube el IC de +0.147 a +0.245 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=531). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3703 sube el IC de +0.244 a +0.275 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1318). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.193 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3529 sube el IC de -0.040 a +0.292 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=585). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.208 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.026 a +0.293 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=872). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.080 a +0.342 en UPDOWN_GBM_ETH_15M_HORA7 (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.080 a +0.342 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8389 sube el IC de +0.292 a +0.320 en UPDOWN_GBM_IBS_ALTO (n=1086). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.83 sube el IC de +0.289 a +0.315 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=582). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.295 a +0.322 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=504). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7872 sube el IC de +0.365 a +0.401 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=634). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8057 sube el IC de +0.364 a +0.391 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=329). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7479 sube el IC de +0.365 a +0.412 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=306). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1938 | +0.090 | +213.85€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1938 | +0.090 | +213.85€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1546 | +0.094 | +185.12€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1546 | +0.094 | +185.12€ | 0 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 284 | +0.070 | +11.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 284 | +0.070 | +11.30€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 77 | +0.108 | +17.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 77 | +0.108 | +17.77€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 685 | -0.002 | +76.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 685 | -0.002 | +76.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 5 | +0.018 | +2.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 5 | +0.018 | +2.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 499 | -0.031 | +42.26€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 499 | -0.031 | +42.26€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 145 | +0.085 | +26.26€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 145 | +0.085 | +26.26€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 40525 | -0.080 | -5008.83€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2249 | +0.034 | -264.90€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 38276 | -0.087 | -4743.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4515 | -0.114 | -773.92€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4515 | -0.114 | -773.92€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2249 | +0.034 | -264.90€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2249 | +0.034 | -264.90€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4341 | -0.105 | -873.70€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4341 | -0.105 | -873.70€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 10802 | -0.020 | -998.03€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 10802 | -0.020 | -998.03€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 10705 | -0.103 | -790.70€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 10705 | -0.103 | -790.70€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 7913 | -0.132 | -1307.57€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 7913 | -0.132 | -1307.57€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 35679 | -0.015 | +3314.17€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 9234 | +0.004 | +1663.11€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 26445 | -0.022 | +1651.06€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 35679 | -0.015 | +3314.17€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 9234 | +0.004 | +1663.11€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 26445 | -0.022 | +1651.06€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 1486 | -0.102 | -190.28€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 176 | -0.045 | -19.67€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 1310 | -0.110 | -170.61€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 788 | -0.089 | -95.94€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 152 | -0.039 | -14.45€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 636 | -0.100 | -81.50€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 491 | -0.125 | -74.32€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 24 | -0.077 | -5.22€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#5min | 467 | -0.127 | -69.10€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 66 | -0.191 | -10.49€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 66 | -0.191 | -10.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 147148 | +0.116 | -5836.09€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 18786 | +0.182 | -580.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 647 | -0.015 | -68.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 118923 | +0.107 | -4880.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 8792 | +0.100 | -307.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 19718 | +0.108 | -1191.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 61 | -0.151 | +10.95€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 19642 | +0.110 | -1190.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 28457 | +0.128 | -413.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5216 | +0.187 | -182.34€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 19703 | +0.121 | -102.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3496 | +0.082 | -106.26€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 19774 | +0.100 | -1353.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 75 | -0.123 | -6.95€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 19684 | +0.101 | -1335.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 31301 | +0.125 | -570.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 8092 | +0.177 | -156.41€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 19973 | +0.107 | -352.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3224 | +0.100 | -52.86€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 28159 | +0.115 | -1380.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5273 | +0.197 | -249.91€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 550 | +0.018 | -14.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 20264 | +0.095 | -968.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2072 | +0.129 | -148.37€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#XRP | 19739 | +0.106 | -926.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 69 | -0.091 | +4.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 19657 | +0.107 | -930.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 23698 | +0.197 | -1413.53€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 23698 | +0.197 | -1413.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 5389 | +0.180 | -450.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 5389 | +0.180 | -450.57€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 3033 | +0.203 | -68.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 3033 | +0.203 | -68.71€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 5328 | +0.181 | -418.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 5328 | +0.181 | -418.97€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4618 | +0.248 | -154.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4618 | +0.248 | -154.67€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 5251 | +0.189 | -334.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 5251 | +0.189 | -334.36€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1029 | +0.426 | -36.01€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1029 | +0.426 | -36.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 405 | +0.434 | -7.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 405 | +0.434 | -7.98€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 407 | +0.431 | -8.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 407 | +0.431 | -8.91€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 203 | +0.402 | -15.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 203 | +0.402 | -15.25€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 82847 | +0.202 | -5853.73€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 82847 | +0.202 | -5853.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 14231 | +0.186 | -1449.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 14231 | +0.186 | -1449.66€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 13377 | +0.225 | -453.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 13377 | +0.225 | -453.16€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 14187 | +0.182 | -1467.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 14187 | +0.182 | -1467.93€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 13457 | +0.221 | -490.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 13457 | +0.221 | -490.02€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 13749 | +0.202 | -897.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 13749 | +0.202 | -897.72€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 13846 | +0.197 | -1095.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 13846 | +0.197 | -1095.24€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 31705 | +0.116 | +177.01€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 31705 | +0.116 | +177.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 15762 | +0.119 | +160.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 15762 | +0.119 | +160.18€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 15943 | +0.114 | +16.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 15943 | +0.114 | +16.83€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2101 | +0.293 | -7.33€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2101 | +0.293 | -7.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 963 | +0.279 | -27.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 963 | +0.279 | -27.20€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1018 | +0.297 | +13.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1018 | +0.297 | +13.76€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 120 | +0.352 | +6.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 120 | +0.352 | +6.11€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 968 | +0.441 | +3.54€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 968 | +0.441 | +3.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 472 | +0.435 | -5.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 472 | +0.435 | -5.80€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 450 | +0.449 | +8.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 450 | +0.449 | +8.79€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1666 | +0.072 | -64.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 643 | +0.052 | -51.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1023 | +0.084 | -12.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 74 | +0.118 | +4.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 74 | +0.118 | +4.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1280 | +0.080 | -26.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 257 | +0.060 | -14.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1023 | +0.084 | -12.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 312 | +0.029 | -42.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 312 | +0.029 | -42.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 62722 | +0.101 | -1596.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 5071 | +0.090 | +44.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 57651 | +0.101 | -1640.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 34495 | +0.105 | -397.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 5071 | +0.090 | +44.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 29424 | +0.108 | -441.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 12914 | +0.108 | -83.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 12914 | +0.108 | -83.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 15313 | +0.083 | -1116.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 15313 | +0.083 | -1116.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 897 | +0.193 | -109.11€ | 4 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 897 | +0.193 | -109.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 897 | +0.193 | -109.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 897 | +0.193 | -109.11€ | 4 | 4 |
| ✅ GBM_LATE_15M | 43086 | +0.095 | +22578.40€ | 0 | 17 |
| ✅ GBM_LATE_15M#15min | 43086 | +0.095 | +22578.40€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 7176 | +0.217 | +5928.84€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 7176 | +0.217 | +5928.84€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 6468 | +0.179 | +4959.05€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 6468 | +0.179 | +4959.05€ | 0 | 21 |
| ✅ GBM_LATE_15M#DOGE | 7706 | +0.205 | +6001.98€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 7706 | +0.205 | +6001.98€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 6000 | +0.043 | +1707.15€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 6000 | +0.043 | +1707.15€ | 1 | 20 |
| ✅ GBM_LATE_15M#SOL | 6064 | -0.032 | +1274.78€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 6064 | -0.032 | +1274.78€ | 4 | 15 |
| ✅ GBM_LATE_15M#XRP | 9672 | -0.030 | +2706.60€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 9672 | -0.030 | +2706.60€ | 4 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 46300 | +0.085 | +25284.33€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 46300 | +0.085 | +25284.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 8951 | +0.003 | +4565.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 8951 | +0.003 | +4565.28€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 9820 | +0.009 | +2344.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 9820 | +0.009 | +2344.42€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 6417 | +0.279 | +6907.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 6417 | +0.279 | +6907.80€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 8372 | +0.013 | +2087.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 8372 | +0.013 | +2087.39€ | 1 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 7362 | +0.039 | +3042.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 7362 | +0.039 | +3042.18€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5378 | +0.304 | +6337.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5378 | +0.304 | +6337.25€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 34129 | +0.180 | +27694.67€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 34129 | +0.180 | +27694.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 5178 | +0.230 | +4616.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 5178 | +0.230 | +4616.05€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 5376 | +0.148 | +3971.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 5376 | +0.148 | +3971.31€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 5472 | +0.224 | +4714.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 5472 | +0.224 | +4714.62€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 5787 | +0.139 | +4427.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 5787 | +0.139 | +4427.52€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 6412 | +0.125 | +4787.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 6412 | +0.125 | +4787.73€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 5904 | +0.226 | +5177.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 5904 | +0.226 | +5177.45€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 9285 | +0.134 | +4540.61€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 9285 | +0.134 | +4540.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2721 | +0.144 | +1552.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2721 | +0.144 | +1552.02€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 467 | +0.150 | +239.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 467 | +0.150 | +239.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2751 | +0.138 | +1317.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2751 | +0.138 | +1317.81€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2314 | +0.109 | +897.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2314 | +0.109 | +897.24€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 627 | +0.133 | +281.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 627 | +0.133 | +281.63€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 43251 | +0.185 | +34662.79€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#15min | 43251 | +0.185 | +34662.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 6848 | +0.242 | +6402.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 6848 | +0.242 | +6402.00€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 6744 | +0.147 | +4627.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 6744 | +0.147 | +4627.23€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 7320 | +0.233 | +6542.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 7320 | +0.233 | +6542.89€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 7139 | +0.139 | +5100.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 7139 | +0.139 | +5100.85€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 7650 | +0.121 | +5279.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 7650 | +0.121 | +5279.36€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 7550 | +0.231 | +6710.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 7550 | +0.231 | +6710.46€ | 0 | 19 |
| ✅ GBM_LATE_5M | 11891 | +0.203 | +9316.41€ | 1 | 30 |
| ✅ GBM_LATE_5M#5min | 11891 | +0.203 | +9316.41€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 984 | +0.242 | +916.10€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 984 | +0.242 | +916.10€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2780 | +0.208 | +2390.04€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2780 | +0.208 | +2390.04€ | 0 | 26 |
| ✅ GBM_LATE_5M#DOGE | 1131 | +0.196 | +834.22€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1131 | +0.196 | +834.22€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 3342 | +0.193 | +2355.71€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3342 | +0.193 | +2355.71€ | 0 | 28 |
| ✅ GBM_LATE_5M#SOL | 1756 | +0.193 | +1347.78€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1756 | +0.193 | +1347.78€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1898 | +0.207 | +1472.55€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1898 | +0.207 | +1472.55€ | 0 | 0 |
| ✅ GBM_LATE_60M | 3551 | +0.066 | +1150.40€ | 0 | 8 |
| ✅ GBM_LATE_60M#60min | 3551 | +0.066 | +1150.40€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1306 | +0.083 | +478.99€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1306 | +0.083 | +478.99€ | 0 | 6 |
| ✅ GBM_LATE_60M#ETH | 1149 | +0.066 | +381.61€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1149 | +0.066 | +381.61€ | 0 | 9 |
| ✅ GBM_LATE_60M#SOL | 1096 | +0.045 | +289.80€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1096 | +0.045 | +289.80€ | 1 | 13 |
| 🚫 GBM_LATE_60M_FADE | 581 | -0.243 | -20.35€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 581 | -0.243 | -20.35€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 216 | -0.248 | -13.87€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 216 | -0.248 | -13.87€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 206 | -0.226 | -0.46€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 206 | -0.226 | -0.46€ | 6 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 159 | -0.252 | -6.01€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 159 | -0.252 | -6.01€ | 7 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1541 | +0.085 | +399.12€ | 0 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1541 | +0.085 | +399.12€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 608 | +0.082 | +150.90€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 608 | +0.082 | +150.90€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 550 | +0.056 | +85.29€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 550 | +0.056 | +85.29€ | 2 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 383 | +0.129 | +162.94€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 383 | +0.129 | +162.94€ | 3 | 9 |
| ✅ LATE_WINDOW_5MIN | 167 | +0.281 | +166.63€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 167 | +0.281 | +166.63€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 167 | +0.281 | +166.63€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 167 | +0.281 | +166.63€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3439 | +0.102 | +855.23€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3439 | +0.102 | +855.23€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3439 | +0.102 | +855.23€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3439 | +0.102 | +855.23€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 546 | -0.042 | -18.62€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 546 | -0.042 | -18.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 154 | -0.013 | +2.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 154 | -0.013 | +2.68€ | 2 | 1 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 106 | -0.028 | -2.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 106 | -0.028 | -2.54€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 205 | -0.012 | -1.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 205 | -0.012 | -1.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 3763 | +0.016 | +87.19€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3763 | +0.016 | +87.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 183 | +0.024 | -1.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 183 | +0.024 | -1.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 795 | +0.008 | +29.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 795 | +0.008 | +29.93€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE | 207 | -0.012 | -4.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 207 | -0.012 | -4.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1368 | +0.025 | +31.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1368 | +0.025 | +31.97€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 758 | +0.012 | +2.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 758 | +0.012 | +2.16€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 452 | +0.018 | +29.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 452 | +0.018 | +29.11€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1777 | -0.041 | -30.06€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1777 | -0.041 | -30.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 514 | -0.031 | -12.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 514 | -0.031 | -12.15€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 608 | -0.016 | +5.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 608 | -0.016 | +5.29€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 655 | -0.071 | -23.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 655 | -0.071 | -23.20€ | 6 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 8984 | -0.027 | +21.17€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 4270 | -0.036 | -77.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 4714 | -0.018 | +98.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 268 | -0.041 | -11.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 136 | -0.022 | -0.57€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 132 | -0.060 | -10.61€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 2237 | -0.020 | +12.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1069 | -0.027 | -8.08€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1168 | -0.015 | +20.82€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 977 | -0.024 | +13.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 489 | -0.042 | -12.15€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 488 | -0.006 | +26.07€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 1974 | -0.039 | -50.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 919 | -0.052 | -53.50€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1055 | -0.028 | +3.35€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1765 | -0.015 | +51.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 844 | -0.027 | +4.33€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 921 | -0.004 | +46.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1763 | -0.031 | +4.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 813 | -0.039 | -7.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 950 | -0.025 | +12.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 14662 | -0.012 | -218.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14662 | -0.012 | -218.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 3379 | -0.021 | -71.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 3379 | -0.021 | -71.38€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 50641 | -0.000 | +2561.37€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 50641 | -0.000 | +2561.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 9132 | +0.026 | +1176.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 9132 | +0.026 | +1176.24€ | 2 | 5 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 7283 | -0.034 | -95.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 7283 | -0.034 | -95.15€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 9239 | +0.025 | +971.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 9239 | +0.025 | +971.66€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 7128 | -0.047 | -137.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 7128 | -0.047 | -137.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 8565 | -0.004 | +230.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 8565 | -0.004 | +230.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 9294 | +0.015 | +415.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 9294 | +0.015 | +415.60€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6667 | -0.059 | -161.62€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6667 | -0.059 | -161.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1743 | -0.078 | -44.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1743 | -0.078 | -44.35€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 55 | -0.061 | -2.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 55 | -0.061 | -2.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 775 | -0.120 | -33.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 775 | -0.120 | -33.97€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2012 | -0.073 | -39.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2012 | -0.073 | -39.60€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 857 | -0.016 | -25.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 857 | -0.016 | -25.51€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3367 | +0.004 | -1.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3367 | +0.004 | -1.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 131 | -0.034 | -0.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 131 | -0.034 | -0.72€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 192 | +0.015 | +1.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 192 | +0.015 | +1.02€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1325 | +0.006 | +6.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1325 | +0.006 | +6.88€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1390 | +0.007 | +0.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1390 | +0.007 | +0.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 190 | -0.010 | -6.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 190 | -0.010 | -6.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 125438 | -0.077 | +1572.19€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 125438 | -0.077 | +1572.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 21828 | -0.077 | +1059.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 21828 | -0.077 | +1059.68€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 18895 | -0.101 | -1038.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 18895 | -0.101 | -1038.01€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 22115 | -0.068 | +1195.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 22115 | -0.068 | +1195.74€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 18440 | -0.097 | -630.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 18440 | -0.097 | -630.32€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 22449 | -0.057 | +304.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 22449 | -0.057 | +304.83€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 21711 | -0.067 | +680.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 21711 | -0.067 | +680.27€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8778 | -0.034 | -184.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8778 | -0.034 | -184.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1001 | -0.017 | -18.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1001 | -0.017 | -18.91€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1989 | -0.046 | -25.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1989 | -0.046 | -25.73€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2602 | -0.026 | -42.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2602 | -0.026 | -42.21€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1207 | -0.056 | -28.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1207 | -0.056 | -28.63€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 971 | -0.031 | -35.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 971 | -0.031 | -35.95€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1694 | +0.124 | +692.51€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 1558 | +0.130 | +679.92€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 363 | +0.136 | +179.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 363 | +0.136 | +179.62€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 321 | +0.119 | +112.97€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 321 | +0.119 | +112.97€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#ETH | 309 | +0.137 | +150.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 309 | +0.137 | +150.62€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 275 | +0.150 | +149.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 275 | +0.150 | +149.73€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 290 | +0.103 | +86.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 290 | +0.103 | +86.98€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1485 | -0.017 | -23.90€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1485 | -0.017 | -23.90€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 292 | -0.003 | +8.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 292 | -0.003 | +8.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 258 | -0.023 | -4.74€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 258 | -0.023 | -4.74€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 384 | -0.047 | -32.39€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 384 | -0.047 | -32.39€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 313 | +0.008 | +3.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 313 | +0.008 | +3.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 238 | -0.008 | +1.65€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 238 | -0.008 | +1.65€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 909 | -0.071 | -44.18€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 424 | -0.110 | -78.04€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 328 | -0.139 | -65.45€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 96 | -0.010 | -12.59€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 320 | -0.028 | +26.27€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 229 | -0.015 | +28.74€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 91 | -0.059 | -2.46€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 165 | -0.051 | +7.59€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 134 | -0.059 | +3.20€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 31 | -0.015 | +4.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 691 | -0.083 | -33.51€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 218 | -0.032 | -10.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1136 | -0.207 | -71.10€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 442 | -0.209 | -42.91€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 385 | -0.213 | -42.68€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 57 | -0.178 | -0.23€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 388 | -0.210 | -34.11€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 340 | -0.222 | -41.12€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 48 | -0.120 | +7.01€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 306 | -0.198 | +5.93€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 285 | -0.193 | +3.81€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 21 | -0.239 | +2.12€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1010 | -0.211 | -80.00€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 126 | -0.172 | +8.90€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 459 | +0.396 | +437.07€ | 0 | 13 |
| ✅ RESOLUTION_SNIPER#BTC | 69 | +0.162 | +55.45€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 69 | +0.162 | +55.45€ | 0 | 2 |
| ✅ RESOLUTION_SNIPER#ETH | 110 | +0.366 | +102.82€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 110 | +0.366 | +102.82€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 280 | +0.461 | +278.80€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 280 | +0.461 | +278.80€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 459 | +0.396 | +437.07€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 728 | +0.032 | +41.15€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 728 | +0.032 | +41.15€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 303 | +0.025 | +3.85€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 303 | +0.025 | +3.85€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 60 | -0.016 | -2.15€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 60 | -0.016 | -2.15€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 73 | -0.007 | +0.78€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 73 | -0.007 | +0.78€ | 3 | 1 |
| ✅ STREAK_FADE_15M#XRP | 292 | +0.058 | +38.68€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 292 | +0.058 | +38.68€ | 0 | 5 |
| ✅ STREAK_FADE_5M | 3442 | -0.021 | -133.79€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3442 | -0.021 | -133.79€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1059 | -0.020 | -35.48€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1059 | -0.020 | -35.48€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 590 | -0.027 | -26.08€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 590 | -0.027 | -26.08€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 165 | -0.039 | -13.80€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 165 | -0.039 | -13.80€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1628 | -0.018 | -58.44€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1628 | -0.018 | -58.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 103 | -0.052 | -9.27€ | 5 | 0 |
| ✅ STREAK_FADE_60M#60min | 103 | -0.052 | -9.27€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 43 | -0.100 | -5.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 43 | -0.100 | -5.07€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 60 | -0.016 | -4.20€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 60 | -0.016 | -4.20€ | 0 | 2 |
| ✅ STREAK_MOM_5M | 10952 | +0.016 | +86.77€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 10952 | +0.016 | +86.77€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2805 | +0.021 | +29.16€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2805 | +0.021 | +29.16€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2860 | +0.018 | +35.53€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2860 | +0.018 | +35.53€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2888 | +0.009 | -0.95€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2888 | +0.009 | -0.95€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2399 | +0.016 | +23.03€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2399 | +0.016 | +23.03€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 9957 | +0.013 | -49.07€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 9957 | +0.013 | -49.07€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4067 | +0.017 | -9.31€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4067 | +0.017 | -9.31€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3616 | +0.011 | -27.14€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3616 | +0.011 | -27.14€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2274 | +0.010 | -12.63€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2274 | +0.010 | -12.63€ | 1 | 0 |
| ✅ UPDOWN_GBM | 77874 | +0.054 | +6895.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 19352 | +0.083 | +4232.65€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 2490 | +0.004 | +22.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 51145 | +0.050 | +2546.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 4616 | +0.007 | +93.57€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6851 | +0.089 | +1075.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1576 | +0.156 | +698.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5198 | +0.070 | +378.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 16861 | +0.055 | +1451.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2519 | +0.089 | +617.92€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 672 | +0.009 | +9.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 11521 | +0.061 | +756.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2051 | +0.004 | +63.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 98 | -0.070 | +3.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8529 | +0.070 | +911.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1555 | +0.147 | +610.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6896 | +0.054 | +302.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 17946 | +0.044 | +1163.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 4591 | +0.065 | +669.86€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 654 | +0.006 | +15.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 10993 | +0.044 | +455.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1617 | +0.011 | +20.06€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 91 | -0.102 | +2.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 17120 | +0.032 | +838.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 4881 | +0.034 | +396.90€ | 0 | 3 |
| ✅ UPDOWN_GBM#SOL#240min | 621 | -0.009 | -0.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 10590 | +0.037 | +436.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 948 | +0.006 | +10.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 80 | -0.134 | -5.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 10565 | +0.065 | +1456.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4230 | +0.102 | +1238.93€ | 0 | 9 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 5947 | +0.041 | +217.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 269 | -0.102 | +1.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 845 | +0.365 | +312.55€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 845 | +0.365 | +312.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 438 | +0.364 | +152.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 438 | +0.364 | +152.73€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 407 | +0.365 | +159.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 407 | +0.365 | +159.82€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 20089 | -0.026 | +4657.67€ | 2 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 20089 | -0.026 | +4657.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3583 | -0.113 | +129.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3583 | -0.113 | +129.40€ | 3 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2464 | +0.216 | +1597.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2464 | +0.216 | +1597.97€ | 1 | 20 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5754 | -0.067 | +669.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5754 | -0.067 | +669.46€ | 5 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5622 | -0.065 | +987.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5622 | -0.065 | +987.58€ | 3 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 236 | +0.050 | +14.42€ | 0 | 5 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 236 | +0.050 | +14.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 236 | +0.050 | +14.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 236 | +0.050 | +14.42€ | 0 | 5 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1447 | +0.292 | +1245.56€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1447 | +0.292 | +1245.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 776 | +0.289 | +631.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 776 | +0.289 | +631.33€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 671 | +0.295 | +614.23€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 671 | +0.295 | +614.23€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 818 | -0.113 | -84.69€ | 6 | 0 |
| ✅ UPDOWN_OU_5M#5min | 818 | -0.113 | -84.69€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 249 | -0.082 | -18.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 249 | -0.082 | -18.61€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 88 | -0.167 | -9.66€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 88 | -0.167 | -9.66€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 98 | -0.190 | -7.06€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 98 | -0.190 | -7.06€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 3650 | +0.303 | +1718.05€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1344 | +0.256 | +168.08€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1403 | +0.299 | +626.40€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 903 | +0.380 | +923.57€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.042) — sin ventaja clara. oversold(IBS<0.3): IC=+0.064 n=27026 | neutral: IC=+0.057 n=28796 | overbought(IBS>0.7): IC=+0.099 n=27473
  - _Datos_: n=86583 IC=+0.074 PNL=+12875.37€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 718 celda(s) pasan gate riguroso completo de 2704 evaluadas (n>=40) y 3755 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.034 < 0.08 — monitorear
  - _Datos_: n=4881 IC=+0.034 PNL=+396.90€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1403/15 IC=+0.299 PNL=+626.40€ | BTC: n=1344/15 IC=+0.256 PNL=+168.08€ | SOL: n=903/15 IC=+0.380 PNL=+923.57€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 31 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
  - _Bloqueante_: N_INSUFICIENTE


### ⏳ Acumulando datos

**⏳ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: 15
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: Falta 11 ops más en GBM@18h (IC actual=-0.067)
  - _Datos_: n=4 IC=-0.067 PNL=-3.02€

**⏳ H-HORA-GBM** — hora_utc causal automático en GBM (forward)
  - _Umbral_: n≥20 forward con hora_utc + alguna hora con n≥15 IC<-0.10 o >+0.10
  - _Acción_: El sistema lo aplica automáticamente vía FEATURE_RULES. Verificar en strategy_params.json.
  - _Estado_: 77812 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.139 n=790/60 | contraria IC=+0.192 n=822 | gap=-0.053 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=469, boost estimado=+0.017. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 275 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1617/40 IC=+0.011 PNL=+20.06€ | BTC#60min: n=2051/40 IC=+0.004 PNL=+63.49€ | SOL#60min: n=948/40 IC=+0.006 PNL=+10.01€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.048 n=564038 | tras_1loss IC=+0.096 n=428450 | tras_2loss IC=+0.065 n=173209/40 | gap=-0.017 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.036 n=10982 | contrario_BTC IC=+0.052 n=9653/40 | gap=+0.017 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


### 🔒 Bloqueadas (requieren dataset/API)

**🔒 H-OBI** — Orderbook Imbalance como señal
  - _Umbral_: Dataset Jon-Becker + API CLOB con orderbook histórico
  - _Acción_: Implementar s_obi en shadow_predict.py usando L2 orderbook
  - _Estado_: Descargar github.com/Jon-Becker/prediction-market-analysis (36GB). Analizar spread bid/ask e imbalance por mercado en 60min previos a resolución.
  - _Bloqueante_: JON_BECKER_DATASET

**🔒 H-OU-THETA** — Calibrar theta OU con datos históricos
  - _Umbral_: Dataset Jon-Becker con series de precios históricos suficientes
  - _Acción_: Ajustar THETA_OU por par en strategy_params.json (BTC/ETH/SOL independientes)
  - _Estado_: Descargar github.com/Jon-Becker/prediction-market-analysis (36GB). Fit OU sobre series históricas por par y estimar theta por MLE.
  - _Bloqueante_: JON_BECKER_DATASET

**🔒 H-HMM-REGIME** — HMM para régimen de mercado
  - _Umbral_: n≥200 ops GBM forward con hora_utc/ibs_15, o dataset Jon-Becker
  - _Acción_: Implementar hmmlearn sobre features GBM; condicionar estrategia al régimen detectado
  - _Estado_: Descargar github.com/Jon-Becker/prediction-market-analysis (36GB). Entrenar HMM 3-estado sobre (drift_60min, sigma_h) histórico. Validar en forward.
  - _Bloqueante_: JON_BECKER_DATASET

**🔒 H-CROSS-ARB** — Arbitraje Polymarket vs Kalshi
  - _Umbral_: API Kalshi activa + credenciales Polymarket live
  - _Acción_: Extender arb_scanner.py con endpoints Kalshi; comparar mismo evento cross-plataforma
  - _Estado_: Requiere acceso API Kalshi + credenciales Polymarket live
  - _Bloqueante_: API_KALSHI


### 🧪 Hipótesis custom (editables en hipotesis_custom.json)

**🟡 H-24H-GBM-BUYYES-MADRUGADA** — GBM BUY_YES en madrugada europea (05-07h UTC) — señal alcista
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona en horas 05-07h UTC (7-9h Madrid). IC=+0.087 n=14 a las 06h, +0.063 n=11 a las 05h, +0.067 n=17 a las 07h. Hipótesis: apertura europea genera momentum alcista que el GBM captura. La dirección dominante cambia de BUY_NO (madrugada americana 13h) a BUY_YES (apertura europea). Objetivo: cubrir franja horaria 05-07h UTC en el camino hacia operación 24h.
  - _Umbral_: n≥40 en franja 05-07h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → añadir GBM BUY_YES a subtypes_permitidos_live para horas 05-07h UTC
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.199 > 0.08 con n=769 PNL=+576.80€
  - _Datos_: n=769 IC=+0.199 PNL=+576.80€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.171 > 0.08 con n=848 PNL=+488.56€
  - _Datos_: n=848 IC=+0.171 PNL=+488.56€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.172 > 0.08 con n=62 PNL=+33.07€
  - _Datos_: n=62 IC=+0.172 PNL=+33.07€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.333 > 0.1 con n=2981 PNL=+1648.11€
  - _Datos_: n=2981 IC=+0.333 PNL=+1648.11€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=701 IC=+0.073 PNL=+80.55€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=701 IC=+0.073 PNL=+80.55€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=85 IC=+0.190 PNL=+58.97€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=85 IC=+0.190 PNL=+58.97€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=73866 IC=+0.053 PNL=+6601.12€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=73866 IC=+0.053 PNL=+6601.12€

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 5/15 ops en el filtro definido (IC actual=+0.054 PNL=+5.10€)
  - _Datos_: n=5 IC=+0.054 PNL=+5.10€

**⏳ H-CUSTOM-OF-07H-BTCSOL** — ORDER_FLOW H=07h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 07h está en el blacklist. Con BTC+SOL solo, el historial muestra 7/12 (58%) IC=+0.043. El blacklist puede estar basado en pares negativos que ya están excluidos.
  - _Umbral_: 20
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 07h del blacklist ORDER_FLOW
  - _Estado_: 2/20 ops en el filtro definido (IC actual=+0.000 PNL=-0.08€)
  - _Datos_: n=2 IC=+0.000 PNL=-0.08€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: 07h sigue en ORDER_FLOW_BLACKLIST_HOURS -- mientras siga ahí, nunca genera fila para volver a evaluarse (26-Ago, triage candidatas estancadas)

**〰️ H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: n=3106 IC=+0.010 PNL=+16.58€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3106 IC=+0.010 PNL=+16.58€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1510 IC=+0.001 PNL=+76.98€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1510 IC=+0.001 PNL=+76.98€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=971 IC=+0.021 PNL=+41.00€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=971 IC=+0.021 PNL=+41.00€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.177 > 0.1 con n=4885 PNL=+3045.79€
  - _Datos_: n=4885 IC=+0.177 PNL=+3045.79€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=2916 IC=+0.068 PNL=+220.27€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2916 IC=+0.068 PNL=+220.27€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=2519 IC=+0.089 PNL=+617.92€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=2519 IC=+0.089 PNL=+617.92€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 0/50 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: confirmada 2026-07-01 (IC=-0.037 n=52) e implementada en shadow_predict.py (skip si drift_15min∈[-0.3,0.3)) -- verificado 26-Ago con 2177 filas post-TWAP reales, 0 caen en la zona filtrada. Frozen by design, no falta n

**🟡 H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.098 > 0.08 con n=11165 PNL=+3148.74€
  - _Datos_: n=11165 IC=+0.098 PNL=+3148.74€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=369 IC=-0.233 PNL=-4.62€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=369 IC=-0.233 PNL=-4.62€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=440 IC=-0.029 PNL=-16.47€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=440 IC=-0.029 PNL=-16.47€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=1007 IC=+0.035 PNL=+85.18€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1007 IC=+0.035 PNL=+85.18€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=124 IC=+0.016 PNL=+2.04€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=124 IC=+0.016 PNL=+2.04€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=8530 IC=+0.021 PNL=+229.81€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=8530 IC=+0.021 PNL=+229.81€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.122 > 0.08 con n=347 PNL=+77.46€
  - _Datos_: n=347 IC=+0.122 PNL=+77.46€

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.281 n=167) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=167 IC=+0.281 PNL=+166.63€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=12851 IC=+0.050 PNL=+1067.44€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=12851 IC=+0.050 PNL=+1067.44€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=4640 IC=+0.064 PNL=+689.60€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4640 IC=+0.064 PNL=+689.60€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.113 > 0.08 con n=551 PNL=+182.56€
  - _Datos_: n=551 IC=+0.113 PNL=+182.56€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.149 > 0.08 con n=1172 PNL=+333.09€
  - _Datos_: n=1172 IC=+0.149 PNL=+333.09€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.097 > 0.08 con n=922 PNL=+446.03€
  - _Datos_: n=922 IC=+0.097 PNL=+446.03€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=64364 IC=+0.118 PNL=+23936.47€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=64364 IC=+0.118 PNL=+23936.47€

**〰️ H-CUSTOM-MERCURY-RETROGRADO** — Mercurio retrógrado: ¿rendimiento peor durante la ventana?
  - _Hipótesis_: Mismo origen que H-CUSTOM-MOON-LLENA (paper de Fornero, 43 Jornadas SADAF 2023). Qi, Wang & Zhang (2022, 48 mercados, 1973-2019): rendimientos 3.33%/año más bajos durante Mercurio retrógrado. Kou & Ma (2022) en China (99.8% cuentas retail): hasta -31% anualizado. Ambos estudios confirman que el mecanismo es la creencia/superstición de inversores retail (mayor efecto cuanto más retail y más supersticioso el mercado), no un efecto astral literal — Polymarket encaja en ese perfil. Ventanas 2026 (fuente pública, actualizar cada año): 26-feb a 20-mar, 29-jun a 23-jul, 24-oct a 13-nov.
  - _Umbral_: n≥100 PERO ADEMÁS necesita cubrir al menos 2-3 ventanas de retrogradación distintas (no solo la de jun-jul 2026) — esperar mínimo hasta después de la ventana de oct-nov 2026
  - _Acción_: Si IC en mercury_retrogrado=1 < IC en mercury_retrogrado=0 con margen ≥0.05 y ≥2 ventanas distintas cubiertas → considerar boost/filtro. No implementar tras una sola ventana (jun-jul 2026) por more que n sea alto — sería solo un evento, no un patrón.
  - _Estado_: n=1792 IC=+0.109 PNL=+195.82€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=1792 IC=+0.109 PNL=+195.82€

**〰️ H-CUSTOM-SMART-MONEY-CONSENSUS** — Consenso de wallets 'smart money' — ¿confirma nuestra dirección?
  - _Hipótesis_: Javi propuso estudiar bots/wallets que operan bien en nuestros mismos mercados. En vez de creer artículos (ya verificamos 2 veces esta semana que las narrativas no aguantan el cruce con datos reales), smart_money_tracker.py mide el track record REAL de wallets activas en BTC/ETH/SOL/XRP Up-or-Down 5/15/60min vía data-api.polymarket.com/positions, filtrado a posiciones 'Up or Down'. Clasifica como 'smart' las wallets con n>=10 posiciones, win_rate>=0.55 y pnl_total>0. smart_money_consensus es el sesgo direccional reciente (Up-Down)/(Up+Down) de esas wallets 'smart' por activo. Hipótesis: si nuestra decisión (BUY_YES/BUY_NO) coincide con el consenso smart money, mejor IC que cuando diverge. RESET METODOLOGICO 2026-07-02: la clasificacion 'smart' original via /positions estaba INVERTIDA para wallets de alta frecuencia (el endpoint solo retiene el residuo perdedor sin redimir; verificado: 'wowitsamazing' figuraba como -$478k y es +$10k/mes en el leaderboard oficial). Desde 2026-07-02T06:12Z el consenso se construye solo con wallets verificadas en el leaderboard oficial (pnl_mes>=$1000, 24 wallets). Los valores de smart_money_consensus capturados en features ANTES de esa fecha provienen de la clasificacion rota — descontar ese tramo al evaluar.
  - _Umbral_: n≥40 y IC>+0.08 — además necesita que existan wallets 'smart' acumuladas (0 al empezar, se van descubriendo cada ciclo)
  - _Acción_: Si IC en confluencia (decisión coincide con signo de smart_money_consensus) supera en >=0.05 al IC en divergencia, con n≥40 en cada lado → boost ×1.1-1.2 cuando coincide, considerar reducir stake cuando diverge fuerte.
  - _Estado_: n=11681 IC=+0.057 PNL=+1136.84€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=11681 IC=+0.057 PNL=+1136.84€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.124 > 0.02 con n=977 PNL=+405.46€
  - _Datos_: n=977 IC=+0.124 PNL=+405.46€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=213 IC=-0.091 PNL=+19.65€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=213 IC=-0.091 PNL=+19.65€

**〰️ H-CUSTOM-WEEKLY-INRANGE-BUYYES** — WEEKLY_PRICE BUY_YES con in_range=1 — ¿estructuralmente sobrevalorado?
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_YES cuando in_range=1 fue 0/3 (todo pérdida). Mecanismo propuesto: acertar un rango de precio estrecho al vencimiento es intrínsecamente poco probable, el mercado puede estar sobrevalorando el 'sí'. Ver H-CUSTOM-WEEKLY-PCTDIST-BUYNO para el lado complementario (BUY_NO con pct_dist alto).
  - _Umbral_: n≥25 y IC<-0.10 para confirmar (evidencia inicial es de solo 3 ops)
  - _Acción_: Si se confirma con n≥25 → filtro causal in_range==1 + BUY_YES → skip en WEEKLY_PRICE
  - _Estado_: n=81 IC=-0.030 PNL=+3.88€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=81 IC=-0.030 PNL=+3.88€

**🟡 H-CUSTOM-WEEKLY-PCTDIST-BUYNO** — WEEKLY_PRICE BUY_NO con pct_dist alto — cuanto más lejos del rango, más seguro
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_NO con pct_dist>=2.09% fue 4/4 victorias (rango 2.09%-23.4%); BUY_NO con pct_dist<8% (pero fuera del corte anterior) tuvo derrotas. Patrón: cuanto más lejos está el spot del rango objetivo al momento de la predicción, más fiable el BUY_NO. Complementa H-CUSTOM-WEEKLY-INRANGE-BUYYES.
  - _Umbral_: n≥25 y IC>+0.10 para confirmar
  - _Acción_: Si se confirma con n≥25 → boost ×1.2 en WEEKLY_PRICE BUY_NO cuando pct_dist≥2
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.450 > 0.1 con n=1669 PNL=+1612.06€
  - _Datos_: n=1669 IC=+0.450 PNL=+1612.06€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=30668 IC=+0.074 PNL=+4459.04€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=30668 IC=+0.074 PNL=+4459.04€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.207 > 0.1 con n=6847 PNL=+4087.72€
  - _Datos_: n=6847 IC=+0.207 PNL=+4087.72€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.141 < -0.1 con n=496 PNL=+60.16€
  - _Datos_: n=496 IC=-0.141 PNL=+60.16€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=3116 IC=+0.067 PNL=+388.88€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=3116 IC=+0.067 PNL=+388.88€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=145 IC=-0.099 PNL=+5.02€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=145 IC=-0.099 PNL=+5.02€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.113 > 0.1 con n=819 PNL=+225.10€
  - _Datos_: n=819 IC=+0.113 PNL=+225.10€

**⏳ H-CUSTOM-ETH15-BUYNO-PRECIO-ALTO** — ETH#15min BUY_NO con precio_yes>0.55 pierde (NO longshot contra favorito)
  - _Hipótesis_: Detectado 2026-07-02: ult.60 shadow ETH15 BUY_NO — py_mkt~0.5 wr=0.67 PNL=+29.3 (n=49); py_mkt 0.6-0.8 wr 0.33-0 PNL=-5.75 (n=9). Filtro RETURN NONE (no SKIP) aplicado en shadow_predict.py (PY_MKT_MAX_BUY_NO_ETH15=0.55) el mismo dia -- bloquea la GENERACIÓN de la fila, no solo la decisión. Esta hipotesis trackea la zona filtrada: si las ops que HABRIAN caido aqui siguen apareciendo en otras estrategias o el IC forward de la zona se vuelve positivo, revisar el filtro. CAVEAT: n=9, muestra chica — el filtro se aplico por asimetria de riesgo (afecta a dinero live), no por significancia. ⚠️ 05-Ago (fix): la clave del filtro decía 'py_mkt', que NUNCA existió ni en features de UPDOWN_GBM (T_h/delta_ratio_macro/drift_15min/drift_60min/pct_spot_vs_ref/sigma_h) ni como columna top-level de results.csv -- corregida a 'precio_yes_mercado' (columna real). Aun así, con la clave correcta esta hipótesis NUNCA podrá acumular n mientras el filtro RETURN NONE siga activo -- es el mismo patrón 'frozen by design' que H-CUSTOM-LATE15-PHOTO-FINISH (más abajo): la propia protección impide generar los datos necesarios para volver a evaluarla. Para monitorearla de verdad haría falta un logger separado que capture la señal SIN aplicar el filtro (mismo patrón que gate_bucket_propio con data/markets histórico) -- no construido, pendiente decisión.
  - _Umbral_: 20
  - _Acción_: Si IC forward de la zona >0 con n>=20 → retirar filtro; si confirma negativo → considerar extender a BTC/SOL 15min
  - _Estado_: 4/20 ops en el filtro definido (IC actual=-0.067 PNL=-2.04€)
  - _Datos_: n=4 IC=-0.067 PNL=-2.04€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: PY_MKT_MAX_BUY_NO_ETH15=0.55 en shadow_predict.py hace RETURN NONE (bloquea generación, no solo decisión) -- nunca podrá acumular n mientras siga activo. Haría falta un logger separado sin el filtro para monitorear de verdad (no construido, 26-Ago)

**〰️ H-PRECIO-YES-BARATO** — BUY_YES con precio de mercado 0.30-0.40 — mercado infravalora YES
  - _Hipótesis_: Detectado 2026-07-03 en benchmark de calibración del mercado (7d, estrategias GBM): en el bucket precio_yes_mercado [0.3-0.4) la frecuencia real de YES fue 0.45 vs 0.35 implícito (+0.10, n=38). Posible sesgo favorito-longshot suave en binarios de 15min (complemento del LONGSHOT ya activo para BUY_NO con py<0.20). Si se confirma, BUY_YES comprado en esa banda lleva viento de cola estructural del propio mercado, independiente del modelo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → kelly_boost ×1.1 para BUY_YES con precio_yes_mercado en [0.30,0.40), simétrico al longshot BUY_NO existente
  - _Estado_: n=32636 IC=-0.133 PNL=+2780.66€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=32636 IC=-0.133 PNL=+2780.66€

**⏳ H-CUSTOM-LATE15-PHOTO-FINISH** — GBM_LATE_15M photo finish — entrar pegado al strike es moneda al aire cobrada como favorito
  - _Hipótesis_: Detectado 2026-07-05 validando contra nuestros datos la única idea aprovechable de un artículo-anuncio de copy-bot: GBM_LATE_15M con |drift_ventana_pct|<0.02 tenía IC=-0.145 n=181 (win 35%, -9.70€), estable en ambas mitades temporales (-0.163/-0.127), monótono con la distancia (0.02-0.05: IC=+0.061; ≥0.05: IC=+0.14..0.19) y consistente en crudo y normalizado por sigma (|d_gbm|<0.1 IC=-0.081 n=244). BTC (IC=-0.163 n=90) y ETH (-0.130 n=79) concentraban el daño; SOL/XRP apenas entran en esa zona. Mecanismo: sin distancia real al strike el resultado es ~50/50 pero py_entrada ya cobra favorito. Filtro GBM_LATE_DRIFT_VENT_MIN_PCT=0.02 aplicado en shadow_predict el 2026-07-05. Esta hipótesis trackea la zona filtrada: si vuelven a aparecer ops aquí, el filtro se ha roto.
  - _Umbral_: 200
  - _Acción_: Si aparecen ops nuevas en la zona → el filtro está roto, revisar shadow_predict. Si el buffer [0.02,0.05) se vuelve negativo con n≥60 forward → subir el corte a 0.05.
  - _Estado_: 0/200 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: GBM_LATE_DRIFT_VENT_MIN_PCT=0.02 aplicado en shadow_predict.py desde 2026-07-05 -- bloquea la generación de la zona que esta hipótesis mide. Se mantiene como vigilancia pasiva (si vuelven a aparecer ops en la zona, el filtro se rompió), no como 'acumulando' (26-Ago)

**⏳ H-CUSTOM-PHOTO-FINISH-SNIPER** — Photo finish sniper — comprar el lado rezagado a 1-3c en los últimos segundos (estilo egig)
  - _Hipótesis_: 2026-07-05: wallet 'egig' verificada on-chain (leaderboard oficial +$41k all-time; flujo 23h: -$729 compras / +$2,140 redeems). Forense de 497 trades: compra a 1-3c (mediana 2c) el lado rezagado a mediana 2s del cierre, exclusivamente en photo finishes (dist spot-strike mediana 0.027%). Mecanismo: el mercado cobra los finales de foto como decididos cuando son ~moneda al aire — es el espejo del filtro photo finish que aplicamos a GBM_LATE el mismo día. Win rate implícito ~6% con breakeven 2% (~3x por ticket). photo_finish_logger.py (screen pfinish) acumula dataset en data/shadow/photo_finish_YYYY-MM-DD.csv: libro del lado rezagado a T-10s + outcome oficial vía outcomePrices. CAVEATS a medir: profundidad real del ask a 1-3c (egig compite por asks rancios), frecuencia del setup, y que nuestro T-10s no es su T-2s.
  - _Umbral_: 200
  - _Acción_: Si EV>2x sostenido con n≥200 → proponer watcher de ejecución dedicado (decisión de Javi: toca dinero real y requiere loop sub-5s). Si win rate ≈ ask (mercado calibrado también aquí) → archivar.
  - _Estado_: 0/200 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: REFUTADA_28JUL_TRACKING_SEPARADO: ya evaluada a mano 28-Jul con data/shadow/photo_finish_YYYY-MM-DD.csv directo (ver CLAUDE.md punto 13 protocolo arranque / memoria hipotesis_auto.md) -- este filtro genérico busca strategy='PHOTO_FINISH_SNIPER' en results.csv, pero photo_finish_logger.py escribe a un CSV propio con schema distinto y JAMÁS escribe ahí, así que n=0 estructuralmente para siempre por este motor. No repetir la evaluación por aquí; si se reabre, hacerlo contra el CSV propio como el 28-Jul.

**〰️ H-CUSTOM-LATE15-BTC-BUYNO-COINFLIP** — GBM_LATE_15M BTC#BUY_NO es moneda al aire — candidata a quitar del motor estrella
  - _Hipótesis_: Detectado 2026-07-06 desglosando la estrategia que carga el bankroll shadow (GBM_LATE_15M, +364€): por par×dirección, BTC#BUY_NO es la única tupla sin edge — 90/182 (49.5%) PNL=+8.92€, prácticamente coinflip, arrastrando a la baja el IC medio del subtipo. Contraste con las estrellas del mismo motor: SOL#BUY_NO 66.1% (+86.70€), XRP#BUY_YES 67.4% (+80.35€), SOL#BUY_YES 64.4% (+77.08€). ETH#BUY_NO (53.6%) es débil pero positivo; BTC#BUY_YES (57.8%) sí funciona. Hipótesis: el edge de entrada tardía en 15min es fuerte en SOL/XRP, medio en ETH/BTC alcista, y NULO en BTC bajista (BTC es el par más eficiente/arbitrado). Quitar BTC#BUY_NO sube el IC del subtipo sin perder PNL real. NO afecta live (la whitelist live es SOL/XRP BUY_NO + ETH BUY_YES, BTC no está).
  - _Umbral_: n≥150 y IC<+0.03 (n=182 ya disponible al crearla)
  - _Acción_: Si IC<+0.03 con n≥150 → filtro causal skip GBM_LATE_15M BTC#BUY_NO en shadow_predict (deja de diluir el subtipo). Si IC sube >+0.08 → mantener.
  - _Estado_: n=3264 IC=+0.132 PNL=+2007.33€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=3264 IC=+0.132 PNL=+2007.33€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.205 > 0.08 con n=4172 PNL=+3044.94€
  - _Datos_: n=4172 IC=+0.205 PNL=+3044.94€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=8049 IC=+0.051 PNL=+635.73€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=8049 IC=+0.051 PNL=+635.73€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.095 > 0.08 con n=3534 PNL=+1941.10€
  - _Datos_: n=3534 IC=+0.095 PNL=+1941.10€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.219 > 0.08 con n=824 PNL=+493.64€
  - _Datos_: n=824 IC=+0.219 PNL=+493.64€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.222 < -0.1 con n=3384 PNL=-270.52€
  - _Datos_: n=3384 IC=-0.222 PNL=-270.52€

**🟡 H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.211 > 0.2 con n=8905 PNL=+7082.39€
  - _Datos_: n=8905 IC=+0.211 PNL=+7082.39€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.122 > 0.08 con n=125 PNL=+55.74€
  - _Datos_: n=125 IC=+0.122 PNL=+55.74€

**🟡 H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.083 > 0.08 con n=3239 PNL=+1147.14€
  - _Datos_: n=3239 IC=+0.083 PNL=+1147.14€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.178 > 0.08 con n=3001 PNL=+2277.38€
  - _Datos_: n=3001 IC=+0.178 PNL=+2277.38€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=5054 IC=-0.025 PNL=+1415.57€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=5054 IC=-0.025 PNL=+1415.57€

**〰️ H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: n=688 IC=+0.074 PNL=-50.29€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=688 IC=+0.074 PNL=-50.29€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.244 > 0.08 con n=4855 PNL=-380.66€
  - _Datos_: n=4855 IC=+0.244 PNL=-380.66€

**〰️ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: n>=40 y IC>0.08
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: n=69 IC=+0.021 PNL=+8.59€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=69 IC=+0.021 PNL=+8.59€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.101 n=1746) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1746 IC=+0.101 PNL=+382.02€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.307 > 0.08 con n=460 PNL=+131.42€
  - _Datos_: n=460 IC=+0.307 PNL=+131.42€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.412 n=567) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=567 IC=+0.412 PNL=+813.96€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=14231 IC=+0.186 PNL=-1449.66€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=14231 IC=+0.186 PNL=-1449.66€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.221 > 0.1 con n=231 PNL=+154.04€
  - _Datos_: n=231 IC=+0.221 PNL=+154.04€
