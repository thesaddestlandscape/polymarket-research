# Hipótesis automáticas — 2026-10-21 05:13 UTC
_Generado por shadow_postmortem.py sobre 989511 resoluciones (PNL=+129105.93€)_

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
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.233 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.144)

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
- **FILTRO** `restante_s_al_confirmar` < `142.39` → IC=-0.202 (n=10105)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 142.39
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=30317)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `128.76` → IC=-0.259 (n=1127)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.76
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3382)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `121.52` → IC=-0.287 (n=1080)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 121.52
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=3243)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `167.36` → IC=-0.204 (n=2670)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 167.36
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=8010)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `133.39` → IC=-0.275 (n=1974)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.39
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=5922)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.214 (n=21836)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.108)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=4343)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `9095.7535` → IC=+0.174 (n=1966)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 9095.7535 (IC base=+0.108)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.130 (n=18546)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.129 (n=33339)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 11.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.227 (n=17352)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.149 (n=7219)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `7066.4098` → IC=+0.159 (n=2790)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 7066.4098 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.199 (n=2029)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.364 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.194 (n=2492)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `16441.1339` → IC=+0.196 (n=646)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 16441.1339 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.190 (n=1786)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 7.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.188 (n=1990)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 17.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.186 (n=2551)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `16197.5868` → IC=+0.194 (n=658)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 16197.5868 (IC base=+0.184)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.170 (n=471)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.61 (IC base=+0.081)

- **PATRÓN** `libro_liquidez` > `6857.6712` → IC=+0.167 (n=124)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 6857.6712 (IC base=+0.081)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.139 (n=1129)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.44 (IC base=+0.084)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=4225)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.161 (n=3589)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 15.0 (IC base=+0.161)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.371 (n=1389)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.225 (n=781)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.347 (n=736)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.214 (n=2196)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.210)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=1065)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.149 (n=691)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 11.0 (IC base=+0.143)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.262 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=835)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `2205.3811` → IC=+0.162 (n=462)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2205.3811 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.162 (n=152)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.068)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.255 (n=846)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.419 (n=1153)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.150 (n=1290)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.158 (n=680)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 7.0 (IC base=+0.149)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.285 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=856)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.149)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `9.0` → IC=+0.168 (n=320)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 9.0 (IC base=+0.151)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.347 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.151)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.141 (n=204)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.02 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.136 (n=1134)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 7.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.245 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.123)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `11.0` → IC=-0.297 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.207 (n=18410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.203 (n=15624)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.235 (n=7596)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.201)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.181 (n=4243)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.182 (n=4232)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 18.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.183 (n=4156)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.73 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.181 (n=3471)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.224 (n=2178)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.226 (n=2290)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.306 (n=761)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.222)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=4173)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.184 (n=3550)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 15.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.188 (n=3278)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.258 (n=3621)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.248)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.361 (n=1172)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=4088)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=3496)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.194 (n=3020)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.190)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.433 (n=784)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.441 (n=809)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.430 (n=830)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `4200.997` → IC=+0.436 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4200.997 (IC base=+0.426)

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

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=24148)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.196 (n=3556)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.189 (n=7628)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 12.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.201 (n=10723)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.186)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=5000)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.226 (n=4912)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.286 (n=3499)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.191 (n=4107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.212 (n=5471)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.182)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.234 (n=3353)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.223 (n=3846)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.278 (n=3403)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.206 (n=9168)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.261 (n=3555)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=3987)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.197 (n=3450)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 5.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.243 (n=5003)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=8717)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=8526)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `3.76` → IC=+0.136 (n=10434)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.76 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=4312)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.143 (n=4357)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=5233)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `2.76` → IC=+0.146 (n=3930)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.76 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.189 (n=4405)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.135 (n=4642)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `3.33` → IC=+0.134 (n=5253)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 3.33 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.301 (n=1664)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.293 (n=1638)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.382 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.293)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.287 (n=755)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.356 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `5029.6626` → IC=+0.290 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5029.6626 (IC base=+0.279)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.321 (n=539)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.301 (n=788)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.297)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.391 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.297)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.298 (n=658)

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
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.442 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.444 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.442 (n=874)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.441)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.438 (n=366)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.436 (n=249)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.437 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.437 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.434)

- **PATRÓN** `libro_liquidez` > `5360.5654` → IC=+0.433 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5360.5654 (IC base=+0.434)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.469 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.449)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.452 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.449)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4759` → IC=+0.139 (n=13430)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.4759 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.125 (n=13559)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.124 (n=9375)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.3786` → IC=+0.166 (n=13429)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.3786 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.7815` → IC=+0.270 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7815 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.904` → IC=+0.191 (n=5082)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 5.904 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.2036` → IC=+0.258 (n=3909)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2036 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `0.6189` → IC=+0.264 (n=3908)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6189 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.3026` → IC=+0.242 (n=1367)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3026 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` > `2.3458` → IC=+0.229 (n=4334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3458 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.124 (n=11276)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.6849` → IC=+0.129 (n=18772)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.6849 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` < `0.6961` → IC=+0.185 (n=2834)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6961 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.0502` → IC=+0.183 (n=2917)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.0502 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2954` → IC=+0.234 (n=1605)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2954 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `1.874` → IC=+0.201 (n=7294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.874 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.6772` → IC=+0.206 (n=3647)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6772 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.222 (n=10794)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 106.0 (IC base=+0.075)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.210 (n=977)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.3472` → IC=+0.205 (n=2921)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3472 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.212 (n=1423)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.205 (n=1953)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `0.981` → IC=+0.280 (n=1324)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.981 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.865` → IC=+0.283 (n=1279)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.865 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.2333` → IC=+0.251 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2333 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `1.4388` → IC=+0.202 (n=2784)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4388 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=3135)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `2076.2686` → IC=+0.207 (n=974)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2076.2686 (IC base=+0.201)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.218 (n=1758)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.239 (n=2446)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.237 (n=1108)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0077 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.0867` → IC=+0.273 (n=814)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0867 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.253 (n=894)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.5313` → IC=+0.259 (n=2442)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5313 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.0944` → IC=+0.239 (n=2190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0944 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.261 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.4411` → IC=+0.243 (n=769)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4411 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.662` → IC=+0.245 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.662 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1626.88` → IC=+0.247 (n=2181)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1626.88 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.239 (n=815)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.237)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.237 (n=1059)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.230 (n=1086)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.1057` → IC=+0.260 (n=1054)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1057 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.239 (n=2503)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.9489` → IC=+0.278 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9489 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `0.1296` → IC=+0.234 (n=1282)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1296 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.349` → IC=+0.263 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.349 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` < `1.2316` → IC=+0.228 (n=2394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2316 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `0.6225` → IC=+0.232 (n=2394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6225 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2776` → IC=+0.266 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2776 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `2.4423` → IC=+0.256 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4423 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.151 (n=2439)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0057 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.168 (n=814)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.153 (n=926)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.725` → IC=+0.176 (n=2437)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.725 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.992` → IC=+0.148 (n=393)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 10.992 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.188` → IC=+0.141 (n=2226)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 4.188 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `1.2041` → IC=+0.139 (n=2437)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.2041 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.0957` → IC=+0.160 (n=888)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0957 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `2.4537` → IC=+0.143 (n=2317)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4537 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `1.415` → IC=+0.134 (n=2317)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.415 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `217.0` → IC=+0.173 (n=989)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 217.0 (IC base=+0.132)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.222 (n=1017)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=3180)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.271 (n=1162)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.269` → IC=+0.275 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.269 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.200 (n=2691)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.3534` → IC=+0.212 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3534 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `2.6984` → IC=+0.211 (n=1336)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6984 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.202 (n=3633)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `1972.2784` → IC=+0.201 (n=1377)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1972.2784 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.224 (n=2394)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.4596` → IC=+0.225 (n=2394)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4596 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=1022)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.219 (n=1256)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.0182` → IC=+0.277 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0182 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.386` → IC=+0.248 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.386 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3474` → IC=+0.260 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3474 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.7242` → IC=+0.229 (n=1171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7242 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.221 (n=1431)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `2050.141` → IC=+0.223 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2050.141 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.222 (n=2248)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.142 (n=149)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=3675)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.162 (n=542)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0037 (IC base=+0.055)

- **PATRÓN** `ibs_20min` > `0.9529` → IC=+0.230 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9529 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` > `0.1401` → IC=+0.330 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1401 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` < `0.3359` → IC=+0.329 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3359 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.142` → IC=+0.190 (n=1164)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 5.142 (IC base=+0.055)

- **PATRÓN** `volumen_regimen` < `0.8577` → IC=+0.334 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8577 (IC base=+0.055)

- **PATRÓN** `volumen_regimen` > `1.2208` → IC=+0.345 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2208 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` < `0.1669` → IC=+0.327 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1669 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.2965` → IC=+0.347 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2965 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` < `1.4113` → IC=+0.350 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4113 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` > `2.2171` → IC=+0.327 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2171 (IC base=+0.055)

- **PATRÓN** `ballena_activa_n` < `132.0` → IC=+0.337 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 132.0 (IC base=+0.055)

- **PATRÓN** `ibs_20min` < `0.093` → IC=+0.174 (n=958)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.093 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` > `0.3288` → IC=+0.142 (n=459)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.3288 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` < `0.1306` → IC=+0.139 (n=1567)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.1306 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` < `0.8417` → IC=+0.148 (n=1136)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8417 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` > `1.1677` → IC=+0.142 (n=568)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.1677 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.202 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=+0.036)

- **PATRÓN** `volumen_spike_ratio` < `1.7769` → IC=+0.140 (n=1088)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.7769 (IC base=+0.036)

- **PATRÓN** `volumen_spike_ratio` > `2.1545` → IC=+0.151 (n=740)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.1545 (IC base=+0.036)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.170 (n=104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=560)

- **FILTRO** `ibs_20min` < `0.2759` → IC=-0.195 (n=165)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2759
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=499)

- **FILTRO** `ibs_20min` > `0.2167` → IC=-0.132 (n=3605)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2167
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=1778)

- **FILTRO** `sigma_ewma_delta_pct` > `8.665` → IC=-0.239 (n=565)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.665
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=4818)

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

- **PATRÓN** `ibs_20min` < `0.2167` → IC=+0.147 (n=1778)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.2167 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` > `0.2659` → IC=+0.279 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2659 (IC base=-0.040)

- **PATRÓN** `volumen_regimen` < `0.7051` → IC=+0.304 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7051 (IC base=-0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.0806` → IC=+0.306 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0806 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` < `2.43` → IC=+0.301 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.43 (IC base=-0.040)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6095` → IC=-0.179 (n=987)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6095
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=2964)

- **FILTRO** `ibs_20min` < `0.755` → IC=-0.150 (n=2607)

  - _Acción_: SKIP cuando `ibs_20min` < 0.755
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=1344)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.162 (n=961)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=2990)

- **FILTRO** `ibs_20min` > `0.75` → IC=-0.205 (n=1418)

  - _Acción_: SKIP cuando `ibs_20min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=4269)

- **PATRÓN** `dist_vwap_pct` > `0.709` → IC=+0.337 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.709 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` < `0.2479` → IC=+0.303 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2479 (IC base=-0.066)

- **PATRÓN** `volumen_regimen` > `0.7043` → IC=+0.317 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7043 (IC base=-0.066)

- **PATRÓN** `volumen_pendiente_norm` < `0.0999` → IC=+0.301 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0999 (IC base=-0.066)

- **PATRÓN** `volumen_pendiente_norm` > `0.0719` → IC=+0.309 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0719 (IC base=-0.066)

- **PATRÓN** `volumen_spike_ratio` < `1.4142` → IC=+0.319 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4142 (IC base=-0.066)

- **PATRÓN** `volumen_spike_ratio` > `1.8402` → IC=+0.309 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8402 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` > `0.7986` → IC=+0.275 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7986 (IC base=-0.006)

- **PATRÓN** `volumen_regimen` > `1.0669` → IC=+0.284 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0669 (IC base=-0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.1038` → IC=+0.282 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1038 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` < `2.1788` → IC=+0.264 (n=1264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1788 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` > `1.4295` → IC=+0.265 (n=1437)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4295 (IC base=-0.006)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.210 (n=5884)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.32` → IC=+0.169 (n=17644)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.32 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.9499` → IC=+0.300 (n=1298)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9499 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.59` → IC=+0.161 (n=7917)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 3.59 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `1.1694` → IC=+0.264 (n=6499)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1694 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `0.6886` → IC=+0.270 (n=5805)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6886 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.2931` → IC=+0.279 (n=1453)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2931 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `1.4592` → IC=+0.263 (n=3457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4592 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `2.6435` → IC=+0.272 (n=3456)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6435 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.296 (n=9963)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.096)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.158 (n=5661)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0093 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.6578` → IC=+0.144 (n=16972)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.6578 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.7051` → IC=+0.262 (n=2358)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7051 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.195` → IC=+0.266 (n=1786)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.195 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2944` → IC=+0.317 (n=1151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2944 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.5798` → IC=+0.290 (n=3385)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5798 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.2663` → IC=+0.283 (n=3487)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2663 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.295 (n=7632)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 77.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.581` → IC=-0.128 (n=2420)

  - _Acción_: SKIP cuando `ibs_20min` < 0.581
  - _Potencial_: sin este filtro IC_bueno=+0.190 (n=2421)

- **FILTRO** `ibs_20min` > `0.7415` → IC=-0.215 (n=1018)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7415
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=3061)

- **FILTRO** `sigma_ewma_delta_pct` > `4.369` → IC=-0.208 (n=893)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.369
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=3186)

- **PATRÓN** `ibs_20min` > `0.9192` → IC=+0.315 (n=1211)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9192 (IC base=+0.031)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.992` → IC=+0.216 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.992 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.2286` → IC=+0.304 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2286 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` < `1.4426` → IC=+0.256 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4426 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` > `2.2427` → IC=+0.275 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2427 (IC base=+0.031)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.282 (n=1070)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.031)

- **PATRÓN** `ibs_20min` < `0.1645` → IC=+0.161 (n=1020)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1645 (IC base=-0.030)

- **PATRÓN** `volumen_pendiente_norm` < `0.0733` → IC=+0.412 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0733 (IC base=-0.030)

- **PATRÓN** `volumen_spike_ratio` < `2.5829` → IC=+0.407 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5829 (IC base=-0.030)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.400 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=-0.030)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1147` → IC=+0.213 (n=875)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1147 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `1.1944` → IC=+0.194 (n=1721)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 1.1944 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `0.6829` → IC=+0.202 (n=1537)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6829 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` < `0.0744` → IC=+0.191 (n=1581)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.0744 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.2755` → IC=+0.233 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2755 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `1.4234` → IC=+0.218 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4234 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` > `2.4856` → IC=+0.195 (n=565)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.4856 (IC base=+0.022)

- **PATRÓN** `ballena_activa_n` < `273.0` → IC=+0.227 (n=1130)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 273.0 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `0.6201` → IC=+0.234 (n=1105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6201 (IC base=-0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2716` → IC=+0.290 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2716 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.5339` → IC=+0.238 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5339 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.1626` → IC=+0.244 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1626 (IC base=-0.004)

- **PATRÓN** `ballena_activa_n` < `201.0` → IC=+0.241 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 201.0 (IC base=-0.004)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.310 (n=858)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.274 (n=2695)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.267)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.310 (n=1353)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.267)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.279` → IC=+0.302 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.279 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.281 (n=2240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` > `1.6102` → IC=+0.273 (n=2484)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6102 (IC base=+0.267)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.278 (n=3058)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.267)

- **PATRÓN** `libro_liquidez` > `2051.92` → IC=+0.285 (n=858)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2051.92 (IC base=+0.267)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.282 (n=1551)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.267)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.325 (n=1010)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.1808` → IC=+0.310 (n=979)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1808 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.320 (n=851)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.293)

- **PATRÓN** `ibs_20min` < `0.3701` → IC=+0.296 (n=2226)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3701 (IC base=+0.293)

- **PATRÓN** `ibs_20min` > `0.2604` → IC=+0.299 (n=1009)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2604 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.541` → IC=+0.310 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.541 (IC base=+0.293)

- **PATRÓN** `volumen_pendiente_norm` < `0.1969` → IC=+0.291 (n=2177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1969 (IC base=+0.293)

- **PATRÓN** `volumen_pendiente_norm` > `0.3414` → IC=+0.308 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3414 (IC base=+0.293)

- **PATRÓN** `volumen_spike_ratio` < `1.7293` → IC=+0.298 (n=935)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7293 (IC base=+0.293)

- **PATRÓN** `volumen_spike_ratio` > `2.6611` → IC=+0.302 (n=963)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6611 (IC base=+0.293)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.294 (n=1174)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `2043.0956` → IC=+0.306 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2043.0956 (IC base=+0.293)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.293 (n=1440)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.293)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7372` → IC=-0.188 (n=1068)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7372
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=3208)

- **PATRÓN** `ibs_20min` > `0.877` → IC=+0.175 (n=1016)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.877 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.1544` → IC=+0.236 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1544 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.2167` → IC=+0.232 (n=1216)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2167 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` < `1.0074` → IC=+0.244 (n=1254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0074 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` > `0.6697` → IC=+0.233 (n=1273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6697 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` < `0.1637` → IC=+0.237 (n=1515)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1637 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.1026` → IC=+0.250 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1026 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `1.3994` → IC=+0.247 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3994 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.265 (n=1232)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 102.0 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.1384` → IC=+0.234 (n=932)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1384 (IC base=-0.002)

- **PATRÓN** `volumen_regimen` < `1.0307` → IC=+0.239 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0307 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` < `0.1015` → IC=+0.250 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1015 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.291 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.7961` → IC=+0.271 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7961 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.4356` → IC=+0.254 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4356 (IC base=-0.002)

- **PATRÓN** `ballena_activa_n` < `109.0` → IC=+0.267 (n=832)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 109.0 (IC base=-0.002)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7619` → IC=-0.214 (n=1858)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7619
  - _Potencial_: sin este filtro IC_bueno=+0.306 (n=1858)

- **FILTRO** `ibs_20min` > `0.6471` → IC=-0.236 (n=906)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6471
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=2721)

- **FILTRO** `sigma_ewma_delta_pct` > `8.508` → IC=-0.245 (n=422)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.508
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=3205)

- **PATRÓN** `ibs_20min` > `0.7619` → IC=+0.306 (n=1858)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7619 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` > `0.2143` → IC=+0.338 (n=825)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2143 (IC base=+0.046)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.526` → IC=+0.186 (n=577)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 9.526 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` < `0.8453` → IC=+0.335 (n=930)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8453 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` > `0.7023` → IC=+0.326 (n=1246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7023 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` < `0.159` → IC=+0.323 (n=1442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.159 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.2751` → IC=+0.353 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2751 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` < `1.4368` → IC=+0.350 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4368 (IC base=+0.046)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.341 (n=1187)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.046)

- **PATRÓN** `ibs_20min` < `0.6471` → IC=+0.121 (n=2721)

  - _Acción_: Kelly boost +0.60€ cuando `ibs_20min` < 0.6471 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` < `0.2053` → IC=+0.252 (n=1115)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2053 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` < `0.7017` → IC=+0.263 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7017 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.0762` → IC=+0.264 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0762 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` < `2.4243` → IC=+0.254 (n=1154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4243 (IC base=+0.032)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.271 (n=1172)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.032)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.347 (n=1751)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.304)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.307 (n=764)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.304)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.314 (n=935)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.304)

- **PATRÓN** `ibs_20min` > `0.66` → IC=+0.336 (n=1960)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.66 (IC base=+0.304)

- **PATRÓN** `dist_vwap_pct` > `0.2066` → IC=+0.330 (n=1104)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2066 (IC base=+0.304)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.798` → IC=+0.324 (n=951)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.798 (IC base=+0.304)

- **PATRÓN** `volumen_regimen` > `0.6266` → IC=+0.312 (n=1959)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6266 (IC base=+0.304)

- **PATRÓN** `volumen_pendiente_norm` > `0.2788` → IC=+0.346 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2788 (IC base=+0.304)

- **PATRÓN** `volumen_spike_ratio` > `1.425` → IC=+0.315 (n=1879)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.425 (IC base=+0.304)

- **PATRÓN** `libro_liquidez` > `2626.4292` → IC=+0.311 (n=1306)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2626.4292 (IC base=+0.304)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.337 (n=1683)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.304)

- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.335 (n=1380)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.304)

- **PATRÓN** `drift_60min` |x|≤ `0.1867` → IC=+0.306 (n=911)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1867 (IC base=+0.304)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.315 (n=802)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.304)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.305 (n=1016)
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

- **PATRÓN** `volumen_spike_ratio` < `1.4161` → IC=+0.312 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4161 (IC base=+0.304)

- **PATRÓN** `volumen_spike_ratio` > `2.1353` → IC=+0.306 (n=859)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1353 (IC base=+0.304)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.226 (n=4340)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.0869` → IC=+0.202 (n=4347)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0869 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=13487)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.5576` → IC=+0.235 (n=13020)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5576 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.1642` → IC=+0.208 (n=5260)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1642 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.361` → IC=+0.256 (n=3417)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.361 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.1872` → IC=+0.169 (n=8638)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1872 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` > `0.624` → IC=+0.165 (n=8638)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.624 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.206 (n=1897)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6117` → IC=+0.191 (n=4208)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6117 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `1977.79` → IC=+0.181 (n=11632)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 1977.79 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.198 (n=11929)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 94.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.185 (n=8337)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.007 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.0796` → IC=+0.228 (n=4171)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0796 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=4659)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.237 (n=12504)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.005` → IC=+0.199 (n=2035)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 10.005 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.685` → IC=+0.182 (n=11023)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 2.685 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.1819` → IC=+0.163 (n=8920)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1819 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2939` → IC=+0.225 (n=1848)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2939 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6363` → IC=+0.186 (n=3914)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6363 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.193 (n=11470)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 100.0 (IC base=+0.180)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.236 (n=728)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.3316` → IC=+0.234 (n=2183)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3316 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.220 (n=2276)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.222 (n=1470)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.9275` → IC=+0.295 (n=1455)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9275 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.939` → IC=+0.331 (n=694)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.939 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.2806` → IC=+0.274 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2806 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `1.4363` → IC=+0.216 (n=2064)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4363 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=2363)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.216)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.252 (n=1694)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0082 (IC base=+0.250)

- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.262 (n=770)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.250)

- **PATRÓN** `drift_60min` |x|≤ `0.0938` → IC=+0.303 (n=743)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0938 (IC base=+0.250)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.254 (n=1727)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.250)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.253 (n=819)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.250)

- **PATRÓN** `ibs_20min` < `0.2966` → IC=+0.274 (n=1486)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2966 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` < `0.1002` → IC=+0.252 (n=1473)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1002 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` > `0.2974` → IC=+0.291 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2974 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` < `1.4328` → IC=+0.272 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4328 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` > `2.6858` → IC=+0.253 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6858 (IC base=+0.250)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.254 (n=1903)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.250)

- **PATRÓN** `libro_liquidez` > `1527.7502` → IC=+0.259 (n=1688)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1527.7502 (IC base=+0.250)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.254 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.250)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.218 (n=657)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.1596` → IC=+0.182 (n=1311)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.1596 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=2065)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.3323` → IC=+0.222 (n=1965)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3323 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.1357` → IC=+0.213 (n=1169)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1357 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.29` → IC=+0.220 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.29 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.6921` → IC=+0.162 (n=865)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.6921 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.194 (n=315)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `1.5085` → IC=+0.168 (n=848)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.5085 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `2.4993` → IC=+0.166 (n=642)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.4993 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `228.0` → IC=+0.166 (n=832)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 228.0 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.169 (n=2059)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0058 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.2342` → IC=+0.173 (n=1809)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2342 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.184 (n=987)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.6154` → IC=+0.205 (n=2056)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6154 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.465` → IC=+0.194 (n=390)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 11.465 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.2065` → IC=+0.159 (n=2056)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2065 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.0934` → IC=+0.147 (n=1745)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.0934 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.4999` → IC=+0.152 (n=1936)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4999 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.4241` → IC=+0.145 (n=1935)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.4241 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `201.0` → IC=+0.176 (n=624)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 201.0 (IC base=+0.144)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.237 (n=1000)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.3996` → IC=+0.225 (n=1939)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3996 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.221 (n=2277)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=1141)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.418` → IC=+0.301 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.418 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` < `0.0994` → IC=+0.215 (n=1887)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0994 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.3545` → IC=+0.233 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3545 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `1.7691` → IC=+0.215 (n=939)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7691 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.7129` → IC=+0.228 (n=968)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7129 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=2630)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `1958.5384` → IC=+0.228 (n=998)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1958.5384 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.0087` → IC=+0.253 (n=1259)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0087 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.2503` → IC=+0.265 (n=1260)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2503 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.280 (n=717)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.0095` → IC=+0.299 (n=831)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0095 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.484` → IC=+0.272 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.484 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.3556` → IC=+0.280 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3556 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` < `1.744` → IC=+0.237 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.744 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.1531` → IC=+0.237 (n=1202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1531 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `2042.7468` → IC=+0.242 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2042.7468 (IC base=+0.235)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.238 (n=1203)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.235)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.172 (n=2113)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0074 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.0759` → IC=+0.197 (n=705)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.0759 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=2188)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.3116` → IC=+0.213 (n=2113)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3116 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.1443` → IC=+0.198 (n=1286)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1443 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.82` → IC=+0.197 (n=490)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 9.82 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `1.0223` → IC=+0.158 (n=1860)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.0223 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1036` → IC=+0.178 (n=867)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1036 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `1.8218` → IC=+0.151 (n=1381)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.8218 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `2.5084` → IC=+0.170 (n=691)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.5084 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `4615.2008` → IC=+0.185 (n=1409)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 4615.2008 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.158 (n=2057)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 139.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.155 (n=2213)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0072 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.395` → IC=+0.145 (n=2213)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.395 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.166 (n=1053)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.684` → IC=+0.187 (n=2213)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.684 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.1535` → IC=+0.157 (n=2209)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1535 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.583` → IC=+0.161 (n=546)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 9.583 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.8551` → IC=+0.156 (n=1476)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8551 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2997` → IC=+0.194 (n=334)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2997 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.8098` → IC=+0.136 (n=1383)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.8098 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `1.4241` → IC=+0.128 (n=2073)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.4241 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `7455.0586` → IC=+0.191 (n=1003)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 7455.0586 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `68.0` → IC=+0.149 (n=908)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 68.0 (IC base=+0.128)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.178 (n=1076)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0103 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.4402` → IC=+0.129 (n=2089)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.4402 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.172 (n=1135)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 15.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `0.4878` → IC=+0.216 (n=2374)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4878 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `0.1961` → IC=+0.191 (n=1381)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1961 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.527` → IC=+0.279 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.527 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `1.1724` → IC=+0.144 (n=2374)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1724 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` < `0.161` → IC=+0.135 (n=2409)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.161 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.4382` → IC=+0.149 (n=768)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4382 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.130 (n=2487)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `2765.4937` → IC=+0.209 (n=1076)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2765.4937 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.159 (n=726)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 19.0 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.140 (n=2424)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0108 (IC base=+0.121)

- **PATRÓN** `drift_60min` |x|≤ `0.1081` → IC=+0.173 (n=809)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.1081 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.141 (n=2463)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.220 (n=2429)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.383` → IC=+0.122 (n=485)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` > 7.383 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.467` → IC=+0.133 (n=2143)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 2.467 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.1753` → IC=+0.129 (n=2424)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1753 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` < `0.1652` → IC=+0.124 (n=2346)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1652 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.2757` → IC=+0.149 (n=323)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.2757 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.4463` → IC=+0.134 (n=753)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.4463 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` > `2.4249` → IC=+0.137 (n=753)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.4249 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2646.993` → IC=+0.190 (n=1099)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2646.993 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.131 (n=1976)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 42.0 (IC base=+0.121)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.246 (n=1954)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0131 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.1286` → IC=+0.240 (n=733)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1286 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.227 (n=2263)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.227 (n=1963)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.66` → IC=+0.259 (n=2193)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.66 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` > `0.1837` → IC=+0.228 (n=1412)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1837 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.606` → IC=+0.250 (n=995)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.606 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `1.1781` → IC=+0.225 (n=2188)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1781 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `0.6187` → IC=+0.231 (n=2187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6187 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.2826` → IC=+0.275 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2826 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `2.4697` → IC=+0.228 (n=2128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4697 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `1.8081` → IC=+0.233 (n=1419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8081 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `2604.0706` → IC=+0.224 (n=1458)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2604.0706 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.233 (n=983)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.229)

- **PATRÓN** `sigma_h` > `0.0226` → IC=+0.239 (n=1011)
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

- **PATRÓN** `ibs_20min` < `0.43` → IC=+0.257 (n=2232)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.43 (IC base=+0.229)

- **PATRÓN** `dist_vwap_pct` > `0.2951` → IC=+0.237 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2951 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.326` → IC=+0.261 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.326 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` > `0.6394` → IC=+0.236 (n=2229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6394 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.284 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `1.4386` → IC=+0.232 (n=2075)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4386 (IC base=+0.229)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.208 (n=1472)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.183)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.190 (n=1112)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0089 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.1295` → IC=+0.201 (n=1469)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1295 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.215 (n=1657)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.4871` → IC=+0.218 (n=2980)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4871 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.7906` → IC=+0.203 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7906 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.62` → IC=+0.212 (n=1444)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.62 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.8634` → IC=+0.205 (n=1998)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8634 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.0999` → IC=+0.192 (n=1196)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0999 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` < `1.4312` → IC=+0.197 (n=1081)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.4312 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.4942` → IC=+0.187 (n=1081)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.4942 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.189 (n=3767)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.02 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `2674.7773` → IC=+0.189 (n=2980)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2674.7773 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.135 (n=1204)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0038 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.3824` → IC=+0.162 (n=2404)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.3824 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.127 (n=1541)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 27.0 (IC base=+0.088)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.202 (n=411)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.3269` → IC=+0.200 (n=931)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3269 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.206 (n=849)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.6364` → IC=+0.236 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6364 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.3078` → IC=+0.196 (n=278)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.3078 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.079` → IC=+0.194 (n=397)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 3.079 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.112` → IC=+0.179 (n=896)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 4.112 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `0.8755` → IC=+0.203 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8755 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.0716` → IC=+0.183 (n=367)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.0716 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `2.2005` → IC=+0.187 (n=801)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.2005 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `1.4097` → IC=+0.180 (n=910)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4097 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `14694.0598` → IC=+0.183 (n=620)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 14694.0598 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `159.0` → IC=+0.210 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 159.0 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.186 (n=371)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0028 (IC base=+0.115)

- **PATRÓN** `drift_60min` |x|≤ `0.2682` → IC=+0.140 (n=975)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.2682 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.128 (n=1006)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 7.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.632` → IC=+0.164 (n=975)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.632 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` > `1.0687` → IC=+0.144 (n=503)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.0687 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.1608` → IC=+0.166 (n=294)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1608 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `2.1184` → IC=+0.128 (n=963)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 2.1184 (IC base=+0.115)

- **PATRÓN** `ballena_activa_n` < `221.0` → IC=+0.161 (n=721)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 221.0 (IC base=+0.115)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.247 (n=679)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.0943` → IC=+0.232 (n=341)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0943 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=1063)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.3758` → IC=+0.257 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3758 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `0.7883` → IC=+0.218 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7883 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` < `0.2076` → IC=+0.219 (n=909)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2076 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.882` → IC=+0.243 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.882 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` < `0.8363` → IC=+0.225 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8363 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `1.1643` → IC=+0.222 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1643 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.268` → IC=+0.254 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.268 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.4245` → IC=+0.240 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4245 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.4732` → IC=+0.236 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4732 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.213 (n=1140)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.213)

- **PATRÓN** `ibs_20min` < `0.104` → IC=+0.170 (n=346)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.104 (IC base=+0.064)

- **PATRÓN** `libro_liquidez` > `6239.7898` → IC=+0.134 (n=691)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 6239.7898 (IC base=+0.064)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.186 (n=278)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0107 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.5286` → IC=+0.168 (n=830)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.5286 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.222 (n=401)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.272 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.9779` → IC=+0.238 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9779 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.1` → IC=+0.237 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.1 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `1.0549` → IC=+0.187 (n=730)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 1.0549 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `0.7125` → IC=+0.175 (n=742)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.7125 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.1632` → IC=+0.189 (n=226)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1632 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.4446` → IC=+0.188 (n=267)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.4446 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `2.1798` → IC=+0.171 (n=363)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.1798 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.175 (n=860)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.02 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `3025.7279` → IC=+0.188 (n=277)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 3025.7279 (IC base=+0.167)

- **PATRÓN** `ibs_20min` < `0.5455` → IC=+0.137 (n=789)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.5455 (IC base=+0.056)

- **PATRÓN** `libro_liquidez` > `2703.0503` → IC=+0.145 (n=406)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 2703.0503 (IC base=+0.056)

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
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.228 (n=5653)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.193 (n=17635)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` > `0.4475` → IC=+0.232 (n=16960)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4475 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` > `0.8962` → IC=+0.211 (n=2091)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8962 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.253` → IC=+0.254 (n=4150)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.253 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` < `1.2221` → IC=+0.170 (n=11372)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.2221 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.2904` → IC=+0.207 (n=2256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2904 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `2.6132` → IC=+0.198 (n=5499)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.6132 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `1791.54` → IC=+0.184 (n=16960)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1791.54 (IC base=+0.184)

- **PATRÓN** `ballena_activa_n` < `112.0` → IC=+0.204 (n=15592)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 112.0 (IC base=+0.184)

- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.191 (n=13521)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0096 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.4907` → IC=+0.192 (n=15365)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.4907 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=5725)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.5833` → IC=+0.243 (n=15368)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5833 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.806` → IC=+0.207 (n=2132)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.806 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.559` → IC=+0.191 (n=14857)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 3.559 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `0.7044` → IC=+0.163 (n=4562)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.7044 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.2904` → IC=+0.253 (n=2076)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2904 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.2593` → IC=+0.196 (n=6590)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.2593 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.216 (n=9622)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.188)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.234 (n=924)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.3478` → IC=+0.229 (n=2767)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3478 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.239 (n=1345)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.229 (n=1859)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.330 (n=1098)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.483` → IC=+0.355 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.483 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2805` → IC=+0.287 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2805 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `2.2896` → IC=+0.236 (n=1205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2896 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.244 (n=2955)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2076.1925` → IC=+0.229 (n=922)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2076.1925 (IC base=+0.226)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.248 (n=1676)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.266 (n=2357)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.262)

- **PATRÓN** `drift_60min` |x|≤ `0.1192` → IC=+0.287 (n=1035)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1192 (IC base=+0.262)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.268 (n=2152)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.262)

- **PATRÓN** `ibs_20min` < `0.5111` → IC=+0.288 (n=2353)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5111 (IC base=+0.262)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.135` → IC=+0.265 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.135 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` < `0.0953` → IC=+0.262 (n=2116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0953 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` > `0.2866` → IC=+0.291 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2866 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` < `1.5578` → IC=+0.265 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5578 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` > `2.6411` → IC=+0.271 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6411 (IC base=+0.262)

- **PATRÓN** `libro_liquidez` > `1625.98` → IC=+0.271 (n=2102)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1625.98 (IC base=+0.262)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.271 (n=978)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.262)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.198 (n=921)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0028 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1044` → IC=+0.164 (n=1210)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1044 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=2860)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.3668` → IC=+0.223 (n=2456)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3668 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1264` → IC=+0.194 (n=1417)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1264 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.511` → IC=+0.159 (n=453)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 11.511 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.176` → IC=+0.153 (n=2397)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 3.176 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.6302` → IC=+0.172 (n=917)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.6302 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.0715` → IC=+0.152 (n=2451)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.0715 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2716` → IC=+0.184 (n=394)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2716 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.179` → IC=+0.157 (n=2366)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.179 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.5283` → IC=+0.156 (n=2402)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.5283 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `239.0` → IC=+0.184 (n=882)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 239.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.164 (n=2291)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.256` → IC=+0.164 (n=2015)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.256 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=863)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.6944` → IC=+0.197 (n=2288)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.6944 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.179` → IC=+0.158 (n=378)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 11.179 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.433` → IC=+0.144 (n=2306)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 6.433 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.1917` → IC=+0.152 (n=2288)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1917 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2175` → IC=+0.197 (n=427)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2175 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `2.4321` → IC=+0.149 (n=2183)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4321 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.7759` → IC=+0.153 (n=1455)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.7759 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=2971)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `274.0` → IC=+0.159 (n=921)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 274.0 (IC base=+0.143)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.259 (n=941)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=2944)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.227 (n=2525)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=1054)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.3` → IC=+0.324 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.3 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` < `0.097` → IC=+0.231 (n=2497)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.097 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `3.1837` → IC=+0.241 (n=914)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1837 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=3369)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `1821.4984` → IC=+0.234 (n=1882)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1821.4984 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.246 (n=2329)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.1804` → IC=+0.257 (n=1165)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1804 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.262 (n=997)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.241 (n=944)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.0328` → IC=+0.307 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0328 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.627` → IC=+0.295 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.627 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.3447` → IC=+0.302 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3447 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.1336` → IC=+0.250 (n=1679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1336 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.245 (n=1404)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1952.5984` → IC=+0.251 (n=1200)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1952.5984 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.258 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.241)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.205 (n=980)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.4209` → IC=+0.158 (n=2917)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4209 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=3021)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.2458` → IC=+0.194 (n=2918)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.2458 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1424` → IC=+0.172 (n=1550)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1424 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.122` → IC=+0.159 (n=1184)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.122 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.8651` → IC=+0.167 (n=1945)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8651 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.190 (n=378)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.525` → IC=+0.163 (n=1253)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.525 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.1748` → IC=+0.158 (n=1290)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.1748 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `6017.9372` → IC=+0.242 (n=1323)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6017.9372 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.169 (n=1229)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 73.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.151 (n=2420)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0075 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.4364` → IC=+0.140 (n=2419)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4364 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.155 (n=883)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.7354` → IC=+0.185 (n=2419)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.7354 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.1494` → IC=+0.146 (n=2202)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1494 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.104` → IC=+0.175 (n=370)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 11.104 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.6973` → IC=+0.146 (n=1065)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.6973 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2956` → IC=+0.219 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2956 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `2.2242` → IC=+0.132 (n=2049)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.2242 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.4292` → IC=+0.136 (n=2327)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4292 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `7156.4491` → IC=+0.212 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7156.4491 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `67.0` → IC=+0.133 (n=798)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 67.0 (IC base=+0.130)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.152 (n=1956)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0085 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.180 (n=1082)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.4426` → IC=+0.200 (n=2934)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4426 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `1.0577` → IC=+0.210 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0577 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.726` → IC=+0.265 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.726 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.2216` → IC=+0.137 (n=2935)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.2216 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1623` → IC=+0.126 (n=3053)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1623 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.131 (n=380)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.8311` → IC=+0.130 (n=1912)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.8311 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.1945` → IC=+0.128 (n=1300)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 2.1945 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.131 (n=3053)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2496.5462` → IC=+0.232 (n=1331)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2496.5462 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.142 (n=928)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 24.0 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.152 (n=2453)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.01 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.1336` → IC=+0.154 (n=930)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1336 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.130 (n=2871)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.6495` → IC=+0.212 (n=2788)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6495 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.252` → IC=+0.134 (n=2684)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 3.252 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.7106` → IC=+0.140 (n=1227)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.7106 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2245` → IC=+0.173 (n=475)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2245 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.4386` → IC=+0.151 (n=870)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4386 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2673.0464` → IC=+0.206 (n=929)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2673.0464 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.132 (n=2304)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 47.0 (IC base=+0.117)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0137` → IC=+0.252 (n=2476)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0137 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.237 (n=2887)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.235 (n=2002)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` > `0.6106` → IC=+0.272 (n=2476)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6106 (IC base=+0.232)

- **PATRÓN** `dist_vwap_pct` > `0.1894` → IC=+0.248 (n=1504)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1894 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.716` → IC=+0.272 (n=930)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.716 (IC base=+0.232)

- **PATRÓN** `volumen_regimen` < `1.2308` → IC=+0.238 (n=2772)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2308 (IC base=+0.232)

- **PATRÓN** `volumen_regimen` > `0.6398` → IC=+0.235 (n=2772)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6398 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.2872` → IC=+0.261 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2872 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.5001` → IC=+0.253 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5001 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.233 (n=3601)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `2959.1804` → IC=+0.236 (n=924)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2959.1804 (IC base=+0.232)

- **PATRÓN** `sigma_h` > `0.0255` → IC=+0.251 (n=958)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0255 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.237 (n=2702)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.230)

- **PATRÓN** `ibs_20min` < `0.5156` → IC=+0.265 (n=2873)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5156 (IC base=+0.230)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.19` → IC=+0.267 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.19 (IC base=+0.230)

- **PATRÓN** `volumen_regimen` > `1.2282` → IC=+0.258 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2282 (IC base=+0.230)

- **PATRÓN** `volumen_pendiente_norm` > `0.282` → IC=+0.296 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.282 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` > `1.4316` → IC=+0.232 (n=2670)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4316 (IC base=+0.230)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.194 (n=4991)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.245 (n=1706)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.5049` → IC=+0.220 (n=5116)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5049 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.227 (n=1867)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.9405` → IC=+0.249 (n=1705)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9405 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` > `0.7003` → IC=+0.213 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7003 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` < `0.2469` → IC=+0.212 (n=3270)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2469 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.0` → IC=+0.217 (n=840)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.0 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.583` → IC=+0.211 (n=4555)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.583 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` < `0.7051` → IC=+0.222 (n=1645)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7051 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` > `0.8832` → IC=+0.211 (n=2491)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8832 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` < `0.1068` → IC=+0.210 (n=4781)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1068 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.1665` → IC=+0.223 (n=1437)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1665 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.4541` → IC=+0.218 (n=1680)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4541 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.8451` → IC=+0.211 (n=3357)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8451 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.216 (n=3941)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2926.428` → IC=+0.217 (n=4570)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2926.428 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.240 (n=1254)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.4897` → IC=+0.209 (n=3756)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4897 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=1271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.209 (n=1677)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.7337` → IC=+0.199 (n=3756)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7337 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.6723` → IC=+0.202 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6723 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.828` → IC=+0.203 (n=3366)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.828 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `1.0967` → IC=+0.202 (n=3135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0967 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.197 (n=3442)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2229` → IC=+0.195 (n=758)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2229 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `1.5329` → IC=+0.198 (n=1629)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.5329 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `1.813` → IC=+0.199 (n=2466)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.813 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.194 (n=4991)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.193)

- **PATRÓN** `ballena_activa_n` < `171.0` → IC=+0.202 (n=3241)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 171.0 (IC base=+0.193)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.273 (n=673)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.260)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.260 (n=682)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.260)

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
- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.225 (n=333)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0072 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.3083` → IC=+0.185 (n=503)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.3083 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.207 (n=775)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` > `0.9259` → IC=+0.247 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9259 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` > `0.7421` → IC=+0.239 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7421 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.222` → IC=+0.207 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.222 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `0.6955` → IC=+0.228 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6955 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` < `0.1062` → IC=+0.197 (n=680)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.1062 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.0788` → IC=+0.192 (n=336)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0788 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `1.5672` → IC=+0.199 (n=323)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.5672 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `2.4766` → IC=+0.211 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4766 (IC base=+0.185)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.190 (n=878)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `3100.278` → IC=+0.205 (n=673)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3100.278 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.201 (n=736)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.185)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.212 (n=370)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.205)

- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.218 (n=186)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.6042` → IC=+0.227 (n=554)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6042 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.241 (n=377)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` < `0.7273` → IC=+0.227 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7273 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.8337` → IC=+0.216 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8337 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.3064` → IC=+0.207 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3064 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.792` → IC=+0.209 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.792 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.862` → IC=+0.213 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.862 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `1.1368` → IC=+0.210 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1368 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `0.9335` → IC=+0.209 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9335 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` < `0.1071` → IC=+0.226 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1071 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `2.1983` → IC=+0.241 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1983 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `2998.9426` → IC=+0.223 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2998.9426 (IC base=+0.205)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.236 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.205)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.160 (n=744)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.004 (IC base=+0.071)

- **PATRÓN** `ibs_20min` > `0.3885` → IC=+0.144 (n=1598)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.3885 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` > `0.3593` → IC=+0.159 (n=555)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.3593 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.973` → IC=+0.160 (n=465)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 8.973 (IC base=+0.071)

- **PATRÓN** `volumen_pendiente_norm` > `0.2759` → IC=+0.146 (n=221)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.2759 (IC base=+0.071)

- **PATRÓN** `ibs_20min` < `0.2186` → IC=+0.227 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2186 (IC base=+0.056)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.342` → IC=+0.171 (n=141)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 10.342 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.1466` → IC=+0.173 (n=243)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1466 (IC base=+0.056)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.134 (n=558)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0056 (IC base=+0.089)

- **PATRÓN** `ibs_20min` > `0.3558` → IC=+0.167 (n=527)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.3558 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` > `0.1227` → IC=+0.158 (n=264)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1227 (IC base=+0.089)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.123 (n=279)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0037 (IC base=+0.072)

- **PATRÓN** `ibs_20min` < `0.0556` → IC=+0.277 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0556 (IC base=+0.072)

- **PATRÓN** `volumen_pendiente_norm` > `0.2162` → IC=+0.201 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2162 (IC base=+0.072)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.128 (n=487)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.006 (IC base=+0.092)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.149 (n=212)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.092)

- **PATRÓN** `ibs_20min` > `0.4221` → IC=+0.175 (n=521)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.4221 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` > `0.1246` → IC=+0.190 (n=269)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1246 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.194` → IC=+0.250 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.194 (IC base=+0.092)

- **PATRÓN** `volumen_regimen` < `0.5758` → IC=+0.136 (n=174)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.5758 (IC base=+0.092)

- **PATRÓN** `volumen_pendiente_norm` > `0.2877` → IC=+0.171 (n=74)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2877 (IC base=+0.092)

- **PATRÓN** `ibs_20min` < `0.0289` → IC=+0.283 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0289 (IC base=+0.021)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.686` → IC=+0.229 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.686 (IC base=+0.021)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` > `0.16` → IC=-0.204 (n=69)

  - _Acción_: SKIP cuando `ibs_20min` > 0.16
  - _Potencial_: sin este filtro IC_bueno=+0.220 (n=209)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.169 (n=367)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.75 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` > `0.736` → IC=+0.147 (n=134)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.736 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.303` → IC=+0.158 (n=118)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 9.303 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.2283` → IC=+0.132 (n=104)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.2283 (IC base=+0.035)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.153 (n=240)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0105 (IC base=+0.073)

- **PATRÓN** `ibs_20min` < `0.16` → IC=+0.220 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.16 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.1699` → IC=+0.138 (n=197)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1699 (IC base=+0.073)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.474` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.474 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` > `1.0779` → IC=+0.208 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0779 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.1508` → IC=+0.234 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1508 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` < `2.1557` → IC=+0.151 (n=164)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.1557 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` > `1.4056` → IC=+0.160 (n=186)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.4056 (IC base=+0.073)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.143 (n=183)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.06 (IC base=+0.073)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1888` → IC=-0.310 (n=77)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1888
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=235)

- **FILTRO** `dist_vwap_pct` > `0.2321` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2321
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=297)

- **FILTRO** `volumen_regimen` < `0.7615` → IC=-0.312 (n=78)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7615
  - _Potencial_: sin este filtro IC_bueno=-0.164 (n=236)

- **FILTRO** `sigma_h` > `0.0052` → IC=-0.336 (n=65)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0052
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=199)

- **FILTRO** `dist_vwap_pct` > `0.4684` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4684
  - _Potencial_: sin este filtro IC_bueno=-0.277 (n=245)

- **FILTRO** `volumen_pendiente_norm` > `0.046` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.046
  - _Potencial_: sin este filtro IC_bueno=-0.273 (n=148)

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
  - _Potencial_: sin este filtro IC_bueno=-0.256 (n=88)

- **FILTRO** `volumen_spike_ratio` > `1.5538` → IC=-0.360 (n=41)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.5538
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=43)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.5786` → IC=-0.464 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5786
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=79)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.375 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=79)

- **FILTRO** `ibs_20min` > `0.725` → IC=-0.389 (n=34)

  - _Acción_: SKIP cuando `ibs_20min` > 0.725
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=67)

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

- **FILTRO** `dist_vwap_pct` > `0.0608` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0608
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=86)

- **FILTRO** `volumen_regimen` < `0.7468` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7468
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=84)

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
- **PATRÓN** `sigma_h` > `0.006` → IC=+0.201 (n=242)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=207)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.152 (n=530)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.6842 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.7432` → IC=+0.224 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7432 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.6225` → IC=+0.182 (n=177)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6225 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` < `0.1528` → IC=+0.151 (n=434)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.1528 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.3996` → IC=+0.176 (n=143)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.3996 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.1541` → IC=+0.147 (n=548)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.1541 (IC base=+0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.099` → IC=+0.181 (n=186)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 9.099 (IC base=+0.057)

- **PATRÓN** `libro_liquidez` > `3253.1348` → IC=+0.138 (n=415)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 3253.1348 (IC base=+0.057)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6933` → IC=-0.214 (n=54)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6933
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=165)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.187 (n=97)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0049 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.153 (n=197)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 12.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.149 (n=112)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 6.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.1681` → IC=+0.200 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1681 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.158` → IC=+0.169 (n=125)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 7.158 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `1.0364` → IC=+0.179 (n=132)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 1.0364 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` < `0.0706` → IC=+0.153 (n=226)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0706 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2726` → IC=+0.167 (n=49)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2726 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.5184` → IC=+0.171 (n=259)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 2.5184 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.5382` → IC=+0.150 (n=232)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.5382 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `4599.6467` → IC=+0.145 (n=260)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 4599.6467 (IC base=+0.138)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1263` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1263
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=173)

- **FILTRO** `ibs_20min` > `0.3277` → IC=-0.162 (n=75)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3277
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=227)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.140 (n=123)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0038 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.196 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=+0.099)

- **PATRÓN** `ibs_20min` > `0.9094` → IC=+0.156 (n=123)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.9094 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` < `0.0908` → IC=+0.139 (n=156)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.0908 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.022` → IC=+0.140 (n=137)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 3.022 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` < `0.6229` → IC=+0.188 (n=62)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.6229 (IC base=+0.099)

- **PATRÓN** `volumen_pendiente_norm` < `0.1263` → IC=+0.146 (n=173)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.1263 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` < `1.7963` → IC=+0.173 (n=105)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.7963 (IC base=+0.099)

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
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.254)

- **PATRÓN** `ibs_20min` > `0.6522` → IC=+0.277 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6522 (IC base=+0.254)

- **PATRÓN** `dist_vwap_pct` > `0.6502` → IC=+0.391 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6502 (IC base=+0.254)

- **PATRÓN** `dist_vwap_pct` < `0.224` → IC=+0.258 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.224 (IC base=+0.254)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.331` → IC=+0.320 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.331 (IC base=+0.254)

- **PATRÓN** `volumen_regimen` < `0.5792` → IC=+0.325 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5792 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` > `0.1037` → IC=+0.336 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1037 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` < `1.4833` → IC=+0.398 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4833 (IC base=+0.254)

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
- **PATRÓN** `libro_liquidez` > `2947.9372` → IC=+0.136 (n=421)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2947.9372 (IC base=+0.102)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2947.9372` → IC=+0.136 (n=421)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2947.9372 (IC base=+0.102)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=195)

- **FILTRO** `libro_liquidez` < `5333.1276` → IC=-0.164 (n=105)

  - _Acción_: SKIP cuando `libro_liquidez` < 5333.1276
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=106)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=312)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `10893.2451` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 10893.2451
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=70)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=36)

- **PATRÓN** `liq_n` > `6.0` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `liq_n` > 6.0 (IC base=-0.016)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=3543)

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
  - _Potencial_: sin este filtro IC_bueno=+0.099 (n=130)

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
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=1312)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=1266)

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
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=420)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=401)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.141 (n=179)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.495 (IC base=+0.023)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=842)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=842)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=835)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=835)

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
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=237)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=261)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=257)

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

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.178 (n=150)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.46 (IC base=+0.016)

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
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=170)

- **FILTRO** `profundidad_ratio` < `40.6` → IC=-0.159 (n=121)

  - _Acción_: SKIP cuando `profundidad_ratio` < 40.6
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=364)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.140 (n=201)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=226)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.167 (n=88)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=375)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.154 (n=128)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=467)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.164 (n=6076)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=18812)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.177 (n=6157)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=19398)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.193 (n=1112)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=3422)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.174 (n=1053)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=3507)

- **PATRÓN** `py_entrada` > `0.495` → IC=+0.129 (n=3052)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` > 0.495 (IC base=+0.041)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.143 (n=1197)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 1.0 (IC base=+0.041)

- **PATRÓN** `libro_liquidez` > `1292.08` → IC=+0.137 (n=2267)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 1292.08 (IC base=+0.041)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.126 (n=2136)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.5 (IC base=+0.011)

- **PATRÓN** `libro_liquidez` > `1490.6972` → IC=+0.152 (n=1551)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1490.6972 (IC base=+0.011)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.156 (n=843)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=2788)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.177 (n=889)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=2734)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.204 (n=1086)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=3579)

- **PATRÓN** `ibs_20min` > `0.9643` → IC=+0.131 (n=1547)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 0.9643 (IC base=+0.038)

- **PATRÓN** `libro_liquidez` > `1805.3784` → IC=+0.127 (n=1545)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 1805.3784 (IC base=+0.038)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.157 (n=1102)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=3436)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2388)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.162 (n=758)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2326)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2813)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=3553)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=440)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.264 (n=138)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=427)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.234 (n=287)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=887)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `libro_liquidez` < `3613.7014` → IC=-0.152 (n=110)

  - _Acción_: SKIP cuando `libro_liquidez` < 3613.7014
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=224)

- **FILTRO** `ballena_activa_n` > `85.0` → IC=-0.194 (n=145)

  - _Acción_: SKIP cuando `ballena_activa_n` > 85.0
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=288)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=931)

- **FILTRO** `libro_liquidez` < `1779.9583` → IC=-0.165 (n=237)

  - _Acción_: SKIP cuando `libro_liquidez` < 1779.9583
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=713)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.130 (n=17164)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=38209)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.285 (n=13648)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=41725)

- **FILTRO** `ibs_7min` < `0.2366` → IC=-0.229 (n=13843)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2366
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=41530)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.153 (n=18419)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=36954)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.242 (n=17106)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=52524)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.183 (n=17224)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=52406)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.148 (n=2768)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=6911)

- **FILTRO** `py_entrada` < `0.46` → IC=-0.236 (n=4780)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=4899)

- **FILTRO** `ibs_7min` < `0.7132` → IC=-0.244 (n=3194)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7132
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=6485)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.180 (n=2040)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=7639)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.272 (n=2997)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=9076)

- **FILTRO** `ibs_7min` > `0.7714` → IC=-0.212 (n=3017)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7714
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=9056)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.128 (n=2250)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=7082)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.266 (n=2190)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=7142)

- **FILTRO** `ibs_7min` < `0.726` → IC=-0.201 (n=2333)

  - _Acción_: SKIP cuando `ibs_7min` < 0.726
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=6999)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.192 (n=2313)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=7019)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.264 (n=2340)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=7155)

- **FILTRO** `ibs_7min` > `0.2677` → IC=-0.196 (n=2372)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2677
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=7123)

- **FILTRO** `ballena_activa_n` > `151.0` → IC=-0.182 (n=2373)

  - _Acción_: SKIP cuando `ballena_activa_n` > 151.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=7122)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.158 (n=2273)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=6928)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.312 (n=2266)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=6935)

- **FILTRO** `ibs_7min` < `0.2953` → IC=-0.246 (n=3036)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2953
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=6165)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.194 (n=2182)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=7019)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.255 (n=3002)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=9837)

- **FILTRO** `ibs_7min` > `0.7342` → IC=-0.178 (n=3208)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7342
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=9631)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.124 (n=2951)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=6072)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.263 (n=2118)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=6905)

- **FILTRO** `ibs_7min` < `0.728` → IC=-0.186 (n=2255)

  - _Acción_: SKIP cuando `ibs_7min` < 0.728
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=6768)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.189 (n=2233)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6790)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.270 (n=2111)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=7236)

- **FILTRO** `ibs_7min` > `0.2751` → IC=-0.179 (n=2334)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2751
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=7013)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.177 (n=2295)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=7052)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=2179)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=6899)

- **FILTRO** `ibs_7min` < `0.7143` → IC=-0.223 (n=2914)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=6164)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.219 (n=2184)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=6894)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.191 (n=3232)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=10066)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.292 (n=2144)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=6916)

- **FILTRO** `ibs_7min` < `0.2` → IC=-0.222 (n=2253)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=6807)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.199 (n=2263)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=6797)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.218 (n=3079)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=9499)

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
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=331)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.143 (n=166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=326)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=443)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=70)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=638)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=387)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.139 (n=1167)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.129 (n=551)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 14.0 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.133 (n=437)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 4.0 (IC base=+0.129)

- **PATRÓN** `total_vol_5m` < `436.8284` → IC=+0.155 (n=389)

  - _Acción_: Kelly boost +0.77€ cuando `total_vol_5m` < 436.8284 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `3635.4092` → IC=+0.148 (n=529)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3635.4092 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.149 (n=380)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 11.0 (IC base=+0.129)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4376` → IC=+0.145 (n=91)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio` |x|> 0.4376 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.202 (n=132)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.137)

- **PATRÓN** `total_vol_5m` < `292.267` → IC=+0.147 (n=182)

  - _Acción_: Kelly boost +0.73€ cuando `total_vol_5m` < 292.267 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2571.3862` → IC=+0.199 (n=91)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2571.3862 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.160 (n=101)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 7.0 (IC base=+0.137)

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
- **FILTRO** `sigma_h` > `0.006` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

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
- **PATRÓN** `streak_estiramiento` < `0.2566` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `streak_estiramiento` < 0.2566 (IC base=+0.012)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1003)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1330)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=1148)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=1201)

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
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=4034)

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
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=2229)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.198 (n=1216)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0047 (IC base=+0.177)

- **PATRÓN** `sigma_h` > `0.012` → IC=+0.197 (n=1216)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.012 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.1764` → IC=+0.192 (n=3209)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1764 (IC base=+0.177)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1909` → IC=+0.178 (n=1655)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.89€ cuando `delta_ratio_macro` |x|> 0.1909 (IC base=+0.177)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1329` → IC=+0.188 (n=1456)

  - _Acción_: Kelly boost +0.94€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1329 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=3367)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.180 (n=3351)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.177)

- **PATRÓN** `ibs_15` > `0.55` → IC=+0.253 (n=3648)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.55 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.1295` → IC=+0.171 (n=1748)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1295 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` < `0.3153` → IC=+0.164 (n=2885)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.3153 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.492` → IC=+0.258 (n=944)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.492 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `4667.8038` → IC=+0.195 (n=1216)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 4667.8038 (IC base=+0.177)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=1447)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.248 (n=272)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.0585` → IC=+0.270 (n=207)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0585 (IC base=+0.220)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2526` → IC=+0.245 (n=206)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2526 (IC base=+0.220)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2297` → IC=+0.232 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2297 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.240 (n=618)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.220)

- **PATRÓN** `ibs_15` > `0.7199` → IC=+0.285 (n=618)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7199 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `0.1378` → IC=+0.238 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1378 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.772` → IC=+0.307 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.772 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.221 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `8754.682` → IC=+0.234 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8754.682 (IC base=+0.220)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.187 (n=241)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0035 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.0667` → IC=+0.153 (n=318)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.0667 (IC base=+0.145)

- **PATRÓN** `drift_15min` |x|≤ `0.3957` → IC=+0.150 (n=241)

  - _Acción_: Kelly boost +0.75€ cuando `drift_15min` |x|≤ 0.3957 (IC base=+0.145)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1432` → IC=+0.151 (n=482)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.75€ cuando `delta_ratio_macro` |x|> 0.1432 (IC base=+0.145)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1283` → IC=+0.159 (n=285)

  - _Acción_: Kelly boost +0.79€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1283 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.154 (n=660)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 6.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.150 (n=750)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 17.0 (IC base=+0.145)

- **PATRÓN** `ibs_15` > `0.5408` → IC=+0.240 (n=721)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5408 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1197` → IC=+0.159 (n=447)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1197 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.707` → IC=+0.266 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.707 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `3217.3698` → IC=+0.151 (n=721)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3217.3698 (IC base=+0.145)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `17.763` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.763
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=341)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1779` → IC=+0.133 (n=556)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.66€ cuando `drift_60min` |x|≤ 0.1779 (IC base=+0.094)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.247 (n=279)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.265` → IC=+0.165 (n=159)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 17.265 (IC base=+0.094)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=462)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.094)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.407` → IC=+0.123 (n=75)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 8.407 (IC base=+0.002)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0239` → IC=+0.236 (n=278)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0239 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.0864` → IC=+0.234 (n=367)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0864 (IC base=+0.202)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.093` → IC=+0.249 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.093 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.202 (n=756)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.214 (n=743)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.202)

- **PATRÓN** `ibs_15` > `0.5333` → IC=+0.280 (n=833)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5333 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.1291` → IC=+0.209 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1291 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.081` → IC=+0.231 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.081 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2960.2418` → IC=+0.296 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2960.2418 (IC base=+0.202)

- **PATRÓN** `ibs_15` < `0.1098` → IC=+0.158 (n=778)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.79€ cuando `ibs_15` < 0.1098 (IC base=+0.067)

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
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.176 (n=2180)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=2181)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.214 (n=1703)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=2658)

- **PATRÓN** `ibs_15` > `0.6326` → IC=+0.280 (n=1053)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6326 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` > `0.1122` → IC=+0.206 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1122 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` < `0.2672` → IC=+0.196 (n=898)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.2672 (IC base=-0.069)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2302` → IC=+0.269 (n=1208)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2302 (IC base=-0.013)

- **PATRÓN** `ibs_15` < `0.3605` → IC=+0.282 (n=3626)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3605 (IC base=-0.013)

- **PATRÓN** `dist_vwap_pct` > `0.6573` → IC=+0.274 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6573 (IC base=-0.013)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0341` → IC=-0.224 (n=1914)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0341
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=644)

- **FILTRO** `sigma_ewma_delta_pct` > `23.271` → IC=-0.271 (n=369)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.271
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=2189)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=66)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=2492)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.168 (n=254)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0028 (IC base=+0.095)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2081` → IC=+0.285 (n=156)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2081 (IC base=+0.095)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1079` → IC=+0.272 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1079 (IC base=+0.095)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.134 (n=375)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 15.0 (IC base=+0.095)

- **PATRÓN** `ibs_15` > `0.7572` → IC=+0.332 (n=343)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7572 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.1051` → IC=+0.286 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1051 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` < `0.2443` → IC=+0.276 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2443 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.58` → IC=+0.130 (n=382)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 8.58 (IC base=+0.095)

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
  - _Potencial_: sin este filtro IC_bueno=+0.157 (n=686)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.161 (n=464)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0058 (IC base=+0.150)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.158 (n=352)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0049 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.0704` → IC=+0.188 (n=232)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0704 (IC base=+0.150)

- **PATRÓN** `drift_15min` |x|≤ `0.3992` → IC=+0.152 (n=176)

  - _Acción_: Kelly boost +0.76€ cuando `drift_15min` |x|≤ 0.3992 (IC base=+0.150)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3006` → IC=+0.192 (n=404)

  - _Acción_: Kelly boost +0.96€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3006 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=530)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.149 (n=540)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 17.0 (IC base=+0.150)

- **PATRÓN** `ibs_15` > `0.6046` → IC=+0.247 (n=528)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6046 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.4673` → IC=+0.164 (n=138)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.4673 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.1598` → IC=+0.150 (n=415)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1598 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.395` → IC=+0.238 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.395 (IC base=+0.150)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=686)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `9675.8313` → IC=+0.157 (n=176)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 9675.8313 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.250 (n=1312)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.245)

- **PATRÓN** `drift_15min` |x|≤ `0.7694` → IC=+0.257 (n=1154)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7694 (IC base=+0.245)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1573` → IC=+0.259 (n=874)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1573 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.247 (n=481)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.246 (n=1169)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.245)

- **PATRÓN** `ibs_15` < `0.3703` → IC=+0.275 (n=1312)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3703 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` > `0.6027` → IC=+0.262 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6027 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.449` → IC=+0.254 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.449 (IC base=+0.245)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0105` → IC=-0.248 (n=252)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=760)

- **FILTRO** `drift_60min` |x|> `0.1729` → IC=-0.257 (n=344)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1729
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=668)

- **FILTRO** `drift_15min` |x|> `0.8922` → IC=-0.283 (n=252)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8922
  - _Potencial_: sin este filtro IC_bueno=-0.163 (n=760)

- **FILTRO** `sigma_ewma_delta_pct` > `6.602` → IC=-0.199 (n=234)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.602
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=778)

- **FILTRO** `sigma_ewma_delta_pct` > `17.981` → IC=-0.149 (n=528)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.981
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4199)

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
- **FILTRO** `sigma_h` > `0.0198` → IC=-0.254 (n=599)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0198
  - _Potencial_: sin este filtro IC_bueno=-0.163 (n=601)

- **FILTRO** `drift_15min` |x|> `1.2406` → IC=-0.267 (n=298)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2406
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=902)

- **FILTRO** `sigma_ewma_delta_pct` > `7.426` → IC=-0.213 (n=374)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.426
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=826)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.209)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.209)

- **PATRÓN** `delta_ratio_macro` |x|> `0.069` → IC=+0.274 (n=776)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.069 (IC base=-0.026)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1155` → IC=+0.294 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1155 (IC base=-0.026)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.293 (n=871)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` > `0.7702` → IC=+0.354 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7702 (IC base=-0.026)

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
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.298 (n=952)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.0531` → IC=+0.321 (n=362)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0531 (IC base=+0.293)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2427` → IC=+0.310 (n=361)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2427 (IC base=+0.293)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2243` → IC=+0.306 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2243 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.309 (n=1126)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.293)

- **PATRÓN** `ibs_15` > `0.8388` → IC=+0.321 (n=1082)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8388 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.2713` → IC=+0.328 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2713 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.513` → IC=+0.381 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.513 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `12311.9188` → IC=+0.313 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12311.9188 (IC base=+0.293)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.311 (n=257)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.290)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.304 (n=264)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.0574` → IC=+0.316 (n=194)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0574 (IC base=+0.290)

- **PATRÓN** `delta_ratio_macro` |x|> `0.258` → IC=+0.316 (n=194)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.258 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.308 (n=581)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.290)

- **PATRÓN** `ibs_15` > `0.8292` → IC=+0.317 (n=581)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8292 (IC base=+0.290)

- **PATRÓN** `dist_vwap_pct` > `0.2552` → IC=+0.329 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2552 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.497` → IC=+0.386 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.497 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `16196.8854` → IC=+0.332 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16196.8854 (IC base=+0.290)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.306 (n=502)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.0515` → IC=+0.318 (n=168)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0515 (IC base=+0.295)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1464` → IC=+0.301 (n=334)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1464 (IC base=+0.295)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2199` → IC=+0.318 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2199 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.317 (n=483)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.295)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.298 (n=454)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.295)

- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.323 (n=501)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` > `0.285` → IC=+0.327 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.285 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.52` → IC=+0.365 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.52 (IC base=+0.295)

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

- **FILTRO** `drift_15min` |x|> `0.4407` → IC=-0.152 (n=162)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.4407
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=316)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.55 sube el IC de +0.177 a +0.253 en UPDOWN_GBM#15min (n=3648). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7199 sube el IC de +0.220 a +0.285 en UPDOWN_GBM#BTC#15min (n=618). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5408 sube el IC de +0.145 a +0.240 en UPDOWN_GBM#ETH#15min (n=721). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de +0.094 a +0.247 en UPDOWN_GBM#SOL#15min (n=279). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5333 sube el IC de +0.202 a +0.280 en UPDOWN_GBM#XRP#15min (n=833). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1098 sube el IC de +0.067 a +0.158 en UPDOWN_GBM#XRP#15min (n=778). Ya aplicado como kelly_boost=+0.79€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6326 sube el IC de -0.069 a +0.280 en UPDOWN_GBM_15M_TARDIO (n=1053). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3605 sube el IC de -0.013 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=3626). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7572 sube el IC de +0.095 a +0.332 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=343). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.618 sube el IC de -0.195 a +0.290 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=60). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6046 sube el IC de +0.150 a +0.247 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=528). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3703 sube el IC de +0.245 a +0.275 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1312). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.193 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3529 sube el IC de -0.040 a +0.292 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=585). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.209 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.026 a +0.293 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=871). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.062 a +0.333 en UPDOWN_GBM_ETH_15M_HORA7 (n=16). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.062 a +0.333 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=16). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8388 sube el IC de +0.293 a +0.321 en UPDOWN_GBM_IBS_ALTO (n=1082). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8292 sube el IC de +0.290 a +0.317 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=581). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.295 a +0.323 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=501). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7872 sube el IC de +0.365 a +0.401 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=634). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8057 sube el IC de +0.364 a +0.391 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=329). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7479 sube el IC de +0.365 a +0.412 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=306). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

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
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 670 | -0.003 | +71.97€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 670 | -0.003 | +71.97€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 5 | +0.018 | +2.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 5 | +0.018 | +2.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 487 | -0.032 | +38.02€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 487 | -0.032 | +38.02€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 142 | +0.083 | +26.43€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 142 | +0.083 | +26.43€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 40422 | -0.081 | -5025.84€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2237 | +0.034 | -261.98€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 38185 | -0.087 | -4763.86€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4509 | -0.114 | -777.62€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4509 | -0.114 | -777.62€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2237 | +0.034 | -261.98€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2237 | +0.034 | -261.98€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4323 | -0.105 | -876.84€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4323 | -0.105 | -876.84€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 10777 | -0.021 | -998.55€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 10777 | -0.021 | -998.55€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 10680 | -0.103 | -793.77€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 10680 | -0.103 | -793.77€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 7896 | -0.132 | -1317.08€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 7896 | -0.132 | -1317.08€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 35522 | -0.015 | +3313.49€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 9194 | +0.004 | +1662.57€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 26328 | -0.022 | +1650.91€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 35522 | -0.015 | +3313.49€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 9194 | +0.004 | +1662.57€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 26328 | -0.022 | +1650.91€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 146687 | +0.116 | -5777.00€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 18745 | +0.182 | -577.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 645 | -0.015 | -67.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 118526 | +0.107 | -4833.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 8771 | +0.100 | -299.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 19652 | +0.108 | -1188.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 61 | -0.151 | +10.95€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 19576 | +0.110 | -1188.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 28381 | +0.128 | -396.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5212 | +0.188 | -180.63€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 19641 | +0.121 | -89.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3486 | +0.083 | -104.36€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 19708 | +0.100 | -1353.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 75 | -0.123 | -6.95€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 19618 | +0.101 | -1334.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 31200 | +0.125 | -553.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 8066 | +0.178 | -150.65€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 19906 | +0.108 | -342.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3216 | +0.100 | -52.15€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 28072 | +0.115 | -1366.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5262 | +0.196 | -254.43€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 548 | +0.018 | -13.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 20193 | +0.095 | -955.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2069 | +0.130 | -142.90€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#XRP | 19674 | +0.106 | -918.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 69 | -0.091 | +4.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 19592 | +0.107 | -922.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 23601 | +0.197 | -1402.15€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 23601 | +0.197 | -1402.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 5368 | +0.180 | -445.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 5368 | +0.180 | -445.74€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 3014 | +0.203 | -67.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 3014 | +0.203 | -67.33€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 5308 | +0.181 | -419.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 5308 | +0.181 | -419.54€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4602 | +0.248 | -151.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4602 | +0.248 | -151.06€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 5230 | +0.189 | -332.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 5230 | +0.189 | -332.23€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1028 | +0.426 | -36.11€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1028 | +0.426 | -36.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 404 | +0.433 | -8.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 404 | +0.433 | -8.08€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 407 | +0.431 | -8.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 407 | +0.431 | -8.91€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 203 | +0.402 | -15.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 203 | +0.402 | -15.25€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 82553 | +0.202 | -5833.33€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 82553 | +0.202 | -5833.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 14178 | +0.186 | -1441.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 14178 | +0.186 | -1441.18€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 13333 | +0.224 | -455.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 13333 | +0.224 | -455.87€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 14138 | +0.182 | -1464.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 14138 | +0.182 | -1464.15€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 13407 | +0.221 | -483.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 13407 | +0.221 | -483.81€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 13700 | +0.202 | -895.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 13700 | +0.202 | -895.23€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 13797 | +0.197 | -1093.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 13797 | +0.197 | -1093.08€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 31601 | +0.116 | +179.67€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 31601 | +0.116 | +179.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 15709 | +0.119 | +160.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 15709 | +0.119 | +160.13€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 15892 | +0.114 | +19.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 15892 | +0.114 | +19.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2092 | +0.293 | -6.90€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2092 | +0.293 | -6.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 959 | +0.279 | -26.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 959 | +0.279 | -26.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1014 | +0.297 | +14.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1014 | +0.297 | +14.18€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 119 | +0.351 | +5.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 119 | +0.351 | +5.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 963 | +0.441 | +2.99€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 963 | +0.441 | +2.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 468 | +0.434 | -6.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 468 | +0.434 | -6.21€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 449 | +0.449 | +8.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 449 | +0.449 | +8.65€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1663 | +0.071 | -65.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 643 | +0.052 | -51.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1020 | +0.083 | -13.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 74 | +0.118 | +4.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 74 | +0.118 | +4.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1277 | +0.079 | -27.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 257 | +0.060 | -14.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1020 | +0.083 | -13.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 312 | +0.029 | -42.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 312 | +0.029 | -42.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 62472 | +0.101 | -1591.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 5051 | +0.090 | +47.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 57421 | +0.101 | -1638.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 34361 | +0.105 | -390.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 5051 | +0.090 | +47.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 29310 | +0.108 | -438.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 12857 | +0.109 | -82.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 12857 | +0.109 | -82.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 15254 | +0.082 | -1117.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 15254 | +0.082 | -1117.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 897 | +0.193 | -109.11€ | 4 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 897 | +0.193 | -109.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 897 | +0.193 | -109.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 897 | +0.193 | -109.11€ | 4 | 4 |
| ✅ GBM_LATE_15M | 42928 | +0.095 | +22487.01€ | 0 | 18 |
| ✅ GBM_LATE_15M#15min | 42928 | +0.095 | +22487.01€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 7149 | +0.217 | +5919.80€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 7149 | +0.217 | +5919.80€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 6440 | +0.179 | +4926.58€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 6440 | +0.179 | +4926.58€ | 0 | 22 |
| ✅ GBM_LATE_15M#DOGE | 7674 | +0.206 | +5987.33€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 7674 | +0.206 | +5987.33€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 5980 | +0.043 | +1686.97€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 5980 | +0.043 | +1686.97€ | 1 | 20 |
| ✅ GBM_LATE_15M#SOL | 6047 | -0.032 | +1274.21€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 6047 | -0.032 | +1274.21€ | 4 | 15 |
| ✅ GBM_LATE_15M#XRP | 9638 | -0.030 | +2692.13€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 9638 | -0.030 | +2692.13€ | 4 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 46149 | +0.085 | +25149.29€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 46149 | +0.085 | +25149.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 8920 | +0.003 | +4502.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 8920 | +0.003 | +4502.75€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 9782 | +0.009 | +2326.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 9782 | +0.009 | +2326.62€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 6395 | +0.279 | +6888.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 6395 | +0.279 | +6888.63€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 8340 | +0.013 | +2077.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 8340 | +0.013 | +2077.60€ | 1 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 7343 | +0.039 | +3026.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 7343 | +0.039 | +3026.29€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5369 | +0.304 | +6327.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5369 | +0.304 | +6327.40€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 34018 | +0.180 | +27626.70€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 34018 | +0.180 | +27626.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 5158 | +0.231 | +4608.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 5158 | +0.231 | +4608.72€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 5360 | +0.148 | +3957.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 5360 | +0.148 | +3957.60€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 5451 | +0.224 | +4709.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 5451 | +0.224 | +4709.29€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 5767 | +0.138 | +4404.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 5767 | +0.138 | +4404.13€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 6394 | +0.125 | +4777.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 6394 | +0.125 | +4777.28€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 5888 | +0.226 | +5169.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 5888 | +0.226 | +5169.67€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 9253 | +0.134 | +4520.13€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 9253 | +0.134 | +4520.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2717 | +0.144 | +1544.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2717 | +0.144 | +1544.83€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 467 | +0.150 | +239.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 467 | +0.150 | +239.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2738 | +0.138 | +1307.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2738 | +0.138 | +1307.65€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2299 | +0.109 | +894.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2299 | +0.109 | +894.11€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 627 | +0.133 | +281.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 627 | +0.133 | +281.63€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 43097 | +0.185 | +34553.68€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#15min | 43097 | +0.185 | +34553.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 6824 | +0.243 | +6390.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 6824 | +0.243 | +6390.76€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 6715 | +0.147 | +4598.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 6715 | +0.147 | +4598.11€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 7291 | +0.233 | +6526.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 7291 | +0.233 | +6526.12€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 7114 | +0.139 | +5079.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 7114 | +0.139 | +5079.72€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 7628 | +0.121 | +5269.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 7628 | +0.121 | +5269.70€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 7525 | +0.231 | +6689.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 7525 | +0.231 | +6689.27€ | 0 | 19 |
| ✅ GBM_LATE_5M | 11826 | +0.203 | +9248.62€ | 1 | 30 |
| ✅ GBM_LATE_5M#5min | 11826 | +0.203 | +9248.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 984 | +0.242 | +916.10€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 984 | +0.242 | +916.10€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2779 | +0.208 | +2389.36€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2779 | +0.208 | +2389.36€ | 0 | 26 |
| ✅ GBM_LATE_5M#DOGE | 1113 | +0.193 | +810.34€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1113 | +0.193 | +810.34€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 3342 | +0.193 | +2355.71€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3342 | +0.193 | +2355.71€ | 0 | 28 |
| ✅ GBM_LATE_5M#SOL | 1742 | +0.194 | +1339.09€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1742 | +0.194 | +1339.09€ | 0 | 29 |
| ✅ GBM_LATE_5M#XRP | 1866 | +0.206 | +1438.02€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1866 | +0.206 | +1438.02€ | 0 | 0 |
| ✅ GBM_LATE_60M | 3534 | +0.066 | +1147.77€ | 0 | 8 |
| ✅ GBM_LATE_60M#60min | 3534 | +0.066 | +1147.77€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1299 | +0.082 | +473.50€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1299 | +0.082 | +473.50€ | 0 | 6 |
| ✅ GBM_LATE_60M#ETH | 1142 | +0.066 | +384.49€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1142 | +0.066 | +384.49€ | 0 | 9 |
| ✅ GBM_LATE_60M#SOL | 1093 | +0.046 | +289.78€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1093 | +0.046 | +289.78€ | 1 | 13 |
| 🚫 GBM_LATE_60M_FADE | 578 | -0.243 | -22.04€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 578 | -0.243 | -22.04€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 214 | -0.250 | -16.08€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 214 | -0.250 | -16.08€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 206 | -0.226 | -0.46€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 206 | -0.226 | -0.46€ | 7 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 158 | -0.250 | -5.50€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 158 | -0.250 | -5.50€ | 6 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1535 | +0.085 | +397.91€ | 0 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1535 | +0.085 | +397.91€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 606 | +0.082 | +150.57€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 606 | +0.082 | +150.57€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 547 | +0.057 | +84.73€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 547 | +0.057 | +84.73€ | 2 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 382 | +0.128 | +162.61€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 382 | +0.128 | +162.61€ | 3 | 9 |
| ✅ LATE_WINDOW_5MIN | 167 | +0.281 | +166.63€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 167 | +0.281 | +166.63€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 167 | +0.281 | +166.63€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 167 | +0.281 | +166.63€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3427 | +0.102 | +850.89€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3427 | +0.102 | +850.89€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3427 | +0.102 | +850.89€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3427 | +0.102 | +850.89€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 544 | -0.044 | -19.76€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 544 | -0.044 | -19.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 153 | -0.016 | +2.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 153 | -0.016 | +2.14€ | 2 | 1 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 105 | -0.033 | -3.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 105 | -0.033 | -3.14€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 205 | -0.012 | -1.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 205 | -0.012 | -1.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 3753 | +0.016 | +83.70€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3753 | +0.016 | +83.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 182 | +0.022 | -2.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 182 | +0.022 | -2.31€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 794 | +0.007 | +29.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 794 | +0.007 | +29.41€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE | 207 | -0.012 | -4.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 207 | -0.012 | -4.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1362 | +0.026 | +32.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1362 | +0.026 | +32.00€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 758 | +0.012 | +2.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 758 | +0.012 | +2.16€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 450 | +0.015 | +26.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 450 | +0.015 | +26.62€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1772 | -0.040 | -27.51€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1772 | -0.040 | -27.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 512 | -0.029 | -11.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 512 | -0.029 | -11.13€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 606 | -0.015 | +6.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 606 | -0.015 | +6.31€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 654 | -0.070 | -22.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 654 | -0.070 | -22.69€ | 6 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 8927 | -0.026 | +26.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 4238 | -0.036 | -73.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 4689 | -0.018 | +100.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 268 | -0.041 | -11.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 136 | -0.022 | -0.57€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 132 | -0.060 | -10.61€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 2219 | -0.019 | +21.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1057 | -0.024 | -1.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1162 | -0.014 | +22.52€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 976 | -0.024 | +14.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 488 | -0.041 | -11.08€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 488 | -0.006 | +26.07€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 1958 | -0.040 | -53.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 912 | -0.052 | -55.51€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1046 | -0.029 | +2.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1757 | -0.016 | +47.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 839 | -0.028 | +2.25€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 918 | -0.004 | +45.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1749 | -0.031 | +7.48€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 806 | -0.038 | -7.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 943 | -0.024 | +15.16€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 50443 | -0.000 | +2525.44€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 50443 | -0.000 | +2525.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 9094 | +0.026 | +1162.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 9094 | +0.026 | +1162.86€ | 2 | 5 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 7254 | -0.034 | -97.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 7254 | -0.034 | -97.20€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 9207 | +0.025 | +954.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 9207 | +0.025 | +954.79€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 7099 | -0.047 | -137.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 7099 | -0.047 | -137.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 8532 | -0.004 | +233.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 8532 | -0.004 | +233.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 9257 | +0.015 | +408.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 9257 | +0.015 | +408.96€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6659 | -0.059 | -162.85€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6659 | -0.059 | -162.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1739 | -0.078 | -45.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1739 | -0.078 | -45.51€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 55 | -0.061 | -2.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 55 | -0.061 | -2.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 775 | -0.120 | -33.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 775 | -0.120 | -33.97€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2008 | -0.074 | -39.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2008 | -0.074 | -39.68€ | 4 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 125003 | -0.077 | +1563.13€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 125003 | -0.077 | +1563.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 21752 | -0.077 | +1058.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 21752 | -0.077 | +1058.53€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 18827 | -0.101 | -1035.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 18827 | -0.101 | -1035.51€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 22040 | -0.068 | +1196.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 22040 | -0.068 | +1196.55€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 18370 | -0.097 | -634.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 18370 | -0.097 | -634.45€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 22376 | -0.057 | +303.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 22376 | -0.057 | +303.74€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 21638 | -0.067 | +674.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 21638 | -0.067 | +674.26€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8770 | -0.034 | -182.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8770 | -0.034 | -182.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1001 | -0.017 | -18.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1001 | -0.017 | -18.91€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1988 | -0.046 | -25.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1988 | -0.046 | -25.22€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2601 | -0.027 | -42.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2601 | -0.027 | -42.85€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1201 | -0.054 | -27.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1201 | -0.054 | -27.02€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 971 | -0.031 | -35.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 971 | -0.031 | -35.95€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1689 | +0.123 | +687.43€ | 0 | 6 |
| ✅ ORDER_FLOW_5M#5min | 1553 | +0.129 | +674.83€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 362 | +0.137 | +181.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 362 | +0.137 | +181.66€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 319 | +0.117 | +109.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 319 | +0.117 | +109.30€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#ETH | 309 | +0.137 | +150.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 309 | +0.137 | +150.62€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 275 | +0.150 | +149.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 275 | +0.150 | +149.73€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 288 | +0.100 | +83.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 288 | +0.100 | +83.53€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1480 | -0.015 | -20.60€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1480 | -0.015 | -20.60€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 291 | -0.002 | +9.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 291 | -0.002 | +9.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 256 | -0.019 | -2.60€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 256 | -0.019 | -2.60€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 383 | -0.045 | -31.32€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 383 | -0.045 | -31.32€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 313 | +0.008 | +3.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 313 | +0.008 | +3.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 237 | -0.011 | +0.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 237 | -0.011 | +0.66€ | 0 | 0 |
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
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 48 | -0.120 | +7.01€ | 3 | 0 |
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
| ✅ STREAK_FADE_15M | 727 | +0.031 | +39.42€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 727 | +0.031 | +39.42€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 303 | +0.025 | +3.85€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 303 | +0.025 | +3.85€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 60 | -0.016 | -2.15€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 60 | -0.016 | -2.15€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 73 | -0.007 | +0.78€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 73 | -0.007 | +0.78€ | 3 | 1 |
| ✅ STREAK_FADE_15M#XRP | 291 | +0.056 | +36.95€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 291 | +0.056 | +36.95€ | 0 | 5 |
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
| ✅ STREAK_MOM_5M | 10932 | +0.016 | +85.88€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 10932 | +0.016 | +85.88€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2799 | +0.020 | +28.18€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2799 | +0.020 | +28.18€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2854 | +0.018 | +35.52€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2854 | +0.018 | +35.52€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2888 | +0.009 | -0.95€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2888 | +0.009 | -0.95€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2391 | +0.016 | +23.13€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2391 | +0.016 | +23.13€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 9932 | +0.013 | -48.13€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 9932 | +0.013 | -48.13€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4053 | +0.018 | -8.03€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4053 | +0.018 | -8.03€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3616 | +0.011 | -27.14€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3616 | +0.011 | -27.14€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2263 | +0.009 | -12.96€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2263 | +0.009 | -12.96€ | 1 | 0 |
| ✅ UPDOWN_GBM | 77647 | +0.054 | +6876.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 19287 | +0.083 | +4228.10€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 2484 | +0.004 | +22.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 51011 | +0.050 | +2535.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 4594 | +0.007 | +90.67€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6851 | +0.089 | +1075.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1576 | +0.156 | +698.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5198 | +0.070 | +378.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 16792 | +0.055 | +1446.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2508 | +0.090 | +618.07€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 670 | +0.009 | +10.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 11474 | +0.061 | +752.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2042 | +0.004 | +62.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 98 | -0.070 | +3.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8515 | +0.070 | +908.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1555 | +0.147 | +610.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6882 | +0.053 | +299.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 17875 | +0.044 | +1156.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 4572 | +0.065 | +669.46€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 652 | +0.006 | +15.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 10950 | +0.044 | +451.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1610 | +0.011 | +17.46€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 91 | -0.102 | +2.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 17062 | +0.032 | +838.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 4856 | +0.034 | +397.28€ | 0 | 4 |
| ✅ UPDOWN_GBM#SOL#240min | 619 | -0.009 | -0.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 10565 | +0.037 | +435.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 942 | +0.007 | +11.03€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 80 | -0.134 | -5.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 10550 | +0.065 | +1452.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4220 | +0.102 | +1234.25€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 5942 | +0.042 | +218.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 269 | -0.102 | +1.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 845 | +0.365 | +312.55€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 845 | +0.365 | +312.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 438 | +0.364 | +152.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 438 | +0.364 | +152.73€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 407 | +0.365 | +159.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 407 | +0.365 | +159.82€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 20039 | -0.025 | +4652.79€ | 2 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 20039 | -0.025 | +4652.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3572 | -0.113 | +128.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3572 | -0.113 | +128.65€ | 3 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2451 | +0.217 | +1598.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2451 | +0.217 | +1598.96€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5739 | -0.067 | +668.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5739 | -0.067 | +668.80€ | 5 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5611 | -0.065 | +983.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5611 | -0.065 | +983.11€ | 3 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 232 | +0.047 | +11.12€ | 0 | 2 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 232 | +0.047 | +11.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 232 | +0.047 | +11.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 232 | +0.047 | +11.12€ | 0 | 2 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1442 | +0.293 | +1243.74€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1442 | +0.293 | +1243.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 774 | +0.290 | +631.43€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 774 | +0.290 | +631.43€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 668 | +0.295 | +612.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 668 | +0.295 | +612.30€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 815 | -0.112 | -83.16€ | 5 | 0 |
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
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.042) — sin ventaja clara. oversold(IBS<0.3): IC=+0.064 n=26941 | neutral: IC=+0.057 n=28647 | overbought(IBS>0.7): IC=+0.099 n=27381
  - _Datos_: n=86254 IC=+0.074 PNL=+12837.87€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 722 celda(s) pasan gate riguroso completo de 2700 evaluadas (n>=40) y 3750 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.034 < 0.08 — monitorear
  - _Datos_: n=4848 IC=+0.034 PNL=+400.17€

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
  - _Estado_: 77509 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.139 n=788/60 | contraria IC=+0.194 n=817 | gap=-0.054 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

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
  - _Estado_: ETH#60min: n=1609/40 IC=+0.010 PNL=+16.98€ | BTC#60min: n=2038/40 IC=+0.004 PNL=+61.19€ | SOL#60min: n=941/40 IC=+0.007 PNL=+10.36€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.048 n=561830 | tras_1loss IC=+0.096 n=426719 | tras_2loss IC=+0.065 n=172510/40 | gap=-0.017 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.036 n=10932 | contrario_BTC IC=+0.052 n=9600/40 | gap=+0.015 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.200 > 0.08 con n=749 PNL=+566.92€
  - _Datos_: n=749 IC=+0.200 PNL=+566.92€

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
  - _Estado_: n=73570 IC=+0.053 PNL=+6571.57€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=73570 IC=+0.053 PNL=+6571.57€

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
  - _Estado_: n=3089 IC=+0.009 PNL=+13.96€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3089 IC=+0.009 PNL=+13.96€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1499 IC=+0.002 PNL=+74.57€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1499 IC=+0.002 PNL=+74.57€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.177 > 0.1 con n=4856 PNL=+3041.55€
  - _Datos_: n=4856 IC=+0.177 PNL=+3041.55€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=2915 IC=+0.068 PNL=+219.59€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2915 IC=+0.068 PNL=+219.59€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=2508 IC=+0.090 PNL=+618.07€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=2508 IC=+0.090 PNL=+618.07€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.098 > 0.08 con n=11112 PNL=+3138.40€
  - _Datos_: n=11112 IC=+0.098 PNL=+3138.40€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=364 IC=-0.238 PNL=-9.09€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=364 IC=-0.238 PNL=-9.09€

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
  - _Estado_: n=989 IC=+0.039 PNL=+92.61€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=989 IC=+0.039 PNL=+92.61€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=121 IC=+0.012 PNL=+1.51€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=121 IC=+0.012 PNL=+1.51€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=8523 IC=+0.021 PNL=+229.26€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=8523 IC=+0.021 PNL=+229.26€

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
  - _Estado_: n=12806 IC=+0.051 PNL=+1066.43€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=12806 IC=+0.051 PNL=+1066.43€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=4620 IC=+0.064 PNL=+687.21€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4620 IC=+0.064 PNL=+687.21€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.111 > 0.08 con n=548 PNL=+177.19€
  - _Datos_: n=548 IC=+0.111 PNL=+177.19€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.149 > 0.08 con n=1169 PNL=+331.83€
  - _Datos_: n=1169 IC=+0.149 PNL=+331.83€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.099 > 0.08 con n=919 PNL=+451.53€
  - _Datos_: n=919 IC=+0.099 PNL=+451.53€

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
  - _Estado_: n=11596 IC=+0.057 PNL=+1132.18€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=11596 IC=+0.057 PNL=+1132.18€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.124 > 0.02 con n=975 PNL=+405.62€
  - _Datos_: n=975 IC=+0.124 PNL=+405.62€

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
  - _Estado_: n=30518 IC=+0.074 PNL=+4437.69€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=30518 IC=+0.074 PNL=+4437.69€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.207 > 0.1 con n=6828 PNL=+4080.64€
  - _Datos_: n=6828 IC=+0.207 PNL=+4080.64€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.141 < -0.1 con n=494 PNL=+59.59€
  - _Datos_: n=494 IC=-0.141 PNL=+59.59€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=3109 IC=+0.067 PNL=+386.11€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=3109 IC=+0.067 PNL=+386.11€

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
  - _Estado_: n=32495 IC=-0.133 PNL=+2741.45€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=32495 IC=-0.133 PNL=+2741.45€

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
  - _Estado_: n=3247 IC=+0.132 PNL=+1985.75€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=3247 IC=+0.132 PNL=+1985.75€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.205 > 0.08 con n=4159 PNL=+3043.09€
  - _Datos_: n=4159 IC=+0.205 PNL=+3043.09€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=7928 IC=+0.050 PNL=+613.21€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=7928 IC=+0.050 PNL=+613.21€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.095 > 0.08 con n=3480 PNL=+1904.81€
  - _Datos_: n=3480 IC=+0.095 PNL=+1904.81€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.220 > 0.08 con n=822 PNL=+493.75€
  - _Datos_: n=822 IC=+0.220 PNL=+493.75€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.223 < -0.1 con n=3372 PNL=-273.08€
  - _Datos_: n=3372 IC=-0.223 PNL=-273.08€

**🟡 H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.211 > 0.2 con n=8866 PNL=+7058.02€
  - _Datos_: n=8866 IC=+0.211 PNL=+7058.02€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.083 > 0.08 con n=3226 PNL=+1139.79€
  - _Datos_: n=3226 IC=+0.083 PNL=+1139.79€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.179 > 0.08 con n=2986 PNL=+2272.42€
  - _Datos_: n=2986 IC=+0.179 PNL=+2272.42€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=5032 IC=-0.025 PNL=+1406.69€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=5032 IC=-0.025 PNL=+1406.69€

**〰️ H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: n=687 IC=+0.075 PNL=-48.77€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=687 IC=+0.075 PNL=-48.77€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.244 > 0.08 con n=4840 PNL=-379.18€
  - _Datos_: n=4840 IC=+0.244 PNL=-379.18€

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.102 n=1742) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1742 IC=+0.102 PNL=+382.12€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.307 > 0.08 con n=459 PNL=+130.92€
  - _Datos_: n=459 IC=+0.307 PNL=+130.92€

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
  - _Estado_: n=14167 IC=+0.186 PNL=-1441.92€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=14167 IC=+0.186 PNL=-1441.92€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.221 > 0.1 con n=231 PNL=+154.04€
  - _Datos_: n=231 IC=+0.221 PNL=+154.04€
