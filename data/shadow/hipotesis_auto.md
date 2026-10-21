# Hipótesis automáticas — 2026-10-21 19:00 UTC
_Generado por shadow_postmortem.py sobre 997681 resoluciones (PNL=+130388.44€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.255 (n=194)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=628)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.236 (n=790)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.138)

- **PATRÓN** `n_total_lado` > `65.0` → IC=+0.179 (n=285)

  - _Acción_: Kelly boost +0.90€ cuando `n_total_lado` > 65.0 (IC base=+0.138)

- **PATRÓN** `banda_hit_calibrado` > `0.6284` → IC=+0.269 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6284 (IC base=+0.138)

- **PATRÓN** `banda_z` > `9.174` → IC=+0.206 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.174 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=916)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `2655.6606` → IC=+0.138 (n=750)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2655.6606 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.153 (n=462)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 98.0 (IC base=+0.138)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.233 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.143)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.199 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.143)

- **PATRÓN** `banda_hit_calibrado` > `0.6167` → IC=+0.262 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6167 (IC base=+0.143)

- **PATRÓN** `banda_z` > `9.568` → IC=+0.211 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.568 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.186 (n=256)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=817)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.155 (n=424)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 100.0 (IC base=+0.143)

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
- **FILTRO** `restante_s_al_confirmar` < `142.26` → IC=-0.200 (n=10163)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 142.26
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=30493)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `128.66` → IC=-0.257 (n=1129)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.66
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=3390)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `122.04` → IC=-0.287 (n=1091)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.04
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=3273)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `167.38` → IC=-0.202 (n=2685)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 167.38
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=8057)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `133.09` → IC=-0.276 (n=1981)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.09
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=5945)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.214 (n=21993)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.108)

- **PATRÓN** `libro_spread` < `0.015` → IC=+0.134 (n=4362)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.015 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `9067.0203` → IC=+0.174 (n=1978)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 9067.0203 (IC base=+0.108)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.129 (n=18603)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.128 (n=33580)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 11.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.226 (n=17470)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.149 (n=7246)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `7054.8156` → IC=+0.158 (n=2800)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 7054.8156 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.199 (n=2036)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.364 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.194 (n=2498)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `16428.8963` → IC=+0.197 (n=648)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 16428.8963 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.189 (n=1791)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 7.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.187 (n=1995)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 17.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.185 (n=2556)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `16193.8223` → IC=+0.194 (n=659)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 16193.8223 (IC base=+0.183)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.170 (n=474)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.61 (IC base=+0.082)

- **PATRÓN** `libro_liquidez` > `6857.6712` → IC=+0.167 (n=124)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 6857.6712 (IC base=+0.082)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.136 (n=1136)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.44 (IC base=+0.082)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=4268)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.162 (n=3622)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 15.0 (IC base=+0.162)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.372 (n=1407)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.226 (n=783)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.347 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.213 (n=2213)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.210)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=1078)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.150 (n=698)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 11.0 (IC base=+0.144)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.263 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=843)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `2205.3811` → IC=+0.161 (n=467)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2205.3811 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.162 (n=152)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.068)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.249 (n=995)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.419 (n=1166)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.151 (n=1293)
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
- **PATRÓN** `hora_utc` > `9.0` → IC=+0.162 (n=323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 9.0 (IC base=+0.144)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.349 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.135 (n=206)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `1142.4326` → IC=+0.127 (n=258)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 1142.4326 (IC base=+0.144)

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

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.207 (n=18625)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.203 (n=15796)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.236 (n=7656)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.202)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.183 (n=4056)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 6.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.181 (n=3602)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 15.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.183 (n=4197)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.73 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.181 (n=3497)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=2217)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.230 (n=1476)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.306 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.223)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=4218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.184 (n=3587)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 15.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.189 (n=3301)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.258 (n=3658)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.248)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.363 (n=1185)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=4133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=3532)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.195 (n=3050)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.190)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.431 (n=798)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.424 (n=700)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=821)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.430 (n=843)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `4221.5556` → IC=+0.435 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4221.5556 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.430 (n=313)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.432)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.441 (n=218)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.445 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.432)

- **PATRÓN** `libro_liquidez` > `15539.3062` → IC=+0.433 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15539.3062 (IC base=+0.432)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.444 (n=282)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.432)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.435 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.432)

- **PATRÓN** `libro_liquidez` > `4514.7204` → IC=+0.433 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4514.7204 (IC base=+0.432)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.404 (n=144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.400)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.402 (n=141)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.400)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.428 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.400)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.77` → IC=-0.318 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.77
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=26)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=24077)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=24365)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.190 (n=4147)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.188 (n=7702)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 12.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.201 (n=10821)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.186)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=5032)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.227 (n=4941)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.285 (n=3527)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.190 (n=4125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.212 (n=5508)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.182)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=5072)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.223 (n=3861)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.276 (n=3432)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.206 (n=9261)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.261 (n=3588)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=4006)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=4031)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.248 (n=4210)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.191 (n=8779)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=8591)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `3.77` → IC=+0.135 (n=10520)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 3.77 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=4336)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.141 (n=4391)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=5258)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `2.77` → IC=+0.146 (n=3971)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.77 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.188 (n=4443)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.113)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.134 (n=4677)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.96 (IC base=+0.113)

- **PATRÓN** `lag_apertura_s` < `3.33` → IC=+0.133 (n=5294)

  - _Acción_: Kelly boost +0.66€ cuando `lag_apertura_s` < 3.33 (IC base=+0.113)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.302 (n=1683)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.294)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.294 (n=1657)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.294)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.383 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.294)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.288 (n=764)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.280)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.358 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `5034.4871` → IC=+0.289 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5034.4871 (IC base=+0.280)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.322 (n=544)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.298)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.302 (n=797)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.298)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.392 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.298)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.298 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.298)

- **PATRÓN** `libro_liquidez` > `2114.2422` → IC=+0.314 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2114.2422 (IC base=+0.298)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.446 (n=777)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.443 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.444 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.442 (n=882)

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
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.450)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.452 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.450)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.451 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.450)

- **PATRÓN** `libro_liquidez` > `1979.4391` → IC=+0.468 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1979.4391 (IC base=+0.450)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4751` → IC=+0.140 (n=13558)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4751 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.126 (n=13721)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.125 (n=9466)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.982` → IC=+0.248 (n=4522)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.982 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.7869` → IC=+0.272 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7869 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` < `0.3721` → IC=+0.260 (n=3804)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3721 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.901` → IC=+0.192 (n=5132)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 5.901 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.2044` → IC=+0.259 (n=3951)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2044 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6184` → IC=+0.265 (n=3951)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6184 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.3024` → IC=+0.243 (n=1387)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3024 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.3461` → IC=+0.230 (n=4380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3461 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.125 (n=11348)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.6857` → IC=+0.129 (n=18924)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.6857 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.1556` → IC=+0.187 (n=6109)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.1556 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` < `0.6963` → IC=+0.185 (n=2855)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6963 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.0511` → IC=+0.182 (n=2941)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.0511 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2955` → IC=+0.233 (n=1619)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2955 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.6774` → IC=+0.205 (n=3679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6774 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `107.0` → IC=+0.221 (n=10899)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 107.0 (IC base=+0.075)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.210 (n=984)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.3476` → IC=+0.205 (n=2950)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3476 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.212 (n=1436)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.204 (n=1973)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.9823` → IC=+0.278 (n=1337)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9823 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.838` → IC=+0.285 (n=1291)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.838 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2339` → IC=+0.251 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2339 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.4401` → IC=+0.203 (n=2813)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4401 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=3172)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `2075.1442` → IC=+0.208 (n=983)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2075.1442 (IC base=+0.200)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.217 (n=1792)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.239 (n=2464)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0086 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.0872` → IC=+0.270 (n=821)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0872 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.254 (n=896)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.5316` → IC=+0.258 (n=2461)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5316 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.0944` → IC=+0.238 (n=2208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0944 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2883` → IC=+0.264 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2883 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.4411` → IC=+0.244 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4411 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.67` → IC=+0.244 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.67 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1622.02` → IC=+0.247 (n=2198)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1622.02 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.238 (n=830)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.237)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.238 (n=1065)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.229)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.232 (n=1098)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.1057` → IC=+0.261 (n=1064)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1057 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.241 (n=2536)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` > `0.9484` → IC=+0.280 (n=806)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9484 (IC base=+0.229)

- **PATRÓN** `dist_vwap_pct` > `0.1308` → IC=+0.237 (n=1306)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1308 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.349` → IC=+0.266 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.349 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` < `1.2335` → IC=+0.230 (n=2419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2335 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` > `0.6224` → IC=+0.234 (n=2418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6224 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.2778` → IC=+0.268 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2778 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `2.4426` → IC=+0.258 (n=794)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4426 (IC base=+0.229)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.151 (n=2469)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0058 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.170 (n=821)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.153 (n=929)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.7272` → IC=+0.176 (n=2463)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.7272 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` < `0.1366` → IC=+0.154 (n=2293)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1366 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.071` → IC=+0.148 (n=399)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 11.071 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.189` → IC=+0.140 (n=2248)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 4.189 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `1.2049` → IC=+0.140 (n=2463)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.2049 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.0951` → IC=+0.160 (n=898)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0951 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `2.4535` → IC=+0.144 (n=2343)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4535 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `1.4133` → IC=+0.134 (n=2344)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.4133 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `217.0` → IC=+0.170 (n=1002)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 217.0 (IC base=+0.132)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.225 (n=1022)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=3220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.271 (n=1174)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.263` → IC=+0.275 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.263 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.201 (n=2719)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.3526` → IC=+0.213 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3526 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `2.6973` → IC=+0.212 (n=1349)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6973 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.203 (n=3673)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `1967.8232` → IC=+0.200 (n=1390)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1967.8232 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.222 (n=2415)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.4588` → IC=+0.224 (n=2414)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4588 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=1024)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.217 (n=968)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` < `0.0192` → IC=+0.275 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0192 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.379` → IC=+0.251 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.379 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.3473` → IC=+0.258 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3473 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `2.7242` → IC=+0.229 (n=1182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7242 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.221 (n=1437)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `2048.3156` → IC=+0.221 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2048.3156 (IC base=+0.216)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.220 (n=2277)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.216)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.141 (n=151)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=3700)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.165 (n=547)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0037 (IC base=+0.056)

- **PATRÓN** `ibs_20min` > `0.9538` → IC=+0.231 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9538 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` > `0.1404` → IC=+0.335 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1404 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` < `0.1948` → IC=+0.329 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1948 (IC base=+0.056)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.146` → IC=+0.192 (n=1175)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 5.146 (IC base=+0.056)

- **PATRÓN** `volumen_regimen` < `0.8578` → IC=+0.336 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8578 (IC base=+0.056)

- **PATRÓN** `volumen_regimen` > `1.2247` → IC=+0.351 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2247 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` < `0.1664` → IC=+0.329 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1664 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.2985` → IC=+0.348 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2985 (IC base=+0.056)

- **PATRÓN** `volumen_spike_ratio` < `1.4107` → IC=+0.352 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4107 (IC base=+0.056)

- **PATRÓN** `volumen_spike_ratio` > `2.2172` → IC=+0.329 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2172 (IC base=+0.056)

- **PATRÓN** `ballena_activa_n` < `131.0` → IC=+0.337 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 131.0 (IC base=+0.056)

- **PATRÓN** `ibs_20min` < `0.093` → IC=+0.174 (n=963)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.093 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` > `0.3285` → IC=+0.143 (n=466)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.3285 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` < `0.1308` → IC=+0.140 (n=1572)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.1308 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` < `0.8417` → IC=+0.147 (n=1144)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8417 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` > `1.1677` → IC=+0.145 (n=572)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.1677 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.203 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=+0.036)

- **PATRÓN** `volumen_spike_ratio` < `1.7775` → IC=+0.139 (n=1096)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.7775 (IC base=+0.036)

- **PATRÓN** `volumen_spike_ratio` > `2.1545` → IC=+0.151 (n=745)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.1545 (IC base=+0.036)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.173 (n=105)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=563)

- **FILTRO** `ibs_20min` < `0.2759` → IC=-0.196 (n=166)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2759
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=502)

- **FILTRO** `ibs_20min` > `0.2174` → IC=-0.133 (n=3631)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2174
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=1791)

- **FILTRO** `sigma_ewma_delta_pct` > `8.658` → IC=-0.239 (n=572)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.658
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=4850)

- **PATRÓN** `ibs_20min` > `0.7834` → IC=+0.183 (n=228)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.7834 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` > `1.0126` → IC=+0.279 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0126 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` < `0.4892` → IC=+0.263 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4892 (IC base=+0.031)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.146` → IC=+0.153 (n=211)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 3.146 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` < `0.7536` → IC=+0.262 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7536 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` > `1.0006` → IC=+0.308 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0006 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` < `0.1553` → IC=+0.279 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1553 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` < `2.1989` → IC=+0.291 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1989 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` > `1.5489` → IC=+0.267 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5489 (IC base=+0.031)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.266 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.031)

- **PATRÓN** `ibs_20min` < `0.2174` → IC=+0.146 (n=1791)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.2174 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` > `0.2659` → IC=+0.280 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2659 (IC base=-0.041)

- **PATRÓN** `volumen_regimen` < `0.7052` → IC=+0.305 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7052 (IC base=-0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.0806` → IC=+0.306 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0806 (IC base=-0.041)

- **PATRÓN** `volumen_spike_ratio` < `2.43` → IC=+0.301 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.43 (IC base=-0.041)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6093` → IC=-0.180 (n=997)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6093
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=2994)

- **FILTRO** `ibs_20min` < `0.7576` → IC=-0.149 (n=2634)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7576
  - _Potencial_: sin este filtro IC_bueno=+0.099 (n=1357)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.161 (n=963)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=3028)

- **FILTRO** `ibs_20min` > `0.75` → IC=-0.204 (n=1431)

  - _Acción_: SKIP cuando `ibs_20min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=4303)

- **PATRÓN** `dist_vwap_pct` > `1.0839` → IC=+0.343 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0839 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` < `0.2486` → IC=+0.305 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2486 (IC base=-0.065)

- **PATRÓN** `volumen_regimen` < `1.1484` → IC=+0.298 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1484 (IC base=-0.065)

- **PATRÓN** `volumen_regimen` > `0.704` → IC=+0.317 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.704 (IC base=-0.065)

- **PATRÓN** `volumen_pendiente_norm` < `0.0995` → IC=+0.302 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0995 (IC base=-0.065)

- **PATRÓN** `volumen_pendiente_norm` > `0.0719` → IC=+0.305 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0719 (IC base=-0.065)

- **PATRÓN** `volumen_spike_ratio` < `1.4142` → IC=+0.317 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4142 (IC base=-0.065)

- **PATRÓN** `volumen_spike_ratio` > `1.8367` → IC=+0.305 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8367 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` > `0.8005` → IC=+0.277 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8005 (IC base=-0.006)

- **PATRÓN** `volumen_regimen` > `1.0685` → IC=+0.286 (n=713)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0685 (IC base=-0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.1042` → IC=+0.282 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1042 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` < `2.1851` → IC=+0.262 (n=1276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1851 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` > `1.4295` → IC=+0.266 (n=1450)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4295 (IC base=-0.006)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.210 (n=5944)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.3205` → IC=+0.169 (n=17804)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.3205 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.9537` → IC=+0.300 (n=1327)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9537 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.593` → IC=+0.163 (n=7995)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 3.593 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` < `1.1721` → IC=+0.264 (n=6569)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1721 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` > `0.6887` → IC=+0.270 (n=5868)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6887 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.2396` → IC=+0.278 (n=1962)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2396 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` < `1.4596` → IC=+0.263 (n=3494)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4596 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` > `2.2717` → IC=+0.271 (n=4749)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2717 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.297 (n=10050)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 91.0 (IC base=+0.097)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.154 (n=5703)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0093 (IC base=+0.073)

- **PATRÓN** `ibs_20min` < `0.6591` → IC=+0.143 (n=17107)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.6591 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.2414` → IC=+0.265 (n=5354)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2414 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` < `0.7047` → IC=+0.263 (n=2371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7047 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` > `1.1955` → IC=+0.266 (n=1796)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1955 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.316 (n=1157)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` < `1.5796` → IC=+0.290 (n=3410)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5796 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` > `2.2644` → IC=+0.283 (n=3513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2644 (IC base=+0.073)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.295 (n=7691)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 77.0 (IC base=+0.073)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.5825` → IC=-0.130 (n=2438)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5825
  - _Potencial_: sin este filtro IC_bueno=+0.191 (n=2438)

- **FILTRO** `ibs_20min` > `0.7414` → IC=-0.213 (n=1030)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7414
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=3094)

- **FILTRO** `sigma_ewma_delta_pct` > `4.36` → IC=-0.209 (n=904)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.36
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=3220)

- **PATRÓN** `ibs_20min` > `0.9221` → IC=+0.316 (n=1219)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9221 (IC base=+0.031)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.977` → IC=+0.216 (n=864)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.977 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.2297` → IC=+0.302 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2297 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` < `1.4432` → IC=+0.251 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4432 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` > `2.253` → IC=+0.277 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.253 (IC base=+0.031)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.282 (n=1087)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.031)

- **PATRÓN** `ibs_20min` < `0.1667` → IC=+0.158 (n=1036)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.1667 (IC base=-0.030)

- **PATRÓN** `volumen_pendiente_norm` < `0.0733` → IC=+0.412 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0733 (IC base=-0.030)

- **PATRÓN** `volumen_spike_ratio` < `2.5999` → IC=+0.407 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5999 (IC base=-0.030)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.400 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=-0.030)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.846` → IC=+0.145 (n=1227)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.846 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.1162` → IC=+0.217 (n=888)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1162 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` < `1.1965` → IC=+0.194 (n=1738)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 1.1965 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` > `0.6835` → IC=+0.203 (n=1552)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6835 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` < `0.0746` → IC=+0.192 (n=1595)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.0746 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.2755` → IC=+0.232 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2755 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `1.4243` → IC=+0.219 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4243 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` > `2.4876` → IC=+0.195 (n=571)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.4876 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `273.0` → IC=+0.228 (n=1139)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 273.0 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` < `0.1638` → IC=+0.232 (n=1155)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1638 (IC base=-0.004)

- **PATRÓN** `volumen_regimen` < `1.1702` → IC=+0.225 (n=1116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1702 (IC base=-0.004)

- **PATRÓN** `volumen_regimen` > `0.6195` → IC=+0.232 (n=1116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6195 (IC base=-0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2713` → IC=+0.293 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2713 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.5317` → IC=+0.235 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5317 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.1554` → IC=+0.246 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1554 (IC base=-0.004)

- **PATRÓN** `ballena_activa_n` < `201.0` → IC=+0.240 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 201.0 (IC base=-0.004)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.311 (n=865)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.268)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.276 (n=2725)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.268)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.310 (n=1367)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.268)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.678` → IC=+0.300 (n=835)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.678 (IC base=+0.268)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.282 (n=2259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.268)

- **PATRÓN** `volumen_spike_ratio` > `1.6104` → IC=+0.274 (n=2507)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6104 (IC base=+0.268)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.279 (n=3088)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.268)

- **PATRÓN** `libro_liquidez` > `2049.8784` → IC=+0.285 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2049.8784 (IC base=+0.268)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.287 (n=1526)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.268)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.325 (n=1017)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.1807` → IC=+0.310 (n=988)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1807 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.320 (n=853)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.291)

- **PATRÓN** `ibs_20min` < `0.3704` → IC=+0.295 (n=2243)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3704 (IC base=+0.291)

- **PATRÓN** `ibs_20min` > `0.2629` → IC=+0.298 (n=1018)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2629 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.522` → IC=+0.309 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.522 (IC base=+0.291)

- **PATRÓN** `volumen_pendiente_norm` < `0.1971` → IC=+0.290 (n=2193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1971 (IC base=+0.291)

- **PATRÓN** `volumen_pendiente_norm` > `0.3414` → IC=+0.304 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3414 (IC base=+0.291)

- **PATRÓN** `volumen_spike_ratio` < `1.5806` → IC=+0.297 (n=716)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5806 (IC base=+0.291)

- **PATRÓN** `volumen_spike_ratio` > `2.6611` → IC=+0.301 (n=972)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6611 (IC base=+0.291)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.294 (n=1180)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `2040.4984` → IC=+0.308 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2040.4984 (IC base=+0.291)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.292 (n=1409)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.291)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7377` → IC=-0.191 (n=1077)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7377
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=3238)

- **PATRÓN** `ibs_20min` > `0.8773` → IC=+0.176 (n=1028)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.8773 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` > `0.1555` → IC=+0.235 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1555 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` < `0.3685` → IC=+0.236 (n=1405)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3685 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` < `1.0079` → IC=+0.243 (n=1276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0079 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` > `0.6686` → IC=+0.233 (n=1295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6686 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` < `0.1634` → IC=+0.237 (n=1536)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1634 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.1024` → IC=+0.247 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1024 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` < `2.4348` → IC=+0.241 (n=1402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4348 (IC base=+0.031)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.266 (n=1254)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 102.0 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` < `0.3363` → IC=+0.235 (n=1080)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3363 (IC base=-0.003)

- **PATRÓN** `volumen_regimen` < `1.0308` → IC=+0.239 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0308 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` < `0.1017` → IC=+0.249 (n=916)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1017 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.291 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.7961` → IC=+0.271 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7961 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.4337` → IC=+0.249 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4337 (IC base=-0.003)

- **PATRÓN** `ballena_activa_n` < `124.0` → IC=+0.260 (n=952)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 124.0 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7619` → IC=-0.214 (n=1875)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7619
  - _Potencial_: sin este filtro IC_bueno=+0.307 (n=1875)

- **FILTRO** `ibs_20min` > `0.6495` → IC=-0.237 (n=911)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6495
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=2735)

- **FILTRO** `sigma_ewma_delta_pct` > `8.501` → IC=-0.248 (n=426)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.501
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=3220)

- **PATRÓN** `ibs_20min` > `0.7619` → IC=+0.307 (n=1875)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7619 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` > `0.2157` → IC=+0.338 (n=837)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2157 (IC base=+0.046)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.526` → IC=+0.185 (n=583)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 9.526 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` < `0.8471` → IC=+0.333 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8471 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` > `0.7021` → IC=+0.327 (n=1257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7021 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` < `0.159` → IC=+0.323 (n=1452)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.159 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.355 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` < `1.4368` → IC=+0.349 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4368 (IC base=+0.046)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.341 (n=1202)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.046)

- **PATRÓN** `ibs_20min` < `0.6495` → IC=+0.120 (n=2735)

  - _Acción_: Kelly boost +0.60€ cuando `ibs_20min` < 0.6495 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` < `0.2053` → IC=+0.252 (n=1120)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2053 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` < `0.7014` → IC=+0.262 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7014 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.0758` → IC=+0.264 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0758 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` < `2.4253` → IC=+0.253 (n=1159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4253 (IC base=+0.031)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.271 (n=1178)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.031)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.347 (n=1766)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.304)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.308 (n=768)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.304)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.314 (n=939)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.304)

- **PATRÓN** `ibs_20min` > `0.6604` → IC=+0.336 (n=1976)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6604 (IC base=+0.304)

- **PATRÓN** `dist_vwap_pct` > `0.2086` → IC=+0.331 (n=1121)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2086 (IC base=+0.304)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.809` → IC=+0.324 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.809 (IC base=+0.304)

- **PATRÓN** `volumen_regimen` > `0.8624` → IC=+0.322 (n=1317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8624 (IC base=+0.304)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.344 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.304)

- **PATRÓN** `volumen_spike_ratio` > `1.8002` → IC=+0.320 (n=1262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8002 (IC base=+0.304)

- **PATRÓN** `libro_liquidez` > `2620.7944` → IC=+0.310 (n=1317)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2620.7944 (IC base=+0.304)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.338 (n=1703)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.304)

- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.336 (n=1385)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.304)

- **PATRÓN** `drift_60min` |x|≤ `0.1858` → IC=+0.306 (n=914)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1858 (IC base=+0.304)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.315 (n=803)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.304)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.306 (n=1017)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.304)

- **PATRÓN** `ibs_20min` < `0.3676` → IC=+0.328 (n=2077)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3676 (IC base=+0.304)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.603` → IC=+0.315 (n=769)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.603 (IC base=+0.304)

- **PATRÓN** `volumen_regimen` < `0.7185` → IC=+0.310 (n=916)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7185 (IC base=+0.304)

- **PATRÓN** `volumen_regimen` > `1.224` → IC=+0.333 (n=692)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.224 (IC base=+0.304)

- **PATRÓN** `volumen_pendiente_norm` > `0.2831` → IC=+0.352 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2831 (IC base=+0.304)

- **PATRÓN** `volumen_spike_ratio` < `1.4153` → IC=+0.315 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4153 (IC base=+0.304)

- **PATRÓN** `volumen_spike_ratio` > `2.1353` → IC=+0.306 (n=862)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1353 (IC base=+0.304)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.226 (n=4393)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.0874` → IC=+0.202 (n=4391)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0874 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=13675)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.5592` → IC=+0.235 (n=13161)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5592 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.1656` → IC=+0.210 (n=5353)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1656 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.204` → IC=+0.263 (n=2583)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.204 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.1893` → IC=+0.169 (n=8728)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.1893 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` > `0.6238` → IC=+0.166 (n=8729)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6238 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2927` → IC=+0.207 (n=1923)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2927 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6104` → IC=+0.193 (n=4255)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6104 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `1973.7124` → IC=+0.182 (n=11758)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 1973.7124 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.199 (n=12084)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 94.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.185 (n=8388)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.007 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.0795` → IC=+0.228 (n=4191)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0795 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=4669)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` < `0.5001` → IC=+0.237 (n=12565)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5001 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` < `0.1749` → IC=+0.175 (n=8921)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.1749 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.004` → IC=+0.198 (n=2049)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 10.004 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.684` → IC=+0.181 (n=11088)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 2.684 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.1823` → IC=+0.163 (n=8967)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1823 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.294` → IC=+0.224 (n=1862)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.294 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6358` → IC=+0.185 (n=3938)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6358 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.192 (n=11546)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 100.0 (IC base=+0.180)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.235 (n=737)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.3321` → IC=+0.233 (n=2209)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3321 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.228 (n=824)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.221 (n=1489)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.9282` → IC=+0.293 (n=1473)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9282 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.906` → IC=+0.327 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.906 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.2806` → IC=+0.275 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2806 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `1.4374` → IC=+0.216 (n=2093)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4374 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=2399)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.216)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.251 (n=1703)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0082 (IC base=+0.250)

- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.264 (n=773)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.250)

- **PATRÓN** `drift_60min` |x|≤ `0.1688` → IC=+0.289 (n=1133)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1688 (IC base=+0.250)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.254 (n=1741)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.250)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.253 (n=819)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.250)

- **PATRÓN** `ibs_20min` < `0.2982` → IC=+0.275 (n=1496)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2982 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` < `0.1004` → IC=+0.252 (n=1483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1004 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` > `0.2975` → IC=+0.291 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2975 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` < `1.4351` → IC=+0.274 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4351 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` > `2.6968` → IC=+0.255 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6968 (IC base=+0.250)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.255 (n=1917)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.250)

- **PATRÓN** `libro_liquidez` > `1523.1906` → IC=+0.259 (n=1698)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1523.1906 (IC base=+0.250)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.252 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.250)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.219 (n=666)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.1598` → IC=+0.182 (n=1324)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.1598 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.170 (n=2091)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.3323` → IC=+0.224 (n=1985)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3323 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.1371` → IC=+0.216 (n=1189)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1371 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.288` → IC=+0.222 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.288 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.6924` → IC=+0.163 (n=874)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.6924 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.194 (n=318)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.4127` → IC=+0.171 (n=649)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.4127 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `2.5032` → IC=+0.168 (n=648)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.5032 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `419.0` → IC=+0.158 (n=1907)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 419.0 (IC base=+0.154)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.169 (n=2064)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0058 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.2342` → IC=+0.173 (n=1816)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2342 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.185 (n=988)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.6182` → IC=+0.205 (n=2064)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6182 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.493` → IC=+0.188 (n=392)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 11.493 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.243` → IC=+0.145 (n=1793)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.243 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.2068` → IC=+0.159 (n=2064)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2068 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.0937` → IC=+0.147 (n=1753)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.0937 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.4999` → IC=+0.152 (n=1944)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4999 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.4236` → IC=+0.145 (n=1944)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.4236 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `201.0` → IC=+0.177 (n=626)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 201.0 (IC base=+0.144)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.243 (n=744)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.3996` → IC=+0.226 (n=1958)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3996 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.236 (n=816)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=1151)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.414` → IC=+0.302 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.414 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` < `0.0994` → IC=+0.215 (n=1909)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0994 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.3534` → IC=+0.231 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3534 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.7691` → IC=+0.214 (n=950)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7691 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `2.7105` → IC=+0.229 (n=978)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7105 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=2661)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `1955.62` → IC=+0.228 (n=1009)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1955.62 (IC base=+0.215)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.245 (n=1674)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.5685` → IC=+0.250 (n=1902)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5685 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.281 (n=718)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0099` → IC=+0.301 (n=837)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0099 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.432` → IC=+0.271 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.432 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.3556` → IC=+0.276 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3556 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.7474` → IC=+0.237 (n=800)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7474 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.7396` → IC=+0.237 (n=824)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7396 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2039.5984` → IC=+0.242 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2039.5984 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.235 (n=1219)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.234)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.210 (n=942)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.0764` → IC=+0.198 (n=713)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.0764 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=2220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.3126` → IC=+0.213 (n=2137)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3126 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1464` → IC=+0.199 (n=1309)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1464 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.733` → IC=+0.203 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.733 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.0223` → IC=+0.158 (n=1881)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.0223 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1034` → IC=+0.179 (n=878)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1034 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.8232` → IC=+0.151 (n=1397)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.8232 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `2.5068` → IC=+0.169 (n=698)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.5068 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `4577.4727` → IC=+0.184 (n=1425)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 4577.4727 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `138.0` → IC=+0.158 (n=2077)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 138.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.155 (n=2230)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0072 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.3949` → IC=+0.145 (n=2227)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3949 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=1057)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.684` → IC=+0.187 (n=2227)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.684 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` < `0.1544` → IC=+0.156 (n=2219)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1544 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.609` → IC=+0.160 (n=551)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 9.609 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.8556` → IC=+0.156 (n=1485)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8556 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.3002` → IC=+0.192 (n=336)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.3002 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.8098` → IC=+0.136 (n=1392)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.8098 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.554` → IC=+0.130 (n=696)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.554 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `7435.6637` → IC=+0.190 (n=1010)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 7435.6637 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `67.0` → IC=+0.152 (n=900)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 67.0 (IC base=+0.127)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.179 (n=1087)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0104 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.174 (n=1144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 15.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` > `0.4909` → IC=+0.218 (n=2393)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4909 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.197` → IC=+0.193 (n=1398)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.197 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.526` → IC=+0.282 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.526 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `1.1755` → IC=+0.145 (n=2393)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1755 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` < `0.1612` → IC=+0.136 (n=2428)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.1612 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.4382` → IC=+0.151 (n=774)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4382 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.132 (n=2507)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `2758.2723` → IC=+0.208 (n=1085)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2758.2723 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.163 (n=740)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 19.0 (IC base=+0.130)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.138 (n=2439)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0108 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1081` → IC=+0.171 (n=813)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1081 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=2483)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.219 (n=2439)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.1983` → IC=+0.149 (n=2303)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1983 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.845` → IC=+0.124 (n=373)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 8.845 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.461` → IC=+0.132 (n=2155)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 2.461 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.1776` → IC=+0.130 (n=2438)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1776 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2754` → IC=+0.149 (n=326)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.2754 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4448` → IC=+0.130 (n=758)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.4448 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `2.4248` → IC=+0.134 (n=758)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.4248 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2646.1014` → IC=+0.190 (n=1105)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2646.1014 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.130 (n=1990)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 42.0 (IC base=+0.120)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.245 (n=1978)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0131 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.1287` → IC=+0.242 (n=739)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1287 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.227 (n=2299)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.227 (n=1991)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.66` → IC=+0.258 (n=2216)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.66 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` > `1.259` → IC=+0.234 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.259 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` < `0.4795` → IC=+0.223 (n=1971)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4795 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.613` → IC=+0.251 (n=1005)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.613 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `1.1809` → IC=+0.225 (n=2216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1809 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `0.619` → IC=+0.232 (n=2214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.619 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.2831` → IC=+0.273 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2831 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `2.47` → IC=+0.228 (n=2155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.47 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `1.8092` → IC=+0.233 (n=1437)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8092 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `2954.7944` → IC=+0.226 (n=738)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2954.7944 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.233 (n=986)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.229)

- **PATRÓN** `sigma_h` > `0.0226` → IC=+0.239 (n=1015)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0226 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.0884` → IC=+0.262 (n=747)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0884 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.248 (n=1091)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.229)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.230 (n=999)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` < `0.43` → IC=+0.257 (n=2242)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.43 (IC base=+0.229)

- **PATRÓN** `dist_vwap_pct` > `0.2966` → IC=+0.237 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2966 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.319` → IC=+0.261 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.319 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` > `0.6385` → IC=+0.236 (n=2238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6385 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.28` → IC=+0.285 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.28 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `1.4386` → IC=+0.232 (n=2083)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4386 (IC base=+0.229)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.208 (n=1487)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.183)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.192 (n=1128)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0089 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.13` → IC=+0.202 (n=1486)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.13 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.216 (n=1675)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.4901` → IC=+0.218 (n=3013)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4901 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.7975` → IC=+0.203 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7975 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.617` → IC=+0.212 (n=1461)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.617 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.8632` → IC=+0.205 (n=2023)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8632 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` > `0.6962` → IC=+0.187 (n=2710)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.6962 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.1` → IC=+0.194 (n=1208)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` < `1.4295` → IC=+0.197 (n=1093)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4295 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.4856` → IC=+0.188 (n=1093)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.4856 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.190 (n=3811)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `2674.4599` → IC=+0.190 (n=3013)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2674.4599 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.134 (n=1214)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0038 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.3846` → IC=+0.161 (n=2423)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.3846 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.125 (n=1557)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 27.0 (IC base=+0.088)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.207 (n=411)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.3259` → IC=+0.202 (n=934)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3259 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.207 (n=852)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.6364` → IC=+0.238 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6364 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.3081` → IC=+0.202 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3081 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.088` → IC=+0.197 (n=401)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 3.088 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.112` → IC=+0.180 (n=898)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 4.112 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.8753` → IC=+0.206 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8753 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.0712` → IC=+0.185 (n=369)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.0712 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `2.1976` → IC=+0.189 (n=804)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.1976 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `1.4097` → IC=+0.181 (n=914)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.4097 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `14694.0598` → IC=+0.185 (n=623)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 14694.0598 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `159.0` → IC=+0.210 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 159.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.186 (n=371)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0028 (IC base=+0.114)

- **PATRÓN** `drift_60min` |x|≤ `0.2687` → IC=+0.140 (n=978)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.2687 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.126 (n=1009)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 7.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.6326` → IC=+0.164 (n=978)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.6326 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` > `1.07` → IC=+0.142 (n=504)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.07 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.1607` → IC=+0.163 (n=295)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.1607 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `2.1209` → IC=+0.128 (n=966)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 2.1209 (IC base=+0.114)

- **PATRÓN** `ballena_activa_n` < `221.0` → IC=+0.161 (n=721)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 221.0 (IC base=+0.114)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.247 (n=693)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.212)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.212 (n=349)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.2086` → IC=+0.225 (n=693)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2086 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.229 (n=1091)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.3797` → IC=+0.255 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3797 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.2147` → IC=+0.220 (n=919)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2147 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.869` → IC=+0.243 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.869 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `0.836` → IC=+0.227 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.836 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `1.1643` → IC=+0.219 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1643 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.2665` → IC=+0.259 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2665 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.4224` → IC=+0.236 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4224 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.4608` → IC=+0.227 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4608 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.1053` → IC=+0.165 (n=350)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.1053 (IC base=+0.064)

- **PATRÓN** `libro_liquidez` > `5942.5327` → IC=+0.131 (n=698)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 5942.5327 (IC base=+0.064)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.197 (n=282)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0108 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.5286` → IC=+0.170 (n=843)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.5286 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.224 (n=407)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.273 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.9868` → IC=+0.242 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9868 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.059` → IC=+0.237 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.059 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `1.0562` → IC=+0.185 (n=742)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 1.0562 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `0.7125` → IC=+0.178 (n=753)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.7125 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.1626` → IC=+0.195 (n=231)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1626 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.4446` → IC=+0.189 (n=271)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.4446 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.1747` → IC=+0.173 (n=368)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.1747 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.178 (n=872)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.02 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `3022.9855` → IC=+0.185 (n=281)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 3022.9855 (IC base=+0.169)

- **PATRÓN** `ibs_20min` < `0.5484` → IC=+0.136 (n=800)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.5484 (IC base=+0.056)

- **PATRÓN** `libro_liquidez` > `2693.1185` → IC=+0.142 (n=412)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2693.1185 (IC base=+0.056)

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
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.223 (n=7766)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=17854)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` > `0.4483` → IC=+0.232 (n=17127)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4483 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` > `0.901` → IC=+0.213 (n=2139)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.901 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.247` → IC=+0.255 (n=4185)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.247 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` < `1.2227` → IC=+0.170 (n=11481)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.2227 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.2905` → IC=+0.208 (n=2284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2905 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `2.6132` → IC=+0.198 (n=5553)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.6132 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `1786.9908` → IC=+0.185 (n=17124)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 1786.9908 (IC base=+0.184)

- **PATRÓN** `ballena_activa_n` < `112.0` → IC=+0.205 (n=15770)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 112.0 (IC base=+0.184)

- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.193 (n=10321)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0074 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.4902` → IC=+0.192 (n=15478)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.4902 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=5737)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.5838` → IC=+0.242 (n=15481)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5838 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` < `0.1768` → IC=+0.171 (n=9436)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1768 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.809` → IC=+0.204 (n=2147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.809 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.561` → IC=+0.190 (n=14969)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 3.561 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `0.7048` → IC=+0.163 (n=4594)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.7048 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.2903` → IC=+0.253 (n=2090)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2903 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.2574` → IC=+0.196 (n=6641)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.2574 (IC base=+0.187)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.216 (n=9714)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.187)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.229 (n=933)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.3479` → IC=+0.230 (n=2794)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3479 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.239 (n=1357)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.228 (n=1878)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.328 (n=1111)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.433` → IC=+0.356 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.433 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2321` → IC=+0.286 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2321 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `2.2907` → IC=+0.238 (n=1217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2907 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.243 (n=2990)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2075.005` → IC=+0.230 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2075.005 (IC base=+0.226)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.248 (n=1708)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.266 (n=2374)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0086 (IC base=+0.262)

- **PATRÓN** `drift_60min` |x|≤ `0.1194` → IC=+0.287 (n=1043)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1194 (IC base=+0.262)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.268 (n=2174)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.262)

- **PATRÓN** `ibs_20min` < `0.5118` → IC=+0.287 (n=2370)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5118 (IC base=+0.262)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.135` → IC=+0.265 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.135 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` < `0.0953` → IC=+0.262 (n=2132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0953 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` > `0.2867` → IC=+0.293 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2867 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` < `1.5574` → IC=+0.267 (n=989)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5574 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` > `2.6397` → IC=+0.271 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6397 (IC base=+0.262)

- **PATRÓN** `libro_liquidez` > `1620.9224` → IC=+0.272 (n=2117)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1620.9224 (IC base=+0.262)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.271 (n=993)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.262)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.199 (n=925)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.1043` → IC=+0.166 (n=1221)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1043 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=2894)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.3667` → IC=+0.224 (n=2479)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3667 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1275` → IC=+0.197 (n=1438)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1275 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.547` → IC=+0.162 (n=456)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.547 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.174` → IC=+0.154 (n=2422)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 3.174 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.63` → IC=+0.175 (n=925)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.63 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.0722` → IC=+0.153 (n=2474)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0722 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2719` → IC=+0.186 (n=399)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2719 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.179` → IC=+0.159 (n=2388)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.179 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.5284` → IC=+0.157 (n=2425)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.5284 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `239.0` → IC=+0.186 (n=889)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 239.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.165 (n=2313)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.2558` → IC=+0.164 (n=2035)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.2558 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=865)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.6967` → IC=+0.197 (n=2312)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.6967 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.1406` → IC=+0.164 (n=2160)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1406 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.229` → IC=+0.154 (n=383)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 11.229 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.461` → IC=+0.143 (n=2329)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 6.461 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.1974` → IC=+0.153 (n=2312)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1974 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2172` → IC=+0.198 (n=431)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2172 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `2.4301` → IC=+0.151 (n=2207)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4301 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.7751` → IC=+0.153 (n=1471)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.7751 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=3003)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `274.0` → IC=+0.159 (n=932)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 274.0 (IC base=+0.143)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.260 (n=951)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=2981)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2555)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=1068)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.293` → IC=+0.326 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.293 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` < `0.1319` → IC=+0.231 (n=2670)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1319 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `3.1781` → IC=+0.244 (n=923)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1781 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=3406)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `1816.8776` → IC=+0.234 (n=1900)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1816.8776 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.244 (n=2350)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.1802` → IC=+0.259 (n=1175)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1802 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.262 (n=999)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.241 (n=947)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0333` → IC=+0.307 (n=891)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0333 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.603` → IC=+0.297 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.603 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3447` → IC=+0.301 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3447 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1309` → IC=+0.249 (n=1694)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1309 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.244 (n=1410)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1949.24` → IC=+0.253 (n=1210)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1949.24 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.256 (n=1152)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.240)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.206 (n=987)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.4224` → IC=+0.159 (n=2946)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4224 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=3059)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.2464` → IC=+0.194 (n=2946)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.2464 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.143` → IC=+0.173 (n=1577)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.143 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.122` → IC=+0.161 (n=1194)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 4.122 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.8648` → IC=+0.167 (n=1964)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8648 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.188 (n=383)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.5241` → IC=+0.164 (n=1265)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.5241 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `2.1748` → IC=+0.158 (n=1303)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.1748 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `5924.4134` → IC=+0.241 (n=1336)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5924.4134 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.171 (n=1242)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 73.0 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.151 (n=2439)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0075 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.4369` → IC=+0.140 (n=2437)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4369 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.156 (n=884)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.7358` → IC=+0.184 (n=2437)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.7358 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.1494` → IC=+0.145 (n=2212)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1494 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.104` → IC=+0.169 (n=373)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 11.104 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.6971` → IC=+0.144 (n=1073)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6971 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2956` → IC=+0.220 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2956 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `2.2235` → IC=+0.132 (n=2062)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.2235 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `1.4309` → IC=+0.136 (n=2343)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4309 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `7126.9264` → IC=+0.210 (n=812)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7126.9264 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `130.0` → IC=+0.131 (n=2082)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 130.0 (IC base=+0.129)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.163 (n=1346)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0103 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.180 (n=1087)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.4444` → IC=+0.200 (n=2961)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4444 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `1.0577` → IC=+0.207 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0577 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.709` → IC=+0.265 (n=750)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.709 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `1.2218` → IC=+0.137 (n=2961)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.2218 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` < `0.1623` → IC=+0.126 (n=3079)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1623 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.133 (n=382)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.5717` → IC=+0.132 (n=1273)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.5717 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.1924` → IC=+0.128 (n=1311)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 2.1924 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.131 (n=3080)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `2490.3844` → IC=+0.229 (n=1342)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2490.3844 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.144 (n=946)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 24.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.152 (n=2466)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.01 (IC base=+0.116)

- **PATRÓN** `drift_60min` |x|≤ `0.1341` → IC=+0.153 (n=935)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1341 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.129 (n=2890)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.65` → IC=+0.211 (n=2804)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.65 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` < `0.2138` → IC=+0.135 (n=2420)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.2138 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.243` → IC=+0.134 (n=2697)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 3.243 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `0.7104` → IC=+0.138 (n=1233)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.7104 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.2244` → IC=+0.174 (n=476)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2244 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `1.4386` → IC=+0.150 (n=875)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4386 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `2667.7367` → IC=+0.205 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2667.7367 (IC base=+0.116)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.131 (n=2319)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 47.0 (IC base=+0.116)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0138` → IC=+0.253 (n=2503)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0138 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.238 (n=2926)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.235 (n=2024)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` > `0.6111` → IC=+0.273 (n=2503)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6111 (IC base=+0.232)

- **PATRÓN** `dist_vwap_pct` > `0.1912` → IC=+0.249 (n=1535)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1912 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.725` → IC=+0.273 (n=938)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.725 (IC base=+0.232)

- **PATRÓN** `volumen_regimen` < `1.2312` → IC=+0.238 (n=2801)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2312 (IC base=+0.232)

- **PATRÓN** `volumen_regimen` > `0.6399` → IC=+0.236 (n=2801)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6399 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.2872` → IC=+0.262 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2872 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.4995` → IC=+0.253 (n=909)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4995 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.234 (n=3639)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `2956.7282` → IC=+0.239 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2956.7282 (IC base=+0.232)

- **PATRÓN** `sigma_h` > `0.0255` → IC=+0.252 (n=964)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0255 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.237 (n=2723)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` < `0.5155` → IC=+0.265 (n=2891)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5155 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.201` → IC=+0.266 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.201 (IC base=+0.231)

- **PATRÓN** `volumen_regimen` > `1.2292` → IC=+0.259 (n=965)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2292 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.282` → IC=+0.297 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.282 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` > `1.432` → IC=+0.233 (n=2688)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.432 (IC base=+0.231)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.194 (n=5031)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.245 (n=1736)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.5103` → IC=+0.221 (n=5191)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5103 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.227 (n=1878)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.9412` → IC=+0.250 (n=1732)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9412 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` > `0.1722` → IC=+0.212 (n=1953)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1722 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` < `0.4352` → IC=+0.214 (n=3709)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4352 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.983` → IC=+0.220 (n=851)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.983 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.592` → IC=+0.212 (n=4622)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.592 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` < `0.7054` → IC=+0.224 (n=1663)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7054 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` < `0.1071` → IC=+0.211 (n=4854)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1071 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.1669` → IC=+0.223 (n=1460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1669 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.4558` → IC=+0.218 (n=1705)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4558 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.8484` → IC=+0.212 (n=3406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8484 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.216 (n=3991)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `3743.9504` → IC=+0.219 (n=3461)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3743.9504 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.240 (n=1262)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.49` → IC=+0.209 (n=3785)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.49 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=1273)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.209 (n=1683)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.7337` → IC=+0.199 (n=3786)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7337 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.6725` → IC=+0.202 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6725 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` < `0.2409` → IC=+0.190 (n=3454)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.2409 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.821` → IC=+0.203 (n=3395)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.821 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `1.0959` → IC=+0.202 (n=3160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0959 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.198 (n=3473)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2228` → IC=+0.194 (n=763)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2228 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `1.5334` → IC=+0.199 (n=1641)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.5334 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.1921` → IC=+0.201 (n=1691)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1921 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.194 (n=5031)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.193)

- **PATRÓN** `ballena_activa_n` < `169.0` → IC=+0.203 (n=3275)

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
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.198 (n=359)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.007 (IC base=+0.192)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.213 (n=368)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0105 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.5854` → IC=+0.205 (n=812)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5854 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=286)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` < `0.7044` → IC=+0.195 (n=542)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.7044 (IC base=+0.192)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.238 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.488` → IC=+0.231 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.488 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` > `0.2095` → IC=+0.240 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2095 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `2.8783` → IC=+0.210 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8783 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `2532.1516` → IC=+0.219 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2532.1516 (IC base=+0.192)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.194 (n=547)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 10.0 (IC base=+0.192)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.229 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.275 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.227)

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
- **PATRÓN** `sigma_h` < `0.008` → IC=+0.214 (n=1379)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.4596` → IC=+0.205 (n=1379)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4596 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=501)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` < `0.5211` → IC=+0.209 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5211 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `0.8784` → IC=+0.199 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8784 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` < `0.4078` → IC=+0.211 (n=1376)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4078 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.112` → IC=+0.206 (n=1240)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.112 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `0.8778` → IC=+0.202 (n=920)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8778 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` > `1.2314` → IC=+0.203 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2314 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` < `0.105` → IC=+0.201 (n=1268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.105 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.1638` → IC=+0.197 (n=411)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1638 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `1.4147` → IC=+0.217 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4147 (IC base=+0.197)

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
- **PATRÓN** `sigma_h` < `0.011` → IC=+0.204 (n=678)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.210 (n=737)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` > `0.9259` → IC=+0.249 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9259 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` > `0.743` → IC=+0.243 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.743 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.222` → IC=+0.206 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.222 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `0.6991` → IC=+0.230 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6991 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` < `0.1062` → IC=+0.196 (n=695)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.1062 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.0788` → IC=+0.195 (n=342)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0788 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `1.5649` → IC=+0.195 (n=329)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.5649 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `2.4746` → IC=+0.213 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4746 (IC base=+0.185)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.189 (n=898)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.02 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `2931.085` → IC=+0.200 (n=770)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2931.085 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.200 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.185)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.213 (n=378)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.205)

- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.207 (n=189)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.6042` → IC=+0.225 (n=566)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6042 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.241 (n=384)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` < `0.7273` → IC=+0.227 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7273 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.8337` → IC=+0.209 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8337 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.3056` → IC=+0.208 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3056 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.862` → IC=+0.212 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.862 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `1.1314` → IC=+0.210 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1314 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `0.9354` → IC=+0.210 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9354 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` < `0.1067` → IC=+0.226 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1067 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `2.2063` → IC=+0.238 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2063 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `3012.3318` → IC=+0.222 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3012.3318 (IC base=+0.205)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.248 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.205)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.160 (n=753)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.004 (IC base=+0.072)

- **PATRÓN** `ibs_20min` > `0.3889` → IC=+0.145 (n=1621)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.3889 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` > `0.1486` → IC=+0.147 (n=853)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1486 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.919` → IC=+0.157 (n=470)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 8.919 (IC base=+0.072)

- **PATRÓN** `volumen_pendiente_norm` > `0.2755` → IC=+0.148 (n=225)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2755 (IC base=+0.072)

- **PATRÓN** `ibs_20min` < `0.2193` → IC=+0.219 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2193 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.336` → IC=+0.164 (n=144)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 10.336 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.1466` → IC=+0.163 (n=250)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.1466 (IC base=+0.053)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.134 (n=566)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0056 (IC base=+0.093)

- **PATRÓN** `ibs_20min` > `0.3563` → IC=+0.170 (n=535)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.3563 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.1276` → IC=+0.163 (n=271)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1276 (IC base=+0.093)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.121 (n=283)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0037 (IC base=+0.068)

- **PATRÓN** `ibs_20min` < `0.0602` → IC=+0.275 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0602 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.2135` → IC=+0.192 (n=76)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2135 (IC base=+0.068)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.6934` → IC=-0.184 (n=96)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6934
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=289)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.126 (n=493)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.006 (IC base=+0.091)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.149 (n=212)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.091)

- **PATRÓN** `ibs_20min` > `0.4221` → IC=+0.174 (n=528)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.4221 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `0.1247` → IC=+0.192 (n=274)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1247 (IC base=+0.091)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.194` → IC=+0.237 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.194 (IC base=+0.091)

- **PATRÓN** `volumen_pendiente_norm` > `0.2871` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.2871 (IC base=+0.091)

- **PATRÓN** `ibs_20min` < `0.0289` → IC=+0.278 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0289 (IC base=+0.017)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.617` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.617 (IC base=+0.017)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` > `0.16` → IC=-0.204 (n=69)

  - _Acción_: SKIP cuando `ibs_20min` > 0.16
  - _Potencial_: sin este filtro IC_bueno=+0.218 (n=211)

- **PATRÓN** `ibs_20min` > `0.7458` → IC=+0.168 (n=372)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.7458 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` > `0.4722` → IC=+0.137 (n=199)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.4722 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.265` → IC=+0.158 (n=118)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 9.265 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.2283` → IC=+0.139 (n=106)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.2283 (IC base=+0.035)

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
- **FILTRO** `hora_utc` > `8.0` → IC=-0.324 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.165 (n=249)

- **FILTRO** `dist_vwap_pct` > `0.2316` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2316
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=298)

- **FILTRO** `volumen_spike_ratio` > `2.8031` → IC=-0.210 (n=60)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.8031
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=181)

- **FILTRO** `libro_liquidez` < `891.5381` → IC=-0.225 (n=78)

  - _Acción_: SKIP cuando `libro_liquidez` < 891.5381
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=237)

- **FILTRO** `drift_60min` |x|> `0.1941` → IC=-0.321 (n=65)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1941
  - _Potencial_: sin este filtro IC_bueno=-0.270 (n=198)

- **FILTRO** `ibs_20min` > `0.5429` → IC=-0.331 (n=134)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5429
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=135)

- **FILTRO** `dist_vwap_pct` > `0.4497` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4497
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=250)

- **FILTRO** `sigma_ewma_delta_pct` > `10.342` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 10.342
  - _Potencial_: sin este filtro IC_bueno=-0.284 (n=243)

- **FILTRO** `volumen_pendiente_norm` > `0.0448` → IC=-0.379 (n=31)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0448
  - _Potencial_: sin este filtro IC_bueno=-0.273 (n=152)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `volumen_regimen` < `1.2175` → IC=-0.284 (n=49)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2175
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=49)

- **FILTRO** `sigma_h` > `0.0043` → IC=-0.339 (n=29)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0043
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=91)

- **FILTRO** `volumen_regimen` > `0.8276` → IC=-0.371 (n=29)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8276
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=91)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.5786` → IC=-0.464 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5786
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=79)

- **FILTRO** `sigma_h` > `0.0048` → IC=-0.352 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.272 (n=77)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.375 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.268 (n=80)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=87)

- **FILTRO** `libro_liquidez` < `1599.2889` → IC=-0.311 (n=51)

  - _Acción_: SKIP cuando `libro_liquidez` < 1599.2889
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

- **FILTRO** `volumen_spike_ratio` > `2.3736` → IC=-0.242 (n=29)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.3736
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=58)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.242 (n=29)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=83)

- **FILTRO** `sigma_h` < `0.006` → IC=-0.324 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.006
  - _Potencial_: sin este filtro IC_bueno=-0.294 (n=32)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=32)

- **FILTRO** `volumen_regimen` < `0.9949` → IC=-0.420 (n=23)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9949
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=24)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.1535` → IC=-0.120 (n=285)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1535
  - _Potencial_: sin este filtro IC_bueno=+0.141 (n=555)

- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.200 (n=245)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.184 (n=245)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 16.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.6875` → IC=+0.157 (n=540)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.6875 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.5388` → IC=+0.234 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5388 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.077` → IC=+0.130 (n=125)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 11.077 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.6195` → IC=+0.189 (n=181)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.6195 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1529` → IC=+0.155 (n=445)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.1529 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.415` → IC=+0.182 (n=146)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.415 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.1535` → IC=+0.141 (n=555)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.1535 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.159` → IC=+0.185 (n=144)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 11.159 (IC base=+0.052)

- **PATRÓN** `libro_liquidez` > `3256.3999` → IC=+0.130 (n=420)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 3256.3999 (IC base=+0.052)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6946` → IC=-0.190 (n=56)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6946
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=168)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.183 (n=99)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0049 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.140 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 12.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.149 (n=112)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 6.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.1681` → IC=+0.194 (n=295)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.1681 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.216` → IC=+0.162 (n=128)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 7.216 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` > `0.6194` → IC=+0.146 (n=295)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.6194 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` < `0.0706` → IC=+0.141 (n=232)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` < 0.0706 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2726` → IC=+0.167 (n=49)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2726 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `2.5184` → IC=+0.162 (n=264)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.5184 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.4429` → IC=+0.147 (n=264)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4429 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `5391.3885` → IC=+0.138 (n=197)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 5391.3885 (IC base=+0.130)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1263` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1263
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=178)

- **FILTRO** `ibs_20min` > `0.327` → IC=-0.167 (n=76)

  - _Acción_: SKIP cuando `ibs_20min` > 0.327
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=231)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.141 (n=126)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0039 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.196 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=+0.103)

- **PATRÓN** `ibs_20min` > `0.9094` → IC=+0.161 (n=125)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.9094 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` < `0.0943` → IC=+0.135 (n=157)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.0943 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.015` → IC=+0.148 (n=140)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 3.015 (IC base=+0.103)

- **PATRÓN** `volumen_regimen` < `0.6195` → IC=+0.192 (n=63)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.6195 (IC base=+0.103)

- **PATRÓN** `volumen_pendiente_norm` < `0.1263` → IC=+0.150 (n=178)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.1263 (IC base=+0.103)

- **PATRÓN** `volumen_spike_ratio` < `1.7963` → IC=+0.179 (n=107)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.7963 (IC base=+0.103)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=159)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.957` → IC=+0.232 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.957 (IC base=+0.018)

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

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.318 (n=124)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` > `0.6522` → IC=+0.282 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6522 (IC base=+0.258)

- **PATRÓN** `dist_vwap_pct` > `0.6667` → IC=+0.394 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6667 (IC base=+0.258)

- **PATRÓN** `dist_vwap_pct` < `0.2335` → IC=+0.262 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2335 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.318` → IC=+0.323 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.318 (IC base=+0.258)

- **PATRÓN** `volumen_regimen` < `0.5792` → IC=+0.328 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5792 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.1037` → IC=+0.341 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1037 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` < `1.4815` → IC=+0.400 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4815 (IC base=+0.258)

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
- **PATRÓN** `libro_liquidez` > `2944.9354` → IC=+0.137 (n=425)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2944.9354 (IC base=+0.103)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2944.9354` → IC=+0.137 (n=425)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2944.9354 (IC base=+0.103)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=196)

- **FILTRO** `libro_liquidez` < `5350.5492` → IC=-0.167 (n=106)

  - _Acción_: SKIP cuando `libro_liquidez` < 5350.5492
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=106)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=317)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `10893.2451` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 10893.2451
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=71)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=39)

- **PATRÓN** `liq_n` > `6.0` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `liq_n` > 6.0 (IC base=+0.008)

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
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=3561)

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
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=1326)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=1280)

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
- **FILTRO** `py_entrada` > `0.505` → IC=-0.140 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=709)

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
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=844)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=844)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.134 (n=260)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=664)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=845)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=845)

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
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=241)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=265)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=258)

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
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=261)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.129 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=189)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.145 (n=60)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=35)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.204 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.132 (n=17)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.121 (n=238)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=275)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.45` → IC=+0.175 (n=149)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.45 (IC base=+0.018)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.178 (n=57)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=262)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.137 (n=155)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=177)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` < 0.5 (IC base=+0.052)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.122 (n=318)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=174)

- **FILTRO** `profundidad_ratio` < `58.4` → IC=-0.146 (n=162)

  - _Acción_: SKIP cuando `profundidad_ratio` < 58.4
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=330)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.142 (n=205)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=233)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.159 (n=89)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=382)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.149 (n=129)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=470)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.163 (n=6131)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=19008)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.178 (n=6234)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=19536)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.193 (n=1120)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=3465)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.174 (n=1065)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=3535)

- **PATRÓN** `py_entrada` > `0.495` → IC=+0.129 (n=3093)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` > 0.495 (IC base=+0.042)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.144 (n=1210)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 1.0 (IC base=+0.042)

- **PATRÓN** `libro_liquidez` > `1282.98` → IC=+0.136 (n=2293)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 1282.98 (IC base=+0.042)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.127 (n=2150)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.5 (IC base=+0.011)

- **PATRÓN** `libro_liquidez` > `1473.076` → IC=+0.153 (n=1564)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1473.076 (IC base=+0.011)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.151 (n=854)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=2814)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.177 (n=896)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=2753)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.205 (n=1095)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=3606)

- **PATRÓN** `ibs_20min` > `0.965` → IC=+0.133 (n=1560)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 0.965 (IC base=+0.039)

- **PATRÓN** `libro_liquidez` > `1525.4289` → IC=+0.120 (n=2294)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 1525.4289 (IC base=+0.039)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.155 (n=1111)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=3474)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2400)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2324)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2817)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=3557)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=445)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.257 (n=142)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=428)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.234 (n=287)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=890)

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

- **FILTRO** `ibs_20min` > `0.9798` → IC=-0.188 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` > 0.9798
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=331)

- **FILTRO** `libro_liquidez` < `3728.8927` → IC=-0.167 (n=220)

  - _Acción_: SKIP cuando `libro_liquidez` < 3728.8927
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=221)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=938)

- **FILTRO** `libro_liquidez` < `1784.2378` → IC=-0.164 (n=239)

  - _Acción_: SKIP cuando `libro_liquidez` < 1784.2378
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=718)

- **FILTRO** `libro_liquidez` < `2089.8344` → IC=-0.170 (n=349)

  - _Acción_: SKIP cuando `libro_liquidez` < 2089.8344
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=710)

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
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=38646)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.285 (n=13756)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=42136)

- **FILTRO** `ibs_7min` < `0.2368` → IC=-0.228 (n=13970)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2368
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=41922)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.152 (n=18582)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=37310)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.242 (n=17262)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=52931)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.182 (n=17380)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=52813)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.148 (n=2787)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=6997)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.311 (n=2332)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=7452)

- **FILTRO** `ibs_7min` < `0.7133` → IC=-0.244 (n=3228)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7133
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=6556)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.180 (n=2051)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=7733)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.272 (n=3026)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=9147)

- **FILTRO** `ibs_7min` > `0.7708` → IC=-0.212 (n=3043)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7708
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=9130)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.128 (n=2255)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=7171)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.265 (n=2207)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=7219)

- **FILTRO** `ibs_7min` < `0.7258` → IC=-0.199 (n=2355)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7258
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=7071)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.190 (n=2340)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=7086)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.263 (n=2358)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=7207)

- **FILTRO** `ibs_7min` > `0.2678` → IC=-0.195 (n=2390)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2678
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=7175)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.184 (n=2372)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=7193)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.158 (n=2281)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=7001)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.312 (n=2282)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=7000)

- **FILTRO** `ibs_7min` < `0.296` → IC=-0.245 (n=3063)

  - _Acción_: SKIP cuando `ibs_7min` < 0.296
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=6219)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.194 (n=2200)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=7082)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.255 (n=3025)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=9919)

- **FILTRO** `ibs_7min` > `0.7338` → IC=-0.178 (n=3235)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7338
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=9709)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.124 (n=2962)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=6147)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.261 (n=2134)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=6975)

- **FILTRO** `ibs_7min` < `0.728` → IC=-0.186 (n=2277)

  - _Acción_: SKIP cuando `ibs_7min` < 0.728
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6832)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.188 (n=2243)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6866)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.268 (n=2132)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=7294)

- **FILTRO** `ibs_7min` > `0.2753` → IC=-0.178 (n=2356)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2753
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=7070)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.178 (n=2304)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=7122)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.283 (n=2201)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=6953)

- **FILTRO** `ibs_7min` < `0.7143` → IC=-0.221 (n=2944)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=6210)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.218 (n=2208)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=6946)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.191 (n=3264)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=10139)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.292 (n=2160)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=6977)

- **FILTRO** `ibs_7min` < `0.2` → IC=-0.222 (n=2268)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=6869)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.198 (n=2274)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=6863)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.218 (n=3114)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=9568)

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
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=496)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.152 (n=156)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=549)

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
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=333)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.143 (n=166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=328)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=445)

- **FILTRO** `libro_liquidez` < `3244.1491` → IC=-0.156 (n=178)

  - _Acción_: SKIP cuando `libro_liquidez` < 3244.1491
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=536)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=387)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.138 (n=1176)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.133 (n=609)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 6.0 (IC base=+0.128)

- **PATRÓN** `total_vol_5m` < `436.8284` → IC=+0.152 (n=392)

  - _Acción_: Kelly boost +0.76€ cuando `total_vol_5m` < 436.8284 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `3627.2442` → IC=+0.150 (n=533)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3627.2442 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.147 (n=386)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 11.0 (IC base=+0.128)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4377` → IC=+0.149 (n=92)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio` |x|> 0.4377 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.193 (n=135)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 14.0 (IC base=+0.133)

- **PATRÓN** `total_vol_5m` < `375.759` → IC=+0.143 (n=242)

  - _Acción_: Kelly boost +0.72€ cuando `total_vol_5m` < 375.759 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `2558.8539` → IC=+0.202 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2558.8539 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.145 (n=105)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 7.0 (IC base=+0.133)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3994` → IC=+0.135 (n=242)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.3994 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.135 (n=217)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 14.0 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.127 (n=290)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.04 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2349.306` → IC=+0.132 (n=161)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2349.306 (IC base=+0.117)

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
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.126 (n=201)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 14.0 (IC base=+0.100)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.179 (n=135)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `3589.6144` → IC=+0.167 (n=100)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3589.6144 (IC base=+0.100)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.9794` → IC=-0.266 (n=45)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.9794
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=139)

- **FILTRO** `sigma_h` > `0.0072` → IC=-0.333 (n=166)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0072
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=501)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.180 (n=167)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0035 (IC base=-0.086)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `87.9936` → IC=-0.245 (n=49)

  - _Acción_: SKIP cuando `T_h` > 87.9936
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=149)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.308 (n=50)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=-0.035)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `pct_vs_K` |x|> `9.8932` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 9.8932
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=49)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0137` → IC=-0.274 (n=29)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0137
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=89)

- **FILTRO** `T_h` < `87.9936` → IC=-0.189 (n=59)

  - _Acción_: SKIP cuando `T_h` < 87.9936
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=59)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0094` → IC=-0.226 (n=407)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=210)

- **FILTRO** `T_h` > `87.6765` → IC=-0.199 (n=413)

  - _Acción_: SKIP cuando `T_h` > 87.6765
  - _Potencial_: sin este filtro IC_bueno=-0.150 (n=204)

- **FILTRO** `sigma_h` > `0.0084` → IC=-0.258 (n=180)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0084
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=350)

- **FILTRO** `T_h` > `54.448` → IC=-0.269 (n=397)

  - _Acción_: SKIP cuando `T_h` > 54.448
  - _Potencial_: sin este filtro IC_bueno=-0.130 (n=133)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `71.159` → IC=-0.176 (n=134)

  - _Acción_: SKIP cuando `T_h` > 71.159
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=67)

- **FILTRO** `pct_vs_K` |x|> `2.7856` → IC=-0.365 (n=50)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7856
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=151)

- **FILTRO** `pct_vs_K` |x|> `2.9891` → IC=-0.436 (n=45)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9891
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=143)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `T_h` < `139.5329` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `T_h` < 139.5329
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `sigma_h` < `0.0078` → IC=-0.262 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0078
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.01` → IC=-0.307 (n=133)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=45)

- **FILTRO** `T_h` > `71.9104` → IC=-0.270 (n=133)

  - _Acción_: SKIP cuando `T_h` > 71.9104
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=45)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.384 (n=41)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=124)

- **FILTRO** `T_h` > `57.7851` → IC=-0.277 (n=110)

  - _Acción_: SKIP cuando `T_h` > 57.7851
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=55)

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
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=129)

- **FILTRO** `T_h` > `94.0115` → IC=-0.224 (n=114)

  - _Acción_: SKIP cuando `T_h` > 94.0115
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=57)

- **FILTRO** `sigma_h` > `0.0135` → IC=-0.357 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0135
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=78)

- **FILTRO** `sigma_h` < `0.0086` → IC=-0.275 (n=38)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0086
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=80)

- **FILTRO** `T_h` > `41.2641` → IC=-0.290 (n=79)

  - _Acción_: SKIP cuando `T_h` > 41.2641
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=39)

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
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=389)

- **PATRÓN** `streak_estiramiento` < `0.8469` → IC=+0.125 (n=262)

  - _Acción_: Kelly boost +0.62€ cuando `streak_estiramiento` < 0.8469 (IC base=+0.048)

- **PATRÓN** `libro_liquidez` > `2526.0042` → IC=+0.143 (n=141)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 2526.0042 (IC base=+0.048)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=27)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=18)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=27)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.000)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `streak_estiramiento` < `0.2566` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `streak_estiramiento` < 0.2566 (IC base=+0.012)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.136 (n=119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 7.0 (IC base=+0.091)

- **PATRÓN** `streak_estiramiento` < `0.4496` → IC=+0.196 (n=100)

  - _Acción_: Kelly boost +0.98€ cuando `streak_estiramiento` < 0.4496 (IC base=+0.091)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.161 (n=110)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 35.0 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `2223.4384` → IC=+0.139 (n=131)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2223.4384 (IC base=+0.091)

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

- **FILTRO** `hora_utc` > `3.0` → IC=-0.140 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

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
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1008)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1330)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=1160)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=1207)

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
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=4069)

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
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=2254)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.197 (n=1229)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0047 (IC base=+0.177)

- **PATRÓN** `sigma_h` > `0.012` → IC=+0.199 (n=1229)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.012 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.1769` → IC=+0.193 (n=3244)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1769 (IC base=+0.177)

- **PATRÓN** `delta_ratio_macro` |x|> `0.191` → IC=+0.179 (n=1672)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.89€ cuando `delta_ratio_macro` |x|> 0.191 (IC base=+0.177)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1332` → IC=+0.186 (n=1475)

  - _Acción_: Kelly boost +0.93€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1332 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=3413)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.180 (n=3395)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.177)

- **PATRÓN** `ibs_15` > `0.5475` → IC=+0.254 (n=3687)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5475 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.1298` → IC=+0.172 (n=1781)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1298 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` < `0.4939` → IC=+0.164 (n=3301)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.4939 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.472` → IC=+0.258 (n=953)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.472 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `4658.9933` → IC=+0.195 (n=1229)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 4658.9933 (IC base=+0.177)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1462)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.254 (n=209)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.0591` → IC=+0.273 (n=209)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0591 (IC base=+0.221)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2541` → IC=+0.248 (n=208)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2541 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.240 (n=626)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.221)

- **PATRÓN** `ibs_15` > `0.7231` → IC=+0.286 (n=624)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7231 (IC base=+0.221)

- **PATRÓN** `dist_vwap_pct` > `0.2448` → IC=+0.241 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2448 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.108` → IC=+0.303 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.108 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.222 (n=810)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `8715.5535` → IC=+0.233 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8715.5535 (IC base=+0.221)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.269` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.269
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=802)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.187 (n=244)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0035 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.0669` → IC=+0.154 (n=322)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.0669 (IC base=+0.144)

- **PATRÓN** `drift_15min` |x|≤ `0.3955` → IC=+0.146 (n=244)

  - _Acción_: Kelly boost +0.73€ cuando `drift_15min` |x|≤ 0.3955 (IC base=+0.144)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1435` → IC=+0.148 (n=487)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio_macro` |x|> 0.1435 (IC base=+0.144)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.129` → IC=+0.161 (n=290)

  - _Acción_: Kelly boost +0.80€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.129 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.154 (n=671)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 6.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.150 (n=763)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 17.0 (IC base=+0.144)

- **PATRÓN** `ibs_15` > `0.537` → IC=+0.239 (n=731)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.537 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1197` → IC=+0.159 (n=455)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1197 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.577` → IC=+0.268 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.577 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `3217.9115` → IC=+0.151 (n=731)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3217.9115 (IC base=+0.144)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `17.774` → IC=-0.192 (n=37)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.774
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=346)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8868` → IC=+0.251 (n=283)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8868 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.128` → IC=+0.171 (n=162)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 17.128 (IC base=+0.096)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=469)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.096)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0239` → IC=+0.231 (n=281)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0239 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.1305` → IC=+0.227 (n=562)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1305 (IC base=+0.203)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0933` → IC=+0.248 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0933 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.214 (n=751)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.203)

- **PATRÓN** `ibs_15` > `0.5294` → IC=+0.278 (n=842)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5294 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.1292` → IC=+0.212 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1292 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.85` → IC=+0.227 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.85 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2959.5982` → IC=+0.291 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2959.5982 (IC base=+0.203)

- **PATRÓN** `ibs_15` < `0.1096` → IC=+0.160 (n=783)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.80€ cuando `ibs_15` < 0.1096 (IC base=+0.067)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.393 (n=213)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.366)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1493` → IC=+0.383 (n=425)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1493 (IC base=+0.366)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1403` → IC=+0.386 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1403 (IC base=+0.366)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.379 (n=643)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.366)

- **PATRÓN** `ibs_15` > `0.7863` → IC=+0.402 (n=638)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7863 (IC base=+0.366)

- **PATRÓN** `dist_vwap_pct` > `0.1477` → IC=+0.384 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1477 (IC base=+0.366)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.239` → IC=+0.387 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.239 (IC base=+0.366)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.370 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.366)

- **PATRÓN** `libro_liquidez` > `3505.1277` → IC=+0.373 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3505.1277 (IC base=+0.366)

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

- **PATRÓN** `delta_ratio_macro` |x|> `0.2158` → IC=+0.387 (n=149)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2158 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1413` → IC=+0.393 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1413 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.383 (n=330)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.8048` → IC=+0.392 (n=330)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8048 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.2485` → IC=+0.393 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2485 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.521` → IC=+0.380 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.521 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `16828.3206` → IC=+0.402 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16828.3206 (IC base=+0.364)

- **PATRÓN** `ballena_activa_n` < `493.0` → IC=+0.408 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 493.0 (IC base=+0.364)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.370 (n=136)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.367)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.387 (n=140)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.367)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.381 (n=276)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.367)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.384 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.367)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.394 (n=149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.367)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.373 (n=140)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.367)

- **PATRÓN** `ibs_15` > `0.7479` → IC=+0.413 (n=309)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7479 (IC base=+0.367)

- **PATRÓN** `dist_vwap_pct` > `0.4613` → IC=+0.395 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4613 (IC base=+0.367)

- **PATRÓN** `dist_vwap_pct` < `0.2948` → IC=+0.368 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2948 (IC base=+0.367)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.889` → IC=+0.393 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.889 (IC base=+0.367)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.371 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.367)

- **PATRÓN** `libro_liquidez` > `4019.374` → IC=+0.394 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4019.374 (IC base=+0.367)

- **PATRÓN** `ballena_activa_n` < `159.0` → IC=+0.378 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 159.0 (IC base=+0.367)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.175 (n=2198)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=2200)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.213 (n=1719)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=2679)

- **PATRÓN** `ibs_15` > `0.6324` → IC=+0.280 (n=1062)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6324 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1122` → IC=+0.205 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1122 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` < `0.2685` → IC=+0.194 (n=904)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.2685 (IC base=-0.068)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2307` → IC=+0.268 (n=1218)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2307 (IC base=-0.014)

- **PATRÓN** `ibs_15` < `0.3605` → IC=+0.282 (n=3651)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3605 (IC base=-0.014)

- **PATRÓN** `dist_vwap_pct` > `0.6583` → IC=+0.274 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6583 (IC base=-0.014)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0341` → IC=-0.225 (n=1933)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0341
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=648)

- **FILTRO** `sigma_ewma_delta_pct` > `23.313` → IC=-0.273 (n=372)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.313
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=2209)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=66)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=2515)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.122 (n=770)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0052 (IC base=+0.096)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1455` → IC=+0.281 (n=231)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1455 (IC base=+0.096)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1125` → IC=+0.274 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1125 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.123 (n=771)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 5.0 (IC base=+0.096)

- **PATRÓN** `ibs_15` > `0.7591` → IC=+0.331 (n=346)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7591 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.1051` → IC=+0.284 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1051 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` < `0.2456` → IC=+0.277 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2456 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.603` → IC=+0.131 (n=385)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 8.603 (IC base=+0.096)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0659` → IC=+0.210 (n=60)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0659 (IC base=-0.196)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1432` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1432 (IC base=-0.196)

- **PATRÓN** `ibs_15` < `0.618` → IC=+0.294 (n=61)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.618 (IC base=-0.196)

- **PATRÓN** `dist_vwap_pct` < `0.0474` → IC=+0.269 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0474 (IC base=-0.196)

- **PATRÓN** `ballena_activa_n` < `291.0` → IC=+0.360 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 291.0 (IC base=-0.196)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=694)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.160 (n=471)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0058 (IC base=+0.148)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.156 (n=356)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0049 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.0544` → IC=+0.189 (n=178)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0544 (IC base=+0.148)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3006` → IC=+0.192 (n=410)

  - _Acción_: Kelly boost +0.96€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3006 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.159 (n=538)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.148)

- **PATRÓN** `ibs_15` > `0.5905` → IC=+0.246 (n=534)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5905 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.4686` → IC=+0.169 (n=140)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.4686 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.1604` → IC=+0.148 (n=418)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1604 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.243` → IC=+0.243 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.243 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=694)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `9633.3802` → IC=+0.156 (n=178)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 9633.3802 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.250 (n=1327)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.244)

- **PATRÓN** `drift_15min` |x|≤ `0.7706` → IC=+0.257 (n=1167)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7706 (IC base=+0.244)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1573` → IC=+0.257 (n=885)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1573 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.248 (n=482)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.248 (n=510)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.244)

- **PATRÓN** `ibs_15` < `0.3707` → IC=+0.274 (n=1327)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3707 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` > `0.6025` → IC=+0.260 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6025 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.434` → IC=+0.255 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.434 (IC base=+0.244)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0105` → IC=-0.246 (n=254)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=764)

- **FILTRO** `drift_60min` |x|> `0.173` → IC=-0.251 (n=344)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.173
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=674)

- **FILTRO** `drift_15min` |x|> `0.888` → IC=-0.285 (n=254)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.888
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=764)

- **FILTRO** `sigma_ewma_delta_pct` > `6.585` → IC=-0.202 (n=236)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.585
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=782)

- **FILTRO** `sigma_ewma_delta_pct` > `17.92` → IC=-0.148 (n=532)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.92
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=4231)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.191)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.191)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.191)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.191)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0814` → IC=+0.235 (n=523)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0814 (IC base=-0.041)

- **PATRÓN** `ibs_15` < `0.3529` → IC=+0.291 (n=588)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3529 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` < `0.4417` → IC=+0.243 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4417 (IC base=-0.041)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0198` → IC=-0.253 (n=605)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0198
  - _Potencial_: sin este filtro IC_bueno=-0.165 (n=606)

- **FILTRO** `sigma_ewma_delta_pct` > `7.379` → IC=-0.213 (n=378)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.379
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=833)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.209)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.209)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0688` → IC=+0.274 (n=782)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0688 (IC base=-0.026)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1165` → IC=+0.294 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1165 (IC base=-0.026)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.292 (n=879)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` > `0.7735` → IC=+0.353 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7735 (IC base=-0.026)

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
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.298 (n=962)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.0533` → IC=+0.320 (n=365)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0533 (IC base=+0.292)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2433` → IC=+0.309 (n=364)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2433 (IC base=+0.292)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.224` → IC=+0.303 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.224 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.308 (n=1141)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.292)

- **PATRÓN** `ibs_15` > `0.8389` → IC=+0.320 (n=1093)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8389 (IC base=+0.292)

- **PATRÓN** `dist_vwap_pct` > `0.2735` → IC=+0.323 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2735 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.52` → IC=+0.378 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.52 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `12266.8327` → IC=+0.315 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12266.8327 (IC base=+0.292)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.313 (n=196)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.289)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.302 (n=266)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0582` → IC=+0.313 (n=196)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0582 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.258` → IC=+0.313 (n=196)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.258 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.307 (n=589)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.83` → IC=+0.315 (n=587)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.83 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.1465` → IC=+0.322 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1465 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.380 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `16178.7073` → IC=+0.333 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16178.7073 (IC base=+0.289)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.305 (n=507)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.0515` → IC=+0.319 (n=169)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0515 (IC base=+0.295)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1458` → IC=+0.300 (n=338)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1458 (IC base=+0.295)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3049` → IC=+0.307 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3049 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.309 (n=521)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.295)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.298 (n=458)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.295)

- **PATRÓN** `ibs_15` > `0.8486` → IC=+0.323 (n=507)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8486 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` > `0.4679` → IC=+0.327 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4679 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.52` → IC=+0.367 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.52 (IC base=+0.295)

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

- **FILTRO** `drift_15min` |x|> `0.3423` → IC=-0.289 (n=17)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3423
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=34)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1941` → IC=-0.241 (n=25)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1941
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=26)

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
- **PATRÓN** `T_h` > `87.7391` → IC=+0.193 (n=490)

  - _Acción_: Kelly boost +0.97€ cuando `T_h` > 87.7391 (IC base=+0.192)

- **PATRÓN** `ratio` < `0.973` → IC=+0.408 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.192)

- **PATRÓN** `T_h` > `115.2222` → IC=+0.352 (n=2232)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 115.2222 (IC base=+0.336)

- **PATRÓN** `ratio` > `1.0229` → IC=+0.374 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0229 (IC base=+0.336)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `109.5528` → IC=+0.178 (n=203)

  - _Acción_: Kelly boost +0.89€ cuando `T_h` > 109.5528 (IC base=+0.161)

- **PATRÓN** `ratio` < `0.983` → IC=+0.332 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.983 (IC base=+0.161)

- **PATRÓN** `T_h` > `111.9824` → IC=+0.302 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9824 (IC base=+0.292)

- **PATRÓN** `ratio` > `1.0189` → IC=+0.333 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0189 (IC base=+0.292)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `83.3501` → IC=+0.234 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.232)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.399 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.232)

- **PATRÓN** `T_h` > `111.9905` → IC=+0.351 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9905 (IC base=+0.324)

- **PATRÓN** `ratio` > `1.0347` → IC=+0.391 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0347 (IC base=+0.324)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0966` → IC=+0.441 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0966 (IC base=+0.399)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5475 sube el IC de +0.177 a +0.254 en UPDOWN_GBM#15min (n=3687). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7231 sube el IC de +0.221 a +0.286 en UPDOWN_GBM#BTC#15min (n=624). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.537 sube el IC de +0.144 a +0.239 en UPDOWN_GBM#ETH#15min (n=731). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.8868 sube el IC de +0.096 a +0.251 en UPDOWN_GBM#SOL#15min (n=283). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5294 sube el IC de +0.203 a +0.278 en UPDOWN_GBM#XRP#15min (n=842). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1096 sube el IC de +0.067 a +0.160 en UPDOWN_GBM#XRP#15min (n=783). Ya aplicado como kelly_boost=+0.80€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6324 sube el IC de -0.068 a +0.280 en UPDOWN_GBM_15M_TARDIO (n=1062). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3605 sube el IC de -0.014 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=3651). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7591 sube el IC de +0.096 a +0.331 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=346). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.618 sube el IC de -0.196 a +0.294 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=61). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5905 sube el IC de +0.148 a +0.246 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=534). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3707 sube el IC de +0.244 a +0.274 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1327). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.191 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3529 sube el IC de -0.041 a +0.291 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=588). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.209 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.026 a +0.292 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=879). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.080 a +0.342 en UPDOWN_GBM_ETH_15M_HORA7 (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.080 a +0.342 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8389 sube el IC de +0.292 a +0.320 en UPDOWN_GBM_IBS_ALTO (n=1093). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.83 sube el IC de +0.289 a +0.315 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=587). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8486 sube el IC de +0.295 a +0.323 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=507). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7863 sube el IC de +0.366 a +0.402 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=638). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8048 sube el IC de +0.364 a +0.392 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=330). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7479 sube el IC de +0.367 a +0.413 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=309). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1941 | +0.091 | +219.43€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1941 | +0.091 | +219.43€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1549 | +0.095 | +190.69€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1549 | +0.095 | +190.69€ | 0 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 284 | +0.070 | +11.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 284 | +0.070 | +11.30€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 77 | +0.108 | +17.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 77 | +0.108 | +17.77€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 693 | -0.005 | +71.73€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 693 | -0.005 | +71.73€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 5 | +0.018 | +2.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 5 | +0.018 | +2.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 506 | -0.035 | +37.26€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 506 | -0.035 | +37.26€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 146 | +0.088 | +26.94€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 146 | +0.088 | +26.94€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 40656 | -0.080 | -5000.91€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2262 | +0.037 | -260.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 38394 | -0.087 | -4739.98€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4519 | -0.113 | -775.79€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4519 | -0.113 | -775.79€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2262 | +0.037 | -260.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2262 | +0.037 | -260.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4364 | -0.105 | -866.48€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4364 | -0.105 | -866.48€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 10843 | -0.019 | -1005.81€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 10843 | -0.019 | -1005.81€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 10742 | -0.103 | -780.36€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 10742 | -0.103 | -780.36€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 7926 | -0.132 | -1311.53€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 7926 | -0.132 | -1311.53€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 35886 | -0.015 | +3314.77€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 9287 | +0.005 | +1661.80€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 26599 | -0.022 | +1652.97€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 35886 | -0.015 | +3314.77€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 9287 | +0.005 | +1661.80€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 26599 | -0.022 | +1652.97€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 147825 | +0.115 | -5914.84€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 18849 | +0.182 | -582.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 651 | -0.015 | -69.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 119500 | +0.106 | -4946.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 8825 | +0.099 | -317.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 19813 | +0.108 | -1209.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 61 | -0.151 | +10.95€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 19737 | +0.109 | -1208.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 28576 | +0.128 | -428.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5224 | +0.187 | -184.91€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 19798 | +0.121 | -112.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3512 | +0.082 | -108.85€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 19868 | +0.100 | -1370.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 75 | -0.123 | -6.95€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 19778 | +0.101 | -1352.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 31451 | +0.125 | -573.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 8129 | +0.178 | -157.37€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 20072 | +0.107 | -354.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3238 | +0.100 | -53.69€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 28282 | +0.115 | -1399.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5291 | +0.197 | -248.92€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 554 | +0.018 | -15.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 20362 | +0.095 | -980.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2075 | +0.128 | -154.49€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 19835 | +0.106 | -933.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 69 | -0.091 | +4.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 19753 | +0.107 | -937.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 23816 | +0.198 | -1405.98€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 23816 | +0.198 | -1405.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 5414 | +0.180 | -450.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 5414 | +0.180 | -450.98€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 3056 | +0.204 | -64.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 3056 | +0.204 | -64.11€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 5353 | +0.182 | -417.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 5353 | +0.182 | -417.78€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4639 | +0.248 | -153.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4639 | +0.248 | -153.15€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 5275 | +0.189 | -333.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 5275 | +0.189 | -333.72€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1042 | +0.425 | -38.89€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1042 | +0.425 | -38.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 411 | +0.432 | -9.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 411 | +0.432 | -9.48€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 410 | +0.432 | -8.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 410 | +0.432 | -8.54€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 207 | +0.400 | -17.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 207 | +0.400 | -17.00€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 83280 | +0.202 | -5890.42€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 83280 | +0.202 | -5890.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 14302 | +0.186 | -1460.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 14302 | +0.186 | -1460.94€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 13446 | +0.225 | -453.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 13446 | +0.225 | -453.09€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 14260 | +0.182 | -1475.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 14260 | +0.182 | -1475.63€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 13532 | +0.220 | -500.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 13532 | +0.220 | -500.44€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 13821 | +0.202 | -901.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 13821 | +0.202 | -901.41€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 13919 | +0.197 | -1098.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 13919 | +0.197 | -1098.91€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 31872 | +0.116 | +159.19€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 31872 | +0.116 | +159.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 15846 | +0.119 | +153.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 15846 | +0.119 | +153.29€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 16026 | +0.113 | +5.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 16026 | +0.113 | +5.90€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2111 | +0.294 | -1.93€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2111 | +0.294 | -1.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 968 | +0.280 | -24.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 968 | +0.280 | -24.73€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1023 | +0.298 | +16.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1023 | +0.298 | +16.69€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 120 | +0.352 | +6.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 120 | +0.352 | +6.11€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 971 | +0.441 | +3.97€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 971 | +0.441 | +3.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 472 | +0.435 | -5.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 472 | +0.435 | -5.80€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 453 | +0.450 | +9.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 453 | +0.450 | +9.22€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1675 | +0.073 | -61.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 644 | +0.053 | -51.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1031 | +0.086 | -10.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 74 | +0.118 | +4.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 74 | +0.118 | +4.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1288 | +0.081 | -24.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 257 | +0.060 | -14.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1031 | +0.086 | -10.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 313 | +0.030 | -41.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 313 | +0.030 | -41.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 63091 | +0.100 | -1624.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 5096 | +0.089 | +37.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 57995 | +0.101 | -1661.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 34691 | +0.105 | -416.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 5096 | +0.089 | +37.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 29595 | +0.108 | -453.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 13000 | +0.108 | -89.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 13000 | +0.108 | -89.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 15400 | +0.083 | -1118.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 15400 | +0.083 | -1118.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 897 | +0.193 | -109.11€ | 4 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 897 | +0.193 | -109.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 897 | +0.193 | -109.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 897 | +0.193 | -109.11€ | 4 | 4 |
| ✅ GBM_LATE_15M | 43304 | +0.095 | +22715.07€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 43304 | +0.095 | +22715.07€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 7212 | +0.217 | +5971.61€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 7212 | +0.217 | +5971.61€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 6507 | +0.180 | +5000.54€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 6507 | +0.180 | +5000.54€ | 0 | 23 |
| ✅ GBM_LATE_15M#DOGE | 7745 | +0.206 | +6042.64€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 7745 | +0.206 | +6042.64€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 6025 | +0.043 | +1715.75€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 6025 | +0.043 | +1715.75€ | 1 | 20 |
| ✅ GBM_LATE_15M#SOL | 6090 | -0.033 | +1272.48€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 6090 | -0.033 | +1272.48€ | 4 | 15 |
| ✅ GBM_LATE_15M#XRP | 9725 | -0.030 | +2712.05€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 9725 | -0.030 | +2712.05€ | 4 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 46543 | +0.085 | +25413.71€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 46543 | +0.085 | +25413.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 9000 | +0.003 | +4570.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 9000 | +0.003 | +4570.79€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 9869 | +0.010 | +2363.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 9869 | +0.010 | +2363.15€ | 0 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 6449 | +0.279 | +6946.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 6449 | +0.279 | +6946.74€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 8427 | +0.013 | +2096.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 8427 | +0.013 | +2096.06€ | 1 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 7396 | +0.039 | +3064.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 7396 | +0.039 | +3064.51€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5402 | +0.304 | +6372.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5402 | +0.304 | +6372.46€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 34301 | +0.181 | +27879.30€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 34301 | +0.181 | +27879.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 5209 | +0.231 | +4653.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 5209 | +0.231 | +4653.14€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 5397 | +0.149 | +3996.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 5397 | +0.149 | +3996.48€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 5501 | +0.224 | +4743.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 5501 | +0.224 | +4743.79€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 5818 | +0.139 | +4443.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 5818 | +0.139 | +4443.36€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 6440 | +0.125 | +4826.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 6440 | +0.125 | +4826.03€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 5936 | +0.226 | +5216.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 5936 | +0.226 | +5216.50€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 9338 | +0.134 | +4576.35€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 9338 | +0.134 | +4576.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2726 | +0.144 | +1549.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2726 | +0.144 | +1549.35€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 467 | +0.150 | +239.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 467 | +0.150 | +239.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2781 | +0.138 | +1335.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2781 | +0.138 | +1335.83€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2332 | +0.111 | +917.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2332 | +0.111 | +917.63€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 627 | +0.133 | +281.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 627 | +0.133 | +281.63€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 43467 | +0.186 | +34901.69€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 43467 | +0.186 | +34901.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 6883 | +0.243 | +6446.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 6883 | +0.243 | +6446.81€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 6781 | +0.147 | +4659.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 6781 | +0.147 | +4659.86€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 7358 | +0.233 | +6585.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 7358 | +0.233 | +6585.59€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 7175 | +0.139 | +5128.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 7175 | +0.139 | +5128.96€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 7682 | +0.121 | +5323.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 7682 | +0.121 | +5323.30€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 7588 | +0.232 | +6757.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 7588 | +0.232 | +6757.16€ | 0 | 19 |
| ✅ GBM_LATE_5M | 11967 | +0.203 | +9378.77€ | 1 | 30 |
| ✅ GBM_LATE_5M#5min | 11967 | +0.203 | +9378.77€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 984 | +0.242 | +916.10€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 984 | +0.242 | +916.10€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2780 | +0.208 | +2390.04€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2780 | +0.208 | +2390.04€ | 0 | 26 |
| ✅ GBM_LATE_5M#DOGE | 1157 | +0.195 | +849.91€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1157 | +0.195 | +849.91€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 3343 | +0.193 | +2356.01€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3343 | +0.193 | +2356.01€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 1780 | +0.194 | +1369.19€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1780 | +0.194 | +1369.19€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1923 | +0.208 | +1497.52€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1923 | +0.208 | +1497.52€ | 0 | 0 |
| ✅ GBM_LATE_60M | 3581 | +0.065 | +1139.10€ | 0 | 8 |
| ✅ GBM_LATE_60M#60min | 3581 | +0.065 | +1139.10€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1319 | +0.082 | +474.29€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1319 | +0.082 | +474.29€ | 0 | 6 |
| ✅ GBM_LATE_60M#ETH | 1158 | +0.065 | +376.79€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1158 | +0.065 | +376.79€ | 1 | 8 |
| ✅ GBM_LATE_60M#SOL | 1104 | +0.046 | +288.02€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1104 | +0.046 | +288.02€ | 1 | 13 |
| 🚫 GBM_LATE_60M_FADE | 584 | -0.242 | -20.70€ | 9 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 584 | -0.242 | -20.70€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 218 | -0.245 | -13.71€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 218 | -0.245 | -13.71€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 207 | -0.227 | -0.97€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 207 | -0.227 | -0.97€ | 5 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 159 | -0.252 | -6.01€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 159 | -0.252 | -6.01€ | 7 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1560 | +0.085 | +396.63€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1560 | +0.085 | +396.63€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 617 | +0.080 | +148.33€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 617 | +0.080 | +148.33€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 557 | +0.056 | +84.17€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 557 | +0.056 | +84.17€ | 2 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 386 | +0.131 | +164.12€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 386 | +0.131 | +164.12€ | 3 | 9 |
| ✅ LATE_WINDOW_5MIN | 167 | +0.281 | +166.63€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 167 | +0.281 | +166.63€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 167 | +0.281 | +166.63€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 167 | +0.281 | +166.63€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3446 | +0.102 | +858.35€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3446 | +0.102 | +858.35€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3446 | +0.102 | +858.35€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3446 | +0.102 | +858.35€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 550 | -0.040 | -17.14€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 550 | -0.040 | -17.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 157 | -0.003 | +4.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 157 | -0.003 | +4.66€ | 2 | 1 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 107 | -0.032 | -3.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 107 | -0.032 | -3.05€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 205 | -0.012 | -1.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 205 | -0.012 | -1.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 3771 | +0.017 | +90.43€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3771 | +0.017 | +90.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 183 | +0.024 | -1.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 183 | +0.024 | -1.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 795 | +0.008 | +29.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 795 | +0.008 | +29.93€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE | 207 | -0.012 | -4.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 207 | -0.012 | -4.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1376 | +0.028 | +35.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1376 | +0.028 | +35.21€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 758 | +0.012 | +2.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 758 | +0.012 | +2.16€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 452 | +0.018 | +29.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 452 | +0.018 | +29.11€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1784 | -0.042 | -32.52€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1784 | -0.042 | -32.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 516 | -0.033 | -13.17€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 516 | -0.033 | -13.17€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 612 | -0.018 | +4.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 612 | -0.018 | +4.36€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 656 | -0.071 | -23.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 656 | -0.071 | -23.71€ | 6 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 9136 | -0.026 | +34.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 4341 | -0.036 | -80.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 4795 | -0.017 | +114.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 278 | -0.029 | -3.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 141 | -0.004 | +4.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 137 | -0.054 | -8.46€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 2282 | -0.020 | +15.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1088 | -0.028 | -12.23€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1194 | -0.012 | +27.39€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 991 | -0.026 | +10.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 498 | -0.044 | -15.43€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 493 | -0.007 | +25.91€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 2005 | -0.038 | -47.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 930 | -0.050 | -52.82€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1075 | -0.027 | +5.48€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1793 | -0.015 | +50.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 859 | -0.027 | +4.06€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 934 | -0.004 | +46.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1787 | -0.030 | +8.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 825 | -0.039 | -9.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 962 | -0.023 | +17.83€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 50909 | -0.000 | +2567.15€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 50909 | -0.000 | +2567.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 9185 | +0.026 | +1181.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 9185 | +0.026 | +1181.33€ | 2 | 5 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 7317 | -0.033 | -89.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 7317 | -0.033 | -89.46€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 9289 | +0.025 | +977.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 9289 | +0.025 | +977.41€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 7163 | -0.048 | -147.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 7163 | -0.048 | -147.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 8610 | -0.004 | +230.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 8610 | -0.004 | +230.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 9345 | +0.015 | +414.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 9345 | +0.015 | +414.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6675 | -0.059 | -159.23€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6675 | -0.059 | -159.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1747 | -0.077 | -43.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1747 | -0.077 | -43.06€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 55 | -0.061 | -2.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 55 | -0.061 | -2.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 775 | -0.120 | -33.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 775 | -0.120 | -33.97€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2016 | -0.073 | -38.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2016 | -0.073 | -38.50€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 857 | -0.016 | -25.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 857 | -0.016 | -25.51€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3368 | +0.004 | -1.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3368 | +0.004 | -1.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 131 | -0.034 | -0.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 131 | -0.034 | -0.72€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 192 | +0.015 | +1.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 192 | +0.015 | +1.02€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1325 | +0.006 | +6.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1325 | +0.006 | +6.88€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1391 | +0.007 | -0.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1391 | +0.007 | -0.19€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 190 | -0.010 | -6.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 190 | -0.010 | -6.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 126085 | -0.077 | +1637.20€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 126085 | -0.077 | +1637.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 21957 | -0.077 | +1069.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 21957 | -0.077 | +1069.64€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 18991 | -0.101 | -1017.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 18991 | -0.101 | -1017.56€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 22226 | -0.068 | +1195.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 22226 | -0.068 | +1195.24€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 18535 | -0.097 | -604.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 18535 | -0.097 | -604.42€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 22557 | -0.057 | +322.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 22557 | -0.057 | +322.47€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 21819 | -0.067 | +671.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 21819 | -0.067 | +671.84€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8781 | -0.034 | -185.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8781 | -0.034 | -185.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1001 | -0.017 | -18.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1001 | -0.017 | -18.91€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1990 | -0.047 | -26.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1990 | -0.047 | -26.24€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2602 | -0.026 | -42.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2602 | -0.026 | -42.21€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1209 | -0.057 | -29.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1209 | -0.057 | -29.65€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 971 | -0.031 | -35.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 971 | -0.031 | -35.95€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1701 | +0.122 | +686.53€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 1565 | +0.128 | +673.93€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 366 | +0.133 | +177.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 366 | +0.133 | +177.42€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 322 | +0.117 | +111.06€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 322 | +0.117 | +111.06€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#ETH | 309 | +0.137 | +150.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 309 | +0.137 | +150.62€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 275 | +0.150 | +149.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 275 | +0.150 | +149.73€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 293 | +0.100 | +85.11€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 293 | +0.100 | +85.11€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1498 | -0.018 | -28.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1498 | -0.018 | -28.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 293 | -0.005 | +7.03€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 293 | -0.005 | +7.03€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 261 | -0.025 | -4.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 261 | -0.025 | -4.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 387 | -0.048 | -32.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 387 | -0.048 | -32.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 317 | +0.005 | +1.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 317 | +0.005 | +1.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 240 | -0.008 | +1.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 240 | -0.008 | +1.23€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 918 | -0.075 | -51.04€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 428 | -0.114 | -81.18€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 332 | -0.144 | -68.58€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 96 | -0.010 | -12.59€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 323 | -0.032 | +23.57€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 232 | -0.021 | +26.03€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 91 | -0.059 | -2.46€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 167 | -0.056 | +6.57€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 136 | -0.065 | +2.18€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 31 | -0.015 | +4.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 700 | -0.088 | -40.37€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 218 | -0.032 | -10.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1147 | -0.208 | -68.82€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 446 | -0.210 | -42.51€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 389 | -0.214 | -42.28€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 57 | -0.178 | -0.23€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 391 | -0.210 | -31.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 343 | -0.222 | -38.30€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 48 | -0.120 | +7.01€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 310 | -0.199 | +4.99€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 289 | -0.194 | +2.87€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 21 | -0.239 | +2.12€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1021 | -0.212 | -77.72€ | 0 | 0 |
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
| ✅ STREAK_FADE_15M | 735 | +0.033 | +45.24€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 735 | +0.033 | +45.24€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 303 | +0.025 | +3.85€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 303 | +0.025 | +3.85€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 62 | +0.000 | -0.54€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 62 | +0.000 | -0.54€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 75 | -0.006 | +1.40€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 75 | -0.006 | +1.40€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 295 | +0.059 | +40.53€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 295 | +0.059 | +40.53€ | 0 | 5 |
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
| ✅ STREAK_FADE_60M | 103 | -0.052 | -9.27€ | 6 | 0 |
| ✅ STREAK_FADE_60M#60min | 103 | -0.052 | -9.27€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 43 | -0.100 | -5.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 43 | -0.100 | -5.07€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 60 | -0.016 | -4.20€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 60 | -0.016 | -4.20€ | 0 | 2 |
| ✅ STREAK_MOM_5M | 10971 | +0.016 | +88.11€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 10971 | +0.016 | +88.11€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2808 | +0.021 | +29.65€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2808 | +0.021 | +29.65€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2866 | +0.018 | +36.51€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2866 | +0.018 | +36.51€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2888 | +0.009 | -0.95€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2888 | +0.009 | -0.95€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2409 | +0.016 | +22.90€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2409 | +0.016 | +22.90€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 9992 | +0.013 | -51.16€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 9992 | +0.013 | -51.16€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4088 | +0.017 | -11.18€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4088 | +0.017 | -11.18€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3616 | +0.011 | -27.14€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3616 | +0.011 | -27.14€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2288 | +0.010 | -12.84€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2288 | +0.010 | -12.84€ | 1 | 0 |
| ✅ UPDOWN_GBM | 78231 | +0.054 | +6941.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 19441 | +0.083 | +4268.19€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 2502 | +0.004 | +22.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 51374 | +0.050 | +2556.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 4637 | +0.007 | +95.00€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6851 | +0.089 | +1075.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1576 | +0.156 | +698.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5198 | +0.070 | +378.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 16976 | +0.055 | +1459.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2537 | +0.088 | +623.22€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 676 | +0.009 | +9.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 11601 | +0.061 | +759.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2062 | +0.004 | +63.94€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 100 | -0.069 | +3.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8566 | +0.070 | +913.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1555 | +0.147 | +610.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6933 | +0.054 | +303.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 18037 | +0.044 | +1171.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 4615 | +0.066 | +673.79€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 658 | +0.006 | +15.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 11045 | +0.044 | +458.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1626 | +0.011 | +20.54€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 93 | -0.100 | +2.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 17196 | +0.032 | +856.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 4908 | +0.034 | +409.24€ | 0 | 3 |
| ✅ UPDOWN_GBM#SOL#240min | 625 | -0.009 | -0.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 10632 | +0.037 | +441.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 949 | +0.007 | +10.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 82 | -0.131 | -5.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 10603 | +0.065 | +1467.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4250 | +0.103 | +1252.91€ | 0 | 9 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 5965 | +0.041 | +214.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 275 | -0.099 | +1.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 850 | +0.366 | +316.02€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 850 | +0.366 | +316.02€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 439 | +0.364 | +153.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 439 | +0.364 | +153.25€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 411 | +0.367 | +162.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 411 | +0.367 | +162.77€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 20182 | -0.026 | +4659.82€ | 2 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 20182 | -0.026 | +4659.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3607 | -0.113 | +128.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3607 | -0.113 | +128.38€ | 3 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2479 | +0.217 | +1606.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2479 | +0.217 | +1606.01€ | 1 | 19 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5781 | -0.067 | +667.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5781 | -0.067 | +667.71€ | 5 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5649 | -0.065 | +984.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5649 | -0.065 | +984.45€ | 2 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 236 | +0.050 | +14.42€ | 0 | 5 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 236 | +0.050 | +14.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 236 | +0.050 | +14.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 236 | +0.050 | +14.42€ | 0 | 5 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1457 | +0.292 | +1253.74€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1457 | +0.292 | +1253.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 782 | +0.289 | +638.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 782 | +0.289 | +638.60€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 675 | +0.295 | +615.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 675 | +0.295 | +615.14€ | 0 | 9 |
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
| ✅ WEEKLY_PRICE | 3691 | +0.304 | +1736.67€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1360 | +0.257 | +170.41€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1419 | +0.299 | +634.07€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 912 | +0.380 | +932.19€ | 0 | 1 |