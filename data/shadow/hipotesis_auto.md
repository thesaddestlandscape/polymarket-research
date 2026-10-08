# Hipótesis automáticas — 2026-10-08 20:24 UTC
_Generado por shadow_postmortem.py sobre 811846 resoluciones (PNL=+100987.46€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **PATRÓN** `py_entrada` > `0.505` → IC=+0.206 (n=686)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.118)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.198 (n=233)

  - _Acción_: Kelly boost +0.99€ cuando `n_total_lado` > 69.0 (IC base=+0.118)

- **PATRÓN** `banda_hit_calibrado` > `0.6165` → IC=+0.234 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6165 (IC base=+0.118)

- **PATRÓN** `banda_z` > `8.976` → IC=+0.191 (n=228)

  - _Acción_: Kelly boost +0.96€ cuando `banda_z` > 8.976 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.155 (n=233)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=726)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.118)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.227 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.122)

- **PATRÓN** `n_total_lado` > `75.0` → IC=+0.208 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 75.0 (IC base=+0.122)

- **PATRÓN** `banda_hit_calibrado` > `0.8116` → IC=+0.260 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8116 (IC base=+0.122)

- **PATRÓN** `banda_z` > `9.563` → IC=+0.179 (n=185)

  - _Acción_: Kelly boost +0.90€ cuando `banda_z` > 9.563 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=578)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.127 (n=628)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.122)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.355` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `py_entrada` < 0.355
  - _Potencial_: sin este filtro IC_bueno=+0.234 (n=107)

- **FILTRO** `banda_hit_calibrado` < `0.8019` → IC=-0.146 (n=46)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.8019
  - _Potencial_: sin este filtro IC_bueno=+0.255 (n=96)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.184 (n=115)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.371 (n=29)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=97)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.177 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=97)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=110)

- **PATRÓN** `py_entrada` > `0.705` → IC=+0.255 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.705 (IC base=+0.125)

- **PATRÓN** `banda_hit_calibrado` > `0.8019` → IC=+0.255 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8019 (IC base=+0.125)

- **PATRÓN** `banda_z` > `7.17` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `banda_z` > 7.17 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.128 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 4.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.136 (n=97)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 14.0 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.184 (n=115)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `1207.4096` → IC=+0.185 (n=71)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1207.4096 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.125 (n=94)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.495 (IC base=+0.000)

### BALLENAS_CONFIRMADAS_15M#XRP#15min
- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `n_ballena_banda` > 26.0 (IC base=+0.154)

- **PATRÓN** `n_total_lado` > `38.0` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 38.0 (IC base=+0.154)

- **PATRÓN** `banda_z` > `2.517` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 2.517 (IC base=+0.154)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.705` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `ballenas_wallet_edge_medio` > 0.705 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.224 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `2518.5859` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2518.5859 (IC base=+0.154)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `144.04` → IC=-0.208 (n=8839)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.04
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=26517)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `131.11` → IC=-0.268 (n=1099)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.11
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=3298)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `123.47` → IC=-0.305 (n=1022)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 123.47
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=3068)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `164.85` → IC=-0.228 (n=2256)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 164.85
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=6770)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `131.04` → IC=-0.301 (n=1727)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.04
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=5181)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.207 (n=18378)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.103)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=3969)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `9526.0822` → IC=+0.183 (n=1767)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 9526.0822 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.134 (n=15165)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.135 (n=18458)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.227 (n=14054)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.162 (n=6522)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7509.1715` → IC=+0.166 (n=2509)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 7509.1715 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=1916)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.197 (n=1870)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.348 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=2351)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `16092.2822` → IC=+0.210 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16092.2822 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.198 (n=1692)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 7.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.198 (n=1877)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.195 (n=2407)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `16044.722` → IC=+0.206 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16044.722 (IC base=+0.192)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.160 (n=410)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` > 0.61 (IC base=+0.087)

- **PATRÓN** `libro_liquidez` > `4988.4492` → IC=+0.126 (n=228)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 4988.4492 (IC base=+0.087)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.134 (n=457)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.091)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.138 (n=982)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.44 (IC base=+0.091)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=3583)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.364 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.230 (n=1596)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.361 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.226 (n=1848)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.221)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=891)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.139 (n=762)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.135)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.251 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.135 (n=981)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `1325.0731` → IC=+0.141 (n=851)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 1325.0731 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.076)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.241 (n=850)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.410 (n=1029)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.148 (n=1247)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=658)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.146)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.289 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=821)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.146)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.179 (n=331)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.376 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.156 (n=193)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.151 (n=379)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.225 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.122)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.284 (n=132)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=68)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=15209)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.199 (n=12896)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.229 (n=6408)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.178 (n=3369)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 6.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.175 (n=3374)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.178 (n=3435)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.174)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.232 (n=1562)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.228 (n=1551)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.317 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.227)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.190 (n=3318)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 6.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.185 (n=3343)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.190 (n=1941)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.72 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.253 (n=3067)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.241)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.331 (n=1065)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.241)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=3427)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.193 (n=2191)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.190 (n=2608)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.71 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.199 (n=1218)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.189)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.429 (n=615)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.426 (n=605)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.427 (n=710)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `2776.9049` → IC=+0.432 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2776.9049 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.430 (n=269)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.432)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.444 (n=178)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.432)

- **PATRÓN** `libro_liquidez` > `17805.5966` → IC=+0.434 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 17805.5966 (IC base=+0.432)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.440 (n=182)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.427)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.434 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.427)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.427 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.427)

- **PATRÓN** `libro_liquidez` > `3399.6895` → IC=+0.437 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3399.6895 (IC base=+0.427)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.408 (n=129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.405)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.408 (n=128)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.405)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.408 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.405)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.410 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.405)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.775` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=17)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=24)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=19522)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.244 (n=19852)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.186 (n=7819)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.186 (n=6252)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.199 (n=8655)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.184)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=4076)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.281 (n=2870)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.181 (n=7772)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 8.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.193 (n=8271)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.234 (n=4111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.273 (n=2816)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.205 (n=7545)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.203 (n=5996)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.260 (n=2944)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.202 (n=3250)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.245 (n=3439)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.194)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=6970)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.118)

- **PATRÓN** `restante_min` < `4.2` → IC=+0.125 (n=6480)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.2 (IC base=+0.118)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.137 (n=6798)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.127 (n=8548)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 7.0 (IC base=+0.118)

- **PATRÓN** `lag_apertura_s` < `2.45` → IC=+0.137 (n=6447)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.45 (IC base=+0.118)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=3464)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.121)

- **PATRÓN** `restante_min` < `4.17` → IC=+0.126 (n=3211)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.17 (IC base=+0.121)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.142 (n=3417)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.136 (n=4234)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.121)

- **PATRÓN** `lag_apertura_s` < `3.08` → IC=+0.145 (n=3204)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 3.08 (IC base=+0.121)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.189 (n=3506)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.131 (n=3719)

  - _Acción_: Kelly boost +0.65€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.134 (n=3258)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 2.25 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.314 (n=964)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.288)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.289 (n=1418)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.380 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `1554.6996` → IC=+0.292 (n=1351)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1554.6996 (IC base=+0.288)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.291 (n=644)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.340 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `5323.7564` → IC=+0.306 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5323.7564 (IC base=+0.279)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.321 (n=461)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.286)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.290 (n=680)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.286)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.386 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `1448.4724` → IC=+0.302 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1448.4724 (IC base=+0.286)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.357 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.350)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.375 (n=78)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.350)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.391 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.350)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.354 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.350)

- **PATRÓN** `libro_liquidez` > `745.0217` → IC=+0.378 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 745.0217 (IC base=+0.350)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.445 (n=614)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.441 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.445 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.440)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.441 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.440)

- **PATRÓN** `libro_liquidez` > `2592.684` → IC=+0.439 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2592.684 (IC base=+0.440)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.444 (n=266)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.440)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.440 (n=299)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.441 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.449 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.440)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.462 (n=102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.450 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.442 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.443 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.442)

- **PATRÓN** `libro_liquidez` > `2138.537` → IC=+0.458 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2138.537 (IC base=+0.442)

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
- **FILTRO** `hora_utc` < `5.0` → IC=-0.273 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=78)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.292 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=52)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.308 (n=222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.297 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.276 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `983.8593` → IC=+0.277 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 983.8593 (IC base=+0.259)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **FILTRO** `hora_utc` < `5.0` → IC=-0.273 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=78)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.292 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=52)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.308 (n=222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.297 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.276 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `983.8593` → IC=+0.277 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 983.8593 (IC base=+0.259)

### GBM_LATE_15M
- **PATRÓN** `drift_60min` |x|≤ `0.3727` → IC=+0.136 (n=9572)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.3727 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.9834` → IC=+0.243 (n=3626)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9834 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.2208` → IC=+0.255 (n=2509)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2208 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.439` → IC=+0.193 (n=2829)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 8.439 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `0.853` → IC=+0.250 (n=2038)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.853 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` > `0.616` → IC=+0.254 (n=3056)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.616 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.301` → IC=+0.231 (n=1101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.301 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `2.323` → IC=+0.218 (n=3460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.323 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.5628` → IC=+0.141 (n=13309)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5628 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` > `0.5841` → IC=+0.202 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5841 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.1514` → IC=+0.184 (n=4607)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.1514 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` < `1.1942` → IC=+0.183 (n=4939)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 1.1942 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` > `0.6248` → IC=+0.181 (n=4939)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.6248 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.2949` → IC=+0.230 (n=1244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2949 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` > `1.448` → IC=+0.203 (n=8468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.448 (IC base=+0.073)

- **PATRÓN** `ballena_activa_n` < `114.0` → IC=+0.218 (n=8287)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 114.0 (IC base=+0.073)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.219 (n=810)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.190 (n=805)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.008 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.3504` → IC=+0.188 (n=2412)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3504 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.196 (n=1170)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.184 (n=1613)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 11.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.279 (n=977)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.782` → IC=+0.295 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.782 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.238 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `1.4349` → IC=+0.183 (n=2285)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.4349 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.196 (n=2497)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `2081.02` → IC=+0.191 (n=804)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2081.02 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.233 (n=1311)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.233)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.242 (n=1756)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.0883` → IC=+0.266 (n=655)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0883 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.254 (n=722)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.0605` → IC=+0.281 (n=864)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0605 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.526` → IC=+0.248 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.526 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.403` → IC=+0.237 (n=2054)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.403 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` < `0.0703` → IC=+0.234 (n=1643)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0703 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.2864` → IC=+0.259 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2864 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.6242` → IC=+0.252 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6242 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=2158)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.233)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.234 (n=853)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.1091` → IC=+0.253 (n=852)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1091 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.233 (n=1943)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.3198` → IC=+0.234 (n=1935)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3198 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` > `0.1983` → IC=+0.220 (n=976)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1983 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.619` → IC=+0.260 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.619 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` < `1.2476` → IC=+0.220 (n=1935)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2476 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` > `0.6188` → IC=+0.223 (n=1935)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6188 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.2786` → IC=+0.243 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2786 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `1.7571` → IC=+0.219 (n=1269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7571 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.4014` → IC=+0.237 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4014 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.151 (n=1932)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0056 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0761` → IC=+0.167 (n=644)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0761 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.160 (n=737)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.7224` → IC=+0.178 (n=1931)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.7224 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1327` → IC=+0.156 (n=1781)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1327 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.254` → IC=+0.156 (n=309)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 11.254 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.301` → IC=+0.143 (n=1769)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.301 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.1913` → IC=+0.147 (n=1931)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.1913 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `0.6232` → IC=+0.138 (n=1931)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.6232 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.0963` → IC=+0.168 (n=699)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.0963 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.449` → IC=+0.148 (n=1816)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.449 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.7828` → IC=+0.145 (n=1212)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.7828 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `230.0` → IC=+0.174 (n=771)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 230.0 (IC base=+0.137)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.202 (n=2449)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.197 (n=2448)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=2192)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.266 (n=947)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.397` → IC=+0.257 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.397 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.194 (n=2153)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.3457` → IC=+0.196 (n=320)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.3457 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `2.1506` → IC=+0.202 (n=1571)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1506 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.197 (n=2920)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.226 (n=1452)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.1319` → IC=+0.230 (n=725)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1319 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=820)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.217 (n=1007)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` < `0.0649` → IC=+0.237 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0649 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.687` → IC=+0.255 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.687 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.3452` → IC=+0.259 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3452 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `1.7153` → IC=+0.219 (n=899)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7153 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.7161` → IC=+0.227 (n=926)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7161 (IC base=+0.214)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.217 (n=1996)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.214)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.144 (n=133)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=2921)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.147 (n=460)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0036 (IC base=+0.043)

- **PATRÓN** `ibs_20min` > `0.9581` → IC=+0.219 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9581 (IC base=+0.043)

- **PATRÓN** `dist_vwap_pct` < `0.188` → IC=+0.322 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.188 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.981` → IC=+0.177 (n=964)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 4.981 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` < `0.8536` → IC=+0.326 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8536 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` > `1.2251` → IC=+0.345 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2251 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.3033` → IC=+0.337 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3033 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.421` → IC=+0.353 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.421 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` > `2.2012` → IC=+0.321 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2012 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `154.0` → IC=+0.321 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 154.0 (IC base=+0.043)

- **PATRÓN** `ibs_20min` < `0.0956` → IC=+0.167 (n=764)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.0956 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` > `0.3085` → IC=+0.193 (n=333)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.3085 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` < `0.8497` → IC=+0.156 (n=820)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8497 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.2877` → IC=+0.215 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2877 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` > `1.5272` → IC=+0.167 (n=1050)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.5272 (IC base=+0.032)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.179 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=453)

- **FILTRO** `ibs_20min` < `0.3056` → IC=-0.189 (n=133)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3056
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=399)

- **FILTRO** `ibs_20min` > `0.225` → IC=-0.126 (n=2963)

  - _Acción_: SKIP cuando `ibs_20min` > 0.225
  - _Potencial_: sin este filtro IC_bueno=+0.141 (n=1461)

- **FILTRO** `sigma_ewma_delta_pct` > `8.773` → IC=-0.224 (n=454)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.773
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=3970)

- **PATRÓN** `ibs_20min` > `0.8` → IC=+0.201 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` > `0.9817` → IC=+0.294 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9817 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.37` → IC=+0.138 (n=183)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 2.37 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` < `0.57` → IC=+0.280 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.57 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` > `1.0233` → IC=+0.297 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0233 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` < `0.0778` → IC=+0.293 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0778 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` < `2.1712` → IC=+0.293 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1712 (IC base=+0.041)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.280 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.041)

- **PATRÓN** `ibs_20min` < `0.225` → IC=+0.141 (n=1461)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.225 (IC base=-0.037)

- **PATRÓN** `dist_vwap_pct` > `0.1849` → IC=+0.274 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1849 (IC base=-0.037)

- **PATRÓN** `volumen_regimen` < `0.695` → IC=+0.282 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.695 (IC base=-0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.0805` → IC=+0.297 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0805 (IC base=-0.037)

- **PATRÓN** `volumen_spike_ratio` < `2.371` → IC=+0.295 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.371 (IC base=-0.037)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.645` → IC=-0.186 (n=770)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.645
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=2312)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.210 (n=866)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2216)

- **FILTRO** `ibs_20min` > `0.7619` → IC=-0.207 (n=1148)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7619
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=3448)

- **PATRÓN** `dist_vwap_pct` > `0.7824` → IC=+0.323 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7824 (IC base=-0.073)

- **PATRÓN** `dist_vwap_pct` < `0.279` → IC=+0.315 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.279 (IC base=-0.073)

- **PATRÓN** `volumen_regimen` < `0.988` → IC=+0.298 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.988 (IC base=-0.073)

- **PATRÓN** `volumen_regimen` > `0.6476` → IC=+0.314 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6476 (IC base=-0.073)

- **PATRÓN** `volumen_pendiente_norm` < `0.1024` → IC=+0.304 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1024 (IC base=-0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.0744` → IC=+0.301 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0744 (IC base=-0.073)

- **PATRÓN** `volumen_spike_ratio` < `2.4802` → IC=+0.302 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4802 (IC base=-0.073)

- **PATRÓN** `volumen_spike_ratio` > `1.8609` → IC=+0.304 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8609 (IC base=-0.073)

- **PATRÓN** `dist_vwap_pct` > `0.8239` → IC=+0.285 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8239 (IC base=-0.011)

- **PATRÓN** `volumen_regimen` < `0.7144` → IC=+0.249 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7144 (IC base=-0.011)

- **PATRÓN** `volumen_regimen` > `1.0756` → IC=+0.277 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0756 (IC base=-0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.1026` → IC=+0.274 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1026 (IC base=-0.011)

- **PATRÓN** `volumen_spike_ratio` < `2.1684` → IC=+0.256 (n=948)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1684 (IC base=-0.011)

- **PATRÓN** `volumen_spike_ratio` > `1.4248` → IC=+0.258 (n=1077)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4248 (IC base=-0.011)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.200 (n=4779)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.4651` → IC=+0.186 (n=12809)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4651 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.6781` → IC=+0.285 (n=1429)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6781 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.69` → IC=+0.154 (n=6458)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 3.69 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` < `1.1739` → IC=+0.249 (n=5251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1739 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` > `0.6895` → IC=+0.256 (n=4690)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6895 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.2933` → IC=+0.261 (n=1194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2933 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `1.4634` → IC=+0.247 (n=2820)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4634 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` > `2.6296` → IC=+0.256 (n=2820)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6296 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.279 (n=8013)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.098)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.167 (n=4625)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0089 (IC base=+0.076)

- **PATRÓN** `ibs_20min` < `0.5403` → IC=+0.160 (n=12204)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.5403 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` < `0.8743` → IC=+0.251 (n=2819)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8743 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` > `1.1987` → IC=+0.262 (n=1409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1987 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.2954` → IC=+0.309 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2954 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` < `1.5868` → IC=+0.281 (n=2608)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5868 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` > `2.275` → IC=+0.271 (n=2687)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.275 (IC base=+0.076)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.285 (n=5825)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 77.0 (IC base=+0.076)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2567` → IC=-0.172 (n=1000)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2567
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=3003)

- **FILTRO** `ibs_20min` > `0.7542` → IC=-0.177 (n=825)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7542
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=2479)

- **FILTRO** `sigma_ewma_delta_pct` > `4.623` → IC=-0.179 (n=728)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.623
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=2576)

- **PATRÓN** `ibs_20min` > `0.9077` → IC=+0.276 (n=1001)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9077 (IC base=+0.038)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.335` → IC=+0.201 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.335 (IC base=+0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.2277` → IC=+0.281 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2277 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` < `1.4427` → IC=+0.217 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4427 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` > `2.2137` → IC=+0.240 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2137 (IC base=+0.038)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.237 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.038)

- **PATRÓN** `ibs_20min` < `0.1579` → IC=+0.149 (n=827)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.1579 (IC base=-0.023)

- **PATRÓN** `volumen_pendiente_norm` < `0.0751` → IC=+0.418 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0751 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` < `2.6396` → IC=+0.411 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6396 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` > `1.5396` → IC=+0.411 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5396 (IC base=-0.023)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.404 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=-0.023)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8619` → IC=+0.152 (n=966)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.8619 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.12` → IC=+0.194 (n=710)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.12 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` > `0.6783` → IC=+0.180 (n=1224)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 0.6783 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.2738` → IC=+0.217 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2738 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.4208` → IC=+0.203 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4208 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` > `2.4101` → IC=+0.190 (n=449)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.4101 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `226.0` → IC=+0.232 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 226.0 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.1603` → IC=+0.228 (n=840)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1603 (IC base=+0.000)

- **PATRÓN** `volumen_regimen` > `0.6201` → IC=+0.233 (n=813)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6201 (IC base=+0.000)

- **PATRÓN** `volumen_pendiente_norm` < `0.0729` → IC=+0.225 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0729 (IC base=+0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.2731` → IC=+0.296 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2731 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` < `1.5463` → IC=+0.237 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5463 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` > `2.1744` → IC=+0.239 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1744 (IC base=+0.000)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.273 (n=2152)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.254)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.260 (n=2166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.254)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.255 (n=1922)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.254)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=1118)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.254)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.792` → IC=+0.283 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.792 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.268 (n=1852)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` > `2.1642` → IC=+0.261 (n=1376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1642 (IC base=+0.254)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.264 (n=2545)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.254)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.303 (n=1818)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.1839` → IC=+0.307 (n=800)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1839 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.320 (n=703)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.288)

- **PATRÓN** `ibs_20min` < `0.3644` → IC=+0.293 (n=1819)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3644 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.656` → IC=+0.304 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.656 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.747` → IC=+0.288 (n=1953)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.747 (IC base=+0.288)

- **PATRÓN** `volumen_pendiente_norm` < `0.1942` → IC=+0.285 (n=1774)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1942 (IC base=+0.288)

- **PATRÓN** `volumen_pendiente_norm` > `0.3385` → IC=+0.297 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3385 (IC base=+0.288)

- **PATRÓN** `volumen_spike_ratio` < `1.7103` → IC=+0.302 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7103 (IC base=+0.288)

- **PATRÓN** `volumen_spike_ratio` > `2.6261` → IC=+0.292 (n=780)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6261 (IC base=+0.288)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.288 (n=1482)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.288)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7614` → IC=-0.180 (n=832)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7614
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=2497)

- **PATRÓN** `ibs_20min` > `0.8996` → IC=+0.165 (n=766)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.8996 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.2204` → IC=+0.217 (n=871)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2204 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `1.0092` → IC=+0.234 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0092 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.1681` → IC=+0.227 (n=1081)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1681 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.0801` → IC=+0.227 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0801 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.4079` → IC=+0.258 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4079 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.283 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.1265` → IC=+0.220 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1265 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` < `1.1993` → IC=+0.225 (n=678)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1993 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2975` → IC=+0.291 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2975 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.8566` → IC=+0.264 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8566 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.2169` → IC=+0.236 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2169 (IC base=+0.001)

- **PATRÓN** `ballena_activa_n` < `135.0` → IC=+0.252 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 135.0 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7645` → IC=-0.189 (n=1526)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7645
  - _Potencial_: sin este filtro IC_bueno=+0.287 (n=1526)

- **FILTRO** `ibs_20min` > `0.6667` → IC=-0.246 (n=750)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6667
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=2330)

- **FILTRO** `sigma_ewma_delta_pct` > `8.653` → IC=-0.232 (n=353)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.653
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=2727)

- **PATRÓN** `ibs_20min` > `0.7645` → IC=+0.287 (n=1526)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7645 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `1.0273` → IC=+0.333 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0273 (IC base=+0.049)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.734` → IC=+0.169 (n=481)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.734 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` < `0.8532` → IC=+0.315 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8532 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` > `0.6339` → IC=+0.306 (n=1161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6339 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` < `0.0986` → IC=+0.304 (n=1095)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0986 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.333 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.325 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.049)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.333 (n=756)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.049)

- **PATRÓN** `ibs_20min` < `0.5614` → IC=+0.134 (n=2035)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.5614 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` < `0.2729` → IC=+0.241 (n=885)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2729 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` < `0.7014` → IC=+0.262 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7014 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` < `0.0988` → IC=+0.235 (n=890)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0988 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.0717` → IC=+0.254 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0717 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `2.4236` → IC=+0.255 (n=887)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4236 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.267 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.024)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.336 (n=1521)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.292)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.309 (n=801)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.292)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.325 (n=1704)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.292)

- **PATRÓN** `dist_vwap_pct` > `0.2129` → IC=+0.320 (n=970)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2129 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.776` → IC=+0.314 (n=844)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.776 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.953` → IC=+0.293 (n=1925)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.953 (IC base=+0.292)

- **PATRÓN** `volumen_regimen` > `0.8564` → IC=+0.315 (n=1134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8564 (IC base=+0.292)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.339 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.292)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.303 (n=1626)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `2669.298` → IC=+0.310 (n=1134)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2669.298 (IC base=+0.292)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.329 (n=1427)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.292)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.322 (n=1209)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.187` → IC=+0.291 (n=796)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.187 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.299 (n=908)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.291)

- **PATRÓN** `ibs_20min` < `0.3675` → IC=+0.316 (n=1809)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3675 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.3121` → IC=+0.293 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3121 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.494` → IC=+0.301 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.494 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.039` → IC=+0.291 (n=2159)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.039 (IC base=+0.291)

- **PATRÓN** `volumen_regimen` < `0.8901` → IC=+0.291 (n=1206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8901 (IC base=+0.291)

- **PATRÓN** `volumen_regimen` > `1.2276` → IC=+0.322 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2276 (IC base=+0.291)

- **PATRÓN** `volumen_pendiente_norm` > `0.2325` → IC=+0.339 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2325 (IC base=+0.291)

- **PATRÓN** `volumen_spike_ratio` < `1.4188` → IC=+0.297 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4188 (IC base=+0.291)

- **PATRÓN** `volumen_spike_ratio` > `2.1367` → IC=+0.291 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1367 (IC base=+0.291)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.186 (n=3533)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0047 (IC base=+0.175)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.212 (n=3525)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.3533` → IC=+0.186 (n=9299)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.3533 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=11059)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` > `0.5651` → IC=+0.229 (n=10567)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5651 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.1714` → IC=+0.200 (n=4436)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1714 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.483` → IC=+0.250 (n=2128)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.483 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` < `1.2011` → IC=+0.168 (n=7030)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2011 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.161 (n=7030)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6279 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` > `0.2939` → IC=+0.195 (n=1558)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2939 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` < `1.5622` → IC=+0.175 (n=4489)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.5622 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `2.5992` → IC=+0.183 (n=3401)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.5992 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `2505.8886` → IC=+0.178 (n=7045)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 2505.8886 (IC base=+0.175)

- **PATRÓN** `ballena_activa_n` < `104.0` → IC=+0.191 (n=9496)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 104.0 (IC base=+0.175)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.190 (n=6810)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0066 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.0817` → IC=+0.222 (n=3402)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0817 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=3837)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` < `0.4857` → IC=+0.233 (n=10204)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4857 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.288` → IC=+0.202 (n=1687)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.288 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `1.1819` → IC=+0.167 (n=7302)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1819 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2917` → IC=+0.224 (n=1490)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2917 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `2.6124` → IC=+0.181 (n=3164)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.6124 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.188 (n=9166)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 106.0 (IC base=+0.178)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.233 (n=590)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.200)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.210 (n=591)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.3396` → IC=+0.221 (n=1769)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3396 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.207 (n=1876)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.204 (n=1181)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.9174` → IC=+0.287 (n=1179)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9174 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.337` → IC=+0.330 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.337 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2803` → IC=+0.259 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2803 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `1.8166` → IC=+0.193 (n=1107)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.8166 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `2.2345` → IC=+0.206 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2345 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.212 (n=1843)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `2014.215` → IC=+0.205 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2014.215 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.249 (n=1212)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.241)

- **PATRÓN** `sigma_h` > `0.0042` → IC=+0.247 (n=1377)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0042 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.1024` → IC=+0.298 (n=607)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1024 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.245 (n=1236)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.247 (n=685)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.3514` → IC=+0.259 (n=1376)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3514 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.383` → IC=+0.241 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.383 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.242` → IC=+0.246 (n=1493)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.242 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` < `0.0996` → IC=+0.240 (n=1182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0996 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.294` → IC=+0.275 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.294 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.4266` → IC=+0.251 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4266 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.6397` → IC=+0.244 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6397 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.246 (n=1516)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.241)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.224 (n=537)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.1657` → IC=+0.186 (n=1066)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.1657 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.178 (n=1604)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 6.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `0.3778` → IC=+0.224 (n=1598)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3778 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.2011` → IC=+0.211 (n=909)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2011 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.501` → IC=+0.233 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.501 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `0.6883` → IC=+0.168 (n=703)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.6883 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.199 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `1.5085` → IC=+0.177 (n=686)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.5085 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `2.4677` → IC=+0.157 (n=520)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.4677 (IC base=+0.157)

- **PATRÓN** `ballena_activa_n` < `233.0` → IC=+0.173 (n=670)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 233.0 (IC base=+0.157)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.164 (n=1691)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0057 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.234` → IC=+0.176 (n=1487)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.234 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.183 (n=642)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.5949` → IC=+0.200 (n=1690)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5949 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.75` → IC=+0.205 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.75 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.2032` → IC=+0.164 (n=1690)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2032 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.2285` → IC=+0.146 (n=1746)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.2285 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.1593` → IC=+0.148 (n=515)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.1593 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.4908` → IC=+0.153 (n=1575)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4908 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.7663` → IC=+0.144 (n=1050)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.7663 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `208.0` → IC=+0.173 (n=506)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 208.0 (IC base=+0.144)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0116` → IC=+0.233 (n=590)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0116 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.4094` → IC=+0.220 (n=1557)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4094 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.215 (n=1852)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.295 (n=927)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.565` → IC=+0.280 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.565 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.1276` → IC=+0.211 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1276 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `1.7658` → IC=+0.210 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7658 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.6813` → IC=+0.214 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6813 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.216 (n=2105)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2050.0484` → IC=+0.226 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2050.0484 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.246 (n=1343)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0101 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.1456` → IC=+0.267 (n=672)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1456 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.278 (n=517)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` < `0.3506` → IC=+0.252 (n=1526)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3506 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.649` → IC=+0.263 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.649 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.3492` → IC=+0.266 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3492 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` < `1.716` → IC=+0.246 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.716 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `2.7161` → IC=+0.237 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7161 (IC base=+0.229)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.233 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.229)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.179 (n=1495)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0064 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.0783` → IC=+0.198 (n=567)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.0783 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=1776)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.3293` → IC=+0.205 (n=1699)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3293 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1399` → IC=+0.188 (n=1071)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1399 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.979` → IC=+0.201 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.979 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `0.8559` → IC=+0.160 (n=1133)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8559 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1014` → IC=+0.167 (n=710)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.1014 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.4305` → IC=+0.161 (n=555)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.4305 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.5102` → IC=+0.155 (n=555)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.5102 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `5128.1918` → IC=+0.195 (n=1133)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 5128.1918 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `149.0` → IC=+0.152 (n=1635)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 149.0 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.162 (n=1798)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0071 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.3873` → IC=+0.152 (n=1798)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.3873 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=674)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.6686` → IC=+0.187 (n=1797)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6686 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.845` → IC=+0.165 (n=618)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 6.845 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.164 (n=1198)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.856 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.2975` → IC=+0.193 (n=272)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2975 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `1.8136` → IC=+0.142 (n=1113)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.8136 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `1.4237` → IC=+0.134 (n=1668)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.4237 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `4565.2642` → IC=+0.168 (n=1198)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4565.2642 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `149.0` → IC=+0.130 (n=1618)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 149.0 (IC base=+0.132)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.161 (n=878)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0098 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.4442` → IC=+0.130 (n=1700)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.4442 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=1980)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.216 (n=1937)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `1.0387` → IC=+0.216 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0387 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.945` → IC=+0.262 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.945 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `1.1983` → IC=+0.143 (n=1932)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1983 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` < `0.1637` → IC=+0.138 (n=1951)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` < 0.1637 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.549` → IC=+0.142 (n=823)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.549 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `2.4852` → IC=+0.134 (n=623)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.4852 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.131 (n=2028)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `2389.1426` → IC=+0.190 (n=1288)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2389.1426 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.150 (n=1528)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 45.0 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.143 (n=1723)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0091 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.1059` → IC=+0.179 (n=652)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.1059 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.141 (n=1978)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.5758` → IC=+0.220 (n=1954)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5758 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.349` → IC=+0.131 (n=592)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 5.349 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.585` → IC=+0.126 (n=1724)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 2.585 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `1.18` → IC=+0.137 (n=1954)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.18 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.276` → IC=+0.163 (n=247)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.276 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.4516` → IC=+0.143 (n=600)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4516 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `1.8145` → IC=+0.130 (n=1199)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.8145 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `2793.6768` → IC=+0.188 (n=886)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2793.6768 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.136 (n=1764)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 52.0 (IC base=+0.126)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.235 (n=1612)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.2883` → IC=+0.222 (n=1203)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2883 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.215 (n=1880)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.216 (n=1214)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.249 (n=1803)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.1969` → IC=+0.215 (n=1203)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1969 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` < `0.2845` → IC=+0.214 (n=1311)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2845 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.606` → IC=+0.244 (n=829)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.606 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` < `1.183` → IC=+0.216 (n=1803)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.183 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` > `0.6223` → IC=+0.220 (n=1803)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6223 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.273 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.283 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `2.4718` → IC=+0.216 (n=1750)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4718 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.4264` → IC=+0.220 (n=1750)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4264 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.213 (n=1668)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2661.3588` → IC=+0.222 (n=1202)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2661.3588 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0119` → IC=+0.229 (n=820)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0119 (IC base=+0.220)

- **PATRÓN** `sigma_h` > `0.0224` → IC=+0.222 (n=844)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0224 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.0901` → IC=+0.242 (n=621)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0901 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.239 (n=914)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` < `0.02` → IC=+0.291 (n=821)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.02 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `1.1769` → IC=+0.230 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1769 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.42` → IC=+0.248 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.42 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `0.6365` → IC=+0.231 (n=1862)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6365 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.280 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` < `2.2006` → IC=+0.213 (n=1509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2006 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `1.4377` → IC=+0.220 (n=1715)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4377 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `2635.1676` → IC=+0.229 (n=1241)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2635.1676 (IC base=+0.220)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.192 (n=1221)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0041 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.169 (n=926)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0083 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.3361` → IC=+0.179 (n=2439)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.3361 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.206 (n=1379)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `0.3274` → IC=+0.197 (n=2772)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.3274 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.784` → IC=+0.183 (n=424)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.784 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.76` → IC=+0.192 (n=1184)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 3.76 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `0.8664` → IC=+0.187 (n=1662)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.8664 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` > `1.2012` → IC=+0.177 (n=831)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 1.2012 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.1025` → IC=+0.175 (n=993)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1025 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.4373` → IC=+0.188 (n=898)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.4373 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.5177` → IC=+0.171 (n=897)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.5177 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.170 (n=2570)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.187 (n=2551)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 150.0 (IC base=+0.168)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.163 (n=951)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0036 (IC base=+0.115)

- **PATRÓN** `drift_60min` |x|≤ `0.3339` → IC=+0.124 (n=2508)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.3339 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.127 (n=2694)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.0737` → IC=+0.199 (n=950)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.0737 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `1.2207` → IC=+0.121 (n=2590)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.2207 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.0744` → IC=+0.127 (n=1088)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` > 0.0744 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `1.4373` → IC=+0.149 (n=922)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4373 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `5224.4606` → IC=+0.144 (n=1898)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 5224.4606 (IC base=+0.115)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.133 (n=926)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 21.0 (IC base=+0.115)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.202 (n=354)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.1011` → IC=+0.201 (n=353)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1011 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.187 (n=739)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.6264` → IC=+0.208 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6264 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.3086` → IC=+0.172 (n=248)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.3086 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.146` → IC=+0.173 (n=338)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 3.146 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.8799` → IC=+0.176 (n=535)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.8799 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.0705` → IC=+0.159 (n=315)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0705 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.2101` → IC=+0.162 (n=690)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.2101 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.414` → IC=+0.151 (n=784)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.414 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `14720.7097` → IC=+0.159 (n=535)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 14720.7097 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `148.0` → IC=+0.201 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 148.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.204 (n=316)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.2682` → IC=+0.166 (n=826)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.2682 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.154 (n=846)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 7.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.148 (n=951)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.611` → IC=+0.185 (n=826)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.611 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.742` → IC=+0.148 (n=180)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 8.742 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.494` → IC=+0.149 (n=989)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 6.494 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.2046` → IC=+0.149 (n=939)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.2046 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `0.7012` → IC=+0.158 (n=839)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.7012 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.197 (n=249)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.1142` → IC=+0.161 (n=816)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.1142 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.4012` → IC=+0.150 (n=927)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.4012 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=1216)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `288.0` → IC=+0.160 (n=799)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 288.0 (IC base=+0.147)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.232 (n=592)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.2086` → IC=+0.211 (n=590)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2086 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.214 (n=931)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `0.34` → IC=+0.234 (n=790)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.34 (IC base=+0.196)

- **PATRÓN** `dist_vwap_pct` > `0.3604` → IC=+0.203 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3604 (IC base=+0.196)

- **PATRÓN** `dist_vwap_pct` < `0.2092` → IC=+0.202 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2092 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.05` → IC=+0.220 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.05 (IC base=+0.196)

- **PATRÓN** `volumen_regimen` < `0.8392` → IC=+0.200 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8392 (IC base=+0.196)

- **PATRÓN** `volumen_regimen` > `1.1824` → IC=+0.217 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1824 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.1608` → IC=+0.224 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1608 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` < `1.4185` → IC=+0.230 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4185 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `2.4481` → IC=+0.213 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4481 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.162 (n=374)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0038 (IC base=+0.113)

- **PATRÓN** `drift_60min` |x|≤ `0.096` → IC=+0.136 (n=284)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.096 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.151 (n=319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.087` → IC=+0.163 (n=283)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.087 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.377` → IC=+0.149 (n=220)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 6.377 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `0.6876` → IC=+0.161 (n=373)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.6876 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.2234` → IC=+0.143 (n=138)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.2234 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.424` → IC=+0.145 (n=274)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.424 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `4111.5445` → IC=+0.137 (n=756)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 4111.5445 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.138 (n=354)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 41.0 (IC base=+0.113)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.4737` → IC=-0.124 (n=269)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4737
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=523)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.173 (n=615)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0051 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.194 (n=563)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 8.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.279 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.97` → IC=+0.243 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.97 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.339` → IC=+0.216 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.339 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `1.0671` → IC=+0.180 (n=542)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 1.0671 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` > `0.6503` → IC=+0.166 (n=615)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6503 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.2809` → IC=+0.177 (n=91)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2809 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `1.4594` → IC=+0.165 (n=198)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.4594 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `2.1972` → IC=+0.175 (n=269)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.1972 (IC base=+0.161)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.166 (n=653)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.02 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `3080.6393` → IC=+0.201 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3080.6393 (IC base=+0.161)

- **PATRÓN** `ibs_20min` < `0.4737` → IC=+0.146 (n=523)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.4737 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` < `1.5709` → IC=+0.126 (n=249)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.5709 (IC base=+0.054)

- **PATRÓN** `libro_liquidez` > `2865.6878` → IC=+0.151 (n=270)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2865.6878 (IC base=+0.054)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.143 (n=242)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 15.0 (IC base=+0.054)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0238` → IC=+0.170 (n=192)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0238 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.186 (n=192)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.007 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.3919` → IC=+0.167 (n=169)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3919 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.181 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 16.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.204 (n=86)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.5556` → IC=+0.184 (n=172)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.5556 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.2393` → IC=+0.167 (n=106)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.2393 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `1.115` → IC=+0.162 (n=214)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 1.115 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.385` → IC=+0.181 (n=164)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 3.385 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `0.6182` → IC=+0.175 (n=192)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6182 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` < `0.2537` → IC=+0.184 (n=188)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.2537 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.4483` → IC=+0.241 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4483 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `2.6132` → IC=+0.172 (n=56)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.6132 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.183 (n=197)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `2503.8283` → IC=+0.169 (n=128)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2503.8283 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.160 (n=189)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0119 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.158 (n=77)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.131 (n=212)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.6 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` > `1.1597` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1597 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.025` → IC=+0.146 (n=80)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 3.025 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` > `0.6515` → IC=+0.126 (n=212)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.6515 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.2293` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2293 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` > `2.8124` → IC=+0.132 (n=66)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.8124 (IC base=+0.116)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.138 (n=172)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 17.0 (IC base=+0.116)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.179 (n=4596)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0046 (IC base=+0.178)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.215 (n=4582)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=14400)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `0.4545` → IC=+0.225 (n=13739)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4545 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `0.1657` → IC=+0.187 (n=5033)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1657 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.443` → IC=+0.246 (n=3379)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.443 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `0.8788` → IC=+0.175 (n=6145)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.8788 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2891` → IC=+0.200 (n=1855)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2891 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `2.5944` → IC=+0.196 (n=4436)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.5944 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `2469.6144` → IC=+0.182 (n=9159)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2469.6144 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.204 (n=10930)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 79.0 (IC base=+0.178)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.197 (n=5477)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0053 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.1473` → IC=+0.197 (n=5469)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.1473 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=4666)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.4505` → IC=+0.251 (n=10937)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4505 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.097` → IC=+0.212 (n=1745)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.097 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.725` → IC=+0.187 (n=11986)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 3.725 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `0.7053` → IC=+0.164 (n=3699)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.7053 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.2895` → IC=+0.252 (n=1662)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2895 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `1.8591` → IC=+0.193 (n=7765)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.8591 (IC base=+0.187)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.210 (n=7632)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.187)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.252 (n=757)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.210)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.229 (n=758)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.3555` → IC=+0.213 (n=2269)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3555 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=1098)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.211 (n=1525)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.329 (n=848)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.776` → IC=+0.347 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.776 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.272 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.4444` → IC=+0.205 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4444 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.589` → IC=+0.226 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.589 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=2332)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2011.3648` → IC=+0.220 (n=1029)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2011.3648 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.267 (n=1271)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.258)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.262 (n=1696)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.124` → IC=+0.276 (n=836)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.124 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.266 (n=1727)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` < `0.359` → IC=+0.284 (n=1670)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.359 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.483` → IC=+0.264 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.483 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.2858` → IC=+0.286 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2858 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `2.6325` → IC=+0.279 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6325 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.260 (n=2088)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.258)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.203 (n=740)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.1796` → IC=+0.167 (n=1477)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1796 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=2326)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.2731` → IC=+0.207 (n=2214)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2731 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.1319` → IC=+0.186 (n=1194)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1319 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.721` → IC=+0.174 (n=369)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 11.721 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.221` → IC=+0.154 (n=2025)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.221 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.6267` → IC=+0.173 (n=738)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.6267 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.27` → IC=+0.191 (n=315)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.27 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.1394` → IC=+0.159 (n=1897)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1394 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.5228` → IC=+0.153 (n=1926)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5228 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `248.0` → IC=+0.187 (n=704)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 248.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.162 (n=1836)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0057 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.2579` → IC=+0.164 (n=1616)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.2579 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.174 (n=700)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.684` → IC=+0.196 (n=1836)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.684 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.135` → IC=+0.166 (n=1705)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.135 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.516` → IC=+0.168 (n=311)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.516 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.1847` → IC=+0.159 (n=1837)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1847 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.1536` → IC=+0.203 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1536 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.432` → IC=+0.154 (n=1734)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.432 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.7717` → IC=+0.160 (n=1156)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7717 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `257.0` → IC=+0.149 (n=548)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 257.0 (IC base=+0.147)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.232 (n=2259)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.230 (n=2258)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.227 (n=2024)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.306 (n=852)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.514` → IC=+0.306 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.514 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` < `0.2044` → IC=+0.225 (n=2285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2044 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `1.615` → IC=+0.227 (n=2178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.615 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.230 (n=2688)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.241 (n=1418)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.184` → IC=+0.256 (n=936)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.184 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.260 (n=807)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.239 (n=764)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.0148` → IC=+0.303 (n=710)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0148 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.961` → IC=+0.289 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.961 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.3408` → IC=+0.299 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3408 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.7062` → IC=+0.243 (n=881)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7062 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.1247` → IC=+0.243 (n=1335)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1247 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.238 (n=1205)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.260 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.237)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.197 (n=1035)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0038 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.3335` → IC=+0.152 (n=2069)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.3335 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.157 (n=2458)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.2662` → IC=+0.192 (n=2351)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.2662 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.5529` → IC=+0.165 (n=606)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.5529 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.19` → IC=+0.152 (n=958)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 4.19 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.873` → IC=+0.164 (n=1568)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.873 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.2368` → IC=+0.173 (n=420)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2368 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.5243` → IC=+0.163 (n=1008)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.5243 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `2.1776` → IC=+0.152 (n=1038)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 2.1776 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `7336.8828` → IC=+0.236 (n=1066)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7336.8828 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.180 (n=757)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 70.0 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.196 (n=633)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0033 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.3466` → IC=+0.146 (n=1670)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3466 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.163 (n=696)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.137 (n=661)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 5.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.733` → IC=+0.188 (n=1898)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.733 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.331` → IC=+0.180 (n=385)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 9.331 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.6234` → IC=+0.150 (n=633)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6234 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.2976` → IC=+0.235 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2976 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.2491` → IC=+0.138 (n=1603)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.2491 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.4421` → IC=+0.146 (n=1821)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4421 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `5601.6515` → IC=+0.198 (n=861)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 5601.6515 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `165.0` → IC=+0.137 (n=1820)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 165.0 (IC base=+0.134)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.138 (n=2368)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.0055 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=868)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.4524` → IC=+0.202 (n=2367)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4524 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `1.0297` → IC=+0.210 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0297 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.077` → IC=+0.256 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.077 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `1.2342` → IC=+0.141 (n=2367)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.2342 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` < `0.1612` → IC=+0.132 (n=2444)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.1612 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.1932` → IC=+0.139 (n=1045)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.1932 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.134 (n=2421)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `2926.4233` → IC=+0.255 (n=789)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2926.4233 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.151 (n=748)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 27.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.175 (n=759)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0056 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.1315` → IC=+0.170 (n=756)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1315 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=2345)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.235 (n=2011)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.218` → IC=+0.141 (n=1920)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.218 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.256` → IC=+0.128 (n=310)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 9.256 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.463` → IC=+0.136 (n=2190)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 3.463 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `0.7133` → IC=+0.158 (n=998)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.7133 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2229` → IC=+0.186 (n=368)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2229 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `2.1519` → IC=+0.143 (n=1847)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.1519 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2831.1065` → IC=+0.203 (n=756)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2831.1065 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.144 (n=1852)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 50.0 (IC base=+0.125)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.237 (n=2283)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.224 (n=2394)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.225 (n=1646)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.267 (n=2046)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `0.208` → IC=+0.235 (n=1272)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.208 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.777` → IC=+0.265 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.777 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` < `1.2332` → IC=+0.226 (n=2284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2332 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `0.6408` → IC=+0.224 (n=2283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6408 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2873` → IC=+0.245 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2873 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.5113` → IC=+0.245 (n=738)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5113 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.226 (n=2082)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `2666.66` → IC=+0.232 (n=1522)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2666.66 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0097` → IC=+0.220 (n=802)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0097 (IC base=+0.218)

- **PATRÓN** `sigma_h` > `0.0227` → IC=+0.234 (n=1091)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0227 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.232 (n=1710)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` < `0.4151` → IC=+0.267 (n=2117)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4151 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.95` → IC=+0.258 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.95 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` > `1.2332` → IC=+0.248 (n=803)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2332 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.2805` → IC=+0.289 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2805 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `1.432` → IC=+0.220 (n=2214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.432 (IC base=+0.218)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.174 (n=4081)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.232 (n=1380)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.5031` → IC=+0.202 (n=4139)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5031 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=1531)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.194 (n=1853)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 6.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` > `0.9402` → IC=+0.242 (n=1380)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9402 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` > `0.1717` → IC=+0.198 (n=1507)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1717 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` < `0.2456` → IC=+0.193 (n=2532)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.2456 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.223` → IC=+0.219 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.223 (IC base=+0.192)

- **PATRÓN** `volumen_regimen` < `0.7028` → IC=+0.204 (n=1280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7028 (IC base=+0.192)

- **PATRÓN** `volumen_regimen` > `0.8857` → IC=+0.195 (n=1939)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` > 0.8857 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` > `0.1685` → IC=+0.219 (n=1160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1685 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` < `1.4561` → IC=+0.200 (n=1360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4561 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `1.8561` → IC=+0.196 (n=2719)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.8561 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.201 (n=3110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `3869.705` → IC=+0.205 (n=2759)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3869.705 (IC base=+0.192)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.221 (n=1025)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.4875` → IC=+0.187 (n=3073)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.4875 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.198 (n=1059)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.192 (n=1389)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 6.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` < `0.1739` → IC=+0.197 (n=1352)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.1739 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.6524` → IC=+0.181 (n=534)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.6524 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.176` → IC=+0.179 (n=3069)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 6.176 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `1.1036` → IC=+0.181 (n=2538)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 1.1036 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.177 (n=2806)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.074` → IC=+0.177 (n=1399)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.074 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` < `2.5514` → IC=+0.175 (n=3031)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 2.5514 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `1.8229` → IC=+0.181 (n=2020)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.8229 (IC base=+0.172)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.174 (n=4081)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.186 (n=1325)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 36.0 (IC base=+0.172)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.239 (n=178)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.0834` → IC=+0.260 (n=177)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0834 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.224 (n=531)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.213 (n=235)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.5153` → IC=+0.236 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5153 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.7702` → IC=+0.216 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7702 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.179` → IC=+0.216 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.179 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.039` → IC=+0.236 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.039 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.526` → IC=+0.215 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.526 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.2246` → IC=+0.222 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2246 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `0.8398` → IC=+0.228 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8398 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.2975` → IC=+0.306 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2975 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.4501` → IC=+0.232 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4501 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `12545.7532` → IC=+0.237 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12545.7532 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.228 (n=469)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.1125` → IC=+0.179 (n=468)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.1125 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.193 (n=398)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.198 (n=356)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 4.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.144` → IC=+0.183 (n=468)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.144 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.6071` → IC=+0.154 (n=483)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.6071 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.6649` → IC=+0.183 (n=102)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.6649 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.211` → IC=+0.151 (n=1080)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.211 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.391` → IC=+0.167 (n=1048)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 6.391 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.8812` → IC=+0.188 (n=710)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8812 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.2218` → IC=+0.182 (n=221)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2218 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.5395` → IC=+0.155 (n=1060)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.5395 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.8221` → IC=+0.170 (n=707)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.8221 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `11531.9522` → IC=+0.161 (n=1064)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 11531.9522 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `700.0` → IC=+0.161 (n=1018)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 700.0 (IC base=+0.149)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.200 (n=231)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.171)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.186 (n=313)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0098 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.581` → IC=+0.179 (n=689)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.581 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` > `0.994` → IC=+0.233 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.994 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.494` → IC=+0.222 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.494 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.2079` → IC=+0.222 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2079 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `1.6744` → IC=+0.172 (n=230)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.6744 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `3.3613` → IC=+0.184 (n=229)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 3.3613 (IC base=+0.171)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.241 (n=56)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.295 (n=37)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.281 (n=39)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `0.2121` → IC=+0.276 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2121 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.442` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.442 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.1988` → IC=+0.259 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1988 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `2.3165` → IC=+0.244 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3165 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `1.861` → IC=+0.265 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.861 (IC base=+0.237)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.211 (n=1100)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.007 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.1493` → IC=+0.222 (n=549)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1493 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=458)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.200 (n=565)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.2837` → IC=+0.219 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2837 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.88` → IC=+0.208 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.88 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.152` → IC=+0.207 (n=1125)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.152 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `0.6294` → IC=+0.208 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6294 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `1.2448` → IC=+0.208 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2448 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` < `0.1066` → IC=+0.200 (n=1149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1066 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.1655` → IC=+0.212 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1655 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.4717` → IC=+0.206 (n=1221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4717 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=1259)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.229 (n=334)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.4937` → IC=+0.194 (n=994)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.4937 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.182 (n=335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.181 (n=666)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 10.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` < `0.7503` → IC=+0.178 (n=994)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.7503 (IC base=+0.170)

- **PATRÓN** `ibs_20min` > `0.0853` → IC=+0.171 (n=993)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.0853 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` > `0.6371` → IC=+0.191 (n=192)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.6371 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.759` → IC=+0.174 (n=1018)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` < 6.759 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `0.6415` → IC=+0.204 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6415 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` > `0.7215` → IC=+0.171 (n=888)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 0.7215 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.187 (n=417)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `2.1925` → IC=+0.185 (n=856)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 2.1925 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `7424.5718` → IC=+0.186 (n=993)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 7424.5718 (IC base=+0.170)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.217 (n=359)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.3032` → IC=+0.181 (n=359)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.3032 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.196 (n=551)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 3.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.5469` → IC=+0.204 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5469 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.1937` → IC=+0.210 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1937 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.559` → IC=+0.220 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.559 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `0.694` → IC=+0.211 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.694 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.1652` → IC=+0.225 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1652 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `1.468` → IC=+0.188 (n=524)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.468 (IC base=+0.172)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.183 (n=645)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `3413.2842` → IC=+0.223 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3413.2842 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.191 (n=464)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 48.0 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.213 (n=134)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.206 (n=134)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.372` → IC=+0.236 (n=267)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.372 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.217 (n=270)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` < `0.1837` → IC=+0.242 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1837 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` > `0.772` → IC=+0.230 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.772 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.035` → IC=+0.216 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.035 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.985` → IC=+0.191 (n=347)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 2.985 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` < `0.756` → IC=+0.202 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.756 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` > `0.6799` → IC=+0.187 (n=400)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.6799 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` < `0.1073` → IC=+0.223 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1073 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` < `1.6271` → IC=+0.194 (n=171)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.6271 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `2.2075` → IC=+0.202 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2075 (IC base=+0.186)

- **PATRÓN** `libro_liquidez` > `3873.4371` → IC=+0.199 (n=267)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 3873.4371 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.223 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.186)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.154 (n=591)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0038 (IC base=+0.073)

- **PATRÓN** `ibs_20min` > `0.4223` → IC=+0.146 (n=1251)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.4223 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` > `0.73` → IC=+0.164 (n=236)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.73 (IC base=+0.073)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.471` → IC=+0.176 (n=282)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 11.471 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.172 (n=175)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.073)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.143 (n=211)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0029 (IC base=+0.058)

- **PATRÓN** `ibs_20min` < `0.1891` → IC=+0.263 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1891 (IC base=+0.058)

- **PATRÓN** `dist_vwap_pct` < `0.0873` → IC=+0.136 (n=553)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.0873 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` > `0.1468` → IC=+0.205 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1468 (IC base=+0.058)

- **PATRÓN** `volumen_spike_ratio` < `2.5683` → IC=+0.136 (n=490)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.5683 (IC base=+0.058)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.139 (n=458)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0058 (IC base=+0.090)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.141 (n=157)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 18.0 (IC base=+0.090)

- **PATRÓN** `ibs_20min` > `0.3951` → IC=+0.167 (n=427)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.3951 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` > `0.1288` → IC=+0.161 (n=219)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1288 (IC base=+0.090)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.132 (n=191)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0036 (IC base=+0.082)

- **PATRÓN** `ibs_20min` < `0.0556` → IC=+0.295 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0556 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` < `0.2087` → IC=+0.131 (n=291)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.2087 (IC base=+0.082)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.245` → IC=+0.143 (n=253)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 7.245 (IC base=+0.082)

- **PATRÓN** `volumen_pendiente_norm` > `0.1526` → IC=+0.167 (n=64)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1526 (IC base=+0.082)

- **PATRÓN** `volumen_spike_ratio` < `2.5091` → IC=+0.140 (n=237)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.5091 (IC base=+0.082)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.145 (n=294)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0046 (IC base=+0.090)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.125 (n=414)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 7.0 (IC base=+0.090)

- **PATRÓN** `ibs_20min` > `0.6816` → IC=+0.201 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6816 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` > `0.1234` → IC=+0.177 (n=218)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1234 (IC base=+0.090)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.674` → IC=+0.256 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.674 (IC base=+0.090)

- **PATRÓN** `volumen_pendiente_norm` > `0.2829` → IC=+0.172 (n=56)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2829 (IC base=+0.090)

- **PATRÓN** `libro_liquidez` > `1182.3241` → IC=+0.143 (n=362)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 1182.3241 (IC base=+0.090)

- **PATRÓN** `ibs_20min` < `0.1005` → IC=+0.289 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1005 (IC base=+0.013)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.243` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 11.243 (IC base=+0.013)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.01` → IC=-0.202 (n=55)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=169)

- **FILTRO** `ibs_20min` > `0.16` → IC=-0.287 (n=45)

  - _Acción_: SKIP cuando `ibs_20min` > 0.16
  - _Potencial_: sin este filtro IC_bueno=+0.264 (n=138)

- **PATRÓN** `ibs_20min` > `0.76` → IC=+0.167 (n=277)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.76 (IC base=+0.040)

- **PATRÓN** `dist_vwap_pct` > `0.7192` → IC=+0.139 (n=106)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.7192 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.2443` → IC=+0.191 (n=82)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2443 (IC base=+0.040)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.175 (n=149)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0081 (IC base=+0.066)

- **PATRÓN** `ibs_20min` < `0.16` → IC=+0.264 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.16 (IC base=+0.066)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.949` → IC=+0.315 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.949 (IC base=+0.066)

- **PATRÓN** `volumen_regimen` > `0.971` → IC=+0.177 (n=63)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.971 (IC base=+0.066)

- **PATRÓN** `volumen_pendiente_norm` > `0.1476` → IC=+0.305 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1476 (IC base=+0.066)

- **PATRÓN** `volumen_spike_ratio` < `2.18` → IC=+0.183 (n=102)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.18 (IC base=+0.066)

- **PATRÓN** `volumen_spike_ratio` > `2.5298` → IC=+0.207 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5298 (IC base=+0.066)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.205 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.066)

- **PATRÓN** `libro_liquidez` > `774.2903` → IC=+0.175 (n=81)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 774.2903 (IC base=+0.066)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1826` → IC=-0.306 (n=65)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1826
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=196)

- **FILTRO** `dist_vwap_pct` > `0.2352` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2352
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=247)

- **FILTRO** `volumen_regimen` < `0.7446` → IC=-0.336 (n=65)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7446
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=198)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.379 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.240 (n=171)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.297 (n=67)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=160)

- **FILTRO** `dist_vwap_pct` > `0.3287` → IC=-0.389 (n=34)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3287
  - _Potencial_: sin este filtro IC_bueno=-0.254 (n=193)

- **FILTRO** `sigma_ewma_delta_pct` > `8.389` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.389
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=197)

- **FILTRO** `volumen_pendiente_norm` > `0.0718` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0718
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=122)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` < `0.0035` → IC=-0.233 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=44)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.283 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=66)

- **FILTRO** `volumen_spike_ratio` > `3.7991` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.7991
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=49)

- **FILTRO** `sigma_h` < `0.002` → IC=-0.308 (n=24)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.002
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=74)

- **FILTRO** `sigma_ewma_delta_pct` > `2.402` → IC=-0.294 (n=32)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.402
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=66)

- **FILTRO** `volumen_regimen` > `0.8276` → IC=-0.346 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8276
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=74)

- **FILTRO** `volumen_regimen` < `0.5547` → IC=-0.269 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.5547
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=74)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` < `0.0026` → IC=-0.370 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0026
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=66)

- **FILTRO** `ibs_20min` < `0.6002` → IC=-0.467 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6002
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=59)

- **FILTRO** `drift_60min` |x|> `0.1855` → IC=-0.273 (n=20)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1855
  - _Potencial_: sin este filtro IC_bueno=-0.262 (n=61)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.354 (n=39)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=45)

- **FILTRO** `ibs_20min` > `0.7492` → IC=-0.367 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7492
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **PATRÓN** `ibs_20min` > `0.9508` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.9508 (IC base=-0.152)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=73)

- **FILTRO** `volumen_spike_ratio` < `1.5614` → IC=-0.389 (n=16)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.5614
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=48)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=63)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=30)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=23)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.167 (n=190)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0058 (IC base=+0.090)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.125 (n=206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 15.0 (IC base=+0.090)

- **PATRÓN** `ibs_20min` > `0.6616` → IC=+0.135 (n=417)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 0.6616 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` > `0.4856` → IC=+0.196 (n=90)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.4856 (IC base=+0.090)

- **PATRÓN** `volumen_spike_ratio` < `2.5313` → IC=+0.123 (n=316)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.5313 (IC base=+0.090)

- **PATRÓN** `ibs_20min` < `0.156` → IC=+0.176 (n=408)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.156 (IC base=+0.084)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.348` → IC=+0.213 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.348 (IC base=+0.084)

- **PATRÓN** `libro_liquidez` > `2835.8733` → IC=+0.166 (n=309)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2835.8733 (IC base=+0.084)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6496` → IC=-0.273 (n=42)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6496
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=128)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.250 (n=70)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.170 (n=95)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.157)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.158 (n=71)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 5.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` < `0.1381` → IC=+0.211 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1381 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.879` → IC=+0.179 (n=166)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 4.879 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` > `0.6869` → IC=+0.188 (n=187)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 0.6869 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` < `0.1895` → IC=+0.185 (n=179)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.1895 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `2.2815` → IC=+0.183 (n=156)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 2.2815 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `1.4468` → IC=+0.182 (n=177)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.4468 (IC base=+0.157)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1562` → IC=-0.167 (n=28)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1562
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=119)

- **PATRÓN** `volumen_spike_ratio` < `1.7963` → IC=+0.158 (n=74)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.7963 (IC base=+0.054)

- **PATRÓN** `libro_liquidez` > `1535.3678` → IC=+0.129 (n=138)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 1535.3678 (IC base=+0.054)

- **PATRÓN** `ibs_20min` < `0.2075` → IC=+0.165 (n=150)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.2075 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.19` → IC=+0.300 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.19 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` < `0.618` → IC=+0.144 (n=57)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.618 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` > `0.2221` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.2221 (IC base=+0.070)

- **PATRÓN** `libro_liquidez` > `2393.5742` → IC=+0.161 (n=57)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2393.5742 (IC base=+0.070)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.1679` → IC=-0.207 (n=56)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1679
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=58)

- **FILTRO** `dist_vwap_pct` > `0.2725` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2725
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=92)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.286 (n=101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.262 (n=141)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.237 (n=154)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` > `0.9412` → IC=+0.248 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9412 (IC base=+0.235)

- **PATRÓN** `dist_vwap_pct` > `0.6388` → IC=+0.372 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6388 (IC base=+0.235)

- **PATRÓN** `dist_vwap_pct` < `0.1413` → IC=+0.241 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1413 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.365` → IC=+0.292 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.365 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` < `1.0151` → IC=+0.272 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0151 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` < `0.2519` → IC=+0.289 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2519 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.321 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` < `1.415` → IC=+0.357 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.415 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.1062` → IC=+0.287 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1062 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.237 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.418` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.418 (IC base=-0.069)

### LATE_WINDOW_5MIN
- **PATRÓN** `drift_ventana_pct` |x|> `0.332` → IC=+0.292 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.332 (IC base=+0.283)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.368 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.283)

- **PATRÓN** `drift_15min` |x|≤ `0.9257` → IC=+0.447 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.9257 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.8011` → IC=+0.351 (n=45)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8011 (IC base=+0.283)

- **PATRÓN** `ballena_activa_n` < `1127.0` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1127.0 (IC base=+0.283)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3418` → IC=+0.250 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3418 (IC base=+0.212)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.220 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.212)

- **PATRÓN** `elapsed_s` < `214.1` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 214.1 (IC base=+0.212)

- **PATRÓN** `drift_15min` |x|≤ `1.251` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.251 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.263 (n=36)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.212)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.307 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.268 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.212)

### LATE_WINDOW_5MIN#BTC#5min
- **PATRÓN** `drift_ventana_pct` |x|> `0.332` → IC=+0.292 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.332 (IC base=+0.283)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.368 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.283)

- **PATRÓN** `drift_15min` |x|≤ `0.9257` → IC=+0.447 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.9257 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.8011` → IC=+0.351 (n=45)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8011 (IC base=+0.283)

- **PATRÓN** `ballena_activa_n` < `1127.0` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1127.0 (IC base=+0.283)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3418` → IC=+0.250 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3418 (IC base=+0.212)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.220 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.212)

- **PATRÓN** `elapsed_s` < `214.1` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 214.1 (IC base=+0.212)

- **PATRÓN** `drift_15min` |x|≤ `1.251` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.251 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.263 (n=36)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.212)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.307 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.268 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.212)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.121 (n=1025)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `2870.4056` → IC=+0.135 (n=477)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2870.4056 (IC base=+0.102)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.121 (n=1025)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `2870.4056` → IC=+0.135 (n=477)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2870.4056 (IC base=+0.102)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=156)

- **FILTRO** `libro_liquidez` < `10545.7403` → IC=-0.178 (n=113)

  - _Acción_: SKIP cuando `libro_liquidez` < 10545.7403
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=59)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=246)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=232)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=54)

- **FILTRO** `hora_utc` < `3.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=58)

- **FILTRO** `libro_liquidez` < `10893.2451` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 10893.2451
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=56)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=25)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `4919.88` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `liq_usd_total` < 4919.88
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.136 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=107)

### LIQUIDACIONES_15M#XRP#15min
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
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=2885)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=98)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=55)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.163 (n=87)

- **FILTRO** `ballena_activa_n` > `98.0` → IC=-0.208 (n=63)

  - _Acción_: SKIP cuando `ballena_activa_n` > 98.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=22)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.188 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=116)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.130 (n=98)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 13.0 (IC base=+0.041)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.132 (n=183)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.495 (IC base=+0.040)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=1072)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=1026)

- **FILTRO** `liq_usd_total` < `9664.41` → IC=-0.231 (n=24)

  - _Acción_: SKIP cuando `liq_usd_total` < 9664.41
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9855` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9855
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=17)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.292 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `ballena_activa_n` > `142.0` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 142.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=666)

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
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=357)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=338)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.151 (n=127)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.495 (IC base=+0.020)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=778)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=778)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.133 (n=246)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=612)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=599)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=599)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=217)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=217)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.136 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=179)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.122 (n=88)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=144)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=149)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=173)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=242)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=174)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=304)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=304)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=215)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.43` → IC=-0.124 (n=1481)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1555)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` > `0.45` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

- **FILTRO** `restante_min` < `3.89` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `restante_min` < 3.89
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

- **FILTRO** `lag_apertura_s` > `66.61` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `lag_apertura_s` > 66.61
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.144 (n=192)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=101)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.140 (n=98)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=259)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.214 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.46 (IC base=+0.045)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `restante_min` < `12.46` → IC=-0.133 (n=96)

  - _Acción_: SKIP cuando `restante_min` < 12.46
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=96)

- **FILTRO** `lag_apertura_s` > `152.92` → IC=-0.129 (n=95)

  - _Acción_: SKIP cuando `lag_apertura_s` > 152.92
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=97)

- **FILTRO** `profundidad_ratio` < `23.6` → IC=-0.133 (n=96)

  - _Acción_: SKIP cuando `profundidad_ratio` < 23.6
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=96)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.125 (n=126)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=73)

- **FILTRO** `lag_apertura_s` > `76.6` → IC=-0.144 (n=99)

  - _Acción_: SKIP cuando `lag_apertura_s` > 76.6
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=100)

- **PATRÓN** `py_entrada` < `0.58` → IC=+0.129 (n=60)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` < 0.58 (IC base=+0.062)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.142 (n=202)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=70)

- **FILTRO** `profundidad_ratio` < `37.6` → IC=-0.200 (n=68)

  - _Acción_: SKIP cuando `profundidad_ratio` < 37.6
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=204)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.235 (n=47)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=201)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.122 (n=88)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.51 (IC base=-0.024)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.123 (n=221)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=124)

- **FILTRO** `restante_min` < `3.32` → IC=-0.187 (n=113)

  - _Acción_: SKIP cuando `restante_min` < 3.32
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=232)

- **FILTRO** `lag_apertura_s` > `98.98` → IC=-0.198 (n=117)

  - _Acción_: SKIP cuando `lag_apertura_s` > 98.98
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=228)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.132 (n=55)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=205)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **PATRÓN** `py_entrada` < `0.5` → IC=+0.135 (n=94)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.5 (IC base=+0.004)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.132 (n=207)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=109)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.159 (n=174)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=221)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.170 (n=4656)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=15078)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.166 (n=5114)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=15367)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.194 (n=853)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=2659)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.152 (n=857)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=2816)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.173 (n=711)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=2246)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.176 (n=888)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=2680)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.186 (n=921)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=2793)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.161 (n=848)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=2673)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2225)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2564)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=3304)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.172 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=412)

- **FILTRO** `ibs_20min` > `0.1725` → IC=-0.142 (n=132)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1725
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=403)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `ibs_20min` < `0.1975` → IC=-0.223 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1975
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=224)

- **FILTRO** `py_entrada` > `0.615` → IC=-0.216 (n=86)

  - _Acción_: SKIP cuando `py_entrada` > 0.615
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=312)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.131 (n=383)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=798)

- **FILTRO** `libro_liquidez` < `2022.006` → IC=-0.165 (n=338)

  - _Acción_: SKIP cuando `libro_liquidez` < 2022.006
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=689)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=232)

### MOMENTUM_IBS_5M#BNB#5min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=40)

- **FILTRO** `drift_7min_pct` |x|> `0.0331` → IC=-0.158 (n=36)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0331
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=19)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0331` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_7min_pct` |x|≤ 0.0331 (IC base=-0.026)

### MOMENTUM_IBS_5M#BTC#5min
- **FILTRO** `hora_utc` > `18.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=90)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.152 (n=44)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.037)

### MOMENTUM_IBS_5M#DOGE#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=38)

### MOMENTUM_IBS_5M#ETH#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=414)

### MOMENTUM_IBS_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=631)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `8.0` → IC=-0.133 (n=13680)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=30668)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=10496)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=33852)

- **FILTRO** `ibs_7min` < `0.2545` → IC=-0.233 (n=11087)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2545
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=33261)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.154 (n=14879)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=29469)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.235 (n=13545)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=42943)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.177 (n=14093)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=42395)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.145 (n=2215)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=5330)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.309 (n=1808)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=5737)

- **FILTRO** `ibs_7min` < `0.708` → IC=-0.250 (n=2489)

  - _Acción_: SKIP cuando `ibs_7min` < 0.708
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=5056)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.190 (n=1584)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=5961)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.269 (n=2378)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=7445)

- **FILTRO** `ibs_7min` > `0.7778` → IC=-0.210 (n=2454)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7778
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=7369)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.132 (n=1796)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=5779)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.246 (n=1876)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=5699)

- **FILTRO** `ibs_7min` < `0.7391` → IC=-0.197 (n=1893)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7391
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=5682)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.184 (n=1886)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=5689)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.264 (n=1830)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=5877)

- **FILTRO** `ibs_7min` > `0.2649` → IC=-0.191 (n=1926)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2649
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=5781)

- **FILTRO** `ballena_activa_n` > `148.0` → IC=-0.188 (n=1912)

  - _Acción_: SKIP cuando `ballena_activa_n` > 148.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=5795)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.165 (n=1777)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=5429)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.318 (n=1714)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=5492)

- **FILTRO** `ibs_7min` < `0.7032` → IC=-0.247 (n=2377)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7032
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=4829)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.221 (n=1603)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5603)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.244 (n=2347)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=8080)

- **FILTRO** `ibs_7min` > `0.7342` → IC=-0.171 (n=2606)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7342
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=7821)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=2358)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=4934)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.240 (n=2174)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=5118)

- **FILTRO** `ibs_7min` < `0.7383` → IC=-0.186 (n=1823)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7383
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5469)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.186 (n=1794)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5498)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.269 (n=1842)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=5683)

- **FILTRO** `ibs_7min` > `0.2759` → IC=-0.179 (n=1879)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2759
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=5646)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.183 (n=1805)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=5720)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.271 (n=1761)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=5695)

- **FILTRO** `ibs_7min` < `0.25` → IC=-0.233 (n=1856)

  - _Acción_: SKIP cuando `ibs_7min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=5600)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.174 (n=2680)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=8092)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.279 (n=1749)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=5525)

- **FILTRO** `ibs_7min` < `0.2364` → IC=-0.223 (n=1818)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2364
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=5456)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.201 (n=1768)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=5506)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.206 (n=2478)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=7756)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=1247)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.147 (n=49)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=619)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1156)

- **FILTRO** `libro_liquidez` < `7941.0101` → IC=-0.131 (n=348)

  - _Acción_: SKIP cuando `libro_liquidez` < 7941.0101
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=709)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=360)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.226 (n=49)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=414)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.129 (n=68)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=598)

- **FILTRO** `libro_liquidez` < `3306.2556` → IC=-0.155 (n=166)

  - _Acción_: SKIP cuando `libro_liquidez` < 3306.2556
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=500)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=275)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3979` → IC=+0.141 (n=972)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio` |x|> 0.3979 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.137 (n=447)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 14.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.130 (n=360)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 4.0 (IC base=+0.127)

- **PATRÓN** `total_vol_5m` < `443.866` → IC=+0.156 (n=324)

  - _Acción_: Kelly boost +0.78€ cuando `total_vol_5m` < 443.866 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `3779.4381` → IC=+0.131 (n=440)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 3779.4381 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.147 (n=318)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 14.0 (IC base=+0.127)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4372` → IC=+0.154 (n=76)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio` |x|> 0.4372 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.223 (n=110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `2659.7686` → IC=+0.244 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2659.7686 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.201 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.145)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.159 (n=86)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 10.0 (IC base=+0.107)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4144` → IC=+0.187 (n=132)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.93€ cuando `delta_ratio` |x|> 0.4144 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.210 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.126)

- **PATRÓN** `total_vol_5m` < `388.5476` → IC=+0.219 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 388.5476 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7275.4252` → IC=+0.137 (n=177)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 7275.4252 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.200 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 73.0 (IC base=+0.126)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.180 (n=173)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.233 (n=58)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.151)

- **PATRÓN** `total_vol_5m` < `8082.459` → IC=+0.169 (n=173)

  - _Acción_: Kelly boost +0.84€ cuando `total_vol_5m` < 8082.459 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.184 (n=55)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 28.0 (IC base=+0.151)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.401` → IC=+0.139 (n=167)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio` |x|> 0.401 (IC base=+0.102)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.125 (n=166)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 13.0 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.195 (n=116)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `3657.3836` → IC=+0.167 (n=85)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3657.3836 (IC base=+0.102)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.6961` → IC=-0.238 (n=40)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.6961
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=122)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.266 (n=276)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=278)

- **FILTRO** `T_h` > `129.5932` → IC=-0.257 (n=138)

  - _Acción_: SKIP cuando `T_h` > 129.5932
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=416)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0049` → IC=-0.221 (n=109)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0049
  - _Potencial_: sin este filtro IC_bueno=+0.272 (n=55)

- **FILTRO** `T_h` > `88.6373` → IC=-0.357 (n=40)

  - _Acción_: SKIP cuando `T_h` > 88.6373
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=124)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.272 (n=55)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.054)

- **PATRÓN** `pct_vs_K` |x|≤ `1.73` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `pct_vs_K` |x|≤ 1.73 (IC base=-0.054)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `pct_vs_K` |x|> `8.3214` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.3214
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=37)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.186 (n=68)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=+0.139 (n=34)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.214 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=-0.077)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.202 (n=377)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=126)

- **FILTRO** `pct_vs_K` |x|> `3.4531` → IC=-0.445 (n=107)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4531
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=329)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0042` → IC=-0.189 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0042
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=131)

- **FILTRO** `T_h` > `77.6652` → IC=-0.161 (n=116)

  - _Acción_: SKIP cuando `T_h` > 77.6652
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=58)

- **FILTRO** `T_h` > `73.6519` → IC=-0.285 (n=119)

  - _Acción_: SKIP cuando `T_h` > 73.6519
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=41)

- **FILTRO** `pct_vs_K` |x|> `2.8429` → IC=-0.407 (n=52)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8429
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=108)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `T_h` < `139.5329` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `T_h` < 139.5329
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

- **FILTRO** `sigma_h` < `0.0085` → IC=-0.239 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

- **FILTRO** `T_h` > `144.5457` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` > 144.5457
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0094` → IC=-0.300 (n=103)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=37)

- **FILTRO** `T_h` < `87.9882` → IC=-0.287 (n=45)

  - _Acción_: SKIP cuando `T_h` < 87.9882
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=95)

- **FILTRO** `pct_vs_K` |x|> `3.1362` → IC=-0.457 (n=45)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.1362
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=88)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `T_h` < `145.7969` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` < 145.7969
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0078` → IC=-0.197 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0078
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=94)

- **FILTRO** `T_h` > `113.0501` → IC=-0.156 (n=62)

  - _Acción_: SKIP cuando `T_h` > 113.0501
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=63)

- **FILTRO** `sigma_h` > `0.0132` → IC=-0.344 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0132
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=59)

- **FILTRO** `T_h` > `36.4645` → IC=-0.382 (n=66)

  - _Acción_: SKIP cuando `T_h` > 36.4645
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=23)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1221` → IC=+0.460 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1221 (IC base=+0.332)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.380 (n=81)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.332)

- **PATRÓN** `T_h` < `1.0173` → IC=+0.349 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.0173 (IC base=+0.332)

- **PATRÓN** `T_h` > `0.8229` → IC=+0.393 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8229 (IC base=+0.332)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.475 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.332)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.347 (n=70)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.332)

- **PATRÓN** `edge` > `0.095` → IC=+0.454 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.095 (IC base=+0.422)

- **PATRÓN** `sigma_h` < `0.0121` → IC=+0.430 (n=169)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0121 (IC base=+0.422)

- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.446 (n=128)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0096 (IC base=+0.422)

- **PATRÓN** `T_h` > `1.48` → IC=+0.455 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.48 (IC base=+0.422)

- **PATRÓN** `dist_50` > `0.3811` → IC=+0.474 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3811 (IC base=+0.422)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.478 (n=132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.422)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1026` → IC=+0.456 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1026 (IC base=+0.429)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.417 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.429)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.458 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.429)

- **PATRÓN** `T_h` < `0.9672` → IC=+0.456 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9672 (IC base=+0.429)

- **PATRÓN** `T_h` > `0.4508` → IC=+0.422 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4508 (IC base=+0.429)

- **PATRÓN** `dist_50` > `0.4084` → IC=+0.478 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4084 (IC base=+0.429)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.423 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.429)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.439 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.429)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.1885` → IC=+0.480 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1885 (IC base=+0.427)

- **PATRÓN** `sigma_h` < `0.0161` → IC=+0.461 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0161 (IC base=+0.427)

- **PATRÓN** `T_h` > `0.7758` → IC=+0.457 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7758 (IC base=+0.427)

- **PATRÓN** `dist_50` > `0.3288` → IC=+0.461 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3288 (IC base=+0.427)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.435 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.427)

- **PATRÓN** `edge` > `0.2005` → IC=+0.477 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2005 (IC base=+0.462)

- **PATRÓN** `sigma_h` < `0.0157` → IC=+0.477 (n=127)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0157 (IC base=+0.462)

- **PATRÓN** `T_h` > `1.2259` → IC=+0.477 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.2259 (IC base=+0.462)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.492 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.462)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.472 (n=139)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.462)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=256)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=342)

- **PATRÓN** `streak_estiramiento` < `0.4547` → IC=+0.125 (n=86)

  - _Acción_: Kelly boost +0.62€ cuando `streak_estiramiento` < 0.4547 (IC base=+0.020)

- **PATRÓN** `streak_estiramiento` < `0.5687` → IC=+0.160 (n=151)

  - _Acción_: Kelly boost +0.80€ cuando `streak_estiramiento` < 0.5687 (IC base=+0.037)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=25)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `volumen_racha` > `982893.6` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `volumen_racha` > 982893.6
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=42)

- **FILTRO** `streak_estiramiento` > `0.479` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.479
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=58)

- **PATRÓN** `volumen_racha` < `982893.6` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_racha` < 982893.6 (IC base=+0.018)

- **PATRÓN** `streak_estiramiento` < `0.4177` → IC=+0.123 (n=51)

  - _Acción_: Kelly boost +0.61€ cuando `streak_estiramiento` < 0.4177 (IC base=+0.018)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.136 (n=75)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 10.0 (IC base=+0.079)

- **PATRÓN** `streak_estiramiento` < `0.3368` → IC=+0.161 (n=60)

  - _Acción_: Kelly boost +0.81€ cuando `streak_estiramiento` < 0.3368 (IC base=+0.079)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.144 (n=102)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 47.0 (IC base=+0.079)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=94)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=100)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=37)

- **FILTRO** `streak_estiramiento` > `1.1202` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_estiramiento` > 1.1202
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=32)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=25)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=820)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=602)

### STREAK_FADE_60M
- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=16)

- **FILTRO** `volumen_racha` > `9229.0178` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `volumen_racha` > 9229.0178
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

### STREAK_FADE_60M#ETH#60min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

### STREAK_FADE_60M#SOL#60min
- **PATRÓN** `regimen_ma_toques` > `4.0` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.038)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=830)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1320)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=979)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=983)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3519)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1873)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.201 (n=878)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.194)

- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.231 (n=878)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.194)

- **PATRÓN** `drift_60min` |x|≤ `0.1615` → IC=+0.202 (n=2316)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1615 (IC base=+0.194)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2234` → IC=+0.197 (n=878)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.2234 (IC base=+0.194)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1311` → IC=+0.213 (n=1012)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1311 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.203 (n=2440)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.194 (n=2727)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 17.0 (IC base=+0.194)

- **PATRÓN** `ibs_15` > `0.6027` → IC=+0.269 (n=2632)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6027 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` > `0.1202` → IC=+0.195 (n=1239)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1202 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.887` → IC=+0.271 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.887 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `6860.5271` → IC=+0.200 (n=878)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6860.5271 (IC base=+0.194)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=1122)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.226 (n=502)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.0582` → IC=+0.271 (n=168)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0582 (IC base=+0.215)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2012` → IC=+0.247 (n=227)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2012 (IC base=+0.215)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1073` → IC=+0.243 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1073 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=506)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.215)

- **PATRÓN** `ibs_15` > `0.7176` → IC=+0.279 (n=501)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7176 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `0.1369` → IC=+0.247 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1369 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.108` → IC=+0.287 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.108 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.215 (n=648)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `16217.9862` → IC=+0.252 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16217.9862 (IC base=+0.215)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.513` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.513
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=648)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.5728` → IC=-0.161 (n=184)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5728
  - _Potencial_: sin este filtro IC_bueno=+0.232 (n=553)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.168 (n=185)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0034 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.0668` → IC=+0.150 (n=244)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.0668 (IC base=+0.133)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2368` → IC=+0.154 (n=186)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio_macro` |x|> 0.2368 (IC base=+0.133)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.128` → IC=+0.149 (n=212)

  - _Acción_: Kelly boost +0.75€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.128 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.148 (n=396)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.137 (n=579)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 17.0 (IC base=+0.133)

- **PATRÓN** `ibs_15` > `0.5728` → IC=+0.232 (n=553)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5728 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.1536` → IC=+0.139 (n=297)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.1536 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.901` → IC=+0.259 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.901 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `3507.1457` → IC=+0.139 (n=494)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3507.1457 (IC base=+0.133)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `20.397` → IC=-0.156 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 20.397
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=228)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.151 (n=190)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0055 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.205 (n=144)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.1865` → IC=+0.188 (n=379)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.1865 (IC base=+0.147)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0629` → IC=+0.160 (n=430)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio_macro` |x|> 0.0629 (IC base=+0.147)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3429` → IC=+0.174 (n=382)

  - _Acción_: Kelly boost +0.87€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3429 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.165 (n=308)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 11.0 (IC base=+0.147)

- **PATRÓN** `ibs_15` > `0.9286` → IC=+0.344 (n=145)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9286 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.6827` → IC=+0.160 (n=51)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.6827 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1905` → IC=+0.155 (n=392)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1905 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.477` → IC=+0.224 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.477 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=278)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.147)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.256` → IC=+0.167 (n=61)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 8.256 (IC base=+0.029)

- **PATRÓN** `libro_liquidez` > `3357.6986` → IC=+0.158 (n=71)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3357.6986 (IC base=+0.029)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.261 (n=558)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0127 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.0805` → IC=+0.218 (n=275)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0805 (IC base=+0.216)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0442` → IC=+0.219 (n=625)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0442 (IC base=+0.216)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0893` → IC=+0.270 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0893 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.231 (n=555)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.216)

- **PATRÓN** `ibs_15` > `0.5854` → IC=+0.295 (n=624)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5854 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `0.1976` → IC=+0.225 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1976 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.749` → IC=+0.250 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.749 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.478` → IC=+0.216 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.478 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `2970.9032` → IC=+0.305 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2970.9032 (IC base=+0.216)

- **PATRÓN** `ibs_15` < `0.1089` → IC=+0.160 (n=671)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.80€ cuando `ibs_15` < 0.1089 (IC base=+0.069)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.364 (n=359)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.359)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.379 (n=179)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0055 (IC base=+0.359)

- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.359 (n=359)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.359)

- **PATRÓN** `drift_15min` |x|≤ `0.4043` → IC=+0.363 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4043 (IC base=+0.359)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1501` → IC=+0.383 (n=358)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1501 (IC base=+0.359)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1371` → IC=+0.391 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1371 (IC base=+0.359)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.375 (n=543)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.359)

- **PATRÓN** `ibs_15` > `0.8305` → IC=+0.407 (n=480)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8305 (IC base=+0.359)

- **PATRÓN** `dist_vwap_pct` > `0.4158` → IC=+0.388 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4158 (IC base=+0.359)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.231` → IC=+0.372 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.231 (IC base=+0.359)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.365 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.359)

- **PATRÓN** `libro_liquidez` > `3489.2833` → IC=+0.368 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3489.2833 (IC base=+0.359)

- **PATRÓN** `ballena_activa_n` < `440.0` → IC=+0.378 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 440.0 (IC base=+0.359)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.360 (n=256)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.359)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.369 (n=97)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.359)

- **PATRÓN** `drift_60min` |x|≤ `0.0547` → IC=+0.359 (n=97)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0547 (IC base=+0.359)

- **PATRÓN** `drift_15min` |x|≤ `0.5086` → IC=+0.362 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5086 (IC base=+0.359)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1528` → IC=+0.382 (n=193)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1528 (IC base=+0.359)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1344` → IC=+0.395 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1344 (IC base=+0.359)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.378 (n=293)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.359)

- **PATRÓN** `ibs_15` > `0.8057` → IC=+0.387 (n=291)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8057 (IC base=+0.359)

- **PATRÓN** `dist_vwap_pct` > `0.3926` → IC=+0.397 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3926 (IC base=+0.359)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.481` → IC=+0.363 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.481 (IC base=+0.359)

- **PATRÓN** `sigma_ewma_delta_pct` < `25.57` → IC=+0.359 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 25.57 (IC base=+0.359)

- **PATRÓN** `libro_liquidez` > `15217.9578` → IC=+0.388 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15217.9578 (IC base=+0.359)

- **PATRÓN** `ballena_activa_n` < `499.0` → IC=+0.407 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 499.0 (IC base=+0.359)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.357 (n=110)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.358)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.377 (n=112)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.358)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.368 (n=165)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.358)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1309` → IC=+0.374 (n=165)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1309 (IC base=+0.358)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2995` → IC=+0.382 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2995 (IC base=+0.358)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.416 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.358)

- **PATRÓN** `ibs_15` > `0.7601` → IC=+0.404 (n=247)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7601 (IC base=+0.358)

- **PATRÓN** `dist_vwap_pct` > `0.4406` → IC=+0.365 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4406 (IC base=+0.358)

- **PATRÓN** `dist_vwap_pct` < `0.2769` → IC=+0.360 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2769 (IC base=+0.358)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.861` → IC=+0.387 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.861 (IC base=+0.358)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.694` → IC=+0.356 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.694 (IC base=+0.358)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.365 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.358)

- **PATRÓN** `libro_liquidez` > `4286.2041` → IC=+0.382 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4286.2041 (IC base=+0.358)

- **PATRÓN** `ballena_activa_n` < `145.0` → IC=+0.364 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 145.0 (IC base=+0.358)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0121` → IC=-0.222 (n=918)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0121
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=2757)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.208 (n=1387)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=2288)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1409` → IC=+0.186 (n=588)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.93€ cuando `delta_ratio_macro` |x|> 0.1409 (IC base=-0.069)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1378` → IC=+0.222 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1378 (IC base=-0.069)

- **PATRÓN** `ibs_15` > `0.6341` → IC=+0.277 (n=882)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6341 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` > `0.1047` → IC=+0.200 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1047 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` < `0.2612` → IC=+0.193 (n=744)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.2612 (IC base=-0.069)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1306` → IC=+0.263 (n=1969)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1306 (IC base=-0.012)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3241` → IC=+0.253 (n=2893)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3241 (IC base=-0.012)

- **PATRÓN** `ibs_15` < `0.3514` → IC=+0.282 (n=2955)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3514 (IC base=-0.012)

- **PATRÓN** `dist_vwap_pct` > `0.6504` → IC=+0.292 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6504 (IC base=-0.012)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.253 (n=2572)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=-0.012)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.212 (n=522)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=1568)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.229 (n=522)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=1568)

- **FILTRO** `sigma_ewma_delta_pct` > `23.695` → IC=-0.264 (n=299)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.695
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=1791)

- **FILTRO** `libro_liquidez` < `16325.7152` → IC=-0.197 (n=1379)

  - _Acción_: SKIP cuando `libro_liquidez` < 16325.7152
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=711)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.176 (n=208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0027 (IC base=+0.088)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1979` → IC=+0.303 (n=120)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1979 (IC base=+0.088)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1064` → IC=+0.305 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1064 (IC base=+0.088)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.121 (n=420)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 12.0 (IC base=+0.088)

- **PATRÓN** `ibs_15` > `0.7533` → IC=+0.331 (n=264)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7533 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.0996` → IC=+0.295 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0996 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` < `0.4912` → IC=+0.294 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4912 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.459` → IC=+0.127 (n=306)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` > 8.459 (IC base=+0.088)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0659` → IC=+0.236 (n=51)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0659 (IC base=-0.190)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1779` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1779 (IC base=-0.190)

- **PATRÓN** `ibs_15` < `0.618` → IC=+0.311 (n=51)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.618 (IC base=-0.190)

- **PATRÓN** `dist_vwap_pct` < `0.0474` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0474 (IC base=-0.190)

- **PATRÓN** `ballena_activa_n` < `295.0` → IC=+0.417 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 295.0 (IC base=-0.190)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.153 (n=568)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.150 (n=387)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0058 (IC base=+0.144)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.160 (n=392)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0038 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.1103` → IC=+0.175 (n=293)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.1103 (IC base=+0.144)

- **PATRÓN** `drift_15min` |x|≤ `0.4046` → IC=+0.144 (n=147)

  - _Acción_: Kelly boost +0.72€ cuando `drift_15min` |x|≤ 0.4046 (IC base=+0.144)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1408` → IC=+0.154 (n=293)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio_macro` |x|> 0.1408 (IC base=+0.144)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.190 (n=327)

  - _Acción_: Kelly boost +0.95€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.170 (n=310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 11.0 (IC base=+0.144)

- **PATRÓN** `ibs_15` > `0.6341` → IC=+0.248 (n=439)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6341 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.5931` → IC=+0.151 (n=81)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.5931 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.1025` → IC=+0.145 (n=319)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1025 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.508` → IC=+0.239 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.508 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=568)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `11031.3332` → IC=+0.178 (n=147)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 11031.3332 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.246 (n=1034)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.3518` → IC=+0.244 (n=911)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3518 (IC base=+0.241)

- **PATRÓN** `drift_15min` |x|≤ `0.7573` → IC=+0.254 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7573 (IC base=+0.241)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2118` → IC=+0.262 (n=469)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2118 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.241 (n=377)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.247 (n=402)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.241)

- **PATRÓN** `ibs_15` < `0.3647` → IC=+0.271 (n=1034)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3647 (IC base=+0.241)

- **PATRÓN** `dist_vwap_pct` > `0.7684` → IC=+0.297 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7684 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.404` → IC=+0.257 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.404 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.664` → IC=+0.245 (n=1081)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.664 (IC base=+0.241)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1711` → IC=-0.248 (n=288)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1711
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=561)

- **FILTRO** `drift_15min` |x|> `0.8825` → IC=-0.280 (n=212)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8825
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=637)

- **FILTRO** `sigma_ewma_delta_pct` > `10.456` → IC=-0.182 (n=146)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 10.456
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=703)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.256 (n=84)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=765)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.179)

- **PATRÓN** `ibs_15` > `0.9167` → IC=+0.340 (n=23)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9167 (IC base=-0.179)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.160 (n=51)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1292 (IC base=-0.179)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.227 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.179)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0787` → IC=+0.247 (n=413)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0787 (IC base=-0.038)

- **PATRÓN** `ibs_15` < `0.3462` → IC=+0.288 (n=461)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3462 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` < `0.172` → IC=+0.253 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.172 (IC base=-0.038)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0193` → IC=-0.249 (n=516)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0193
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=518)

- **FILTRO** `drift_60min` |x|> `0.1533` → IC=-0.204 (n=258)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1533
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=776)

- **FILTRO** `drift_15min` |x|> `0.5345` → IC=-0.226 (n=692)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5345
  - _Potencial_: sin este filtro IC_bueno=-0.148 (n=342)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.201)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.201)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1482` → IC=+0.276 (n=329)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1482 (IC base=-0.026)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.17` → IC=+0.293 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.17 (IC base=-0.026)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.296 (n=725)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` > `0.8057` → IC=+0.352 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8057 (IC base=-0.026)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `dist_vwap_pct` > `0.1918` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.1918 (IC base=+0.032)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `dist_vwap_pct` > `0.1918` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.1918 (IC base=+0.032)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.290 (n=785)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.053` → IC=+0.326 (n=297)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.053 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2395` → IC=+0.299 (n=297)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2395 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.224` → IC=+0.306 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.224 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.306 (n=933)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.8382` → IC=+0.320 (n=891)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8382 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.424` → IC=+0.328 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.424 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.701` → IC=+0.353 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.701 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `12909.8374` → IC=+0.305 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12909.8374 (IC base=+0.287)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.311 (n=162)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.0569` → IC=+0.329 (n=162)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0569 (IC base=+0.285)

- **PATRÓN** `drift_15min` |x|≤ `0.4185` → IC=+0.287 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4185 (IC base=+0.285)

- **PATRÓN** `delta_ratio_macro` |x|> `0.252` → IC=+0.311 (n=162)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.252 (IC base=+0.285)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2304` → IC=+0.291 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2304 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.309 (n=485)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.285)

- **PATRÓN** `ibs_15` > `0.8279` → IC=+0.313 (n=485)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8279 (IC base=+0.285)

- **PATRÓN** `dist_vwap_pct` > `0.2555` → IC=+0.334 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2555 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.837` → IC=+0.362 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.837 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.285 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `16334.7136` → IC=+0.329 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16334.7136 (IC base=+0.285)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.295 (n=271)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.288)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.294 (n=406)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.0515` → IC=+0.319 (n=136)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0515 (IC base=+0.288)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1506` → IC=+0.288 (n=272)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1506 (IC base=+0.288)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3023` → IC=+0.311 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3023 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.311 (n=364)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.288)

- **PATRÓN** `ibs_15` > `0.8537` → IC=+0.328 (n=406)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8537 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` > `0.4372` → IC=+0.313 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4372 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.99` → IC=+0.333 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.99 (IC base=+0.288)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0872` → IC=-0.256 (n=76)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0872
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=230)

- **FILTRO** `sigma_h` > `0.0042` → IC=-0.245 (n=104)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0042
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=202)

- **FILTRO** `drift_60min` |x|> `0.2527` → IC=-0.154 (n=76)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2527
  - _Potencial_: sin este filtro IC_bueno=-0.116 (n=230)

- **FILTRO** `ballena_activa_n` > `41.0` → IC=-0.196 (n=67)

  - _Acción_: SKIP cuando `ballena_activa_n` > 41.0
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=134)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0682` → IC=-0.145 (n=60)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0682
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=117)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.126` → IC=-0.174 (n=44)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.126
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=133)

- **FILTRO** `drift_15min` |x|> `0.3481` → IC=-0.278 (n=16)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3481
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=33)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1941` → IC=-0.231 (n=24)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1941
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=25)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1931` → IC=-0.167 (n=25)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1931
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=26)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.296` → IC=-0.370 (n=21)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.296
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `sigma_h` > `0.0046` → IC=-0.222 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0046
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=12)

### UPDOWN_OU_5M#XRP#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1195` → IC=-0.206 (n=15)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1195
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `sigma_h` > `0.006` → IC=-0.265 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

- **FILTRO** `drift_15min` |x|> `0.3593` → IC=-0.206 (n=15)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3593
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.3119` → IC=-0.184 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.3119
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `82.5234` → IC=+0.218 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 82.5234 (IC base=+0.203)

- **PATRÓN** `ratio` < `0.9763` → IC=+0.444 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9763 (IC base=+0.203)

- **PATRÓN** `T_h` > `145.7409` → IC=+0.388 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7409 (IC base=+0.337)

- **PATRÓN** `ratio` > `1.0572` → IC=+0.451 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0572 (IC base=+0.337)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `103.3918` → IC=+0.209 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 103.3918 (IC base=+0.182)

- **PATRÓN** `ratio` < `0.972` → IC=+0.415 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.972 (IC base=+0.182)

- **PATRÓN** `T_h` > `109.696` → IC=+0.300 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 109.696 (IC base=+0.291)

- **PATRÓN** `ratio` > `1.0228` → IC=+0.330 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0228 (IC base=+0.291)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `83.3501` → IC=+0.256 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.238)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.417 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.238)

- **PATRÓN** `T_h` > `111.9712` → IC=+0.347 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9712 (IC base=+0.324)

- **PATRÓN** `ratio` > `1.0127` → IC=+0.363 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0127 (IC base=+0.324)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1118` → IC=+0.454 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1118 (IC base=+0.401)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6027 sube el IC de +0.194 a +0.269 en UPDOWN_GBM#15min (n=2632). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7176 sube el IC de +0.215 a +0.279 en UPDOWN_GBM#BTC#15min (n=501). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5728 sube el IC de +0.133 a +0.232 en UPDOWN_GBM#ETH#15min (n=553). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.9286 sube el IC de +0.147 a +0.344 en UPDOWN_GBM#SOL#15min (n=145). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5854 sube el IC de +0.216 a +0.295 en UPDOWN_GBM#XRP#15min (n=624). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1089 sube el IC de +0.069 a +0.160 en UPDOWN_GBM#XRP#15min (n=671). Ya aplicado como kelly_boost=+0.80€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6341 sube el IC de -0.069 a +0.277 en UPDOWN_GBM_15M_TARDIO (n=882). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3514 sube el IC de -0.012 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=2955). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7533 sube el IC de +0.088 a +0.331 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=264). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.618 sube el IC de -0.190 a +0.311 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=51). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6341 sube el IC de +0.144 a +0.248 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=439). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3647 sube el IC de +0.241 a +0.271 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1034). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9167 sube el IC de -0.179 a +0.340 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3462 sube el IC de -0.038 a +0.288 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=461). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.201 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.026 a +0.296 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=725). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8382 sube el IC de +0.287 a +0.320 en UPDOWN_GBM_IBS_ALTO (n=891). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8279 sube el IC de +0.285 a +0.313 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=485). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8537 sube el IC de +0.288 a +0.328 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=406). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.8305 sube el IC de +0.359 a +0.407 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=480). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8057 sube el IC de +0.359 a +0.387 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=291). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7601 sube el IC de +0.358 a +0.404 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=247). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1621 | +0.088 | +175.20€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1621 | +0.088 | +175.20€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1250 | +0.093 | +148.17€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1250 | +0.093 | +148.17€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 268 | +0.067 | +11.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 268 | +0.067 | +11.32€ | 6 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 72 | +0.108 | +16.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 72 | +0.108 | +16.05€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 322 | +0.006 | +63.11€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 322 | +0.006 | +63.11€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 252 | +0.012 | +55.34€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 252 | +0.012 | +55.34€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 48 | +0.000 | +5.47€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 48 | +0.000 | +5.47€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 22 | -0.042 | +2.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 22 | -0.042 | +2.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 35356 | -0.084 | -4628.37€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1772 | -0.016 | -230.37€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 33584 | -0.087 | -4398.00€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4397 | -0.117 | -761.21€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4397 | -0.117 | -761.21€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1772 | -0.016 | -230.37€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1772 | -0.016 | -230.37€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4090 | -0.113 | -839.13€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4090 | -0.113 | -839.13€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 9163 | +0.008 | -851.16€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 9163 | +0.008 | -851.16€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 9026 | -0.109 | -683.64€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 9026 | -0.109 | -683.64€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 6908 | -0.152 | -1262.85€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 6908 | -0.152 | -1262.85€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 27605 | -0.019 | +3712.75€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 7139 | +0.002 | +1767.25€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 20466 | -0.027 | +1945.50€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 27605 | -0.019 | +3712.75€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 7139 | +0.002 | +1767.25€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 20466 | -0.027 | +1945.50€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 121587 | +0.113 | -5370.81€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 16702 | +0.182 | -518.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 521 | -0.041 | -62.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 96866 | +0.103 | -4520.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 7498 | +0.104 | -269.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 16082 | +0.103 | -1103.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 56 | -0.155 | +9.14€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 16011 | +0.105 | -1101.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 23963 | +0.128 | -425.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4914 | +0.195 | -153.14€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 16062 | +0.116 | -172.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2945 | +0.089 | -77.31€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 16129 | +0.095 | -1241.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 63 | -0.100 | -2.83€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 16051 | +0.096 | -1227.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 25831 | +0.124 | -447.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 6845 | +0.175 | -112.29€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 16248 | +0.106 | -272.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2726 | +0.101 | -54.29€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 23483 | +0.114 | -1281.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4767 | +0.190 | -269.89€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 424 | -0.005 | -8.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 16465 | +0.093 | -865.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1827 | +0.133 | -138.37€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#XRP | 16099 | +0.102 | -871.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 57 | -0.042 | +10.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 16029 | +0.102 | -881.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 19418 | +0.194 | -1220.43€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 19418 | +0.194 | -1220.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4492 | +0.174 | -419.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4492 | +0.174 | -419.34€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 2172 | +0.201 | -40.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 2172 | +0.201 | -40.04€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 4425 | +0.182 | -355.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 4425 | +0.182 | -355.01€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3885 | +0.241 | -141.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3885 | +0.241 | -141.07€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4365 | +0.189 | -278.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4365 | +0.189 | -278.73€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 894 | +0.425 | -34.21€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 894 | +0.425 | -34.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 351 | +0.432 | -8.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 351 | +0.432 | -8.06€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 343 | +0.427 | -10.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 343 | +0.427 | -10.89€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 188 | +0.405 | -12.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 188 | +0.405 | -12.81€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 67567 | +0.200 | -5008.15€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 67567 | +0.200 | -5008.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 11619 | +0.184 | -1222.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 11619 | +0.184 | -1222.08€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 10886 | +0.224 | -384.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 10886 | +0.224 | -384.54€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 11598 | +0.177 | -1286.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 11598 | +0.177 | -1286.06€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 10947 | +0.221 | -405.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 10947 | +0.221 | -405.75€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 11196 | +0.202 | -749.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 11196 | +0.202 | -749.53€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 11321 | +0.194 | -960.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 11321 | +0.194 | -960.18€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 25771 | +0.118 | +242.22€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 25771 | +0.118 | +242.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 12801 | +0.121 | +192.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 12801 | +0.121 | +192.10€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 12970 | +0.114 | +50.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 12970 | +0.114 | +50.12€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1801 | +0.288 | -25.19€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1801 | +0.288 | -25.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 814 | +0.279 | -18.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 814 | +0.279 | -18.68€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 869 | +0.286 | -11.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 869 | +0.286 | -11.16€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 118 | +0.350 | +4.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 118 | +0.350 | +4.65€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 817 | +0.440 | +1.97€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 817 | +0.440 | +1.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 395 | +0.440 | -0.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 395 | +0.440 | -0.40€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 376 | +0.442 | +1.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 376 | +0.442 | +1.81€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1398 | +0.067 | -69.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 516 | +0.056 | -42.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 882 | +0.073 | -27.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 68 | +0.100 | +1.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 68 | +0.100 | +1.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1089 | +0.074 | -34.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 207 | +0.074 | -7.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 882 | +0.073 | -27.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 241 | +0.027 | -36.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 241 | +0.027 | -36.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 49751 | +0.099 | -1279.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 4039 | +0.092 | +58.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 45712 | +0.100 | -1338.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 27551 | +0.104 | -296.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 4039 | +0.092 | +58.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 23512 | +0.106 | -355.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 9935 | +0.109 | -25.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 9935 | +0.109 | -25.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 12265 | +0.080 | -957.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 12265 | +0.080 | -957.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 871 | +0.203 | -101.16€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 871 | +0.203 | -101.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 871 | +0.203 | -101.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 871 | +0.203 | -101.16€ | 2 | 4 |
| ✅ GBM_LATE_15M | 34665 | +0.090 | +17337.30€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 34665 | +0.090 | +17337.30€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 5833 | +0.205 | +4538.21€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 5833 | +0.205 | +4538.21€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 5153 | +0.178 | +3737.02€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 5153 | +0.178 | +3737.02€ | 0 | 24 |
| ✅ GBM_LATE_15M#DOGE | 6158 | +0.202 | +4697.49€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 6158 | +0.202 | +4697.49€ | 0 | 19 |
| ✅ GBM_LATE_15M#ETH | 4887 | +0.036 | +1234.82€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4887 | +0.036 | +1234.82€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 4956 | -0.029 | +1078.81€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 4956 | -0.029 | +1078.81€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 7678 | -0.036 | +2050.96€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 7678 | -0.036 | +2050.96€ | 3 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 37605 | +0.087 | +20050.53€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 37605 | +0.087 | +20050.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 7307 | +0.011 | +3718.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 7307 | +0.011 | +3718.62€ | 3 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 7804 | +0.013 | +1665.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 7804 | +0.013 | +1665.71€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 5292 | +0.270 | +5494.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 5292 | +0.270 | +5494.37€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 6392 | +0.013 | +1438.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 6392 | +0.013 | +1438.07€ | 1 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 6132 | +0.037 | +2457.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 6132 | +0.037 | +2457.04€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4678 | +0.291 | +5276.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4678 | +0.291 | +5276.72€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 27692 | +0.177 | +21807.86€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 27692 | +0.177 | +21807.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 4192 | +0.218 | +3529.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 4192 | +0.218 | +3529.18€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 4383 | +0.151 | +3206.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 4383 | +0.151 | +3206.95€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 4392 | +0.218 | +3681.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 4392 | +0.218 | +3681.80€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 4660 | +0.138 | +3448.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 4660 | +0.138 | +3448.90€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 5180 | +0.127 | +3849.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 5180 | +0.127 | +3849.72€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4885 | +0.216 | +4091.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4885 | +0.216 | +4091.32€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 7491 | +0.141 | +3659.45€ | 0 | 23 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 7491 | +0.141 | +3659.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 341 | +0.141 | +188.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 341 | +0.141 | +188.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2320 | +0.149 | +1317.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2320 | +0.149 | +1317.30€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 375 | +0.142 | +175.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 375 | +0.142 | +175.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2306 | +0.155 | +1151.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2306 | +0.155 | +1151.59€ | 0 | 22 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1612 | +0.108 | +586.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1612 | +0.108 | +586.89€ | 1 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 537 | +0.135 | +240.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 537 | +0.135 | +240.44€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 34889 | +0.182 | +27179.41€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 34889 | +0.182 | +27179.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 5554 | +0.232 | +4959.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 5554 | +0.232 | +4959.98€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 5398 | +0.148 | +3559.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 5398 | +0.148 | +3559.89€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 5844 | +0.229 | +5137.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 5844 | +0.229 | +5137.06€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 5664 | +0.138 | +3947.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 5664 | +0.138 | +3947.74€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 6178 | +0.127 | +4313.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 6178 | +0.127 | +4313.63€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 6251 | +0.219 | +5261.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 6251 | +0.219 | +5261.10€ | 0 | 20 |
| ✅ GBM_LATE_5M | 9614 | +0.184 | +6779.73€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 9614 | +0.184 | +6779.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 898 | +0.233 | +801.22€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 898 | +0.233 | +801.22€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2125 | +0.170 | +1538.88€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2125 | +0.170 | +1538.88€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 992 | +0.176 | +650.38€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 992 | +0.176 | +650.38€ | 0 | 17 |
| ✅ GBM_LATE_5M#ETH | 2986 | +0.187 | +2046.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2986 | +0.187 | +2046.40€ | 0 | 26 |
| ✅ GBM_LATE_5M#SOL | 1250 | +0.178 | +871.81€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1250 | +0.178 | +871.81€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1363 | +0.175 | +871.02€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1363 | +0.175 | +871.02€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2627 | +0.069 | +935.11€ | 0 | 10 |
| ✅ GBM_LATE_60M#60min | 2627 | +0.069 | +935.11€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 988 | +0.087 | +360.73€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 988 | +0.087 | +360.73€ | 0 | 10 |
| ✅ GBM_LATE_60M#ETH | 822 | +0.068 | +349.14€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 822 | +0.068 | +349.14€ | 0 | 9 |
| ✅ GBM_LATE_60M#SOL | 817 | +0.047 | +225.24€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 817 | +0.047 | +225.24€ | 2 | 12 |
| 🚫 GBM_LATE_60M_FADE | 490 | -0.240 | -15.90€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 490 | -0.240 | -15.90€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 185 | -0.233 | -11.64€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 185 | -0.233 | -11.64€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 171 | -0.217 | +1.92€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 171 | -0.217 | +1.92€ | 5 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 134 | -0.272 | -6.17€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 134 | -0.272 | -6.17€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1174 | +0.087 | +306.23€ | 0 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1174 | +0.087 | +306.23€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 448 | +0.080 | +94.07€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 448 | +0.080 | +94.07€ | 1 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 410 | +0.063 | +69.86€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 410 | +0.063 | +69.86€ | 1 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 316 | +0.126 | +142.30€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 316 | +0.126 | +142.30€ | 2 | 14 |
| ✅ LATE_WINDOW_5MIN | 138 | +0.250 | +117.05€ | 0 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 138 | +0.250 | +117.05€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 138 | +0.250 | +117.05€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 138 | +0.250 | +117.05€ | 0 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 2858 | +0.101 | +734.08€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2858 | +0.101 | +734.08€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2858 | +0.101 | +734.08€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2858 | +0.101 | +734.08€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 439 | -0.069 | -32.39€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 439 | -0.069 | -32.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 123 | -0.028 | -1.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 123 | -0.028 | -1.03€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 68 | -0.086 | -7.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 68 | -0.086 | -7.96€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 167 | -0.033 | -6.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 167 | -0.033 | -6.54€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M | 3089 | +0.019 | +72.24€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3089 | +0.019 | +72.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 152 | +0.026 | -1.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 152 | +0.026 | -1.43€ | 1 | 1 |
| ✅ LIQUIDACIONES_5M#BTC | 520 | +0.025 | +34.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 520 | +0.025 | +34.01€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1121 | +0.028 | +29.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1121 | +0.028 | +29.00€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 707 | +0.012 | +1.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 707 | +0.012 | +1.07€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 386 | +0.013 | +14.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 386 | +0.013 | +14.69€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1472 | -0.039 | -22.79€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1472 | -0.039 | -22.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 420 | -0.033 | -10.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 420 | -0.033 | -10.52€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 488 | -0.016 | +4.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 488 | -0.016 | +4.13€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 564 | -0.064 | -16.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 564 | -0.064 | -16.39€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 5533 | -0.021 | +77.69€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 2598 | -0.026 | -1.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 2935 | -0.016 | +79.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 162 | +0.000 | +9.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 77 | +0.044 | +12.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 85 | -0.040 | -2.60€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 1379 | -0.013 | +24.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 650 | -0.020 | -4.20€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 729 | -0.006 | +28.96€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 615 | -0.024 | +10.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 306 | -0.039 | -5.85€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 309 | -0.008 | +16.55€ | 2 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 1140 | -0.040 | -39.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 520 | -0.058 | -41.29€ | 3 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 620 | -0.026 | +2.29€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1080 | -0.011 | +41.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 515 | -0.011 | +24.19€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 565 | -0.011 | +16.89€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1157 | -0.021 | +30.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 530 | -0.021 | +13.30€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 627 | -0.021 | +17.05€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 14662 | -0.012 | -218.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14662 | -0.012 | -218.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 40215 | -0.002 | +1940.54€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 40215 | -0.002 | +1940.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 7185 | +0.024 | +942.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 7185 | +0.024 | +942.90€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 5954 | -0.032 | -92.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 5954 | -0.032 | -92.95€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 7282 | +0.022 | +718.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 7282 | +0.022 | +718.80€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 5774 | -0.049 | -144.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 5774 | -0.049 | -144.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 6786 | -0.007 | +203.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 6786 | -0.007 | +203.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 7234 | +0.014 | +312.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 7234 | +0.014 | +312.60€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6247 | -0.059 | -142.25€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6247 | -0.059 | -142.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1220 | +0.001 | -13.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1220 | +0.001 | -13.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1545 | -0.075 | -29.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1545 | -0.075 | -29.69€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 50 | -0.077 | -3.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 50 | -0.077 | -3.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 732 | -0.123 | -33.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 732 | -0.123 | -33.18€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1844 | -0.078 | -37.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1844 | -0.078 | -37.01€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 856 | -0.015 | -25.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 856 | -0.015 | -25.00€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3353 | +0.004 | -3.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3353 | +0.004 | -3.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 192 | +0.015 | +1.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 192 | +0.015 | +1.02€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 137 | -0.004 | -2.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 137 | -0.004 | -2.36€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1320 | +0.005 | +5.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1320 | +0.005 | +5.15€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1388 | +0.007 | +0.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1388 | +0.007 | +0.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 100836 | -0.073 | +1741.22€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 100836 | -0.073 | +1741.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 17368 | -0.074 | +896.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 17368 | -0.074 | +896.57€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 15282 | -0.098 | -825.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 15282 | -0.098 | -825.19€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 17633 | -0.065 | +1060.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 17633 | -0.065 | +1060.38€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 14817 | -0.095 | -444.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 14817 | -0.095 | -444.31€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 18228 | -0.052 | +377.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 18228 | -0.052 | +377.07€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 17508 | -0.064 | +676.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 17508 | -0.064 | +676.71€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8124 | -0.032 | -156.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8124 | -0.032 | -156.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1930 | -0.043 | -19.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1930 | -0.043 | -19.28€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2246 | -0.026 | -32.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2246 | -0.026 | -32.47€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1129 | -0.050 | -24.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1129 | -0.050 | -24.29€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 815 | -0.025 | -28.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 815 | -0.025 | -28.11€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1430 | +0.121 | +562.50€ | 0 | 6 |
| ✅ ORDER_FLOW_5M#5min | 1294 | +0.127 | +549.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 302 | +0.145 | +160.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 302 | +0.145 | +160.43€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 250 | +0.107 | +73.58€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 250 | +0.107 | +73.58€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 263 | +0.126 | +116.34€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 263 | +0.126 | +116.34€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 230 | +0.151 | +125.13€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 230 | +0.151 | +125.13€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 249 | +0.102 | +74.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 249 | +0.102 | +74.43€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1034 | -0.016 | -16.97€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1034 | -0.016 | -16.97€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 203 | -0.007 | +4.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 203 | -0.007 | +4.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 161 | -0.003 | +4.74€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 161 | -0.003 | +4.74€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 273 | -0.031 | -14.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 273 | -0.031 | -14.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 226 | +0.009 | +2.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 226 | +0.009 | +2.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 171 | -0.049 | -14.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 171 | -0.049 | -14.81€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 783 | -0.078 | -61.26€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 357 | -0.132 | -77.72€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 277 | -0.170 | -70.58€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 80 | +0.000 | -7.14€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 277 | -0.038 | +3.02€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 198 | -0.035 | +2.25€ | 2 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 79 | -0.043 | +0.77€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 149 | -0.023 | +13.44€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 120 | -0.033 | +8.03€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 29 | +0.016 | +5.41€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 595 | -0.098 | -60.30€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 188 | -0.016 | -0.96€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 939 | -0.200 | -42.91€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 389 | -0.196 | -30.12€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 334 | -0.199 | -30.91€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 55 | -0.167 | +0.79€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 317 | -0.212 | -27.02€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 273 | -0.220 | -32.60€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 44 | -0.152 | +5.58€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 233 | -0.189 | +14.23€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 214 | -0.185 | +11.09€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 19 | -0.204 | +3.14€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 821 | -0.203 | -52.42€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 118 | -0.175 | +9.51€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 396 | +0.397 | +364.69€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#BTC | 46 | +0.104 | +40.61€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 46 | +0.104 | +40.61€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 101 | +0.374 | +91.49€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 101 | +0.374 | +91.49€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 249 | +0.456 | +232.60€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 249 | +0.456 | +232.60€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 396 | +0.397 | +364.69€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 636 | +0.030 | +23.71€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 636 | +0.030 | +23.71€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 295 | +0.022 | +2.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 295 | +0.022 | +2.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 49 | +0.010 | -2.27€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 49 | +0.010 | -2.27€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 66 | -0.015 | -2.23€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 66 | -0.015 | -2.23€ | 2 | 0 |
| ✅ STREAK_FADE_15M#XRP | 226 | +0.057 | +25.91€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 226 | +0.057 | +25.91€ | 2 | 5 |
| ✅ STREAK_FADE_5M | 3237 | -0.021 | -126.97€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3237 | -0.021 | -126.97€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1014 | -0.024 | -37.66€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1014 | -0.024 | -37.66€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 585 | -0.026 | -25.65€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 585 | -0.026 | -25.65€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1482 | -0.015 | -49.25€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1482 | -0.015 | -49.25€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 92 | -0.053 | -9.32€ | 2 | 0 |
| ✅ STREAK_FADE_60M#60min | 92 | -0.053 | -9.32€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 39 | -0.085 | -3.98€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 39 | -0.085 | -3.98€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 53 | -0.027 | -5.34€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 53 | -0.027 | -5.34€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 9921 | +0.019 | +105.97€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 9921 | +0.019 | +105.97€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2641 | +0.021 | +28.82€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2641 | +0.021 | +28.82€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2413 | +0.026 | +48.35€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2413 | +0.026 | +48.35€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2863 | +0.009 | -1.83€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2863 | +0.009 | -1.83€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2004 | +0.021 | +30.63€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2004 | +0.021 | +30.63€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 8964 | +0.013 | -45.77€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 8964 | +0.013 | -45.77€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3538 | +0.018 | -5.41€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3538 | +0.018 | -5.41€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3519 | +0.011 | -25.79€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3519 | +0.011 | -25.79€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1907 | +0.008 | -14.57€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1907 | +0.008 | -14.57€ | 1 | 0 |
| ✅ UPDOWN_GBM | 62061 | +0.049 | +5089.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 15459 | +0.084 | +3396.47€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2066 | +0.005 | +7.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 40778 | +0.042 | +1626.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 3543 | +0.007 | +61.23€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6439 | +0.084 | +921.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1364 | +0.156 | +590.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 71 | -0.021 | -2.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5004 | +0.066 | +333.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 12049 | +0.051 | +989.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1949 | +0.090 | +464.67€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 532 | +0.011 | +5.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 7887 | +0.055 | +473.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1602 | +0.005 | +43.75€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 79 | -0.080 | +1.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 7553 | +0.063 | +731.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1346 | +0.148 | +524.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 68 | +0.000 | -2.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6139 | +0.045 | +209.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 13511 | +0.038 | +760.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3641 | +0.056 | +459.88€ | 1 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 525 | +0.007 | +8.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 8066 | +0.039 | +287.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1208 | +0.005 | +1.47€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 71 | -0.103 | +3.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 13696 | +0.027 | +574.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 3645 | +0.037 | +340.80€ | 0 | 11 |
| ✅ UPDOWN_GBM#SOL#240min | 514 | +0.000 | +0.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 8741 | +0.027 | +222.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 733 | +0.016 | +16.01€ | 0 | 2 |
| ✅ UPDOWN_GBM#SOL#daily | 63 | -0.146 | -5.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 8811 | +0.057 | +1113.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3514 | +0.104 | +1015.96€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 356 | +0.006 | -1.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 4941 | +0.028 | +99.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 213 | -0.109 | -0.28€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 716 | +0.359 | +248.51€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 716 | +0.359 | +248.51€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 387 | +0.359 | +127.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 387 | +0.359 | +127.29€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 329 | +0.358 | +121.22€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 329 | +0.358 | +121.22€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 16930 | -0.025 | +4095.97€ | 2 | 10 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 16930 | -0.025 | +4095.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1464 | -0.052 | +481.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1464 | -0.052 | +481.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2918 | -0.111 | +142.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2918 | -0.111 | +142.29€ | 4 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 834 | +0.218 | +685.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 834 | +0.218 | +685.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1963 | +0.212 | +1237.09€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1963 | +0.212 | +1237.09€ | 1 | 23 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 4850 | -0.063 | +642.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 4850 | -0.063 | +642.41€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 4901 | -0.063 | +907.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 4901 | -0.063 | +907.96€ | 3 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 187 | +0.034 | +6.83€ | 0 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 187 | +0.034 | +6.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 187 | +0.034 | +6.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 187 | +0.034 | +6.83€ | 0 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1187 | +0.287 | +971.27€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1187 | +0.287 | +971.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 646 | +0.285 | +508.86€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 646 | +0.285 | +508.86€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 541 | +0.288 | +462.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 541 | +0.288 | +462.41€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 768 | -0.114 | -84.12€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 768 | -0.114 | -84.12€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 226 | -0.088 | -18.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 226 | -0.088 | -18.31€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 80 | -0.159 | -7.73€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 80 | -0.159 | -7.73€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 83 | -0.194 | -8.02€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 83 | -0.194 | -8.02€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 34 | -0.194 | -7.31€ | 4 | 0 |
| ✅ WEEKLY_PRICE | 3058 | +0.306 | +1505.31€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1094 | +0.259 | +157.21€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1169 | +0.299 | +524.07€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 795 | +0.378 | +824.02€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.016 n=769 — no justifica filtro, seguir monitorizando
  - _Datos_: n=769 IC=+0.016 PNL=+37.43€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 649 celda(s) pasan gate riguroso completo de 2517 evaluadas (n>=40) y 3506 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.037 < 0.08 — monitorear
  - _Datos_: n=3641 IC=+0.037 PNL=+336.66€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1169/15 IC=+0.299 PNL=+524.07€ | BTC: n=1094/15 IC=+0.259 PNL=+157.21€ | SOL: n=795/15 IC=+0.378 PNL=+824.02€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.138 n=623/60 | contraria IC=+0.201 n=636 | gap=-0.062 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=397, boost estimado=+0.012. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1207/40 IC=+0.004 PNL=+0.97€ | BTC#60min: n=1600/40 IC=+0.005 PNL=+43.73€ | SOL#60min: n=732/40 IC=+0.015 PNL=+15.51€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.048 n=459333 | tras_1loss IC=+0.090 n=351569 | tras_2loss IC=+0.059 n=143928/40 | gap=-0.011 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.215 > 0.08 con n=539 PNL=+437.71€
  - _Datos_: n=539 IC=+0.215 PNL=+437.71€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.207 > 0.08 con n=599 PNL=+433.93€
  - _Datos_: n=599 IC=+0.207 PNL=+433.93€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.173 > 0.08 con n=53 PNL=+27.40€
  - _Datos_: n=53 IC=+0.173 PNL=+27.40€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.334 > 0.1 con n=2497 PNL=+1384.89€
  - _Datos_: n=2497 IC=+0.334 PNL=+1384.89€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=499 IC=+0.073 PNL=+54.48€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=499 IC=+0.073 PNL=+54.48€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=69 IC=+0.190 PNL=+47.57€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=69 IC=+0.190 PNL=+47.57€

**⏳ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: 30
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 4/15 ops en el filtro definido (IC actual=+0.067 PNL=+7.14€)
  - _Datos_: n=4 IC=+0.067 PNL=+7.14€

**⏳ H-CUSTOM-OF-07H-BTCSOL** — ORDER_FLOW H=07h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 07h está en el blacklist. Con BTC+SOL solo, el historial muestra 7/12 (58%) IC=+0.043. El blacklist puede estar basado en pares negativos que ya están excluidos.
  - _Umbral_: 20
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 07h del blacklist ORDER_FLOW
  - _Estado_: 1/20 ops en el filtro definido (IC actual=+0.008 PNL=+1.96€)
  - _Datos_: n=1 IC=+0.008 PNL=+1.96€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: 07h sigue en ORDER_FLOW_BLACKLIST_HOURS -- mientras siga ahí, nunca genera fila para volver a evaluarse (26-Ago, triage candidatas estancadas)

**〰️ H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: n=2364 IC=+0.005 PNL=-1.41€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2364 IC=+0.005 PNL=-1.41€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1175 IC=+0.011 PNL=+61.61€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1175 IC=+0.011 PNL=+61.61€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=769 IC=+0.016 PNL=+37.43€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=769 IC=+0.016 PNL=+37.43€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.194 > 0.1 con n=3505 PNL=+2380.25€
  - _Datos_: n=3505 IC=+0.194 PNL=+2380.25€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1947 IC=+0.091 PNL=+465.69€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1947 IC=+0.091 PNL=+465.69€

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
  - _Estado_: n=805 IC=+0.034 PNL=+70.88€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=805 IC=+0.034 PNL=+70.88€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=87 IC=+0.051 PNL=+4.69€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=87 IC=+0.051 PNL=+4.69€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.250 n=138) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=138 IC=+0.250 PNL=+117.05€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.128 > 0.02 con n=823 PNL=+347.36€
  - _Datos_: n=823 IC=+0.128 PNL=+347.36€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=191 IC=-0.070 PNL=+27.59€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=191 IC=-0.070 PNL=+27.59€

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
  - _Estado_: n=23236 IC=+0.070 PNL=+3250.50€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=23236 IC=+0.070 PNL=+3250.50€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.130 < -0.1 con n=368 PNL=+50.78€
  - _Datos_: n=368 IC=-0.130 PNL=+50.78€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2682 IC=+0.069 PNL=+337.30€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2682 IC=+0.069 PNL=+337.30€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=116 IC=-0.093 PNL=+5.87€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=116 IC=-0.093 PNL=+5.87€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.118 > 0.1 con n=634 PNL=+167.13€
  - _Datos_: n=634 IC=+0.118 PNL=+167.13€

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
  - _Estado_: n=25347 IC=-0.137 PNL=+1729.96€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=25347 IC=-0.137 PNL=+1729.96€

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
  - _Estado_: n=2572 IC=+0.138 PNL=+1496.49€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2572 IC=+0.138 PNL=+1496.49€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=6415 IC=+0.044 PNL=+435.81€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6415 IC=+0.044 PNL=+435.81€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.088 > 0.08 con n=2829 PNL=+1481.44€
  - _Datos_: n=2829 IC=+0.088 PNL=+1481.44€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.226 < -0.1 con n=2595 PNL=-201.28€
  - _Datos_: n=2595 IC=-0.226 PNL=-201.28€

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
  - _Estado_: n=55 IC=-0.009 PNL=+6.29€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=55 IC=-0.009 PNL=+6.29€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.100 n=1457) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1457 IC=+0.100 PNL=+326.69€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.411 n=513) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=513 IC=+0.411 PNL=+730.63€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=11611 IC=+0.183 PNL=-1224.93€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=11611 IC=+0.183 PNL=-1224.93€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.213 > 0.1 con n=186 PNL=+117.73€
  - _Datos_: n=186 IC=+0.213 PNL=+117.73€
