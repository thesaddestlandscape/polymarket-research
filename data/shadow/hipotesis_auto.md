# Hipótesis automáticas — 2026-11-04 13:16 UTC
_Generado por shadow_postmortem.py sobre 1189995 resoluciones (PNL=+161908.68€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.5` → IC=-0.317 (n=195)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=681)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.201 (n=991)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.132)

- **PATRÓN** `n_total_lado` > `63.0` → IC=+0.182 (n=313)

  - _Acción_: Kelly boost +0.91€ cuando `n_total_lado` > 63.0 (IC base=+0.132)

- **PATRÓN** `banda_hit_calibrado` > `0.6154` → IC=+0.249 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6154 (IC base=+0.132)

- **PATRÓN** `banda_z` > `8.703` → IC=+0.208 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.703 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=343)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.132 (n=672)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 12.0 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=1010)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `3343.4249` → IC=+0.135 (n=619)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 3343.4249 (IC base=+0.132)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.505` → IC=+0.199 (n=856)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.136)

- **PATRÓN** `n_total_lado` > `66.0` → IC=+0.185 (n=271)

  - _Acción_: Kelly boost +0.92€ cuando `n_total_lado` > 66.0 (IC base=+0.136)

- **PATRÓN** `banda_hit_calibrado` > `0.8136` → IC=+0.272 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8136 (IC base=+0.136)

- **PATRÓN** `banda_z` > `9.03` → IC=+0.205 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.03 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.159 (n=291)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=910)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.136)

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
- **FILTRO** `ballenas_wallet_edge_medio` < `2.833` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `ballenas_wallet_edge_medio` < 2.833
  - _Potencial_: sin este filtro IC_bueno=+0.375 (n=6)

- **PATRÓN** `py_entrada` > `0.495` → IC=+0.167 (n=46)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.495 (IC base=+0.162)

- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 26.0 (IC base=+0.162)

- **PATRÓN** `n_total_lado` > `43.0` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 43.0 (IC base=+0.162)

- **PATRÓN** `banda_hit_calibrado` > `0.6068` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `banda_hit_calibrado` > 0.6068 (IC base=+0.162)

- **PATRÓN** `banda_z` > `2.495` → IC=+0.231 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 2.495 (IC base=+0.162)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.729` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `ballenas_wallet_edge_medio` > 0.729 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.269 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.167 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 7.0 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.214 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `2453.7234` → IC=+0.202 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2453.7234 (IC base=+0.162)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `134.84` → IC=-0.217 (n=11308)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 134.84
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=33938)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `127.47` → IC=-0.254 (n=1175)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.47
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=3526)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `117.09` → IC=-0.311 (n=1169)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 117.09
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3507)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `118.43` → IC=-0.159 (n=3087)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 118.43
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=9265)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `156.46` → IC=-0.240 (n=3055)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 156.46
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=9170)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `131.52` → IC=-0.255 (n=2154)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.52
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=6463)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.211 (n=25835)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `8521.1605` → IC=+0.161 (n=2245)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 8521.1605 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=22061)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=26980)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.224 (n=20379)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=7981)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6747.5472` → IC=+0.149 (n=3081)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 6747.5472 (IC base=+0.124)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=2074)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.364 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.179)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.182 (n=2662)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `9415.8912` → IC=+0.181 (n=1852)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 9415.8912 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.187 (n=1890)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.183 (n=2116)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` < `0.295` → IC=+0.312 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.295 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.182 (n=2710)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `16111.0352` → IC=+0.185 (n=699)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 16111.0352 (IC base=+0.180)

### FAVORITO_CONFIRMADO#BTC#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.335 (n=95)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=2073)

- **PATRÓN** `py_entrada` > `0.61` → IC=+0.171 (n=560)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.61 (IC base=+0.074)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.143 (n=1319)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.44 (IC base=+0.082)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=4968)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.168 (n=4208)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 15.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.375 (n=1582)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.215 (n=2234)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` < `0.27` → IC=+0.345 (n=811)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.27 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=2598)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=1265)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.149 (n=1079)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 15.0 (IC base=+0.142)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.258 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.143 (n=1402)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.160 (n=154)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.071)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.257 (n=923)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.228)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1288)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.147 (n=1379)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=714)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.146)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.286 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.146)

### FAVORITO_CONFIRMADO#SOL#60min
- **FILTRO** `libro_liquidez` < `947.2335` → IC=-0.128 (n=154)

  - _Acción_: SKIP cuando `libro_liquidez` < 947.2335
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=313)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.160 (n=454)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` > 0.55 (IC base=+0.049)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.132 (n=1175)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 7.0 (IC base=+0.121)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.244 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.121)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.297 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=22170)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.200 (n=18790)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.228 (n=9232)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.198)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.177 (n=5056)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.176 (n=5038)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 18.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.182 (n=4820)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.175 (n=4229)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` > 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.215 (n=2888)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.215 (n=2571)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.212)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.290 (n=965)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.212)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=4968)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.180 (n=4224)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.178 (n=5140)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.186 (n=3878)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.258 (n=4229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.250)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.250 (n=3594)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.250)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.356 (n=1458)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.79 (IC base=+0.250)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.250)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=4881)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=4154)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.191 (n=3630)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.187)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.430 (n=827)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.426)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.428 (n=913)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.440 (n=930)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=971)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `4437.5111` → IC=+0.444 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4437.5111 (IC base=+0.426)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.444 (n=376)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.459 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.440)

- **PATRÓN** `libro_liquidez` > `12430.0394` → IC=+0.448 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12430.0394 (IC base=+0.440)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.431 (n=362)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.428 (n=359)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `4655.9741` → IC=+0.442 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4655.9741 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.399 (n=146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.396)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.403 (n=143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.396)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.412 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.396)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `14.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.257 (n=35)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=34)

- **FILTRO** `libro_liquidez` < `6112.397` → IC=-0.300 (n=33)

  - _Acción_: SKIP cuando `libro_liquidez` < 6112.397
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=17)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=28929)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.243 (n=29238)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.201)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.190 (n=4301)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 18.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.182 (n=9261)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 12.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.193 (n=13178)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.227 (n=12123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.226)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.288 (n=4152)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.226)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.186 (n=4967)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.199 (n=10237)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.225 (n=6075)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.223 (n=4643)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.270 (n=4087)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `hora_utc` > `3.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `libro_liquidez` < `3176.5987` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 3176.5987
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.206 (n=11035)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.258 (n=4267)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=4812)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.200 (n=4813)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.244 (n=5046)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.191 (n=10376)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=10708)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `3.55` → IC=+0.137 (n=12655)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.55 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=5063)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.144 (n=4841)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.125 (n=6365)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.64` → IC=+0.145 (n=4785)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 2.64 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.189 (n=5313)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.115)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=5867)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.115)

- **PATRÓN** `lag_apertura_s` < `3.21` → IC=+0.136 (n=6359)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.21 (IC base=+0.115)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.307 (n=1298)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.387 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.293)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.285 (n=874)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.281)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.367 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.281)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.320 (n=630)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.298)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.301 (n=924)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.298)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.392 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.298)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.300 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.298)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` < `16.0` → IC=+0.362 (n=92)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.339)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.388 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.339)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.368 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.339)

- **PATRÓN** `libro_liquidez` > `720.8183` → IC=+0.371 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 720.8183 (IC base=+0.339)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.443 (n=886)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.447 (n=854)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.442 (n=1023)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.441)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.436 (n=417)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.441 (n=286)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.435 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.443 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.435)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.465 (n=140)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.447)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.450 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.447)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.447)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.448 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.447)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.417 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.404)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.417 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.404)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.404)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `hora_utc` < `5.0` → IC=-0.269 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=109)

- **FILTRO** `py_entrada` > `0.735` → IC=-0.386 (n=42)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=91)

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
- **FILTRO** `hora_utc` < `5.0` → IC=-0.269 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=109)

- **FILTRO** `py_entrada` > `0.735` → IC=-0.386 (n=42)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=91)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4736` → IC=+0.138 (n=16328)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.4736 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.126 (n=16505)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=11410)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.3732` → IC=+0.165 (n=16329)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.3732 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.7895` → IC=+0.283 (n=927)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7895 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.551` → IC=+0.184 (n=8158)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 3.551 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6963` → IC=+0.265 (n=4320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6963 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.3037` → IC=+0.245 (n=1682)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3037 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.739` → IC=+0.231 (n=3900)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.739 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=8212)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `4721.8184` → IC=+0.145 (n=5443)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 4721.8184 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.121 (n=10158)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.006 (IC base=+0.080)

- **PATRÓN** `ibs_20min` < `0.6792` → IC=+0.132 (n=23077)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.6792 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` > `0.6084` → IC=+0.188 (n=1392)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.6084 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` < `0.1614` → IC=+0.189 (n=7876)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.1614 (IC base=+0.080)

- **PATRÓN** `volumen_regimen` < `0.863` → IC=+0.192 (n=5462)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.863 (IC base=+0.080)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.228 (n=2024)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.080)

- **PATRÓN** `volumen_spike_ratio` > `1.4565` → IC=+0.204 (n=13925)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4565 (IC base=+0.080)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.226 (n=13824)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 102.0 (IC base=+0.080)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3633` → IC=+0.210 (n=3497)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3633 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.223 (n=1692)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.212 (n=2352)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `0.9851` → IC=+0.280 (n=1586)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9851 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.566` → IC=+0.280 (n=1554)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.566 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.2828` → IC=+0.261 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2828 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `1.4344` → IC=+0.211 (n=3348)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4344 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.222 (n=3838)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2064.8387` → IC=+0.212 (n=1166)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2064.8387 (IC base=+0.209)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.222 (n=3155)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 28.0 (IC base=+0.209)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.242 (n=3049)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.01 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.0896` → IC=+0.273 (n=1016)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0896 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.252 (n=1122)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.242 (n=1414)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.4691` → IC=+0.259 (n=2681)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4691 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` < `0.0948` → IC=+0.245 (n=2751)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0948 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.2883` → IC=+0.253 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2883 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.4445` → IC=+0.246 (n=967)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4445 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `1.8593` → IC=+0.243 (n=1932)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8593 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.242 (n=3496)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1769.2902` → IC=+0.249 (n=2031)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1769.2902 (IC base=+0.240)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.230 (n=1945)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.0811` → IC=+0.261 (n=972)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0811 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=3046)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.225 (n=2079)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.914` → IC=+0.264 (n=971)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.914 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.1869` → IC=+0.234 (n=1360)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1869 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.015` → IC=+0.262 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.015 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` < `1.2269` → IC=+0.225 (n=2914)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2269 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.6995` → IC=+0.229 (n=2603)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6995 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2786` → IC=+0.269 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2786 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.4278` → IC=+0.251 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4278 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.150 (n=3085)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0062 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.0775` → IC=+0.152 (n=1028)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.0775 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.150 (n=1145)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.7113` → IC=+0.166 (n=3083)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.7113 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` < `0.1376` → IC=+0.144 (n=2940)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1376 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.727` → IC=+0.132 (n=498)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 10.727 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.01` → IC=+0.133 (n=2825)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 4.01 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `1.2025` → IC=+0.135 (n=3083)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.2025 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.150 (n=1128)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `2.1366` → IC=+0.136 (n=2604)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.1366 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.128 (n=3999)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `204.0` → IC=+0.166 (n=1273)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 204.0 (IC base=+0.127)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.217 (n=1230)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=3878)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.266 (n=1433)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.093` → IC=+0.275 (n=804)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.093 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.197 (n=3303)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.3536` → IC=+0.216 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3536 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.7293` → IC=+0.209 (n=1632)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7293 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.199 (n=4444)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `1387.1784` → IC=+0.197 (n=3690)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 1387.1784 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.224 (n=2969)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0111 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.1772` → IC=+0.235 (n=1484)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1772 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=1271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.222 (n=1537)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` < `0.0404` → IC=+0.270 (n=1124)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0404 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.038` → IC=+0.263 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.038 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.3493` → IC=+0.257 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3493 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` < `1.7617` → IC=+0.219 (n=1422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7617 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.1534` → IC=+0.226 (n=2155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1534 (IC base=+0.219)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.225 (n=1698)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `1920.8826` → IC=+0.222 (n=1528)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1920.8826 (IC base=+0.219)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.223 (n=3192)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.219)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=184)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=4450)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.161 (n=633)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0038 (IC base=+0.057)

- **PATRÓN** `ibs_20min` > `0.9435` → IC=+0.233 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9435 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` > `0.1384` → IC=+0.337 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1384 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` < `0.5334` → IC=+0.333 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5334 (IC base=+0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.077` → IC=+0.201 (n=1379)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.077 (IC base=+0.057)

- **PATRÓN** `volumen_regimen` > `1.0907` → IC=+0.349 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0907 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` < `0.0777` → IC=+0.334 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0777 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.3033` → IC=+0.333 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3033 (IC base=+0.057)

- **PATRÓN** `volumen_spike_ratio` < `1.4175` → IC=+0.340 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4175 (IC base=+0.057)

- **PATRÓN** `volumen_spike_ratio` > `2.2709` → IC=+0.339 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2709 (IC base=+0.057)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.337 (n=733)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 143.0 (IC base=+0.057)

- **PATRÓN** `ibs_20min` < `0.092` → IC=+0.182 (n=1159)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.092 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` > `0.3354` → IC=+0.158 (n=574)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.3354 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` < `0.1388` → IC=+0.145 (n=2022)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1388 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` < `0.8365` → IC=+0.158 (n=1451)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8365 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.206 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` < `1.7747` → IC=+0.150 (n=1395)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.7747 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` > `2.1533` → IC=+0.157 (n=948)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.1533 (IC base=+0.046)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.184 (n=131)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=695)

- **FILTRO** `ibs_20min` < `0.2667` → IC=-0.173 (n=206)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2667
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=620)

- **FILTRO** `ibs_20min` > `0.2051` → IC=-0.132 (n=4365)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2051
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=2153)

- **FILTRO** `sigma_ewma_delta_pct` > `8.401` → IC=-0.226 (n=702)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.401
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=5816)

- **PATRÓN** `ibs_20min` > `0.7547` → IC=+0.178 (n=281)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.7547 (IC base=+0.019)

- **PATRÓN** `dist_vwap_pct` > `0.9638` → IC=+0.277 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9638 (IC base=+0.019)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.051` → IC=+0.156 (n=193)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 5.051 (IC base=+0.019)

- **PATRÓN** `volumen_regimen` > `1.0267` → IC=+0.293 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0267 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` < `0.0791` → IC=+0.285 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0791 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` < `2.4693` → IC=+0.283 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4693 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` > `1.544` → IC=+0.266 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.544 (IC base=+0.019)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.275 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.019)

- **PATRÓN** `ibs_20min` < `0.2051` → IC=+0.154 (n=2153)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.2051 (IC base=-0.037)

- **PATRÓN** `dist_vwap_pct` > `0.2141` → IC=+0.286 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2141 (IC base=-0.037)

- **PATRÓN** `dist_vwap_pct` < `0.4903` → IC=+0.282 (n=1085)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4903 (IC base=-0.037)

- **PATRÓN** `volumen_regimen` < `0.6963` → IC=+0.306 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6963 (IC base=-0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.0789` → IC=+0.294 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0789 (IC base=-0.037)

- **PATRÓN** `volumen_spike_ratio` < `2.4493` → IC=+0.305 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4493 (IC base=-0.037)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7778` → IC=-0.153 (n=3265)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7778
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=1686)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.166 (n=1125)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=3826)

- **FILTRO** `ibs_20min` > `0.7457` → IC=-0.199 (n=1734)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7457
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=5206)

- **PATRÓN** `dist_vwap_pct` > `1.0084` → IC=+0.359 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0084 (IC base=-0.061)

- **PATRÓN** `dist_vwap_pct` < `0.2464` → IC=+0.304 (n=820)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2464 (IC base=-0.061)

- **PATRÓN** `volumen_regimen` > `0.7048` → IC=+0.318 (n=831)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7048 (IC base=-0.061)

- **PATRÓN** `volumen_pendiente_norm` < `0.1062` → IC=+0.303 (n=878)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1062 (IC base=-0.061)

- **PATRÓN** `volumen_pendiente_norm` > `0.0772` → IC=+0.304 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0772 (IC base=-0.061)

- **PATRÓN** `volumen_spike_ratio` < `1.5776` → IC=+0.305 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5776 (IC base=-0.061)

- **PATRÓN** `volumen_spike_ratio` > `2.523` → IC=+0.313 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.523 (IC base=-0.061)

- **PATRÓN** `dist_vwap_pct` > `0.7921` → IC=+0.276 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7921 (IC base=+0.000)

- **PATRÓN** `dist_vwap_pct` < `0.2213` → IC=+0.265 (n=1959)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2213 (IC base=+0.000)

- **PATRÓN** `volumen_regimen` < `0.722` → IC=+0.272 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.722 (IC base=+0.000)

- **PATRÓN** `volumen_regimen` > `1.0635` → IC=+0.286 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0635 (IC base=+0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.1697` → IC=+0.287 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1697 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` < `2.1787` → IC=+0.267 (n=1642)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1787 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` > `1.4406` → IC=+0.271 (n=1866)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4406 (IC base=+0.000)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.199 (n=7055)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0105 (IC base=+0.090)

- **PATRÓN** `ibs_20min` > `0.873` → IC=+0.288 (n=9598)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.873 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` > `0.9377` → IC=+0.303 (n=1531)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9377 (IC base=+0.090)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.528` → IC=+0.167 (n=9465)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.528 (IC base=+0.090)

- **PATRÓN** `volumen_regimen` < `1.1764` → IC=+0.268 (n=7767)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1764 (IC base=+0.090)

- **PATRÓN** `volumen_regimen` > `0.6927` → IC=+0.275 (n=6939)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6927 (IC base=+0.090)

- **PATRÓN** `volumen_pendiente_norm` > `0.2401` → IC=+0.288 (n=2330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2401 (IC base=+0.090)

- **PATRÓN** `volumen_spike_ratio` > `2.6525` → IC=+0.282 (n=4106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6525 (IC base=+0.090)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.307 (n=11920)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.090)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.157 (n=6807)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.01 (IC base=+0.079)

- **PATRÓN** `ibs_20min` < `0.6439` → IC=+0.151 (n=20399)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.6439 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` < `0.2543` → IC=+0.276 (n=6757)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2543 (IC base=+0.079)

- **PATRÓN** `volumen_regimen` < `0.7021` → IC=+0.278 (n=2925)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7021 (IC base=+0.079)

- **PATRÓN** `volumen_regimen` > `1.193` → IC=+0.274 (n=2216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.193 (IC base=+0.079)

- **PATRÓN** `volumen_pendiente_norm` > `0.2941` → IC=+0.324 (n=1460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2941 (IC base=+0.079)

- **PATRÓN** `volumen_spike_ratio` < `1.5762` → IC=+0.299 (n=4290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5762 (IC base=+0.079)

- **PATRÓN** `volumen_spike_ratio` > `2.2821` → IC=+0.296 (n=4420)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2821 (IC base=+0.079)

- **PATRÓN** `ballena_activa_n` < `74.0` → IC=+0.307 (n=9722)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 74.0 (IC base=+0.079)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8` → IC=-0.121 (n=3795)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8
  - _Potencial_: sin este filtro IC_bueno=+0.292 (n=1962)

- **FILTRO** `ibs_20min` > `0.7206` → IC=-0.228 (n=1257)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7206
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=3773)

- **FILTRO** `sigma_ewma_delta_pct` > `4.182` → IC=-0.227 (n=1086)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.182
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=3944)

- **PATRÓN** `ibs_20min` > `0.9337` → IC=+0.335 (n=1440)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9337 (IC base=+0.020)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.055` → IC=+0.189 (n=1926)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.055 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.2286` → IC=+0.325 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2286 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` < `1.4469` → IC=+0.277 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4469 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` > `2.2395` → IC=+0.297 (n=844)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2395 (IC base=+0.020)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.313 (n=1252)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.020)

- **PATRÓN** `ibs_20min` < `0.1723` → IC=+0.160 (n=1258)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1723 (IC base=-0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.1515` → IC=+0.404 (n=887)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1515 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.4257` → IC=+0.428 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4257 (IC base=-0.026)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.401 (n=886)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=-0.026)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.3024` → IC=+0.226 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3024 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` < `1.1954` → IC=+0.207 (n=2061)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1954 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` > `0.6955` → IC=+0.211 (n=1841)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6955 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.2788` → IC=+0.246 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2788 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` < `1.417` → IC=+0.232 (n=678)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.417 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` > `2.4483` → IC=+0.206 (n=678)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4483 (IC base=+0.014)

- **PATRÓN** `ballena_activa_n` < `266.0` → IC=+0.241 (n=1355)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 266.0 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` < `0.1295` → IC=+0.250 (n=1426)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1295 (IC base=-0.005)

- **PATRÓN** `volumen_regimen` > `0.6223` → IC=+0.245 (n=1408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6223 (IC base=-0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2713` → IC=+0.309 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2713 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.5307` → IC=+0.249 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5307 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.1537` → IC=+0.259 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1537 (IC base=-0.005)

- **PATRÓN** `ballena_activa_n` < `213.0` → IC=+0.258 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 213.0 (IC base=-0.005)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.325 (n=1361)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.281)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.290 (n=2996)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.281)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.323 (n=1629)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.617` → IC=+0.301 (n=1987)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.617 (IC base=+0.281)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.294 (n=2626)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.281)

- **PATRÓN** `volumen_spike_ratio` > `1.6095` → IC=+0.286 (n=2907)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6095 (IC base=+0.281)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.290 (n=3577)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `2040.8584` → IC=+0.295 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2040.8584 (IC base=+0.281)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.305 (n=1861)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.281)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.320 (n=2402)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0073 (IC base=+0.302)

- **PATRÓN** `drift_60min` |x|≤ `0.1781` → IC=+0.321 (n=1182)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1781 (IC base=+0.302)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.328 (n=1024)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.302)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.304 (n=1217)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.302)

- **PATRÓN** `ibs_20min` < `0.0124` → IC=+0.303 (n=1181)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0124 (IC base=+0.302)

- **PATRÓN** `ibs_20min` > `0.1385` → IC=+0.312 (n=1789)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1385 (IC base=+0.302)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.32` → IC=+0.313 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.32 (IC base=+0.302)

- **PATRÓN** `volumen_pendiente_norm` < `0.1982` → IC=+0.303 (n=2637)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1982 (IC base=+0.302)

- **PATRÓN** `volumen_pendiente_norm` > `0.3444` → IC=+0.309 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3444 (IC base=+0.302)

- **PATRÓN** `volumen_spike_ratio` < `1.7441` → IC=+0.302 (n=1137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7441 (IC base=+0.302)

- **PATRÓN** `volumen_spike_ratio` > `2.7258` → IC=+0.315 (n=1171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7258 (IC base=+0.302)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.305 (n=1358)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.302)

- **PATRÓN** `libro_liquidez` > `1922.908` → IC=+0.314 (n=1217)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1922.908 (IC base=+0.302)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.309 (n=2244)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.302)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7282` → IC=-0.182 (n=1317)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7282
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=3954)

- **PATRÓN** `ibs_20min` > `0.8542` → IC=+0.166 (n=1289)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.8542 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.1469` → IC=+0.232 (n=979)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1469 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` < `0.3618` → IC=+0.234 (n=1802)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3618 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` < `1.1635` → IC=+0.233 (n=1850)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1635 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` > `0.6714` → IC=+0.231 (n=1653)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6714 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` < `0.1623` → IC=+0.235 (n=1944)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1623 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.1029` → IC=+0.236 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1029 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `2.4586` → IC=+0.236 (n=1792)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4586 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `117.0` → IC=+0.255 (n=1830)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 117.0 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` < `0.3486` → IC=+0.244 (n=1453)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3486 (IC base=+0.004)

- **PATRÓN** `volumen_regimen` < `1.0163` → IC=+0.251 (n=1159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0163 (IC base=+0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.309 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.787` → IC=+0.282 (n=841)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.787 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.4276` → IC=+0.266 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4276 (IC base=+0.004)

- **PATRÓN** `ballena_activa_n` < `101.0` → IC=+0.277 (n=1128)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 101.0 (IC base=+0.004)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7455` → IC=-0.242 (n=2194)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7455
  - _Potencial_: sin este filtro IC_bueno=+0.312 (n=2194)

- **FILTRO** `ibs_20min` > `0.6279` → IC=-0.232 (n=1052)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6279
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=3157)

- **FILTRO** `sigma_ewma_delta_pct` > `8.314` → IC=-0.252 (n=482)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.314
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=3727)

- **PATRÓN** `ibs_20min` > `0.7455` → IC=+0.312 (n=2194)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7455 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` > `0.2161` → IC=+0.347 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2161 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.484` → IC=+0.152 (n=1768)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 2.484 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` < `0.8471` → IC=+0.341 (n=1072)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8471 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` > `0.6974` → IC=+0.335 (n=1435)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6974 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` < `0.1578` → IC=+0.335 (n=1660)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1578 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.2747` → IC=+0.356 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2747 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `1.432` → IC=+0.364 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.432 (IC base=+0.035)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.354 (n=1400)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.035)

- **PATRÓN** `ibs_20min` < `0.6279` → IC=+0.145 (n=3157)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.6279 (IC base=+0.051)

- **PATRÓN** `dist_vwap_pct` < `0.4926` → IC=+0.260 (n=1712)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4926 (IC base=+0.051)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.034` → IC=+0.125 (n=2966)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` < 3.034 (IC base=+0.051)

- **PATRÓN** `volumen_regimen` < `0.6966` → IC=+0.285 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6966 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.0707` → IC=+0.277 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0707 (IC base=+0.051)

- **PATRÓN** `volumen_spike_ratio` < `2.4411` → IC=+0.267 (n=1486)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4411 (IC base=+0.051)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.281 (n=1520)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.051)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.356 (n=2011)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.313)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.315 (n=2273)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.313)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.316 (n=2364)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.313)

- **PATRÓN** `ibs_20min` > `0.6693` → IC=+0.344 (n=2251)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6693 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` > `0.2044` → IC=+0.338 (n=1248)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2044 (IC base=+0.313)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.814` → IC=+0.330 (n=1088)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.814 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` > `0.6304` → IC=+0.322 (n=2251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6304 (IC base=+0.313)

- **PATRÓN** `volumen_pendiente_norm` > `0.2809` → IC=+0.344 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2809 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` > `1.4298` → IC=+0.325 (n=2166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4298 (IC base=+0.313)

- **PATRÓN** `libro_liquidez` > `2966.0162` → IC=+0.318 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2966.0162 (IC base=+0.313)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.343 (n=1990)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.313)

- **PATRÓN** `sigma_h` > `0.0153` → IC=+0.347 (n=1592)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0153 (IC base=+0.315)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.322 (n=1206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.315)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.318 (n=1165)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.315)

- **PATRÓN** `ibs_20min` < `0.381` → IC=+0.335 (n=2386)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.381 (IC base=+0.315)

- **PATRÓN** `dist_vwap_pct` < `0.2369` → IC=+0.320 (n=2298)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2369 (IC base=+0.315)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.624` → IC=+0.330 (n=880)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.624 (IC base=+0.315)

- **PATRÓN** `volumen_regimen` < `0.7201` → IC=+0.320 (n=1050)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7201 (IC base=+0.315)

- **PATRÓN** `volumen_regimen` > `1.2103` → IC=+0.343 (n=796)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2103 (IC base=+0.315)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.366 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.315)

- **PATRÓN** `volumen_spike_ratio` < `1.4124` → IC=+0.324 (n=736)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4124 (IC base=+0.315)

- **PATRÓN** `volumen_spike_ratio` > `2.1376` → IC=+0.318 (n=1000)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1376 (IC base=+0.315)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.228 (n=5286)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.0876` → IC=+0.195 (n=5275)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.0876 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=16419)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `0.5407` → IC=+0.233 (n=15825)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5407 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.1633` → IC=+0.207 (n=6170)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1633 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.91` → IC=+0.259 (n=3094)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.91 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `1.186` → IC=+0.157 (n=10537)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.186 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` > `0.6262` → IC=+0.156 (n=10538)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.6262 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.2944` → IC=+0.207 (n=2291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2944 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `2.6089` → IC=+0.191 (n=5128)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.6089 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.196 (n=14733)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 89.0 (IC base=+0.176)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.190 (n=6774)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0057 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.0802` → IC=+0.220 (n=5131)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0802 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=5784)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.5212` → IC=+0.239 (n=15392)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5212 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.1803` → IC=+0.177 (n=11083)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1803 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.689` → IC=+0.194 (n=2453)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 9.689 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.572` → IC=+0.187 (n=13697)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 2.572 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `1.182` → IC=+0.164 (n=10967)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.182 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2941` → IC=+0.216 (n=2305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2941 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6363` → IC=+0.189 (n=4866)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6363 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.197 (n=14373)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 94.0 (IC base=+0.182)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1052` → IC=+0.257 (n=1148)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1052 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=962)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.229 (n=1771)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.8091` → IC=+0.275 (n=2329)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8091 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.627` → IC=+0.329 (n=844)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.627 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2806` → IC=+0.292 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2806 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `1.8299` → IC=+0.224 (n=1655)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8299 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.4336` → IC=+0.227 (n=2482)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4336 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=2885)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.258 (n=2094)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.255)

- **PATRÓN** `drift_60min` |x|≤ `0.0973` → IC=+0.305 (n=922)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0973 (IC base=+0.255)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.260 (n=2163)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.255)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.257 (n=1912)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.255)

- **PATRÓN** `ibs_20min` < `0.4264` → IC=+0.272 (n=2095)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4264 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` < `0.1002` → IC=+0.259 (n=1835)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1002 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` > `0.3012` → IC=+0.276 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3012 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` < `1.4456` → IC=+0.279 (n=667)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4456 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` > `2.7154` → IC=+0.259 (n=666)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7154 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.258 (n=2407)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `1511.3592` → IC=+0.264 (n=1870)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1511.3592 (IC base=+0.255)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.255 (n=1773)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.255)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.199 (n=811)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.003 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.1597` → IC=+0.163 (n=1613)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1597 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.150 (n=2533)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.2676` → IC=+0.209 (n=2418)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2676 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.1856` → IC=+0.215 (n=1240)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1856 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.763` → IC=+0.208 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.763 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.6953` → IC=+0.143 (n=1064)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6953 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` > `1.0616` → IC=+0.139 (n=1097)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 1.0616 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.180 (n=376)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `1.4018` → IC=+0.146 (n=792)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4018 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `2.4689` → IC=+0.146 (n=792)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.4689 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `403.0` → IC=+0.139 (n=2341)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 403.0 (IC base=+0.134)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.171 (n=2549)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0063 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.2376` → IC=+0.168 (n=2239)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.2376 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.182 (n=1215)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.6112` → IC=+0.206 (n=2544)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6112 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.1457` → IC=+0.172 (n=2640)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1457 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.077` → IC=+0.179 (n=478)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 11.077 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.063` → IC=+0.147 (n=2227)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 4.063 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.2025` → IC=+0.159 (n=2544)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2025 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` < `0.094` → IC=+0.149 (n=2203)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.094 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.128` → IC=+0.151 (n=2130)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.128 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `214.0` → IC=+0.184 (n=1042)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 214.0 (IC base=+0.145)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.235 (n=1217)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.395` → IC=+0.225 (n=2359)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.395 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.234 (n=977)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=1413)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.193` → IC=+0.305 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.193 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.0992` → IC=+0.211 (n=2326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0992 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.3552` → IC=+0.235 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3552 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.7278` → IC=+0.225 (n=1185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7278 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.217 (n=3226)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `2030.1067` → IC=+0.222 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2030.1067 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.246 (n=2056)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.4174` → IC=+0.262 (n=2053)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4174 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.282 (n=890)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.0313` → IC=+0.290 (n=1026)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0313 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.203` → IC=+0.282 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.203 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.3584` → IC=+0.285 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3584 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.7655` → IC=+0.239 (n=988)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7655 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `2.1788` → IC=+0.247 (n=1497)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1788 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.240 (n=1198)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1916.24` → IC=+0.247 (n=1058)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1916.24 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.243 (n=1541)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.239)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.199 (n=1143)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0042 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0786` → IC=+0.193 (n=865)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.0786 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=2684)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.2661` → IC=+0.199 (n=2590)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.2661 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.1399` → IC=+0.190 (n=1538)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1399 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.397` → IC=+0.201 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.397 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.8476` → IC=+0.145 (n=1727)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.8476 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2887` → IC=+0.180 (n=385)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2887 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.8246` → IC=+0.138 (n=1692)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.8246 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.5248` → IC=+0.158 (n=846)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.5248 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `6908.9474` → IC=+0.200 (n=1175)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6908.9474 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `131.0` → IC=+0.144 (n=2538)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 131.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.166 (n=2410)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0066 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.3952` → IC=+0.145 (n=2739)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3952 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.163 (n=1308)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.6735` → IC=+0.187 (n=2739)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6735 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.1597` → IC=+0.156 (n=2742)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1597 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.343` → IC=+0.147 (n=663)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 9.343 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.8525` → IC=+0.155 (n=1826)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8525 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2952` → IC=+0.175 (n=411)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2952 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.8021` → IC=+0.132 (n=1727)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.8021 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `1.4194` → IC=+0.128 (n=2589)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.4194 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `6251.2816` → IC=+0.188 (n=1242)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 6251.2816 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `108.0` → IC=+0.135 (n=2245)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 108.0 (IC base=+0.128)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.175 (n=965)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0124 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=2957)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.4737` → IC=+0.210 (n=2892)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4737 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.1987` → IC=+0.191 (n=1589)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1987 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.152` → IC=+0.291 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.152 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `1.1752` → IC=+0.133 (n=2889)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.1752 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.7049` → IC=+0.124 (n=2581)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.7049 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` < `0.1633` → IC=+0.130 (n=2945)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1633 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.5416` → IC=+0.138 (n=1234)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.5416 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.125 (n=3013)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2660.8307` → IC=+0.201 (n=1310)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2660.8307 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.145 (n=1251)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 21.0 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0117` → IC=+0.143 (n=3003)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0117 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.1117` → IC=+0.162 (n=1001)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1117 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=3068)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.6429` → IC=+0.219 (n=3004)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6429 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` < `0.2101` → IC=+0.146 (n=2921)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.2101 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.313` → IC=+0.138 (n=2648)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 2.313 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.1776` → IC=+0.129 (n=3002)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1776 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.2745` → IC=+0.132 (n=414)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.2745 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4332` → IC=+0.130 (n=943)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.4332 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `2.4341` → IC=+0.127 (n=943)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.4341 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2536.3138` → IC=+0.186 (n=1361)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2536.3138 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.124 (n=2822)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 46.0 (IC base=+0.119)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.250 (n=2360)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0131 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1657` → IC=+0.241 (n=1162)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1657 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.228 (n=2742)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.231 (n=2380)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.259 (n=2641)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.1803` → IC=+0.234 (n=1656)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1803 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` < `0.817` → IC=+0.226 (n=2710)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.817 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.503` → IC=+0.261 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.503 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.6249` → IC=+0.234 (n=2643)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6249 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2349` → IC=+0.269 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2349 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.8145` → IC=+0.235 (n=1716)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8145 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2556.3782` → IC=+0.233 (n=1761)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2556.3782 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.239 (n=1181)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0227` → IC=+0.251 (n=1220)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0227 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.085` → IC=+0.264 (n=896)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.085 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.254 (n=1311)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.245 (n=1202)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.44` → IC=+0.264 (n=2693)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.44 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `0.3035` → IC=+0.246 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3035 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.209` → IC=+0.269 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.209 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` < `0.8655` → IC=+0.241 (n=1789)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8655 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` > `0.6411` → IC=+0.241 (n=2682)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6411 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.288 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `2.5331` → IC=+0.235 (n=2519)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5331 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `1.4358` → IC=+0.240 (n=2519)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4358 (IC base=+0.238)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.207 (n=1352)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.1316` → IC=+0.182 (n=1776)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.1316 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.177 (n=4238)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `0.3201` → IC=+0.200 (n=4035)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3201 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.8117` → IC=+0.195 (n=643)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.8117 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.697` → IC=+0.205 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.697 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `0.8641` → IC=+0.181 (n=2444)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.8641 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` > `1.1944` → IC=+0.174 (n=1222)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 1.1944 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.0989` → IC=+0.173 (n=1445)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.0989 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `1.5342` → IC=+0.171 (n=1729)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5342 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.168 (n=4525)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.02 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `2633.3465` → IC=+0.177 (n=3605)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 2633.3465 (IC base=+0.166)

- **PATRÓN** `ibs_20min` < `0.1986` → IC=+0.194 (n=1905)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.1986 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.129 (n=1842)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 26.0 (IC base=+0.088)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.196 (n=1099)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.006 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.101` → IC=+0.231 (n=484)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.101 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.213 (n=993)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `0.2144` → IC=+0.211 (n=1098)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2144 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `0.3087` → IC=+0.214 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3087 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.957` → IC=+0.201 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.957 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.399` → IC=+0.179 (n=1156)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 6.399 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `0.8803` → IC=+0.193 (n=733)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.8803 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` < `0.1499` → IC=+0.181 (n=1157)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.1499 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.0705` → IC=+0.188 (n=434)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.0705 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` < `2.1894` → IC=+0.192 (n=948)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.1894 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `15863.0179` → IC=+0.192 (n=498)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 15863.0179 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `159.0` → IC=+0.185 (n=475)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 159.0 (IC base=+0.178)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.170 (n=444)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.003 (IC base=+0.097)

- **PATRÓN** `ibs_20min` < `0.1952` → IC=+0.197 (n=586)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.1952 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.1608` → IC=+0.140 (n=348)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.1608 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `160.0` → IC=+0.174 (n=575)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 160.0 (IC base=+0.097)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.242 (n=552)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.2091` → IC=+0.189 (n=833)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.2091 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=1303)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.8185` → IC=+0.273 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8185 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.8048` → IC=+0.191 (n=208)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.8048 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` < `0.2075` → IC=+0.182 (n=1113)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.2075 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.898` → IC=+0.219 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.898 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.836` → IC=+0.197 (n=832)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.836 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` > `1.16` → IC=+0.184 (n=416)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 1.16 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.1583` → IC=+0.206 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1583 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `1.4263` → IC=+0.184 (n=410)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.4263 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `1.7873` → IC=+0.195 (n=820)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.7873 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.1016` → IC=+0.186 (n=409)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.1016 (IC base=+0.072)

- **PATRÓN** `libro_liquidez` > `8099.017` → IC=+0.143 (n=556)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 8099.017 (IC base=+0.072)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.151 (n=437)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.007 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.173 (n=707)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 11.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.191 (n=992)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.4706 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `0.9739` → IC=+0.205 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9739 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.017` → IC=+0.238 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.017 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `1.0509` → IC=+0.141 (n=873)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.0509 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` > `0.7048` → IC=+0.134 (n=887)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 0.7048 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2257` → IC=+0.161 (n=184)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.2257 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.4223` → IC=+0.146 (n=320)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4223 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `1.7996` → IC=+0.129 (n=639)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.7996 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.134 (n=1046)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `2723.2049` → IC=+0.173 (n=450)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2723.2049 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.2105` → IC=+0.213 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2105 (IC base=+0.055)

- **PATRÓN** `libro_liquidez` > `2847.0357` → IC=+0.157 (n=357)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2847.0357 (IC base=+0.055)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0164` → IC=+0.239 (n=220)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0164 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.233 (n=155)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` > `0.7308` → IC=+0.220 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7308 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` > `0.3083` → IC=+0.218 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3083 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.634` → IC=+0.209 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.634 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` > `1.0332` → IC=+0.222 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0332 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` < `0.1101` → IC=+0.199 (n=290)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.1101 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` < `1.8284` → IC=+0.209 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8284 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `1.5411` → IC=+0.196 (n=268)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.5411 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.192 (n=365)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.03 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `2513.635` → IC=+0.215 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2513.635 (IC base=+0.184)

- **PATRÓN** `sigma_h` > `0.0237` → IC=+0.220 (n=162)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0237 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.2745` → IC=+0.154 (n=238)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.2745 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.200 (n=168)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.51` → IC=+0.164 (n=316)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.51 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `1.1213` → IC=+0.239 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1213 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.225` → IC=+0.184 (n=96)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 5.225 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.234` → IC=+0.144 (n=318)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 2.234 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.872` → IC=+0.179 (n=238)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.872 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.113` → IC=+0.151 (n=325)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.113 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.191 (n=66)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.5346` → IC=+0.198 (n=114)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.5346 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `2.6826` → IC=+0.164 (n=114)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.6826 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.154 (n=339)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 20.0 (IC base=+0.144)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.233 (n=6892)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=21542)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.4334` → IC=+0.229 (n=20661)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4334 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.8824` → IC=+0.214 (n=2509)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8824 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.023` → IC=+0.254 (n=5062)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.023 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.2177` → IC=+0.161 (n=13898)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2177 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2415` → IC=+0.206 (n=3721)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2415 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6202` → IC=+0.193 (n=6719)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6202 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.202 (n=19312)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 106.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.197 (n=8336)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0059 (IC base=+0.192)

- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.199 (n=6310)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.4818` → IC=+0.196 (n=18905)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.4818 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=7021)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` < `0.5909` → IC=+0.243 (n=18904)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5909 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` < `0.1786` → IC=+0.175 (n=11782)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.1786 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.543` → IC=+0.201 (n=2564)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.543 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.437` → IC=+0.196 (n=18410)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` < 3.437 (IC base=+0.192)

- **PATRÓN** `volumen_regimen` < `0.6331` → IC=+0.174 (n=4236)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6331 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` > `0.2917` → IC=+0.251 (n=2586)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2917 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `2.6295` → IC=+0.203 (n=6013)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6295 (IC base=+0.192)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.208 (n=17794)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.192)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.249 (n=1606)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.235 (n=2244)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` > `0.8623` → IC=+0.302 (n=2215)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8623 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.655` → IC=+0.338 (n=1082)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.655 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2327` → IC=+0.294 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2327 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.2784` → IC=+0.239 (n=1453)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2784 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.249 (n=3632)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2064.165` → IC=+0.235 (n=1108)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2064.165 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.253 (n=2057)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.234)

- **PATRÓN** `sigma_h` < `0.0099` → IC=+0.268 (n=2942)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0099 (IC base=+0.266)

- **PATRÓN** `drift_60min` |x|≤ `0.1226` → IC=+0.290 (n=1290)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1226 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.269 (n=2698)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.266)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.267 (n=2667)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` < `0.5368` → IC=+0.285 (n=2932)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5368 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` < `0.0962` → IC=+0.267 (n=2659)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0962 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` > `0.289` → IC=+0.288 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.289 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` < `1.5615` → IC=+0.266 (n=1233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5615 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` > `2.6564` → IC=+0.275 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6564 (IC base=+0.266)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.267 (n=3368)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.266)

- **PATRÓN** `libro_liquidez` > `1769.6091` → IC=+0.275 (n=1954)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1769.6091 (IC base=+0.266)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.274 (n=1271)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.266)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.179 (n=1135)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0031 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0786` → IC=+0.149 (n=1129)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.0786 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=3524)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.2053` → IC=+0.189 (n=3383)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2053 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.3218` → IC=+0.198 (n=1133)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.3218 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.238` → IC=+0.162 (n=542)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.238 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6365` → IC=+0.155 (n=1128)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6365 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.0743` → IC=+0.138 (n=1534)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 1.0743 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.272` → IC=+0.180 (n=485)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.272 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.1556` → IC=+0.142 (n=2920)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.1556 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.5138` → IC=+0.140 (n=2965)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.5138 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `307.0` → IC=+0.150 (n=2190)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 307.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.161 (n=2879)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0063 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0793` → IC=+0.171 (n=960)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.0793 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.168 (n=1050)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.6828` → IC=+0.184 (n=2879)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6828 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1407` → IC=+0.152 (n=2756)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1407 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.046` → IC=+0.144 (n=1370)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 3.046 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.1917` → IC=+0.147 (n=2879)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.1917 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2185` → IC=+0.190 (n=534)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2185 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.4123` → IC=+0.144 (n=924)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4123 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.7752` → IC=+0.142 (n=1846)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.7752 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=3736)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `228.0` → IC=+0.152 (n=897)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 228.0 (IC base=+0.137)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.244 (n=2297)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=3606)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=3085)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=1287)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.115` → IC=+0.320 (n=761)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.115 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` < `0.132` → IC=+0.227 (n=3256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.132 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `2.7388` → IC=+0.238 (n=1524)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7388 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.231 (n=4135)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `1378.3384` → IC=+0.229 (n=3442)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1378.3384 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.247 (n=2880)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.1791` → IC=+0.262 (n=1437)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1791 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.266 (n=1232)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.242 (n=1495)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.0556` → IC=+0.304 (n=1093)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0556 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.291` → IC=+0.302 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.291 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.3488` → IC=+0.305 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3488 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `2.1664` → IC=+0.255 (n=2091)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1664 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.249 (n=1660)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `2024.2984` → IC=+0.253 (n=1089)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2024.2984 (IC base=+0.242)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.250 (n=2731)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.242)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.195 (n=1191)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0036 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.4329` → IC=+0.149 (n=3565)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4329 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.150 (n=3703)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.8929` → IC=+0.277 (n=1190)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8929 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.1963` → IC=+0.167 (n=1660)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1963 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.986` → IC=+0.159 (n=1589)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 2.986 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.156 (n=2377)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8616 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2331` → IC=+0.185 (n=629)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2331 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.5179` → IC=+0.156 (n=1533)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.5179 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.178` → IC=+0.144 (n=1580)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.178 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `5434.3244` → IC=+0.231 (n=1617)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5434.3244 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.150 (n=2301)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 91.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.158 (n=2994)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0077 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.444` → IC=+0.149 (n=2994)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.444 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.166 (n=1096)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.7157` → IC=+0.193 (n=2993)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.7157 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.1518` → IC=+0.152 (n=2766)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1518 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.93` → IC=+0.159 (n=446)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 10.93 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.11` → IC=+0.140 (n=2607)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 3.11 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.6157` → IC=+0.158 (n=998)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.6157 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.212 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.215` → IC=+0.142 (n=2541)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.215 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.5364` → IC=+0.147 (n=2579)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.5364 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `6321.4176` → IC=+0.214 (n=998)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6321.4176 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.151 (n=1947)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 93.0 (IC base=+0.139)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.151 (n=1638)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0111 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.151 (n=2550)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 11.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.4333` → IC=+0.193 (n=3609)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.4333 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `1.0166` → IC=+0.209 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0166 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.36` → IC=+0.267 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.36 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `0.8783` → IC=+0.133 (n=2407)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8783 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.101` → IC=+0.123 (n=3423)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.101 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.8238` → IC=+0.127 (n=2351)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.8238 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.121 (n=3769)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2714.4195` → IC=+0.242 (n=1203)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2714.4195 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.132 (n=1135)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 20.0 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.155 (n=3005)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0107 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.1373` → IC=+0.153 (n=1138)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1373 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.160 (n=1600)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 15.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.6604` → IC=+0.216 (n=3409)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6604 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` < `0.2182` → IC=+0.144 (n=3061)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.2182 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.086` → IC=+0.150 (n=3293)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 3.086 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `1.195` → IC=+0.136 (n=3409)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.195 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2253` → IC=+0.175 (n=595)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2253 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.4331` → IC=+0.159 (n=1076)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4331 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `2620.7147` → IC=+0.207 (n=1136)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2620.7147 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.139 (n=3251)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 51.0 (IC base=+0.127)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0138` → IC=+0.259 (n=2985)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0138 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.242 (n=3489)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.243 (n=2232)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `0.615` → IC=+0.273 (n=2986)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.615 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `0.1917` → IC=+0.255 (n=1764)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1917 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.223` → IC=+0.285 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.223 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` < `1.2209` → IC=+0.239 (n=3341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2209 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` > `0.6442` → IC=+0.241 (n=3341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6442 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2391` → IC=+0.262 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2391 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.5042` → IC=+0.258 (n=1088)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5042 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `2957.795` → IC=+0.245 (n=1114)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2957.795 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0258` → IC=+0.264 (n=1143)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0258 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.252 (n=1676)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.5208` → IC=+0.273 (n=3427)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5208 (IC base=+0.240)

- **PATRÓN** `dist_vwap_pct` < `0.2162` → IC=+0.247 (n=3221)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2162 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.162` → IC=+0.279 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.162 (IC base=+0.240)

- **PATRÓN** `volumen_regimen` > `1.2152` → IC=+0.262 (n=1143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2152 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.2859` → IC=+0.304 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2859 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `1.4324` → IC=+0.242 (n=3219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4324 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.239 (n=3172)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.240)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=5751)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.245 (n=1967)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.5031` → IC=+0.226 (n=5895)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5031 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=2129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` > `0.9333` → IC=+0.255 (n=1965)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9333 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` < `0.4279` → IC=+0.221 (n=4308)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4279 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.574` → IC=+0.225 (n=1930)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.574 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` < `0.7092` → IC=+0.229 (n=1921)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7092 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` > `0.8841` → IC=+0.220 (n=2910)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8841 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` < `0.1055` → IC=+0.219 (n=5496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1055 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.1653` → IC=+0.223 (n=1667)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1653 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `2.2548` → IC=+0.221 (n=5106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2548 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.225 (n=4625)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `3758.8412` → IC=+0.227 (n=3930)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3758.8412 (IC base=+0.217)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.237 (n=1446)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.4924` → IC=+0.212 (n=4325)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4924 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=1455)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.214 (n=1913)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.0883` → IC=+0.210 (n=1442)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0883 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.6584` → IC=+0.210 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6584 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.779` → IC=+0.211 (n=3881)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.779 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `1.0952` → IC=+0.205 (n=3628)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0952 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.201 (n=3982)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.200 (n=1931)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `1.5316` → IC=+0.203 (n=1876)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5316 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.1859` → IC=+0.207 (n=1933)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1859 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=5751)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `169.0` → IC=+0.212 (n=3744)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 169.0 (IC base=+0.199)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.276 (n=814)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.269)

- **PATRÓN** `drift_60min` |x|≤ `0.0846` → IC=+0.297 (n=309)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0846 (IC base=+0.269)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.279 (n=925)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.269)

- **PATRÓN** `ibs_20min` < `0.8328` → IC=+0.278 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.8328 (IC base=+0.269)

- **PATRÓN** `dist_vwap_pct` < `0.6679` → IC=+0.277 (n=1076)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6679 (IC base=+0.269)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.118` → IC=+0.300 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.118 (IC base=+0.269)

- **PATRÓN** `volumen_regimen` < `1.2212` → IC=+0.271 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2212 (IC base=+0.269)

- **PATRÓN** `volumen_regimen` > `0.8749` → IC=+0.288 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8749 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.351 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` < `2.4907` → IC=+0.276 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4907 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` > `2.1895` → IC=+0.269 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1895 (IC base=+0.269)

- **PATRÓN** `libro_liquidez` > `12909.5134` → IC=+0.279 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12909.5134 (IC base=+0.269)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.263 (n=509)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.3854` → IC=+0.190 (n=1518)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.3854 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=557)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.185 (n=564)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 5.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` < `0.138` → IC=+0.197 (n=668)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.138 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.6955` → IC=+0.197 (n=140)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.6955 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.315` → IC=+0.199 (n=1487)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 6.315 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `1.2377` → IC=+0.185 (n=1518)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 1.2377 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.1521` → IC=+0.194 (n=462)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1521 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` < `2.4929` → IC=+0.182 (n=1510)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.4929 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `2.1703` → IC=+0.180 (n=685)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.1703 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `14605.0565` → IC=+0.180 (n=688)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 14605.0565 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `686.0` → IC=+0.188 (n=1473)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 686.0 (IC base=+0.176)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.216 (n=589)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.5864` → IC=+0.204 (n=882)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5864 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=341)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` < `0.712` → IC=+0.200 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.712 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.240 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.494` → IC=+0.244 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.494 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.2073` → IC=+0.232 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2073 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `1.8048` → IC=+0.203 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8048 (IC base=+0.196)

- **PATRÓN** `ballena_activa_n` < `5.0` → IC=+0.202 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 5.0 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.0116` → IC=+0.242 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0116 (IC base=+0.228)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.286 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.009 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.295 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `0.216` → IC=+0.258 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.216 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.971` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.971 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` < `0.1317` → IC=+0.272 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1317 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` < `2.3165` → IC=+0.262 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3165 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `1.7721` → IC=+0.245 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7721 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `2388.306` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2388.306 (IC base=+0.228)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.220 (n=1620)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.4542` → IC=+0.214 (n=1620)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4542 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.225 (n=568)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` < `0.4996` → IC=+0.218 (n=1080)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4996 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.8568` → IC=+0.207 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8568 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.3956` → IC=+0.217 (n=1621)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3956 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.508` → IC=+0.211 (n=1646)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.508 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `0.7054` → IC=+0.212 (n=713)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7054 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `1.2249` → IC=+0.207 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2249 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` < `0.1032` → IC=+0.210 (n=1491)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1032 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `2.4455` → IC=+0.213 (n=1585)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4455 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=1683)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.242 (n=448)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.4865` → IC=+0.221 (n=1340)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4865 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.211 (n=506)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.216 (n=907)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.75` → IC=+0.203 (n=1340)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.75 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.0909` → IC=+0.205 (n=1340)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0909 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `0.6238` → IC=+0.217 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6238 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.351` → IC=+0.205 (n=1222)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.351 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `0.6391` → IC=+0.228 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6391 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.0738` → IC=+0.226 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0738 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.1885` → IC=+0.206 (n=1156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1885 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.7831` → IC=+0.202 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7831 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `6511.755` → IC=+0.206 (n=1197)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6511.755 (IC base=+0.200)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0097` → IC=+0.223 (n=622)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0097 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.232 (n=644)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.275 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.196)

- **PATRÓN** `dist_vwap_pct` > `0.7605` → IC=+0.242 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7605 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.21` → IC=+0.222 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.21 (IC base=+0.196)

- **PATRÓN** `volumen_regimen` < `0.643` → IC=+0.244 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.643 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.205 (n=838)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.0799` → IC=+0.202 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0799 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` < `2.1469` → IC=+0.201 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1469 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `1.4746` → IC=+0.202 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4746 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.204 (n=1107)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `4318.6372` → IC=+0.238 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4318.6372 (IC base=+0.196)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.201 (n=811)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.222 (n=605)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0118 (IC base=+0.222)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.237 (n=458)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.5971` → IC=+0.240 (n=687)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5971 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.222 (n=639)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.250 (n=478)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.7308` → IC=+0.249 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7308 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.5335` → IC=+0.223 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5335 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.788` → IC=+0.235 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.788 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` < `1.0973` → IC=+0.226 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0973 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `1.2826` → IC=+0.227 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2826 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` < `0.0825` → IC=+0.239 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0825 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.5701` → IC=+0.264 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5701 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `3258.9665` → IC=+0.237 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3258.9665 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.258 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=+0.222)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.149 (n=688)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0037 (IC base=+0.054)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.189 (n=1320)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.75 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` > `0.149` → IC=+0.140 (n=988)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.149 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.621` → IC=+0.145 (n=435)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 10.621 (IC base=+0.054)

- **PATRÓN** `ibs_20min` < `0.0508` → IC=+0.263 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0508 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.1437` → IC=+0.124 (n=362)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.1437 (IC base=+0.045)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.3865` → IC=-0.151 (n=210)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3865
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=631)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.178 (n=293)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0031 (IC base=+0.071)

- **PATRÓN** `ibs_20min` > `0.3865` → IC=+0.146 (n=631)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.3865 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` > `0.1218` → IC=+0.163 (n=307)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1218 (IC base=+0.071)

- **PATRÓN** `ibs_20min` < `0.0742` → IC=+0.280 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0742 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.2162` → IC=+0.160 (n=104)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2162 (IC base=+0.050)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.5205` → IC=-0.121 (n=280)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5205
  - _Potencial_: sin este filtro IC_bueno=+0.173 (n=570)

- **FILTRO** `ibs_20min` > `0.6985` → IC=-0.171 (n=141)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6985
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=424)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.143 (n=295)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.004 (IC base=+0.072)

- **PATRÓN** `ibs_20min` > `0.7811` → IC=+0.224 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7811 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` > `0.1272` → IC=+0.176 (n=319)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.1272 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.717` → IC=+0.204 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.717 (IC base=+0.072)

- **PATRÓN** `ibs_20min` < `0.0322` → IC=+0.257 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0322 (IC base=+0.018)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.981` → IC=+0.202 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.981 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.721` → IC=+0.140 (n=162)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.721 (IC base=+0.022)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.724` → IC=+0.136 (n=149)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 8.724 (IC base=+0.022)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.151 (n=339)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0112 (IC base=+0.067)

- **PATRÓN** `ibs_20min` < `0.4857` → IC=+0.170 (n=355)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.4857 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` < `0.2741` → IC=+0.123 (n=361)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.2741 (IC base=+0.067)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.903` → IC=+0.300 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.903 (IC base=+0.067)

- **PATRÓN** `volumen_regimen` > `1.1045` → IC=+0.167 (n=118)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.1045 (IC base=+0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.1508` → IC=+0.154 (n=105)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.1508 (IC base=+0.067)

- **PATRÓN** `volumen_spike_ratio` > `1.5463` → IC=+0.120 (n=293)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_spike_ratio` > 1.5463 (IC base=+0.067)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1871` → IC=-0.295 (n=86)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=261)

- **FILTRO** `dist_vwap_pct` > `0.2402` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2402
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=334)

- **FILTRO** `libro_liquidez` < `902.1333` → IC=-0.219 (n=87)

  - _Acción_: SKIP cuando `libro_liquidez` < 902.1333
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=262)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.295 (n=76)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.283 (n=242)

- **FILTRO** `dist_vwap_pct` > `0.3644` → IC=-0.406 (n=30)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3644
  - _Potencial_: sin este filtro IC_bueno=-0.272 (n=288)

- **FILTRO** `sigma_ewma_delta_pct` > `9.955` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.955
  - _Potencial_: sin este filtro IC_bueno=-0.282 (n=291)

- **FILTRO** `volumen_pendiente_norm` > `0.0448` → IC=-0.379 (n=31)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0448
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=199)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` < `0.0059` → IC=-0.241 (n=79)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0059
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=27)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.280 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=58)

- **FILTRO** `volumen_regimen` < `0.8856` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8856
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=80)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.257 (n=72)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=73)

- **FILTRO** `ibs_20min` > `0.7502` → IC=-0.265 (n=49)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7502
  - _Potencial_: sin este filtro IC_bueno=-0.245 (n=96)

- **FILTRO** `volumen_regimen` > `0.805` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.230 (n=109)

- **FILTRO** `libro_liquidez` < `5514.5282` → IC=-0.255 (n=108)

  - _Acción_: SKIP cuando `libro_liquidez` < 5514.5282
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=37)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.5777` → IC=-0.468 (n=29)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5777
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=88)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.365 (n=35)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=87)

- **FILTRO** `ibs_20min` > `0.6985` → IC=-0.407 (n=41)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6985
  - _Potencial_: sin este filtro IC_bueno=-0.259 (n=81)

- **FILTRO** `volumen_spike_ratio` < `1.7371` → IC=-0.370 (n=44)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.7371
  - _Potencial_: sin este filtro IC_bueno=-0.261 (n=44)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.307 (n=107)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.400 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=108)

- **FILTRO** `volumen_regimen` < `0.8232` → IC=-0.314 (n=41)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8232
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=85)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.242 (n=29)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=97)

- **FILTRO** `sigma_h` < `0.0107` → IC=-0.325 (n=38)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0107
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=36)

- **FILTRO** `dist_vwap_pct` > `0.3005` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3005
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=34)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.25` → IC=-0.152 (n=251)

  - _Acción_: SKIP cuando `ibs_20min` > 0.25
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=754)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.218 (n=214)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.189 (n=329)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `0.6732` → IC=+0.175 (n=642)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.6732 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.7712` → IC=+0.271 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7712 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.656` → IC=+0.143 (n=351)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 3.656 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.625` → IC=+0.181 (n=214)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.625 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` < `0.2099` → IC=+0.160 (n=598)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` < 0.2099 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.4024` → IC=+0.156 (n=536)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4024 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.1381` → IC=+0.120 (n=664)

  - _Acción_: Kelly boost +0.60€ cuando `ibs_20min` < 0.1381 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.784` → IC=+0.154 (n=218)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 8.784 (IC base=+0.035)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.7127` → IC=-0.146 (n=63)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7127
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=192)

- **PATRÓN** `dist_vwap_pct` > `0.5672` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.5672 (IC base=+0.021)

- **PATRÓN** `ibs_20min` < `0.2252` → IC=+0.165 (n=353)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.2252 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.348` → IC=+0.134 (n=80)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 11.348 (IC base=+0.095)

- **PATRÓN** `volumen_pendiente_norm` > `0.2688` → IC=+0.127 (n=57)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.2688 (IC base=+0.095)

- **PATRÓN** `volumen_spike_ratio` > `1.7675` → IC=+0.130 (n=214)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.7675 (IC base=+0.095)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1257` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1257
  - _Potencial_: sin este filtro IC_bueno=+0.164 (n=206)

- **FILTRO** `ibs_20min` > `0.1452` → IC=-0.126 (n=121)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1452
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=237)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.148 (n=140)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0041 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.1946` → IC=+0.127 (n=140)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.1946 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.189 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 18.0 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.130 (n=71)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.8015` → IC=+0.156 (n=187)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.8015 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` < `0.0967` → IC=+0.138 (n=172)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.0967 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.502` → IC=+0.147 (n=219)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 9.502 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `0.6244` → IC=+0.181 (n=70)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6244 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.1257` → IC=+0.164 (n=206)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` < 0.1257 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `2.1187` → IC=+0.154 (n=160)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.1187 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=179)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.828` → IC=+0.202 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.828 (IC base=+0.008)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2` → IC=-0.233 (n=58)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=119)

- **FILTRO** `dist_vwap_pct` > `0.1813` → IC=-0.167 (n=37)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1813
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=140)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.292 (n=171)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.274 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `0.6943` → IC=+0.397 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6943 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.903` → IC=+0.344 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.903 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` < `0.5991` → IC=+0.295 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5991 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.305 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.4721` → IC=+0.321 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4721 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.3741` → IC=+0.281 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3741 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.977` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.977 (IC base=-0.070)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.312 (n=94)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3447` → IC=+0.324 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3447 (IC base=+0.314)

- **PATRÓN** `elapsed_s` > `187.1` → IC=+0.365 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 187.1 (IC base=+0.314)

- **PATRÓN** `drift_15min` |x|≤ `2.6528` → IC=+0.351 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.6528 (IC base=+0.314)

- **PATRÓN** `drift_60min` |x|≤ `0.9568` → IC=+0.378 (n=72)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9568 (IC base=+0.314)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.388 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.314)

- **PATRÓN** `ballena_activa_n` < `1067.0` → IC=+0.385 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1067.0 (IC base=+0.314)

- **PATRÓN** `drift_ventana_pct` |x|> `0.4356` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4356 (IC base=+0.243)

- **PATRÓN** `elapsed_s` < `203.0` → IC=+0.259 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 203.0 (IC base=+0.243)

- **PATRÓN** `drift_15min` |x|≤ `1.234` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.234 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.6365` → IC=+0.276 (n=56)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6365 (IC base=+0.243)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.312 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.243)

- **PATRÓN** `ballena_activa_n` < `1342.0` → IC=+0.328 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1342.0 (IC base=+0.243)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.312 (n=94)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3447` → IC=+0.324 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3447 (IC base=+0.314)

- **PATRÓN** `elapsed_s` > `187.1` → IC=+0.365 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 187.1 (IC base=+0.314)

- **PATRÓN** `drift_15min` |x|≤ `2.6528` → IC=+0.351 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.6528 (IC base=+0.314)

- **PATRÓN** `drift_60min` |x|≤ `0.9568` → IC=+0.378 (n=72)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9568 (IC base=+0.314)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.388 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.314)

- **PATRÓN** `ballena_activa_n` < `1067.0` → IC=+0.385 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1067.0 (IC base=+0.314)

- **PATRÓN** `drift_ventana_pct` |x|> `0.4356` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4356 (IC base=+0.243)

- **PATRÓN** `elapsed_s` < `203.0` → IC=+0.259 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 203.0 (IC base=+0.243)

- **PATRÓN** `drift_15min` |x|≤ `1.234` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.234 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.6365` → IC=+0.276 (n=56)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6365 (IC base=+0.243)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.312 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.243)

- **PATRÓN** `ballena_activa_n` < `1342.0` → IC=+0.328 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1342.0 (IC base=+0.243)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=239)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=239)

- **FILTRO** `libro_liquidez` < `2998.5952` → IC=-0.177 (n=63)

  - _Acción_: SKIP cuando `libro_liquidez` < 2998.5952
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=192)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=604)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `11321.3584` → IC=-0.167 (n=31)

  - _Acción_: SKIP cuando `libro_liquidez` < 11321.3584
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=95)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `4139.65` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `liq_usd_total` < 4139.65
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=27)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=30)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.172 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 6.0 (IC base=+0.058)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `liq_n` < `7.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `liq_n` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `libro_liquidez` < `2892.3985` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 2892.3985
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=3882)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=118)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=118)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=22)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=15)

- **FILTRO** `libro_liquidez` < `13988.6712` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 13988.6712
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

- **FILTRO** `ballena_activa_n` > `558.0` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `ballena_activa_n` > 558.0
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.121 (n=270)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.495 (IC base=+0.022)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1585)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=1539)

- **FILTRO** `liq_n` < `3.0` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `liq_n` < 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `liq_usd_total` < `6520.36` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `liq_usd_total` < 6520.36
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.286 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `ballena_activa_n` > `133.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `ballena_activa_n` > 133.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=723)

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
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=440)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=421)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.147 (n=185)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.495 (IC base=+0.022)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=952)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=952)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.128 (n=294)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=738)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1130)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1130)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=259)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=259)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.141 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=321)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=368)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=292)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=386)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=386)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=231)

- **FILTRO** `libro_liquidez` < `657.5195` → IC=-0.133 (n=137)

  - _Acción_: SKIP cuando `libro_liquidez` < 657.5195
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=279)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=322)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.145 (n=29)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=69)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.176 (n=69)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=87)

- **FILTRO** `py_entrada` > `0.53` → IC=-0.140 (n=48)

  - _Acción_: SKIP cuando `py_entrada` > 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=28)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.269 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=52)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.47` → IC=+0.152 (n=219)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.47 (IC base=-0.009)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.142 (n=252)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=518)

- **FILTRO** `profundidad_ratio` < `62.0` → IC=-0.121 (n=254)

  - _Acción_: SKIP cuando `profundidad_ratio` < 62.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=516)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.132 (n=308)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=325)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.172 (n=132)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=568)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.123 (n=468)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=251)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.141 (n=104)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=325)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.152 (n=271)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=574)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=7798)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2151.302` → IC=-0.153 (n=47)

  - _Acción_: SKIP cuando `libro_liquidez` < 2151.302
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=143)

### MOMENTUM_IBS_15M#BTC#15min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=1058)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=2289)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1413)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.46` → IC=-0.172 (n=7235)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=23314)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.174 (n=7745)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=23724)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.185 (n=1400)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=4232)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.146 (n=1865)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=3724)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.136 (n=1472)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 1.0 (IC base=+0.043)

- **PATRÓN** `libro_liquidez` > `1866.2952` → IC=+0.140 (n=1408)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 1866.2952 (IC base=+0.043)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.124 (n=2870)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.505 (IC base=+0.013)

- **PATRÓN** `libro_liquidez` > `1136.175` → IC=+0.152 (n=1901)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1136.175 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.170 (n=1002)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=3300)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.180 (n=1098)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3347)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.205 (n=1379)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=4334)

- **PATRÓN** `ibs_20min` > `0.9643` → IC=+0.133 (n=1920)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 0.9643 (IC base=+0.036)

- **PATRÓN** `libro_liquidez` > `1345.8584` → IC=+0.121 (n=2816)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 1345.8584 (IC base=+0.036)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.155 (n=1403)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=4264)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2425)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=2349)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2934)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3886)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `14.0` → IC=-0.157 (n=135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=437)

- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=447)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `ibs_20min` < `0.1975` → IC=-0.223 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1975
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=224)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.204 (n=113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=350)

- **FILTRO** `drift_20min_pct` |x|> `0.1569` → IC=-0.148 (n=157)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1569
  - _Potencial_: sin este filtro IC_bueno=-0.114 (n=306)

- **FILTRO** `libro_liquidez` < `3195.1545` → IC=-0.182 (n=152)

  - _Acción_: SKIP cuando `libro_liquidez` < 3195.1545
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=311)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=961)

- **FILTRO** `libro_liquidez` < `1813.405` → IC=-0.164 (n=245)

  - _Acción_: SKIP cuando `libro_liquidez` < 1813.405
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=735)

- **FILTRO** `ibs_20min` > `0.8824` → IC=-0.137 (n=576)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8824
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=579)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.211 (n=278)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=868)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=234)

### MOMENTUM_IBS_5M#BNB#5min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=44)

- **FILTRO** `drift_7min_pct` |x|> `0.0725` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0725
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=28)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0331` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_7min_pct` |x|≤ 0.0331 (IC base=-0.026)

### MOMENTUM_IBS_5M#BTC#5min
- **FILTRO** `hora_utc` > `18.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=91)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.125 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 17.0 (IC base=+0.024)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.132 (n=20898)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=46853)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.297 (n=16059)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=51692)

- **FILTRO** `ibs_7min` < `0.2222` → IC=-0.232 (n=16906)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2222
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=50845)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.152 (n=22459)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=45292)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.243 (n=21174)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=63724)

- **FILTRO** `ibs_7min` > `0.2837` → IC=-0.183 (n=21219)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2837
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=63679)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.154 (n=2941)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=9064)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.318 (n=2924)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=9081)

- **FILTRO** `ibs_7min` < `0.7103` → IC=-0.250 (n=3961)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7103
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=8044)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.150 (n=2719)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=9286)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.277 (n=3527)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=11157)

- **FILTRO** `ibs_7min` > `0.7742` → IC=-0.213 (n=3669)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7742
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=11015)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.260 (n=2699)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=8621)

- **FILTRO** `ibs_7min` < `0.717` → IC=-0.205 (n=2829)

  - _Acción_: SKIP cuando `ibs_7min` < 0.717
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=8491)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.195 (n=2810)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=8510)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.268 (n=2635)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=8919)

- **FILTRO** `ibs_7min` > `0.2659` → IC=-0.193 (n=2887)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2659
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=8667)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.180 (n=2881)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=8673)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.164 (n=2791)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=8697)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.323 (n=2720)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=8768)

- **FILTRO** `ibs_7min` < `0.2875` → IC=-0.249 (n=3791)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2875
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=7697)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.198 (n=2395)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=9093)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.259 (n=3715)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=11819)

- **FILTRO** `ibs_7min` > `0.7319` → IC=-0.184 (n=3883)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7319
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=11651)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.263 (n=2691)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=8274)

- **FILTRO** `ibs_7min` < `0.7186` → IC=-0.192 (n=2741)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7186
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=8224)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.187 (n=2722)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=8243)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.258 (n=2629)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=8821)

- **FILTRO** `ibs_7min` > `0.2747` → IC=-0.174 (n=2861)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2747
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=8589)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.169 (n=2841)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=8609)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.295 (n=2543)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=8375)

- **FILTRO** `ibs_7min` < `0.7059` → IC=-0.228 (n=3582)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7059
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=7336)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.222 (n=2534)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=8384)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.195 (n=3956)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=12451)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=3551)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=7504)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.308 (n=2587)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=8468)

- **FILTRO** `ibs_7min` < `0.1739` → IC=-0.230 (n=2763)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1739
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=8292)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.203 (n=2519)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=8536)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.233 (n=3550)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=11719)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.160 (n=301)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=1007)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1293)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.156 (n=158)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=602)

- **FILTRO** `libro_liquidez` < `10485.1399` → IC=-0.156 (n=190)

  - _Acción_: SKIP cuando `libro_liquidez` < 10485.1399
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=570)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=879)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.123 (n=221)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=279)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.143 (n=166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=333)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=450)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.136 (n=97)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=668)

- **FILTRO** `libro_liquidez` < `3298.5458` → IC=-0.153 (n=191)

  - _Acción_: SKIP cuando `libro_liquidez` < 3298.5458
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=574)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4306` → IC=+0.155 (n=639)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.78€ cuando `delta_ratio` |x|> 0.4306 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.135 (n=723)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 6.0 (IC base=+0.125)

- **PATRÓN** `total_vol_5m` < `418.5531` → IC=+0.165 (n=470)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 418.5531 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `3545.3151` → IC=+0.140 (n=639)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3545.3151 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.132 (n=634)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 13.0 (IC base=+0.125)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.196 (n=166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 14.0 (IC base=+0.135)

- **PATRÓN** `total_vol_5m` < `377.422` → IC=+0.157 (n=298)

  - _Acción_: Kelly boost +0.78€ cuando `total_vol_5m` < 377.422 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `2527.6661` → IC=+0.230 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2527.6661 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.141 (n=151)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 6.0 (IC base=+0.135)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.4378` → IC=+0.153 (n=99)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio` |x|> 0.4378 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.142 (n=255)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 14.0 (IC base=+0.119)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4162` → IC=+0.194 (n=178)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.97€ cuando `delta_ratio` |x|> 0.4162 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.147 (n=281)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 4.0 (IC base=+0.131)

- **PATRÓN** `total_vol_5m` < `506.4056` → IC=+0.174 (n=179)

  - _Acción_: Kelly boost +0.87€ cuando `total_vol_5m` < 506.4056 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `5255.107` → IC=+0.132 (n=267)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 5255.107 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.195 (n=93)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 59.0 (IC base=+0.131)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.398` → IC=+0.168 (n=242)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.84€ cuando `delta_ratio` |x|> 0.398 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.186 (n=173)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.142)

- **PATRÓN** `total_vol_5m` < `6100.528` → IC=+0.170 (n=213)

  - _Acción_: Kelly boost +0.85€ cuando `total_vol_5m` < 6100.528 (IC base=+0.142)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `10.0` → IC=+0.141 (n=182)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 10.0 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=186)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.097)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.4417` → IC=-0.272 (n=55)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.4417
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=167)

- **FILTRO** `sigma_h` > `0.0076` → IC=-0.302 (n=195)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0076
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=589)

- **FILTRO** `T_h` > `129.5914` → IC=-0.170 (n=195)

  - _Acción_: SKIP cuando `T_h` > 129.5914
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=589)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.173 (n=197)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0038 (IC base=-0.080)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `87.9952` → IC=-0.229 (n=57)

  - _Acción_: SKIP cuando `T_h` > 87.9952
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=175)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.260 (n=77)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.034)

- **PATRÓN** `pct_vs_K` |x|≤ `1.632` → IC=+0.158 (n=77)

  - _Acción_: Kelly boost +0.79€ cuando `pct_vs_K` |x|≤ 1.632 (IC base=-0.034)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.01` → IC=-0.155 (n=27)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=54)

- **FILTRO** `T_h` > `88.6` → IC=-0.145 (n=60)

  - _Acción_: SKIP cuando `T_h` > 88.6
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=21)

- **FILTRO** `pct_vs_K` |x|> `6.9241` → IC=-0.259 (n=27)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.9241
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=54)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0142` → IC=-0.237 (n=36)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0142
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=112)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `T_h` < `146.0708` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `T_h` < 146.0708
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0109` → IC=-0.233 (n=541)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0109
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=181)

- **FILTRO** `T_h` > `97.9538` → IC=-0.229 (n=360)

  - _Acción_: SKIP cuando `T_h` > 97.9538
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=362)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.211 (n=154)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=463)

- **FILTRO** `pct_vs_K` |x|> `3.1362` → IC=-0.417 (n=154)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.1362
  - _Potencial_: sin este filtro IC_bueno=-0.137 (n=463)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.009` → IC=-0.201 (n=175)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.009
  - _Potencial_: sin este filtro IC_bueno=-0.123 (n=59)

- **FILTRO** `T_h` > `63.9952` → IC=-0.203 (n=156)

  - _Acción_: SKIP cuando `T_h` > 63.9952
  - _Potencial_: sin este filtro IC_bueno=-0.138 (n=78)

- **FILTRO** `T_h` > `143.7867` → IC=-0.237 (n=55)

  - _Acción_: SKIP cuando `T_h` > 143.7867
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=168)

- **FILTRO** `pct_vs_K` |x|> `2.9577` → IC=-0.377 (n=55)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9577
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=168)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `T_h` < `139.5329` → IC=-0.340 (n=23)

  - _Acción_: SKIP cuando `T_h` < 139.5329
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

- **FILTRO** `sigma_h` < `0.0066` → IC=-0.265 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0066
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=16)

- **FILTRO** `T_h` > `148.7378` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `T_h` > 148.7378
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=16)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.327 (n=131)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=70)

- **FILTRO** `T_h` > `98.1124` → IC=-0.294 (n=100)

  - _Acción_: SKIP cuando `T_h` > 98.1124
  - _Potencial_: sin este filtro IC_bueno=-0.248 (n=101)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.357 (n=47)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=142)

- **FILTRO** `sigma_h` < `0.0054` → IC=-0.194 (n=47)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0054
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=142)

- **FILTRO** `T_h` > `57.2342` → IC=-0.227 (n=126)

  - _Acción_: SKIP cuando `T_h` > 57.2342
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=63)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `T_h` < `132.3532` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `T_h` < 132.3532
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0082` → IC=-0.308 (n=50)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0082
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=153)

- **FILTRO** `T_h` > `70.1391` → IC=-0.221 (n=152)

  - _Acción_: SKIP cuando `T_h` > 70.1391
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=51)

- **FILTRO** `sigma_h` > `0.014` → IC=-0.312 (n=46)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.014
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=91)

- **FILTRO** `sigma_h` < `0.0082` → IC=-0.278 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0082
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=103)

- **FILTRO** `T_h` > `33.8406` → IC=-0.260 (n=102)

  - _Acción_: SKIP cuando `T_h` > 33.8406
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=35)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1195` → IC=+0.470 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1195 (IC base=+0.341)

- **PATRÓN** `sigma_h` < `0.013` → IC=+0.357 (n=96)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.013 (IC base=+0.341)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.380 (n=73)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.341)

- **PATRÓN** `T_h` < `0.3439` → IC=+0.397 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3439 (IC base=+0.341)

- **PATRÓN** `T_h` > `0.8789` → IC=+0.385 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8789 (IC base=+0.341)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.481 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.341)

- **PATRÓN** `edge` > `0.0997` → IC=+0.438 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.0997 (IC base=+0.404)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.408 (n=85)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.404)

- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.430 (n=170)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.404)

- **PATRÓN** `T_h` < `0.6127` → IC=+0.443 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6127 (IC base=+0.404)

- **PATRÓN** `T_h` > `1.4829` → IC=+0.408 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4829 (IC base=+0.404)

- **PATRÓN** `dist_50` > `0.4237` → IC=+0.452 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4237 (IC base=+0.404)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.416 (n=321)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.404)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1021` → IC=+0.300 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1021 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.278 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.194)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.237 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.194)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.265 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.269 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.194)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1023` → IC=+0.464 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.417)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.419 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0102 (IC base=+0.417)

- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.403 (n=60)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.417)

- **PATRÓN** `T_h` < `1.2415` → IC=+0.451 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.2415 (IC base=+0.417)

- **PATRÓN** `dist_50` > `0.4084` → IC=+0.482 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4084 (IC base=+0.417)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.414 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.417)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.444 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.417)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.175` → IC=+0.485 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.175 (IC base=+0.435)

- **PATRÓN** `sigma_h` < `0.0154` → IC=+0.467 (n=59)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0154 (IC base=+0.435)

- **PATRÓN** `T_h` > `0.3968` → IC=+0.457 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.3968 (IC base=+0.435)

- **PATRÓN** `dist_50` > `0.354` → IC=+0.471 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.354 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.435)

- **PATRÓN** `edge` > `0.2005` → IC=+0.470 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2005 (IC base=+0.462)

- **PATRÓN** `sigma_h` < `0.0162` → IC=+0.473 (n=148)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0162 (IC base=+0.462)

- **PATRÓN** `T_h` < `0.8229` → IC=+0.455 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.8229 (IC base=+0.462)

- **PATRÓN** `T_h` > `1.486` → IC=+0.481 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.486 (IC base=+0.462)

- **PATRÓN** `dist_50` > `0.4597` → IC=+0.492 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4597 (IC base=+0.462)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.467 (n=148)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.462)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=372)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=452)

- **PATRÓN** `streak_estiramiento` < `0.293` → IC=+0.167 (n=94)

  - _Acción_: Kelly boost +0.83€ cuando `streak_estiramiento` < 0.293 (IC base=+0.027)

- **PATRÓN** `streak_estiramiento` < `0.3595` → IC=+0.217 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.3595 (IC base=+0.058)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.158 (n=118)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 16.0 (IC base=+0.058)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.495 (IC base=+0.064)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=30)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=23)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.495 (IC base=+0.025)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `streak_estiramiento` > `0.4315` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4315
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=122)

- **PATRÓN** `streak_estiramiento` < `0.3805` → IC=+0.120 (n=106)

  - _Acción_: Kelly boost +0.60€ cuando `streak_estiramiento` < 0.3805 (IC base=+0.030)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.126 (n=153)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 7.0 (IC base=+0.094)

- **PATRÓN** `streak_estiramiento` < `0.5545` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `streak_estiramiento` < 0.5545 (IC base=+0.094)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.167 (n=142)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 32.0 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `2254.1726` → IC=+0.122 (n=149)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2254.1726 (IC base=+0.094)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=100)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=109)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.210 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=36)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=50)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=820)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` < `11.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=21)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=21)

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
- **PATRÓN** `regimen_ma_toques` > `4.0` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.045)

- **PATRÓN** `volumen_racha` < `16919.513` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_racha` < 16919.513 (IC base=+0.045)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=1054)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1336)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1244)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=1293)

### STRUCT_NO_15M
- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=36)

- **FILTRO** `libro_liquidez` < `6744.0765` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `libro_liquidez` < 6744.0765
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=4589)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=36)

- **FILTRO** `libro_liquidez` < `6744.0765` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `libro_liquidez` < 6744.0765
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=2643)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.188 (n=2070)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0059 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.2138` → IC=+0.169 (n=4704)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.2138 (IC base=+0.155)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3544` → IC=+0.164 (n=4355)

  - _Acción_: Kelly boost +0.82€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3544 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.166 (n=4339)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 6.0 (IC base=+0.155)

- **PATRÓN** `ibs_15` > `0.5` → IC=+0.222 (n=4709)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.1318` → IC=+0.148 (n=2234)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1318 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` < `0.6789` → IC=+0.140 (n=4573)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.6789 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.591` → IC=+0.263 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.591 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `4833.632` → IC=+0.178 (n=1568)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 4833.632 (IC base=+0.155)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=1821)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.224 (n=736)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0055 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.0597` → IC=+0.254 (n=246)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0597 (IC base=+0.204)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2668` → IC=+0.221 (n=245)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2668 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.225 (n=766)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.204)

- **PATRÓN** `ibs_15` > `0.713` → IC=+0.279 (n=735)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.713 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.3749` → IC=+0.229 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3749 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` < `0.5123` → IC=+0.208 (n=829)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5123 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.778` → IC=+0.313 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.778 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=951)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `12092.0019` → IC=+0.220 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12092.0019 (IC base=+0.204)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.156 (n=898)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0069 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.1103` → IC=+0.149 (n=599)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.1103 (IC base=+0.136)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1428` → IC=+0.137 (n=599)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio_macro` |x|> 0.1428 (IC base=+0.136)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.129` → IC=+0.144 (n=363)

  - _Acción_: Kelly boost +0.72€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.129 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.142 (n=820)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 6.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.139 (n=944)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_15` > `0.5` → IC=+0.223 (n=898)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.1194` → IC=+0.149 (n=562)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1194 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.4333` → IC=+0.137 (n=953)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.4333 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.945` → IC=+0.289 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.945 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `5812.1498` → IC=+0.165 (n=407)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 5812.1498 (IC base=+0.136)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8636` → IC=+0.185 (n=411)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.93€ cuando `ibs_15` > 0.8636 (IC base=+0.066)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0249` → IC=+0.179 (n=1101)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0249 (IC base=+0.177)

- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.188 (n=1101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0128 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.0664` → IC=+0.215 (n=367)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0664 (IC base=+0.177)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3523` → IC=+0.203 (n=998)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3523 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.181 (n=1006)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.182 (n=988)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 14.0 (IC base=+0.177)

- **PATRÓN** `ibs_15` > `0.4651` → IC=+0.246 (n=1105)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4651 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.4973` → IC=+0.212 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4973 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.939` → IC=+0.225 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.939 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `2947.1524` → IC=+0.215 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2947.1524 (IC base=+0.177)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.165 (n=908)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.82€ cuando `ibs_15` < 0.1111 (IC base=+0.067)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.384 (n=239)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1505` → IC=+0.379 (n=477)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1505 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1386` → IC=+0.381 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1386 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.372 (n=757)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.7904` → IC=+0.395 (n=714)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7904 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.1523` → IC=+0.383 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1523 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.219` → IC=+0.398 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.219 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.368 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `10048.6909` → IC=+0.380 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10048.6909 (IC base=+0.364)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.369 (n=120)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1584` → IC=+0.371 (n=238)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1584 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1464` → IC=+0.388 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1464 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.381 (n=333)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.386 (n=357)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.3743` → IC=+0.389 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3743 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.244` → IC=+0.388 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.244 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `8157.6321` → IC=+0.383 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8157.6321 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `493.0` → IC=+0.402 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 493.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.369 (n=358)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.364)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.375 (n=238)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.364)

- **PATRÓN** `drift_60min` |x|≤ `0.1077` → IC=+0.363 (n=239)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1077 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0833` → IC=+0.375 (n=319)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0833 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.380 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.367 (n=359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.364)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.373 (n=163)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.762` → IC=+0.397 (n=357)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.762 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.375 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` < `0.6569` → IC=+0.369 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6569 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.534` → IC=+0.407 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.534 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.368 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `4051.4429` → IC=+0.384 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4051.4429 (IC base=+0.364)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0102` → IC=-0.224 (n=1711)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0102
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=3323)

- **FILTRO** `drift_15min` |x|> `0.9075` → IC=-0.139 (n=1258)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9075
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=3775)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.215 (n=2069)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=2965)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1404` → IC=+0.224 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1404 (IC base=-0.076)

- **PATRÓN** `ibs_15` > `0.6306` → IC=+0.280 (n=1163)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6306 (IC base=-0.076)

- **PATRÓN** `dist_vwap_pct` > `0.1109` → IC=+0.201 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1109 (IC base=-0.076)

- **PATRÓN** `dist_vwap_pct` < `0.5648` → IC=+0.202 (n=1227)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5648 (IC base=-0.076)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2357` → IC=+0.268 (n=1509)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2357 (IC base=-0.006)

- **PATRÓN** `ibs_15` < `0.3679` → IC=+0.284 (n=4525)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3679 (IC base=-0.006)

- **PATRÓN** `dist_vwap_pct` > `0.6502` → IC=+0.278 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6502 (IC base=-0.006)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0322` → IC=-0.222 (n=2364)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0322
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=792)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.214 (n=789)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=2367)

- **FILTRO** `sigma_ewma_delta_pct` > `22.485` → IC=-0.263 (n=453)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.485
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=2703)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.149 (n=403)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0034 (IC base=+0.076)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2667` → IC=+0.269 (n=132)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2667 (IC base=+0.076)

- **PATRÓN** `ibs_15` > `0.7609` → IC=+0.329 (n=396)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7609 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` > `0.1043` → IC=+0.280 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1043 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` < `0.4914` → IC=+0.286 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4914 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.8` → IC=+0.143 (n=208)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 22.8 (IC base=+0.076)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0674` → IC=+0.240 (n=71)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0674 (IC base=-0.186)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0839` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0839 (IC base=-0.186)

- **PATRÓN** `ibs_15` < `0.6255` → IC=+0.322 (n=71)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6255 (IC base=-0.186)

- **PATRÓN** `dist_vwap_pct` < `0.0453` → IC=+0.314 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0453 (IC base=-0.186)

- **PATRÓN** `ballena_activa_n` < `381.0` → IC=+0.306 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 381.0 (IC base=-0.186)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=761)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.157 (n=584)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0065 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.0733` → IC=+0.181 (n=258)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.0733 (IC base=+0.149)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3021` → IC=+0.202 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3021 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.163 (n=419)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 11.0 (IC base=+0.149)

- **PATRÓN** `ibs_15` > `0.5756` → IC=+0.242 (n=584)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5756 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.1135` → IC=+0.149 (n=363)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1135 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.6543` → IC=+0.150 (n=672)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.6543 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.1` → IC=+0.265 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.1 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=761)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `5063.7944` → IC=+0.155 (n=389)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 5063.7944 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.257 (n=1137)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.3573` → IC=+0.245 (n=1500)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3573 (IC base=+0.243)

- **PATRÓN** `drift_15min` |x|≤ `0.7736` → IC=+0.256 (n=1500)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7736 (IC base=+0.243)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2187` → IC=+0.263 (n=773)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2187 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.247 (n=1225)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.244 (n=643)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.243)

- **PATRÓN** `ibs_15` < `0.3774` → IC=+0.275 (n=1706)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3774 (IC base=+0.243)

- **PATRÓN** `dist_vwap_pct` > `0.6087` → IC=+0.272 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6087 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.354` → IC=+0.247 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.354 (IC base=+0.243)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1822` → IC=-0.253 (n=289)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1822
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=869)

- **FILTRO** `drift_60min` |x|> `0.1726` → IC=-0.254 (n=393)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1726
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=765)

- **FILTRO** `drift_15min` |x|> `0.9075` → IC=-0.283 (n=288)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9075
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=870)

- **FILTRO** `sigma_ewma_delta_pct` > `6.328` → IC=-0.205 (n=269)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.328
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=889)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.192)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.192)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.192)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 29.0 (IC base=-0.192)

- **PATRÓN** `ibs_15` < `0.3913` → IC=+0.298 (n=774)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3913 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` < `0.4547` → IC=+0.242 (n=830)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4547 (IC base=-0.031)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.1502` → IC=-0.230 (n=350)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1502
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=1051)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.242 (n=680)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=721)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.213)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.213)

- **PATRÓN** `delta_ratio_macro` |x|> `0.117` → IC=+0.273 (n=684)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.117 (IC base=-0.022)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1183` → IC=+0.290 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1183 (IC base=-0.022)

- **PATRÓN** `ibs_15` < `0.325` → IC=+0.290 (n=1025)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.325 (IC base=-0.022)

- **PATRÓN** `dist_vwap_pct` > `0.7525` → IC=+0.338 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7525 (IC base=-0.022)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.146 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0062 (IC base=+0.103)

- **PATRÓN** `drift_60min` |x|≤ `0.1919` → IC=+0.146 (n=46)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1919 (IC base=+0.103)

- **PATRÓN** `drift_15min` |x|≤ `0.375` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.375 (IC base=+0.103)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2558` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2558 (IC base=+0.103)

- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.370 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` > `0.4193` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.4193 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` < `0.0951` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0951 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `3511.4523` → IC=+0.125 (n=46)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 3511.4523 (IC base=+0.103)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.146 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0062 (IC base=+0.103)

- **PATRÓN** `drift_60min` |x|≤ `0.1919` → IC=+0.146 (n=46)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1919 (IC base=+0.103)

- **PATRÓN** `drift_15min` |x|≤ `0.375` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.375 (IC base=+0.103)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2558` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2558 (IC base=+0.103)

- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.370 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` > `0.4193` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.4193 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` < `0.0951` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0951 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `3511.4523` → IC=+0.125 (n=46)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 3511.4523 (IC base=+0.103)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.292 (n=1261)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.0733` → IC=+0.312 (n=556)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0733 (IC base=+0.286)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1522` → IC=+0.290 (n=840)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1522 (IC base=+0.286)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2237` → IC=+0.295 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2237 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.302 (n=1303)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.286)

- **PATRÓN** `ibs_15` > `0.8395` → IC=+0.315 (n=1261)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8395 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.2684` → IC=+0.315 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2684 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.379` → IC=+0.391 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.379 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `13496.6656` → IC=+0.306 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13496.6656 (IC base=+0.286)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.311 (n=225)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.279)

- **PATRÓN** `drift_60min` |x|≤ `0.0593` → IC=+0.319 (n=224)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0593 (IC base=+0.279)

- **PATRÓN** `drift_15min` |x|≤ `0.3849` → IC=+0.279 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3849 (IC base=+0.279)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3931` → IC=+0.285 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3931 (IC base=+0.279)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.301 (n=702)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.279)

- **PATRÓN** `ibs_15` > `0.8292` → IC=+0.304 (n=672)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8292 (IC base=+0.279)

- **PATRÓN** `dist_vwap_pct` > `0.2516` → IC=+0.312 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2516 (IC base=+0.279)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.15` → IC=+0.388 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.15 (IC base=+0.279)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.280 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `15946.6772` → IC=+0.319 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15946.6772 (IC base=+0.279)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.310 (n=589)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.0524` → IC=+0.319 (n=197)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0524 (IC base=+0.293)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0669` → IC=+0.295 (n=589)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0669 (IC base=+0.293)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1019` → IC=+0.337 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1019 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.307 (n=564)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.300 (n=538)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.293)

- **PATRÓN** `ibs_15` > `0.8503` → IC=+0.322 (n=589)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8503 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.1243` → IC=+0.311 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1243 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` < `0.6569` → IC=+0.294 (n=667)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6569 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.513` → IC=+0.388 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.513 (IC base=+0.293)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2656` → IC=-0.130 (n=90)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2656
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=273)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.126` → IC=-0.159 (n=89)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.126
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=274)

- **FILTRO** `ballena_activa_n` > `34.0` → IC=-0.129 (n=246)

  - _Acción_: SKIP cuando `ballena_activa_n` > 34.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=85)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1228` → IC=-0.211 (n=119)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1228
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=368)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.183 (n=121)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=366)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.14` → IC=-0.148 (n=52)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.14
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=156)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2065` → IC=-0.259 (n=27)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2065
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=28)

- **FILTRO** `ballena_activa_n` > `595.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 595.0
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=32)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.311` → IC=-0.143 (n=40)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.311
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=21)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.326 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=12)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.306` → IC=-0.385 (n=24)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.306
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `sigma_h` < `0.0094` → IC=-0.167 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=19)

- **FILTRO** `ballena_activa_n` > `42.0` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 42.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=32)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.250 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=39)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0863` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0863
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

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
- **PATRÓN** `ratio` < `0.9709` → IC=+0.388 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9709 (IC base=+0.177)

- **PATRÓN** `T_h` > `116.1269` → IC=+0.354 (n=2616)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 116.1269 (IC base=+0.336)

- **PATRÓN** `ratio` > `1.0203` → IC=+0.380 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0203 (IC base=+0.336)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.9933` → IC=+0.261 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9933 (IC base=+0.138)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.314 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.300)

- **PATRÓN** `ratio` > `1.0429` → IC=+0.422 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0429 (IC base=+0.300)

### WEEKLY_PRICE#ETH
- **PATRÓN** `ratio` < `0.9849` → IC=+0.420 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9849 (IC base=+0.223)

- **PATRÓN** `T_h` > `111.996` → IC=+0.353 (n=950)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.996 (IC base=+0.321)

- **PATRÓN** `ratio` > `1.0298` → IC=+0.401 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0298 (IC base=+0.321)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0625` → IC=+0.429 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0625 (IC base=+0.398)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5 sube el IC de +0.155 a +0.222 en UPDOWN_GBM#15min (n=4709). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.713 sube el IC de +0.204 a +0.279 en UPDOWN_GBM#BTC#15min (n=735). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5 sube el IC de +0.136 a +0.223 en UPDOWN_GBM#ETH#15min (n=898). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.8636 sube el IC de +0.066 a +0.185 en UPDOWN_GBM#SOL#15min (n=411). Ya aplicado como kelly_boost=+0.93€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.4651 sube el IC de +0.177 a +0.246 en UPDOWN_GBM#XRP#15min (n=1105). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.067 a +0.165 en UPDOWN_GBM#XRP#15min (n=908). Ya aplicado como kelly_boost=+0.82€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6306 sube el IC de -0.076 a +0.280 en UPDOWN_GBM_15M_TARDIO (n=1163). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3679 sube el IC de -0.006 a +0.284 en UPDOWN_GBM_15M_TARDIO (n=4525). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7609 sube el IC de +0.076 a +0.329 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=396). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.186 a +0.322 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=71). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5756 sube el IC de +0.149 a +0.242 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=584). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3774 sube el IC de +0.243 a +0.275 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1706). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.192 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3913 sube el IC de -0.031 a +0.298 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=774). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.213 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.325 sube el IC de -0.022 a +0.290 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=1025). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.103 a +0.370 en UPDOWN_GBM_ETH_15M_HORA7 (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.103 a +0.370 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8395 sube el IC de +0.286 a +0.315 en UPDOWN_GBM_IBS_ALTO (n=1261). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8292 sube el IC de +0.279 a +0.304 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=672). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8503 sube el IC de +0.293 a +0.322 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=589). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7904 sube el IC de +0.364 a +0.395 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=714). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.362 a +0.386 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=357). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.762 sube el IC de +0.364 a +0.397 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=357). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2114 | +0.086 | +233.31€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2114 | +0.086 | +233.31€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1709 | +0.086 | +194.02€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1709 | +0.086 | +194.02€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 284 | +0.070 | +11.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 284 | +0.070 | +11.30€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 90 | +0.130 | +28.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 90 | +0.130 | +28.32€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 976 | -0.022 | +72.66€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 976 | -0.022 | +72.66€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 745 | -0.043 | +49.89€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 745 | -0.043 | +49.89€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 153 | +0.081 | +25.47€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 153 | +0.081 | +25.47€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 72 | -0.027 | -4.40€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 72 | -0.027 | -4.40€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 45246 | -0.085 | -5611.45€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2675 | +0.056 | -284.03€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 42571 | -0.094 | -5327.42€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4701 | -0.112 | -761.79€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4701 | -0.112 | -761.79€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2675 | +0.056 | -284.03€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2675 | +0.056 | -284.03€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4676 | -0.118 | -916.48€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4676 | -0.118 | -916.48€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 12352 | -0.038 | -1116.54€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 12352 | -0.038 | -1116.54€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 12225 | -0.115 | -1195.95€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 12225 | -0.115 | -1195.95€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8617 | -0.124 | -1336.66€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8617 | -0.124 | -1336.66€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 44823 | -0.013 | +3071.05€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 11575 | +0.005 | +1590.86€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 33248 | -0.019 | +1480.19€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 44823 | -0.013 | +3071.05€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 11575 | +0.005 | +1590.86€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 33248 | -0.019 | +1480.19€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 174984 | +0.113 | -7133.71€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 20943 | +0.181 | -648.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 795 | +0.001 | -75.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 143113 | +0.106 | -6028.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 10133 | +0.092 | -380.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 23715 | +0.105 | -1557.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 71 | -0.158 | +15.94€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 23629 | +0.106 | -1561.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 33403 | +0.124 | -564.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5560 | +0.180 | -222.48€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 23697 | +0.120 | -174.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4104 | +0.078 | -145.13€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 23765 | +0.099 | -1693.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 83 | -0.112 | +7.08€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 23667 | +0.100 | -1689.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 37337 | +0.124 | -729.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 9490 | +0.178 | -206.85€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 24065 | +0.106 | -454.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3770 | +0.101 | -58.97€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 33023 | +0.112 | -1534.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5657 | +0.199 | -253.73€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 698 | +0.029 | -21.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 24409 | +0.095 | -1082.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2259 | +0.102 | -176.51€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO#XRP | 23741 | +0.107 | -1054.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 82 | -0.107 | +11.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 23646 | +0.107 | -1065.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 28311 | +0.194 | -1861.75€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 28311 | +0.194 | -1861.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 6396 | +0.175 | -595.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 6396 | +0.175 | -595.95€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 3953 | +0.198 | -134.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 3953 | +0.198 | -134.83€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 6308 | +0.176 | -540.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 6308 | +0.176 | -540.73€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5358 | +0.250 | -189.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5358 | +0.250 | -189.22€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 6217 | +0.186 | -414.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 6217 | +0.186 | -414.78€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1183 | +0.426 | -43.25€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1183 | +0.426 | -43.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 483 | +0.440 | -3.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 483 | +0.440 | -3.30€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 476 | +0.425 | -17.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 476 | +0.425 | -17.35€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 210 | +0.396 | -18.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 210 | +0.396 | -18.74€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 99689 | +0.200 | -7229.10€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 99689 | +0.200 | -7229.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 17177 | +0.181 | -1880.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 17177 | +0.181 | -1880.97€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 16077 | +0.226 | -510.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 16077 | +0.226 | -510.04€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 17108 | +0.181 | -1803.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 17108 | +0.181 | -1803.26€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 16213 | +0.218 | -651.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 16213 | +0.218 | -651.97€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 16490 | +0.203 | -1059.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 16490 | +0.203 | -1059.75€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 16624 | +0.197 | -1323.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 16624 | +0.197 | -1323.11€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 38309 | +0.116 | +278.27€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 38309 | +0.116 | +278.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 19073 | +0.117 | +187.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 19073 | +0.117 | +187.22€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 19236 | +0.115 | +91.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 19236 | +0.115 | +91.05€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2429 | +0.293 | -6.75€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2429 | +0.293 | -6.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1111 | +0.281 | -27.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1111 | +0.281 | -27.28€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1183 | +0.298 | +16.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1183 | +0.298 | +16.68€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 135 | +0.339 | +3.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 135 | +0.339 | +3.85€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1115 | +0.441 | +2.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1115 | +0.441 | +2.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 535 | +0.435 | -6.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 535 | +0.435 | -6.78€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 530 | +0.447 | +8.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 530 | +0.447 | +8.05€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 50 | +0.404 | +1.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 50 | +0.404 | +1.12€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1872 | +0.068 | -82.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1147 | +0.081 | -18.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1438 | +0.076 | -37.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1147 | +0.081 | -18.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 77186 | +0.100 | -1865.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 6216 | +0.095 | +118.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 70970 | +0.101 | -1983.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 42253 | +0.105 | -426.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 6216 | +0.095 | +118.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 36037 | +0.107 | -544.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 16260 | +0.109 | -84.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 16260 | +0.109 | -84.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 18673 | +0.082 | -1354.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 18673 | +0.082 | -1354.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 2 | 4 |
| ✅ GBM_LATE_15M | 52528 | +0.097 | +28892.44€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 52528 | +0.097 | +28892.44€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 8724 | +0.224 | +7459.92€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 8724 | +0.224 | +7459.92€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 7994 | +0.174 | +6215.60€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 7994 | +0.174 | +6215.60€ | 0 | 23 |
| ✅ GBM_LATE_15M#DOGE | 9414 | +0.206 | +7380.25€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 9414 | +0.206 | +7380.25€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 7161 | +0.050 | +2192.48€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 7161 | +0.050 | +2192.48€ | 1 | 18 |
| ✅ GBM_LATE_15M#SOL | 7344 | -0.031 | +1904.34€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 7344 | -0.031 | +1904.34€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 11891 | -0.025 | +3739.85€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 11891 | -0.025 | +3739.85€ | 3 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 55413 | +0.085 | +31884.97€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 55413 | +0.085 | +31884.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 10787 | -0.001 | +5773.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 10787 | -0.001 | +5773.30€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 11852 | +0.004 | +3089.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 11852 | +0.004 | +3089.20€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 7572 | +0.291 | +8537.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 7572 | +0.291 | +8537.53€ | 0 | 23 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 10423 | +0.014 | +3153.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 10423 | +0.014 | +3153.98€ | 1 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 8597 | +0.043 | +3803.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 8597 | +0.043 | +3803.48€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 6182 | +0.314 | +7527.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 6182 | +0.314 | +7527.48€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 41619 | +0.179 | +34343.39€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 41619 | +0.179 | +34343.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 6267 | +0.239 | +5822.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 6267 | +0.239 | +5822.93€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 6615 | +0.140 | +4864.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 6615 | +0.140 | +4864.20€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 6683 | +0.225 | +5797.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 6683 | +0.225 | +5797.33€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 7104 | +0.133 | +5563.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 7104 | +0.133 | +5563.43€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 7853 | +0.121 | +5898.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 7853 | +0.121 | +5898.09€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 7097 | +0.232 | +6397.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 7097 | +0.232 | +6397.41€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 11151 | +0.126 | +5545.43€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 11151 | +0.126 | +5545.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 463 | +0.158 | +306.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 463 | +0.158 | +306.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3239 | +0.133 | +1788.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3239 | +0.133 | +1788.25€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 491 | +0.153 | +259.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 491 | +0.153 | +259.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3298 | +0.127 | +1615.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3298 | +0.127 | +1615.55€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2747 | +0.091 | +1032.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2747 | +0.091 | +1032.11€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 913 | +0.163 | +542.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 913 | +0.163 | +542.66€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 52749 | +0.186 | +43098.74€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 52749 | +0.186 | +43098.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 8337 | +0.248 | +8020.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 8337 | +0.248 | +8020.29€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 8347 | +0.136 | +5706.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 8347 | +0.136 | +5706.70€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 8943 | +0.233 | +8022.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 8943 | +0.233 | +8022.10€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 8743 | +0.140 | +6413.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 8743 | +0.140 | +6413.20€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 9356 | +0.123 | +6633.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 9356 | +0.123 | +6633.52€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 9023 | +0.239 | +8302.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 9023 | +0.239 | +8302.93€ | 0 | 20 |
| ✅ GBM_LATE_5M | 13625 | +0.210 | +11028.15€ | 1 | 27 |
| ✅ GBM_LATE_5M#5min | 13625 | +0.210 | +11028.15€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3256 | +0.211 | +2806.84€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3256 | +0.211 | +2806.84€ | 0 | 25 |
| ✅ GBM_LATE_5M#DOGE | 1254 | +0.198 | +940.72€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1254 | +0.198 | +940.72€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 3945 | +0.203 | +2966.88€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3945 | +0.203 | +2966.88€ | 0 | 25 |
| ✅ GBM_LATE_5M#SOL | 2158 | +0.207 | +1778.23€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2158 | +0.207 | +1778.23€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1958 | +0.209 | +1535.21€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1958 | +0.209 | +1535.21€ | 0 | 0 |
| ✅ GBM_LATE_60M | 4590 | +0.050 | +1216.43€ | 0 | 6 |
| ✅ GBM_LATE_60M#60min | 4590 | +0.050 | +1216.43€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1622 | +0.062 | +500.70€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1622 | +0.062 | +500.70€ | 1 | 5 |
| ✅ GBM_LATE_60M#ETH | 1485 | +0.051 | +433.48€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1485 | +0.051 | +433.48€ | 2 | 5 |
| ✅ GBM_LATE_60M#SOL | 1483 | +0.037 | +282.26€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1483 | +0.037 | +282.26€ | 0 | 10 |
| 🚫 GBM_LATE_60M_FADE | 667 | -0.250 | -35.29€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 667 | -0.250 | -35.29€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 251 | -0.251 | -20.27€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 251 | -0.251 | -20.27€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 239 | -0.247 | -7.78€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 239 | -0.247 | -7.78€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 177 | -0.249 | -7.24€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 177 | -0.249 | -7.24€ | 6 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1860 | +0.081 | +471.27€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1860 | +0.081 | +471.27€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 725 | +0.070 | +169.08€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 725 | +0.070 | +169.08€ | 1 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 637 | +0.057 | +113.06€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 637 | +0.057 | +113.06€ | 2 | 12 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 498 | +0.128 | +189.13€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 498 | +0.128 | +189.13€ | 2 | 9 |
| ✅ LATE_WINDOW_5MIN | 206 | +0.279 | +219.29€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 206 | +0.279 | +219.29€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 206 | +0.279 | +219.29€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 206 | +0.279 | +219.29€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4168 | +0.097 | +953.78€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4168 | +0.097 | +953.78€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4168 | +0.097 | +953.78€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4168 | +0.097 | +953.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 880 | -0.013 | +13.99€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 880 | -0.013 | +13.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 31 | -0.015 | -0.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 31 | -0.015 | -0.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 253 | -0.018 | +3.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 253 | -0.018 | +3.68€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 29 | -0.145 | -4.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 29 | -0.145 | -4.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 242 | +0.029 | +20.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 242 | +0.029 | +20.46€ | 2 | 1 |
| ✅ LIQUIDACIONES_15M#SOL | 271 | +0.002 | +5.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 271 | +0.002 | +5.11€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 54 | -0.161 | -9.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 54 | -0.161 | -9.89€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4106 | +0.016 | +98.20€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 4106 | +0.016 | +98.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 196 | +0.030 | -0.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 196 | +0.030 | -0.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 822 | +0.015 | +39.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 822 | +0.015 | +39.25€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 217 | -0.002 | -0.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 217 | -0.002 | -0.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1637 | +0.019 | +27.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1637 | +0.019 | +27.76€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 764 | +0.012 | +2.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 764 | +0.012 | +2.20€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 470 | +0.015 | +29.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 470 | +0.015 | +29.46€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2177 | -0.035 | -16.47€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2177 | -0.035 | -16.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 657 | -0.024 | -6.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 657 | -0.024 | -6.89€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 767 | -0.014 | +11.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 767 | -0.014 | +11.77€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 753 | -0.066 | -21.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 753 | -0.066 | -21.35€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 13205 | -0.033 | -139.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 6329 | -0.036 | -105.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 6876 | -0.030 | -34.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 470 | -0.044 | -19.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 238 | -0.008 | +9.86€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 232 | -0.081 | -28.89€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 3446 | -0.025 | -4.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1639 | -0.024 | +5.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1807 | -0.027 | -9.32€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1330 | -0.023 | +28.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 676 | -0.031 | +2.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 654 | -0.015 | +26.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 2970 | -0.037 | -75.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1403 | -0.044 | -59.61€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1567 | -0.032 | -15.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 2538 | -0.031 | -11.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1225 | -0.037 | -21.63€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1313 | -0.025 | +9.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 2451 | -0.042 | -58.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1148 | -0.050 | -41.58€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1303 | -0.036 | -16.81€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 14662 | -0.012 | -218.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14662 | -0.012 | -218.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 3379 | -0.021 | -71.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 3379 | -0.021 | -71.38€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 62018 | +0.000 | +3405.32€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 62018 | +0.000 | +3405.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 11221 | +0.028 | +1536.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 11221 | +0.028 | +1536.90€ | 2 | 4 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 8747 | -0.035 | -93.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 8747 | -0.035 | -93.44€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 11344 | +0.025 | +1234.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 11344 | +0.025 | +1234.00€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 8651 | -0.049 | -167.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 8651 | -0.049 | -167.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 10536 | -0.004 | +300.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 10536 | -0.004 | +300.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 11519 | +0.018 | +594.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 11519 | +0.018 | +594.38€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7029 | -0.055 | -118.49€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7029 | -0.055 | -118.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1242 | -0.002 | -15.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1242 | -0.002 | -15.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1927 | -0.067 | -31.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1927 | -0.067 | -31.00€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 70 | +0.000 | +1.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 70 | +0.000 | +1.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 797 | -0.119 | -34.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 797 | -0.119 | -34.54€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2135 | -0.068 | -12.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2135 | -0.068 | -12.36€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 858 | -0.016 | -26.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 858 | -0.016 | -26.02€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3375 | +0.003 | -2.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3375 | +0.003 | -2.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 132 | -0.037 | -1.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 132 | -0.037 | -1.23€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 195 | +0.008 | -2.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 195 | +0.008 | -2.19€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1326 | +0.006 | +6.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1326 | +0.006 | +6.37€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1391 | +0.007 | -0.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1391 | +0.007 | -0.19€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 192 | -0.010 | -2.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 192 | -0.010 | -2.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 152649 | -0.077 | +2178.70€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 152649 | -0.077 | +2178.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 26689 | -0.078 | +1496.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 26689 | -0.078 | +1496.22€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 22874 | -0.100 | -1053.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 22874 | -0.100 | -1053.94€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 27022 | -0.069 | +1279.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 27022 | -0.069 | +1279.98€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 22415 | -0.097 | -637.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 22415 | -0.097 | -637.02€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 27325 | -0.058 | +321.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 27325 | -0.058 | +321.82€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 26324 | -0.070 | +771.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 26324 | -0.070 | +771.63€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8979 | -0.035 | -186.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8979 | -0.035 | -186.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1002 | -0.017 | -19.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1002 | -0.017 | -19.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2068 | -0.047 | -29.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2068 | -0.047 | -29.51€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2630 | -0.026 | -39.67€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2630 | -0.026 | -39.67€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1265 | -0.064 | -32.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1265 | -0.064 | -32.47€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1005 | -0.031 | -33.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1005 | -0.031 | -33.06€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 2013 | +0.121 | +807.63€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 1877 | +0.125 | +795.03€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 450 | +0.135 | +221.03€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 450 | +0.135 | +221.03€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 386 | +0.119 | +136.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 386 | +0.119 | +136.08€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 356 | +0.131 | +168.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 356 | +0.131 | +168.15€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 322 | +0.142 | +165.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 322 | +0.142 | +165.86€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 363 | +0.097 | +103.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 363 | +0.097 | +103.91€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1934 | -0.015 | -15.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1934 | -0.015 | -15.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 366 | +0.014 | +22.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 366 | +0.014 | +22.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 349 | -0.033 | -13.32€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 349 | -0.033 | -13.32€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 490 | -0.045 | -35.90€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 490 | -0.045 | -35.90€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 391 | -0.001 | +0.46€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 391 | -0.001 | +0.46€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 338 | -0.003 | +11.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 338 | -0.003 | +11.18€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1073 | -0.079 | -51.14€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 494 | -0.111 | -77.53€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 382 | -0.128 | -59.07€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 112 | -0.053 | -18.46€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 377 | -0.038 | +20.55€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 266 | -0.022 | +29.99€ | 1 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 111 | -0.075 | -9.44€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 202 | -0.073 | +5.84€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 166 | -0.071 | +4.01€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 36 | -0.079 | +1.84€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 814 | -0.082 | -25.07€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 259 | -0.067 | -26.07€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1339 | -0.209 | -88.77€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 524 | -0.209 | -50.18€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 457 | -0.208 | -45.87€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 67 | -0.210 | -4.31€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 448 | -0.213 | -40.12€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 390 | -0.225 | -47.02€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 58 | -0.133 | +6.91€ | 1 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 367 | -0.202 | +1.52€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 340 | -0.199 | -0.88€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 27 | -0.224 | +2.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1187 | -0.211 | -93.77€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 152 | -0.188 | +5.00€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 516 | +0.386 | +476.17€ | 0 | 13 |
| ✅ RESOLUTION_SNIPER#BTC | 94 | +0.167 | +63.15€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 94 | +0.167 | +63.15€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#ETH | 122 | +0.371 | +105.56€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 122 | +0.371 | +105.56€ | 0 | 7 |
| ✅ RESOLUTION_SNIPER#SOL | 300 | +0.457 | +307.46€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 300 | +0.457 | +307.46€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 516 | +0.386 | +476.17€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 862 | +0.044 | +78.66€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 862 | +0.044 | +78.66€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 322 | +0.031 | +8.08€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 322 | +0.031 | +8.08€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 69 | +0.007 | +1.00€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 69 | +0.007 | +1.00€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 83 | +0.018 | +6.06€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 83 | +0.018 | +6.06€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 388 | +0.067 | +63.52€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 388 | +0.067 | +63.52€ | 1 | 5 |
| ✅ STREAK_FADE_5M | 3542 | -0.023 | -142.37€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3542 | -0.023 | -142.37€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 604 | -0.030 | -27.91€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 604 | -0.030 | -27.91€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 169 | -0.038 | -13.78€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 169 | -0.038 | -13.78€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1642 | -0.019 | -60.48€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1642 | -0.019 | -60.48€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 116 | -0.042 | -10.16€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 116 | -0.042 | -10.16€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 44 | -0.087 | -4.62€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 44 | -0.087 | -4.62€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 72 | -0.013 | -5.54€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 72 | -0.013 | -5.54€ | 0 | 2 |
| ✅ STREAK_MOM_5M | 11443 | +0.015 | +75.25€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11443 | +0.015 | +75.25€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2984 | +0.017 | +22.85€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2984 | +0.017 | +22.85€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2970 | +0.018 | +37.04€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2970 | +0.018 | +37.04€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2910 | +0.009 | -1.79€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2910 | +0.009 | -1.79€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2579 | +0.013 | +17.14€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2579 | +0.013 | +17.14€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 11048 | +0.015 | -38.50€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 11048 | +0.015 | -38.50€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4608 | +0.020 | +0.71€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4608 | +0.020 | +0.71€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3763 | +0.011 | -26.99€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3763 | +0.011 | -26.99€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2677 | +0.011 | -12.22€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2677 | +0.011 | -12.22€ | 1 | 0 |
| ✅ UPDOWN_GBM | 96212 | +0.059 | +9142.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 23472 | +0.083 | +5024.63€ | 0 | 9 |
| ✅ UPDOWN_GBM#240min | 2950 | +0.001 | +31.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 63756 | +0.059 | +3991.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 5702 | +0.001 | +98.09€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 8003 | +0.103 | +1461.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1780 | +0.164 | +821.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 6133 | +0.087 | +641.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 21995 | +0.057 | +1930.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3166 | +0.082 | +729.95€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 826 | +0.002 | +15.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 15327 | +0.065 | +1114.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2556 | -0.002 | +66.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 120 | -0.066 | +4.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 10340 | +0.078 | +1206.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1761 | +0.154 | +738.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 8493 | +0.062 | +469.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 22831 | +0.049 | +1576.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 5587 | +0.072 | +848.55€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 796 | +0.005 | +16.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 14248 | +0.050 | +684.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2089 | +0.004 | +24.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 111 | -0.102 | +2.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 20624 | +0.038 | +1144.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 6111 | +0.034 | +435.99€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 755 | -0.010 | +3.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 12602 | +0.047 | +704.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1057 | +0.003 | +7.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 99 | -0.144 | -7.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 12417 | +0.072 | +1825.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 5067 | +0.099 | +1450.22€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 6953 | +0.056 | +376.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 330 | -0.102 | -1.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 952 | +0.364 | +344.34€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 952 | +0.364 | +344.34€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 476 | +0.362 | +165.49€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 476 | +0.362 | +165.49€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 476 | +0.364 | +178.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 476 | +0.364 | +178.85€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 23485 | -0.021 | +5835.40€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 23485 | -0.021 | +5835.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 4373 | -0.113 | +225.28€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 4373 | -0.113 | +225.28€ | 3 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3050 | +0.219 | +1952.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3050 | +0.219 | +1952.74€ | 1 | 19 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 6624 | -0.059 | +981.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 6624 | -0.059 | +981.27€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 6386 | -0.064 | +1215.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 6386 | -0.064 | +1215.05€ | 2 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 281 | +0.062 | +26.33€ | 0 | 8 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 281 | +0.062 | +26.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 281 | +0.062 | +26.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 281 | +0.062 | +26.33€ | 0 | 8 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1680 | +0.286 | +1413.95€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1680 | +0.286 | +1413.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 895 | +0.279 | +704.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 895 | +0.279 | +704.44€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 785 | +0.293 | +709.51€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 785 | +0.293 | +709.51€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 850 | -0.114 | -84.77€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#5min | 850 | -0.114 | -84.77€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 263 | -0.085 | -20.76€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 263 | -0.085 | -20.76€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 94 | -0.167 | -10.43€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 94 | -0.167 | -10.43€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 110 | -0.179 | -4.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 110 | -0.179 | -4.23€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 4327 | +0.302 | +1996.04€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 1633 | +0.258 | +210.83€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 1665 | +0.295 | +721.13€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1029 | +0.381 | +1064.08€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.024 n=1182 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1182 IC=+0.024 PNL=+60.55€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 785 celda(s) pasan gate riguroso completo de 2831 evaluadas (n>=40) y 3942 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.034 < 0.08 — monitorear
  - _Datos_: n=6108 IC=+0.034 PNL=+435.47€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1665/15 IC=+0.295 PNL=+721.13€ | BTC: n=1633/15 IC=+0.258 PNL=+210.83€ | SOL: n=1029/15 IC=+0.381 PNL=+1064.08€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 31 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
  - _Bloqueante_: N_INSUFICIENTE


### ⏳ Acumulando datos

**⏳ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: 40
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Solo 0 ops con ibs_15 (feature añadida 2026-06-27). Esperar n≥40.

**⏳ H-HORA-GBM** — hora_utc causal automático en GBM (forward)
  - _Umbral_: 20
  - _Acción_: El sistema lo aplica automáticamente vía FEATURE_RULES. Verificar en strategy_params.json.
  - _Estado_: Solo 0 ops GBM con hora_utc en features. Esperar n≥20 para patrones.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.145 n=1009/60 | contraria IC=+0.187 n=1059 | gap=-0.042 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=552, boost estimado=+0.013. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=2087/40 IC=+0.004 PNL=+24.21€ | BTC#60min: n=2554/40 IC=-0.002 PNL=+66.59€ | SOL#60min: n=1057/40 IC=+0.003 PNL=+7.35€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.046 n=676175 | tras_1loss IC=+0.099 n=513030 | tras_2loss IC=+0.068 n=205933/40 | gap=-0.022 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.000 n=0 | contrario_BTC IC=+0.000 n=0/40 | gap=+0.000 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.175 > 0.08 con n=939 PNL=+619.74€
  - _Datos_: n=939 IC=+0.175 PNL=+619.74€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.150 > 0.08 con n=1110 PNL=+575.68€
  - _Datos_: n=1110 IC=+0.150 PNL=+575.68€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.167 > 0.08 con n=76 PNL=+40.16€
  - _Datos_: n=76 IC=+0.167 PNL=+40.16€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.333 > 0.1 con n=3532 PNL=+1970.96€
  - _Datos_: n=3532 IC=+0.333 PNL=+1970.96€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=945 IC=+0.068 PNL=+94.87€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=945 IC=+0.068 PNL=+94.87€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=100 IC=+0.186 PNL=+68.50€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=100 IC=+0.186 PNL=+68.50€

**⏳ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: 30
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 6/15 ops en el filtro definido (IC actual=+0.075 PNL=+7.10€)
  - _Datos_: n=6 IC=+0.075 PNL=+7.10€

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
  - _Estado_: n=3825 IC=+0.003 PNL=-11.03€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3825 IC=+0.003 PNL=-11.03€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1873 IC=-0.002 PNL=+109.18€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1873 IC=-0.002 PNL=+109.18€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1182 IC=+0.024 PNL=+60.55€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1182 IC=+0.024 PNL=+60.55€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.155 > 0.1 con n=6270 PNL=+3446.92€
  - _Datos_: n=6270 IC=+0.155 PNL=+3446.92€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=3164 IC=+0.082 PNL=+729.93€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=3164 IC=+0.082 PNL=+729.93€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 0/50 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: confirmada 2026-07-01 (IC=-0.037 n=52) e implementada en shadow_predict.py (skip si drift_15min∈[-0.3,0.3)) -- verificado 26-Ago con 2177 filas post-TWAP reales, 0 caen en la zona filtrada. Frozen by design, no falta n

**⏳ H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: 40
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: 20
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: 0/20 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=1220 IC=+0.038 PNL=+104.45€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1220 IC=+0.038 PNL=+104.45€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=158 IC=-0.006 PNL=-1.60€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=158 IC=-0.006 PNL=-1.60€

**⏳ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: 40
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: 30
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.278 n=205) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=205 IC=+0.278 PNL=+217.37€

**⏳ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: 40
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: 40
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: 40
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: 40
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: 40
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: 200
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: 0/200 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-MERCURY-RETROGRADO** — Mercurio retrógrado: ¿rendimiento peor durante la ventana?
  - _Hipótesis_: Mismo origen que H-CUSTOM-MOON-LLENA (paper de Fornero, 43 Jornadas SADAF 2023). Qi, Wang & Zhang (2022, 48 mercados, 1973-2019): rendimientos 3.33%/año más bajos durante Mercurio retrógrado. Kou & Ma (2022) en China (99.8% cuentas retail): hasta -31% anualizado. Ambos estudios confirman que el mecanismo es la creencia/superstición de inversores retail (mayor efecto cuanto más retail y más supersticioso el mercado), no un efecto astral literal — Polymarket encaja en ese perfil. Ventanas 2026 (fuente pública, actualizar cada año): 26-feb a 20-mar, 29-jun a 23-jul, 24-oct a 13-nov.
  - _Umbral_: 100
  - _Acción_: Si IC en mercury_retrogrado=1 < IC en mercury_retrogrado=0 con margen ≥0.05 y ≥2 ventanas distintas cubiertas → considerar boost/filtro. No implementar tras una sola ventana (jun-jul 2026) por more que n sea alto — sería solo un evento, no un patrón.
  - _Estado_: 0/100 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-SMART-MONEY-CONSENSUS** — Consenso de wallets 'smart money' — ¿confirma nuestra dirección?
  - _Hipótesis_: Javi propuso estudiar bots/wallets que operan bien en nuestros mismos mercados. En vez de creer artículos (ya verificamos 2 veces esta semana que las narrativas no aguantan el cruce con datos reales), smart_money_tracker.py mide el track record REAL de wallets activas en BTC/ETH/SOL/XRP Up-or-Down 5/15/60min vía data-api.polymarket.com/positions, filtrado a posiciones 'Up or Down'. Clasifica como 'smart' las wallets con n>=10 posiciones, win_rate>=0.55 y pnl_total>0. smart_money_consensus es el sesgo direccional reciente (Up-Down)/(Up+Down) de esas wallets 'smart' por activo. Hipótesis: si nuestra decisión (BUY_YES/BUY_NO) coincide con el consenso smart money, mejor IC que cuando diverge. RESET METODOLOGICO 2026-07-02: la clasificacion 'smart' original via /positions estaba INVERTIDA para wallets de alta frecuencia (el endpoint solo retiene el residuo perdedor sin redimir; verificado: 'wowitsamazing' figuraba como -$478k y es +$10k/mes en el leaderboard oficial). Desde 2026-07-02T06:12Z el consenso se construye solo con wallets verificadas en el leaderboard oficial (pnl_mes>=$1000, 24 wallets). Los valores de smart_money_consensus capturados en features ANTES de esa fecha provienen de la clasificacion rota — descontar ese tramo al evaluar.
  - _Umbral_: 40
  - _Acción_: Si IC en confluencia (decisión coincide con signo de smart_money_consensus) supera en >=0.05 al IC en divergencia, con n≥40 en cada lado → boost ×1.1-1.2 cuando coincide, considerar reducir stake cuando diverge fuerte.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.124 > 0.02 con n=1180 PNL=+497.89€
  - _Datos_: n=1180 IC=+0.124 PNL=+497.89€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=251 IC=-0.117 PNL=+7.41€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=251 IC=-0.117 PNL=+7.41€

**⏳ H-CUSTOM-WEEKLY-INRANGE-BUYYES** — WEEKLY_PRICE BUY_YES con in_range=1 — ¿estructuralmente sobrevalorado?
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_YES cuando in_range=1 fue 0/3 (todo pérdida). Mecanismo propuesto: acertar un rango de precio estrecho al vencimiento es intrínsecamente poco probable, el mercado puede estar sobrevalorando el 'sí'. Ver H-CUSTOM-WEEKLY-PCTDIST-BUYNO para el lado complementario (BUY_NO con pct_dist alto).
  - _Umbral_: 25
  - _Acción_: Si se confirma con n≥25 → filtro causal in_range==1 + BUY_YES → skip en WEEKLY_PRICE
  - _Estado_: 0/25 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-WEEKLY-PCTDIST-BUYNO** — WEEKLY_PRICE BUY_NO con pct_dist alto — cuanto más lejos del rango, más seguro
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_NO con pct_dist>=2.09% fue 4/4 victorias (rango 2.09%-23.4%); BUY_NO con pct_dist<8% (pero fuera del corte anterior) tuvo derrotas. Patrón: cuanto más lejos está el spot del rango objetivo al momento de la predicción, más fiable el BUY_NO. Complementa H-CUSTOM-WEEKLY-INRANGE-BUYYES.
  - _Umbral_: 25
  - _Acción_: Si se confirma con n≥25 → boost ×1.2 en WEEKLY_PRICE BUY_NO cuando pct_dist≥2
  - _Estado_: 0/25 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=39046 IC=+0.074 PNL=+5562.41€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=39046 IC=+0.074 PNL=+5562.41€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.134 < -0.1 con n=695 PNL=+102.52€
  - _Datos_: n=695 IC=-0.134 PNL=+102.52€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=3597 IC=+0.067 PNL=+467.04€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=3597 IC=+0.067 PNL=+467.04€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=173 IC=-0.117 PNL=-1.71€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=173 IC=-0.117 PNL=-1.71€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.104 > 0.1 con n=1005 PNL=+262.37€
  - _Datos_: n=1005 IC=+0.104 PNL=+262.37€

**⏳ H-CUSTOM-ETH15-BUYNO-PRECIO-ALTO** — ETH#15min BUY_NO con precio_yes>0.55 pierde (NO longshot contra favorito)
  - _Hipótesis_: Detectado 2026-07-02: ult.60 shadow ETH15 BUY_NO — py_mkt~0.5 wr=0.67 PNL=+29.3 (n=49); py_mkt 0.6-0.8 wr 0.33-0 PNL=-5.75 (n=9). Filtro RETURN NONE (no SKIP) aplicado en shadow_predict.py (PY_MKT_MAX_BUY_NO_ETH15=0.55) el mismo dia -- bloquea la GENERACIÓN de la fila, no solo la decisión. Esta hipotesis trackea la zona filtrada: si las ops que HABRIAN caido aqui siguen apareciendo en otras estrategias o el IC forward de la zona se vuelve positivo, revisar el filtro. CAVEAT: n=9, muestra chica — el filtro se aplico por asimetria de riesgo (afecta a dinero live), no por significancia. ⚠️ 05-Ago (fix): la clave del filtro decía 'py_mkt', que NUNCA existió ni en features de UPDOWN_GBM (T_h/delta_ratio_macro/drift_15min/drift_60min/pct_spot_vs_ref/sigma_h) ni como columna top-level de results.csv -- corregida a 'precio_yes_mercado' (columna real). Aun así, con la clave correcta esta hipótesis NUNCA podrá acumular n mientras el filtro RETURN NONE siga activo -- es el mismo patrón 'frozen by design' que H-CUSTOM-LATE15-PHOTO-FINISH (más abajo): la propia protección impide generar los datos necesarios para volver a evaluarla. Para monitorearla de verdad haría falta un logger separado que capture la señal SIN aplicar el filtro (mismo patrón que gate_bucket_propio con data/markets histórico) -- no construido, pendiente decisión.
  - _Umbral_: 20
  - _Acción_: Si IC forward de la zona >0 con n>=20 → retirar filtro; si confirma negativo → considerar extender a BTC/SOL 15min
  - _Estado_: 6/20 ops en el filtro definido (IC actual=-0.075 PNL=-1.82€)
  - _Datos_: n=6 IC=-0.075 PNL=-1.82€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: PY_MKT_MAX_BUY_NO_ETH15=0.55 en shadow_predict.py hace RETURN NONE (bloquea generación, no solo decisión) -- nunca podrá acumular n mientras siga activo. Haría falta un logger separado sin el filtro para monitorear de verdad (no construido, 26-Ago)

**〰️ H-PRECIO-YES-BARATO** — BUY_YES con precio de mercado 0.30-0.40 — mercado infravalora YES
  - _Hipótesis_: Detectado 2026-07-03 en benchmark de calibración del mercado (7d, estrategias GBM): en el bucket precio_yes_mercado [0.3-0.4) la frecuencia real de YES fue 0.45 vs 0.35 implícito (+0.10, n=38). Posible sesgo favorito-longshot suave en binarios de 15min (complemento del LONGSHOT ya activo para BUY_NO con py<0.20). Si se confirma, BUY_YES comprado en esa banda lleva viento de cola estructural del propio mercado, independiente del modelo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → kelly_boost ×1.1 para BUY_YES con precio_yes_mercado en [0.30,0.40), simétrico al longshot BUY_NO existente
  - _Estado_: n=40041 IC=-0.136 PNL=+2667.74€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=40041 IC=-0.136 PNL=+2667.74€

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
  - _Estado_: n=4108 IC=+0.128 PNL=+2652.84€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=4108 IC=+0.128 PNL=+2652.84€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=9888 IC=+0.059 PNL=+878.54€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=9888 IC=+0.059 PNL=+878.54€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.099 > 0.08 con n=4272 PNL=+2372.39€
  - _Datos_: n=4272 IC=+0.099 PNL=+2372.39€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.220 < -0.1 con n=4325 PNL=-354.54€
  - _Datos_: n=4325 IC=-0.220 PNL=-354.54€

**⏳ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: 100
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: 0/100 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: 40
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: 40
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: 40
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: n>=40 y IC>0.08
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: n=88 IC=+0.044 PNL=+15.50€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=88 IC=+0.044 PNL=+15.50€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.095 n=2116) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2116 IC=+0.095 PNL=+426.36€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.411 n=653) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=653 IC=+0.411 PNL=+943.88€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=17168 IC=+0.181 PNL=-1878.99€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=17168 IC=+0.181 PNL=-1878.99€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.229 > 0.1 con n=271 PNL=+187.30€
  - _Datos_: n=271 IC=+0.229 PNL=+187.30€
