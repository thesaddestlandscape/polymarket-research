# Hipótesis automáticas — 2026-11-01 09:13 UTC
_Generado por shadow_postmortem.py sobre 1144815 resoluciones (PNL=+153758.32€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.225 (n=877)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.134)

- **PATRÓN** `n_total_lado` > `63.0` → IC=+0.185 (n=312)

  - _Acción_: Kelly boost +0.92€ cuando `n_total_lado` > 63.0 (IC base=+0.134)

- **PATRÓN** `banda_hit_calibrado` > `0.6161` → IC=+0.252 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6161 (IC base=+0.134)

- **PATRÓN** `banda_z` > `8.831` → IC=+0.211 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.831 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.157 (n=339)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.149 (n=998)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `3323.3759` → IC=+0.138 (n=612)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 3323.3759 (IC base=+0.134)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.220 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.138)

- **PATRÓN** `n_total_lado` > `67.0` → IC=+0.192 (n=264)

  - _Acción_: Kelly boost +0.96€ cuando `n_total_lado` > 67.0 (IC base=+0.138)

- **PATRÓN** `banda_hit_calibrado` > `0.6114` → IC=+0.242 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6114 (IC base=+0.138)

- **PATRÓN** `banda_z` > `9.107` → IC=+0.206 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.107 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=287)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=898)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `3054.6814` → IC=+0.140 (n=703)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3054.6814 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `9072.3581` → IC=+0.123 (n=218)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 9072.3581 (IC base=+0.003)

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

- **PATRÓN** `py_entrada` < `0.49` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.49 (IC base=+0.167)

- **PATRÓN** `n_ballena_banda` > `30.0` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 30.0 (IC base=+0.167)

- **PATRÓN** `n_total_lado` > `43.0` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 43.0 (IC base=+0.167)

- **PATRÓN** `banda_hit_calibrado` > `0.6045` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `banda_hit_calibrado` > 0.6045 (IC base=+0.167)

- **PATRÓN** `banda_z` > `2.461` → IC=+0.229 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 2.461 (IC base=+0.167)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.729` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `ballenas_wallet_edge_medio` > 0.729 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.243 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.214 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `2452.7664` → IC=+0.221 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2452.7664 (IC base=+0.167)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `136.46` → IC=-0.214 (n=11065)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 136.46
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=33202)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `127.54` → IC=-0.258 (n=1161)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.54
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=3486)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `117.81` → IC=-0.303 (n=1150)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 117.81
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3450)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `157.2` → IC=-0.246 (n=2999)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 157.2
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=8998)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `131.97` → IC=-0.261 (n=2125)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.97
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=6378)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.212 (n=24971)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `8630.2248` → IC=+0.162 (n=2201)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 8630.2248 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.127 (n=21367)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=26075)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.225 (n=19720)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=7833)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6771.8206` → IC=+0.150 (n=3028)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 6771.8206 (IC base=+0.124)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=2158)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.364 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=2640)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `9416.0594` → IC=+0.182 (n=1837)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 9416.0594 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.186 (n=1879)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.183 (n=2099)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` < `0.295` → IC=+0.312 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.295 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.182 (n=2691)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `16119.9456` → IC=+0.185 (n=694)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 16119.9456 (IC base=+0.180)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.173 (n=537)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` > 0.61 (IC base=+0.077)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.141 (n=1272)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.44 (IC base=+0.080)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=4813)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.166 (n=4082)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 15.0 (IC base=+0.163)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.376 (n=1593)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.215 (n=2162)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.348 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=2510)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=1222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.150 (n=1037)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 15.0 (IC base=+0.143)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.259 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=975)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `3079.6088` → IC=+0.134 (n=230)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 3079.6088 (IC base=+0.069)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.255 (n=915)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1275)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.148 (n=1362)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=710)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.146)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.286 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=905)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.146)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `py_entrada` > `0.55` → IC=+0.157 (n=450)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` > 0.55 (IC base=+0.055)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.134 (n=1170)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 7.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.244 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.123)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.297 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.228 (n=145)

- **FILTRO** `py_entrada` > `0.75` → IC=-0.293 (n=162)

  - _Acción_: SKIP cuando `py_entrada` > 0.75
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=55)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=21355)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.200 (n=18108)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.230 (n=8857)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.198)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.182 (n=2310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.177 (n=4863)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 18.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.182 (n=4688)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.177 (n=4057)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.217 (n=2733)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.220 (n=2432)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.215)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.294 (n=922)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.215)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=4802)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.179 (n=4087)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.177 (n=4986)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=3743)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=4100)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.249 (n=3479)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.249)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.359 (n=1396)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.79 (IC base=+0.249)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.249)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=4710)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=4012)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.187 (n=3607)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.71 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=3503)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.187)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.429 (n=890)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.429 (n=895)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `4385.1965` → IC=+0.443 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4385.1965 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.443 (n=367)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

- **PATRÓN** `libro_liquidez` > `12430.0394` → IC=+0.446 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12430.0394 (IC base=+0.438)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.434 (n=349)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.427)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.432 (n=351)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.427)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.427)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.434 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.427)

- **PATRÓN** `libro_liquidez` > `4649.4982` → IC=+0.441 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4649.4982 (IC base=+0.427)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.398 (n=145)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.396)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.403 (n=142)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.396)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.412 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.396)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `14.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=32)

- **FILTRO** `py_entrada` > `0.77` → IC=-0.318 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.77
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=16)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=31)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=27918)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.245 (n=28134)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.201)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.190 (n=4153)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 18.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.184 (n=8904)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 12.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.195 (n=12644)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.229 (n=5808)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.225 (n=5726)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.287 (n=4006)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=4789)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.200 (n=9844)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=5859)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.223 (n=4477)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.271 (n=3956)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.211 (n=3973)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.259 (n=4129)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=4643)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.201 (n=4634)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.246 (n=4843)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=9953)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=10196)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.38` → IC=+0.139 (n=9246)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.38 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=4877)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.118)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.145 (n=4620)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=6127)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.118)

- **PATRÓN** `lag_apertura_s` < `2.66` → IC=+0.146 (n=4586)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.66 (IC base=+0.118)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.190 (n=5076)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=5576)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `3.24` → IC=+0.137 (n=6115)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.24 (IC base=+0.116)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.312 (n=1258)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.295)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.388 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.295)

- **PATRÓN** `libro_liquidez` > `3872.2908` → IC=+0.297 (n=800)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3872.2908 (IC base=+0.295)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.290 (n=846)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.283)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.364 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.283)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.323 (n=612)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.300)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.304 (n=892)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.300)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.397 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.300)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.300 (n=1017)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.300)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` < `16.0` → IC=+0.359 (n=90)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.335)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.381 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.335)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.365 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.335)

- **PATRÓN** `libro_liquidez` > `720.8183` → IC=+0.367 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 720.8183 (IC base=+0.335)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.448 (n=856)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.444)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.445 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.444)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.452 (n=826)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.444)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.445 (n=986)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.444)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.441 (n=405)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.440 (n=280)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.440 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.444 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.439)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.460 (n=273)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.451)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.456 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.451)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.455 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.451)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.452 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.451)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` > `13.0` → IC=+0.393 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.400)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.414 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.400)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.431 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.400)

- **PATRÓN** `libro_liquidez` > `702.9243` → IC=+0.386 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 702.9243 (IC base=+0.400)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.735` → IC=-0.386 (n=42)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=88)

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
- **FILTRO** `py_entrada` > `0.735` → IC=-0.386 (n=42)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=88)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4742` → IC=+0.139 (n=15652)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.4742 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.126 (n=15801)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.125 (n=10920)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.375` → IC=+0.164 (n=15660)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.375 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.7769` → IC=+0.280 (n=870)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7769 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.593` → IC=+0.182 (n=7824)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 3.593 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6225` → IC=+0.265 (n=4596)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6225 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.3033` → IC=+0.245 (n=1608)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3033 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.3492` → IC=+0.228 (n=5076)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3492 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=7942)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `4666.2222` → IC=+0.147 (n=5217)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 4666.2222 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.121 (n=9738)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0059 (IC base=+0.079)

- **PATRÓN** `ibs_20min` < `0.68` → IC=+0.131 (n=22129)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.68 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` > `0.6036` → IC=+0.187 (n=1298)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.6036 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` < `0.1589` → IC=+0.187 (n=7506)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.1589 (IC base=+0.079)

- **PATRÓN** `volumen_regimen` < `0.864` → IC=+0.190 (n=5211)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.864 (IC base=+0.079)

- **PATRÓN** `volumen_pendiente_norm` > `0.297` → IC=+0.230 (n=1934)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.297 (IC base=+0.079)

- **PATRÓN** `volumen_spike_ratio` > `2.6839` → IC=+0.208 (n=4427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6839 (IC base=+0.079)

- **PATRÓN** `ballena_activa_n` < `104.0` → IC=+0.225 (n=13171)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 104.0 (IC base=+0.079)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3613` → IC=+0.210 (n=3369)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3613 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.223 (n=1260)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.211 (n=2261)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.9843` → IC=+0.280 (n=1527)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9843 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.649` → IC=+0.280 (n=1498)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.649 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.2834` → IC=+0.259 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2834 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.4363` → IC=+0.208 (n=3225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4363 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=3696)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `2055.0744` → IC=+0.210 (n=1123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2055.0744 (IC base=+0.207)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.223 (n=2029)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.242 (n=2918)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0096 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.0889` → IC=+0.277 (n=973)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0889 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.244 (n=2691)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.240 (n=1354)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.5515` → IC=+0.260 (n=2916)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5515 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` < `0.0954` → IC=+0.243 (n=2633)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0954 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.2916` → IC=+0.258 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2916 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.4444` → IC=+0.242 (n=924)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4444 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.6846` → IC=+0.244 (n=923)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6846 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.242 (n=3349)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1481.96` → IC=+0.246 (n=2604)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1481.96 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.238 (n=1302)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.240)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.235 (n=930)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.0053` → IC=+0.227 (n=1268)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0053 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.1069` → IC=+0.258 (n=1229)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1069 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.238 (n=2915)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.228 (n=1986)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.9238` → IC=+0.270 (n=930)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9238 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `0.1856` → IC=+0.236 (n=1308)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1856 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.099` → IC=+0.257 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.099 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` < `1.2254` → IC=+0.228 (n=2791)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2254 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `0.6977` → IC=+0.231 (n=2493)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6977 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.270 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.4011` → IC=+0.231 (n=919)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4011 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `2.4278` → IC=+0.254 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4278 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.150 (n=2975)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0061 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.0775` → IC=+0.157 (n=992)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0775 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.151 (n=1102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.7157` → IC=+0.166 (n=2971)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.7157 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` < `0.1371` → IC=+0.144 (n=2830)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1371 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.778` → IC=+0.139 (n=486)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 10.778 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.024` → IC=+0.132 (n=2716)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 4.024 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `1.2035` → IC=+0.133 (n=2971)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.2035 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.0974` → IC=+0.149 (n=1082)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.0974 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `2.1407` → IC=+0.134 (n=2506)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.1407 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.127 (n=3854)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `205.0` → IC=+0.165 (n=1224)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 205.0 (IC base=+0.127)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.215 (n=1184)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=3722)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.265 (n=1374)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.107` → IC=+0.278 (n=767)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.107 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.097` → IC=+0.196 (n=3166)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.097 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.3532` → IC=+0.219 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3532 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.709` → IC=+0.207 (n=1567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.709 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=4261)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `2035.1584` → IC=+0.203 (n=1183)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2035.1584 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.222 (n=2844)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.1781` → IC=+0.235 (n=1422)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1781 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=1220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.222 (n=1478)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` < `0.037` → IC=+0.270 (n=1079)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.037 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.115` → IC=+0.262 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.115 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.3494` → IC=+0.263 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3494 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.1475` → IC=+0.225 (n=2061)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1475 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=1654)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `1917.241` → IC=+0.221 (n=1465)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1917.241 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.218 (n=2706)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.218)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.163 (n=179)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=4271)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.158 (n=609)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0038 (IC base=+0.055)

- **PATRÓN** `ibs_20min` > `0.946` → IC=+0.236 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.946 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` > `0.137` → IC=+0.335 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.137 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` < `0.3349` → IC=+0.328 (n=666)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3349 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.13` → IC=+0.197 (n=1319)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 5.13 (IC base=+0.055)

- **PATRÓN** `volumen_regimen` > `0.7003` → IC=+0.338 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7003 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` < `0.0775` → IC=+0.328 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0775 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.3033` → IC=+0.335 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3033 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` < `1.4167` → IC=+0.341 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4167 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` > `2.2606` → IC=+0.332 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2606 (IC base=+0.055)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.333 (n=697)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 143.0 (IC base=+0.055)

- **PATRÓN** `ibs_20min` < `0.0921` → IC=+0.181 (n=1114)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.0921 (IC base=+0.045)

- **PATRÓN** `dist_vwap_pct` > `0.3304` → IC=+0.164 (n=537)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.3304 (IC base=+0.045)

- **PATRÓN** `dist_vwap_pct` < `0.1359` → IC=+0.145 (n=1917)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1359 (IC base=+0.045)

- **PATRÓN** `volumen_regimen` < `0.8345` → IC=+0.159 (n=1376)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8345 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.2851` → IC=+0.210 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2851 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` < `1.7812` → IC=+0.149 (n=1323)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.7812 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` > `2.156` → IC=+0.164 (n=899)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.156 (IC base=+0.045)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.174 (n=127)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=667)

- **FILTRO** `ibs_20min` < `0.2667` → IC=-0.168 (n=197)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2667
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=597)

- **FILTRO** `ibs_20min` > `0.2069` → IC=-0.133 (n=4183)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2069
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=2065)

- **FILTRO** `sigma_ewma_delta_pct` > `8.459` → IC=-0.223 (n=676)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.459
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=5572)

- **PATRÓN** `ibs_20min` > `0.7606` → IC=+0.173 (n=270)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.7606 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.9638` → IC=+0.277 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9638 (IC base=+0.025)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.051` → IC=+0.156 (n=187)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 5.051 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `1.0267` → IC=+0.298 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0267 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` < `0.1558` → IC=+0.284 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1558 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.4484` → IC=+0.287 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4484 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` > `1.449` → IC=+0.262 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.449 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.271 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.025)

- **PATRÓN** `ibs_20min` < `0.2069` → IC=+0.150 (n=2065)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.2069 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` < `0.2912` → IC=+0.277 (n=935)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2912 (IC base=-0.039)

- **PATRÓN** `volumen_regimen` < `0.6963` → IC=+0.309 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6963 (IC base=-0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.0783` → IC=+0.293 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0783 (IC base=-0.039)

- **PATRÓN** `volumen_spike_ratio` < `2.4559` → IC=+0.303 (n=821)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4559 (IC base=-0.039)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7692` → IC=-0.152 (n=3102)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7692
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=1603)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.168 (n=1084)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=3621)

- **FILTRO** `ibs_20min` > `0.7464` → IC=-0.196 (n=1663)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7464
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=4991)

- **PATRÓN** `dist_vwap_pct` > `1.0492` → IC=+0.358 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0492 (IC base=-0.063)

- **PATRÓN** `dist_vwap_pct` < `0.2465` → IC=+0.307 (n=756)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2465 (IC base=-0.063)

- **PATRÓN** `volumen_regimen` > `0.7043` → IC=+0.319 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7043 (IC base=-0.063)

- **PATRÓN** `volumen_pendiente_norm` < `0.1025` → IC=+0.306 (n=809)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1025 (IC base=-0.063)

- **PATRÓN** `volumen_spike_ratio` < `1.4319` → IC=+0.318 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4319 (IC base=-0.063)

- **PATRÓN** `volumen_spike_ratio` > `1.8639` → IC=+0.310 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8639 (IC base=-0.063)

- **PATRÓN** `dist_vwap_pct` > `0.7999` → IC=+0.272 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7999 (IC base=-0.001)

- **PATRÓN** `dist_vwap_pct` < `0.2214` → IC=+0.262 (n=1865)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2214 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` < `0.7253` → IC=+0.271 (n=833)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7253 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` > `1.0651` → IC=+0.284 (n=859)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0651 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.1688` → IC=+0.281 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1688 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `2.1776` → IC=+0.265 (n=1557)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1776 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `1.4309` → IC=+0.267 (n=1769)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4309 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.204 (n=6787)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.091)

- **PATRÓN** `ibs_20min` > `0.875` → IC=+0.287 (n=9233)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.875 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `0.9303` → IC=+0.302 (n=1460)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9303 (IC base=+0.091)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.548` → IC=+0.167 (n=9122)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.548 (IC base=+0.091)

- **PATRÓN** `volumen_regimen` < `1.1736` → IC=+0.269 (n=7459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1736 (IC base=+0.091)

- **PATRÓN** `volumen_regimen` > `0.6921` → IC=+0.275 (n=6665)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6921 (IC base=+0.091)

- **PATRÓN** `volumen_pendiente_norm` > `0.2399` → IC=+0.287 (n=2240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2399 (IC base=+0.091)

- **PATRÓN** `volumen_spike_ratio` < `1.4574` → IC=+0.272 (n=3956)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4574 (IC base=+0.091)

- **PATRÓN** `volumen_spike_ratio` > `2.6467` → IC=+0.278 (n=3955)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6467 (IC base=+0.091)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.304 (n=11479)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 91.0 (IC base=+0.091)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.155 (n=6554)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0098 (IC base=+0.077)

- **PATRÓN** `ibs_20min` < `0.6471` → IC=+0.149 (n=19661)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.6471 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` < `0.2482` → IC=+0.272 (n=6459)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2482 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` < `0.704` → IC=+0.272 (n=2803)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.704 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` > `1.1945` → IC=+0.270 (n=2123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1945 (IC base=+0.077)

- **PATRÓN** `volumen_pendiente_norm` > `0.294` → IC=+0.321 (n=1389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.294 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` < `1.5758` → IC=+0.296 (n=4092)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5758 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` > `2.275` → IC=+0.291 (n=4216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.275 (IC base=+0.077)

- **PATRÓN** `ballena_activa_n` < `75.0` → IC=+0.302 (n=9261)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 75.0 (IC base=+0.077)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.5796` → IC=-0.160 (n=2776)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5796
  - _Potencial_: sin este filtro IC_bueno=+0.206 (n=2777)

- **FILTRO** `ibs_20min` > `0.7241` → IC=-0.225 (n=1206)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7241
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=3620)

- **FILTRO** `sigma_ewma_delta_pct` > `4.245` → IC=-0.227 (n=1044)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.245
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=3782)

- **PATRÓN** `ibs_20min` > `0.9291` → IC=+0.332 (n=1389)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9291 (IC base=+0.023)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.091` → IC=+0.185 (n=1864)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 3.091 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.2292` → IC=+0.323 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2292 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` < `1.4451` → IC=+0.273 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4451 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` > `2.2519` → IC=+0.293 (n=818)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2519 (IC base=+0.023)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.311 (n=1219)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.023)

- **PATRÓN** `ibs_20min` < `0.1707` → IC=+0.156 (n=1207)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.1707 (IC base=-0.027)

- **PATRÓN** `volumen_pendiente_norm` < `0.1512` → IC=+0.405 (n=810)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1512 (IC base=-0.027)

- **PATRÓN** `volumen_spike_ratio` < `1.4194` → IC=+0.424 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4194 (IC base=-0.027)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.399 (n=809)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=-0.027)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.2965` → IC=+0.223 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2965 (IC base=+0.017)

- **PATRÓN** `volumen_regimen` < `1.1937` → IC=+0.206 (n=1985)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1937 (IC base=+0.017)

- **PATRÓN** `volumen_regimen` > `0.693` → IC=+0.210 (n=1775)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.693 (IC base=+0.017)

- **PATRÓN** `volumen_pendiente_norm` > `0.2774` → IC=+0.248 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2774 (IC base=+0.017)

- **PATRÓN** `volumen_spike_ratio` < `1.4174` → IC=+0.231 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4174 (IC base=+0.017)

- **PATRÓN** `volumen_spike_ratio` > `2.4426` → IC=+0.208 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4426 (IC base=+0.017)

- **PATRÓN** `ballena_activa_n` < `267.0` → IC=+0.240 (n=1309)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 267.0 (IC base=+0.017)

- **PATRÓN** `dist_vwap_pct` < `0.1262` → IC=+0.247 (n=1378)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1262 (IC base=-0.004)

- **PATRÓN** `volumen_regimen` < `1.1678` → IC=+0.237 (n=1357)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1678 (IC base=-0.004)

- **PATRÓN** `volumen_regimen` > `0.6223` → IC=+0.241 (n=1357)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6223 (IC base=-0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2713` → IC=+0.305 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2713 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.5317` → IC=+0.243 (n=575)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5317 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.1523` → IC=+0.253 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1523 (IC base=-0.004)

- **PATRÓN** `ballena_activa_n` < `214.0` → IC=+0.249 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 214.0 (IC base=-0.004)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.322 (n=1317)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.277)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.286 (n=3049)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.277)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.320 (n=1571)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.277)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.663` → IC=+0.310 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.663 (IC base=+0.277)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.290 (n=2544)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.277)

- **PATRÓN** `volumen_spike_ratio` > `1.6095` → IC=+0.282 (n=2814)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6095 (IC base=+0.277)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.287 (n=3459)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `2034.7208` → IC=+0.294 (n=968)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2034.7208 (IC base=+0.277)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.301 (n=1763)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.277)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.334 (n=1170)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.298)

- **PATRÓN** `drift_60min` |x|≤ `0.1789` → IC=+0.318 (n=1137)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1789 (IC base=+0.298)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.324 (n=987)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.298)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.302 (n=1171)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.298)

- **PATRÓN** `ibs_20min` < `0.0082` → IC=+0.303 (n=1136)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0082 (IC base=+0.298)

- **PATRÓN** `ibs_20min` > `0.1337` → IC=+0.307 (n=1720)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1337 (IC base=+0.298)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.337` → IC=+0.310 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.337 (IC base=+0.298)

- **PATRÓN** `volumen_pendiente_norm` < `0.1981` → IC=+0.298 (n=2537)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1981 (IC base=+0.298)

- **PATRÓN** `volumen_pendiente_norm` > `0.3435` → IC=+0.309 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3435 (IC base=+0.298)

- **PATRÓN** `volumen_spike_ratio` < `1.7424` → IC=+0.299 (n=1091)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7424 (IC base=+0.298)

- **PATRÓN** `volumen_spike_ratio` > `2.722` → IC=+0.311 (n=1125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.722 (IC base=+0.298)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.303 (n=1323)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.298)

- **PATRÓN** `libro_liquidez` > `1918.1184` → IC=+0.306 (n=1170)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1918.1184 (IC base=+0.298)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.305 (n=1697)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.298)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7325` → IC=-0.184 (n=1258)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7325
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=3790)

- **PATRÓN** `ibs_20min` > `0.8619` → IC=+0.165 (n=1226)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.8619 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.1456` → IC=+0.232 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1456 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.3584` → IC=+0.235 (n=1715)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3584 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `1.0082` → IC=+0.239 (n=1541)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0082 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `0.6704` → IC=+0.231 (n=1564)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6704 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.1022` → IC=+0.238 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1022 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.4521` → IC=+0.239 (n=1695)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4521 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `118.0` → IC=+0.253 (n=1729)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 118.0 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.1458` → IC=+0.242 (n=1205)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1458 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` < `1.1913` → IC=+0.245 (n=1239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1913 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.299 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.7888` → IC=+0.278 (n=790)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7888 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.4256` → IC=+0.264 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4256 (IC base=+0.003)

- **PATRÓN** `ballena_activa_n` < `103.0` → IC=+0.273 (n=1060)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 103.0 (IC base=+0.003)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7455` → IC=-0.238 (n=2110)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7455
  - _Potencial_: sin este filtro IC_bueno=+0.312 (n=2113)

- **FILTRO** `ibs_20min` > `0.6333` → IC=-0.233 (n=1011)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6333
  - _Potencial_: sin este filtro IC_bueno=+0.135 (n=3062)

- **FILTRO** `sigma_ewma_delta_pct` > `8.36` → IC=-0.251 (n=467)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.36
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=3606)

- **PATRÓN** `ibs_20min` > `0.7455` → IC=+0.312 (n=2113)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7455 (IC base=+0.037)

- **PATRÓN** `dist_vwap_pct` > `0.2124` → IC=+0.345 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2124 (IC base=+0.037)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.287` → IC=+0.197 (n=661)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 9.287 (IC base=+0.037)

- **PATRÓN** `volumen_regimen` < `0.8471` → IC=+0.341 (n=1034)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8471 (IC base=+0.037)

- **PATRÓN** `volumen_regimen` > `0.6998` → IC=+0.335 (n=1383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6998 (IC base=+0.037)

- **PATRÓN** `volumen_pendiente_norm` < `0.1583` → IC=+0.336 (n=1604)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1583 (IC base=+0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.2751` → IC=+0.354 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2751 (IC base=+0.037)

- **PATRÓN** `volumen_spike_ratio` < `1.4314` → IC=+0.361 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4314 (IC base=+0.037)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.354 (n=1330)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.037)

- **PATRÓN** `ibs_20min` < `0.6333` → IC=+0.135 (n=3062)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.6333 (IC base=+0.044)

- **PATRÓN** `dist_vwap_pct` < `0.2117` → IC=+0.254 (n=1405)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2117 (IC base=+0.044)

- **PATRÓN** `volumen_regimen` < `0.6966` → IC=+0.279 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6966 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.0706` → IC=+0.270 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0706 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` < `2.4505` → IC=+0.259 (n=1405)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4505 (IC base=+0.044)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.273 (n=1423)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.044)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.356 (n=1945)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.312)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.313 (n=2198)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.312)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.314 (n=2286)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.312)

- **PATRÓN** `ibs_20min` > `0.7632` → IC=+0.348 (n=1945)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7632 (IC base=+0.312)

- **PATRÓN** `dist_vwap_pct` > `0.2044` → IC=+0.336 (n=1209)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2044 (IC base=+0.312)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.824` → IC=+0.329 (n=1057)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.824 (IC base=+0.312)

- **PATRÓN** `volumen_regimen` > `0.6293` → IC=+0.321 (n=2177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6293 (IC base=+0.312)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.348 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.312)

- **PATRÓN** `volumen_spike_ratio` > `1.425` → IC=+0.323 (n=2093)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.425 (IC base=+0.312)

- **PATRÓN** `libro_liquidez` > `2571.936` → IC=+0.312 (n=1451)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2571.936 (IC base=+0.312)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.342 (n=1908)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.312)

- **PATRÓN** `sigma_h` > `0.0153` → IC=+0.344 (n=1546)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0153 (IC base=+0.313)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.321 (n=1163)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.313)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.315 (n=1138)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.313)

- **PATRÓN** `ibs_20min` < `0.38` → IC=+0.333 (n=2321)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.38 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` < `0.2325` → IC=+0.318 (n=2230)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2325 (IC base=+0.313)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.621` → IC=+0.330 (n=860)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.621 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` < `0.723` → IC=+0.320 (n=1020)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.723 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` > `1.2131` → IC=+0.341 (n=773)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2131 (IC base=+0.313)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.365 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` < `1.4108` → IC=+0.324 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4108 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` > `2.1339` → IC=+0.315 (n=970)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1339 (IC base=+0.313)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.227 (n=5072)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.122` → IC=+0.195 (n=6689)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.122 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=15759)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `0.545` → IC=+0.234 (n=15202)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.545 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.1618` → IC=+0.207 (n=5959)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1618 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.169` → IC=+0.255 (n=3958)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.169 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `1.1856` → IC=+0.160 (n=10110)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1856 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` > `0.6244` → IC=+0.158 (n=10110)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.6244 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.2937` → IC=+0.206 (n=2204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2937 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `2.6045` → IC=+0.188 (n=4926)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6045 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.196 (n=14128)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 90.0 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0115` → IC=+0.184 (n=14778)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0115 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.0803` → IC=+0.222 (n=4929)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0803 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=5545)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.5192` → IC=+0.238 (n=14773)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5192 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` < `0.1774` → IC=+0.175 (n=10637)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1774 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.757` → IC=+0.194 (n=2366)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 9.757 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.472` → IC=+0.184 (n=13823)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 3.472 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.1817` → IC=+0.163 (n=10533)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1817 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2955` → IC=+0.221 (n=2210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2955 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6404` → IC=+0.189 (n=4664)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6404 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `95.0` → IC=+0.195 (n=13740)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 95.0 (IC base=+0.181)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.225 (n=841)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0055 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.1043` → IC=+0.259 (n=1108)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1043 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.240 (n=933)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.229 (n=1704)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.9377` → IC=+0.298 (n=1678)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9377 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.714` → IC=+0.330 (n=808)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.714 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2817` → IC=+0.286 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2817 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` < `1.8383` → IC=+0.223 (n=1598)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8383 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `1.4361` → IC=+0.224 (n=2394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4361 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=2785)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.257 (n=2007)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0091 (IC base=+0.254)

- **PATRÓN** `drift_60min` |x|≤ `0.097` → IC=+0.307 (n=883)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.097 (IC base=+0.254)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.260 (n=2075)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.254)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.256 (n=1834)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.254)

- **PATRÓN** `ibs_20min` < `0.4211` → IC=+0.272 (n=2006)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4211 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` < `0.1005` → IC=+0.258 (n=1761)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1005 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` > `0.3016` → IC=+0.278 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3016 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` < `1.4432` → IC=+0.277 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4432 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` > `2.7158` → IC=+0.258 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7158 (IC base=+0.254)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.257 (n=2307)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.254)

- **PATRÓN** `libro_liquidez` > `1469.58` → IC=+0.263 (n=1792)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1469.58 (IC base=+0.254)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.256 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.254)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.202 (n=774)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.0641` → IC=+0.183 (n=770)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.0641 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.157 (n=2415)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.2835` → IC=+0.213 (n=2310)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2835 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.185` → IC=+0.215 (n=1192)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.185 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.002` → IC=+0.211 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.002 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.6949` → IC=+0.152 (n=1018)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6949 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `1.0614` → IC=+0.142 (n=1047)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.0614 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.185 (n=357)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.4042` → IC=+0.158 (n=756)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4042 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.4689` → IC=+0.152 (n=756)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 2.4689 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `408.0` → IC=+0.145 (n=2233)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 408.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.174 (n=2443)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0062 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.2376` → IC=+0.168 (n=2148)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.2376 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.182 (n=1165)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.6183` → IC=+0.206 (n=2441)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6183 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.165` → IC=+0.178 (n=461)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 11.165 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.076` → IC=+0.146 (n=2132)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 4.076 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.2012` → IC=+0.158 (n=2441)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2012 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.0946` → IC=+0.147 (n=2112)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.0946 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.4805` → IC=+0.148 (n=2318)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4805 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.4259` → IC=+0.143 (n=2320)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4259 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `215.0` → IC=+0.183 (n=989)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 215.0 (IC base=+0.144)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.238 (n=1168)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.3992` → IC=+0.225 (n=2266)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3992 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.236 (n=940)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=1355)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.269` → IC=+0.307 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.269 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.213 (n=2233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.353` → IC=+0.235 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.353 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.7603` → IC=+0.213 (n=1104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7603 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.7088` → IC=+0.224 (n=1137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7088 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.218 (n=3090)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `1924.7784` → IC=+0.226 (n=1168)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1924.7784 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.244 (n=1968)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.4221` → IC=+0.260 (n=1967)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4221 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.283 (n=851)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.0286` → IC=+0.289 (n=986)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0286 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.242` → IC=+0.283 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.242 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.3592` → IC=+0.293 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3592 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.7622` → IC=+0.237 (n=947)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7622 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.1736` → IC=+0.245 (n=1432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1736 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.239 (n=1168)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1911.3596` → IC=+0.250 (n=1014)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1911.3596 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.243 (n=1448)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.237)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.206 (n=831)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0775` → IC=+0.196 (n=829)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.0775 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.150 (n=2573)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.2722` → IC=+0.202 (n=2484)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2722 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.1388` → IC=+0.187 (n=1478)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1388 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.512` → IC=+0.195 (n=431)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 11.512 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.0218` → IC=+0.144 (n=2186)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.0218 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2887` → IC=+0.175 (n=370)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2887 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.8246` → IC=+0.142 (n=1623)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.8246 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.516` → IC=+0.158 (n=811)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.516 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `6882.1647` → IC=+0.201 (n=1127)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6882.1647 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `132.0` → IC=+0.145 (n=2427)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 132.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.165 (n=2324)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0065 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.3948` → IC=+0.141 (n=2634)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3948 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.160 (n=1252)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 15.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.6798` → IC=+0.184 (n=2634)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6798 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.1576` → IC=+0.153 (n=2639)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1576 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.411` → IC=+0.145 (n=637)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 9.411 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8521` → IC=+0.154 (n=1757)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8521 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2969` → IC=+0.184 (n=397)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2969 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.8095` → IC=+0.128 (n=1658)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.8095 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `1.5263` → IC=+0.126 (n=2221)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.5263 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `6175.844` → IC=+0.180 (n=1194)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 6175.844 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `110.0` → IC=+0.132 (n=2159)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 110.0 (IC base=+0.126)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.169 (n=1262)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.011 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.161 (n=1336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 15.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.4769` → IC=+0.212 (n=2780)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4769 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.195` → IC=+0.190 (n=1543)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.195 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.221` → IC=+0.290 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.221 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `1.1752` → IC=+0.133 (n=2780)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.1752 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.7046` → IC=+0.125 (n=2484)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.7046 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` < `0.1634` → IC=+0.132 (n=2836)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.1634 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.437` → IC=+0.143 (n=900)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.437 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.126 (n=2902)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2638.9696` → IC=+0.200 (n=1261)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2638.9696 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.145 (n=1155)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 21.0 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0115` → IC=+0.143 (n=2873)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0115 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1101` → IC=+0.165 (n=959)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1101 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=2929)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.64` → IC=+0.219 (n=2874)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.64 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.2013` → IC=+0.146 (n=2779)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.2013 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.354` → IC=+0.137 (n=2534)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 2.354 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.1787` → IC=+0.128 (n=2873)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.1787 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.276` → IC=+0.135 (n=395)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.276 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.5414` → IC=+0.123 (n=1188)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 1.5414 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` > `2.4486` → IC=+0.126 (n=900)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.4486 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2519.0986` → IC=+0.182 (n=1303)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2519.0986 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.125 (n=2663)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 46.0 (IC base=+0.118)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.248 (n=2267)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.1681` → IC=+0.240 (n=1117)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1681 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.227 (n=2634)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.230 (n=2282)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.6633` → IC=+0.258 (n=2537)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6633 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` > `0.1804` → IC=+0.232 (n=1600)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1804 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` < `0.8265` → IC=+0.226 (n=2614)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8265 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.58` → IC=+0.255 (n=1144)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.58 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` < `1.1691` → IC=+0.225 (n=2537)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1691 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.6232` → IC=+0.233 (n=2537)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6232 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2319` → IC=+0.266 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2319 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `2.4642` → IC=+0.228 (n=2473)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4642 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `1.8078` → IC=+0.234 (n=1648)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8078 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `2934.4818` → IC=+0.234 (n=846)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2934.4818 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0128` → IC=+0.241 (n=1139)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0128 (IC base=+0.236)

- **PATRÓN** `sigma_h` > `0.0227` → IC=+0.246 (n=1176)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0227 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.0881` → IC=+0.262 (n=863)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0881 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.252 (n=1258)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.242 (n=1160)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.438` → IC=+0.264 (n=2587)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.438 (IC base=+0.236)

- **PATRÓN** `dist_vwap_pct` > `0.3035` → IC=+0.244 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3035 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.279` → IC=+0.272 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.279 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` < `0.8693` → IC=+0.237 (n=1725)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8693 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` > `0.6424` → IC=+0.240 (n=2586)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6424 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.287 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `1.8332` → IC=+0.234 (n=1617)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8332 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `1.4336` → IC=+0.237 (n=2425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4336 (IC base=+0.236)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.203 (n=1681)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.131` → IC=+0.187 (n=1677)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.131 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=3996)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `0.3287` → IC=+0.202 (n=3810)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3287 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.8042` → IC=+0.196 (n=580)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.8042 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.557` → IC=+0.200 (n=1633)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.557 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `0.8609` → IC=+0.186 (n=2294)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.8609 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` > `1.1918` → IC=+0.170 (n=1147)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.1918 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.0739` → IC=+0.174 (n=1537)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.0739 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.4277` → IC=+0.181 (n=1237)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.4277 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.173 (n=4277)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `8460.6979` → IC=+0.185 (n=1727)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 8460.6979 (IC base=+0.168)

- **PATRÓN** `ibs_20min` < `0.3902` → IC=+0.158 (n=2744)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.3902 (IC base=+0.083)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.123 (n=1783)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 27.0 (IC base=+0.083)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.197 (n=1028)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0057 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.0994` → IC=+0.236 (n=453)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0994 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.217 (n=930)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `0.2259` → IC=+0.218 (n=1028)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2259 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `0.3033` → IC=+0.210 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3033 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.975` → IC=+0.201 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.975 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.474` → IC=+0.184 (n=1082)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 6.474 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.8799` → IC=+0.201 (n=686)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8799 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` < `0.1523` → IC=+0.186 (n=1083)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.1523 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.0916` → IC=+0.187 (n=359)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.0916 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `2.1871` → IC=+0.198 (n=886)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.1871 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `10184.2164` → IC=+0.186 (n=1028)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 10184.2164 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.164 (n=555)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0033 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.6372` → IC=+0.139 (n=1106)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.6372 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `163.0` → IC=+0.169 (n=539)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 163.0 (IC base=+0.085)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.245 (n=528)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.2106` → IC=+0.192 (n=796)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.2106 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=1244)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.6377` → IC=+0.252 (n=795)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6377 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.7815` → IC=+0.195 (n=188)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.7815 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` < `0.2051` → IC=+0.183 (n=1076)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.2051 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.859` → IC=+0.218 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.859 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.8339` → IC=+0.196 (n=796)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8339 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.159` → IC=+0.201 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.159 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `1.4263` → IC=+0.189 (n=393)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.4263 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `1.7848` → IC=+0.190 (n=785)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.7848 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.1008` → IC=+0.183 (n=389)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.1008 (IC base=+0.075)

- **PATRÓN** `libro_liquidez` > `8174.0114` → IC=+0.142 (n=529)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 8174.0114 (IC base=+0.075)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.154 (n=420)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.007 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.165 (n=954)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 6.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.199 (n=956)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.97` → IC=+0.218 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.97 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.049` → IC=+0.238 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.049 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `0.884` → IC=+0.157 (n=636)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.884 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` > `0.7054` → IC=+0.152 (n=851)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.7054 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2298` → IC=+0.165 (n=177)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.2298 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `1.4313` → IC=+0.170 (n=307)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.4313 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `2.1542` → IC=+0.144 (n=417)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.1542 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.151 (n=997)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.02 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `2749.8` → IC=+0.177 (n=432)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 2749.8 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.5745` → IC=+0.133 (n=922)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.5745 (IC base=+0.047)

- **PATRÓN** `libro_liquidez` > `2580.4685` → IC=+0.144 (n=475)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 2580.4685 (IC base=+0.047)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0261` → IC=+0.170 (n=268)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0261 (IC base=+0.163)

- **PATRÓN** `sigma_h` > `0.0165` → IC=+0.213 (n=179)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0165 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.2705` → IC=+0.180 (n=179)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.2705 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.220 (n=130)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.7333` → IC=+0.196 (n=179)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.7333 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.3078` → IC=+0.178 (n=141)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.3078 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` < `1.1996` → IC=+0.166 (n=300)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 1.1996 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.317` → IC=+0.188 (n=238)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 3.317 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `0.9954` → IC=+0.168 (n=236)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.9954 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` > `0.6893` → IC=+0.169 (n=240)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 0.6893 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.1036` → IC=+0.178 (n=85)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1036 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.806` → IC=+0.193 (n=161)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.806 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `2.3887` → IC=+0.175 (n=81)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.3887 (IC base=+0.163)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.186 (n=320)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.03 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `2665.5936` → IC=+0.194 (n=122)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2665.5936 (IC base=+0.163)

- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.172 (n=266)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0131 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.152 (n=268)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 7.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.1942` → IC=+0.162 (n=131)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.1942 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `1.2189` → IC=+0.278 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2189 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.338` → IC=+0.183 (n=80)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 5.338 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.8744` → IC=+0.167 (n=199)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8744 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` < `0.1158` → IC=+0.142 (n=272)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` < 0.1158 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2383` → IC=+0.178 (n=57)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2383 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.5322` → IC=+0.201 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5322 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `2.7694` → IC=+0.156 (n=94)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.7694 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `1946.0402` → IC=+0.139 (n=297)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 1946.0402 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.153 (n=275)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 19.0 (IC base=+0.136)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.230 (n=6615)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=20654)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.4375` → IC=+0.229 (n=19829)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4375 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.8756` → IC=+0.211 (n=2386)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8756 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.089` → IC=+0.254 (n=4865)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.089 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.2173` → IC=+0.163 (n=13328)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2173 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2411` → IC=+0.206 (n=3578)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2411 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6173` → IC=+0.192 (n=6443)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6173 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `107.0` → IC=+0.202 (n=18479)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 107.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.197 (n=8002)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0058 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.012` → IC=+0.195 (n=6048)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.012 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.484` → IC=+0.194 (n=18144)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.484 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=6750)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` < `0.5909` → IC=+0.242 (n=18150)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5909 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` < `0.1767` → IC=+0.172 (n=11297)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1767 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.615` → IC=+0.204 (n=2481)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.615 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.461` → IC=+0.194 (n=17633)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 3.461 (IC base=+0.190)

- **PATRÓN** `volumen_regimen` < `0.633` → IC=+0.171 (n=4070)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.633 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.292` → IC=+0.254 (n=2482)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.292 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.6327` → IC=+0.202 (n=5763)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6327 (IC base=+0.190)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.222 (n=11522)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.190)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3589` → IC=+0.232 (n=3198)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3589 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.247 (n=1549)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.234 (n=2155)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` > `0.8601` → IC=+0.300 (n=2131)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8601 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.727` → IC=+0.337 (n=1036)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.727 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.2324` → IC=+0.292 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2324 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` < `1.4443` → IC=+0.232 (n=1028)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4443 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.2779` → IC=+0.238 (n=1398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2779 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.248 (n=3493)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `2052.17` → IC=+0.235 (n=1066)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2052.17 (IC base=+0.232)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.253 (n=1970)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.232)

- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.270 (n=2804)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0096 (IC base=+0.266)

- **PATRÓN** `drift_60min` |x|≤ `0.1216` → IC=+0.292 (n=1234)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1216 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.271 (n=2579)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.266)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.267 (n=2546)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` < `0.5314` → IC=+0.287 (n=2803)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5314 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` < `0.097` → IC=+0.267 (n=2540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.097 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` > `0.289` → IC=+0.290 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.289 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` < `1.5624` → IC=+0.266 (n=1177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5624 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` > `2.6599` → IC=+0.275 (n=892)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6599 (IC base=+0.266)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.266 (n=3224)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.266)

- **PATRÓN** `libro_liquidez` > `1756.63` → IC=+0.274 (n=1868)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1756.63 (IC base=+0.266)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.275 (n=965)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.266)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.184 (n=1082)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.003 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.1043` → IC=+0.153 (n=1421)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1043 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=3362)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.2171` → IC=+0.193 (n=3231)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.2171 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.3183` → IC=+0.201 (n=1094)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3183 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.461` → IC=+0.158 (n=677)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 9.461 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.111` → IC=+0.142 (n=2836)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.111 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.6354` → IC=+0.163 (n=1077)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.6354 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` > `1.0732` → IC=+0.143 (n=1464)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.0732 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` < `0.0721` → IC=+0.143 (n=2890)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` < 0.0721 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.2726` → IC=+0.180 (n=461)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2726 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.1554` → IC=+0.148 (n=2786)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.1554 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.5212` → IC=+0.144 (n=2829)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.5212 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `426.0` → IC=+0.151 (n=3105)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 426.0 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.160 (n=2774)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0061 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0785` → IC=+0.177 (n=925)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.0785 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=1011)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.6865` → IC=+0.185 (n=2773)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6865 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1394` → IC=+0.151 (n=2654)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1394 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.052` → IC=+0.143 (n=1327)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 3.052 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.0503` → IC=+0.150 (n=2441)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.0503 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2189` → IC=+0.193 (n=515)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2189 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.4125` → IC=+0.142 (n=889)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4125 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.7762` → IC=+0.142 (n=1778)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.7762 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=3600)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `232.0` → IC=+0.145 (n=861)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 232.0 (IC base=+0.136)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.253 (n=1103)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0128 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=3456)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=2961)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=1235)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.184` → IC=+0.324 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.184 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` < `0.1312` → IC=+0.227 (n=3111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1312 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `2.7317` → IC=+0.236 (n=1461)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7317 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.231 (n=3958)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `1351.5384` → IC=+0.230 (n=3303)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1351.5384 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.245 (n=2759)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0109 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.1798` → IC=+0.260 (n=1379)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1798 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.264 (n=1186)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.243 (n=1436)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.0525` → IC=+0.305 (n=1044)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0525 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.326` → IC=+0.302 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.326 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.349` → IC=+0.308 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.349 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.1556` → IC=+0.254 (n=2001)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1556 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.247 (n=1618)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1913.1432` → IC=+0.251 (n=1419)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1913.1432 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.248 (n=2021)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.241)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.189 (n=1510)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0041 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.4311` → IC=+0.150 (n=3424)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4311 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=3554)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.9017` → IC=+0.277 (n=1142)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9017 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.1961` → IC=+0.166 (n=1588)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1961 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.995` → IC=+0.155 (n=1533)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 2.995 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.6164` → IC=+0.163 (n=1142)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.6164 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.2331` → IC=+0.183 (n=604)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2331 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.5203` → IC=+0.157 (n=1471)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.5203 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `7311.7758` → IC=+0.240 (n=1141)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7311.7758 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.153 (n=1455)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 69.0 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.158 (n=2862)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0077 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.4405` → IC=+0.147 (n=2860)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.4405 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=1048)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.7175` → IC=+0.192 (n=2860)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.7175 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1485` → IC=+0.149 (n=2636)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1485 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.985` → IC=+0.166 (n=429)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 10.985 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.6918` → IC=+0.154 (n=1259)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6918 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2944` → IC=+0.225 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2944 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.22` → IC=+0.140 (n=2427)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.22 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.5368` → IC=+0.146 (n=2465)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.5368 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `6185.2895` → IC=+0.209 (n=954)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6185.2895 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `95.0` → IC=+0.145 (n=1870)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 95.0 (IC base=+0.137)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.152 (n=1572)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.011 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.152 (n=2444)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 11.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.4333` → IC=+0.193 (n=3467)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.4333 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `1.0106` → IC=+0.207 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0106 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.428` → IC=+0.265 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.428 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `0.8787` → IC=+0.134 (n=2310)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8787 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.1012` → IC=+0.124 (n=3285)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1012 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `2.4923` → IC=+0.123 (n=3382)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.4923 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.123 (n=3615)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2698.1582` → IC=+0.243 (n=1154)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2698.1582 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.154 (n=2881)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0106 (IC base=+0.121)

- **PATRÓN** `drift_60min` |x|≤ `0.1356` → IC=+0.155 (n=1090)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1356 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.154 (n=1533)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 15.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.210 (n=3285)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6667 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` < `0.2128` → IC=+0.140 (n=2918)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.2128 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.138` → IC=+0.144 (n=3147)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 3.138 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `0.6386` → IC=+0.149 (n=1090)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6386 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.2253` → IC=+0.170 (n=574)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2253 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.4353` → IC=+0.154 (n=1029)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4353 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2571.994` → IC=+0.200 (n=1090)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2571.994 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.133 (n=3078)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 51.0 (IC base=+0.121)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0139` → IC=+0.258 (n=2871)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0139 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.240 (n=3354)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.240 (n=2885)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` > `0.6154` → IC=+0.271 (n=2872)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6154 (IC base=+0.236)

- **PATRÓN** `dist_vwap_pct` > `0.1915` → IC=+0.251 (n=1702)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1915 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.272` → IC=+0.282 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.272 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` < `1.2206` → IC=+0.240 (n=3214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2206 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` > `0.6427` → IC=+0.240 (n=3214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6427 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2366` → IC=+0.259 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2366 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `1.5432` → IC=+0.243 (n=2802)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5432 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `2934.4818` → IC=+0.241 (n=1072)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2934.4818 (IC base=+0.236)

- **PATRÓN** `sigma_h` > `0.0258` → IC=+0.260 (n=1103)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0258 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.243 (n=3118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.5206` → IC=+0.270 (n=3308)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5206 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` < `0.2951` → IC=+0.244 (n=3238)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2951 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.201` → IC=+0.278 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.201 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` > `1.2151` → IC=+0.260 (n=1103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2151 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2857` → IC=+0.304 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2857 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.8121` → IC=+0.236 (n=2069)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8121 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `1.4292` → IC=+0.240 (n=3102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4292 (IC base=+0.238)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.237 (n=3035)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.238)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.199 (n=5629)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.245 (n=1929)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.5012` → IC=+0.224 (n=5772)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5012 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.230 (n=2093)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.9338` → IC=+0.253 (n=1924)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9338 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` < `0.4234` → IC=+0.219 (n=4191)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4234 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.856` → IC=+0.222 (n=948)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.856 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.569` → IC=+0.216 (n=5136)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.569 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` < `0.707` → IC=+0.227 (n=1877)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.707 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `0.883` → IC=+0.218 (n=2845)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.883 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` < `0.1054` → IC=+0.218 (n=5387)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1054 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.1654` → IC=+0.222 (n=1630)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1654 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `1.4525` → IC=+0.224 (n=1894)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4525 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.223 (n=4523)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `3721.1308` → IC=+0.225 (n=3848)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3721.1308 (IC base=+0.216)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.238 (n=1414)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.4905` → IC=+0.212 (n=4234)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4905 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=1432)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.212 (n=1883)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` < `0.7304` → IC=+0.205 (n=4234)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7304 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.6484` → IC=+0.209 (n=730)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6484 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` < `0.1762` → IC=+0.194 (n=3752)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1762 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.791` → IC=+0.209 (n=3786)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.791 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` < `1.0969` → IC=+0.204 (n=3547)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0969 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` > `0.7271` → IC=+0.194 (n=3601)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` > 0.7271 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.199 (n=3893)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.2229` → IC=+0.203 (n=852)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2229 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` < `1.5345` → IC=+0.203 (n=1836)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5345 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `2.1886` → IC=+0.206 (n=1892)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1886 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.199 (n=5629)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `ballena_activa_n` < `171.0` → IC=+0.208 (n=3661)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 171.0 (IC base=+0.198)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.275 (n=797)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.265)

- **PATRÓN** `drift_60min` |x|≤ `0.1127` → IC=+0.292 (n=397)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1127 (IC base=+0.265)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.275 (n=900)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.265)

- **PATRÓN** `ibs_20min` < `0.4609` → IC=+0.283 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4609 (IC base=+0.265)

- **PATRÓN** `dist_vwap_pct` < `0.1962` → IC=+0.278 (n=836)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1962 (IC base=+0.265)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.122` → IC=+0.286 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.122 (IC base=+0.265)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.694` → IC=+0.266 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.694 (IC base=+0.265)

- **PATRÓN** `volumen_regimen` < `1.2234` → IC=+0.267 (n=901)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2234 (IC base=+0.265)

- **PATRÓN** `volumen_regimen` > `0.868` → IC=+0.284 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.868 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` > `0.2866` → IC=+0.343 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2866 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` < `2.4907` → IC=+0.270 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4907 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` > `2.1875` → IC=+0.265 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1875 (IC base=+0.265)

- **PATRÓN** `libro_liquidez` > `12852.1439` → IC=+0.276 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12852.1439 (IC base=+0.265)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.261 (n=499)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.3831` → IC=+0.193 (n=1495)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.3831 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.220 (n=547)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.188 (n=555)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 5.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` < `0.1373` → IC=+0.199 (n=658)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.1373 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.6858` → IC=+0.202 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6858 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.318` → IC=+0.201 (n=1466)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.318 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `1.2393` → IC=+0.188 (n=1495)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 1.2393 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.1519` → IC=+0.198 (n=455)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1519 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `1.4122` → IC=+0.197 (n=496)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4122 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `1.8036` → IC=+0.182 (n=991)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.8036 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `14605.0565` → IC=+0.185 (n=678)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 14605.0565 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `684.0` → IC=+0.191 (n=1449)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 684.0 (IC base=+0.179)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `drift_60min` |x|≤ `0.587` → IC=+0.203 (n=858)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.587 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.235 (n=323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` < `0.3897` → IC=+0.198 (n=286)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.3897 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.240 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.492` → IC=+0.239 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.492 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.2085` → IC=+0.238 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2085 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `1.8172` → IC=+0.204 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8172 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `2760.165` → IC=+0.226 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2760.165 (IC base=+0.195)

- **PATRÓN** `ballena_activa_n` < `5.0` → IC=+0.197 (n=381)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 5.0 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0116` → IC=+0.242 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0116 (IC base=+0.228)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.224 (n=27)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.233 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.228)

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
- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.219 (n=1601)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.4527` → IC=+0.213 (n=1600)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4527 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.223 (n=565)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` < `0.4986` → IC=+0.221 (n=1067)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4986 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` < `0.3965` → IC=+0.216 (n=1605)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3965 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.026` → IC=+0.214 (n=1454)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.026 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `0.707` → IC=+0.212 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.707 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `1.224` → IC=+0.206 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.224 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` < `0.1034` → IC=+0.210 (n=1474)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1034 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `2.4455` → IC=+0.214 (n=1566)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4455 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=1661)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.240 (n=440)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.4848` → IC=+0.217 (n=1314)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4848 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.208 (n=501)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.211 (n=886)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` < `0.4046` → IC=+0.199 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4046 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `0.0897` → IC=+0.201 (n=1314)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0897 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` > `0.6251` → IC=+0.212 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6251 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.353` → IC=+0.199 (n=1193)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 4.353 (IC base=+0.195)

- **PATRÓN** `volumen_regimen` < `0.6401` → IC=+0.223 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6401 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.074` → IC=+0.226 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.074 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` < `2.1958` → IC=+0.202 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1958 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `1.7867` → IC=+0.197 (n=858)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.7867 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `6506.9218` → IC=+0.202 (n=1174)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6506.9218 (IC base=+0.195)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.215 (n=587)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0096 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.226 (n=593)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.270 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.189)

- **PATRÓN** `dist_vwap_pct` > `0.7224` → IC=+0.236 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7224 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.252` → IC=+0.219 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.252 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` < `0.6386` → IC=+0.236 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6386 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` < `0.1058` → IC=+0.200 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1058 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.0795` → IC=+0.194 (n=394)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0795 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` < `1.5721` → IC=+0.198 (n=376)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.5721 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `1.4783` → IC=+0.195 (n=854)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4783 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.198 (n=1036)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.02 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `3561.855` → IC=+0.219 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3561.855 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.218 (n=285)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.217)

- **PATRÓN** `sigma_h` > `0.0116` → IC=+0.219 (n=293)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0116 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.5971` → IC=+0.239 (n=646)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5971 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.247 (n=452)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.7347` → IC=+0.242 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7347 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` > `0.5012` → IC=+0.223 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5012 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` < `0.3026` → IC=+0.218 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3026 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.893` → IC=+0.220 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.893 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.823` → IC=+0.226 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.823 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` > `0.6739` → IC=+0.219 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6739 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` < `0.1057` → IC=+0.231 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1057 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.1932` → IC=+0.256 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1932 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `2968.4304` → IC=+0.236 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2968.4304 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.254 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.217)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.154 (n=663)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0036 (IC base=+0.059)

- **PATRÓN** `ibs_20min` > `0.7519` → IC=+0.194 (n=1261)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.7519 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.1457` → IC=+0.140 (n=957)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.1457 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.663` → IC=+0.147 (n=414)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 10.663 (IC base=+0.059)

- **PATRÓN** `ibs_20min` < `0.0478` → IC=+0.260 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0478 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.1459` → IC=+0.132 (n=338)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.1459 (IC base=+0.041)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.3733` → IC=-0.152 (n=202)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3733
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=609)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.128 (n=641)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0059 (IC base=+0.081)

- **PATRÓN** `ibs_20min` > `0.3733` → IC=+0.160 (n=609)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.3733 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.1188` → IC=+0.174 (n=299)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.1188 (IC base=+0.081)

- **PATRÓN** `ibs_20min` < `0.0653` → IC=+0.285 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0653 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.2162` → IC=+0.167 (n=100)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2162 (IC base=+0.051)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.7036` → IC=-0.159 (n=130)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7036
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=392)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.130 (n=433)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0051 (IC base=+0.076)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.132 (n=316)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 15.0 (IC base=+0.076)

- **PATRÓN** `ibs_20min` > `0.7794` → IC=+0.225 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7794 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` > `0.1265` → IC=+0.175 (n=309)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.1265 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.677` → IC=+0.204 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.677 (IC base=+0.076)

- **PATRÓN** `ibs_20min` < `0.0314` → IC=+0.252 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0314 (IC base=+0.012)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.200 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` > `0.7109` → IC=+0.135 (n=154)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.7109 (IC base=+0.023)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.801` → IC=+0.134 (n=140)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 8.801 (IC base=+0.023)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.145 (n=311)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.011 (IC base=+0.059)

- **PATRÓN** `ibs_20min` < `0.449` → IC=+0.167 (n=322)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.449 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.982` → IC=+0.295 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.982 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` > `1.1045` → IC=+0.173 (n=108)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 1.1045 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.1522` → IC=+0.157 (n=97)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.1522 (IC base=+0.059)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `8.0` → IC=-0.336 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=269)

- **FILTRO** `dist_vwap_pct` > `0.2352` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2352
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=324)

- **FILTRO** `volumen_regimen` < `0.7761` → IC=-0.305 (n=85)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7761
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=255)

- **FILTRO** `libro_liquidez` < `903.6493` → IC=-0.213 (n=85)

  - _Acción_: SKIP cuando `libro_liquidez` < 903.6493
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=255)

- **FILTRO** `ibs_20min` > `0.5111` → IC=-0.314 (n=154)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5111
  - _Potencial_: sin este filtro IC_bueno=-0.264 (n=155)

- **FILTRO** `dist_vwap_pct` > `0.4704` → IC=-0.450 (n=18)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4704
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=291)

- **FILTRO** `sigma_ewma_delta_pct` > `9.965` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.965
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=283)

- **FILTRO** `volumen_pendiente_norm` > `0.0448` → IC=-0.379 (n=31)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0448
  - _Potencial_: sin este filtro IC_bueno=-0.276 (n=190)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `volumen_regimen` < `1.2266` → IC=-0.296 (n=52)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2266
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=52)

- **FILTRO** `ibs_20min` < `0.3442` → IC=-0.266 (n=45)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3442
  - _Potencial_: sin este filtro IC_bueno=-0.240 (n=94)

- **FILTRO** `volumen_regimen` > `0.807` → IC=-0.333 (n=34)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.807
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=105)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` < `0.0027` → IC=-0.293 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0027
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=87)

- **FILTRO** `ibs_20min` < `0.5843` → IC=-0.467 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5843
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=86)

- **FILTRO** `ibs_20min` > `0.702` → IC=-0.405 (n=40)

  - _Acción_: SKIP cuando `ibs_20min` > 0.702
  - _Potencial_: sin este filtro IC_bueno=-0.268 (n=80)

- **FILTRO** `dist_vwap_pct` > `0.1281` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1281
  - _Potencial_: sin este filtro IC_bueno=-0.293 (n=90)

- **FILTRO** `volumen_spike_ratio` < `1.7061` → IC=-0.367 (n=43)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.7061
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=43)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.313 (n=105)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.400 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=104)

- **FILTRO** `volumen_regimen` < `0.7553` → IC=-0.344 (n=30)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7553
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=92)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.242 (n=29)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.216 (n=93)

- **FILTRO** `sigma_h` < `0.0099` → IC=-0.321 (n=37)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0099
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=13)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.230 (n=35)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.426 (n=25)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=25)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.213 (n=207)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.191 (n=318)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 15.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `0.6686` → IC=+0.177 (n=617)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.6686 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.5399` → IC=+0.256 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5399 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.608` → IC=+0.138 (n=338)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 3.608 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.636` → IC=+0.140 (n=454)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 2.636 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.6225` → IC=+0.183 (n=206)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6225 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` < `0.2099` → IC=+0.163 (n=571)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` < 0.2099 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.4061` → IC=+0.162 (n=512)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.4061 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.831` → IC=+0.152 (n=208)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 8.831 (IC base=+0.032)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.7055` → IC=-0.172 (n=59)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7055
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=184)

- **PATRÓN** `dist_vwap_pct` > `0.5497` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5497 (IC base=+0.018)

- **PATRÓN** `ibs_20min` < `0.2374` → IC=+0.172 (n=336)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.2374 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.854` → IC=+0.141 (n=101)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 9.854 (IC base=+0.095)

- **PATRÓN** `volumen_pendiente_norm` > `0.2682` → IC=+0.136 (n=53)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.2682 (IC base=+0.095)

- **PATRÓN** `volumen_spike_ratio` > `1.773` → IC=+0.129 (n=203)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.773 (IC base=+0.095)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1261` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1261
  - _Potencial_: sin este filtro IC_bueno=+0.177 (n=196)

- **FILTRO** `ibs_20min` > `0.1566` → IC=-0.147 (n=114)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1566
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=224)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.142 (n=135)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.004 (IC base=+0.126)

- **PATRÓN** `sigma_h` > `0.003` → IC=+0.137 (n=180)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.003 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.188` → IC=+0.128 (n=135)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.188 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.200 (n=68)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.148 (n=69)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.8015` → IC=+0.165 (n=180)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.8015 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.0967` → IC=+0.149 (n=166)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.0967 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.169` → IC=+0.162 (n=211)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 9.169 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.6242` → IC=+0.186 (n=68)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6242 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` > `1.1915` → IC=+0.138 (n=67)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 1.1915 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` < `0.1261` → IC=+0.177 (n=196)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.1261 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.7967` → IC=+0.195 (n=116)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.7967 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=170)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `1624.9844` → IC=+0.185 (n=201)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1624.9844 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.906` → IC=+0.182 (n=61)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 10.906 (IC base=+0.000)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2` → IC=-0.233 (n=58)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=114)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.287 (n=167)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` > `0.6818` → IC=+0.274 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6818 (IC base=+0.232)

- **PATRÓN** `dist_vwap_pct` > `0.6827` → IC=+0.387 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6827 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.903` → IC=+0.338 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.903 (IC base=+0.232)

- **PATRÓN** `volumen_regimen` < `0.5821` → IC=+0.287 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5821 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` < `0.2645` → IC=+0.256 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2645 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.0951` → IC=+0.298 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0951 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` < `1.4665` → IC=+0.315 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4665 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.2925` → IC=+0.274 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2925 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.003` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.003 (IC base=-0.069)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.306 (n=91)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3447` → IC=+0.314 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3447 (IC base=+0.304)

- **PATRÓN** `elapsed_s` > `187.1` → IC=+0.357 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 187.1 (IC base=+0.304)

- **PATRÓN** `drift_15min` |x|≤ `2.6528` → IC=+0.343 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.6528 (IC base=+0.304)

- **PATRÓN** `drift_60min` |x|≤ `0.9568` → IC=+0.371 (n=68)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9568 (IC base=+0.304)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.380 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.304)

- **PATRÓN** `ballena_activa_n` < `1067.0` → IC=+0.380 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1067.0 (IC base=+0.304)

- **PATRÓN** `drift_ventana_pct` |x|> `0.345` → IC=+0.260 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.345 (IC base=+0.236)

- **PATRÓN** `elapsed_s` < `203.6` → IC=+0.254 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 203.6 (IC base=+0.236)

- **PATRÓN** `drift_15min` |x|≤ `1.251` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.251 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.272 (n=55)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.236)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.306 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `1395.0` → IC=+0.325 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1395.0 (IC base=+0.236)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.306 (n=91)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3447` → IC=+0.314 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3447 (IC base=+0.304)

- **PATRÓN** `elapsed_s` > `187.1` → IC=+0.357 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 187.1 (IC base=+0.304)

- **PATRÓN** `drift_15min` |x|≤ `2.6528` → IC=+0.343 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.6528 (IC base=+0.304)

- **PATRÓN** `drift_60min` |x|≤ `0.9568` → IC=+0.371 (n=68)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9568 (IC base=+0.304)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.380 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.304)

- **PATRÓN** `ballena_activa_n` < `1067.0` → IC=+0.380 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1067.0 (IC base=+0.304)

- **PATRÓN** `drift_ventana_pct` |x|> `0.345` → IC=+0.260 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.345 (IC base=+0.236)

- **PATRÓN** `elapsed_s` < `203.6` → IC=+0.254 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 203.6 (IC base=+0.236)

- **PATRÓN** `drift_15min` |x|≤ `1.251` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.251 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.272 (n=55)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.236)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.306 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `1395.0` → IC=+0.325 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1395.0 (IC base=+0.236)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `libro_liquidez` > `2927.8455` → IC=+0.131 (n=497)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2927.8455 (IC base=+0.100)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2927.8455` → IC=+0.131 (n=497)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2927.8455 (IC base=+0.100)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=224)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=224)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=511)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `4006.09` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `liq_usd_total` < 4006.09
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=26)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=35)

- **PATRÓN** `liq_n` > `2.0` → IC=+0.132 (n=93)

  - _Acción_: Kelly boost +0.66€ cuando `liq_n` > 2.0 (IC base=+0.056)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.138 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 8.0 (IC base=+0.056)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=3812)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=117)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=104)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=117)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=22)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.127 (n=266)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=+0.024)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=1527)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=1481)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=722)

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
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=925)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=925)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=1062)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=1062)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=249)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=249)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.140 (n=73)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=191)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.190 (n=56)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=307)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=348)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=284)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=377)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=377)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=222)

- **FILTRO** `libro_liquidez` < `652.2458` → IC=-0.140 (n=134)

  - _Acción_: SKIP cuando `libro_liquidez` < 652.2458
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=273)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=306)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `restante_min` < `10.72` → IC=-0.145 (n=29)

  - _Acción_: SKIP cuando `restante_min` < 10.72
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=60)

- **FILTRO** `lag_apertura_s` > `255.1` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `lag_apertura_s` > 255.1
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=59)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.197 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=79)

- **FILTRO** `py_entrada` > `0.52` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `py_entrada` > 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=25)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.250 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=49)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.51` → IC=+0.148 (n=265)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.51 (IC base=+0.000)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` > `0.61` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=176)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.129 (n=141)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=565)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.137 (n=282)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=302)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.172 (n=126)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=527)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.146 (n=258)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=533)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.174 (n=6934)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=22383)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.177 (n=7334)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=22797)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.191 (n=1309)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=4082)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.177 (n=1244)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=4108)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.138 (n=1415)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 1.0 (IC base=+0.041)

- **PATRÓN** `libro_liquidez` > `1040.7991` → IC=+0.140 (n=2696)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 1040.7991 (IC base=+0.041)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.132 (n=2513)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.5 (IC base=+0.013)

- **PATRÓN** `libro_liquidez` > `1142.3414` → IC=+0.150 (n=1820)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1142.3414 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.206 (n=1316)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=4161)

- **PATRÓN** `ibs_20min` > `0.9643` → IC=+0.130 (n=1840)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.9643 (IC base=+0.036)

- **PATRÓN** `libro_liquidez` > `1738.62` → IC=+0.123 (n=1835)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 1738.62 (IC base=+0.036)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.154 (n=1343)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=4070)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2418)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=2342)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=3813)

- **FILTRO** `ballena_activa_n` > `33.0` → IC=-0.135 (n=1277)

  - _Acción_: SKIP cuando `ballena_activa_n` > 33.0
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=2524)

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

- **FILTRO** `libro_liquidez` < `3613.7014` → IC=-0.152 (n=110)

  - _Acción_: SKIP cuando `libro_liquidez` < 3613.7014
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=224)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.204 (n=113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=344)

- **FILTRO** `drift_20min_pct` |x|> `0.2038` → IC=-0.147 (n=114)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.2038
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=343)

- **FILTRO** `libro_liquidez` < `3186.5516` → IC=-0.184 (n=150)

  - _Acción_: SKIP cuando `libro_liquidez` < 3186.5516
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=307)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=954)

- **FILTRO** `libro_liquidez` < `1797.2058` → IC=-0.161 (n=243)

  - _Acción_: SKIP cuando `libro_liquidez` < 1797.2058
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=730)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.196 (n=366)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=741)

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

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.177 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 15.0 (IC base=+0.030)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.133 (n=20124)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=44894)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.297 (n=15298)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=49720)

- **FILTRO** `ibs_7min` < `0.2265` → IC=-0.232 (n=16254)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2265
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=48764)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.152 (n=21759)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=43259)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.244 (n=20239)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=61364)

- **FILTRO** `ibs_7min` > `0.2832` → IC=-0.182 (n=20400)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2832
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=61203)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.154 (n=2834)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=8632)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.318 (n=2788)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=8678)

- **FILTRO** `ibs_7min` < `0.7113` → IC=-0.249 (n=3783)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7113
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=7683)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.150 (n=2683)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=8783)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.277 (n=3367)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=10748)

- **FILTRO** `ibs_7min` > `0.7709` → IC=-0.215 (n=3528)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7709
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=10587)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.262 (n=2598)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=8295)

- **FILTRO** `ibs_7min` < `0.7179` → IC=-0.205 (n=2723)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7179
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=8170)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.194 (n=2715)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=8178)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.261 (n=2765)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=8337)

- **FILTRO** `ibs_7min` > `0.2661` → IC=-0.192 (n=2775)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2661
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=8327)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.180 (n=2761)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=8341)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.163 (n=2682)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=8288)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.323 (n=2586)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=8384)

- **FILTRO** `ibs_7min` < `0.2864` → IC=-0.247 (n=3619)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2864
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=7351)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.198 (n=2345)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=8625)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.259 (n=3558)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=11388)

- **FILTRO** `ibs_7min` > `0.7308` → IC=-0.183 (n=3736)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7308
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=11210)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=2565)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=7984)

- **FILTRO** `ibs_7min` < `0.7204` → IC=-0.194 (n=2637)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7204
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=7912)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.188 (n=2635)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=7914)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.258 (n=2519)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=8471)

- **FILTRO** `ibs_7min` > `0.2751` → IC=-0.174 (n=2745)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2751
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=8245)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.174 (n=2648)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=8342)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.295 (n=2426)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=8099)

- **FILTRO** `ibs_7min` < `0.7083` → IC=-0.227 (n=3451)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7083
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=7074)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.222 (n=2465)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=8060)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.193 (n=3757)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=11993)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.127 (n=3419)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=7196)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.299 (n=2653)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=7962)

- **FILTRO** `ibs_7min` < `0.1818` → IC=-0.231 (n=2649)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1818
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=7966)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.203 (n=2465)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=8150)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.228 (n=3653)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=11047)

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
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=594)

- **FILTRO** `libro_liquidez` < `10474.9398` → IC=-0.153 (n=188)

  - _Acción_: SKIP cuando `libro_liquidez` < 10474.9398
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=564)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=873)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.143 (n=166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=333)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=450)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.210 (n=184)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=564)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3985` → IC=+0.135 (n=1353)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.3985 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.130 (n=596)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 5.0 (IC base=+0.124)

- **PATRÓN** `total_vol_5m` < `422.987` → IC=+0.158 (n=451)

  - _Acción_: Kelly boost +0.79€ cuando `total_vol_5m` < 422.987 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `3556.2094` → IC=+0.145 (n=613)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3556.2094 (IC base=+0.124)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.175 (n=152)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 14.0 (IC base=+0.125)

- **PATRÓN** `total_vol_5m` < `372.075` → IC=+0.151 (n=279)

  - _Acción_: Kelly boost +0.76€ cuando `total_vol_5m` < 372.075 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2530.2591` → IC=+0.222 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2530.2591 (IC base=+0.125)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.4053` → IC=+0.124 (n=251)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.62€ cuando `delta_ratio` |x|> 0.4053 (IC base=+0.113)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.136 (n=248)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 14.0 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `2312.7298` → IC=+0.135 (n=187)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2312.7298 (IC base=+0.113)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4164` → IC=+0.193 (n=174)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.97€ cuando `delta_ratio` |x|> 0.4164 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.154 (n=273)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 4.0 (IC base=+0.136)

- **PATRÓN** `total_vol_5m` < `510.4612` → IC=+0.182 (n=174)

  - _Acción_: Kelly boost +0.91€ cuando `total_vol_5m` < 510.4612 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `5172.0718` → IC=+0.139 (n=261)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 5172.0718 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.214 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 59.0 (IC base=+0.136)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4322` → IC=+0.209 (n=108)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4322 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.196 (n=113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 6.0 (IC base=+0.147)

- **PATRÓN** `total_vol_5m` < `4680.799` → IC=+0.188 (n=158)

  - _Acción_: Kelly boost +0.94€ cuando `total_vol_5m` < 4680.799 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `3168.76` → IC=+0.168 (n=212)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 3168.76 (IC base=+0.147)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.125 (n=230)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 13.0 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=175)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.097)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.6638` → IC=-0.259 (n=52)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.6638
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=158)

- **FILTRO** `T_h` > `129.6188` → IC=-0.181 (n=189)

  - _Acción_: SKIP cuando `T_h` > 129.6188
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=570)

- **FILTRO** `pct_vs_K` |x|> `3.4276` → IC=-0.192 (n=258)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4276
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=501)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.177 (n=190)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0037 (IC base=-0.081)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `4.2538` → IC=-0.293 (n=56)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.2538
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=170)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.297 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=-0.035)

- **PATRÓN** `pct_vs_K` |x|≤ `1.617` → IC=+0.149 (n=75)

  - _Acción_: Kelly boost +0.75€ cuando `pct_vs_K` |x|≤ 1.617 (IC base=-0.035)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.01` → IC=-0.179 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.123 (n=51)

- **FILTRO** `pct_vs_K` |x|> `2.327` → IC=-0.195 (n=57)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.327
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `pct_vs_K` |x|> `2.96` → IC=-0.208 (n=70)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.96
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=72)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0105` → IC=-0.233 (n=522)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.116 (n=175)

- **FILTRO** `T_h` > `74.273` → IC=-0.220 (n=466)

  - _Acción_: SKIP cuando `T_h` > 74.273
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=231)

- **FILTRO** `sigma_h` < `0.005` → IC=-0.227 (n=148)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=445)

- **FILTRO** `pct_vs_K` |x|> `3.1913` → IC=-0.420 (n=148)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.1913
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=445)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0089` → IC=-0.211 (n=171)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0089
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=57)

- **FILTRO** `T_h` > `88.3739` → IC=-0.204 (n=113)

  - _Acción_: SKIP cuando `T_h` > 88.3739
  - _Potencial_: sin este filtro IC_bueno=-0.150 (n=115)

- **FILTRO** `pct_vs_K` |x|> `1.9209` → IC=-0.389 (n=106)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 1.9209
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=108)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `sigma_h` < `0.0085` → IC=-0.250 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.326 (n=130)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=67)

- **FILTRO** `T_h` > `102.0012` → IC=-0.290 (n=98)

  - _Acción_: SKIP cuando `T_h` > 102.0012
  - _Potencial_: sin este filtro IC_bueno=-0.243 (n=99)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.351 (n=45)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.114 (n=138)

- **FILTRO** `sigma_h` < `0.0052` → IC=-0.202 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0052
  - _Potencial_: sin este filtro IC_bueno=-0.164 (n=138)

- **FILTRO** `T_h` > `57.1769` → IC=-0.242 (n=122)

  - _Acción_: SKIP cuando `T_h` > 57.1769
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=61)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` < `0.0099` → IC=-0.184 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0099
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0082` → IC=-0.304 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0082
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=147)

- **FILTRO** `T_h` > `70.3179` → IC=-0.209 (n=146)

  - _Acción_: SKIP cuando `T_h` > 70.3179
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=50)

- **FILTRO** `sigma_h` < `0.0088` → IC=-0.278 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0088
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=88)

- **FILTRO** `pct_vs_K` |x|> `3.2111` → IC=-0.435 (n=44)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.2111
  - _Potencial_: sin este filtro IC_bueno=-0.129 (n=87)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1208` → IC=+0.469 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1208 (IC base=+0.343)

- **PATRÓN** `sigma_h` < `0.0147` → IC=+0.361 (n=106)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0147 (IC base=+0.343)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.377 (n=71)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.343)

- **PATRÓN** `T_h` < `0.3439` → IC=+0.395 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3439 (IC base=+0.343)

- **PATRÓN** `T_h` > `0.7258` → IC=+0.377 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7258 (IC base=+0.343)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.481 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.343)

- **PATRÓN** `edge` > `0.0997` → IC=+0.439 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.0997 (IC base=+0.409)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.433 (n=162)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.409)

- **PATRÓN** `T_h` < `0.6127` → IC=+0.441 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6127 (IC base=+0.409)

- **PATRÓN** `T_h` > `1.4832` → IC=+0.416 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4832 (IC base=+0.409)

- **PATRÓN** `dist_50` > `0.3767` → IC=+0.447 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3767 (IC base=+0.409)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.472 (n=142)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.409)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1444` → IC=+0.269 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1444 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.300 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0073 (IC base=+0.203)

- **PATRÓN** `T_h` < `0.659` → IC=+0.382 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.659 (IC base=+0.203)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.267 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.294 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.203)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1023` → IC=+0.462 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.412)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.414 (n=56)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0101 (IC base=+0.412)

- **PATRÓN** `T_h` < `1.2618` → IC=+0.431 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.2618 (IC base=+0.412)

- **PATRÓN** `dist_50` > `0.4077` → IC=+0.481 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4077 (IC base=+0.412)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.403 (n=29)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.412)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.444 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.412)

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

- **PATRÓN** `edge` > `0.1961` → IC=+0.470 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1961 (IC base=+0.462)

- **PATRÓN** `sigma_h` < `0.0162` → IC=+0.473 (n=147)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0162 (IC base=+0.462)

- **PATRÓN** `T_h` < `0.8279` → IC=+0.456 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.8279 (IC base=+0.462)

- **PATRÓN** `T_h` > `1.486` → IC=+0.481 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.486 (IC base=+0.462)

- **PATRÓN** `dist_50` > `0.4605` → IC=+0.492 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4605 (IC base=+0.462)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.467 (n=148)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.462)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=359)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=435)

- **PATRÓN** `streak_estiramiento` < `0.2936` → IC=+0.156 (n=91)

  - _Acción_: Kelly boost +0.78€ cuando `streak_estiramiento` < 0.2936 (IC base=+0.019)

- **PATRÓN** `streak_estiramiento` < `0.2597` → IC=+0.243 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.2597 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.132 (n=226)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 33.0 (IC base=+0.059)

- **PATRÓN** `libro_liquidez` > `2519.037` → IC=+0.139 (n=156)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2519.037 (IC base=+0.059)

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
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=22)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.495 (IC base=+0.038)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.133 (n=145)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 7.0 (IC base=+0.094)

- **PATRÓN** `streak_estiramiento` < `0.4354` → IC=+0.188 (n=123)

  - _Acción_: Kelly boost +0.94€ cuando `streak_estiramiento` < 0.4354 (IC base=+0.094)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.214 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `2225.9523` → IC=+0.136 (n=141)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2225.9523 (IC base=+0.094)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=99)

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

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=35)

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
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=19)

- **FILTRO** `volumen_racha` > `9229.0178` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `volumen_racha` > 9229.0178
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=18)

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
- **PATRÓN** `regimen_ma_toques` > `4.0` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.069)

- **PATRÓN** `volumen_racha` < `24607.606` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_racha` < 24607.606 (IC base=+0.069)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=1051)

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
- **FILTRO** `hora_utc` < `15.0` → IC=-0.167 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=26)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=36)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=4457)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.167 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=26)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=36)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=2546)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.191 (n=1916)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0057 (IC base=+0.163)

- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.171 (n=1449)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0128 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.21` → IC=+0.175 (n=4348)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.21 (IC base=+0.163)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3522` → IC=+0.172 (n=4001)

  - _Acción_: Kelly boost +0.86€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3522 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.169 (n=4581)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 4.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.164 (n=4014)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 15.0 (IC base=+0.163)

- **PATRÓN** `ibs_15` > `0.5144` → IC=+0.234 (n=4347)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5144 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.1304` → IC=+0.156 (n=2083)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1304 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` < `0.3163` → IC=+0.147 (n=3521)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.3163 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.758` → IC=+0.268 (n=837)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.758 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `5266.1649` → IC=+0.182 (n=1449)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 5266.1649 (IC base=+0.163)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=1728)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.246 (n=313)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.0591` → IC=+0.253 (n=237)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0591 (IC base=+0.205)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2648` → IC=+0.224 (n=237)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2648 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.224 (n=740)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.205)

- **PATRÓN** `ibs_15` > `0.7141` → IC=+0.280 (n=710)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7141 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.3743` → IC=+0.222 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3743 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.199` → IC=+0.311 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.199 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=919)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `8052.1794` → IC=+0.213 (n=710)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8052.1794 (IC base=+0.205)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.156 (n=868)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0068 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.151` → IC=+0.149 (n=764)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.151 (IC base=+0.136)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1432` → IC=+0.137 (n=579)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio_macro` |x|> 0.1432 (IC base=+0.136)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2833` → IC=+0.139 (n=698)

  - _Acción_: Kelly boost +0.69€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2833 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.144 (n=791)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 6.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.140 (n=911)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_15` > `0.5034` → IC=+0.228 (n=868)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5034 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.1197` → IC=+0.148 (n=543)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1197 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.4313` → IC=+0.137 (n=923)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.4313 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.066` → IC=+0.284 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.066 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `5798.0128` → IC=+0.169 (n=394)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 5798.0128 (IC base=+0.136)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.875` → IC=+0.220 (n=369)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.875 (IC base=+0.081)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=545)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.081)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0194` → IC=+0.192 (n=653)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0194 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.193 (n=875)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0151 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.207` → IC=+0.198 (n=979)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.207 (IC base=+0.186)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3496` → IC=+0.216 (n=878)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3496 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=894)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.195 (n=877)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 14.0 (IC base=+0.186)

- **PATRÓN** `ibs_15` > `0.5889` → IC=+0.286 (n=875)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5889 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` > `0.5089` → IC=+0.221 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5089 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.533` → IC=+0.237 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.533 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.189 (n=679)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.02 (IC base=+0.186)

- **PATRÓN** `libro_liquidez` > `2325.2328` → IC=+0.210 (n=979)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2325.2328 (IC base=+0.186)

- **PATRÓN** `ibs_15` < `0.1076` → IC=+0.171 (n=842)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.85€ cuando `ibs_15` < 0.1076 (IC base=+0.068)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.387 (n=317)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.366)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1505` → IC=+0.380 (n=465)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1505 (IC base=+0.366)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1379` → IC=+0.386 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1379 (IC base=+0.366)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.374 (n=742)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.366)

- **PATRÓN** `ibs_15` > `0.7881` → IC=+0.399 (n=699)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7881 (IC base=+0.366)

- **PATRÓN** `dist_vwap_pct` > `0.1523` → IC=+0.385 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1523 (IC base=+0.366)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.204` → IC=+0.397 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.204 (IC base=+0.366)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.370 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.366)

- **PATRÓN** `libro_liquidez` > `3489.2833` → IC=+0.373 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3489.2833 (IC base=+0.366)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.367 (n=118)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.362)

- **PATRÓN** `drift_15min` |x|≤ `0.5207` → IC=+0.361 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5207 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1565` → IC=+0.369 (n=234)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1565 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1436` → IC=+0.393 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1436 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.379 (n=328)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.8077` → IC=+0.387 (n=352)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8077 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.3743` → IC=+0.387 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3743 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.166` → IC=+0.386 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.166 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `8065.6565` → IC=+0.384 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8065.6565 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `489.0` → IC=+0.403 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 489.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.369 (n=348)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.368)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.384 (n=231)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.368)

- **PATRÓN** `drift_60min` |x|≤ `0.1074` → IC=+0.367 (n=232)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1074 (IC base=+0.368)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0833` → IC=+0.381 (n=310)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0833 (IC base=+0.368)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.383 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.368)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.383 (n=161)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.368)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.376 (n=159)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.368)

- **PATRÓN** `ibs_15` > `0.8138` → IC=+0.407 (n=310)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8138 (IC base=+0.368)

- **PATRÓN** `dist_vwap_pct` > `0.1227` → IC=+0.376 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1227 (IC base=+0.368)

- **PATRÓN** `dist_vwap_pct` < `0.2918` → IC=+0.372 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2918 (IC base=+0.368)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.408` → IC=+0.406 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.408 (IC base=+0.368)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.374 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.368)

- **PATRÓN** `libro_liquidez` > `4035.6016` → IC=+0.400 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4035.6016 (IC base=+0.368)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0099` → IC=-0.215 (n=1629)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0099
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=3163)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.216 (n=1913)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=2879)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1392` → IC=+0.220 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1392 (IC base=-0.073)

- **PATRÓN** `ibs_15` > `0.6326` → IC=+0.280 (n=1132)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6326 (IC base=-0.073)

- **PATRÓN** `dist_vwap_pct` > `0.1122` → IC=+0.203 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1122 (IC base=-0.073)

- **PATRÓN** `dist_vwap_pct` < `0.4235` → IC=+0.200 (n=1113)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4235 (IC base=-0.073)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2336` → IC=+0.268 (n=1416)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2336 (IC base=-0.009)

- **PATRÓN** `ibs_15` < `0.3673` → IC=+0.282 (n=4249)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3673 (IC base=-0.009)

- **PATRÓN** `dist_vwap_pct` > `0.6491` → IC=+0.273 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6491 (IC base=-0.009)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0327` → IC=-0.224 (n=2263)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0327
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=756)

- **FILTRO** `sigma_h` < `0.0036` → IC=-0.221 (n=754)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0036
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=2265)

- **FILTRO** `sigma_ewma_delta_pct` > `18.991` → IC=-0.261 (n=550)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.991
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=2469)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.157 (n=292)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0029 (IC base=+0.079)

- **PATRÓN** `ibs_15` > `0.7639` → IC=+0.329 (n=384)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7639 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` > `0.1051` → IC=+0.282 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1051 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` < `0.3658` → IC=+0.285 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3658 (IC base=+0.079)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.034` → IC=+0.148 (n=200)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 23.034 (IC base=+0.079)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0674` → IC=+0.246 (n=69)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0674 (IC base=-0.188)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1389` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1389 (IC base=-0.188)

- **PATRÓN** `ibs_15` < `0.6221` → IC=+0.319 (n=70)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6221 (IC base=-0.188)

- **PATRÓN** `dist_vwap_pct` < `0.0459` → IC=+0.310 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0459 (IC base=-0.188)

- **PATRÓN** `ballena_activa_n` < `288.0` → IC=+0.375 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 288.0 (IC base=-0.188)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.157 (n=736)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.161 (n=497)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0058 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.0722` → IC=+0.185 (n=249)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.0722 (IC base=+0.150)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2951` → IC=+0.193 (n=437)

  - _Acción_: Kelly boost +0.96€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2951 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.168 (n=408)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 11.0 (IC base=+0.150)

- **PATRÓN** `ibs_15` > `0.5867` → IC=+0.244 (n=565)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5867 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.4658` → IC=+0.158 (n=147)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.4658 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.1604` → IC=+0.156 (n=440)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1604 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.049` → IC=+0.259 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.049 (IC base=+0.150)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=736)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `5125.6863` → IC=+0.154 (n=377)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 5125.6863 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.262 (n=540)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.1029` → IC=+0.244 (n=542)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1029 (IC base=+0.241)

- **PATRÓN** `drift_15min` |x|≤ `0.7706` → IC=+0.257 (n=1424)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7706 (IC base=+0.241)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1554` → IC=+0.260 (n=1079)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1554 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.245 (n=599)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.247 (n=610)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.241)

- **PATRÓN** `ibs_15` < `0.3774` → IC=+0.274 (n=1618)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3774 (IC base=+0.241)

- **PATRÓN** `dist_vwap_pct` > `0.6017` → IC=+0.272 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6017 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.327` → IC=+0.246 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.327 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.254` → IC=+0.248 (n=1688)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.254 (IC base=+0.241)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0476` → IC=-0.209 (n=824)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0476
  - _Potencial_: sin este filtro IC_bueno=-0.124 (n=275)

- **FILTRO** `drift_60min` |x|> `0.172` → IC=-0.244 (n=373)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.172
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=726)

- **FILTRO** `drift_15min` |x|> `0.8935` → IC=-0.275 (n=274)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8935
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=825)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.189)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.189)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1292 (IC base=-0.189)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=-0.189)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0653` → IC=+0.223 (n=726)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0653 (IC base=-0.034)

- **PATRÓN** `ibs_15` < `0.3939` → IC=+0.293 (n=727)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3939 (IC base=-0.034)

- **PATRÓN** `dist_vwap_pct` < `0.4441` → IC=+0.233 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4441 (IC base=-0.034)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.057` → IC=-0.230 (n=985)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.057
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=329)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.248 (n=606)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=708)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.212)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.212)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0516` → IC=+0.272 (n=955)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0516 (IC base=-0.024)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1174` → IC=+0.291 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1174 (IC base=-0.024)

- **PATRÓN** `ibs_15` < `0.1351` → IC=+0.309 (n=636)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1351 (IC base=-0.024)

- **PATRÓN** `dist_vwap_pct` > `0.7727` → IC=+0.339 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7727 (IC base=-0.024)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.177 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0049 (IC base=+0.093)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.177 (n=29)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.093)

- **PATRÓN** `drift_15min` |x|≤ `0.3696` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3696 (IC base=+0.093)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.093)

- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.364 (n=20)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` < `0.0951` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0951 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.1943` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.1943 (IC base=+0.053)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.177 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0049 (IC base=+0.093)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.177 (n=29)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.093)

- **PATRÓN** `drift_15min` |x|≤ `0.3696` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3696 (IC base=+0.093)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.093)

- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.364 (n=20)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` < `0.0951` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0951 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.1943` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.1943 (IC base=+0.053)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.292 (n=1227)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.0542` → IC=+0.320 (n=409)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0542 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1511` → IC=+0.289 (n=817)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1511 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2235` → IC=+0.299 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2235 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.303 (n=1271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.8393` → IC=+0.317 (n=1227)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8393 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.2676` → IC=+0.317 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2676 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.379` → IC=+0.387 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.379 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `13582.8192` → IC=+0.308 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13582.8192 (IC base=+0.287)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.309 (n=218)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.281)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.299 (n=296)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.0592` → IC=+0.318 (n=218)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0592 (IC base=+0.281)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2673` → IC=+0.283 (n=219)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2673 (IC base=+0.281)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3906` → IC=+0.287 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3906 (IC base=+0.281)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.300 (n=683)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.281)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.306 (n=653)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.829 (IC base=+0.281)

- **PATRÓN** `dist_vwap_pct` > `0.2522` → IC=+0.314 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2522 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.55` → IC=+0.379 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.55 (IC base=+0.281)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.281 (n=843)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `16041.7902` → IC=+0.318 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16041.7902 (IC base=+0.281)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.309 (n=574)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.1075` → IC=+0.316 (n=383)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1075 (IC base=+0.294)

- **PATRÓN** `delta_ratio_macro` |x|> `0.145` → IC=+0.297 (n=383)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.145 (IC base=+0.294)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1009` → IC=+0.344 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1009 (IC base=+0.294)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.310 (n=551)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.294)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.298 (n=524)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.294)

- **PATRÓN** `ibs_15` > `0.8743` → IC=+0.330 (n=514)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8743 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` > `0.2815` → IC=+0.319 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2815 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.513` → IC=+0.385 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.513 (IC base=+0.294)

### UPDOWN_OU_5M
- **FILTRO** `delta_ratio_macro` |x|≤ `0.126` → IC=-0.159 (n=89)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.126
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=269)

- **FILTRO** `ballena_activa_n` > `35.0` → IC=-0.126 (n=244)

  - _Acción_: SKIP cuando `ballena_activa_n` > 35.0
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=82)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.157` → IC=-0.138 (n=67)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.157
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=137)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1149` → IC=-0.206 (n=15)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1149
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=46)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2685` → IC=-0.370 (n=21)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2685
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=12)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `drift_60min` |x|> `0.2455` → IC=-0.184 (n=17)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2455
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=35)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.250 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=39)

- **FILTRO** `drift_15min` |x|> `0.2309` → IC=-0.225 (n=38)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2309
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=19)

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
- **PATRÓN** `ratio` < `0.9726` → IC=+0.397 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9726 (IC base=+0.177)

- **PATRÓN** `T_h` > `115.8544` → IC=+0.354 (n=2510)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 115.8544 (IC base=+0.336)

- **PATRÓN** `ratio` > `1.0211` → IC=+0.379 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0211 (IC base=+0.336)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `111.9836` → IC=+0.154 (n=232)

  - _Acción_: Kelly boost +0.77€ cuando `T_h` > 111.9836 (IC base=+0.144)

- **PATRÓN** `ratio` < `0.9811` → IC=+0.324 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9811 (IC base=+0.144)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.312 (n=887)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.298)

- **PATRÓN** `ratio` > `1.0422` → IC=+0.417 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0422 (IC base=+0.298)

### WEEKLY_PRICE#ETH
- **PATRÓN** `ratio` < `0.9854` → IC=+0.392 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.218)

- **PATRÓN** `T_h` > `111.996` → IC=+0.353 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.996 (IC base=+0.323)

- **PATRÓN** `ratio` > `1.0298` → IC=+0.395 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0298 (IC base=+0.323)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0624` → IC=+0.435 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0624 (IC base=+0.398)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5144 sube el IC de +0.163 a +0.234 en UPDOWN_GBM#15min (n=4347). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7141 sube el IC de +0.205 a +0.280 en UPDOWN_GBM#BTC#15min (n=710). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5034 sube el IC de +0.136 a +0.228 en UPDOWN_GBM#ETH#15min (n=868). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.875 sube el IC de +0.081 a +0.220 en UPDOWN_GBM#SOL#15min (n=369). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5889 sube el IC de +0.186 a +0.286 en UPDOWN_GBM#XRP#15min (n=875). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1076 sube el IC de +0.068 a +0.171 en UPDOWN_GBM#XRP#15min (n=842). Ya aplicado como kelly_boost=+0.85€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6326 sube el IC de -0.073 a +0.280 en UPDOWN_GBM_15M_TARDIO (n=1132). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3673 sube el IC de -0.009 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=4249). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7639 sube el IC de +0.079 a +0.329 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=384). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6221 sube el IC de -0.188 a +0.319 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=70). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5867 sube el IC de +0.150 a +0.244 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=565). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3774 sube el IC de +0.241 a +0.274 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1618). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.189 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3939 sube el IC de -0.034 a +0.293 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=727). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.212 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.1351 sube el IC de -0.024 a +0.309 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=636). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.093 a +0.364 en UPDOWN_GBM_ETH_15M_HORA7 (n=20). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.093 a +0.364 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=20). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8393 sube el IC de +0.287 a +0.317 en UPDOWN_GBM_IBS_ALTO (n=1227). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.281 a +0.306 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=653). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8743 sube el IC de +0.294 a +0.330 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=514). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7881 sube el IC de +0.366 a +0.399 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=699). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8077 sube el IC de +0.362 a +0.387 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=352). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.8138 sube el IC de +0.368 a +0.407 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=310). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2089 | +0.086 | +222.68€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2089 | +0.086 | +222.68€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1689 | +0.087 | +185.12€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1689 | +0.087 | +185.12€ | 0 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 284 | +0.070 | +11.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 284 | +0.070 | +11.30€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 85 | +0.132 | +26.59€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 85 | +0.132 | +26.59€ | 1 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 935 | -0.025 | +77.01€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 935 | -0.025 | +77.01€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 718 | -0.046 | +55.15€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 718 | -0.046 | +55.15€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 150 | +0.086 | +25.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 150 | +0.086 | +25.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 61 | -0.056 | -5.61€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 61 | -0.056 | -5.61€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 44267 | -0.085 | -5583.40€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2623 | +0.058 | -282.78€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 41644 | -0.094 | -5300.62€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4647 | -0.116 | -760.21€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4647 | -0.116 | -760.21€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2623 | +0.058 | -282.78€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2623 | +0.058 | -282.78€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4600 | -0.116 | -895.63€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4600 | -0.116 | -895.63€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 11897 | -0.027 | -1068.16€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 11897 | -0.027 | -1068.16€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 11997 | -0.120 | -1206.90€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 11997 | -0.120 | -1206.90€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8503 | -0.126 | -1369.72€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8503 | -0.126 | -1369.72€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 42833 | -0.013 | +3207.48€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 11045 | +0.005 | +1608.27€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 31788 | -0.019 | +1599.20€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 42833 | -0.013 | +3207.48€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 11045 | +0.005 | +1608.27€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 31788 | -0.019 | +1599.20€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 169042 | +0.114 | -6870.73€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 20545 | +0.180 | -683.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 764 | -0.004 | -78.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 137875 | +0.106 | -5758.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 9858 | +0.093 | -351.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 22845 | +0.106 | -1456.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 68 | -0.186 | +4.73€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 22762 | +0.107 | -1449.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 32361 | +0.125 | -533.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5516 | +0.180 | -229.68€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 22833 | +0.120 | -152.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3970 | +0.078 | -129.49€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 22898 | +0.099 | -1631.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 82 | -0.119 | -3.25€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 22801 | +0.100 | -1616.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 36038 | +0.124 | -724.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 9199 | +0.177 | -205.47€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 23180 | +0.106 | -455.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3647 | +0.101 | -54.78€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 32027 | +0.112 | -1514.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5601 | +0.198 | -255.41€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 667 | +0.025 | -24.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 23518 | +0.095 | -1067.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2241 | +0.105 | -166.86€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#XRP | 22873 | +0.107 | -1010.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 79 | -0.117 | +5.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 22781 | +0.108 | -1016.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 27312 | +0.195 | -1774.33€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 27312 | +0.195 | -1774.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 6169 | +0.176 | -560.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 6169 | +0.176 | -560.64€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 3751 | +0.201 | -112.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 3751 | +0.201 | -112.26€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 6105 | +0.176 | -524.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 6105 | +0.176 | -524.92€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5200 | +0.249 | -187.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5200 | +0.249 | -187.63€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 6008 | +0.186 | -402.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 6008 | +0.186 | -402.64€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1152 | +0.425 | -42.56€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1152 | +0.425 | -42.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 467 | +0.438 | -5.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 467 | +0.438 | -5.09€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 462 | +0.427 | -14.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 462 | +0.427 | -14.73€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 209 | +0.396 | -18.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 209 | +0.396 | -18.87€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 95993 | +0.201 | -6904.99€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 95993 | +0.201 | -6904.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 16540 | +0.182 | -1783.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 16540 | +0.182 | -1783.89€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 15485 | +0.225 | -497.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 15485 | +0.225 | -497.56€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 16469 | +0.181 | -1722.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 16469 | +0.181 | -1722.84€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 15608 | +0.219 | -614.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 15608 | +0.219 | -614.75€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 15899 | +0.202 | -1027.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 15899 | +0.202 | -1027.92€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 15992 | +0.198 | -1258.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 15992 | +0.198 | -1258.03€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 36837 | +0.117 | +306.24€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 36837 | +0.117 | +306.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 18333 | +0.118 | +195.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 18333 | +0.118 | +195.97€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 18504 | +0.116 | +110.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 18504 | +0.116 | +110.27€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2351 | +0.295 | +6.25€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2351 | +0.295 | +6.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1074 | +0.283 | -16.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1074 | +0.283 | -16.94€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1146 | +0.300 | +21.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1146 | +0.300 | +21.22€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 131 | +0.335 | +1.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 131 | +0.335 | +1.96€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1077 | +0.444 | +10.67€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1077 | +0.444 | +10.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 520 | +0.439 | -2.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 520 | +0.439 | -2.17€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 509 | +0.451 | +11.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 509 | +0.451 | +11.97€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 48 | +0.400 | +0.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 48 | +0.400 | +0.86€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1839 | +0.068 | -79.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1114 | +0.082 | -15.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1405 | +0.076 | -34.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1114 | +0.082 | -15.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 73970 | +0.101 | -1788.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 5953 | +0.094 | +97.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 68017 | +0.101 | -1885.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 40515 | +0.106 | -407.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 5953 | +0.094 | +97.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 34562 | +0.108 | -504.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 15520 | +0.109 | -80.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 15520 | +0.109 | -80.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 17935 | +0.082 | -1300.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 17935 | +0.082 | -1300.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 911 | +0.187 | -109.28€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 911 | +0.187 | -109.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 911 | +0.187 | -109.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 911 | +0.187 | -109.28€ | 1 | 4 |
| ✅ GBM_LATE_15M | 50373 | +0.097 | +27509.26€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 50373 | +0.097 | +27509.26€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 8377 | +0.222 | +7106.86€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 8377 | +0.222 | +7106.86€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 7680 | +0.175 | +5960.77€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 7680 | +0.175 | +5960.77€ | 0 | 25 |
| ✅ GBM_LATE_15M#DOGE | 9035 | +0.205 | +7029.62€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 9035 | +0.205 | +7029.62€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 6880 | +0.048 | +2044.47€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 6880 | +0.048 | +2044.47€ | 1 | 18 |
| ✅ GBM_LATE_15M#SOL | 7042 | -0.032 | +1804.98€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 7042 | -0.032 | +1804.98€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 11359 | -0.026 | +3562.56€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 11359 | -0.026 | +3562.56€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 53339 | +0.085 | +30240.24€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 53339 | +0.085 | +30240.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 10379 | -0.000 | +5355.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 10379 | -0.000 | +5355.30€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 11412 | +0.006 | +2929.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 11412 | +0.006 | +2929.41€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 7310 | +0.287 | +8121.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 7310 | +0.287 | +8121.24€ | 0 | 23 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 9950 | +0.014 | +2977.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 9950 | +0.014 | +2977.00€ | 1 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 8296 | +0.041 | +3604.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 8296 | +0.041 | +3604.73€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5992 | +0.312 | +7252.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5992 | +0.312 | +7252.57€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 39964 | +0.179 | +32767.57€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 39964 | +0.179 | +32767.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 6029 | +0.237 | +5546.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 6029 | +0.237 | +5546.19€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 6333 | +0.142 | +4696.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 6333 | +0.142 | +4696.04€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 6413 | +0.224 | +5539.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 6413 | +0.224 | +5539.77€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 6823 | +0.132 | +5266.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 6823 | +0.132 | +5266.20€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 7536 | +0.121 | +5603.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 7536 | +0.121 | +5603.14€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 6830 | +0.231 | +6116.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 6830 | +0.231 | +6116.23€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 10557 | +0.124 | +5125.99€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 10557 | +0.124 | +5125.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 457 | +0.158 | +289.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 457 | +0.158 | +289.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3045 | +0.129 | +1644.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3045 | +0.129 | +1644.08€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 491 | +0.153 | +259.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 491 | +0.153 | +259.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3145 | +0.129 | +1525.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3145 | +0.129 | +1525.77€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2666 | +0.093 | +1007.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2666 | +0.093 | +1007.53€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 753 | +0.149 | +399.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 753 | +0.149 | +399.23€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 50623 | +0.185 | +41115.81€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 50623 | +0.185 | +41115.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 7997 | +0.247 | +7639.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 7997 | +0.247 | +7639.57€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 8002 | +0.139 | +5510.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 8002 | +0.139 | +5510.67€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 8577 | +0.233 | +7661.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 8577 | +0.233 | +7661.57€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 8377 | +0.139 | +6071.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 8377 | +0.139 | +6071.23€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 8975 | +0.120 | +6294.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 8975 | +0.120 | +6294.80€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 8695 | +0.237 | +7937.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 8695 | +0.237 | +7937.98€ | 0 | 21 |
| ✅ GBM_LATE_5M | 13339 | +0.208 | +10722.65€ | 1 | 30 |
| ✅ GBM_LATE_5M#5min | 13339 | +0.208 | +10722.65€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3192 | +0.211 | +2758.98€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3192 | +0.211 | +2758.98€ | 0 | 26 |
| ✅ GBM_LATE_5M#DOGE | 1222 | +0.198 | +913.92€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1222 | +0.198 | +913.92€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 3883 | +0.201 | +2889.05€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3883 | +0.201 | +2889.05€ | 0 | 24 |
| ✅ GBM_LATE_5M#SOL | 2032 | +0.201 | +1625.18€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2032 | +0.201 | +1625.18€ | 0 | 26 |
| ✅ GBM_LATE_5M#XRP | 1956 | +0.209 | +1535.25€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1956 | +0.209 | +1535.25€ | 0 | 0 |
| ✅ GBM_LATE_60M | 4364 | +0.052 | +1222.18€ | 0 | 6 |
| ✅ GBM_LATE_60M#60min | 4364 | +0.052 | +1222.18€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1552 | +0.068 | +512.98€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1552 | +0.068 | +512.98€ | 1 | 5 |
| ✅ GBM_LATE_60M#ETH | 1415 | +0.051 | +433.72€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1415 | +0.051 | +433.72€ | 1 | 6 |
| ✅ GBM_LATE_60M#SOL | 1397 | +0.035 | +275.48€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1397 | +0.035 | +275.48€ | 0 | 8 |
| 🚫 GBM_LATE_60M_FADE | 649 | -0.250 | -31.65€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 649 | -0.250 | -31.65€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 243 | -0.247 | -17.39€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 243 | -0.247 | -17.39€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 234 | -0.246 | -6.56€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 234 | -0.246 | -6.56€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 172 | -0.253 | -7.69€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 172 | -0.253 | -7.69€ | 6 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1779 | +0.079 | +441.08€ | 0 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1779 | +0.079 | +441.08€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 690 | +0.068 | +148.78€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 690 | +0.068 | +148.78€ | 1 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 606 | +0.056 | +107.50€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 606 | +0.056 | +107.50€ | 2 | 15 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 483 | +0.125 | +184.80€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 483 | +0.125 | +184.80€ | 1 | 10 |
| ✅ LATE_WINDOW_5MIN | 198 | +0.270 | +203.69€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 198 | +0.270 | +203.69€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 198 | +0.270 | +203.69€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 198 | +0.270 | +203.69€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4023 | +0.098 | +937.16€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4023 | +0.098 | +937.16€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4023 | +0.098 | +937.16€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4023 | +0.098 | +937.16€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 772 | -0.013 | +7.54€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 772 | -0.013 | +7.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 7 | -0.058 | -1.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 7 | -0.058 | -1.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 235 | +0.002 | +8.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 235 | +0.002 | +8.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 27 | -0.155 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 27 | -0.155 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 201 | +0.027 | +12.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 201 | +0.027 | +12.96€ | 2 | 2 |
| ✅ LIQUIDACIONES_15M#SOL | 250 | -0.004 | +2.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 250 | -0.004 | +2.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4035 | +0.018 | +106.75€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 4035 | +0.018 | +106.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 189 | +0.034 | +0.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 189 | +0.034 | +0.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 818 | +0.016 | +41.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 818 | +0.016 | +41.53€ | 1 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 216 | +0.000 | +1.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 216 | +0.000 | +1.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1579 | +0.022 | +32.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1579 | +0.022 | +32.03€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 763 | +0.011 | +1.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 763 | +0.011 | +1.66€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 470 | +0.015 | +29.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 470 | +0.015 | +29.46€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2082 | -0.039 | -27.61€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2082 | -0.039 | -27.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 627 | -0.034 | -14.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 627 | -0.034 | -14.80€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 727 | -0.016 | +9.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 727 | -0.016 | +9.06€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 728 | -0.067 | -21.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 728 | -0.067 | -21.87€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 12278 | -0.031 | -79.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 5880 | -0.035 | -81.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 6398 | -0.027 | +1.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 428 | -0.046 | -18.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 214 | -0.018 | +3.26€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 214 | -0.074 | -22.13€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 3179 | -0.021 | +24.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1511 | -0.023 | +9.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1668 | -0.020 | +15.55€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1269 | -0.023 | +27.48€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 646 | -0.032 | +2.11€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 623 | -0.014 | +25.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 2732 | -0.037 | -64.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1290 | -0.041 | -44.15€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1442 | -0.033 | -20.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 2368 | -0.030 | -12.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1143 | -0.038 | -24.09€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1225 | -0.023 | +11.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 2302 | -0.039 | -36.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1076 | -0.045 | -28.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1226 | -0.033 | -8.54€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 59448 | -0.000 | +3091.73€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 59448 | -0.000 | +3091.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 10743 | +0.027 | +1412.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 10743 | +0.027 | +1412.91€ | 2 | 4 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 8420 | -0.036 | -121.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 8420 | -0.036 | -121.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 10874 | +0.025 | +1142.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 10874 | +0.025 | +1142.80€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 8315 | -0.049 | -175.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 8315 | -0.049 | -175.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 10091 | -0.004 | +274.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 10091 | -0.004 | +274.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 11005 | +0.017 | +558.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 11005 | +0.017 | +558.46€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6949 | -0.056 | -133.02€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6949 | -0.056 | -133.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1237 | -0.002 | -17.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1237 | -0.002 | -17.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1907 | -0.069 | -33.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1907 | -0.069 | -33.89€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 67 | -0.007 | +0.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 67 | -0.007 | +0.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 791 | -0.119 | -33.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 791 | -0.119 | -33.96€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2089 | -0.069 | -22.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2089 | -0.069 | -22.50€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 858 | -0.016 | -26.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 858 | -0.016 | -26.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M | 3373 | +0.004 | -0.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3373 | +0.004 | -0.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 132 | -0.037 | -1.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 132 | -0.037 | -1.23€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 194 | +0.010 | -0.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 194 | +0.010 | -0.77€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1326 | +0.006 | +6.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1326 | +0.006 | +6.37€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1391 | +0.007 | -0.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1391 | +0.007 | -0.19€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 191 | -0.008 | -2.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 191 | -0.008 | -2.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 146621 | -0.077 | +1944.83€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 146621 | -0.077 | +1944.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 25581 | -0.078 | +1380.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 25581 | -0.078 | +1380.41€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 21995 | -0.100 | -1054.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 21995 | -0.100 | -1054.96€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 25916 | -0.069 | +1238.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 25916 | -0.069 | +1238.89€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 21539 | -0.097 | -641.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 21539 | -0.097 | -641.40€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 26275 | -0.057 | +326.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 26275 | -0.057 | +326.75€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 25315 | -0.069 | +695.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 25315 | -0.069 | +695.14€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8946 | -0.035 | -183.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8946 | -0.035 | -183.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1002 | -0.017 | -19.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1002 | -0.017 | -19.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2060 | -0.047 | -27.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2060 | -0.047 | -27.56€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2624 | -0.026 | -39.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2624 | -0.026 | -39.96€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1248 | -0.062 | -32.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1248 | -0.062 | -32.71€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1003 | -0.030 | -32.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1003 | -0.030 | -32.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 1938 | +0.119 | +765.31€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1802 | +0.124 | +752.71€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 422 | +0.125 | +191.29€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 422 | +0.125 | +191.29€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 373 | +0.113 | +125.38€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 373 | +0.113 | +125.38€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#ETH | 347 | +0.136 | +170.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 347 | +0.136 | +170.50€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 315 | +0.147 | +168.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 315 | +0.147 | +168.22€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 345 | +0.097 | +97.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 345 | +0.097 | +97.33€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1821 | -0.018 | -30.63€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1821 | -0.018 | -30.63€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 342 | +0.003 | +12.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 342 | +0.003 | +12.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 328 | -0.039 | -15.60€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 328 | -0.039 | -15.60€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 471 | -0.043 | -35.46€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 471 | -0.043 | -35.46€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 376 | +0.005 | +4.32€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 376 | +0.005 | +4.32€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 304 | -0.010 | +3.39€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 304 | -0.010 | +3.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1036 | -0.077 | -50.59€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 477 | -0.110 | -78.82€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 371 | -0.130 | -62.70€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 106 | -0.037 | -16.12€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 365 | -0.037 | +22.38€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 260 | -0.023 | +28.35€ | 1 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 105 | -0.070 | -5.97€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 194 | -0.071 | +5.85€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 160 | -0.074 | +3.00€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 34 | -0.056 | +2.86€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 791 | -0.084 | -31.36€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 245 | -0.055 | -19.23€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1290 | -0.210 | -85.24€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 503 | -0.211 | -49.89€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 442 | -0.212 | -47.62€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 61 | -0.198 | -2.27€ | 1 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 434 | -0.216 | -39.45€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 380 | -0.225 | -45.44€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 54 | -0.143 | +5.99€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 353 | -0.199 | +4.10€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 327 | -0.196 | +1.20€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 26 | -0.214 | +2.91€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1149 | -0.212 | -91.87€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 141 | -0.185 | +6.63€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 499 | +0.390 | +470.65€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#BTC | 84 | +0.174 | +61.71€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 84 | +0.174 | +61.71€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#ETH | 116 | +0.364 | +102.68€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 116 | +0.364 | +102.68€ | 0 | 6 |
| ✅ RESOLUTION_SNIPER#SOL | 299 | +0.457 | +306.27€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 299 | +0.457 | +306.27€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 499 | +0.390 | +470.65€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 832 | +0.041 | +71.67€ | 2 | 4 |
| ✅ STREAK_FADE_15M#15min | 832 | +0.041 | +71.67€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 310 | +0.026 | +5.92€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 310 | +0.026 | +5.92€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 69 | +0.007 | +1.00€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 69 | +0.007 | +1.00€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 82 | +0.024 | +7.24€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 82 | +0.024 | +7.24€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 371 | +0.063 | +57.51€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 371 | +0.063 | +57.51€ | 0 | 4 |
| ✅ STREAK_FADE_5M | 3538 | -0.023 | -142.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3538 | -0.023 | -142.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 601 | -0.029 | -27.44€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 601 | -0.029 | -27.44€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 169 | -0.038 | -13.78€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 169 | -0.038 | -13.78€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1641 | -0.020 | -60.99€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1641 | -0.020 | -60.99€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 110 | -0.036 | -7.34€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 110 | -0.036 | -7.34€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 43 | -0.100 | -5.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 43 | -0.100 | -5.07€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 67 | +0.007 | -2.27€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 67 | +0.007 | -2.27€ | 0 | 2 |
| ✅ STREAK_MOM_5M | 11394 | +0.015 | +77.84€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11394 | +0.015 | +77.84€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2946 | +0.018 | +25.04€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2946 | +0.018 | +25.04€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2959 | +0.018 | +37.45€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2959 | +0.018 | +37.45€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2910 | +0.009 | -1.79€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2910 | +0.009 | -1.79€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2579 | +0.013 | +17.14€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2579 | +0.013 | +17.14€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 10686 | +0.014 | -46.48€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 10686 | +0.014 | -46.48€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4476 | +0.019 | -5.34€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4476 | +0.019 | -5.34€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3630 | +0.010 | -28.88€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3630 | +0.010 | -28.88€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2580 | +0.011 | -12.26€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2580 | +0.011 | -12.26€ | 1 | 0 |
| ✅ UPDOWN_GBM | 90996 | +0.058 | +8519.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 22087 | +0.084 | +4817.95€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2857 | +0.002 | +31.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 60326 | +0.057 | +3571.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 5407 | +0.003 | +102.62€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 7478 | +0.099 | +1307.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1682 | +0.166 | +787.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5706 | +0.081 | +521.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 20860 | +0.057 | +1816.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3021 | +0.083 | +688.11€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 796 | +0.004 | +14.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 14489 | +0.065 | +1041.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2439 | +0.001 | +69.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 115 | -0.073 | +2.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 9719 | +0.075 | +1100.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1662 | +0.154 | +693.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 7971 | +0.059 | +407.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 21651 | +0.048 | +1480.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 5356 | +0.072 | +810.55€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 763 | +0.007 | +18.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 13440 | +0.049 | +621.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1985 | +0.006 | +26.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 107 | -0.105 | +1.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 19600 | +0.038 | +1124.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 5697 | +0.037 | +470.82€ | 0 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 725 | -0.010 | +2.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 12100 | +0.045 | +651.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 983 | +0.003 | +6.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 95 | -0.139 | -6.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 11686 | +0.070 | +1692.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4669 | +0.101 | +1366.96€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 6620 | +0.053 | +327.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 317 | -0.105 | -1.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 931 | +0.366 | +343.62€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 931 | +0.366 | +343.62€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 469 | +0.362 | +164.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 469 | +0.362 | +164.30€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 462 | +0.368 | +179.31€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 462 | +0.368 | +179.31€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 22350 | -0.022 | +5399.65€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 22350 | -0.022 | +5399.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1866 | -0.054 | +526.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1866 | -0.054 | +526.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 4186 | -0.114 | +208.28€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 4186 | -0.114 | +208.28€ | 3 | 10 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1010 | +0.220 | +840.22€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1010 | +0.220 | +840.22€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2910 | +0.218 | +1849.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2910 | +0.218 | +1849.33€ | 1 | 20 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 6329 | -0.061 | +881.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 6329 | -0.061 | +881.82€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 6049 | -0.065 | +1093.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 6049 | -0.065 | +1093.95€ | 2 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 270 | +0.062 | +25.25€ | 0 | 7 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 270 | +0.062 | +25.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 270 | +0.062 | +25.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 270 | +0.062 | +25.25€ | 0 | 7 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1635 | +0.287 | +1378.12€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1635 | +0.287 | +1378.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 870 | +0.281 | +685.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 870 | +0.281 | +685.64€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 765 | +0.294 | +692.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 765 | +0.294 | +692.48€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 845 | -0.114 | -84.20€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 845 | -0.114 | -84.20€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 259 | -0.086 | -20.70€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 259 | -0.086 | -20.70€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 94 | -0.167 | -10.43€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 94 | -0.167 | -10.43€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 109 | -0.176 | -3.72€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 109 | -0.176 | -3.72€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 4147 | +0.302 | +1918.86€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 1552 | +0.258 | +190.79€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1593 | +0.295 | +688.71€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1002 | +0.381 | +1039.37€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.025 n=1126 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1126 IC=+0.025 PNL=+58.51€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 766 celda(s) pasan gate riguroso completo de 2804 evaluadas (n>=40) y 3898 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.037 < 0.08 — monitorear
  - _Datos_: n=5689 IC=+0.037 PNL=+472.30€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1593/15 IC=+0.295 PNL=+688.71€ | BTC: n=1552/15 IC=+0.258 PNL=+190.79€ | SOL: n=1002/15 IC=+0.381 PNL=+1039.37€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.147 n=970/60 | contraria IC=+0.192 n=997 | gap=-0.045 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=537, boost estimado=+0.017. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1983/40 IC=+0.006 PNL=+26.90€ | BTC#60min: n=2438/40 IC=+0.000 PNL=+68.88€ | SOL#60min: n=981/40 IC=+0.003 PNL=+6.34€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.046 n=650260 | tras_1loss IC=+0.098 n=493676 | tras_2loss IC=+0.067 n=198651/40 | gap=-0.021 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.186 > 0.08 con n=876 PNL=+617.61€
  - _Datos_: n=876 IC=+0.186 PNL=+617.61€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.154 > 0.08 con n=1042 PNL=+554.27€
  - _Datos_: n=1042 IC=+0.154 PNL=+554.27€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.153 > 0.08 con n=73 PNL=+34.44€
  - _Datos_: n=73 IC=+0.153 PNL=+34.44€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.333 > 0.1 con n=3389 PNL=+1891.17€
  - _Datos_: n=3389 IC=+0.333 PNL=+1891.17€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=883 IC=+0.068 PNL=+87.61€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=883 IC=+0.068 PNL=+87.61€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=98 IC=+0.190 PNL=+68.62€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=98 IC=+0.190 PNL=+68.62€

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
  - _Estado_: n=3622 IC=+0.005 PNL=-0.48€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3622 IC=+0.005 PNL=-0.48€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1780 IC=-0.002 PNL=+102.60€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1780 IC=-0.002 PNL=+102.60€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1126 IC=+0.025 PNL=+58.51€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1126 IC=+0.025 PNL=+58.51€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.163 > 0.1 con n=5783 PNL=+3344.88€
  - _Datos_: n=5783 IC=+0.163 PNL=+3344.88€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=3018 IC=+0.083 PNL=+688.41€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=3018 IC=+0.083 PNL=+688.41€

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
  - _Estado_: n=1131 IC=+0.037 PNL=+93.95€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1131 IC=+0.037 PNL=+93.95€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=146 IC=+0.013 PNL=+1.57€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=146 IC=+0.013 PNL=+1.57€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.270 n=198) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=198 IC=+0.270 PNL=+203.69€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.123 > 0.02 con n=1140 PNL=+476.59€
  - _Datos_: n=1140 IC=+0.123 PNL=+476.59€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=239 IC=-0.110 PNL=+10.85€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=239 IC=-0.110 PNL=+10.85€

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
  - _Estado_: n=36667 IC=+0.074 PNL=+5264.18€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=36667 IC=+0.074 PNL=+5264.18€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.137 < -0.1 con n=665 PNL=+91.93€
  - _Datos_: n=665 IC=-0.137 PNL=+91.93€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=3361 IC=+0.068 PNL=+444.71€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=3361 IC=+0.068 PNL=+444.71€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=168 IC=-0.118 PNL=-1.49€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=168 IC=-0.118 PNL=-1.49€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.105 > 0.1 con n=966 PNL=+248.46€
  - _Datos_: n=966 IC=+0.105 PNL=+248.46€

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
  - _Estado_: n=38460 IC=-0.136 PNL=+2604.44€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=38460 IC=-0.136 PNL=+2604.44€

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
  - _Estado_: n=3960 IC=+0.127 PNL=+2520.41€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=3960 IC=+0.127 PNL=+2520.41€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=9369 IC=+0.057 PNL=+815.40€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=9369 IC=+0.057 PNL=+815.40€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.098 > 0.08 con n=4095 PNL=+2282.02€
  - _Datos_: n=4095 IC=+0.098 PNL=+2282.02€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.219 < -0.1 con n=4110 PNL=-323.85€
  - _Datos_: n=4110 IC=-0.219 PNL=-323.85€

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
  - _Estado_: n=82 IC=+0.036 PNL=+12.80€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=82 IC=+0.036 PNL=+12.80€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.097 n=2038) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2038 IC=+0.097 PNL=+415.45€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.410 n=640) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=640 IC=+0.410 PNL=+919.25€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=16529 IC=+0.182 PNL=-1785.04€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=16529 IC=+0.182 PNL=-1785.04€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.226 > 0.1 con n=261 PNL=+177.93€
  - _Datos_: n=261 IC=+0.226 PNL=+177.93€
