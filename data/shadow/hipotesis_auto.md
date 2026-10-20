# Hipótesis automáticas — 2026-10-20 23:29 UTC
_Generado por shadow_postmortem.py sobre 986005 resoluciones (PNL=+128721.48€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.255 (n=194)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=627)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.237 (n=788)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.139)

- **PATRÓN** `n_total_lado` > `65.0` → IC=+0.182 (n=284)

  - _Acción_: Kelly boost +0.91€ cuando `n_total_lado` > 65.0 (IC base=+0.139)

- **PATRÓN** `banda_hit_calibrado` > `0.7972` → IC=+0.271 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7972 (IC base=+0.139)

- **PATRÓN** `banda_z` > `9.189` → IC=+0.205 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.189 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=910)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `2653.7599` → IC=+0.139 (n=746)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2653.7599 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.154 (n=458)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 98.0 (IC base=+0.139)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.545` → IC=+0.272 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.545 (IC base=+0.144)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.199 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.144)

- **PATRÓN** `banda_hit_calibrado` > `0.6174` → IC=+0.265 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6174 (IC base=+0.144)

- **PATRÓN** `banda_z` > `9.588` → IC=+0.209 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.588 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.186 (n=256)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=811)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.156 (n=420)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 100.0 (IC base=+0.144)

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
  - _Potencial_: sin este filtro IC_bueno=+0.124 (n=107)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.124 (n=107)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.495 (IC base=+0.011)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 79.0 (IC base=+0.011)

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
- **FILTRO** `restante_s_al_confirmar` < `142.41` → IC=-0.203 (n=10081)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 142.41
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=30248)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `128.8` → IC=-0.261 (n=1124)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.8
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=3374)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `121.52` → IC=-0.287 (n=1080)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 121.52
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=3243)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `167.27` → IC=-0.205 (n=2663)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 167.27
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=7990)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `133.28` → IC=-0.275 (n=1968)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.28
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=5907)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.214 (n=21774)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.108)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=4333)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `9119.7631` → IC=+0.176 (n=1960)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 9119.7631 (IC base=+0.108)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.130 (n=18531)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.129 (n=33130)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 11.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.227 (n=17274)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.149 (n=7207)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `7070.6627` → IC=+0.158 (n=2785)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 7070.6627 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.199 (n=2029)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.192 (n=1982)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 17.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.364 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.194 (n=2488)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `16419.986` → IC=+0.200 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16419.986 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.190 (n=1786)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 7.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.188 (n=1986)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 17.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.186 (n=2547)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `16193.8223` → IC=+0.195 (n=657)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 16193.8223 (IC base=+0.184)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.170 (n=470)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.61 (IC base=+0.081)

- **PATRÓN** `libro_liquidez` > `6857.6712` → IC=+0.167 (n=124)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 6857.6712 (IC base=+0.081)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.139 (n=1124)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.44 (IC base=+0.084)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=4223)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.162 (n=3574)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 15.0 (IC base=+0.161)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.371 (n=1383)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.226 (n=780)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.347 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.213 (n=2190)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.210)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=1065)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.149 (n=687)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 11.0 (IC base=+0.143)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.263 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=832)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `2205.3811` → IC=+0.161 (n=461)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2205.3811 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.162 (n=152)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.069)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.254 (n=844)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.419 (n=1152)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.150 (n=1290)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.159 (n=678)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 7.0 (IC base=+0.149)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.285 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=855)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.149)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `9.0` → IC=+0.170 (n=319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 9.0 (IC base=+0.154)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.347 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.145 (n=201)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.136 (n=1134)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 7.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.245 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.123)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `11.0` → IC=-0.297 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.206 (n=18399)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.203 (n=15552)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.235 (n=7576)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.201)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.183 (n=4012)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 6.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.182 (n=4215)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 18.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.184 (n=4139)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.73 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.181 (n=3460)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.224 (n=2176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.227 (n=2274)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.305 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.222)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=4171)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.184 (n=3535)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 15.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.188 (n=3268)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.258 (n=3619)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.248)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.361 (n=1166)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=4085)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=3483)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.194 (n=3013)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.190)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.432 (n=783)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.427)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.441 (n=808)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.427)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.427)

- **PATRÓN** `libro_liquidez` > `4188.4622` → IC=+0.438 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4188.4622 (IC base=+0.427)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.432 (n=307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.433)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.442 (n=204)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.447 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.433)

- **PATRÓN** `libro_liquidez` > `20878.8113` → IC=+0.442 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 20878.8113 (IC base=+0.433)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.449 (n=215)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.433)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.437 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.433)

- **PATRÓN** `libro_liquidez` > `4484.2424` → IC=+0.442 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4484.2424 (IC base=+0.433)

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

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.212 (n=20560)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=24068)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.196 (n=3549)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.188 (n=7588)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 12.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.201 (n=10682)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.186)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=4995)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.227 (n=4872)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.286 (n=3489)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.191 (n=4102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.211 (n=5452)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.182)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.234 (n=3347)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.223 (n=3805)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.278 (n=3397)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.206 (n=9163)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.261 (n=3545)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=3983)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=3976)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.248 (n=4142)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=8674)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=8497)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.76` → IC=+0.136 (n=10393)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.76 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=4290)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.143 (n=4339)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.130 (n=4540)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 6.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `2.76` → IC=+0.146 (n=3915)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.76 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.189 (n=4384)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.135 (n=4628)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `3.33` → IC=+0.134 (n=5233)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 3.33 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.301 (n=1664)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.293 (n=1634)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.382 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.293)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.287 (n=755)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.280)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.356 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `5028.8269` → IC=+0.290 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5028.8269 (IC base=+0.280)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.321 (n=539)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.301 (n=787)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.297)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.391 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.297)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.298 (n=657)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.297)

- **PATRÓN** `libro_liquidez` > `2113.1713` → IC=+0.312 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2113.1713 (IC base=+0.297)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.357 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.351)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.377 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.351)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.391 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.351)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.356 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.351)

- **PATRÓN** `libro_liquidez` > `761.0655` → IC=+0.378 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 761.0655 (IC base=+0.351)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.446 (n=769)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.442 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.446 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.443 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.442)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.438 (n=366)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.440 (n=247)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.436 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.442 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.436)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.469 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.449)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.452 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.449)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.451 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.449)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.450 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.449)

- **PATRÓN** `libro_liquidez` > `1978.9685` → IC=+0.468 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1978.9685 (IC base=+0.449)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4766` → IC=+0.139 (n=13375)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.4766 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.125 (n=13550)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.124 (n=9312)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.3784` → IC=+0.166 (n=13375)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.3784 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.783` → IC=+0.269 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.783 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` < `0.2135` → IC=+0.258 (n=3266)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2135 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.91` → IC=+0.191 (n=5064)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 5.91 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.2036` → IC=+0.259 (n=3890)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2036 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6192` → IC=+0.265 (n=3888)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6192 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.3025` → IC=+0.242 (n=1360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3025 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.3455` → IC=+0.229 (n=4314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3455 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.125 (n=7118)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.6853` → IC=+0.129 (n=18697)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.6853 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` < `0.6954` → IC=+0.186 (n=2817)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6954 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.0502` → IC=+0.182 (n=2904)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.0502 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2955` → IC=+0.234 (n=1598)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2955 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.676` → IC=+0.207 (n=3631)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.676 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.221 (n=10747)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 106.0 (IC base=+0.075)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.210 (n=977)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.3476` → IC=+0.205 (n=2909)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3476 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.211 (n=1421)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.203 (n=1116)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.9802` → IC=+0.280 (n=1319)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9802 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.873` → IC=+0.283 (n=1273)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.873 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2333` → IC=+0.249 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2333 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.44` → IC=+0.202 (n=2772)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.44 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=3119)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `2077.12` → IC=+0.207 (n=970)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2077.12 (IC base=+0.200)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.218 (n=1744)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.239 (n=2438)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.237 (n=1105)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0077 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.0872` → IC=+0.272 (n=812)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0872 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.253 (n=893)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.5307` → IC=+0.258 (n=2434)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5307 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.0944` → IC=+0.239 (n=2182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0944 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.287` → IC=+0.261 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.287 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.4379` → IC=+0.242 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4379 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.6589` → IC=+0.244 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6589 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.240 (n=2738)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1628.38` → IC=+0.246 (n=2175)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1628.38 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.240 (n=809)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.237)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.239 (n=1054)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.228)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.230 (n=1081)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.228)

- **PATRÓN** `drift_60min` |x|≤ `0.106` → IC=+0.261 (n=1049)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.106 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.239 (n=2502)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.228 (n=1686)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `0.9506` → IC=+0.276 (n=794)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9506 (IC base=+0.228)

- **PATRÓN** `dist_vwap_pct` > `0.1298` → IC=+0.233 (n=1281)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1298 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.335` → IC=+0.265 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.335 (IC base=+0.228)

- **PATRÓN** `volumen_regimen` < `1.2317` → IC=+0.229 (n=2383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2317 (IC base=+0.228)

- **PATRÓN** `volumen_regimen` > `0.6225` → IC=+0.232 (n=2382)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6225 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.2776` → IC=+0.265 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2776 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` < `1.5102` → IC=+0.228 (n=1033)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5102 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `2.4426` → IC=+0.255 (n=782)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4426 (IC base=+0.228)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.152 (n=2425)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0057 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.167 (n=811)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.154 (n=923)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.7268` → IC=+0.177 (n=2425)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.7268 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.992` → IC=+0.149 (n=391)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 10.992 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.177` → IC=+0.141 (n=2217)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 4.177 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `1.2042` → IC=+0.140 (n=2425)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.2042 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.0961` → IC=+0.158 (n=884)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.0961 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.4537` → IC=+0.144 (n=2305)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4537 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.4138` → IC=+0.135 (n=2304)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4138 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `217.0` → IC=+0.175 (n=982)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 217.0 (IC base=+0.133)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.223 (n=1012)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=3178)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.272 (n=1156)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.287` → IC=+0.275 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.287 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.201 (n=2680)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.353` → IC=+0.214 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.353 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `2.6967` → IC=+0.212 (n=1330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6967 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.203 (n=3616)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `1973.5984` → IC=+0.202 (n=1371)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1973.5984 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.225 (n=2386)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.461` → IC=+0.225 (n=2384)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.461 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=1020)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.218 (n=1243)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.0173` → IC=+0.276 (n=903)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0173 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.391` → IC=+0.247 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.391 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3473` → IC=+0.260 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3473 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.719` → IC=+0.229 (n=1167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.719 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.221 (n=1426)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `2051.6413` → IC=+0.223 (n=903)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2051.6413 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.222 (n=2233)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.142 (n=149)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=3664)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.162 (n=540)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0037 (IC base=+0.055)

- **PATRÓN** `ibs_20min` > `0.9529` → IC=+0.230 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9529 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` > `0.1401` → IC=+0.329 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1401 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` < `0.19` → IC=+0.329 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.19 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.12` → IC=+0.189 (n=1162)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 5.12 (IC base=+0.055)

- **PATRÓN** `volumen_regimen` < `0.8578` → IC=+0.335 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8578 (IC base=+0.055)

- **PATRÓN** `volumen_regimen` > `1.2208` → IC=+0.344 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2208 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.2964` → IC=+0.351 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2964 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` < `1.4107` → IC=+0.349 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4107 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` > `2.21` → IC=+0.330 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.21 (IC base=+0.055)

- **PATRÓN** `ballena_activa_n` < `132.0` → IC=+0.337 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 132.0 (IC base=+0.055)

- **PATRÓN** `ibs_20min` < `0.093` → IC=+0.174 (n=954)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.093 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` > `0.3288` → IC=+0.143 (n=458)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.3288 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` < `0.1308` → IC=+0.139 (n=1557)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1308 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` < `0.8415` → IC=+0.149 (n=1130)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8415 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` > `1.1679` → IC=+0.140 (n=565)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 1.1679 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.2852` → IC=+0.202 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2852 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `1.7769` → IC=+0.139 (n=1082)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.7769 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` > `2.1533` → IC=+0.153 (n=736)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.1533 (IC base=+0.035)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.170 (n=104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=558)

- **FILTRO** `ibs_20min` < `0.2759` → IC=-0.193 (n=164)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2759
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=498)

- **FILTRO** `ibs_20min` > `0.2167` → IC=-0.132 (n=3591)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2167
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=1770)

- **FILTRO** `sigma_ewma_delta_pct` > `8.666` → IC=-0.237 (n=561)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.666
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=4800)

- **PATRÓN** `ibs_20min` > `0.7857` → IC=+0.184 (n=226)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.7857 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` > `1.0155` → IC=+0.279 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0155 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` < `0.4892` → IC=+0.263 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4892 (IC base=+0.032)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.146` → IC=+0.151 (n=210)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 3.146 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` > `1.0155` → IC=+0.306 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0155 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` < `0.1553` → IC=+0.279 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1553 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` < `2.1989` → IC=+0.290 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1989 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` > `1.5481` → IC=+0.262 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5481 (IC base=+0.032)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.265 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.032)

- **PATRÓN** `ibs_20min` < `0.2167` → IC=+0.147 (n=1770)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.2167 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` > `0.1911` → IC=+0.277 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1911 (IC base=-0.040)

- **PATRÓN** `volumen_regimen` < `0.704` → IC=+0.303 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.704 (IC base=-0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.0806` → IC=+0.304 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0806 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` < `2.43` → IC=+0.300 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.43 (IC base=-0.040)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6099` → IC=-0.178 (n=982)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6099
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=2952)

- **FILTRO** `ibs_20min` < `0.754` → IC=-0.150 (n=2596)

  - _Acción_: SKIP cuando `ibs_20min` < 0.754
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=1338)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.161 (n=960)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=2974)

- **FILTRO** `ibs_20min` > `0.75` → IC=-0.204 (n=1413)

  - _Acción_: SKIP cuando `ibs_20min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=4253)

- **PATRÓN** `dist_vwap_pct` > `0.7127` → IC=+0.336 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7127 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` < `0.2524` → IC=+0.303 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2524 (IC base=-0.066)

- **PATRÓN** `volumen_regimen` < `1.1484` → IC=+0.298 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1484 (IC base=-0.066)

- **PATRÓN** `volumen_regimen` > `0.704` → IC=+0.317 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.704 (IC base=-0.066)

- **PATRÓN** `volumen_pendiente_norm` < `0.0999` → IC=+0.301 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0999 (IC base=-0.066)

- **PATRÓN** `volumen_pendiente_norm` > `0.0729` → IC=+0.307 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0729 (IC base=-0.066)

- **PATRÓN** `volumen_spike_ratio` < `1.4187` → IC=+0.318 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4187 (IC base=-0.066)

- **PATRÓN** `volumen_spike_ratio` > `1.8376` → IC=+0.310 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8376 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` > `0.803` → IC=+0.274 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.803 (IC base=-0.006)

- **PATRÓN** `volumen_regimen` > `1.0685` → IC=+0.283 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0685 (IC base=-0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.1041` → IC=+0.281 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1041 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` < `2.1803` → IC=+0.264 (n=1258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1803 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` > `1.4298` → IC=+0.264 (n=1430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4298 (IC base=-0.006)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.210 (n=5864)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.3208` → IC=+0.169 (n=17588)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.3208 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.9516` → IC=+0.300 (n=1295)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9516 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.592` → IC=+0.162 (n=7890)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 3.592 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `1.1704` → IC=+0.265 (n=6479)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1704 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `0.6886` → IC=+0.270 (n=5788)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6886 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.2394` → IC=+0.279 (n=1930)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2394 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `1.4587` → IC=+0.263 (n=3447)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4587 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `2.6418` → IC=+0.272 (n=3447)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6418 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.296 (n=9909)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 91.0 (IC base=+0.096)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.157 (n=5645)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0093 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.6579` → IC=+0.144 (n=16912)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.6579 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.7049` → IC=+0.263 (n=2349)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7049 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.1953` → IC=+0.266 (n=1780)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1953 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2947` → IC=+0.316 (n=1145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2947 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.5797` → IC=+0.290 (n=3371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5797 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.2663` → IC=+0.283 (n=3473)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2663 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.295 (n=7602)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 77.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.581` → IC=-0.128 (n=2414)

  - _Acción_: SKIP cuando `ibs_20min` < 0.581
  - _Potencial_: sin este filtro IC_bueno=+0.189 (n=2414)

- **FILTRO** `ibs_20min` > `0.7415` → IC=-0.214 (n=1015)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7415
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=3049)

- **FILTRO** `sigma_ewma_delta_pct` > `4.372` → IC=-0.207 (n=890)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.372
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=3174)

- **PATRÓN** `ibs_20min` > `0.9192` → IC=+0.314 (n=1207)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9192 (IC base=+0.031)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.0` → IC=+0.215 (n=855)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.0 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.2287` → IC=+0.303 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2287 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` < `1.4419` → IC=+0.256 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4419 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` > `2.2427` → IC=+0.274 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2427 (IC base=+0.031)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.281 (n=1067)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.031)

- **PATRÓN** `ibs_20min` < `0.1638` → IC=+0.160 (n=1017)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1638 (IC base=-0.029)

- **PATRÓN** `volumen_pendiente_norm` < `0.0724` → IC=+0.414 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0724 (IC base=-0.029)

- **PATRÓN** `volumen_spike_ratio` < `2.5496` → IC=+0.408 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5496 (IC base=-0.029)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.402 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=-0.029)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1147` → IC=+0.213 (n=875)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1147 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `1.195` → IC=+0.193 (n=1713)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 1.195 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `0.6829` → IC=+0.202 (n=1530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6829 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.276` → IC=+0.233 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.276 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `1.4226` → IC=+0.217 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4226 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` > `2.4876` → IC=+0.194 (n=563)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.4876 (IC base=+0.022)

- **PATRÓN** `ballena_activa_n` < `273.0` → IC=+0.229 (n=1123)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 273.0 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `0.6195` → IC=+0.234 (n=1098)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6195 (IC base=-0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2721` → IC=+0.287 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2721 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.5339` → IC=+0.239 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5339 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.1623` → IC=+0.246 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1623 (IC base=-0.004)

- **PATRÓN** `ballena_activa_n` < `201.0` → IC=+0.241 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 201.0 (IC base=-0.004)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.311 (n=855)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.274 (n=2694)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.267)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.310 (n=1349)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.267)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.287` → IC=+0.302 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.287 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` < `0.0977` → IC=+0.281 (n=2232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0977 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` > `3.2041` → IC=+0.282 (n=827)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2041 (IC base=+0.267)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.278 (n=3049)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.267)

- **PATRÓN** `libro_liquidez` > `2053.9739` → IC=+0.285 (n=855)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2053.9739 (IC base=+0.267)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.282 (n=1544)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.267)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.325 (n=1007)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.1816` → IC=+0.310 (n=976)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1816 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.319 (n=850)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.293)

- **PATRÓN** `ibs_20min` < `0.3704` → IC=+0.296 (n=2218)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3704 (IC base=+0.293)

- **PATRÓN** `ibs_20min` > `0.2604` → IC=+0.299 (n=1005)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2604 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.552` → IC=+0.309 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.552 (IC base=+0.293)

- **PATRÓN** `volumen_pendiente_norm` < `0.1976` → IC=+0.291 (n=2168)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1976 (IC base=+0.293)

- **PATRÓN** `volumen_pendiente_norm` > `0.3416` → IC=+0.308 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3416 (IC base=+0.293)

- **PATRÓN** `volumen_spike_ratio` < `1.7295` → IC=+0.298 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7295 (IC base=+0.293)

- **PATRÓN** `volumen_spike_ratio` > `2.6617` → IC=+0.302 (n=960)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6617 (IC base=+0.293)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.294 (n=1170)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `2044.5699` → IC=+0.308 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2044.5699 (IC base=+0.293)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.294 (n=1432)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.293)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7377` → IC=-0.188 (n=1064)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7377
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=3195)

- **PATRÓN** `ibs_20min` > `0.8775` → IC=+0.173 (n=1011)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.8775 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` > `0.1544` → IC=+0.236 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1544 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.2167` → IC=+0.233 (n=1207)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2167 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` < `1.0074` → IC=+0.245 (n=1247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0074 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` > `0.6697` → IC=+0.233 (n=1266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6697 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.1022` → IC=+0.255 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1022 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` < `1.398` → IC=+0.245 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.398 (IC base=+0.030)

- **PATRÓN** `ballena_activa_n` < `103.0` → IC=+0.267 (n=1235)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 103.0 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.1951` → IC=+0.232 (n=972)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1951 (IC base=-0.002)

- **PATRÓN** `volumen_regimen` < `1.0308` → IC=+0.238 (n=862)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0308 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` < `0.1012` → IC=+0.249 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1012 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.289 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.7947` → IC=+0.271 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7947 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.4356` → IC=+0.253 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4356 (IC base=-0.002)

- **PATRÓN** `ballena_activa_n` < `125.0` → IC=+0.260 (n=944)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 125.0 (IC base=-0.002)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7619` → IC=-0.214 (n=1854)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7619
  - _Potencial_: sin este filtro IC_bueno=+0.307 (n=1854)

- **FILTRO** `ibs_20min` > `0.6475` → IC=-0.236 (n=904)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6475
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=2715)

- **FILTRO** `sigma_ewma_delta_pct` > `8.508` → IC=-0.245 (n=421)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.508
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=3198)

- **PATRÓN** `ibs_20min` > `0.7619` → IC=+0.307 (n=1854)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7619 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` > `0.2157` → IC=+0.338 (n=824)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2157 (IC base=+0.046)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.527` → IC=+0.185 (n=576)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 9.527 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` < `0.8446` → IC=+0.336 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8446 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` > `0.7023` → IC=+0.327 (n=1243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7023 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` < `0.1585` → IC=+0.324 (n=1439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1585 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.352 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` < `1.4368` → IC=+0.350 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4368 (IC base=+0.046)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.342 (n=1201)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.046)

- **PATRÓN** `ibs_20min` < `0.6475` → IC=+0.120 (n=2715)

  - _Acción_: Kelly boost +0.60€ cuando `ibs_20min` < 0.6475 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` < `0.2066` → IC=+0.250 (n=1111)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2066 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` < `0.7014` → IC=+0.262 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7014 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.0762` → IC=+0.263 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0762 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` < `2.4236` → IC=+0.254 (n=1150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4236 (IC base=+0.031)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.270 (n=1167)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.031)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.347 (n=1750)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.304)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.307 (n=764)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.304)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.314 (n=934)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.304)

- **PATRÓN** `ibs_20min` > `0.66` → IC=+0.336 (n=1959)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.66 (IC base=+0.304)

- **PATRÓN** `dist_vwap_pct` > `0.2054` → IC=+0.330 (n=1103)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2054 (IC base=+0.304)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.798` → IC=+0.324 (n=951)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.798 (IC base=+0.304)

- **PATRÓN** `volumen_regimen` > `0.6263` → IC=+0.312 (n=1959)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6263 (IC base=+0.304)

- **PATRÓN** `volumen_pendiente_norm` > `0.2788` → IC=+0.346 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2788 (IC base=+0.304)

- **PATRÓN** `volumen_spike_ratio` > `1.425` → IC=+0.315 (n=1878)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.425 (IC base=+0.304)

- **PATRÓN** `libro_liquidez` > `2626.4292` → IC=+0.311 (n=1306)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2626.4292 (IC base=+0.304)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.337 (n=1682)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.304)

- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.335 (n=1377)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.304)

- **PATRÓN** `drift_60min` |x|≤ `0.1867` → IC=+0.306 (n=909)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1867 (IC base=+0.304)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.315 (n=802)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.304)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.304 (n=1011)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.304)

- **PATRÓN** `ibs_20min` < `0.3675` → IC=+0.328 (n=2065)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3675 (IC base=+0.304)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.345` → IC=+0.318 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.345 (IC base=+0.304)

- **PATRÓN** `volumen_regimen` < `0.7185` → IC=+0.309 (n=911)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7185 (IC base=+0.304)

- **PATRÓN** `volumen_regimen` > `1.2233` → IC=+0.332 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2233 (IC base=+0.304)

- **PATRÓN** `volumen_pendiente_norm` > `0.2838` → IC=+0.352 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2838 (IC base=+0.304)

- **PATRÓN** `volumen_spike_ratio` < `1.4167` → IC=+0.312 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4167 (IC base=+0.304)

- **PATRÓN** `volumen_spike_ratio` > `2.1367` → IC=+0.305 (n=856)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1367 (IC base=+0.304)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.227 (n=4325)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.0873` → IC=+0.202 (n=4327)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0873 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=13482)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.5581` → IC=+0.235 (n=12972)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5581 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.1649` → IC=+0.209 (n=5249)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1649 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.225` → IC=+0.261 (n=2546)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.225 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.1875` → IC=+0.170 (n=8609)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.1875 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` > `0.6238` → IC=+0.165 (n=8609)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6238 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.206 (n=1889)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.61` → IC=+0.192 (n=4192)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.61 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `1978.841` → IC=+0.182 (n=11589)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 1978.841 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `95.0` → IC=+0.199 (n=11905)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 95.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.184 (n=10962)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0091 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.0795` → IC=+0.228 (n=4150)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0795 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=4649)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.237 (n=12458)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.019` → IC=+0.198 (n=2029)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 10.019 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.685` → IC=+0.182 (n=10985)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 2.685 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.1821` → IC=+0.163 (n=8890)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1821 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2939` → IC=+0.225 (n=1842)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2939 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6358` → IC=+0.187 (n=3900)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6358 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.193 (n=11423)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 100.0 (IC base=+0.180)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.236 (n=725)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.3316` → IC=+0.233 (n=2171)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3316 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.219 (n=2275)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.222 (n=1457)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.9275` → IC=+0.295 (n=1448)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9275 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.832` → IC=+0.315 (n=990)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.832 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.2805` → IC=+0.272 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2805 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `1.4364` → IC=+0.215 (n=2054)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4364 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=2349)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.216)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.252 (n=1685)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.250)

- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.263 (n=765)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.250)

- **PATRÓN** `drift_60min` |x|≤ `0.0938` → IC=+0.303 (n=741)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0938 (IC base=+0.250)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.254 (n=1726)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.250)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.254 (n=814)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.250)

- **PATRÓN** `ibs_20min` < `0.2954` → IC=+0.274 (n=1482)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2954 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.252 (n=1471)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` > `0.2974` → IC=+0.290 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2974 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` < `1.4323` → IC=+0.272 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4323 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` > `2.6858` → IC=+0.254 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6858 (IC base=+0.250)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.255 (n=1897)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.250)

- **PATRÓN** `libro_liquidez` > `1529.4134` → IC=+0.259 (n=1683)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1529.4134 (IC base=+0.250)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.255 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.250)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.219 (n=656)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.1598` → IC=+0.183 (n=1305)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1598 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=2064)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.3355` → IC=+0.224 (n=1957)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3355 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.1362` → IC=+0.213 (n=1167)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1362 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.288` → IC=+0.224 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.288 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.6912` → IC=+0.163 (n=861)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.6912 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.195 (n=313)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.5085` → IC=+0.171 (n=845)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5085 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `2.4993` → IC=+0.166 (n=639)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.4993 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `419.0` → IC=+0.158 (n=1879)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 419.0 (IC base=+0.154)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.170 (n=2050)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0058 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.2342` → IC=+0.174 (n=1802)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2342 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.185 (n=985)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.6155` → IC=+0.206 (n=2048)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6155 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.447` → IC=+0.196 (n=389)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 11.447 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.2053` → IC=+0.160 (n=2048)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2053 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` < `0.0934` → IC=+0.149 (n=1739)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.0934 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.4965` → IC=+0.153 (n=1928)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4965 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.4236` → IC=+0.146 (n=1928)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4236 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `201.0` → IC=+0.179 (n=619)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 201.0 (IC base=+0.145)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.239 (n=996)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.3997` → IC=+0.225 (n=1931)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3997 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.220 (n=2276)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.305 (n=1135)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.422` → IC=+0.300 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.422 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` < `0.0992` → IC=+0.214 (n=1879)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0992 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.3549` → IC=+0.235 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3549 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `1.767` → IC=+0.215 (n=936)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.767 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.7121` → IC=+0.228 (n=964)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7121 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=2621)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `1959.2048` → IC=+0.228 (n=995)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1959.2048 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.248 (n=1652)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.5724` → IC=+0.251 (n=1878)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5724 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.281 (n=715)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.0083` → IC=+0.301 (n=827)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0083 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.494` → IC=+0.275 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.494 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.3553` → IC=+0.278 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3553 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `1.7471` → IC=+0.237 (n=790)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7471 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.1514` → IC=+0.238 (n=1196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1514 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `2044.5699` → IC=+0.242 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2044.5699 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.238 (n=1193)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.236)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.173 (n=2107)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0074 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.0762` → IC=+0.197 (n=705)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.0762 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=2187)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.3118` → IC=+0.214 (n=2107)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3118 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1444` → IC=+0.199 (n=1284)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1444 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.858` → IC=+0.197 (n=490)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 9.858 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.0223` → IC=+0.159 (n=1854)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.0223 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1034` → IC=+0.180 (n=861)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1034 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.8191` → IC=+0.151 (n=1377)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.8191 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `2.5068` → IC=+0.170 (n=688)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.5068 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `4615.2008` → IC=+0.186 (n=1404)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 4615.2008 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.159 (n=2048)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 139.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.155 (n=2207)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0072 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.3952` → IC=+0.145 (n=2207)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3952 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=1051)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.6846` → IC=+0.187 (n=2207)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6846 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.1535` → IC=+0.157 (n=2203)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1535 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.603` → IC=+0.160 (n=545)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 9.603 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.8554` → IC=+0.157 (n=1472)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8554 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2997` → IC=+0.193 (n=333)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2997 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.8099` → IC=+0.136 (n=1379)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.8099 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.5483` → IC=+0.131 (n=689)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.5483 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `7462.3925` → IC=+0.191 (n=1001)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 7462.3925 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `68.0` → IC=+0.150 (n=903)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 68.0 (IC base=+0.128)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.179 (n=1075)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0103 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.4413` → IC=+0.131 (n=2082)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.4413 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.172 (n=1134)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 15.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` > `0.4878` → IC=+0.217 (n=2367)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4878 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.1964` → IC=+0.191 (n=1378)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1964 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.563` → IC=+0.281 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.563 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `1.1741` → IC=+0.145 (n=2366)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1741 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` < `0.161` → IC=+0.137 (n=2399)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.161 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.4382` → IC=+0.151 (n=766)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4382 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.132 (n=2478)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `2769.2348` → IC=+0.209 (n=1073)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2769.2348 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.169 (n=765)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 20.0 (IC base=+0.130)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.139 (n=2414)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0108 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.108` → IC=+0.174 (n=805)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.108 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.141 (n=2461)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.219 (n=2420)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.386` → IC=+0.124 (n=482)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 7.386 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.467` → IC=+0.132 (n=2135)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 2.467 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.1753` → IC=+0.129 (n=2413)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.1753 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1653` → IC=+0.123 (n=2334)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1653 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2757` → IC=+0.149 (n=323)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.2757 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4463` → IC=+0.134 (n=750)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.4463 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `2.4253` → IC=+0.137 (n=750)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.4253 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2652.3341` → IC=+0.191 (n=1094)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2652.3341 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.130 (n=1963)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 42.0 (IC base=+0.120)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.247 (n=1948)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0131 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.1287` → IC=+0.239 (n=727)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1287 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.227 (n=2263)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.227 (n=1953)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.66` → IC=+0.259 (n=2187)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.66 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` > `0.1837` → IC=+0.228 (n=1411)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1837 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.61` → IC=+0.253 (n=992)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.61 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `1.1768` → IC=+0.225 (n=2180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1768 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `0.6183` → IC=+0.231 (n=2180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6183 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.274 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.283 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `2.47` → IC=+0.229 (n=2121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.47 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `1.8081` → IC=+0.232 (n=1414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8081 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `2845.0997` → IC=+0.225 (n=989)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2845.0997 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.233 (n=978)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.229)

- **PATRÓN** `sigma_h` > `0.0226` → IC=+0.240 (n=1008)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0226 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.0876` → IC=+0.261 (n=742)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0876 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.248 (n=1086)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.229)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.229 (n=991)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` < `0.4296` → IC=+0.257 (n=2223)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4296 (IC base=+0.229)

- **PATRÓN** `dist_vwap_pct` > `0.2951` → IC=+0.237 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2951 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.326` → IC=+0.260 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.326 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` > `0.6394` → IC=+0.236 (n=2223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6394 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.2803` → IC=+0.284 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2803 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `1.4384` → IC=+0.231 (n=2068)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4384 (IC base=+0.229)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.207 (n=1471)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.183)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.192 (n=1110)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0089 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.1295` → IC=+0.202 (n=1464)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1295 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.215 (n=1656)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.4878` → IC=+0.218 (n=2969)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4878 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.7944` → IC=+0.205 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7944 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.623` → IC=+0.212 (n=1438)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.623 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.8627` → IC=+0.205 (n=1990)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8627 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` > `0.6964` → IC=+0.187 (n=2666)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 0.6964 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.0999` → IC=+0.193 (n=1192)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0999 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` < `1.4307` → IC=+0.198 (n=1077)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.4307 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `1.8205` → IC=+0.187 (n=2155)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.8205 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.190 (n=3751)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `2677.4245` → IC=+0.190 (n=2969)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2677.4245 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `148.0` → IC=+0.194 (n=3108)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 148.0 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.137 (n=1197)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0038 (IC base=+0.089)

- **PATRÓN** `ibs_20min` < `0.381` → IC=+0.161 (n=2390)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.381 (IC base=+0.089)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.127 (n=1524)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 27.0 (IC base=+0.089)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.202 (n=410)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.3265` → IC=+0.200 (n=930)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3265 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.206 (n=849)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `0.6361` → IC=+0.236 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6361 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `0.3078` → IC=+0.196 (n=278)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.3078 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.069` → IC=+0.192 (n=397)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 3.069 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.112` → IC=+0.179 (n=895)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 4.112 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `0.8753` → IC=+0.204 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8753 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.0716` → IC=+0.183 (n=367)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.0716 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` < `2.2005` → IC=+0.187 (n=800)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.2005 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `1.4097` → IC=+0.179 (n=909)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4097 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `14694.0598` → IC=+0.183 (n=620)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 14694.0598 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `159.0` → IC=+0.210 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 159.0 (IC base=+0.178)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.186 (n=371)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0028 (IC base=+0.116)

- **PATRÓN** `drift_60min` |x|≤ `0.2687` → IC=+0.142 (n=973)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.2687 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.129 (n=1005)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 7.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.6326` → IC=+0.167 (n=973)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.6326 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.686` → IC=+0.129 (n=219)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 8.686 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` > `1.07` → IC=+0.146 (n=501)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.07 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.1612` → IC=+0.166 (n=294)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1612 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `2.1209` → IC=+0.130 (n=961)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 2.1209 (IC base=+0.116)

- **PATRÓN** `ballena_activa_n` < `220.0` → IC=+0.162 (n=717)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 220.0 (IC base=+0.116)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.248 (n=676)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.0937` → IC=+0.235 (n=338)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0937 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=1063)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `0.3764` → IC=+0.258 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3764 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `0.7903` → IC=+0.216 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7903 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` < `0.2089` → IC=+0.223 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2089 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.884` → IC=+0.244 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.884 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` < `0.8358` → IC=+0.226 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8358 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `1.1649` → IC=+0.224 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1649 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.1583` → IC=+0.250 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1583 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.4231` → IC=+0.241 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4231 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `2.4732` → IC=+0.238 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4732 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.216 (n=1134)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.1051` → IC=+0.165 (n=344)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.1051 (IC base=+0.063)

- **PATRÓN** `libro_liquidez` > `6363.1832` → IC=+0.134 (n=687)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 6363.1832 (IC base=+0.063)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.185 (n=277)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0107 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.5315` → IC=+0.169 (n=823)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.5315 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.221 (n=400)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.276 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.9868` → IC=+0.238 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9868 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.973` → IC=+0.250 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.973 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `1.0562` → IC=+0.187 (n=726)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 1.0562 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` > `0.714` → IC=+0.177 (n=735)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.714 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.1626` → IC=+0.189 (n=226)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1626 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.4413` → IC=+0.185 (n=265)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.4413 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.1768` → IC=+0.174 (n=360)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.1768 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.176 (n=851)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.02 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `3029.7873` → IC=+0.190 (n=275)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 3029.7873 (IC base=+0.168)

- **PATRÓN** `ibs_20min` < `0.5455` → IC=+0.136 (n=781)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.5455 (IC base=+0.055)

- **PATRÓN** `libro_liquidez` > `2709.2975` → IC=+0.148 (n=401)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 2709.2975 (IC base=+0.055)

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

- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.149 (n=226)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0125 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.135 (n=176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 10.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.61` → IC=+0.130 (n=252)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.61 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `1.1964` → IC=+0.318 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1964 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.225` → IC=+0.176 (n=66)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 5.225 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.8919` → IC=+0.141 (n=168)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.8919 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2383` → IC=+0.194 (n=47)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2383 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` > `2.3392` → IC=+0.136 (n=108)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.3392 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.130 (n=233)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 19.0 (IC base=+0.117)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.228 (n=5631)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.193 (n=17624)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` > `0.4476` → IC=+0.232 (n=16890)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4476 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` > `0.8998` → IC=+0.211 (n=2084)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8998 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.256` → IC=+0.255 (n=4127)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.256 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` < `1.2222` → IC=+0.170 (n=11326)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.2222 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.2905` → IC=+0.208 (n=2245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2905 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `2.6131` → IC=+0.198 (n=5480)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.6131 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `1793.2208` → IC=+0.185 (n=16890)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1793.2208 (IC base=+0.184)

- **PATRÓN** `ballena_activa_n` < `112.0` → IC=+0.205 (n=15516)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 112.0 (IC base=+0.184)

- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.192 (n=13474)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0096 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.4911` → IC=+0.192 (n=15305)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.4911 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=5714)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.5833` → IC=+0.243 (n=15314)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5833 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.809` → IC=+0.207 (n=2122)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.809 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.565` → IC=+0.190 (n=14805)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 3.565 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `0.7044` → IC=+0.164 (n=4546)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.7044 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.2904` → IC=+0.253 (n=2070)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2904 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.259` → IC=+0.197 (n=6563)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.259 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.216 (n=9570)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.188)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.235 (n=919)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.3484` → IC=+0.229 (n=2755)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3484 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.238 (n=1343)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.229 (n=1845)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.330 (n=1092)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.487` → IC=+0.354 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.487 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.232` → IC=+0.284 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.232 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `1.4449` → IC=+0.223 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4449 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `2.2863` → IC=+0.237 (n=1199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2863 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.244 (n=2939)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2077.0202` → IC=+0.229 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2077.0202 (IC base=+0.226)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.249 (n=1662)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.266 (n=2348)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.262)

- **PATRÓN** `drift_60min` |x|≤ `0.1194` → IC=+0.286 (n=1032)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1194 (IC base=+0.262)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.268 (n=2151)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.262)

- **PATRÓN** `ibs_20min` < `0.5111` → IC=+0.288 (n=2346)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5111 (IC base=+0.262)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.136` → IC=+0.266 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.136 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` < `0.0953` → IC=+0.262 (n=2108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0953 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` > `0.2864` → IC=+0.291 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2864 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` < `1.5569` → IC=+0.265 (n=978)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5569 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` > `2.6409` → IC=+0.271 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6409 (IC base=+0.262)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.263 (n=2644)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.262)

- **PATRÓN** `libro_liquidez` > `1628.1602` → IC=+0.271 (n=2095)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1628.1602 (IC base=+0.262)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.272 (n=971)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.262)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.199 (n=920)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0028 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1045` → IC=+0.165 (n=1204)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1045 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=2858)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.3685` → IC=+0.224 (n=2445)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3685 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1264` → IC=+0.194 (n=1415)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1264 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.562` → IC=+0.162 (n=580)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 9.562 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.172` → IC=+0.153 (n=2386)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 3.172 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.6301` → IC=+0.173 (n=913)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6301 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.0719` → IC=+0.153 (n=2439)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.0719 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2717` → IC=+0.186 (n=393)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2717 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1808` → IC=+0.158 (n=2355)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1808 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.5282` → IC=+0.156 (n=2390)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.5282 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `239.0` → IC=+0.185 (n=874)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 239.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.165 (n=2278)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0058 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.2566` → IC=+0.165 (n=2004)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.2566 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=860)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.6963` → IC=+0.198 (n=2277)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.6963 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.176` → IC=+0.159 (n=376)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 11.176 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.413` → IC=+0.144 (n=2295)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 6.413 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.0486` → IC=+0.157 (n=2004)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0486 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.218` → IC=+0.196 (n=426)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.218 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.4323` → IC=+0.149 (n=2172)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4323 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.7759` → IC=+0.154 (n=1448)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.7759 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=2956)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `274.0` → IC=+0.159 (n=918)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 274.0 (IC base=+0.144)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.259 (n=937)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=2942)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2511)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=1049)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.304` → IC=+0.324 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.304 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` < `0.097` → IC=+0.231 (n=2486)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.097 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `3.1781` → IC=+0.241 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1781 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=3354)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `1824.1584` → IC=+0.234 (n=1874)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1824.1584 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.247 (n=2320)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.1812` → IC=+0.257 (n=1160)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1812 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.262 (n=995)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.0323` → IC=+0.306 (n=880)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0323 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.627` → IC=+0.295 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.627 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.3447` → IC=+0.301 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3447 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.1315` → IC=+0.250 (n=1671)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1315 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.244 (n=1399)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1953.22` → IC=+0.252 (n=1195)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1953.22 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.258 (n=1123)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.241)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.205 (n=977)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.4224` → IC=+0.159 (n=2905)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4224 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=3019)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.2464` → IC=+0.195 (n=2904)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.2464 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.1424` → IC=+0.172 (n=1547)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1424 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.123` → IC=+0.160 (n=1179)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.123 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.8651` → IC=+0.167 (n=1938)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.8651 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.2803` → IC=+0.195 (n=378)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2803 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.5241` → IC=+0.163 (n=1247)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.5241 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `2.1716` → IC=+0.159 (n=1285)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.1716 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `6084.071` → IC=+0.241 (n=1317)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6084.071 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `74.0` → IC=+0.171 (n=1239)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 74.0 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.151 (n=2411)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0075 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.4386` → IC=+0.140 (n=2410)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4386 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.156 (n=882)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.7358` → IC=+0.185 (n=2410)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.7358 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.1496` → IC=+0.145 (n=2192)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1496 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.081` → IC=+0.176 (n=368)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 11.081 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.6983` → IC=+0.145 (n=1061)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.6983 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2959` → IC=+0.219 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2959 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.5408` → IC=+0.137 (n=2071)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.5408 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `7168.1488` → IC=+0.211 (n=804)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7168.1488 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `67.0` → IC=+0.133 (n=793)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 67.0 (IC base=+0.130)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.160 (n=1326)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0103 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.180 (n=1080)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.4407` → IC=+0.201 (n=2925)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4407 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `1.0609` → IC=+0.208 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0609 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.731` → IC=+0.267 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.731 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `1.2216` → IC=+0.137 (n=2925)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.2216 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` < `0.1622` → IC=+0.127 (n=3040)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1622 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2791` → IC=+0.131 (n=377)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.2791 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.831` → IC=+0.128 (n=1905)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.831 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.1941` → IC=+0.130 (n=1296)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.1941 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.131 (n=3041)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `2497.3328` → IC=+0.233 (n=1326)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2497.3328 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.144 (n=917)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 24.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.153 (n=2445)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.01 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.1336` → IC=+0.154 (n=926)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1336 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.130 (n=2868)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.6471` → IC=+0.212 (n=2777)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6471 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` < `0.2141` → IC=+0.136 (n=2397)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.2141 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.253` → IC=+0.134 (n=2676)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 3.253 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.7102` → IC=+0.141 (n=1222)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.7102 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2248` → IC=+0.173 (n=475)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2248 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.4404` → IC=+0.154 (n=867)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4404 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2673.0464` → IC=+0.206 (n=926)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2673.0464 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.133 (n=2289)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 47.0 (IC base=+0.117)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0137` → IC=+0.251 (n=2467)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0137 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.237 (n=2886)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.235 (n=1989)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` > `0.6102` → IC=+0.272 (n=2467)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6102 (IC base=+0.232)

- **PATRÓN** `dist_vwap_pct` > `0.1902` → IC=+0.248 (n=1501)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1902 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.73` → IC=+0.273 (n=926)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.73 (IC base=+0.232)

- **PATRÓN** `volumen_regimen` < `1.2308` → IC=+0.238 (n=2761)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2308 (IC base=+0.232)

- **PATRÓN** `volumen_regimen` > `0.6395` → IC=+0.234 (n=2761)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6395 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.2873` → IC=+0.259 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2873 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.5041` → IC=+0.253 (n=896)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5041 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.233 (n=3587)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `2959.7939` → IC=+0.237 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2959.7939 (IC base=+0.232)

- **PATRÓN** `sigma_h` > `0.0255` → IC=+0.251 (n=956)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0255 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.237 (n=2701)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.230)

- **PATRÓN** `ibs_20min` < `0.5152` → IC=+0.265 (n=2864)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5152 (IC base=+0.230)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.196` → IC=+0.266 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.196 (IC base=+0.230)

- **PATRÓN** `volumen_regimen` > `1.2292` → IC=+0.258 (n=956)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2292 (IC base=+0.230)

- **PATRÓN** `volumen_pendiente_norm` > `0.2821` → IC=+0.300 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2821 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.232 (n=2661)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=+0.230)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.194 (n=4972)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.246 (n=1700)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.5055` → IC=+0.219 (n=5099)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5055 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.226 (n=1865)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.9402` → IC=+0.250 (n=1700)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9402 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` > `0.1722` → IC=+0.213 (n=1905)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1722 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` < `0.2474` → IC=+0.211 (n=3252)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2474 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.012` → IC=+0.217 (n=836)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.012 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.59` → IC=+0.211 (n=4538)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.59 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` < `0.7046` → IC=+0.221 (n=1636)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7046 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` > `0.8836` → IC=+0.210 (n=2480)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8836 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` < `0.1066` → IC=+0.210 (n=4764)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1066 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.1667` → IC=+0.223 (n=1431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1667 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.4546` → IC=+0.218 (n=1674)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4546 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.8464` → IC=+0.210 (n=3346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8464 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.215 (n=3928)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2926.7434` → IC=+0.216 (n=4554)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2926.7434 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.240 (n=1248)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.49` → IC=+0.208 (n=3741)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.49 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=1271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.208 (n=1658)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.7334` → IC=+0.199 (n=3741)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.7334 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.6749` → IC=+0.200 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6749 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` < `0.2402` → IC=+0.190 (n=3421)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.2402 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.833` → IC=+0.203 (n=3354)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.833 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `1.0967` → IC=+0.202 (n=3122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0967 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.197 (n=3430)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2229` → IC=+0.195 (n=756)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2229 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `1.5329` → IC=+0.198 (n=1623)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.5329 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `1.813` → IC=+0.199 (n=2458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.813 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.194 (n=4972)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.193)

- **PATRÓN** `ballena_activa_n` < `173.0` → IC=+0.201 (n=3229)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 173.0 (IC base=+0.193)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.273 (n=673)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.260)

- **PATRÓN** `drift_60min` |x|≤ `0.0853` → IC=+0.294 (n=255)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0853 (IC base=+0.260)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.266 (n=766)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.260)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.260 (n=765)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.260)

- **PATRÓN** `ibs_20min` < `0.489` → IC=+0.279 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.489 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.054` → IC=+0.274 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.054 (IC base=+0.260)

- **PATRÓN** `volumen_regimen` < `1.2151` → IC=+0.267 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2151 (IC base=+0.260)

- **PATRÓN** `volumen_regimen` > `0.868` → IC=+0.273 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.868 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` > `0.2875` → IC=+0.350 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2875 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` < `1.8249` → IC=+0.267 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8249 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `16321.2566` → IC=+0.274 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16321.2566 (IC base=+0.260)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.253 (n=582)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.3687` → IC=+0.194 (n=1321)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.3687 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.225 (n=481)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.200 (n=482)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.207 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1382 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `0.6081` → IC=+0.179 (n=599)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.6081 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `0.7021` → IC=+0.186 (n=116)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.7021 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.38` → IC=+0.197 (n=1304)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` < 6.38 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `1.2212` → IC=+0.192 (n=1321)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 1.2212 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2183` → IC=+0.202 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2183 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` < `1.4018` → IC=+0.196 (n=438)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4018 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `1.8036` → IC=+0.187 (n=876)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.8036 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `14901.4739` → IC=+0.191 (n=599)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 14901.4739 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `694.0` → IC=+0.190 (n=1277)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 694.0 (IC base=+0.178)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.199 (n=344)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.007 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.218 (n=353)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.581` → IC=+0.202 (n=779)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.581 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=279)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` < `0.7037` → IC=+0.194 (n=521)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.7037 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `0.994` → IC=+0.237 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.994 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.492` → IC=+0.231 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.492 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.211` → IC=+0.244 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.211 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.2469` → IC=+0.200 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2469 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `2469.4536` → IC=+0.224 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2469.4536 (IC base=+0.190)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.194 (n=560)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 11.0 (IC base=+0.190)

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

- **PATRÓN** `dist_vwap_pct` < `0.2168` → IC=+0.209 (n=1221)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2168 (IC base=+0.197)

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
- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.223 (n=330)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0072 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.206 (n=773)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` > `0.925` → IC=+0.248 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.925 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` > `0.7483` → IC=+0.241 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7483 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.222` → IC=+0.206 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.222 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` < `0.6955` → IC=+0.226 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6955 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` < `0.2316` → IC=+0.193 (n=816)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.2316 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.0788` → IC=+0.194 (n=335)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0788 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` < `1.5672` → IC=+0.200 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5672 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `2.4766` → IC=+0.210 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4766 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.189 (n=872)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.02 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `3097.399` → IC=+0.205 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3097.399 (IC base=+0.184)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.200 (n=730)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.184)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.213 (n=367)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0093 (IC base=+0.204)

- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.219 (n=183)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.6119` → IC=+0.225 (n=550)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6119 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.240 (n=371)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` < `0.7273` → IC=+0.225 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7273 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.5149` → IC=+0.214 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5149 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` < `0.3104` → IC=+0.206 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3104 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.822` → IC=+0.213 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.822 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.926` → IC=+0.213 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.926 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` < `1.3372` → IC=+0.208 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.3372 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `0.9335` → IC=+0.206 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9335 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` < `0.1073` → IC=+0.224 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1073 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `2.2063` → IC=+0.243 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2063 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2993.9452` → IC=+0.222 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2993.9452 (IC base=+0.204)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.235 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.204)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.159 (n=743)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.004 (IC base=+0.071)

- **PATRÓN** `ibs_20min` > `0.3889` → IC=+0.144 (n=1592)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.3889 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` > `0.1486` → IC=+0.143 (n=830)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.1486 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.973` → IC=+0.159 (n=464)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 8.973 (IC base=+0.071)

- **PATRÓN** `ibs_20min` < `0.21` → IC=+0.231 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.21 (IC base=+0.056)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.344` → IC=+0.167 (n=139)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 10.344 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.1467` → IC=+0.172 (n=239)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1467 (IC base=+0.056)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.133 (n=556)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0056 (IC base=+0.089)

- **PATRÓN** `ibs_20min` > `0.3558` → IC=+0.168 (n=525)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.3558 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` > `0.1227` → IC=+0.158 (n=264)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1227 (IC base=+0.089)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.125 (n=182)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0029 (IC base=+0.071)

- **PATRÓN** `ibs_20min` < `0.0493` → IC=+0.275 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0493 (IC base=+0.071)

- **PATRÓN** `volumen_pendiente_norm` > `0.2162` → IC=+0.197 (n=74)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2162 (IC base=+0.071)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.6985` → IC=-0.174 (n=93)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6985
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=280)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.130 (n=484)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.006 (IC base=+0.090)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.149 (n=212)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.090)

- **PATRÓN** `ibs_20min` > `0.4223` → IC=+0.174 (n=519)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.4223 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` > `0.1258` → IC=+0.193 (n=268)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1258 (IC base=+0.090)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.194` → IC=+0.250 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.194 (IC base=+0.090)

- **PATRÓN** `volumen_regimen` < `0.8145` → IC=+0.122 (n=347)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 0.8145 (IC base=+0.090)

- **PATRÓN** `volumen_pendiente_norm` > `0.2877` → IC=+0.167 (n=73)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2877 (IC base=+0.090)

- **PATRÓN** `ibs_20min` < `0.0314` → IC=+0.292 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0314 (IC base=+0.020)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.686` → IC=+0.223 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.686 (IC base=+0.020)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` > `0.16` → IC=-0.204 (n=69)

  - _Acción_: SKIP cuando `ibs_20min` > 0.16
  - _Potencial_: sin este filtro IC_bueno=+0.224 (n=208)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.169 (n=366)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.75 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` > `0.7372` → IC=+0.144 (n=133)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.7372 (IC base=+0.034)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.311` → IC=+0.158 (n=118)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 9.311 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.2287` → IC=+0.132 (n=104)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.2287 (IC base=+0.034)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.156 (n=239)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0103 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.16` → IC=+0.224 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.16 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.1716` → IC=+0.141 (n=196)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.1716 (IC base=+0.075)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.474` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.474 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.0779` → IC=+0.208 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0779 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.1508` → IC=+0.234 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1508 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `2.18` → IC=+0.157 (n=164)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.18 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `1.3981` → IC=+0.160 (n=186)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.3981 (IC base=+0.075)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.147 (n=182)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.06 (IC base=+0.075)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `8.0` → IC=-0.336 (n=65)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.168 (n=245)

- **FILTRO** `dist_vwap_pct` > `0.2306` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2306
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=293)

- **FILTRO** `volumen_spike_ratio` > `2.8366` → IC=-0.200 (n=58)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.8366
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=178)

- **FILTRO** `libro_liquidez` < `888.9132` → IC=-0.222 (n=77)

  - _Acción_: SKIP cuando `libro_liquidez` < 888.9132
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=233)

- **FILTRO** `sigma_h` > `0.0052` → IC=-0.336 (n=65)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0052
  - _Potencial_: sin este filtro IC_bueno=-0.270 (n=198)

- **FILTRO** `dist_vwap_pct` > `0.4684` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4684
  - _Potencial_: sin este filtro IC_bueno=-0.276 (n=244)

- **FILTRO** `volumen_pendiente_norm` > `0.0465` → IC=-0.371 (n=29)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0465
  - _Potencial_: sin este filtro IC_bueno=-0.273 (n=148)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.271 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=51)

- **FILTRO** `volumen_regimen` < `0.8402` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8402
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=73)

- **FILTRO** `sigma_h` > `0.0043` → IC=-0.333 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0043
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=88)

- **FILTRO** `sigma_ewma_delta_pct` > `2.3` → IC=-0.263 (n=36)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.3
  - _Potencial_: sin este filtro IC_bueno=-0.256 (n=80)

- **FILTRO** `volumen_regimen` > `0.8213` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8213
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=88)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` < `0.0026` → IC=-0.321 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0026
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=78)

- **FILTRO** `drift_60min` |x|> `0.149` → IC=-0.315 (n=25)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.149
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=79)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.375 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=79)

- **FILTRO** `ibs_20min` > `0.725` → IC=-0.389 (n=34)

  - _Acción_: SKIP cuando `ibs_20min` > 0.725
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=67)

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

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.941 (IC base=-0.151)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.395 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `ibs_20min` < `0.25` → IC=-0.284 (n=35)

  - _Acción_: SKIP cuando `ibs_20min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=74)

- **FILTRO** `sigma_h` < `0.006` → IC=-0.324 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.006
  - _Potencial_: sin este filtro IC_bueno=-0.288 (n=31)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=31)

- **FILTRO** `dist_vwap_pct` < `0.2328` → IC=-0.352 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.2328
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=21)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.1558` → IC=-0.121 (n=280)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1558
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=546)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.200 (n=241)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=207)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.153 (n=528)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.6842 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.744` → IC=+0.224 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.744 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.6229` → IC=+0.185 (n=176)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6229 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` < `0.1529` → IC=+0.151 (n=431)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.1529 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.3996` → IC=+0.174 (n=142)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.3996 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.1558` → IC=+0.146 (n=546)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.1558 (IC base=+0.056)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.085` → IC=+0.177 (n=184)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 9.085 (IC base=+0.056)

- **PATRÓN** `libro_liquidez` > `3247.8769` → IC=+0.136 (n=413)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 3247.8769 (IC base=+0.056)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6933` → IC=-0.214 (n=54)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6933
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=164)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.184 (n=96)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0049 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.151 (n=196)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 12.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.143 (n=110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 6.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.1684` → IC=+0.194 (n=289)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.1684 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.158` → IC=+0.164 (n=123)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 7.158 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` > `1.0364` → IC=+0.177 (n=131)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.0364 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` < `0.0706` → IC=+0.150 (n=224)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.0706 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.2726` → IC=+0.167 (n=49)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2726 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.5184` → IC=+0.168 (n=257)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 2.5184 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.533` → IC=+0.142 (n=230)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.533 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `4595.2336` → IC=+0.142 (n=258)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 4595.2336 (IC base=+0.135)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1261` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1261
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=172)

- **FILTRO** `ibs_20min` > `0.3277` → IC=-0.162 (n=75)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3277
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=227)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.143 (n=124)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0039 (IC base=+0.098)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.196 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.8015` → IC=+0.139 (n=164)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.8015 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` < `0.0943` → IC=+0.137 (n=155)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.0943 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.314` → IC=+0.128 (n=170)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 6.314 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` < `0.6242` → IC=+0.172 (n=62)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.6242 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` < `0.1261` → IC=+0.144 (n=172)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` < 0.1261 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `1.7943` → IC=+0.170 (n=104)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.7943 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.906` → IC=+0.219 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.906 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.136 (n=31)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.023)

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
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.253)

- **PATRÓN** `ibs_20min` > `0.6522` → IC=+0.276 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6522 (IC base=+0.253)

- **PATRÓN** `dist_vwap_pct` > `0.6667` → IC=+0.389 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6667 (IC base=+0.253)

- **PATRÓN** `dist_vwap_pct` < `0.224` → IC=+0.258 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.224 (IC base=+0.253)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.331` → IC=+0.317 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.331 (IC base=+0.253)

- **PATRÓN** `volumen_regimen` < `0.5792` → IC=+0.325 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5792 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` > `0.1048` → IC=+0.336 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1048 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` < `1.4854` → IC=+0.398 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4854 (IC base=+0.253)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.256 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.253)

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
- **PATRÓN** `libro_liquidez` > `2845.305` → IC=+0.132 (n=571)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2845.305 (IC base=+0.102)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2845.305` → IC=+0.132 (n=571)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2845.305 (IC base=+0.102)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=193)

- **FILTRO** `libro_liquidez` < `2848.5092` → IC=-0.204 (n=52)

  - _Acción_: SKIP cuando `libro_liquidez` < 2848.5092
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=157)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=308)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `10893.2451` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 10893.2451
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=69)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=34)

- **PATRÓN** `liq_n` > `6.0` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `liq_n` > 6.0 (IC base=-0.017)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `ballena_activa_n` > `63.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 63.0
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` > `4.0` → IC=-0.167 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=3536)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=104)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=104)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.146 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=129)

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
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=1307)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=1261)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=716)

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
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=420)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=401)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.141 (n=179)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.495 (IC base=+0.023)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=841)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=841)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.132 (n=259)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=662)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=829)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=829)

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

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=234)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=258)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=256)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=349)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=349)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=194)

- **FILTRO** `libro_liquidez` < `625.8426` → IC=-0.138 (n=125)

  - _Acción_: SKIP cuando `libro_liquidez` < 625.8426
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=254)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=259)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.129 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=187)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `py_entrada` > `0.59` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=34)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.145 (n=60)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=35)

- **FILTRO** `py_entrada` > `0.47` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.155 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.178 (n=150)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.46 (IC base=+0.016)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.190 (n=56)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=253)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.139 (n=153)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=175)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` < 0.5 (IC base=+0.053)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.127 (n=314)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=168)

- **FILTRO** `profundidad_ratio` < `40.5` → IC=-0.164 (n=120)

  - _Acción_: SKIP cuando `profundidad_ratio` < 40.5
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=362)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.139 (n=200)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=224)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `profundidad_ratio` < `20.7` → IC=-0.133 (n=148)

  - _Acción_: SKIP cuando `profundidad_ratio` < 20.7
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=302)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.163 (n=87)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=368)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.120 (n=285)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=308)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.164 (n=6053)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=18740)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.176 (n=6128)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=19316)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.193 (n=1107)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=3406)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.173 (n=1047)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=3494)

- **PATRÓN** `py_entrada` > `0.495` → IC=+0.128 (n=3036)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` > 0.495 (IC base=+0.041)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.143 (n=1191)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 1.0 (IC base=+0.041)

- **PATRÓN** `libro_liquidez` > `1268.5562` → IC=+0.138 (n=2257)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 1268.5562 (IC base=+0.041)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.127 (n=2126)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.5 (IC base=+0.011)

- **PATRÓN** `libro_liquidez` > `1499.2588` → IC=+0.155 (n=1544)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1499.2588 (IC base=+0.011)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.156 (n=840)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=2781)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.177 (n=886)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=2720)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.203 (n=1083)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=3563)

- **PATRÓN** `ibs_20min` > `0.9645` → IC=+0.131 (n=1538)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 0.9645 (IC base=+0.038)

- **PATRÓN** `libro_liquidez` > `1539.75` → IC=+0.121 (n=2262)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 1539.75 (IC base=+0.038)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.158 (n=1099)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=3419)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2384)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.162 (n=758)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2322)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2810)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=3550)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=439)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.264 (n=138)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=426)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.234 (n=287)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=884)

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
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=928)

- **FILTRO** `libro_liquidez` < `1778.6635` → IC=-0.164 (n=236)

  - _Acción_: SKIP cuando `libro_liquidez` < 1778.6635
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=711)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=16980)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=38189)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.285 (n=13580)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=41589)

- **FILTRO** `ibs_7min` < `0.2378` → IC=-0.229 (n=13792)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2378
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=41377)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.153 (n=18369)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=36800)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.242 (n=17041)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=52330)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.183 (n=17156)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=52215)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.146 (n=2401)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=7242)

- **FILTRO** `py_entrada` < `0.46` → IC=-0.236 (n=4758)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=4885)

- **FILTRO** `ibs_7min` < `0.7136` → IC=-0.244 (n=3182)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7136
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=6461)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.180 (n=2037)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=7606)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.271 (n=2984)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=9042)

- **FILTRO** `ibs_7min` > `0.7699` → IC=-0.211 (n=3006)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7699
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=9020)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.266 (n=2178)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=7121)

- **FILTRO** `ibs_7min` < `0.726` → IC=-0.200 (n=2323)

  - _Acción_: SKIP cuando `ibs_7min` < 0.726
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=6976)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.191 (n=2322)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=6977)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.264 (n=2331)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=7128)

- **FILTRO** `ibs_7min` > `0.2678` → IC=-0.197 (n=2363)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2678
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=7096)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.184 (n=2343)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=7116)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.158 (n=2239)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=6923)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.313 (n=2252)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=6910)

- **FILTRO** `ibs_7min` < `0.2963` → IC=-0.246 (n=3022)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2963
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=6140)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.194 (n=2174)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=6988)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.254 (n=2995)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=9803)

- **FILTRO** `ibs_7min` > `0.7342` → IC=-0.179 (n=3198)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7342
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=9600)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.262 (n=2110)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=6886)

- **FILTRO** `ibs_7min` < `0.7281` → IC=-0.186 (n=2249)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7281
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6747)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.188 (n=2230)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6766)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.270 (n=2101)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=7205)

- **FILTRO** `ibs_7min` > `0.275` → IC=-0.180 (n=2325)

  - _Acción_: SKIP cuando `ibs_7min` > 0.275
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=6981)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.177 (n=2291)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=7015)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=2168)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=6872)

- **FILTRO** `ibs_7min` < `0.2143` → IC=-0.233 (n=2256)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2143
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=6784)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.218 (n=2178)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=6862)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.192 (n=3219)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=10031)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.292 (n=2132)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=6897)

- **FILTRO** `ibs_7min` < `0.2` → IC=-0.223 (n=2243)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=6786)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.199 (n=2257)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=6772)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.218 (n=3068)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=9464)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=120)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.158 (n=299)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=985)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=1269)

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
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=850)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.475` → IC=-0.122 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=330)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.143 (n=166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=325)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=442)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=70)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=637)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=387)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.139 (n=1166)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.129 (n=551)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 14.0 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.132 (n=436)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 4.0 (IC base=+0.129)

- **PATRÓN** `total_vol_5m` < `437.371` → IC=+0.155 (n=389)

  - _Acción_: Kelly boost +0.77€ cuando `total_vol_5m` < 437.371 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `3639.8241` → IC=+0.147 (n=528)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3639.8241 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.148 (n=379)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 11.0 (IC base=+0.129)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4374` → IC=+0.145 (n=91)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio` |x|> 0.4374 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.202 (n=132)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.136)

- **PATRÓN** `total_vol_5m` < `292.267` → IC=+0.145 (n=181)

  - _Acción_: Kelly boost +0.72€ cuando `total_vol_5m` < 292.267 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `2571.3862` → IC=+0.199 (n=91)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2571.3862 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.157 (n=100)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 7.0 (IC base=+0.136)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3992` → IC=+0.132 (n=240)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio` |x|> 0.3992 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.131 (n=215)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 14.0 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.126 (n=287)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.04 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2340.1091` → IC=+0.136 (n=160)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2340.1091 (IC base=+0.117)

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
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.126 (n=196)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 14.0 (IC base=+0.100)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.187 (n=132)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `3589.6144` → IC=+0.160 (n=98)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3589.6144 (IC base=+0.100)

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
- **FILTRO** `sigma_h` > `0.0072` → IC=-0.197 (n=31)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0072
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=33)

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
- **FILTRO** `sigma_h` < `0.0103` → IC=-0.218 (n=459)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0103
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=154)

- **FILTRO** `T_h` > `69.3519` → IC=-0.199 (n=459)

  - _Acción_: SKIP cuando `T_h` > 69.3519
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=154)

- **FILTRO** `pct_vs_K` |x|> `3.3065` → IC=-0.432 (n=130)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.3065
  - _Potencial_: sin este filtro IC_bueno=-0.163 (n=393)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=307)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=381)

- **PATRÓN** `streak_estiramiento` < `0.8382` → IC=+0.120 (n=256)

  - _Acción_: Kelly boost +0.60€ cuando `streak_estiramiento` < 0.8382 (IC base=+0.044)

- **PATRÓN** `libro_liquidez` > `2756.3002` → IC=+0.150 (n=101)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2756.3002 (IC base=+0.044)

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
- **PATRÓN** `streak_estiramiento` < `0.258` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `streak_estiramiento` < 0.258 (IC base=+0.008)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.136 (n=116)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 7.0 (IC base=+0.087)

- **PATRÓN** `streak_estiramiento` < `0.4496` → IC=+0.187 (n=97)

  - _Acción_: Kelly boost +0.93€ cuando `streak_estiramiento` < 0.4496 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.151 (n=107)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 35.0 (IC base=+0.087)

- **PATRÓN** `libro_liquidez` > `2414.7926` → IC=+0.155 (n=114)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2414.7926 (IC base=+0.087)

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
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=42)

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

  - _Acción_: Kelly boost +1.00€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.045)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1000)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1330)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=1144)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=1197)

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
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=4023)

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
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=2222)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.199 (n=1209)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.012` → IC=+0.197 (n=1209)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.012 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.1757` → IC=+0.193 (n=3191)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1757 (IC base=+0.179)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.133` → IC=+0.190 (n=1448)

  - _Acción_: Kelly boost +0.95€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.133 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=3366)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.182 (n=3323)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 15.0 (IC base=+0.179)

- **PATRÓN** `ibs_15` > `0.5526` → IC=+0.254 (n=3625)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5526 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.1296` → IC=+0.170 (n=1742)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1296 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` < `0.3169` → IC=+0.166 (n=2862)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.3169 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.553` → IC=+0.257 (n=941)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.553 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `4680.6995` → IC=+0.196 (n=1209)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 4680.6995 (IC base=+0.179)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1437)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.241 (n=412)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.0585` → IC=+0.270 (n=207)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0585 (IC base=+0.221)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2526` → IC=+0.245 (n=206)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2526 (IC base=+0.221)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2298` → IC=+0.234 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2298 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.240 (n=618)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.221)

- **PATRÓN** `ibs_15` > `0.7184` → IC=+0.287 (n=617)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7184 (IC base=+0.221)

- **PATRÓN** `dist_vwap_pct` > `0.2443` → IC=+0.242 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2443 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.772` → IC=+0.306 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.772 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.222 (n=800)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `8758.4418` → IC=+0.233 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8758.4418 (IC base=+0.221)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.186 (n=240)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0035 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.0667` → IC=+0.154 (n=316)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.0667 (IC base=+0.146)

- **PATRÓN** `drift_15min` |x|≤ `0.3955` → IC=+0.149 (n=240)

  - _Acción_: Kelly boost +0.74€ cuando `drift_15min` |x|≤ 0.3955 (IC base=+0.146)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1432` → IC=+0.153 (n=479)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio_macro` |x|> 0.1432 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.129` → IC=+0.164 (n=284)

  - _Acción_: Kelly boost +0.82€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.129 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.154 (n=660)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 6.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.152 (n=745)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.5408` → IC=+0.241 (n=717)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5408 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1202` → IC=+0.159 (n=444)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1202 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.827` → IC=+0.265 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.827 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `3217.3698` → IC=+0.152 (n=717)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3217.3698 (IC base=+0.146)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `17.774` → IC=-0.192 (n=37)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.774
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=339)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1764` → IC=+0.135 (n=548)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.1764 (IC base=+0.098)

- **PATRÓN** `ibs_15` > `0.8929` → IC=+0.257 (n=274)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8929 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.389` → IC=+0.156 (n=155)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 17.389 (IC base=+0.098)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=457)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.098)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.407` → IC=+0.132 (n=74)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 8.407 (IC base=+0.004)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0239` → IC=+0.237 (n=276)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0239 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.0867` → IC=+0.235 (n=364)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0867 (IC base=+0.202)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3374` → IC=+0.231 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3374 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.202 (n=756)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.214 (n=736)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.202)

- **PATRÓN** `ibs_15` > `0.5333` → IC=+0.280 (n=828)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5333 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.1302` → IC=+0.210 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1302 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.103` → IC=+0.228 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.103 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2964.3096` → IC=+0.295 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2964.3096 (IC base=+0.202)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.157 (n=785)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.78€ cuando `ibs_15` < 0.1111 (IC base=+0.066)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.392 (n=211)
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

- **PATRÓN** `ibs_15` > `0.7872` → IC=+0.401 (n=633)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7872 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.1463` → IC=+0.383 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1463 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.239` → IC=+0.386 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.239 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.369 (n=771)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `10357.0212` → IC=+0.386 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10357.0212 (IC base=+0.365)

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
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.368 (n=134)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.365)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.387 (n=139)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.380 (n=273)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.382 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.393 (n=147)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.365)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.372 (n=139)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.7479` → IC=+0.412 (n=305)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7479 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.4536` → IC=+0.382 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4536 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.861` → IC=+0.392 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.861 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.369 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `4001.8474` → IC=+0.394 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4001.8474 (IC base=+0.365)

- **PATRÓN** `ballena_activa_n` < `137.0` → IC=+0.368 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 137.0 (IC base=+0.365)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.175 (n=2176)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=2177)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.213 (n=1699)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=2654)

- **PATRÓN** `ibs_15` > `0.6326` → IC=+0.282 (n=1051)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6326 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` > `0.1124` → IC=+0.208 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1124 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` < `0.2675` → IC=+0.197 (n=897)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.2675 (IC base=-0.069)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2301` → IC=+0.269 (n=1205)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2301 (IC base=-0.013)

- **PATRÓN** `ibs_15` < `0.3596` → IC=+0.282 (n=3610)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3596 (IC base=-0.013)

- **PATRÓN** `dist_vwap_pct` > `0.6601` → IC=+0.276 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6601 (IC base=-0.013)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0341` → IC=-0.223 (n=1906)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0341
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=641)

- **FILTRO** `drift_15min` |x|> `0.6791` → IC=-0.196 (n=636)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.6791
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=1911)

- **FILTRO** `sigma_ewma_delta_pct` > `23.188` → IC=-0.270 (n=368)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.188
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=2179)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=66)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=2481)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.122 (n=760)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0053 (IC base=+0.096)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2051` → IC=+0.291 (n=156)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2051 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.122 (n=759)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 5.0 (IC base=+0.096)

- **PATRÓN** `ibs_15` > `0.7572` → IC=+0.334 (n=342)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7572 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.1061` → IC=+0.286 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1061 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` < `0.2456` → IC=+0.279 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2456 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.58` → IC=+0.130 (n=382)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 8.58 (IC base=+0.096)

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
  - _Potencial_: sin este filtro IC_bueno=+0.158 (n=685)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.162 (n=465)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0058 (IC base=+0.151)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.157 (n=351)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0049 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.0704` → IC=+0.188 (n=232)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0704 (IC base=+0.151)

- **PATRÓN** `drift_15min` |x|≤ `0.3992` → IC=+0.152 (n=176)

  - _Acción_: Kelly boost +0.76€ cuando `drift_15min` |x|≤ 0.3992 (IC base=+0.151)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3006` → IC=+0.192 (n=404)

  - _Acción_: Kelly boost +0.96€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3006 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=530)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.151 (n=539)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 17.0 (IC base=+0.151)

- **PATRÓN** `ibs_15` > `0.6046` → IC=+0.249 (n=527)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6046 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.4682` → IC=+0.169 (n=137)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.4682 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.1604` → IC=+0.151 (n=414)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1604 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.395` → IC=+0.238 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.395 (IC base=+0.151)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.158 (n=685)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `9675.8313` → IC=+0.157 (n=176)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 9675.8313 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.252 (n=1303)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.245)

- **PATRÓN** `drift_15min` |x|≤ `0.7694` → IC=+0.258 (n=1147)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7694 (IC base=+0.245)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1569` → IC=+0.260 (n=869)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1569 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.248 (n=479)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.247 (n=1160)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.245)

- **PATRÓN** `ibs_15` < `0.3696` → IC=+0.275 (n=1303)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3696 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` > `0.6087` → IC=+0.264 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6087 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.449` → IC=+0.256 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.449 (IC base=+0.245)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0105` → IC=-0.248 (n=252)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=759)

- **FILTRO** `drift_60min` |x|> `0.173` → IC=-0.255 (n=341)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.173
  - _Potencial_: sin este filtro IC_bueno=-0.161 (n=670)

- **FILTRO** `drift_15min` |x|> `0.89` → IC=-0.283 (n=252)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.89
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=759)

- **FILTRO** `sigma_ewma_delta_pct` > `6.65` → IC=-0.202 (n=233)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.65
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=778)

- **FILTRO** `sigma_ewma_delta_pct` > `17.995` → IC=-0.148 (n=527)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.995
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4180)

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

- **PATRÓN** `delta_ratio_macro` |x|> `0.0814` → IC=+0.236 (n=517)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0814 (IC base=-0.040)

- **PATRÓN** `ibs_15` < `0.3529` → IC=+0.292 (n=581)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3529 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` < `0.1869` → IC=+0.243 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1869 (IC base=-0.040)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0198` → IC=-0.251 (n=597)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0198
  - _Potencial_: sin este filtro IC_bueno=-0.164 (n=599)

- **FILTRO** `sigma_ewma_delta_pct` > `7.426` → IC=-0.213 (n=374)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.426
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=822)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.208)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.208)

- **PATRÓN** `delta_ratio_macro` |x|> `0.069` → IC=+0.273 (n=774)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.069 (IC base=-0.026)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.116` → IC=+0.294 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.116 (IC base=-0.026)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.292 (n=868)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` > `0.7727` → IC=+0.353 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7727 (IC base=-0.026)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.333 (n=16)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.062)

- **PATRÓN** `dist_vwap_pct` < `0.1207` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1207 (IC base=+0.062)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.333 (n=16)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.062)

- **PATRÓN** `dist_vwap_pct` < `0.1207` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1207 (IC base=+0.062)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.299 (n=949)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.0531` → IC=+0.321 (n=361)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0531 (IC base=+0.294)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2427` → IC=+0.312 (n=359)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2427 (IC base=+0.294)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2243` → IC=+0.307 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2243 (IC base=+0.294)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.309 (n=1126)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.294)

- **PATRÓN** `ibs_15` > `0.8382` → IC=+0.322 (n=1078)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8382 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` > `0.2727` → IC=+0.328 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2727 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.497` → IC=+0.380 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.497 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `12322.191` → IC=+0.313 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12322.191 (IC base=+0.294)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.309 (n=255)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.291)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.304 (n=263)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.0574` → IC=+0.316 (n=194)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0574 (IC base=+0.291)

- **PATRÓN** `delta_ratio_macro` |x|> `0.26` → IC=+0.315 (n=193)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.26 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.308 (n=581)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8292` → IC=+0.318 (n=579)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8292 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.2555` → IC=+0.329 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2555 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.497` → IC=+0.385 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.497 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `16201.6469` → IC=+0.331 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16201.6469 (IC base=+0.291)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.306 (n=499)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.296)

- **PATRÓN** `drift_60min` |x|≤ `0.0515` → IC=+0.317 (n=167)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0515 (IC base=+0.296)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1458` → IC=+0.303 (n=333)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1458 (IC base=+0.296)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2157` → IC=+0.317 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2157 (IC base=+0.296)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.310 (n=514)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.296)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.299 (n=451)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.296)

- **PATRÓN** `ibs_15` > `0.8486` → IC=+0.324 (n=499)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8486 (IC base=+0.296)

- **PATRÓN** `dist_vwap_pct` > `0.2899` → IC=+0.327 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2899 (IC base=+0.296)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.513` → IC=+0.365 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.513 (IC base=+0.296)

### UPDOWN_OU_5M
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1226` → IC=-0.151 (n=84)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1226
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=253)

- **FILTRO** `ballena_activa_n` > `46.0` → IC=-0.135 (n=228)

  - _Acción_: SKIP cuando `ballena_activa_n` > 46.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=77)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1228` → IC=-0.214 (n=117)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1228
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=361)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.186 (n=119)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=359)

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

- **FILTRO** `drift_60min` |x|> `0.2244` → IC=-0.222 (n=16)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2244
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=34)

- **FILTRO** `drift_15min` |x|> `0.3481` → IC=-0.278 (n=16)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3481
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
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=37)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.326 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=11)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0623` → IC=-0.286 (n=26)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0623
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5526 sube el IC de +0.179 a +0.254 en UPDOWN_GBM#15min (n=3625). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7184 sube el IC de +0.221 a +0.287 en UPDOWN_GBM#BTC#15min (n=617). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5408 sube el IC de +0.146 a +0.241 en UPDOWN_GBM#ETH#15min (n=717). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.8929 sube el IC de +0.098 a +0.257 en UPDOWN_GBM#SOL#15min (n=274). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5333 sube el IC de +0.202 a +0.280 en UPDOWN_GBM#XRP#15min (n=828). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.066 a +0.157 en UPDOWN_GBM#XRP#15min (n=785). Ya aplicado como kelly_boost=+0.78€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6326 sube el IC de -0.069 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=1051). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3596 sube el IC de -0.013 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=3610). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7572 sube el IC de +0.096 a +0.334 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=342). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.618 sube el IC de -0.195 a +0.290 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=60). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6046 sube el IC de +0.151 a +0.249 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=527). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3696 sube el IC de +0.245 a +0.275 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1303). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.193 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3529 sube el IC de -0.040 a +0.292 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=581). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.208 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.026 a +0.292 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=868). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.062 a +0.333 en UPDOWN_GBM_ETH_15M_HORA7 (n=16). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.062 a +0.333 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=16). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8382 sube el IC de +0.294 a +0.322 en UPDOWN_GBM_IBS_ALTO (n=1078). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8292 sube el IC de +0.291 a +0.318 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=579). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8486 sube el IC de +0.296 a +0.324 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=499). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7872 sube el IC de +0.365 a +0.401 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=633). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8057 sube el IC de +0.364 a +0.391 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=329). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7479 sube el IC de +0.365 a +0.412 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=305). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1934 | +0.091 | +221.20€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1934 | +0.091 | +221.20€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1543 | +0.095 | +191.24€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1543 | +0.095 | +191.24€ | 0 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 283 | +0.072 | +12.53€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 283 | +0.072 | +12.53€ | 4 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 77 | +0.108 | +17.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 77 | +0.108 | +17.77€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 664 | -0.003 | +71.82€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 664 | -0.003 | +71.82€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 483 | -0.032 | +37.60€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 483 | -0.032 | +37.60€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 141 | +0.080 | +25.62€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 141 | +0.080 | +25.62€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 40329 | -0.081 | -5028.37€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2224 | +0.033 | -260.63€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 38105 | -0.088 | -4767.74€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4498 | -0.115 | -778.17€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4498 | -0.115 | -778.17€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2224 | +0.033 | -260.63€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2224 | +0.033 | -260.63€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4323 | -0.105 | -876.84€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4323 | -0.105 | -876.84€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 10756 | -0.021 | -998.86€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 10756 | -0.021 | -998.86€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 10653 | -0.104 | -798.86€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 10653 | -0.104 | -798.86€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 7875 | -0.132 | -1314.99€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 7875 | -0.132 | -1314.99€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 35360 | -0.015 | +3327.08€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 9152 | +0.004 | +1661.74€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 26208 | -0.022 | +1665.34€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 35360 | -0.015 | +3327.08€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 9152 | +0.004 | +1661.74€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 26208 | -0.022 | +1665.34€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 146199 | +0.116 | -5760.78€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 18703 | +0.182 | -572.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 642 | -0.015 | -67.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 118108 | +0.107 | -4816.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 8746 | +0.100 | -304.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 19583 | +0.108 | -1188.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 61 | -0.151 | +10.95€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 19507 | +0.109 | -1187.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 28294 | +0.129 | -389.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5204 | +0.188 | -177.61€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 19572 | +0.121 | -85.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3476 | +0.083 | -104.31€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 19638 | +0.100 | -1354.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 74 | -0.118 | -5.77€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 19549 | +0.101 | -1337.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 31095 | +0.125 | -553.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 8041 | +0.178 | -150.83€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 19836 | +0.108 | -341.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3206 | +0.100 | -52.95€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 27984 | +0.115 | -1364.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5255 | +0.196 | -254.58€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 545 | +0.017 | -14.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 20120 | +0.095 | -949.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2064 | +0.130 | -147.21€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#XRP | 19605 | +0.106 | -910.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 68 | -0.086 | +5.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 19524 | +0.107 | -915.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 23517 | +0.197 | -1396.70€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 23517 | +0.197 | -1396.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 5349 | +0.180 | -444.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 5349 | +0.180 | -444.46€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 2996 | +0.203 | -67.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 2996 | +0.203 | -67.03€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 5291 | +0.181 | -417.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 5291 | +0.181 | -417.49€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4589 | +0.248 | -150.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4589 | +0.248 | -150.55€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 5213 | +0.189 | -330.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 5213 | +0.189 | -330.92€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1025 | +0.427 | -34.37€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1025 | +0.427 | -34.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 404 | +0.433 | -8.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 404 | +0.433 | -8.08€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 404 | +0.433 | -7.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 404 | +0.433 | -7.18€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 203 | +0.402 | -15.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 203 | +0.402 | -15.25€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 82273 | +0.202 | -5816.84€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 82273 | +0.202 | -5816.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 14131 | +0.186 | -1442.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 14131 | +0.186 | -1442.17€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 13288 | +0.225 | -452.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 13288 | +0.225 | -452.28€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 14090 | +0.182 | -1460.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 14090 | +0.182 | -1460.97€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 13360 | +0.221 | -481.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 13360 | +0.221 | -481.57€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 13651 | +0.202 | -887.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 13651 | +0.202 | -887.26€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 13753 | +0.197 | -1092.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 13753 | +0.197 | -1092.60€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 31480 | +0.117 | +190.66€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 31480 | +0.117 | +190.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 15649 | +0.119 | +164.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 15649 | +0.119 | +164.72€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 15831 | +0.114 | +25.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 15831 | +0.114 | +25.94€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2088 | +0.293 | -6.32€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2088 | +0.293 | -6.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 956 | +0.280 | -25.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 956 | +0.280 | -25.30€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1013 | +0.297 | +13.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1013 | +0.297 | +13.67€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 119 | +0.351 | +5.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 119 | +0.351 | +5.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 961 | +0.442 | +4.93€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 961 | +0.442 | +4.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 466 | +0.436 | -4.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 466 | +0.436 | -4.27€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 449 | +0.449 | +8.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 449 | +0.449 | +8.65€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1656 | +0.071 | -65.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 640 | +0.053 | -50.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1016 | +0.083 | -14.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 74 | +0.118 | +4.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 74 | +0.118 | +4.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1272 | +0.079 | -27.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 256 | +0.062 | -12.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1016 | +0.083 | -14.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 310 | +0.029 | -42.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 310 | +0.029 | -42.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 62229 | +0.101 | -1581.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 5033 | +0.091 | +48.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 57196 | +0.101 | -1629.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 34233 | +0.105 | -388.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 5033 | +0.091 | +48.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 29200 | +0.108 | -437.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 12797 | +0.109 | -80.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 12797 | +0.109 | -80.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 15199 | +0.082 | -1112.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 15199 | +0.082 | -1112.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 897 | +0.193 | -109.11€ | 4 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 897 | +0.193 | -109.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 897 | +0.193 | -109.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 897 | +0.193 | -109.11€ | 4 | 4 |
| ✅ GBM_LATE_15M | 42760 | +0.095 | +22407.05€ | 0 | 18 |
| ✅ GBM_LATE_15M#15min | 42760 | +0.095 | +22407.05€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 7123 | +0.217 | +5891.80€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 7123 | +0.217 | +5891.80€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 6408 | +0.180 | +4923.11€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 6408 | +0.180 | +4923.11€ | 0 | 24 |
| ✅ GBM_LATE_15M#DOGE | 7642 | +0.206 | +5968.72€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 7642 | +0.206 | +5968.72€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 5964 | +0.042 | +1686.60€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 5964 | +0.042 | +1686.60€ | 1 | 19 |
| ✅ GBM_LATE_15M#SOL | 6023 | -0.032 | +1257.83€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 6023 | -0.032 | +1257.83€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 9600 | -0.030 | +2678.99€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 9600 | -0.030 | +2678.99€ | 4 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 45999 | +0.085 | +25070.75€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 45999 | +0.085 | +25070.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 8892 | +0.003 | +4496.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 8892 | +0.003 | +4496.15€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 9739 | +0.009 | +2311.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 9739 | +0.009 | +2311.54€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 6375 | +0.279 | +6865.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 6375 | +0.279 | +6865.47€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 8303 | +0.014 | +2067.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 8303 | +0.014 | +2067.46€ | 1 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 7327 | +0.039 | +3014.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 7327 | +0.039 | +3014.42€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5363 | +0.304 | +6315.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5363 | +0.304 | +6315.72€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 33895 | +0.181 | +27551.40€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 33895 | +0.181 | +27551.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 5138 | +0.231 | +4592.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 5138 | +0.231 | +4592.41€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 5339 | +0.149 | +3963.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 5339 | +0.149 | +3963.54€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 5428 | +0.224 | +4690.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 5428 | +0.224 | +4690.28€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 5750 | +0.139 | +4393.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 5750 | +0.139 | +4393.10€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 6371 | +0.125 | +4764.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 6371 | +0.125 | +4764.85€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 5869 | +0.226 | +5147.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 5869 | +0.226 | +5147.22€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 9210 | +0.134 | +4528.45€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 9210 | +0.134 | +4528.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2712 | +0.145 | +1552.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2712 | +0.145 | +1552.54€ | 0 | 22 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 467 | +0.150 | +239.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 467 | +0.150 | +239.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2724 | +0.139 | +1312.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2724 | +0.139 | +1312.05€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2276 | +0.109 | +888.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2276 | +0.109 | +888.27€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 626 | +0.134 | +283.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 626 | +0.134 | +283.67€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 42925 | +0.186 | +34440.39€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#15min | 42925 | +0.186 | +34440.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 6798 | +0.242 | +6362.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 6798 | +0.242 | +6362.76€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 6683 | +0.147 | +4586.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 6683 | +0.147 | +4586.35€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 7260 | +0.233 | +6499.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 7260 | +0.233 | +6499.50€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 7085 | +0.139 | +5077.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 7085 | +0.139 | +5077.82€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 7600 | +0.121 | +5260.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 7600 | +0.121 | +5260.78€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 7499 | +0.231 | +6653.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 7499 | +0.231 | +6653.18€ | 0 | 19 |
| ✅ GBM_LATE_5M | 11784 | +0.202 | +9196.20€ | 1 | 31 |
| ✅ GBM_LATE_5M#5min | 11784 | +0.202 | +9196.20€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 984 | +0.242 | +916.10€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 984 | +0.242 | +916.10€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2778 | +0.208 | +2391.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2778 | +0.208 | +2391.40€ | 0 | 25 |
| ✅ GBM_LATE_5M#DOGE | 1113 | +0.193 | +810.34€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1113 | +0.193 | +810.34€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 3342 | +0.193 | +2355.71€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3342 | +0.193 | +2355.71€ | 0 | 28 |
| ✅ GBM_LATE_5M#SOL | 1730 | +0.193 | +1321.63€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1730 | +0.193 | +1321.63€ | 0 | 28 |
| ✅ GBM_LATE_5M#XRP | 1837 | +0.204 | +1401.02€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1837 | +0.204 | +1401.02€ | 0 | 0 |
| ✅ GBM_LATE_60M | 3514 | +0.065 | +1144.97€ | 0 | 7 |
| ✅ GBM_LATE_60M#60min | 3514 | +0.065 | +1144.97€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1290 | +0.081 | +473.78€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1290 | +0.081 | +473.78€ | 0 | 6 |
| ✅ GBM_LATE_60M#ETH | 1135 | +0.066 | +381.01€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1135 | +0.066 | +381.01€ | 1 | 9 |
| ✅ GBM_LATE_60M#SOL | 1089 | +0.046 | +290.18€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1089 | +0.046 | +290.18€ | 1 | 13 |
| 🚫 GBM_LATE_60M_FADE | 573 | -0.244 | -22.02€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 573 | -0.244 | -22.02€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 213 | -0.249 | -15.57€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 213 | -0.249 | -15.57€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 205 | -0.225 | +0.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 205 | -0.225 | +0.05€ | 7 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 155 | -0.258 | -6.50€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 155 | -0.258 | -6.50€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1529 | +0.084 | +393.30€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1529 | +0.084 | +393.30€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 602 | +0.081 | +146.80€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 602 | +0.081 | +146.80€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 546 | +0.057 | +84.34€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 546 | +0.057 | +84.34€ | 2 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 381 | +0.127 | +162.17€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 381 | +0.127 | +162.17€ | 3 | 10 |
| ✅ LATE_WINDOW_5MIN | 167 | +0.281 | +166.63€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 167 | +0.281 | +166.63€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 167 | +0.281 | +166.63€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 167 | +0.281 | +166.63€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3417 | +0.102 | +846.33€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3417 | +0.102 | +846.33€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3417 | +0.102 | +846.33€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3417 | +0.102 | +846.33€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 538 | -0.041 | -17.80€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 538 | -0.041 | -17.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 150 | -0.013 | +2.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 150 | -0.013 | +2.57€ | 2 | 1 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 104 | -0.028 | -2.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 104 | -0.028 | -2.63€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 203 | -0.007 | -0.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 203 | -0.007 | -0.87€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 3746 | +0.015 | +82.87€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3746 | +0.015 | +82.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 181 | +0.019 | -2.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 181 | +0.019 | -2.82€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 794 | +0.007 | +29.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 794 | +0.007 | +29.41€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE | 207 | -0.012 | -4.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 207 | -0.012 | -4.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1357 | +0.026 | +32.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1357 | +0.026 | +32.36€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 757 | +0.011 | +1.48€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 757 | +0.011 | +1.48€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 450 | +0.015 | +26.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 450 | +0.015 | +26.62€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1765 | -0.040 | -28.09€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1765 | -0.040 | -28.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 509 | -0.032 | -12.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 509 | -0.032 | -12.63€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 603 | -0.014 | +6.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 603 | -0.014 | +6.72€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 653 | -0.070 | -22.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 653 | -0.070 | -22.18€ | 6 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 8863 | -0.027 | +4.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 4205 | -0.037 | -83.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 4658 | -0.019 | +87.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 266 | -0.041 | -11.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 135 | -0.025 | -1.89€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 131 | -0.056 | -9.54€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 2203 | -0.020 | +13.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1050 | -0.026 | -5.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1153 | -0.015 | +18.93€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 971 | -0.024 | +13.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 484 | -0.043 | -13.46€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 487 | -0.005 | +27.14€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 1946 | -0.040 | -55.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 906 | -0.052 | -53.47€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1040 | -0.030 | -1.59€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1735 | -0.018 | +37.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 828 | -0.030 | -2.22€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 907 | -0.007 | +39.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1742 | -0.031 | +6.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 802 | -0.039 | -6.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 940 | -0.024 | +13.11€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 50237 | -0.000 | +2512.82€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 50237 | -0.000 | +2512.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 9054 | +0.026 | +1156.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 9054 | +0.026 | +1156.18€ | 2 | 5 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 7227 | -0.033 | -93.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 7227 | -0.033 | -93.75€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 9169 | +0.025 | +949.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 9169 | +0.025 | +949.87€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 7074 | -0.047 | -143.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 7074 | -0.047 | -143.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 8493 | -0.004 | +237.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 8493 | -0.004 | +237.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 9220 | +0.015 | +405.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 9220 | +0.015 | +405.60€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6652 | -0.059 | -160.38€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6652 | -0.059 | -160.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1735 | -0.078 | -44.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1735 | -0.078 | -44.56€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 55 | -0.061 | -2.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 55 | -0.061 | -2.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 775 | -0.120 | -33.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 775 | -0.120 | -33.97€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2005 | -0.073 | -38.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2005 | -0.073 | -38.15€ | 3 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 124540 | -0.076 | +1597.44€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 124540 | -0.076 | +1597.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 21669 | -0.077 | +1071.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 21669 | -0.077 | +1071.21€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 18758 | -0.101 | -1019.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 18758 | -0.101 | -1019.05€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 21960 | -0.068 | +1194.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 21960 | -0.068 | +1194.28€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 18302 | -0.097 | -624.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 18302 | -0.097 | -624.53€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 22290 | -0.057 | +302.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 22290 | -0.057 | +302.08€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 21561 | -0.067 | +673.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 21561 | -0.067 | +673.46€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8768 | -0.034 | -183.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8768 | -0.034 | -183.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1001 | -0.017 | -18.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1001 | -0.017 | -18.91€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1988 | -0.046 | -25.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1988 | -0.046 | -25.22€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2601 | -0.027 | -42.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2601 | -0.027 | -42.85€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1199 | -0.055 | -28.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1199 | -0.055 | -28.27€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 971 | -0.031 | -35.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 971 | -0.031 | -35.95€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1688 | +0.123 | +685.51€ | 0 | 6 |
| ✅ ORDER_FLOW_5M#5min | 1552 | +0.129 | +672.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 361 | +0.136 | +179.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 361 | +0.136 | +179.73€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 319 | +0.117 | +109.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 319 | +0.117 | +109.30€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#ETH | 309 | +0.137 | +150.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 309 | +0.137 | +150.62€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 275 | +0.150 | +149.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 275 | +0.150 | +149.73€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 288 | +0.100 | +83.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 288 | +0.100 | +83.53€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1474 | -0.016 | -20.90€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1474 | -0.016 | -20.90€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 290 | -0.003 | +8.19€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 290 | -0.003 | +8.19€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 254 | -0.016 | -0.45€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 254 | -0.016 | -0.45€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 383 | -0.045 | -31.32€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 383 | -0.045 | -31.32€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 312 | +0.006 | +2.16€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 312 | +0.006 | +2.16€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 235 | -0.011 | +0.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 235 | -0.011 | +0.52€ | 0 | 0 |
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
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 385 | -0.213 | -42.68€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 57 | -0.178 | -0.23€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 388 | -0.210 | -34.11€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 340 | -0.222 | -41.12€ | 3 | 0 |
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
| ✅ STREAK_FADE_15M | 726 | +0.030 | +38.10€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 726 | +0.030 | +38.10€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 303 | +0.025 | +3.85€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 303 | +0.025 | +3.85€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 60 | -0.016 | -2.15€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 60 | -0.016 | -2.15€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 73 | -0.007 | +0.78€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 73 | -0.007 | +0.78€ | 3 | 1 |
| ✅ STREAK_FADE_15M#XRP | 290 | +0.055 | +35.62€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 290 | +0.055 | +35.62€ | 0 | 5 |
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
| ✅ STREAK_FADE_60M | 102 | -0.058 | -9.71€ | 5 | 0 |
| ✅ STREAK_FADE_60M#60min | 102 | -0.058 | -9.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 43 | -0.100 | -5.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 43 | -0.100 | -5.07€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 59 | -0.025 | -4.64€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 59 | -0.025 | -4.64€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 10910 | +0.016 | +86.03€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 10910 | +0.016 | +86.03€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2792 | +0.020 | +27.71€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2792 | +0.020 | +27.71€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2847 | +0.019 | +37.07€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2847 | +0.019 | +37.07€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2888 | +0.009 | -0.95€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2888 | +0.009 | -0.95€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2383 | +0.016 | +22.20€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2383 | +0.016 | +22.20€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 9914 | +0.013 | -50.70€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 9914 | +0.013 | -50.70€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4042 | +0.017 | -9.22€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4042 | +0.017 | -9.22€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3616 | +0.011 | -27.14€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3616 | +0.011 | -27.14€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2256 | +0.009 | -14.34€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2256 | +0.009 | -14.34€ | 1 | 0 |
| ✅ UPDOWN_GBM | 77248 | +0.053 | +6841.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 19204 | +0.083 | +4225.92€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2475 | +0.003 | +22.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 50732 | +0.050 | +2504.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 4566 | +0.007 | +88.70€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6851 | +0.089 | +1075.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1576 | +0.156 | +698.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5198 | +0.070 | +378.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 16672 | +0.055 | +1433.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2495 | +0.090 | +613.73€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 666 | +0.009 | +10.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 11383 | +0.061 | +745.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2030 | +0.004 | +61.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 98 | -0.070 | +3.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8485 | +0.070 | +899.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1555 | +0.147 | +610.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6852 | +0.052 | +290.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 17753 | +0.044 | +1155.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 4550 | +0.066 | +673.21€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 649 | +0.005 | +15.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 10862 | +0.044 | +447.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1601 | +0.010 | +17.04€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 91 | -0.102 | +2.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 16964 | +0.032 | +841.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 4820 | +0.035 | +407.00€ | 0 | 4 |
| ✅ UPDOWN_GBM#SOL#240min | 617 | -0.009 | -0.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 10512 | +0.037 | +429.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 935 | +0.008 | +10.38€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 80 | -0.134 | -5.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 10521 | +0.064 | +1436.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4208 | +0.102 | +1222.94€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 5925 | +0.041 | +213.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 269 | -0.102 | +1.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 844 | +0.365 | +311.90€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 844 | +0.365 | +311.90€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 438 | +0.364 | +152.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 438 | +0.364 | +152.73€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 406 | +0.365 | +159.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 406 | +0.365 | +159.18€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 19981 | -0.025 | +4639.05€ | 2 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 19981 | -0.025 | +4639.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3559 | -0.112 | +129.81€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3559 | -0.112 | +129.81€ | 4 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2439 | +0.218 | +1596.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2439 | +0.218 | +1596.74€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5718 | -0.067 | +653.50€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5718 | -0.067 | +653.50€ | 5 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5599 | -0.065 | +985.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5599 | -0.065 | +985.73€ | 2 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 232 | +0.047 | +11.12€ | 0 | 2 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 232 | +0.047 | +11.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 232 | +0.047 | +11.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 232 | +0.047 | +11.12€ | 0 | 2 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1437 | +0.294 | +1243.29€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1437 | +0.294 | +1243.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 772 | +0.291 | +631.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 772 | +0.291 | +631.55€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 665 | +0.296 | +611.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 665 | +0.296 | +611.74€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 815 | -0.112 | -83.16€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 815 | -0.112 | -83.16€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 248 | -0.080 | -18.10€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 248 | -0.080 | -18.10€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 87 | -0.163 | -9.15€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 87 | -0.163 | -9.15€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 97 | -0.187 | -6.55€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 97 | -0.187 | -6.55€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 3650 | +0.303 | +1718.05€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1344 | +0.256 | +168.08€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1403 | +0.299 | +626.40€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 903 | +0.380 | +923.57€ | 0 | 1 |