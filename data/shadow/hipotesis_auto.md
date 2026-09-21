# Hipótesis automáticas — 2026-09-21 17:26 UTC
_Generado por shadow_postmortem.py sobre 545076 resoluciones (PNL=+60825.31€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.505` → IC=-0.152 (n=202)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.247 (n=489)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=452)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.247 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.131)

- **PATRÓN** `n_total_lado` > `76.0` → IC=+0.208 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 76.0 (IC base=+0.131)

- **PATRÓN** `banda_hit_calibrado` > `0.8046` → IC=+0.250 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8046 (IC base=+0.131)

- **PATRÓN** `banda_z` > `9.932` → IC=+0.226 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.932 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.146 (n=362)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 11.0 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=555)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `2914.8041` → IC=+0.138 (n=346)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2914.8041 (IC base=+0.131)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.134 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.253 (n=387)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=325)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.253 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.139)

- **PATRÓN** `n_total_lado` > `72.0` → IC=+0.214 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 72.0 (IC base=+0.139)

- **PATRÓN** `banda_hit_calibrado` > `0.8036` → IC=+0.258 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8036 (IC base=+0.139)

- **PATRÓN** `banda_z` > `10.993` → IC=+0.221 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.993 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.158 (n=296)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 11.0 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=469)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.142 (n=118)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 96.0 (IC base=+0.043)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.515` → IC=-0.204 (n=42)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.256 (n=88)

- **FILTRO** `py_entrada` > `0.845` → IC=-0.393 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.845
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=87)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.190 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=86)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=97)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.256 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.106)

- **PATRÓN** `banda_hit_calibrado` > `0.6274` → IC=+0.222 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6274 (IC base=+0.106)

- **PATRÓN** `banda_z` > `6.043` → IC=+0.172 (n=65)

  - _Acción_: Kelly boost +0.86€ cuando `banda_z` > 6.043 (IC base=+0.106)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.160 (n=104)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.02 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `1185.8848` → IC=+0.142 (n=65)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 1185.8848 (IC base=+0.106)

### BALLENAS_CONFIRMADAS_15M#XRP#15min
- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `n_ballena_banda` > 26.0 (IC base=+0.154)

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
- **FILTRO** `restante_s_al_confirmar` < `145.51` → IC=-0.234 (n=6576)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 145.51
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=19728)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `140.57` → IC=-0.237 (n=891)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 140.57
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=2673)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` < `493.55` → IC=-0.153 (n=350)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 493.55
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=1051)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `133.45` → IC=-0.278 (n=795)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.45
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=2387)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `161.55` → IC=-0.229 (n=1550)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 161.55
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=4650)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `122.42` → IC=-0.364 (n=1302)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.42
  - _Potencial_: sin este filtro IC_bueno=-0.121 (n=3908)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.47` → IC=-0.235 (n=342)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=389)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.171 (n=223)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=454)

### CANDIDATA9_BOT_CONSENSO#BTC#5min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.259 (n=164)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=169)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.214 (n=75)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=227)

### CANDIDATA9_BOT_CONSENSO#ETH#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.329 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=169)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.162 (n=72)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=141)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.173 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=163)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.200 (n=13178)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3301)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `9509.4092` → IC=+0.192 (n=1428)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 9509.4092 (IC base=+0.101)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.142 (n=10372)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.138 (n=12720)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.129)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.233 (n=10123)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.175 (n=5363)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `7601.2069` → IC=+0.171 (n=2015)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 7601.2069 (IC base=+0.129)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=1605)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.208 (n=1579)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.350 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=1982)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `15752.6972` → IC=+0.237 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15752.6972 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.204 (n=1419)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.203 (n=1568)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.261 (n=1424)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.199 (n=2003)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `15455.9709` → IC=+0.209 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15455.9709 (IC base=+0.198)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.62` → IC=+0.181 (n=305)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.62 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `4624.034` → IC=+0.144 (n=234)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 4624.034 (IC base=+0.105)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.145 (n=328)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 7.0 (IC base=+0.111)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.148 (n=790)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.44 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.125 (n=556)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `5871.1399` → IC=+0.161 (n=219)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 5871.1399 (IC base=+0.111)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=2639)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.144 (n=2262)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.143)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.332 (n=888)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.252 (n=497)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.236)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.358 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.243 (n=1398)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `3741.733` → IC=+0.236 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3741.733 (IC base=+0.236)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.149 (n=431)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.142 (n=560)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 15.0 (IC base=+0.136)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.227 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=511)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `1300.2394` → IC=+0.148 (n=617)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 1300.2394 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.072)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.225 (n=664)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.430 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.172 (n=1036)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 7.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.27` → IC=+0.313 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.27 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.178 (n=706)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.168)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.174 (n=299)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 7.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.165 (n=210)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 13.0 (IC base=+0.166)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.361 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.174 (n=185)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.02 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `1261.7454` → IC=+0.161 (n=222)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 1261.7454 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.158 (n=290)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.115)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.216 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.115)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `9.0` → IC=-0.298 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=106)

- **FILTRO** `py_entrada` > `0.8` → IC=-0.333 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=129)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=10619)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.202 (n=10206)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.224 (n=3638)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.339 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `8491.3442` → IC=+0.342 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8491.3442 (IC base=+0.198)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.176 (n=2484)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.183 (n=1801)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.71 (IC base=+0.168)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **FILTRO** `py_entrada` < `0.775` → IC=-0.284 (n=49)

  - _Acción_: SKIP cuando `py_entrada` < 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=63)

- **FILTRO** `libro_liquidez` < `9614.35` → IC=-0.328 (n=56)

  - _Acción_: SKIP cuando `libro_liquidez` < 9614.35
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.270 (n=316)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.259)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.262 (n=692)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.359 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.259)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=2416)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.188 (n=2446)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.189 (n=1114)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.73 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.247 (n=2274)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.239)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.320 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.321 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.239)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=2473)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.195 (n=2390)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 17.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.195 (n=1802)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.71 (IC base=+0.192)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.438 (n=464)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.428)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.430 (n=440)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.428)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.470 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.428)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.427 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.428)

- **PATRÓN** `libro_liquidez` > `2060.1801` → IC=+0.436 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2060.1801 (IC base=+0.428)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.433 (n=192)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.431)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.433 (n=191)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.431)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.452 (n=164)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.470 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.435)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.436 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.435)

- **PATRÓN** `libro_liquidez` > `3322.2122` → IC=+0.444 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3322.2122 (IC base=+0.435)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.406 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.401)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.404 (n=102)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.401)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.417 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.401)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.403 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.401)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=22)

- **FILTRO** `libro_liquidez` < `6836.9618` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `libro_liquidez` < 6836.9618
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.201 (n=31459)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.241 (n=11731)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.176 (n=6404)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.181 (n=5434)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.189 (n=5854)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=5634)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.227 (n=5641)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.275 (n=2029)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.177 (n=5736)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=5782)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.174)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.233 (n=2810)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=2137)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.265 (n=1981)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.211 (n=5209)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.254 (n=2144)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.205)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.195 (n=5265)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 8.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.194 (n=5261)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.252 (n=2058)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.192)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.199 (n=4842)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` < `4.12` → IC=+0.129 (n=4419)

  - _Acción_: Kelly boost +0.65€ cuando `restante_min` < 4.12 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.143 (n=4653)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=5817)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `3.15` → IC=+0.143 (n=4402)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 3.15 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.201 (n=2442)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.123)

- **PATRÓN** `restante_min` < `4.07` → IC=+0.131 (n=2191)

  - _Acción_: Kelly boost +0.65€ cuando `restante_min` < 4.07 (IC base=+0.123)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.140 (n=2300)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.94 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.142 (n=2516)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 6.0 (IC base=+0.123)

- **PATRÓN** `lag_apertura_s` < `3.5` → IC=+0.144 (n=2183)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 3.5 (IC base=+0.123)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=2400)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.115)

- **PATRÓN** `restante_min` < `4.49` → IC=+0.126 (n=2935)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.49 (IC base=+0.115)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=2360)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.115)

- **PATRÓN** `lag_apertura_s` < `2.34` → IC=+0.143 (n=2217)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 2.34 (IC base=+0.115)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.320 (n=738)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.385 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `1569.8406` → IC=+0.297 (n=1044)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1569.8406 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.285 (n=491)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.277)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.340 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `4199.8248` → IC=+0.295 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4199.8248 (IC base=+0.277)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.336 (n=351)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.297)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.385 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.297)

- **PATRÓN** `libro_liquidez` > `1466.4356` → IC=+0.315 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1466.4356 (IC base=+0.297)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.347 (n=83)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.340)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.363 (n=71)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.340)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.378 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.340)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.375 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.340)

- **PATRÓN** `libro_liquidez` > `720.8183` → IC=+0.375 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 720.8183 (IC base=+0.340)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.447 (n=485)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.438)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.445 (n=414)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.442 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.445 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.440 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.438)

- **PATRÓN** `libro_liquidez` > `1834.428` → IC=+0.440 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1834.428 (IC base=+0.438)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.446 (n=222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.438)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.443 (n=191)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.444 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.448 (n=229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.452 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.440)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.441 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.440)

- **PATRÓN** `libro_liquidez` > `2031.364` → IC=+0.460 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2031.364 (IC base=+0.440)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` < `12.0` → IC=+0.370 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.381)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.72` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=31)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.303 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.257)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.315 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.274 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1376.3842` → IC=+0.285 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1376.3842 (IC base=+0.257)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **FILTRO** `py_entrada` > `0.72` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=31)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.303 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.257)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.315 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.274 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1376.3842` → IC=+0.285 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1376.3842 (IC base=+0.257)

### GBM_LATE_15M
- **PATRÓN** `drift_60min` |x|≤ `0.3592` → IC=+0.124 (n=6488)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.3592 (IC base=+0.104)

- **PATRÓN** `ibs_20min` > `0.982` → IC=+0.241 (n=2459)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.982 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` < `0.6151` → IC=+0.246 (n=2054)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6151 (IC base=+0.104)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.939` → IC=+0.177 (n=2845)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 5.939 (IC base=+0.104)

- **PATRÓN** `volumen_regimen` < `1.2188` → IC=+0.242 (n=1971)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2188 (IC base=+0.104)

- **PATRÓN** `volumen_regimen` > `1.0538` → IC=+0.250 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0538 (IC base=+0.104)

- **PATRÓN** `volumen_pendiente_norm` > `0.3067` → IC=+0.213 (n=736)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3067 (IC base=+0.104)

- **PATRÓN** `volumen_spike_ratio` > `1.9133` → IC=+0.207 (n=3341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9133 (IC base=+0.104)

- **PATRÓN** `ibs_20min` < `0.5714` → IC=+0.131 (n=8892)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5714 (IC base=+0.062)

- **PATRÓN** `dist_vwap_pct` > `0.5801` → IC=+0.198 (n=646)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.5801 (IC base=+0.062)

- **PATRÓN** `dist_vwap_pct` < `0.1436` → IC=+0.173 (n=2747)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1436 (IC base=+0.062)

- **PATRÓN** `volumen_regimen` < `0.7016` → IC=+0.178 (n=1338)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.7016 (IC base=+0.062)

- **PATRÓN** `volumen_regimen` > `0.8706` → IC=+0.175 (n=2026)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.8706 (IC base=+0.062)

- **PATRÓN** `volumen_pendiente_norm` > `0.1678` → IC=+0.225 (n=1462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1678 (IC base=+0.062)

- **PATRÓN** `volumen_spike_ratio` > `1.5811` → IC=+0.202 (n=4525)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5811 (IC base=+0.062)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.212 (n=4847)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.062)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.177 (n=558)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.005 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.175 (n=558)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0082 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.3446` → IC=+0.165 (n=1674)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.3446 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.163 (n=809)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.175 (n=1121)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 11.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.270 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.097` → IC=+0.277 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.097 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.208 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `1.4352` → IC=+0.166 (n=1559)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.4352 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.253 (n=1094)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.0886` → IC=+0.290 (n=408)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0886 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.248 (n=836)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.062` → IC=+0.300 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.062 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.416` → IC=+0.251 (n=1281)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.416 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` < `0.0912` → IC=+0.233 (n=1040)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0912 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2749` → IC=+0.270 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2749 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.6252` → IC=+0.255 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6252 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `1774.62` → IC=+0.249 (n=815)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1774.62 (IC base=+0.236)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.235 (n=565)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.0846` → IC=+0.256 (n=425)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0846 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.229 (n=1336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.216 (n=1304)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `0.9089` → IC=+0.257 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9089 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `0.1895` → IC=+0.217 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1895 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` < `0.7288` → IC=+0.217 (n=1406)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7288 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.863` → IC=+0.247 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.863 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` < `1.2558` → IC=+0.219 (n=1273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2558 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` > `0.8736` → IC=+0.220 (n=849)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8736 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.0745` → IC=+0.229 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0745 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `1.403` → IC=+0.223 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.403 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.3807` → IC=+0.219 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3807 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `15860.9645` → IC=+0.227 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15860.9645 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.175 (n=444)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0026 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0761` → IC=+0.157 (n=441)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0761 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=520)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.6839` → IC=+0.168 (n=1321)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.6839 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1261` → IC=+0.154 (n=1177)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1261 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.539` → IC=+0.159 (n=423)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 6.539 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.195` → IC=+0.137 (n=1196)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 4.195 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.2089` → IC=+0.148 (n=1321)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.2089 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.1569` → IC=+0.179 (n=353)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1569 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4386` → IC=+0.147 (n=1211)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4386 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.7701` → IC=+0.145 (n=807)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.7701 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `411.0` → IC=+0.145 (n=1127)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 411.0 (IC base=+0.136)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.205 (n=1084)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0079 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.188 (n=1627)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 6.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=1463)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.265 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.096` → IC=+0.248 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.096 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` < `0.2131` → IC=+0.189 (n=1614)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.2131 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.3666` → IC=+0.193 (n=213)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.3666 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.9149` → IC=+0.207 (n=698)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9149 (IC base=+0.187)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.196 (n=1104)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.02 (IC base=+0.187)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.223 (n=1382)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0109 (IC base=+0.217)

- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.219 (n=1235)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0066 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.5459` → IC=+0.218 (n=1382)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5459 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.257 (n=520)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.0643` → IC=+0.244 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0643 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.55` → IC=+0.241 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.55 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3595` → IC=+0.277 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3595 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.9116` → IC=+0.230 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9116 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.228 (n=880)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `1858.5555` → IC=+0.233 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1858.5555 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.224 (n=817)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.149 (n=92)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=2052)

- **PATRÓN** `ibs_20min` > `0.94` → IC=+0.202 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.94 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` > `0.3551` → IC=+0.322 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3551 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` < `0.7574` → IC=+0.326 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7574 (IC base=+0.020)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.725` → IC=+0.150 (n=652)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 4.725 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` < `0.6017` → IC=+0.332 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6017 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` > `1.1961` → IC=+0.330 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1961 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` < `0.1771` → IC=+0.320 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1771 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.3014` → IC=+0.333 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3014 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` < `1.4012` → IC=+0.337 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4012 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` > `2.2012` → IC=+0.318 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2012 (IC base=+0.020)

- **PATRÓN** `ballena_activa_n` < `165.0` → IC=+0.328 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 165.0 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` > `0.3253` → IC=+0.176 (n=242)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.3253 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` < `0.8548` → IC=+0.155 (n=496)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8548 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` > `1.1607` → IC=+0.145 (n=249)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.1607 (IC base=+0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.2244` → IC=+0.231 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2244 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` > `1.5138` → IC=+0.178 (n=616)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.5138 (IC base=+0.011)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.155 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=293)

- **FILTRO** `ibs_20min` < `0.2667` → IC=-0.197 (n=87)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2667
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=262)

- **FILTRO** `ibs_20min` > `0.2632` → IC=-0.128 (n=2028)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2632
  - _Potencial_: sin este filtro IC_bueno=+0.126 (n=1002)

- **FILTRO** `sigma_ewma_delta_pct` > `8.666` → IC=-0.207 (n=329)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.666
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2701)

- **PATRÓN** `ibs_20min` > `0.7727` → IC=+0.227 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7727 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` > `1.6376` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.6376 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` < `0.5528` → IC=+0.272 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5528 (IC base=+0.053)

- **PATRÓN** `volumen_regimen` < `0.6528` → IC=+0.271 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6528 (IC base=+0.053)

- **PATRÓN** `volumen_regimen` > `1.1487` → IC=+0.338 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1487 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` < `0.0735` → IC=+0.316 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0735 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` < `2.2264` → IC=+0.296 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2264 (IC base=+0.053)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.296 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.053)

- **PATRÓN** `ibs_20min` < `0.2632` → IC=+0.126 (n=1002)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.2632 (IC base=-0.044)

- **PATRÓN** `dist_vwap_pct` > `0.6475` → IC=+0.276 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6475 (IC base=-0.044)

- **PATRÓN** `volumen_regimen` < `1.0999` → IC=+0.232 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0999 (IC base=-0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.1582` → IC=+0.253 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1582 (IC base=-0.044)

- **PATRÓN** `volumen_spike_ratio` < `2.456` → IC=+0.263 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.456 (IC base=-0.044)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6317` → IC=-0.187 (n=513)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6317
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=1542)

- **FILTRO** `ibs_20min` < `0.6977` → IC=-0.158 (n=1355)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6977
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=700)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.196 (n=396)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=1659)

- **FILTRO** `ibs_20min` > `0.7761` → IC=-0.201 (n=765)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7761
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=2297)

- **PATRÓN** `dist_vwap_pct` > `0.7356` → IC=+0.297 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7356 (IC base=-0.074)

- **PATRÓN** `dist_vwap_pct` < `0.2607` → IC=+0.316 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2607 (IC base=-0.074)

- **PATRÓN** `volumen_regimen` > `0.6166` → IC=+0.298 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6166 (IC base=-0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.0744` → IC=+0.297 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0744 (IC base=-0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.5359` → IC=+0.294 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5359 (IC base=-0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.1503` → IC=+0.292 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1503 (IC base=-0.074)

- **PATRÓN** `dist_vwap_pct` > `1.0236` → IC=+0.302 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0236 (IC base=-0.025)

- **PATRÓN** `volumen_regimen` < `0.742` → IC=+0.257 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.742 (IC base=-0.025)

- **PATRÓN** `volumen_regimen` > `1.0811` → IC=+0.297 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0811 (IC base=-0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.1058` → IC=+0.284 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1058 (IC base=-0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.2199` → IC=+0.257 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2199 (IC base=-0.025)

- **PATRÓN** `volumen_spike_ratio` > `1.5829` → IC=+0.250 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5829 (IC base=-0.025)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.195 (n=3065)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0096 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.187 (n=8215)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4706 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `1.0351` → IC=+0.296 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0351 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.562` → IC=+0.155 (n=4357)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.562 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `0.6856` → IC=+0.244 (n=2895)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6856 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.2979` → IC=+0.263 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2979 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `1.472` → IC=+0.239 (n=1760)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.472 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `2.702` → IC=+0.240 (n=1759)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.702 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.267 (n=4785)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 98.0 (IC base=+0.096)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.144 (n=3101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0089 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.5524` → IC=+0.149 (n=8168)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.5524 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.9674` → IC=+0.237 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9674 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` < `0.2394` → IC=+0.236 (n=2507)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2394 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` < `0.7156` → IC=+0.237 (n=1173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7156 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` > `1.2035` → IC=+0.244 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2035 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` > `0.2475` → IC=+0.307 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2475 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` < `1.6193` → IC=+0.255 (n=1530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6193 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` > `2.3458` → IC=+0.261 (n=1576)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3458 (IC base=+0.070)

- **PATRÓN** `ballena_activa_n` < `82.0` → IC=+0.263 (n=3348)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 82.0 (IC base=+0.070)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `2.676` → IC=-0.152 (n=667)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.676
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=1500)

- **PATRÓN** `ibs_20min` > `0.8947` → IC=+0.263 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8947 (IC base=+0.046)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.29` → IC=+0.164 (n=871)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 3.29 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.2224` → IC=+0.272 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2224 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` < `1.4395` → IC=+0.172 (n=269)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.4395 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` > `2.1445` → IC=+0.190 (n=366)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.1445 (IC base=+0.046)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.176 (n=353)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 15.0 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` < `0.1845` → IC=+0.475 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1845 (IC base=-0.022)

- **PATRÓN** `volumen_spike_ratio` < `1.4415` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4415 (IC base=-0.022)

- **PATRÓN** `volumen_spike_ratio` > `2.2378` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2378 (IC base=-0.022)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8156` → IC=-0.149 (n=668)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8156
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=2007)

- **PATRÓN** `ibs_20min` > `0.8635` → IC=+0.160 (n=618)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.8635 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.4783` → IC=+0.172 (n=245)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.4783 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` > `0.6687` → IC=+0.158 (n=753)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.6687 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.2765` → IC=+0.206 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2765 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `1.4247` → IC=+0.197 (n=275)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4247 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `249.0` → IC=+0.193 (n=359)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 249.0 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.6152` → IC=+0.205 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6152 (IC base=-0.001)

- **PATRÓN** `dist_vwap_pct` < `0.1524` → IC=+0.213 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1524 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` > `0.6059` → IC=+0.211 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6059 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2733` → IC=+0.297 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2733 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.4599` → IC=+0.221 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4599 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1868` → IC=+0.221 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1868 (IC base=-0.001)

- **PATRÓN** `ballena_activa_n` < `483.0` → IC=+0.212 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 483.0 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.287 (n=975)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0077 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.246 (n=1465)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.256 (n=547)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=773)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.641` → IC=+0.282 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.641 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` < `0.1386` → IC=+0.259 (n=1290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1386 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `2.9317` → IC=+0.263 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9317 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.257 (n=978)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `1925.7032` → IC=+0.254 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1925.7032 (IC base=+0.245)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.326 (n=522)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.327 (n=392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.285)

- **PATRÓN** `ibs_20min` < `0.2248` → IC=+0.291 (n=1013)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2248 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.816` → IC=+0.304 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.816 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` > `0.3435` → IC=+0.315 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3435 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` < `1.6226` → IC=+0.291 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6226 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` > `2.1984` → IC=+0.286 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1984 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.297 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `1910.1836` → IC=+0.316 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1910.1836 (IC base=+0.285)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.285 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 30.0 (IC base=+0.285)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.2756` → IC=-0.194 (n=442)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2756
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=1330)

- **FILTRO** `ibs_20min` > `0.7832` → IC=-0.179 (n=547)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7832
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=1649)

- **PATRÓN** `ibs_20min` > `0.806` → IC=+0.154 (n=603)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.806 (IC base=+0.008)

- **PATRÓN** `dist_vwap_pct` > `0.4586` → IC=+0.230 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4586 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` < `0.9869` → IC=+0.234 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9869 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` > `0.6488` → IC=+0.212 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6488 (IC base=+0.008)

- **PATRÓN** `volumen_pendiente_norm` > `0.1655` → IC=+0.271 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1655 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` < `2.1113` → IC=+0.244 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1113 (IC base=+0.008)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.260 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 102.0 (IC base=+0.008)

- **PATRÓN** `dist_vwap_pct` > `0.1525` → IC=+0.193 (n=187)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1525 (IC base=-0.010)

- **PATRÓN** `dist_vwap_pct` < `0.636` → IC=+0.180 (n=407)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.636 (IC base=-0.010)

- **PATRÓN** `volumen_regimen` < `1.1649` → IC=+0.193 (n=359)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 1.1649 (IC base=-0.010)

- **PATRÓN** `volumen_regimen` > `0.7204` → IC=+0.184 (n=321)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 0.7204 (IC base=-0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.265 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=-0.010)

- **PATRÓN** `volumen_spike_ratio` < `1.8338` → IC=+0.238 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8338 (IC base=-0.010)

- **PATRÓN** `volumen_spike_ratio` > `2.1499` → IC=+0.253 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1499 (IC base=-0.010)

- **PATRÓN** `ballena_activa_n` < `120.0` → IC=+0.236 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 120.0 (IC base=-0.010)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7124` → IC=-0.203 (n=975)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7124
  - _Potencial_: sin este filtro IC_bueno=+0.273 (n=976)

- **FILTRO** `ibs_20min` > `0.6923` → IC=-0.234 (n=505)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6923
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=1546)

- **FILTRO** `sigma_ewma_delta_pct` > `4.705` → IC=-0.180 (n=457)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.705
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=1594)

- **PATRÓN** `ibs_20min` > `0.7124` → IC=+0.273 (n=976)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7124 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` > `0.8456` → IC=+0.344 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8456 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.568` → IC=+0.156 (n=306)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 9.568 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` < `0.8657` → IC=+0.299 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8657 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` > `0.6388` → IC=+0.286 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6388 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` < `0.1045` → IC=+0.290 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1045 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.2738` → IC=+0.294 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2738 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `1.443` → IC=+0.315 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.443 (IC base=+0.035)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.313 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.035)

- **PATRÓN** `ibs_20min` < `0.1` → IC=+0.208 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1 (IC base=+0.012)

- **PATRÓN** `dist_vwap_pct` < `0.2117` → IC=+0.225 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2117 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` < `0.7067` → IC=+0.268 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7067 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.210 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.2213` → IC=+0.208 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2213 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` < `2.5113` → IC=+0.221 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5113 (IC base=+0.012)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.235 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=+0.012)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0162` → IC=+0.318 (n=798)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0162 (IC base=+0.275)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.292 (n=561)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.275)

- **PATRÓN** `ibs_20min` > `0.63` → IC=+0.310 (n=1197)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.63 (IC base=+0.275)

- **PATRÓN** `dist_vwap_pct` > `0.2807` → IC=+0.320 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2807 (IC base=+0.275)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.487` → IC=+0.300 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.487 (IC base=+0.275)

- **PATRÓN** `volumen_regimen` > `0.8624` → IC=+0.301 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8624 (IC base=+0.275)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.314 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.275)

- **PATRÓN** `volumen_spike_ratio` > `2.1716` → IC=+0.288 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1716 (IC base=+0.275)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.280 (n=1262)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.275)

- **PATRÓN** `libro_liquidez` > `2607.8081` → IC=+0.286 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2607.8081 (IC base=+0.275)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.323 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.275)

- **PATRÓN** `sigma_h` > `0.0149` → IC=+0.299 (n=876)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0149 (IC base=+0.271)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.279 (n=596)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.271)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.272 (n=655)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.271)

- **PATRÓN** `ibs_20min` < `0.3962` → IC=+0.304 (n=1315)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3962 (IC base=+0.271)

- **PATRÓN** `dist_vwap_pct` > `0.2867` → IC=+0.285 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2867 (IC base=+0.271)

- **PATRÓN** `dist_vwap_pct` < `0.9159` → IC=+0.271 (n=1484)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9159 (IC base=+0.271)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.484` → IC=+0.287 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.484 (IC base=+0.271)

- **PATRÓN** `volumen_regimen` > `1.2419` → IC=+0.314 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2419 (IC base=+0.271)

- **PATRÓN** `volumen_pendiente_norm` > `0.2396` → IC=+0.339 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2396 (IC base=+0.271)

- **PATRÓN** `volumen_spike_ratio` < `2.5218` → IC=+0.268 (n=1148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5218 (IC base=+0.271)

- **PATRÓN** `volumen_spike_ratio` > `2.1688` → IC=+0.273 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1688 (IC base=+0.271)

- **PATRÓN** `libro_liquidez` > `2588.4404` → IC=+0.277 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2588.4404 (IC base=+0.271)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.170 (n=2427)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0049 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.011` → IC=+0.203 (n=2418)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.0896` → IC=+0.185 (n=2421)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.0896 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=7581)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `0.582` → IC=+0.217 (n=7254)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.582 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.1712` → IC=+0.195 (n=3186)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1712 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.243` → IC=+0.259 (n=1489)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.243 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `1.2184` → IC=+0.161 (n=4799)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2184 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` > `0.6273` → IC=+0.160 (n=4798)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6273 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.2463` → IC=+0.194 (n=1460)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2463 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.5645` → IC=+0.170 (n=3052)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5645 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.639` → IC=+0.177 (n=2312)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.639 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `2385.005` → IC=+0.169 (n=4836)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2385.005 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `118.0` → IC=+0.181 (n=6171)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 118.0 (IC base=+0.168)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.183 (n=4581)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0065 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.0795` → IC=+0.204 (n=2290)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0795 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.208 (n=2299)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` < `0.4787` → IC=+0.227 (n=6869)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4787 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` < `0.2262` → IC=+0.159 (n=4997)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.2262 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.246` → IC=+0.198 (n=1165)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 10.246 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `1.1795` → IC=+0.153 (n=5008)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1795 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.2911` → IC=+0.224 (n=990)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2911 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.5722` → IC=+0.167 (n=2729)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.5722 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.2739` → IC=+0.173 (n=2811)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.2739 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `120.0` → IC=+0.172 (n=5837)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 120.0 (IC base=+0.168)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.215 (n=416)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.189 (n=564)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0076 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.3418` → IC=+0.204 (n=1245)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3418 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.198 (n=831)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 11.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.097` → IC=+0.310 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.097 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2294` → IC=+0.239 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2294 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `1.4343` → IC=+0.182 (n=1145)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.4343 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.241 (n=771)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.241)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.256 (n=782)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.1827` → IC=+0.293 (n=583)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1827 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.249 (n=791)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.248 (n=427)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.1111` → IC=+0.279 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1111 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.095` → IC=+0.256 (n=947)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.095 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` < `0.0936` → IC=+0.241 (n=719)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0936 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.2757` → IC=+0.259 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2757 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.4163` → IC=+0.262 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4163 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.631` → IC=+0.239 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.631 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.241 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1781.7648` → IC=+0.255 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1781.7648 (IC base=+0.241)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.245 (n=359)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.0752` → IC=+0.209 (n=359)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0752 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=1135)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.4088` → IC=+0.230 (n=1077)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4088 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.2011` → IC=+0.216 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2011 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.523` → IC=+0.236 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.523 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `1.268` → IC=+0.169 (n=1077)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.268 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` > `1.0767` → IC=+0.169 (n=488)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.0767 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.2332` → IC=+0.200 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2332 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `1.414` → IC=+0.203 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.414 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `15796.8084` → IC=+0.175 (n=488)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 15796.8084 (IC base=+0.165)

- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.199 (n=393)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0025 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.2906` → IC=+0.155 (n=1172)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.2906 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.178 (n=395)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 18.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.5583` → IC=+0.183 (n=1173)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.5583 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.1307` → IC=+0.160 (n=1169)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1307 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.856` → IC=+0.211 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.856 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `1.2129` → IC=+0.155 (n=1172)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.2129 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.1572` → IC=+0.158 (n=358)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.1572 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.4443` → IC=+0.143 (n=1062)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4443 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `221.0` → IC=+0.151 (n=328)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 221.0 (IC base=+0.135)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.232 (n=551)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.2176` → IC=+0.216 (n=809)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2176 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.224 (n=407)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.293 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.816` → IC=+0.282 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.816 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` < `0.211` → IC=+0.197 (n=1171)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.211 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.1346` → IC=+0.195 (n=474)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1346 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `1.6522` → IC=+0.196 (n=383)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.6522 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.9184` → IC=+0.211 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9184 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.211 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `1929.4792` → IC=+0.203 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1929.4792 (IC base=+0.199)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.237 (n=989)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0108 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.0935` → IC=+0.254 (n=331)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0935 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.279 (n=351)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` < `0.2453` → IC=+0.259 (n=870)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2453 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.635` → IC=+0.277 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.635 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.3592` → IC=+0.275 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3592 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` < `1.6284` → IC=+0.226 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6284 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.2488` → IC=+0.230 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2488 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `1861.22` → IC=+0.225 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1861.22 (IC base=+0.224)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.228 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.224)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.174 (n=1017)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0067 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.4324` → IC=+0.162 (n=1156)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.4324 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=1216)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.3926` → IC=+0.199 (n=1155)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3926 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.1565` → IC=+0.182 (n=778)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1565 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.979` → IC=+0.244 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.979 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.0512` → IC=+0.154 (n=1017)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.0512 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `0.6326` → IC=+0.151 (n=1155)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6326 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.2917` → IC=+0.222 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2917 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.5382` → IC=+0.151 (n=497)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.5382 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `2.5308` → IC=+0.175 (n=377)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.5308 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `6960.2205` → IC=+0.185 (n=770)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 6960.2205 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `167.0` → IC=+0.150 (n=1091)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 167.0 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.157 (n=1207)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0073 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.3828` → IC=+0.143 (n=1207)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3828 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.187 (n=404)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 18.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.6177` → IC=+0.170 (n=1207)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.6177 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` < `0.1565` → IC=+0.143 (n=1165)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.1565 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.91` → IC=+0.178 (n=426)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 6.91 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `0.8526` → IC=+0.142 (n=805)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.8526 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2884` → IC=+0.204 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2884 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.7982` → IC=+0.128 (n=727)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.7982 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.4834` → IC=+0.141 (n=363)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.4834 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `9988.1936` → IC=+0.162 (n=548)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 9988.1936 (IC base=+0.123)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.163 (n=598)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0101 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.135 (n=1351)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` > `0.5217` → IC=+0.201 (n=1314)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5217 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` > `0.8302` → IC=+0.213 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8302 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.609` → IC=+0.253 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.609 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `1.2251` → IC=+0.127 (n=1316)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.2251 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `1.4429` → IC=+0.142 (n=423)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4429 (IC base=+0.116)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.124 (n=1369)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `2893.8059` → IC=+0.196 (n=596)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2893.8059 (IC base=+0.116)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.136 (n=998)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 50.0 (IC base=+0.116)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.150 (n=583)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.006 (IC base=+0.112)

- **PATRÓN** `drift_60min` |x|≤ `0.1029` → IC=+0.144 (n=442)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.1029 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.132 (n=1346)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.112)

- **PATRÓN** `ibs_20min` < `0.5652` → IC=+0.209 (n=1325)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5652 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` > `0.9725` → IC=+0.144 (n=178)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.9725 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` < `0.1953` → IC=+0.137 (n=1206)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1953 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.478` → IC=+0.151 (n=276)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 7.478 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` < `1.1902` → IC=+0.122 (n=1325)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.1902 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` > `0.2749` → IC=+0.169 (n=161)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2749 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` < `1.4585` → IC=+0.136 (n=394)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.4585 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` > `2.1681` → IC=+0.124 (n=535)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 2.1681 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `3069.2676` → IC=+0.160 (n=442)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3069.2676 (IC base=+0.112)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0184` → IC=+0.211 (n=835)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0184 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=1303)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.200 (n=571)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` > `0.7358` → IC=+0.257 (n=1119)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7358 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `1.2538` → IC=+0.229 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2538 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.444` → IC=+0.244 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.444 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `1.2094` → IC=+0.202 (n=1253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2094 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` > `0.6187` → IC=+0.210 (n=1253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6187 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2349` → IC=+0.271 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2349 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `2.1646` → IC=+0.211 (n=1063)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1646 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `1.8081` → IC=+0.206 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8081 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.202 (n=1315)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `2598.6802` → IC=+0.203 (n=835)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2598.6802 (IC base=+0.199)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.237 (n=435)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.205)

- **PATRÓN** `sigma_h` > `0.0222` → IC=+0.219 (n=592)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0222 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.0889` → IC=+0.219 (n=436)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0889 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.223 (n=643)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.214 (n=597)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` < `0.4434` → IC=+0.247 (n=1305)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4434 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `1.1415` → IC=+0.228 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1415 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.388` → IC=+0.242 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.388 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `0.6303` → IC=+0.218 (n=1305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6303 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.2842` → IC=+0.284 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2842 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `2.6078` → IC=+0.194 (n=1165)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.6078 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `1.4586` → IC=+0.200 (n=1164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4586 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `2565.3121` → IC=+0.211 (n=870)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2565.3121 (IC base=+0.205)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.160 (n=568)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0039 (IC base=+0.146)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.172 (n=565)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.009 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.1355` → IC=+0.154 (n=744)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1355 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.186 (n=851)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 15.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.3984` → IC=+0.181 (n=1690)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.3984 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.3813` → IC=+0.182 (n=510)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.3813 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.709` → IC=+0.175 (n=787)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.709 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.8735` → IC=+0.162 (n=978)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8735 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` > `1.21` → IC=+0.156 (n=489)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.21 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1638` → IC=+0.179 (n=469)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1638 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.4378` → IC=+0.159 (n=543)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4378 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.5522` → IC=+0.170 (n=541)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.5522 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.149 (n=1901)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.02 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `3260.328` → IC=+0.150 (n=1127)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3260.328 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `167.0` → IC=+0.165 (n=1471)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 167.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.127 (n=1181)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0057 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.121 (n=1183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 11.0 (IC base=+0.099)

- **PATRÓN** `ibs_20min` < `0.0561` → IC=+0.197 (n=591)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.0561 (IC base=+0.099)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3431` → IC=+0.127 (n=419)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.3431 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.143 (n=379)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 9.0 (IC base=+0.104)

- **PATRÓN** `ibs_20min` > `0.2422` → IC=+0.146 (n=419)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.2422 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` > `0.2886` → IC=+0.149 (n=146)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.2886 (IC base=+0.104)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.291` → IC=+0.130 (n=190)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 3.291 (IC base=+0.104)

- **PATRÓN** `volumen_regimen` < `0.6134` → IC=+0.141 (n=140)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.6134 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `14609.6219` → IC=+0.137 (n=279)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 14609.6219 (IC base=+0.104)

- **PATRÓN** `ballena_activa_n` < `160.0` → IC=+0.142 (n=132)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 160.0 (IC base=+0.104)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.204 (n=187)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.3378` → IC=+0.140 (n=557)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.3378 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.144 (n=501)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 7.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.3447` → IC=+0.198 (n=372)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.3447 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.2854` → IC=+0.148 (n=591)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2854 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.406` → IC=+0.151 (n=216)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 4.406 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` > `0.7202` → IC=+0.142 (n=498)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.7202 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.205 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `2.1115` → IC=+0.149 (n=482)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.1115 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `1.415` → IC=+0.136 (n=547)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.415 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `337.0` → IC=+0.138 (n=462)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 337.0 (IC base=+0.126)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.269 (n=219)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.203)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.208 (n=166)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.0949` → IC=+0.226 (n=166)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0949 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.248 (n=248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `0.7017` → IC=+0.269 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7017 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.149` → IC=+0.232 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.149 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.067` → IC=+0.238 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.067 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` < `0.8422` → IC=+0.216 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8422 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `1.1584` → IC=+0.220 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1584 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2555` → IC=+0.340 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2555 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `1.3839` → IC=+0.241 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3839 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `2.391` → IC=+0.264 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.391 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `ibs_20min` < `0.0811` → IC=+0.165 (n=153)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.0811 (IC base=+0.071)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.4189` → IC=-0.127 (n=164)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4189
  - _Potencial_: sin este filtro IC_bueno=+0.158 (n=320)

- **FILTRO** `dist_vwap_pct` > `0.3414` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3414
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=450)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.159 (n=171)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0088 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.152 (n=352)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 8.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.9048` → IC=+0.223 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9048 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.6259` → IC=+0.203 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6259 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.234` → IC=+0.198 (n=177)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 5.234 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `1.0699` → IC=+0.133 (n=330)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.0699 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` > `0.7264` → IC=+0.138 (n=335)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.7264 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.289` → IC=+0.191 (n=53)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.289 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` > `2.2097` → IC=+0.159 (n=162)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.2097 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `3065.6596` → IC=+0.209 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3065.6596 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.156 (n=120)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 22.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.4189` → IC=+0.158 (n=320)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.4189 (IC base=+0.062)

- **PATRÓN** `volumen_spike_ratio` < `1.604` → IC=+0.165 (n=150)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.604 (IC base=+0.062)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0232` → IC=+0.161 (n=178)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0232 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.182 (n=177)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0068 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.2324` → IC=+0.178 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2324 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.167 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 16.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.216 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.4` → IC=+0.189 (n=178)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.2468` → IC=+0.153 (n=93)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.2468 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `1.0795` → IC=+0.160 (n=201)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 1.0795 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.705` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 7.705 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.317` → IC=+0.175 (n=152)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` < 3.317 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `0.6778` → IC=+0.171 (n=159)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 0.6778 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.2547` → IC=+0.174 (n=173)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` < 0.2547 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.222 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.176 (n=180)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.02 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `2727.8122` → IC=+0.163 (n=81)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2727.8122 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.022` → IC=+0.181 (n=92)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.022 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.178` → IC=+0.170 (n=89)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.178 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `1.1744` → IC=+0.295 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1744 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.576` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.576 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.8853` → IC=+0.128 (n=135)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.8853 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6515` → IC=+0.136 (n=201)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6515 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1187` → IC=+0.130 (n=179)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1187 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.6848` → IC=+0.135 (n=83)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.6848 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.8185` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.8185 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.146 (n=162)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 17.0 (IC base=+0.122)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.204 (n=3070)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.177 (n=9631)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.4722` → IC=+0.216 (n=9211)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4722 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.9321` → IC=+0.203 (n=1306)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9321 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.605` → IC=+0.227 (n=4487)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.605 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `0.8827` → IC=+0.165 (n=4106)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8827 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.2903` → IC=+0.199 (n=1267)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2903 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `2.6183` → IC=+0.188 (n=2942)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6183 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `2329.7709` → IC=+0.170 (n=6140)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2329.7709 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.194 (n=6915)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 89.0 (IC base=+0.167)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.191 (n=5557)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0069 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.4847` → IC=+0.183 (n=8335)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.4847 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=3157)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.5663` → IC=+0.238 (n=8335)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5663 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` < `0.2408` → IC=+0.161 (n=5168)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2408 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.924` → IC=+0.200 (n=1171)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.924 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.71` → IC=+0.182 (n=8088)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.71 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.7055` → IC=+0.158 (n=2539)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.7055 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2882` → IC=+0.244 (n=1087)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2882 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `1.8701` → IC=+0.188 (n=5061)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.8701 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.190 (n=4855)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 49.0 (IC base=+0.181)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.208 (n=525)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.189)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.221 (n=525)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.3486` → IC=+0.189 (n=1570)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3486 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.194 (n=755)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 15.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.202 (n=1059)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.319 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.977` → IC=+0.314 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.977 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.2272` → IC=+0.246 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2272 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `2.5691` → IC=+0.210 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5691 (IC base=+0.189)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.265 (n=1068)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.1272` → IC=+0.292 (n=527)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1272 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.269 (n=1083)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.259)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.260 (n=1093)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.35` → IC=+0.292 (n=1051)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.35 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.458` → IC=+0.268 (n=1258)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.458 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.2233` → IC=+0.297 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2233 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `1.8671` → IC=+0.279 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8671 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.260 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1774.62` → IC=+0.274 (n=796)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1774.62 (IC base=+0.259)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.198 (n=495)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0028 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.0841` → IC=+0.168 (n=492)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0841 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=1543)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.3123` → IC=+0.203 (n=1476)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3123 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.1248` → IC=+0.184 (n=847)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1248 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.755` → IC=+0.169 (n=339)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.755 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.242` → IC=+0.154 (n=1321)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.242 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.6273` → IC=+0.180 (n=492)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6273 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.2688` → IC=+0.196 (n=212)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2688 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.1158` → IC=+0.161 (n=1251)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1158 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.7608` → IC=+0.154 (n=947)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.7608 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `13725.8693` → IC=+0.153 (n=984)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 13725.8693 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `481.0` → IC=+0.157 (n=1355)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 481.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.162 (n=1273)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0057 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.3218` → IC=+0.159 (n=1273)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.3218 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.178 (n=426)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 18.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.6466` → IC=+0.192 (n=1273)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.6466 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.6888` → IC=+0.157 (n=214)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.6888 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.1289` → IC=+0.164 (n=1151)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1289 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.174` → IC=+0.159 (n=616)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.174 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `1.1954` → IC=+0.161 (n=1273)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1954 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1509` → IC=+0.199 (n=343)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1509 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.4292` → IC=+0.159 (n=1175)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.4292 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.7532` → IC=+0.159 (n=783)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.7532 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `429.0` → IC=+0.154 (n=950)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 429.0 (IC base=+0.149)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.243 (n=672)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.223 (n=1555)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.224 (n=1514)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.6739` → IC=+0.257 (n=1325)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6739 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.749` → IC=+0.293 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.749 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` < `0.2144` → IC=+0.224 (n=1455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2144 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.8889` → IC=+0.242 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8889 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.230 (n=1003)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `1928.9792` → IC=+0.222 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1928.9792 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.241 (n=1373)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0109 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.242 (n=1226)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0065 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.1586` → IC=+0.243 (n=605)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1586 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.265 (n=518)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.283 (n=919)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.746` → IC=+0.282 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.746 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.3476` → IC=+0.296 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3476 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.7836` → IC=+0.237 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7836 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.2222` → IC=+0.239 (n=831)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2222 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.250 (n=875)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1913.8215` → IC=+0.254 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1913.8215 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.255 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.237)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.184 (n=529)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0035 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.4369` → IC=+0.143 (n=1570)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.4369 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=1647)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.8801` → IC=+0.262 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8801 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.3636` → IC=+0.168 (n=631)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.3636 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.275` → IC=+0.171 (n=259)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 11.275 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.8782` → IC=+0.158 (n=1047)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8782 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.236 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.5208` → IC=+0.150 (n=667)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.5208 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `2.4694` → IC=+0.155 (n=506)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.4694 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `8150.9955` → IC=+0.230 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8150.9955 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `81.0` → IC=+0.150 (n=489)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 81.0 (IC base=+0.137)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.155 (n=1279)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0076 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4451` → IC=+0.153 (n=1279)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4451 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=479)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.139 (n=583)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 7.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.6933` → IC=+0.184 (n=1280)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6933 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.5894` → IC=+0.140 (n=1405)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.5894 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.13` → IC=+0.188 (n=190)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 11.13 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.142 (n=853)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.8616 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.1852` → IC=+0.143 (n=427)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.1852 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2815` → IC=+0.257 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2815 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.4416` → IC=+0.150 (n=1208)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.4416 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `11036.6607` → IC=+0.209 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11036.6607 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `182.0` → IC=+0.142 (n=1201)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 182.0 (IC base=+0.136)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.008` → IC=+0.134 (n=1042)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.008 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.168 (n=579)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.106)

- **PATRÓN** `ibs_20min` > `0.4717` → IC=+0.188 (n=1558)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4717 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` > `1.0671` → IC=+0.199 (n=310)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 1.0671 (IC base=+0.106)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.414` → IC=+0.233 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.414 (IC base=+0.106)

- **PATRÓN** `volumen_regimen` < `0.8911` → IC=+0.134 (n=1039)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8911 (IC base=+0.106)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.126 (n=1083)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `2911.4143` → IC=+0.245 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2911.4143 (IC base=+0.106)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.128 (n=1184)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 54.0 (IC base=+0.106)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.178 (n=511)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0057 (IC base=+0.112)

- **PATRÓN** `drift_60min` |x|≤ `0.1292` → IC=+0.155 (n=511)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1292 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.125 (n=1583)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 5.0 (IC base=+0.112)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.206 (n=1528)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` < `0.2162` → IC=+0.130 (n=1229)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.2162 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.446` → IC=+0.127 (n=1478)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.446 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` < `0.7204` → IC=+0.156 (n=673)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.7204 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` > `0.2244` → IC=+0.171 (n=235)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2244 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` < `1.4564` → IC=+0.141 (n=457)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4564 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` > `2.2013` → IC=+0.126 (n=621)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.2013 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `2852.4784` → IC=+0.166 (n=510)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2852.4784 (IC base=+0.112)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0188` → IC=+0.217 (n=1038)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0188 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.212 (n=1625)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.207 (n=1399)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `0.5143` → IC=+0.247 (n=1557)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5143 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.8562` → IC=+0.242 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8562 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.498` → IC=+0.250 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.498 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `0.6356` → IC=+0.214 (n=1556)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6356 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.2351` → IC=+0.244 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2351 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `2.5239` → IC=+0.235 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5239 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.214 (n=1610)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `2603.3702` → IC=+0.215 (n=1037)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2603.3702 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.230 (n=564)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.200)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.220 (n=563)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.210 (n=826)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.200 (n=1788)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.5208` → IC=+0.256 (n=1690)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5208 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` < `0.8649` → IC=+0.203 (n=1877)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8649 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.806` → IC=+0.262 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.806 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `1.2323` → IC=+0.240 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2323 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2851` → IC=+0.260 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2851 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.2213` → IC=+0.194 (n=1326)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.2213 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.4427` → IC=+0.201 (n=1506)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4427 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=1044)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.135 (n=2829)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.159 (n=2404)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0093 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.5256` → IC=+0.160 (n=2732)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.5256 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.162 (n=1088)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.170 (n=952)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 4.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.9407` → IC=+0.210 (n=912)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9407 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1902` → IC=+0.161 (n=978)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.1902 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.5048` → IC=+0.141 (n=1615)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.5048 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.152` → IC=+0.181 (n=447)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 10.152 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` > `0.9039` → IC=+0.161 (n=1149)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.9039 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1728` → IC=+0.183 (n=746)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1728 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.4578` → IC=+0.157 (n=901)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.4578 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.8913` → IC=+0.161 (n=1800)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.8913 (IC base=+0.150)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.150 (n=1823)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `3647.4412` → IC=+0.154 (n=1821)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3647.4412 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.192 (n=712)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0038 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.4826` → IC=+0.153 (n=2134)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4826 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=783)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.160 (n=724)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 4.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.1809` → IC=+0.164 (n=939)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.1809 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.9181` → IC=+0.145 (n=328)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.9181 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.2447` → IC=+0.126 (n=1899)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` < 0.2447 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.22` → IC=+0.140 (n=2122)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 6.22 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.9014` → IC=+0.148 (n=1355)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.9014 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.0721` → IC=+0.146 (n=999)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.0721 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `1.5352` → IC=+0.138 (n=929)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.5352 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.8163` → IC=+0.141 (n=1407)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.8163 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=2829)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `7196.849` → IC=+0.148 (n=1906)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 7196.849 (IC base=+0.133)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.169 (n=315)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0056 (IC base=+0.157)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.168 (n=320)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0033 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.0919` → IC=+0.189 (n=120)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0919 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=366)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` < `0.5245` → IC=+0.197 (n=239)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.5245 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.2197` → IC=+0.179 (n=166)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.2197 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` < `0.4017` → IC=+0.163 (n=351)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.4017 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.366` → IC=+0.170 (n=386)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 2.366 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` > `0.849` → IC=+0.192 (n=238)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` > 0.849 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.3073` → IC=+0.295 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3073 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `1.4564` → IC=+0.189 (n=120)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.4564 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `2.7022` → IC=+0.203 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7022 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `12537.6672` → IC=+0.198 (n=319)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 12537.6672 (IC base=+0.157)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.211 (n=400)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.1108` → IC=+0.171 (n=399)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1108 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=347)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.167 (n=334)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 5.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.1409` → IC=+0.172 (n=400)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.1409 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.6091` → IC=+0.142 (n=412)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.6091 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.7021` → IC=+0.147 (n=83)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.7021 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.06` → IC=+0.150 (n=990)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 9.06 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.8811` → IC=+0.182 (n=605)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.8811 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.0696` → IC=+0.162 (n=427)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.0696 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `1.4214` → IC=+0.141 (n=302)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4214 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.8194` → IC=+0.143 (n=603)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.8194 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `11328.3365` → IC=+0.147 (n=907)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 11328.3365 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `712.0` → IC=+0.142 (n=862)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 712.0 (IC base=+0.134)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.186 (n=208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.006 (IC base=+0.165)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.181 (n=283)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0099 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.4173` → IC=+0.173 (n=548)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.4173 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.222 (n=232)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.994` → IC=+0.233 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.994 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.706` → IC=+0.225 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.706 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.2084` → IC=+0.204 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2084 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `2.8576` → IC=+0.167 (n=547)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.8576 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `2.2621` → IC=+0.171 (n=414)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.2621 (IC base=+0.165)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.312 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.254)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.262 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.254)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.262 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.254)

- **PATRÓN** `ibs_20min` > `0.4722` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4722 (IC base=+0.254)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.213` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.213 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` < `0.1317` → IC=+0.273 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1317 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` > `0.1037` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1037 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` < `2.5115` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5115 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` > `3.6446` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6446 (IC base=+0.254)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.159 (n=367)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.005 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.159 (n=834)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0044 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.4866` → IC=+0.161 (n=835)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4866 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.170 (n=295)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 4.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.5456` → IC=+0.157 (n=557)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.5456 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.1886` → IC=+0.159 (n=834)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.1886 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `1.006` → IC=+0.165 (n=195)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 1.006 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.4256` → IC=+0.163 (n=772)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.4256 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.678` → IC=+0.161 (n=835)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 6.678 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `1.0946` → IC=+0.159 (n=734)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.0946 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `0.7181` → IC=+0.156 (n=746)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.7181 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.1126` → IC=+0.153 (n=771)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.1126 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.1724` → IC=+0.168 (n=245)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.1724 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.5244` → IC=+0.159 (n=819)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.5244 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.5194` → IC=+0.153 (n=731)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5194 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=813)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.151 (n=695)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0084 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.4933` → IC=+0.165 (n=694)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.4933 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=249)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.150 (n=244)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 4.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.0998` → IC=+0.149 (n=694)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.0998 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.6351` → IC=+0.167 (n=163)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.6351 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.3871` → IC=+0.140 (n=696)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.3871 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.966` → IC=+0.156 (n=155)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 8.966 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.266` → IC=+0.138 (n=627)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 4.266 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.0954` → IC=+0.149 (n=611)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.0954 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `0.7257` → IC=+0.141 (n=620)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.7257 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.0731` → IC=+0.174 (n=299)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.0731 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.1885` → IC=+0.151 (n=600)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.1885 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.7747` → IC=+0.158 (n=454)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.7747 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `7614.1842` → IC=+0.162 (n=694)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 7614.1842 (IC base=+0.138)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.200 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.067)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.142` → IC=+0.163 (n=96)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 2.142 (IC base=+0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.1583` → IC=+0.212 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1583 (IC base=+0.067)

- **PATRÓN** `libro_liquidez` > `3372.8412` → IC=+0.130 (n=160)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 3372.8412 (IC base=+0.067)

- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.212 (n=78)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.071)

- **PATRÓN** `drift_60min` |x|≤ `0.3887` → IC=+0.141 (n=115)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3887 (IC base=+0.071)

- **PATRÓN** `ibs_20min` < `0.1` → IC=+0.183 (n=58)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.1 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` > `0.6343` → IC=+0.171 (n=86)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.6343 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.689` → IC=+0.124 (n=99)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 2.689 (IC base=+0.071)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.006` → IC=-0.195 (n=149)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=291)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.235 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=344)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.214 (n=358)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.123 (n=840)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.103)

- **PATRÓN** `ibs_20min` > `0.575` → IC=+0.197 (n=717)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.575 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` > `0.3558` → IC=+0.172 (n=282)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.3558 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.471` → IC=+0.206 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.471 (IC base=+0.103)

- **PATRÓN** `volumen_regimen` > `0.98` → IC=+0.140 (n=326)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.98 (IC base=+0.103)

- **PATRÓN** `volumen_pendiente_norm` > `0.2853` → IC=+0.216 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2853 (IC base=+0.103)

- **PATRÓN** `volumen_spike_ratio` < `2.0999` → IC=+0.155 (n=535)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.0999 (IC base=+0.103)

- **PATRÓN** `volumen_spike_ratio` > `1.4022` → IC=+0.130 (n=608)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.4022 (IC base=+0.103)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.134 (n=582)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `2435.8886` → IC=+0.156 (n=315)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2435.8886 (IC base=+0.103)

- **PATRÓN** `ibs_20min` < `0.0482` → IC=+0.254 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0482 (IC base=-0.016)

- **PATRÓN** `volumen_pendiente_norm` > `0.0685` → IC=+0.193 (n=86)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0685 (IC base=-0.016)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.175 (n=278)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.006 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.125 (n=278)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 7.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.5717` → IC=+0.203 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5717 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `0.1296` → IC=+0.182 (n=130)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1296 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.622` → IC=+0.141 (n=151)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 3.622 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.0596` → IC=+0.132 (n=218)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.0596 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` < `0.067` → IC=+0.150 (n=184)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.067 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.2625` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2625 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `2.0105` → IC=+0.203 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0105 (IC base=+0.113)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.126 (n=252)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `3951.7016` → IC=+0.139 (n=106)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 3951.7016 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.4946` → IC=+0.184 (n=96)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.4946 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` < `0.5944` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.5944 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.0668` → IC=+0.214 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0668 (IC base=+0.034)

- **PATRÓN** `volumen_spike_ratio` < `2.4111` → IC=+0.148 (n=86)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4111 (IC base=+0.034)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0063` → IC=-0.271 (n=33)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0063
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=102)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.243 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=102)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.184 (n=185)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.005 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.148 (n=248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 8.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` > `0.557` → IC=+0.218 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.557 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `0.335` → IC=+0.176 (n=100)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.335 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.217` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.217 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `0.8144` → IC=+0.141 (n=165)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.8144 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` > `0.6396` → IC=+0.135 (n=220)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6396 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.3002` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3002 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `1.7369` → IC=+0.162 (n=131)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.7369 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` > `1.503` → IC=+0.138 (n=175)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.503 (IC base=+0.115)

- **PATRÓN** `libro_spread` < `0.013` → IC=+0.146 (n=162)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.013 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `1116.0758` → IC=+0.165 (n=216)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 1116.0758 (IC base=+0.115)

- **PATRÓN** `drift_60min` |x|≤ `0.1124` → IC=+0.174 (n=44)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.1124 (IC base=-0.040)

- **PATRÓN** `ibs_20min` < `0.1419` → IC=+0.257 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1419 (IC base=-0.040)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.924` → IC=+0.122 (n=35)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` > 2.924 (IC base=-0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.1363` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1363 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` > `2.7298` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7298 (IC base=-0.040)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.122 (n=72)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=-0.040)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` > `0.0882` → IC=-0.278 (n=43)

  - _Acción_: SKIP cuando `ibs_20min` > 0.0882
  - _Potencial_: sin este filtro IC_bueno=+0.287 (n=45)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.123 (n=112)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.006 (IC base=+0.078)

- **PATRÓN** `ibs_20min` > `0.6875` → IC=+0.190 (n=201)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.6875 (IC base=+0.078)

- **PATRÓN** `dist_vwap_pct` > `0.1948` → IC=+0.147 (n=131)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1948 (IC base=+0.078)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.203` → IC=+0.213 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.203 (IC base=+0.078)

- **PATRÓN** `volumen_regimen` > `1.0632` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.0632 (IC base=+0.078)

- **PATRÓN** `volumen_pendiente_norm` > `0.0847` → IC=+0.199 (n=91)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.0847 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` < `2.4945` → IC=+0.123 (n=205)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.4945 (IC base=+0.078)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.167 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0057 (IC base=-0.057)

- **PATRÓN** `ibs_20min` < `0.0882` → IC=+0.287 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0882 (IC base=-0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.174` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 2.174 (IC base=-0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.1012` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1012 (IC base=-0.057)

- **PATRÓN** `volumen_spike_ratio` > `1.4069` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.4069 (IC base=-0.057)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `10.0` → IC=-0.409 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=141)

- **FILTRO** `dist_vwap_pct` > `0.2334` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2334
  - _Potencial_: sin este filtro IC_bueno=-0.216 (n=167)

- **FILTRO** `volumen_regimen` < `0.7363` → IC=-0.355 (n=60)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7363
  - _Potencial_: sin este filtro IC_bueno=-0.164 (n=123)

- **FILTRO** `dist_vwap_pct` > `0.4126` → IC=-0.409 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4126
  - _Potencial_: sin este filtro IC_bueno=-0.275 (n=136)

- **FILTRO** `sigma_ewma_delta_pct` > `8.389` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.389
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=126)

- **FILTRO** `volumen_pendiente_norm` > `0.074` → IC=-0.400 (n=18)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.074
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=54)

- **FILTRO** `volumen_spike_ratio` > `2.1911` → IC=-0.395 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.1911
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=55)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=49)

- **FILTRO** `volumen_regimen` < `0.7761` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7761
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=48)

- **FILTRO** `sigma_h` < `0.0019` → IC=-0.283 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=44)

- **FILTRO** `drift_60min` |x|> `0.1778` → IC=-0.324 (n=15)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1778
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=48)

- **FILTRO** `volumen_regimen` > `0.807` → IC=-0.333 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.807
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=43)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.8396` → IC=-0.429 (n=40)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8396
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=22)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.333 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=34)

- **FILTRO** `ibs_20min` > `0.6482` → IC=-0.346 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6482
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=26)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=41)

- **FILTRO** `dist_vwap_pct` > `0.0767` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0767
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=41)

- **FILTRO** `dist_vwap_pct` < `0.1871` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.318 (n=20)

- **FILTRO** `volumen_regimen` < `1.0683` → IC=-0.431 (n=27)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.0683
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=14)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.2059` → IC=-0.129 (n=114)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2059
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=222)

- **FILTRO** `dist_vwap_pct` > `0.6296` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6296
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=310)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.124 (n=107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 15.0 (IC base=+0.082)

- **PATRÓN** `ibs_20min` > `0.6522` → IC=+0.161 (n=234)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.6522 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` > `0.4724` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.4724 (IC base=+0.082)

- **PATRÓN** `ibs_20min` < `0.2059` → IC=+0.120 (n=222)

  - _Acción_: Kelly boost +0.60€ cuando `ibs_20min` < 0.2059 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.105` → IC=+0.139 (n=106)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 6.105 (IC base=+0.035)

- **PATRÓN** `libro_liquidez` > `3761.0521` → IC=+0.141 (n=115)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 3761.0521 (IC base=+0.035)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.557` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `ibs_20min` < 0.557
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=77)

- **FILTRO** `volumen_regimen` < `0.7797` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7797
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=77)

- **PATRÓN** `volumen_spike_ratio` > `1.4652` → IC=+0.155 (n=56)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.4652 (IC base=-0.019)

- **PATRÓN** `ibs_20min` < `0.1361` → IC=+0.180 (n=101)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.1361 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` < `0.1782` → IC=+0.140 (n=84)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` < 0.1782 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `3566.36` → IC=+0.147 (n=114)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3566.36 (IC base=+0.097)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` < `0.8361` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8361
  - _Potencial_: sin este filtro IC_bueno=+0.184 (n=55)

- **FILTRO** `ibs_20min` > `0.3115` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3115
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=81)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.156 (n=62)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0042 (IC base=+0.059)

- **PATRÓN** `drift_60min` |x|≤ `0.2855` → IC=+0.125 (n=62)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.2855 (IC base=+0.059)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.239 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.059)

- **PATRÓN** `ibs_20min` > `0.8361` → IC=+0.184 (n=55)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.8361 (IC base=+0.059)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=56)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.059)

- **PATRÓN** `libro_liquidez` > `1549.4073` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1549.4073 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.321` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.321 (IC base=+0.005)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `volumen_pendiente_norm` < `0.0772` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0772
  - _Potencial_: sin este filtro IC_bueno=+0.262 (n=19)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.206 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.174)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.206 (n=32)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=44)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.180 (n=95)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 17.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` < `0.7619` → IC=+0.182 (n=42)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.7619 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.6434` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6434 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.614` → IC=+0.212 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.614 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `0.7968` → IC=+0.258 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7968 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `1.5483` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5483 (IC base=+0.174)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.179 (n=51)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.03 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `514.5372` → IC=+0.173 (n=96)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 514.5372 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.0772` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0772 (IC base=-0.044)

### LATE_WINDOW_5MIN
- **PATRÓN** `elapsed_s` > `209.6` → IC=+0.385 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.6 (IC base=+0.296)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.296)

- **PATRÓN** `drift_60min` |x|≤ `0.969` → IC=+0.353 (n=32)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.969 (IC base=+0.296)

- **PATRÓN** `ballena_activa_n` < `1777.0` → IC=+0.294 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1777.0 (IC base=+0.296)

### LATE_WINDOW_5MIN#BTC#5min
- **PATRÓN** `elapsed_s` > `209.6` → IC=+0.385 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.6 (IC base=+0.296)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.296)

- **PATRÓN** `drift_60min` |x|≤ `0.969` → IC=+0.353 (n=32)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.969 (IC base=+0.296)

- **PATRÓN** `ballena_activa_n` < `1777.0` → IC=+0.294 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1777.0 (IC base=+0.296)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `hora_utc` > `16.0` → IC=+0.136 (n=223)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 16.0 (IC base=+0.106)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.121 (n=621)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `2861.5817` → IC=+0.167 (n=211)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2861.5817 (IC base=+0.106)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `16.0` → IC=+0.136 (n=223)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 16.0 (IC base=+0.106)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.121 (n=621)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `2861.5817` → IC=+0.167 (n=211)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2861.5817 (IC base=+0.106)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `10.0` → IC=-0.204 (n=69)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=76)

- **FILTRO** `py_entrada` < `0.435` → IC=-0.176 (n=35)

  - _Acción_: SKIP cuando `py_entrada` < 0.435
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=110)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=129)

- **FILTRO** `libro_liquidez` < `2453.3967` → IC=-0.263 (n=36)

  - _Acción_: SKIP cuando `libro_liquidez` < 2453.3967
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=109)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=201)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=187)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=36)

- **FILTRO** `liq_n` < `4.0` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `liq_n` < 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

- **FILTRO** `libro_liquidez` < `15479.8554` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 15479.8554
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

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
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=1568)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=49)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.167 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=61)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `38677.73` → IC=-0.123 (n=51)

  - _Acción_: SKIP cuando `liq_usd_total` < 38677.73
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=105)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

- **PATRÓN** `liq_n` > `18.0` → IC=+0.221 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 18.0 (IC base=+0.038)

- **PATRÓN** `liq_usd_total` > `74841.37` → IC=+0.188 (n=78)

  - _Acción_: Kelly boost +0.94€ cuando `liq_usd_total` > 74841.37 (IC base=+0.038)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9773` → IC=-0.156 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9773
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=90)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=701)

- **FILTRO** `liq_usd_total` < `9664.41` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `liq_usd_total` < 9664.41
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9593` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9593
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=16)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=425)

- **FILTRO** `liq_n` < `8.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `liq_n` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **FILTRO** `liq_usd_total` < `24810.11` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `liq_usd_total` < 24810.11
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

### LIQUIDACIONES_5M#XRP#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=115)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.7738` → IC=-0.176 (n=32)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.7738
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=99)

### LIQUIDACIONES_60M
- **FILTRO** `py_entrada` < `0.44` → IC=-0.143 (n=208)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=470)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=314)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=314)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=170)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=170)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.125 (n=78)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=107)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.138 (n=45)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=140)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.123 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=37)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=89)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=185)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=72)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=75)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=228)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=228)

- **FILTRO** `libro_liquidez` < `494.66` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `libro_liquidez` < 494.66
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=173)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=113)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=7268)

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

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1413)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.47` → IC=-0.176 (n=3096)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=9765)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.174 (n=3248)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=10052)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.214 (n=551)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=1664)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.173 (n=554)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=1822)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.203 (n=554)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=1703)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.203 (n=588)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=1780)

- **FILTRO** `ibs_20min` > `0.2857` → IC=-0.170 (n=579)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=1789)

- **PATRÓN** `libro_liquidez` > `1725.1772` → IC=+0.122 (n=768)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1725.1772 (IC base=+0.029)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.184 (n=542)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=1652)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.192 (n=567)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=1800)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=2634)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=2790)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=2796)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` > `20.0` → IC=-0.130 (n=106)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=332)

- **FILTRO** `ibs_20min` > `0.1763` → IC=-0.142 (n=107)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1763
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=331)

- **FILTRO** `libro_liquidez` < `16862.2515` → IC=-0.145 (n=212)

  - _Acción_: SKIP cuando `libro_liquidez` < 16862.2515
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=638)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.214 (n=68)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=225)

- **FILTRO** `ibs_20min` < `0.1006` → IC=-0.247 (n=73)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1006
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=220)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.192 (n=89)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=182)

- **FILTRO** `drift_20min_pct` |x|> `0.1791` → IC=-0.167 (n=67)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1791
  - _Potencial_: sin este filtro IC_bueno=-0.121 (n=204)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=729)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=223)

### MOMENTUM_IBS_5M#BNB#5min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=40)

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

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.179 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 15.0 (IC base=+0.032)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=9157)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=20533)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.275 (n=7163)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=22527)

- **FILTRO** `ibs_7min` < `0.2941` → IC=-0.236 (n=7415)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2941
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=22275)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.157 (n=10043)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=19647)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.229 (n=9240)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=27860)

- **FILTRO** `ibs_7min` > `0.2941` → IC=-0.179 (n=9267)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2941
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=27833)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.308 (n=1162)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=3704)

- **FILTRO** `ibs_7min` < `0.7097` → IC=-0.253 (n=1602)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7097
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=3264)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.182 (n=1151)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=3715)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.151 (n=4298)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=2097)

- **FILTRO** `drift_7min_pct` |x|> `0.1121` → IC=-0.124 (n=2174)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1121
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=4221)

- **FILTRO** `ibs_7min` > `0.7937` → IC=-0.206 (n=1598)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7937
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=4797)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.137 (n=1204)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=3952)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.250 (n=1237)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=3919)

- **FILTRO** `ibs_7min` < `0.752` → IC=-0.189 (n=1289)

  - _Acción_: SKIP cuando `ibs_7min` < 0.752
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=3867)

- **FILTRO** `ballena_activa_n` > `160.0` → IC=-0.172 (n=1283)

  - _Acción_: SKIP cuando `ballena_activa_n` > 160.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=3873)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.260 (n=1285)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=3907)

- **FILTRO** `ibs_7min` > `0.2588` → IC=-0.174 (n=1295)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2588
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=3897)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.187 (n=1297)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=3895)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.171 (n=1130)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=3475)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.308 (n=1118)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=3487)

- **FILTRO** `ibs_7min` < `0.1972` → IC=-0.259 (n=1151)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1972
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3454)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.213 (n=1099)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=3506)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.237 (n=1590)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=5215)

- **FILTRO** `ibs_7min` > `0.759` → IC=-0.179 (n=1700)

  - _Acción_: SKIP cuando `ibs_7min` > 0.759
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=5105)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=1566)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=3315)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.244 (n=1196)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=3685)

- **FILTRO** `ibs_7min` < `0.7437` → IC=-0.182 (n=1220)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7437
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=3661)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.176 (n=1188)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=3693)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.261 (n=1246)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=3749)

- **FILTRO** `ibs_7min` > `0.2751` → IC=-0.174 (n=1248)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2751
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=3747)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.190 (n=1219)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=3776)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.36` → IC=-0.261 (n=1227)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=4001)

- **FILTRO** `ibs_7min` < `0.7037` → IC=-0.230 (n=1306)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7037
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3922)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.179 (n=1694)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=5342)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.275 (n=1160)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=3794)

- **FILTRO** `ibs_7min` < `0.7083` → IC=-0.233 (n=1238)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7083
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=3716)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.212 (n=1188)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3766)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.204 (n=1641)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=5036)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=1038)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=518)

- **FILTRO** `libro_liquidez` < `10575.5071` → IC=-0.143 (n=141)

  - _Acción_: SKIP cuando `libro_liquidez` < 10575.5071
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=423)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=568)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=323)

- **FILTRO** `ballena_activa_n` > `2.0` → IC=-0.138 (n=139)

  - _Acción_: SKIP cuando `ballena_activa_n` > 2.0
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=286)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=543)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=436)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4164` → IC=+0.146 (n=472)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio` |x|> 0.4164 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.123 (n=638)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.115)

- **PATRÓN** `total_vol_5m` < `464.449` → IC=+0.148 (n=237)

  - _Acción_: Kelly boost +0.74€ cuando `total_vol_5m` < 464.449 (IC base=+0.115)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.171 (n=168)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `total_vol_5m` < `422.506` → IC=+0.137 (n=144)

  - _Acción_: Kelly boost +0.68€ cuando `total_vol_5m` < 422.506 (IC base=+0.136)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.121 (n=101)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 10.0 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 13.0 (IC base=+0.096)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4131` → IC=+0.170 (n=95)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.85€ cuando `delta_ratio` |x|> 0.4131 (IC base=+0.094)

- **PATRÓN** `total_vol_5m` < `391.8444` → IC=+0.208 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 391.8444 (IC base=+0.094)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.160 (n=48)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 69.0 (IC base=+0.094)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3985` → IC=+0.175 (n=124)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio` |x|> 0.3985 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.205 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.141)

- **PATRÓN** `total_vol_5m` < `6272.013` → IC=+0.167 (n=109)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 6272.013 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 34.0 (IC base=+0.141)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.3998` → IC=+0.151 (n=124)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.75€ cuando `delta_ratio` |x|> 0.3998 (IC base=+0.104)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.141 (n=126)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 13.0 (IC base=+0.104)

- **PATRÓN** `total_vol_5m` < `257344.8` → IC=+0.153 (n=93)

  - _Acción_: Kelly boost +0.76€ cuando `total_vol_5m` < 257344.8 (IC base=+0.104)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.223 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `3728.9067` → IC=+0.194 (n=47)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 3728.9067 (IC base=+0.104)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.0073` → IC=-0.339 (n=116)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0073
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=227)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0076` → IC=-0.392 (n=35)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0076
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=70)

- **FILTRO** `T_h` > `87.9936` → IC=-0.429 (n=26)

  - _Acción_: SKIP cuando `T_h` > 87.9936
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=79)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.203 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=-0.145)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0107` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0107
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=20)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0142` → IC=-0.206 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0142
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=49)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `pct_vs_K` |x|> `2.8381` → IC=-0.243 (n=177)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8381
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=178)

- **FILTRO** `pct_vs_K` |x|> `3.3729` → IC=-0.442 (n=101)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.3729
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=197)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.004` → IC=-0.227 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.004
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=94)

- **FILTRO** `pct_vs_K` |x|> `0.8662` → IC=-0.244 (n=80)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 0.8662
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=45)

- **FILTRO** `sigma_h` < `0.0071` → IC=-0.315 (n=79)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0071
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=27)

- **FILTRO** `T_h` > `144.5878` → IC=-0.315 (n=25)

  - _Acción_: SKIP cuando `T_h` > 144.5878
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=81)

- **FILTRO** `T_h` < `96.6729` → IC=-0.361 (n=34)

  - _Acción_: SKIP cuando `T_h` < 96.6729
  - _Potencial_: sin este filtro IC_bueno=-0.243 (n=72)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `2.4552` → IC=-0.360 (n=48)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.4552
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=51)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.385 (n=24)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=74)

- **FILTRO** `T_h` > `53.9898` → IC=-0.313 (n=73)

  - _Acción_: SKIP cuando `T_h` > 53.9898
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=25)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0099` → IC=-0.151 (n=41)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0099
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=41)

- **FILTRO** `T_h` > `135.1308` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `T_h` > 135.1308
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=55)

- **FILTRO** `pct_vs_K` |x|> `5.0222` → IC=-0.318 (n=20)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 5.0222
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=62)

- **FILTRO** `sigma_h` < `0.015` → IC=-0.367 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.015
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=15)

- **FILTRO** `T_h` > `63.9197` → IC=-0.389 (n=43)

  - _Acción_: SKIP cuando `T_h` > 63.9197
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=15)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.131` → IC=+0.463 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.131 (IC base=+0.389)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.473 (n=35)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.389)

- **PATRÓN** `T_h` > `0.4742` → IC=+0.446 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4742 (IC base=+0.389)

- **PATRÓN** `dist_50` > `0.4444` → IC=+0.473 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4444 (IC base=+0.389)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.466 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.389)

- **PATRÓN** `edge` > `0.1023` → IC=+0.457 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.422)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.462 (n=103)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.422)

- **PATRÓN** `T_h` > `1.4813` → IC=+0.452 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4813 (IC base=+0.422)

- **PATRÓN** `dist_50` > `0.3938` → IC=+0.483 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3938 (IC base=+0.422)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.447 (n=111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.422)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `dist_50` > `0.47` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.433)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.413 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.433)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.423 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.433)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.225` → IC=+0.471 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.225 (IC base=+0.480)

- **PATRÓN** `sigma_h` < `0.0148` → IC=+0.471 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0148 (IC base=+0.480)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.471 (n=32)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.480)

- **PATRÓN** `T_h` > `0.8566` → IC=+0.471 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8566 (IC base=+0.480)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.463 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.480)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.463 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.480)

- **PATRÓN** `edge` > `0.1043` → IC=+0.474 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1043 (IC base=+0.474)

- **PATRÓN** `sigma_h` < `0.0163` → IC=+0.475 (n=77)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0163 (IC base=+0.474)

- **PATRÓN** `T_h` > `0.9178` → IC=+0.472 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.9178 (IC base=+0.474)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.486 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.474)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.464 (n=54)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.474)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.464 (n=82)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.474)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=149)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=270)

- **FILTRO** `streak_estiramiento` > `0.836` → IC=-0.178 (n=57)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.836
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=172)

- **PATRÓN** `streak_estiramiento` < `0.4576` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `streak_estiramiento` < 0.4576 (IC base=+0.030)

- **PATRÓN** `streak_estiramiento` < `0.4013` → IC=+0.192 (n=76)

  - _Acción_: Kelly boost +0.96€ cuando `streak_estiramiento` < 0.4013 (IC base=+0.032)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `ballena_activa_n` > `52.0` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 52.0
  - _Potencial_: sin este filtro IC_bueno=+0.186 (n=33)

- **PATRÓN** `volumen_racha` < `990711.2` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_racha` < 990711.2 (IC base=+0.000)

- **PATRÓN** `streak_estiramiento` < `0.4152` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `streak_estiramiento` < 0.4152 (IC base=+0.000)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 52.0 (IC base=+0.000)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=77)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=87)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=36)

- **FILTRO** `streak_estiramiento` > `1.1202` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_estiramiento` > 1.1202
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=31)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=24)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=683)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=689)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=371)

### STREAK_FADE_60M
- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `libro_liquidez` < `2389.5844` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 2389.5844
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

### STREAK_FADE_60M#ETH#60min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=544)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=1089)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=669)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=668)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=2712)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1395)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1403)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.221 (n=643)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.1627` → IC=+0.192 (n=1248)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1627 (IC base=+0.185)

- **PATRÓN** `delta_ratio_macro` |x|> `0.217` → IC=+0.193 (n=473)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.217 (IC base=+0.185)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3328` → IC=+0.215 (n=1096)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3328 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.199 (n=1003)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 11.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.186 (n=1436)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 16.0 (IC base=+0.185)

- **PATRÓN** `ibs_15` > `0.6122` → IC=+0.262 (n=1418)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6122 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` > `0.2881` → IC=+0.187 (n=509)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.2881 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.122` → IC=+0.271 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.122 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `2980.6496` → IC=+0.190 (n=945)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2980.6496 (IC base=+0.185)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=491)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.218 (n=225)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.0591` → IC=+0.289 (n=112)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0591 (IC base=+0.202)

- **PATRÓN** `drift_15min` |x|≤ `0.3806` → IC=+0.210 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3806 (IC base=+0.202)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2587` → IC=+0.237 (n=112)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2587 (IC base=+0.202)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1483` → IC=+0.261 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1483 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.224 (n=353)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.202)

- **PATRÓN** `ibs_15` > `0.7721` → IC=+0.288 (n=300)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7721 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.3848` → IC=+0.268 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3848 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.495` → IC=+0.256 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.495 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `15928.6386` → IC=+0.237 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15928.6386 (IC base=+0.202)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `25.173` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 25.173
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=315)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.143 (n=113)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0035 (IC base=+0.142)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.165 (n=225)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.005 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.0692` → IC=+0.156 (n=149)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0692 (IC base=+0.142)

- **PATRÓN** `delta_ratio_macro` |x|> `0.14` → IC=+0.161 (n=225)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio_macro` |x|> 0.14 (IC base=+0.142)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2561` → IC=+0.171 (n=235)

  - _Acción_: Kelly boost +0.85€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2561 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.164 (n=251)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 11.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.142 (n=344)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 16.0 (IC base=+0.142)

- **PATRÓN** `ibs_15` > `0.6192` → IC=+0.221 (n=338)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6192 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.1598` → IC=+0.163 (n=262)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1598 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.57` → IC=+0.218 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.57 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `3462.5082` → IC=+0.148 (n=302)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3462.5082 (IC base=+0.142)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `drift_15min` |x|> `0.6001` → IC=-0.139 (n=34)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.6001
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=67)

- **FILTRO** `hora_utc` < `5.0` → IC=-0.192 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=72)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.254 (n=59)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.1474` → IC=+0.201 (n=155)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1474 (IC base=+0.161)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0662` → IC=+0.192 (n=157)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.0662 (IC base=+0.161)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3414` → IC=+0.235 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3414 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.203 (n=119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.161)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.243 (n=177)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.118` → IC=+0.183 (n=102)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.118 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` < `0.6573` → IC=+0.162 (n=199)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.6573 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.532` → IC=+0.395 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.532 (IC base=+0.161)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.171 (n=138)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `3004.732` → IC=+0.268 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3004.732 (IC base=+0.161)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.219 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.161)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.7105` → IC=-0.146 (n=97)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.7105
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=778)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `24.491` → IC=+0.145 (n=29)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 24.491 (IC base=+0.025)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.662` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 15.662 (IC base=+0.005)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0171` → IC=+0.226 (n=257)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0171 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.0851` → IC=+0.198 (n=170)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.0851 (IC base=+0.182)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0401` → IC=+0.190 (n=385)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.95€ cuando `delta_ratio_macro` |x|> 0.0401 (IC base=+0.182)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0919` → IC=+0.237 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0919 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=191)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.182)

- **PATRÓN** `ibs_15` > `0.5488` → IC=+0.278 (n=385)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5488 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `0.1268` → IC=+0.202 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1268 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.987` → IC=+0.227 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.987 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.952` → IC=+0.182 (n=325)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 5.952 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `2863.6552` → IC=+0.263 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2863.6552 (IC base=+0.182)

- **PATRÓN** `ibs_15` < `0.1176` → IC=+0.166 (n=429)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.83€ cuando `ibs_15` < 0.1176 (IC base=+0.045)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.374 (n=173)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.337)

- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.342 (n=257)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.337)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1462` → IC=+0.363 (n=254)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1462 (IC base=+0.337)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1316` → IC=+0.373 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1316 (IC base=+0.337)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.360 (n=383)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.337)

- **PATRÓN** `ibs_15` > `0.7853` → IC=+0.385 (n=381)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7853 (IC base=+0.337)

- **PATRÓN** `dist_vwap_pct` > `0.4267` → IC=+0.373 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4267 (IC base=+0.337)

- **PATRÓN** `dist_vwap_pct` < `0.1075` → IC=+0.337 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1075 (IC base=+0.337)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.143` → IC=+0.351 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.143 (IC base=+0.337)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.343 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.337)

- **PATRÓN** `libro_liquidez` > `3544.0094` → IC=+0.351 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3544.0094 (IC base=+0.337)

- **PATRÓN** `ballena_activa_n` < `478.0` → IC=+0.359 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 478.0 (IC base=+0.337)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.343 (n=189)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.340)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.378 (n=72)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.340)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.351 (n=72)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.340)

- **PATRÓN** `drift_15min` |x|≤ `0.4231` → IC=+0.345 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4231 (IC base=+0.340)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2136` → IC=+0.370 (n=98)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2136 (IC base=+0.340)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1224` → IC=+0.389 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1224 (IC base=+0.340)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.366 (n=200)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.340)

- **PATRÓN** `ibs_15` > `0.8048` → IC=+0.380 (n=215)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8048 (IC base=+0.340)

- **PATRÓN** `dist_vwap_pct` > `0.4001` → IC=+0.406 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4001 (IC base=+0.340)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.381` → IC=+0.357 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.381 (IC base=+0.340)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.597` → IC=+0.341 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.597 (IC base=+0.340)

- **PATRÓN** `ballena_activa_n` < `582.0` → IC=+0.393 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 582.0 (IC base=+0.340)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.328 (n=167)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.330)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.376 (n=111)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.330)

- **PATRÓN** `drift_60min` |x|≤ `0.1039` → IC=+0.342 (n=112)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1039 (IC base=+0.330)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0587` → IC=+0.346 (n=167)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0587 (IC base=+0.330)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.298` → IC=+0.356 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.298 (IC base=+0.330)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.385 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.330)

- **PATRÓN** `ibs_15` > `0.7403` → IC=+0.394 (n=167)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7403 (IC base=+0.330)

- **PATRÓN** `dist_vwap_pct` > `0.4534` → IC=+0.357 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4534 (IC base=+0.330)

- **PATRÓN** `dist_vwap_pct` < `0.1197` → IC=+0.342 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1197 (IC base=+0.330)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.717` → IC=+0.354 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.717 (IC base=+0.330)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.342 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.330)

- **PATRÓN** `libro_liquidez` > `4001.8474` → IC=+0.359 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4001.8474 (IC base=+0.330)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.013` → IC=-0.216 (n=604)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.013
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=1813)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.191 (n=782)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1635)

- **FILTRO** `libro_liquidez` < `3925.9545` → IC=-0.135 (n=1595)

  - _Acción_: SKIP cuando `libro_liquidez` < 3925.9545
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=822)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1373` → IC=+0.260 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1373 (IC base=-0.059)

- **PATRÓN** `ibs_15` > `0.6326` → IC=+0.270 (n=598)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6326 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` > `0.5693` → IC=+0.178 (n=113)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.5693 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` < `0.2727` → IC=+0.181 (n=468)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.2727 (IC base=-0.059)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1175` → IC=+0.240 (n=985)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1175 (IC base=-0.040)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1804` → IC=+0.241 (n=948)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1804 (IC base=-0.040)

- **PATRÓN** `ibs_15` < `0.3521` → IC=+0.283 (n=1475)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3521 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` > `0.655` → IC=+0.286 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.655 (IC base=-0.040)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.220 (n=370)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=1111)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.225 (n=488)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=993)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.208 (n=938)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=543)

- **FILTRO** `sigma_ewma_delta_pct` > `19.843` → IC=-0.250 (n=262)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.843
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=1219)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.176 (n=137)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0028 (IC base=+0.084)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2033` → IC=+0.281 (n=71)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2033 (IC base=+0.084)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1422` → IC=+0.336 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1422 (IC base=+0.084)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.351 (n=139)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.084)

- **PATRÓN** `dist_vwap_pct` > `0.1352` → IC=+0.292 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1352 (IC base=+0.084)

- **PATRÓN** `dist_vwap_pct` < `0.536` → IC=+0.282 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.536 (IC base=+0.084)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6642` → IC=-0.208 (n=94)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6642
  - _Potencial_: sin este filtro IC_bueno=+0.262 (n=288)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=365)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.184 (n=191)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0051 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.0771` → IC=+0.221 (n=127)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0771 (IC base=+0.146)

- **PATRÓN** `drift_15min` |x|≤ `0.4246` → IC=+0.163 (n=96)

  - _Acción_: Kelly boost +0.82€ cuando `drift_15min` |x|≤ 0.4246 (IC base=+0.146)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1329` → IC=+0.158 (n=191)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio_macro` |x|> 0.1329 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3059` → IC=+0.241 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3059 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.196 (n=133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.6642` → IC=+0.262 (n=288)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6642 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.4741` → IC=+0.147 (n=83)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.4741 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1187` → IC=+0.180 (n=204)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.1187 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.661` → IC=+0.155 (n=227)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 6.661 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.159 (n=365)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `10970.0273` → IC=+0.182 (n=130)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 10970.0273 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.238 (n=602)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.226)

- **PATRÓN** `drift_15min` |x|≤ `0.7761` → IC=+0.233 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7761 (IC base=+0.226)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2` → IC=+0.253 (n=273)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.241 (n=299)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.226)

- **PATRÓN** `ibs_15` < `0.356` → IC=+0.267 (n=602)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.356 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.7494` → IC=+0.295 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7494 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.074` → IC=+0.257 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.074 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.262` → IC=+0.230 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.262 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `3539.2271` → IC=+0.230 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3539.2271 (IC base=+0.226)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0101` → IC=-0.229 (n=142)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0101
  - _Potencial_: sin este filtro IC_bueno=-0.138 (n=429)

- **FILTRO** `drift_60min` |x|> `0.1671` → IC=-0.225 (n=194)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1671
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=377)

- **FILTRO** `drift_15min` |x|> `0.888` → IC=-0.257 (n=142)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.888
  - _Potencial_: sin este filtro IC_bueno=-0.129 (n=429)

- **FILTRO** `sigma_ewma_delta_pct` > `18.047` → IC=-0.133 (n=306)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.047
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=2450)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=-0.161)

- **PATRÓN** `dist_vwap_pct` < `0.1511` → IC=+0.122 (n=43)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.1511 (IC base=-0.161)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0726` → IC=+0.218 (n=246)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0726 (IC base=-0.044)

- **PATRÓN** `ibs_15` < `0.3542` → IC=+0.262 (n=275)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3542 (IC base=-0.044)

- **PATRÓN** `dist_vwap_pct` > `0.6964` → IC=+0.210 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6964 (IC base=-0.044)

- **PATRÓN** `dist_vwap_pct` < `0.1869` → IC=+0.216 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1869 (IC base=-0.044)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0196` → IC=-0.264 (n=363)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0196
  - _Potencial_: sin este filtro IC_bueno=-0.127 (n=365)

- **FILTRO** `drift_15min` |x|> `1.2028` → IC=-0.243 (n=181)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2028
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=547)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.260 (n=181)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=547)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1531` → IC=+0.277 (n=137)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1531 (IC base=-0.046)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1035` → IC=+0.371 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1035 (IC base=-0.046)

- **PATRÓN** `ibs_15` < `0.3457` → IC=+0.318 (n=409)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3457 (IC base=-0.046)

- **PATRÓN** `dist_vwap_pct` > `1.0924` → IC=+0.412 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0924 (IC base=-0.046)

### UPDOWN_GBM_ETH_15M_HORA7
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2775` → IC=-0.136 (n=20)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2775
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **FILTRO** `ibs_15` < `0.8489` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8489
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **PATRÓN** `drift_60min` |x|≤ `0.083` → IC=+0.179 (n=26)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.083 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.1565` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1565 (IC base=+0.069)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2775` → IC=-0.136 (n=20)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2775
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **FILTRO** `ibs_15` < `0.8489` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8489
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **PATRÓN** `drift_60min` |x|≤ `0.083` → IC=+0.179 (n=26)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.083 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.1565` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1565 (IC base=+0.069)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.295 (n=412)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.291)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.294 (n=280)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.0571` → IC=+0.317 (n=206)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0571 (IC base=+0.291)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2395` → IC=+0.303 (n=206)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2395 (IC base=+0.291)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1083` → IC=+0.343 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1083 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.311 (n=648)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8382` → IC=+0.329 (n=618)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8382 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.2752` → IC=+0.328 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2752 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.453` → IC=+0.336 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.453 (IC base=+0.291)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.294 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `14354.3614` → IC=+0.308 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14354.3614 (IC base=+0.291)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.310 (n=114)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.286)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.296 (n=155)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.336 (n=114)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.286)

- **PATRÓN** `drift_15min` |x|≤ `0.3892` → IC=+0.284 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3892 (IC base=+0.286)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2603` → IC=+0.302 (n=114)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2603 (IC base=+0.286)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1432` → IC=+0.320 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1432 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.306 (n=359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.286)

- **PATRÓN** `ibs_15` > `0.83` → IC=+0.317 (n=342)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.83 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.2565` → IC=+0.355 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2565 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.837` → IC=+0.364 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.837 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `15946.6772` → IC=+0.336 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15946.6772 (IC base=+0.286)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.303 (n=277)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.297)

- **PATRÓN** `drift_60min` |x|≤ `0.1133` → IC=+0.302 (n=185)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1133 (IC base=+0.297)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1481` → IC=+0.312 (n=184)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1481 (IC base=+0.297)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.288` → IC=+0.337 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.288 (IC base=+0.297)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.329 (n=249)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.297)

- **PATRÓN** `ibs_15` > `0.8475` → IC=+0.338 (n=276)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8475 (IC base=+0.297)

- **PATRÓN** `dist_vwap_pct` > `0.6245` → IC=+0.300 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6245 (IC base=+0.297)

- **PATRÓN** `dist_vwap_pct` < `0.456` → IC=+0.299 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.456 (IC base=+0.297)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.169` → IC=+0.332 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.169 (IC base=+0.297)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.308 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.297)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2669` → IC=-0.181 (n=67)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2669
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=205)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1131` → IC=-0.171 (n=68)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1131
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=204)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.121` → IC=-0.164 (n=105)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.121
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=327)

- **FILTRO** `drift_15min` |x|> `0.4386` → IC=-0.135 (n=146)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.4386
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=286)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1445` → IC=-0.148 (n=52)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1445
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=106)

- **FILTRO** `drift_60min` |x|> `0.1544` → IC=-0.214 (n=19)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1544
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2236` → IC=-0.133 (n=28)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2236
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.309 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2122` → IC=-0.395 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2122
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1066` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1066
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.0931` → IC=-0.214 (n=19)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=11)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `74.1058` → IC=+0.187 (n=266)

  - _Acción_: Kelly boost +0.93€ cuando `T_h` > 74.1058 (IC base=+0.180)

- **PATRÓN** `ratio` < `0.9766` → IC=+0.464 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9766 (IC base=+0.180)

- **PATRÓN** `T_h` > `145.7998` → IC=+0.399 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7998 (IC base=+0.336)

- **PATRÓN** `ratio` > `1.0449` → IC=+0.394 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0449 (IC base=+0.336)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `144.2203` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `T_h` > 144.2203 (IC base=+0.148)

- **PATRÓN** `ratio` < `0.9922` → IC=+0.328 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9922 (IC base=+0.148)

- **PATRÓN** `T_h` < `111.9936` → IC=+0.293 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 111.9936 (IC base=+0.289)

- **PATRÓN** `T_h` > `98.1369` → IC=+0.295 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 98.1369 (IC base=+0.289)

- **PATRÓN** `ratio` > `1.0449` → IC=+0.417 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0449 (IC base=+0.289)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `87.9957` → IC=+0.246 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9957 (IC base=+0.230)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.404 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.230)

- **PATRÓN** `T_h` > `102.672` → IC=+0.333 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 102.672 (IC base=+0.312)

- **PATRÓN** `ratio` > `1.0088` → IC=+0.321 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0088 (IC base=+0.312)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1402` → IC=+0.455 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1402 (IC base=+0.404)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6122 sube el IC de +0.185 a +0.262 en UPDOWN_GBM#15min (n=1418). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7721 sube el IC de +0.202 a +0.288 en UPDOWN_GBM#BTC#15min (n=300). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6192 sube el IC de +0.142 a +0.221 en UPDOWN_GBM#ETH#15min (n=338). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.161 a +0.243 en UPDOWN_GBM#SOL#15min (n=177). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5488 sube el IC de +0.182 a +0.278 en UPDOWN_GBM#XRP#15min (n=385). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1176 sube el IC de +0.045 a +0.166 en UPDOWN_GBM#XRP#15min (n=429). Ya aplicado como kelly_boost=+0.83€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6326 sube el IC de -0.059 a +0.270 en UPDOWN_GBM_15M_TARDIO (n=598). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3521 sube el IC de -0.040 a +0.283 en UPDOWN_GBM_15M_TARDIO (n=1475). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.084 a +0.351 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=139). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6642 sube el IC de +0.146 a +0.262 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=288). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.356 sube el IC de +0.226 a +0.267 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=602). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.161 a +0.342 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3542 sube el IC de -0.044 a +0.262 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=275). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3457 sube el IC de -0.046 a +0.318 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=409). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8382 sube el IC de +0.291 a +0.329 en UPDOWN_GBM_IBS_ALTO (n=618). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.83 sube el IC de +0.286 a +0.317 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=342). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8475 sube el IC de +0.297 a +0.338 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=276). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7853 sube el IC de +0.337 a +0.385 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=381). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8048 sube el IC de +0.340 a +0.380 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=215). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7403 sube el IC de +0.330 a +0.394 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=167). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1255 | +0.091 | +153.01€ | 2 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1255 | +0.091 | +153.01€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 926 | +0.100 | +127.82€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 926 | +0.100 | +127.82€ | 2 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 243 | +0.047 | +6.54€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 243 | +0.047 | +6.54€ | 4 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 60 | +0.145 | +20.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 60 | +0.145 | +20.16€ | 0 | 6 |
| ✅ BALLENAS_TARDIAS | 23496 | -0.091 | -3097.55€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1401 | -0.047 | -214.63€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 22095 | -0.094 | -2882.92€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3564 | -0.084 | -574.45€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3564 | -0.084 | -574.45€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1401 | -0.047 | -214.63€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1401 | -0.047 | -214.63€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 374 | -0.136 | -161.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 374 | -0.136 | -161.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 6747 | -0.029 | -608.41€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 6747 | -0.029 | -608.41€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 6200 | -0.094 | -414.02€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 6200 | -0.094 | -414.02€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 5210 | -0.182 | -1124.99€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 5210 | -0.182 | -1124.99€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 15952 | -0.032 | +4129.38€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 4195 | -0.001 | +1835.05€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 11757 | -0.043 | +2294.33€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 15952 | -0.032 | +4129.38€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 4195 | -0.001 | +1835.05€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 11757 | -0.043 | +2294.33€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 1408 | -0.101 | -177.90€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 160 | -0.056 | -20.80€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 1248 | -0.107 | -157.10€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 771 | -0.091 | -96.00€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 136 | -0.051 | -15.57€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 635 | -0.100 | -80.43€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 439 | -0.126 | -68.02€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 24 | -0.077 | -5.22€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#5min | 415 | -0.128 | -62.79€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 57 | -0.161 | -4.36€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 57 | -0.161 | -4.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 86013 | +0.113 | -4382.01€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 13173 | +0.184 | -424.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 340 | -0.099 | -49.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 66796 | +0.100 | -3711.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 5704 | +0.110 | -196.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 11115 | +0.098 | -976.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 43 | -0.167 | -2.82€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 11057 | +0.099 | -961.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 17399 | +0.132 | -355.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4110 | +0.201 | -143.69€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 11071 | +0.112 | -167.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2176 | +0.108 | -21.82€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 11155 | +0.088 | -1066.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 50 | -0.077 | -4.56€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 11090 | +0.090 | -1050.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 18348 | +0.124 | -366.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 5091 | +0.175 | -75.22€ | 1 | 7 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 11183 | +0.105 | -228.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2062 | +0.097 | -54.85€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 16863 | +0.115 | -961.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 3836 | +0.187 | -206.52€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 243 | -0.059 | +4.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 11318 | +0.093 | -640.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1466 | +0.129 | -119.80€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 11133 | +0.102 | -655.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 43 | -0.033 | +7.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 11077 | +0.102 | -662.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 13647 | +0.192 | -892.41€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 13647 | +0.192 | -892.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3290 | +0.168 | -350.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3290 | +0.168 | -350.23€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1010 | +0.199 | +2.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1010 | +0.199 | +2.96€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3222 | +0.182 | -271.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3222 | +0.182 | -271.90€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 2885 | +0.239 | -90.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 2885 | +0.239 | -90.09€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3161 | +0.192 | -196.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3161 | +0.192 | -196.90€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 648 | +0.428 | -20.71€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 648 | +0.428 | -20.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 246 | +0.431 | -5.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 246 | +0.431 | -5.40€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 244 | +0.435 | -3.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 244 | +0.435 | -3.05€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 150 | +0.401 | -11.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 150 | +0.401 | -11.23€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 46788 | +0.198 | -3685.66€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 46788 | +0.198 | -3685.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 8111 | +0.175 | -953.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 8111 | +0.175 | -953.84€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 7463 | +0.224 | -267.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 7463 | +0.224 | -267.46€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 8082 | +0.174 | -964.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 8082 | +0.174 | -964.55€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 7549 | +0.219 | -290.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 7549 | +0.219 | -290.98€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 7728 | +0.204 | -505.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 7728 | +0.204 | -505.56€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 7855 | +0.192 | -703.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 7855 | +0.192 | -703.27€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 17588 | +0.119 | +167.85€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 17588 | +0.119 | +167.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 8724 | +0.123 | +132.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 8724 | +0.123 | +132.92€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 8864 | +0.115 | +34.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 8864 | +0.115 | +34.92€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1391 | +0.292 | -7.83€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1391 | +0.292 | -7.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 620 | +0.277 | -17.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 620 | +0.277 | -17.67€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 667 | +0.297 | +8.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 667 | +0.297 | +8.04€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 104 | +0.340 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 104 | +0.340 | +1.79€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 612 | +0.438 | +0.15€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 612 | +0.438 | +0.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 289 | +0.438 | -0.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 289 | +0.438 | -0.20€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 283 | +0.440 | +0.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 283 | +0.440 | +0.46€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 40 | +0.381 | -0.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 40 | +0.381 | -0.11€ | 0 | 1 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1021 | +0.077 | -37.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 356 | +0.064 | -26.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 665 | +0.083 | -11.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 60 | +0.129 | +4.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 60 | +0.129 | +4.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 802 | +0.085 | -12.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 137 | +0.090 | -0.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 665 | +0.083 | -11.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 159 | +0.015 | -29.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 159 | +0.015 | -29.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 32069 | +0.098 | -976.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 2659 | +0.090 | +16.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 29410 | +0.099 | -993.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 18090 | +0.102 | -285.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 2659 | +0.090 | +16.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 15431 | +0.104 | -302.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 5882 | +0.109 | -18.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 5882 | +0.109 | -18.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 8097 | +0.081 | -672.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 8097 | +0.081 | -672.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 767 | +0.226 | -91.34€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 767 | +0.226 | -91.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 767 | +0.226 | -91.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 767 | +0.226 | -91.34€ | 1 | 4 |
| ✅ GBM_LATE_15M | 23297 | +0.080 | +10905.63€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 23297 | +0.080 | +10905.63€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 3861 | +0.193 | +2803.17€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 3861 | +0.193 | +2803.17€ | 0 | 18 |
| ✅ GBM_LATE_15M#BTC | 3457 | +0.175 | +2356.11€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 3457 | +0.175 | +2356.11€ | 0 | 26 |
| ✅ GBM_LATE_15M#DOGE | 4010 | +0.201 | +3027.34€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 4010 | +0.201 | +3027.34€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 3473 | +0.014 | +669.49€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 3473 | +0.014 | +669.49€ | 1 | 16 |
| ✅ GBM_LATE_15M#SOL | 3379 | -0.034 | +780.01€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 3379 | -0.034 | +780.01€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 5117 | -0.044 | +1269.51€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 5117 | -0.044 | +1269.51€ | 4 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 24627 | +0.083 | +12882.60€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 24627 | +0.083 | +12882.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 4687 | +0.015 | +2590.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 4687 | +0.015 | +2590.29€ | 1 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 5145 | +0.011 | +1026.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 5145 | +0.011 | +1026.28€ | 1 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 3477 | +0.263 | +3513.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 3477 | +0.263 | +3513.67€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 3968 | -0.002 | +723.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 3968 | -0.002 | +723.87€ | 2 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 4002 | +0.024 | +1491.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 4002 | +0.024 | +1491.30€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 3348 | +0.273 | +3537.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 3348 | +0.273 | +3537.17€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 18830 | +0.168 | +13932.07€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 18830 | +0.168 | +13932.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 2822 | +0.207 | +2244.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 2822 | +0.207 | +2244.92€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 2997 | +0.149 | +2157.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 2997 | +0.149 | +2157.15€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 2935 | +0.210 | +2356.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 2935 | +0.210 | +2356.92€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 3149 | +0.135 | +2150.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 3149 | +0.135 | +2150.23€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 3518 | +0.114 | +2351.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 3518 | +0.114 | +2351.03€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 3409 | +0.202 | +2671.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 3409 | +0.202 | +2671.81€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 4613 | +0.122 | +1846.74€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 4613 | +0.122 | +1846.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 184 | +0.118 | +76.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 184 | +0.118 | +76.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1300 | +0.117 | +542.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1300 | +0.117 | +542.32€ | 0 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 369 | +0.147 | +180.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 369 | +0.147 | +180.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1273 | +0.140 | +550.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1273 | +0.140 | +550.56€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 983 | +0.090 | +280.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 983 | +0.090 | +280.16€ | 2 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 504 | +0.134 | +216.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 504 | +0.134 | +216.54€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 23391 | +0.174 | +17213.65€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 23391 | +0.174 | +17213.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 3685 | +0.219 | +3090.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 3685 | +0.219 | +3090.77€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 3664 | +0.149 | +2385.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 3664 | +0.149 | +2385.69€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 3804 | +0.227 | +3300.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 3804 | +0.227 | +3300.40€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 3798 | +0.136 | +2547.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 3798 | +0.136 | +2547.18€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 4114 | +0.109 | +2520.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 4114 | +0.109 | +2520.12€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 4326 | +0.203 | +3369.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 4326 | +0.203 | +3369.50€ | 0 | 23 |
| ✅ GBM_LATE_5M | 6486 | +0.142 | +3575.50€ | 1 | 28 |
| ✅ GBM_LATE_5M#5min | 6486 | +0.142 | +3575.50€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 589 | +0.185 | +410.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 589 | +0.185 | +410.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1685 | +0.141 | +1077.74€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1685 | +0.141 | +1077.74€ | 0 | 27 |
| ✅ GBM_LATE_5M#DOGE | 889 | +0.171 | +564.50€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 889 | +0.171 | +564.50€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 2037 | +0.146 | +1104.81€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2037 | +0.146 | +1104.81€ | 0 | 32 |
| ✅ GBM_LATE_5M#SOL | 467 | +0.069 | +101.36€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 467 | +0.069 | +101.36€ | 0 | 9 |
| ✅ GBM_LATE_5M#XRP | 819 | +0.115 | +316.33€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 819 | +0.115 | +316.33€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1518 | +0.068 | +667.46€ | 2 | 13 |
| ✅ GBM_LATE_60M#60min | 1518 | +0.068 | +667.46€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 546 | +0.088 | +231.98€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 546 | +0.088 | +231.98€ | 0 | 15 |
| ✅ GBM_LATE_60M#ETH | 504 | +0.073 | +265.37€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 504 | +0.073 | +265.37€ | 2 | 18 |
| ✅ GBM_LATE_60M#SOL | 468 | +0.040 | +170.11€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 468 | +0.040 | +170.11€ | 1 | 12 |
| 🚫 GBM_LATE_60M_FADE | 339 | -0.263 | -27.05€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 339 | -0.263 | -27.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 129 | -0.210 | -7.76€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 129 | -0.210 | -7.76€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 112 | -0.281 | -11.47€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 112 | -0.281 | -11.47€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 98 | -0.300 | -7.82€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 98 | -0.300 | -7.82€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 647 | +0.058 | +125.35€ | 2 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 647 | +0.058 | +125.35€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 254 | +0.051 | +45.16€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 254 | +0.051 | +45.16€ | 2 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 189 | +0.029 | -3.13€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 189 | +0.029 | -3.13€ | 2 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 204 | +0.092 | +83.32€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 204 | +0.092 | +83.32€ | 1 | 13 |
| ✅ LATE_WINDOW_5MIN | 87 | +0.264 | +70.88€ | 0 | 4 |
| ✅ LATE_WINDOW_5MIN#5min | 87 | +0.264 | +70.88€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 87 | +0.264 | +70.88€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 87 | +0.264 | +70.88€ | 0 | 4 |
| ✅ LEADLAG_BTC_XRP_15M | 1732 | +0.099 | +470.62€ | 0 | 3 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1732 | +0.099 | +470.62€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1732 | +0.099 | +470.62€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1732 | +0.099 | +470.62€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M | 367 | -0.080 | -33.57€ | 6 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 367 | -0.080 | -33.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 94 | -0.062 | -5.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 94 | -0.062 | -5.45€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 67 | -0.080 | -7.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 67 | -0.080 | -7.45€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 125 | -0.020 | -3.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 125 | -0.020 | -3.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 1766 | +0.007 | +16.07€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1766 | +0.007 | +16.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 95 | -0.005 | -3.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 95 | -0.005 | -3.44€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 190 | +0.000 | +12.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 190 | +0.000 | +12.06€ | 2 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 124 | -0.032 | -5.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 124 | -0.032 | -5.20€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 748 | +0.033 | +26.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 748 | +0.033 | +26.62€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 465 | -0.003 | -6.48€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 465 | -0.003 | -6.48€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 144 | -0.048 | -7.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 144 | -0.048 | -7.49€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 1007 | -0.045 | -26.74€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1007 | -0.045 | -26.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 289 | -0.043 | -12.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 289 | -0.043 | -12.32€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 332 | -0.033 | -3.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 332 | -0.033 | -3.53€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 386 | -0.057 | -10.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 386 | -0.057 | -10.89€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M | 14132 | -0.013 | -215.57€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14132 | -0.013 | -215.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 2849 | -0.025 | -68.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 2849 | -0.025 | -68.75€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 26161 | -0.008 | +1152.81€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 26161 | -0.008 | +1152.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 4591 | +0.015 | +576.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 4591 | +0.015 | +576.16€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 4117 | -0.026 | -41.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 4117 | -0.026 | -41.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 4625 | +0.012 | +397.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 4625 | +0.012 | +397.88€ | 3 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 3892 | -0.052 | -137.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 3892 | -0.052 | -137.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 4375 | -0.012 | +165.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 4375 | -0.012 | +165.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 4561 | +0.005 | +191.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 4561 | +0.005 | +191.60€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 5525 | -0.054 | -134.48€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 5525 | -0.054 | -134.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1203 | +0.000 | -15.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1203 | +0.000 | -15.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1288 | -0.073 | -33.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1288 | -0.073 | -33.27€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 564 | -0.122 | -22.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 564 | -0.122 | -22.51€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1580 | -0.074 | -32.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1580 | -0.074 | -32.01€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 847 | -0.016 | -25.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 847 | -0.016 | -25.72€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3343 | +0.005 | -1.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3343 | +0.005 | -1.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 189 | +0.013 | -1.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 189 | +0.013 | -1.05€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1315 | +0.007 | +7.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1315 | +0.007 | +7.70€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1388 | +0.007 | +0.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1388 | +0.007 | +0.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 66790 | -0.073 | +1517.78€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 66790 | -0.073 | +1517.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 11261 | -0.080 | +650.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 11261 | -0.080 | +650.82€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 10348 | -0.093 | -468.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 10348 | -0.093 | -468.15€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 11410 | -0.069 | +614.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 11410 | -0.069 | +614.66€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 9876 | -0.093 | -176.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 9876 | -0.093 | -176.94€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 12264 | -0.049 | +346.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 12264 | -0.049 | +346.58€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 11631 | -0.062 | +550.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 11631 | -0.062 | +550.81€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6912 | -0.024 | -103.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6912 | -0.024 | -103.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1617 | -0.025 | -3.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1617 | -0.025 | -3.53€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1002 | -0.020 | -30.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1002 | -0.020 | -30.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1536 | -0.020 | -9.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1536 | -0.020 | -9.47€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1023 | -0.040 | -16.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1023 | -0.040 | -16.69€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 738 | -0.020 | -23.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 738 | -0.020 | -23.52€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1080 | +0.108 | +361.13€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#5min | 944 | +0.115 | +348.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 218 | +0.136 | +107.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 218 | +0.136 | +107.53€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#DOGE | 186 | +0.096 | +44.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 186 | +0.096 | +44.24€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 190 | +0.094 | +59.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 190 | +0.094 | +59.73€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#SOL | 165 | +0.141 | +80.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 165 | +0.141 | +80.87€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 185 | +0.104 | +56.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 185 | +0.104 | +56.17€ | 0 | 5 |
| ✅ ORDER_FLOW_5M_REACTIVO | 380 | -0.044 | -32.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 380 | -0.044 | -32.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 80 | +0.037 | +9.75€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 80 | +0.037 | +9.75€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 50 | -0.115 | -13.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 50 | -0.115 | -13.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 108 | -0.073 | -19.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 108 | -0.073 | -19.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 74 | +0.000 | +2.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 74 | +0.000 | +2.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 68 | -0.086 | -11.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 68 | -0.086 | -11.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 528 | -0.094 | -27.18€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 241 | -0.138 | -47.77€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 193 | -0.182 | -50.46€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 48 | +0.040 | +2.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 183 | -0.084 | +1.67€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 139 | -0.096 | -6.48€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 44 | -0.043 | +8.15€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 104 | -0.009 | +18.92€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 82 | -0.024 | +12.23€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 22 | +0.042 | +6.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 414 | -0.123 | -44.71€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 114 | +0.009 | +17.52€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 653 | -0.210 | -35.95€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 268 | -0.200 | -30.73€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 231 | -0.195 | -30.34€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 37 | -0.218 | -0.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 229 | -0.227 | -23.00€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 197 | -0.239 | -27.66€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 32 | -0.147 | +4.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 156 | -0.196 | +17.78€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 140 | -0.197 | +13.11€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 16 | -0.133 | +4.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 568 | -0.212 | -44.89€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 85 | -0.190 | +8.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 256 | +0.415 | +207.32€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#BTC | 28 | +0.033 | -4.76€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 28 | +0.033 | -4.76€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 65 | +0.396 | +60.03€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 65 | +0.396 | +60.03€ | 0 | 3 |
| ✅ RESOLUTION_SNIPER#SOL | 163 | +0.482 | +152.04€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 163 | +0.482 | +152.04€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#sniper | 256 | +0.415 | +207.32€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 457 | +0.032 | +15.48€ | 3 | 2 |
| ✅ STREAK_FADE_15M#15min | 457 | +0.032 | +15.48€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 215 | +0.030 | +3.83€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 215 | +0.030 | +3.83€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 27 | +0.086 | +3.10€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 27 | +0.086 | +3.10€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 48 | -0.020 | -3.52€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 48 | -0.020 | -3.52€ | 1 | 0 |
| ✅ STREAK_FADE_15M#XRP | 167 | +0.038 | +12.06€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 167 | +0.038 | +12.06€ | 1 | 3 |
| ✅ STREAK_FADE_5M | 2638 | -0.024 | -114.15€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2638 | -0.024 | -114.15€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 565 | -0.022 | -22.81€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 565 | -0.022 | -22.81€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 155 | -0.048 | -14.93€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 155 | -0.048 | -14.93€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1114 | -0.026 | -49.47€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1114 | -0.026 | -49.47€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 67 | -0.051 | -6.33€ | 2 | 0 |
| ✅ STREAK_FADE_60M#60min | 67 | -0.051 | -6.33€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 37 | -0.090 | -3.93€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 37 | -0.090 | -3.93€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 30 | +0.000 | -2.40€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 30 | +0.000 | -2.40€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 7322 | +0.023 | +110.45€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 7322 | +0.023 | +110.45€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2121 | +0.021 | +20.90€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2121 | +0.021 | +20.90€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1596 | +0.034 | +47.64€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1596 | +0.034 | +47.64€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2226 | +0.013 | +4.41€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2226 | +0.013 | +4.41€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1379 | +0.031 | +37.50€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1379 | +0.031 | +37.50€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 6843 | +0.010 | -53.66€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 6843 | +0.010 | -53.66€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2731 | +0.014 | -13.44€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2731 | +0.014 | -13.44€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2685 | +0.011 | -17.96€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2685 | +0.011 | -17.96€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1427 | -0.000 | -22.25€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1427 | -0.000 | -22.25€ | 2 | 0 |
| ✅ UPDOWN_GBM | 32637 | +0.030 | +1917.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 8749 | +0.062 | +1511.94€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 1206 | +0.005 | +8.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 20581 | +0.022 | +377.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 1974 | +0.008 | +21.40€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 3096 | +0.069 | +328.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 462 | +0.153 | +187.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 23 | -0.020 | -0.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 2611 | +0.054 | +141.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 6080 | +0.032 | +393.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1103 | +0.078 | +241.49€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 334 | +0.021 | +7.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 3710 | +0.029 | +128.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 884 | +0.003 | +15.27€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 49 | -0.108 | +0.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 3818 | +0.041 | +219.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 434 | +0.144 | +164.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 18 | +0.000 | -0.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 3366 | +0.028 | +54.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 6911 | +0.019 | +277.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 2313 | +0.044 | +252.92€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 322 | +0.006 | +7.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 3556 | +0.008 | +14.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 679 | +0.007 | -0.45€ | 2 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 41 | -0.151 | +3.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 7942 | +0.017 | +203.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2221 | +0.022 | +137.51€ | 0 | 12 |
| ✅ UPDOWN_GBM#SOL#240min | 316 | -0.006 | -3.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 4959 | +0.016 | +65.71€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 411 | +0.021 | +6.59€ | 0 | 2 |
| ✅ UPDOWN_GBM#SOL#daily | 35 | -0.176 | -2.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 4788 | +0.035 | +497.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2216 | +0.077 | +527.67€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 193 | -0.003 | -2.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 2379 | -0.002 | -27.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 125 | -0.146 | +0.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 508 | +0.337 | +147.38€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 508 | +0.337 | +147.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 286 | +0.340 | +79.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 286 | +0.340 | +79.72€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 222 | +0.330 | +67.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 222 | +0.330 | +67.67€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 10768 | -0.044 | +2253.99€ | 3 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 10768 | -0.044 | +2253.99€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 626 | -0.045 | +333.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 626 | -0.045 | +333.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2025 | -0.124 | +39.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2025 | -0.124 | +39.85€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 265 | +0.163 | +157.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 265 | +0.163 | +157.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1184 | +0.201 | +682.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1184 | +0.201 | +682.10€ | 2 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 3327 | -0.064 | +522.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 3327 | -0.064 | +522.35€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 3341 | -0.079 | +519.50€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 3341 | -0.079 | +519.50€ | 3 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 127 | +0.050 | +9.69€ | 2 | 2 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 127 | +0.050 | +9.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 127 | +0.050 | +9.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 127 | +0.050 | +9.69€ | 2 | 2 |
| ✅ UPDOWN_GBM_IBS_ALTO | 823 | +0.291 | +669.27€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 823 | +0.291 | +669.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 455 | +0.286 | +346.68€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 455 | +0.286 | +346.68€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 368 | +0.297 | +322.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 368 | +0.297 | +322.59€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 704 | -0.106 | -79.18€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 704 | -0.106 | -79.18€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 197 | -0.063 | -11.26€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 197 | -0.063 | -11.26€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 69 | -0.162 | -8.81€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 69 | -0.162 | -8.81€ | 3 | 0 |
| 🚫 UPDOWN_OU_5M#SOL | 60 | -0.210 | -9.56€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#SOL#5min | 60 | -0.210 | -9.56€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 2223 | +0.300 | +1106.87€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 761 | +0.248 | +106.26€ | 0 | 5 |
| ✅ WEEKLY_PRICE#ETH | 820 | +0.288 | +332.38€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 642 | +0.376 | +668.23€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.023 n=430 — no justifica filtro, seguir monitorizando
  - _Datos_: n=430 IC=+0.023 PNL=+23.10€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 505 celda(s) pasan gate riguroso completo de 2145 evaluadas (n>=40) y 3153 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.022 < 0.08 — monitorear
  - _Datos_: n=2219 IC=+0.022 PNL=+137.53€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=820/15 IC=+0.288 PNL=+332.38€ | BTC: n=761/15 IC=+0.248 PNL=+106.26€ | SOL: n=642/15 IC=+0.376 PNL=+668.23€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 29 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
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
  - _Estado_: alineada_con_outcome_prev IC=+0.093 n=246/60 | contraria IC=+0.143 n=236 | gap=-0.050 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=268, boost estimado=+0.008. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=677/40 IC=+0.007 PNL=-0.39€ | BTC#60min: n=882/40 IC=+0.003 PNL=+14.93€ | SOL#60min: n=411/40 IC=+0.021 PNL=+6.59€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.052 n=306174 | tras_1loss IC=+0.076 n=238354 | tras_2loss IC=+0.044 n=101085/40 | gap=+0.008 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.179 > 0.08 con n=294 PNL=+187.59€
  - _Datos_: n=294 IC=+0.179 PNL=+187.59€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.217 > 0.08 con n=344 PNL=+246.62€
  - _Datos_: n=344 IC=+0.217 PNL=+246.62€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.269 > 0.08 con n=37 PNL=+31.71€
  - _Datos_: n=37 IC=+0.269 PNL=+31.71€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.331 > 0.1 con n=1845 PNL=+1054.70€
  - _Datos_: n=1845 IC=+0.331 PNL=+1054.70€

**🟡 H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.083 > 0.08 con n=250 PNL=+33.14€
  - _Datos_: n=250 IC=+0.083 PNL=+33.14€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=49 IC=+0.186 PNL=+32.29€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=49 IC=+0.186 PNL=+32.29€

**⏳ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: 30
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 3/15 ops en el filtro definido (IC actual=+0.045 PNL=+5.14€)
  - _Datos_: n=3 IC=+0.045 PNL=+5.14€

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
  - _Estado_: n=1427 IC=+0.018 PNL=+16.04€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1427 IC=+0.018 PNL=+16.04€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=543 IC=-0.019 PNL=+5.10€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=543 IC=-0.019 PNL=+5.10€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=430 IC=+0.023 PNL=+23.10€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=430 IC=+0.023 PNL=+23.10€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.185 > 0.1 con n=1889 PNL=+1162.90€
  - _Datos_: n=1889 IC=+0.185 PNL=+1162.90€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1102 IC=+0.078 PNL=+241.01€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1102 IC=+0.078 PNL=+241.01€

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
  - _Estado_: n=482 IC=+0.012 PNL=+33.84€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=482 IC=+0.012 PNL=+33.84€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=43 IC=+0.056 PNL=+2.44€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=43 IC=+0.056 PNL=+2.44€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.264 n=87) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=87 IC=+0.264 PNL=+70.88€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.125 > 0.02 con n=619 PNL=+242.46€
  - _Datos_: n=619 IC=+0.125 PNL=+242.46€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=147 IC=-0.044 PNL=+35.89€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=147 IC=-0.044 PNL=+35.89€

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
  - _Estado_: n=11295 IC=+0.057 PNL=+1397.79€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=11295 IC=+0.057 PNL=+1397.79€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.167 < -0.1 con n=208 PNL=+17.28€
  - _Datos_: n=208 IC=-0.167 PNL=+17.28€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=1701 IC=+0.045 PNL=+182.43€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1701 IC=+0.045 PNL=+182.43€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=68 IC=-0.143 PNL=+2.20€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=68 IC=-0.143 PNL=+2.20€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.130 > 0.1 con n=347 PNL=+104.47€
  - _Datos_: n=347 IC=+0.130 PNL=+104.47€

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
  - _Estado_: n=16116 IC=-0.137 PNL=+1136.70€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=16116 IC=-0.137 PNL=+1136.70€

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
  - _Estado_: n=1759 IC=+0.136 PNL=+932.67€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1759 IC=+0.136 PNL=+932.67€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=3406 IC=+0.018 PNL=+107.38€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3406 IC=+0.018 PNL=+107.38€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.085 > 0.08 con n=1885 PNL=+981.47€
  - _Datos_: n=1885 IC=+0.085 PNL=+981.47€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.241 < -0.1 con n=1588 PNL=-194.45€
  - _Datos_: n=1588 IC=-0.241 PNL=-194.45€

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

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 33/40 ops en el filtro definido (IC actual=-0.043 PNL=+2.97€)
  - _Datos_: n=33 IC=-0.043 PNL=+2.97€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.091 n=891) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=891 IC=+0.091 PNL=+209.04€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.411 n=426) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=426 IC=+0.411 PNL=+599.27€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=8109 IC=+0.175 PNL=-953.20€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=8109 IC=+0.175 PNL=-953.20€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.205 > 0.1 con n=127 PNL=+76.45€
  - _Datos_: n=127 IC=+0.205 PNL=+76.45€
