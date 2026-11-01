# Hipótesis automáticas — 2026-11-01 21:03 UTC
_Generado por shadow_postmortem.py sobre 1151532 resoluciones (PNL=+154882.72€)_

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
- **FILTRO** `restante_s_al_confirmar` < `136.2` → IC=-0.216 (n=11101)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 136.2
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=33304)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `127.57` → IC=-0.258 (n=1162)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.57
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=3486)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `117.81` → IC=-0.303 (n=1150)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 117.81
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3453)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `156.74` → IC=-0.247 (n=3005)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 156.74
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=9016)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `132.04` → IC=-0.260 (n=2131)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.04
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=6394)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.212 (n=25119)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `8608.3515` → IC=+0.163 (n=2210)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 8608.3515 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.127 (n=21473)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=26075)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.225 (n=19806)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=7853)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6768.7899` → IC=+0.150 (n=3035)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 6768.7899 (IC base=+0.124)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.187 (n=2061)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.364 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=2646)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `9413.2764` → IC=+0.182 (n=1842)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 9413.2764 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.187 (n=1885)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.183 (n=2104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` < `0.295` → IC=+0.312 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.295 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=2695)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `16113.412` → IC=+0.185 (n=696)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 16113.412 (IC base=+0.180)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.173 (n=539)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` > 0.61 (IC base=+0.076)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.142 (n=1279)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.44 (IC base=+0.081)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=4840)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.166 (n=4099)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 15.0 (IC base=+0.163)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.375 (n=1600)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.215 (n=2177)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.349 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=2522)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=1229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.150 (n=1041)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 15.0 (IC base=+0.143)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.260 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.144 (n=1353)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `3079.6088` → IC=+0.134 (n=230)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 3079.6088 (IC base=+0.070)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.255 (n=918)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1279)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.148 (n=1363)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=710)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.146)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.286 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.146)

### FAVORITO_CONFIRMADO#SOL#60min
- **FILTRO** `libro_liquidez` < `946.7065` → IC=-0.123 (n=152)

  - _Acción_: SKIP cuando `libro_liquidez` < 946.7065
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=311)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.157 (n=450)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` > 0.55 (IC base=+0.050)

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

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=21498)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.201 (n=18194)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.229 (n=8919)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.198)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.182 (n=2328)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.178 (n=4893)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 18.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.182 (n=4706)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.177 (n=4083)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.218 (n=2760)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.220 (n=2448)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.216)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.292 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.216)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=4828)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.179 (n=4102)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.177 (n=5005)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=3757)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=4124)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.249 (n=3496)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.249)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.358 (n=1405)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=4740)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=4030)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.188 (n=3623)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.71 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=3524)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.187)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.429 (n=891)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.429 (n=896)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=905)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=941)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `4385.1965` → IC=+0.443 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4385.1965 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.443 (n=368)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.450 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

- **PATRÓN** `libro_liquidez` > `12297.8844` → IC=+0.446 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12297.8844 (IC base=+0.438)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=28112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.245 (n=28337)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.201)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.190 (n=4175)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 18.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.184 (n=8937)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 12.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.195 (n=12727)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.229 (n=5853)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.226)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.288 (n=4027)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.226)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=4825)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.200 (n=9910)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.228 (n=3934)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.223 (n=4477)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.272 (n=3982)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.211 (n=3997)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.259 (n=4160)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=4675)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.201 (n=4634)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=4875)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=10016)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=10252)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.38` → IC=+0.139 (n=9294)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.38 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=4898)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.118)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.144 (n=4635)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=6127)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.118)

- **PATRÓN** `lag_apertura_s` < `2.68` → IC=+0.144 (n=4625)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 2.68 (IC base=+0.118)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.190 (n=5118)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=5617)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `3.24` → IC=+0.137 (n=6158)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.24 (IC base=+0.116)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.311 (n=1266)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.294)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.387 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `3872.2908` → IC=+0.296 (n=803)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3872.2908 (IC base=+0.294)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.290 (n=849)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.283)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.364 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.283)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.322 (n=617)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.299)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.303 (n=898)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.299)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.395 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.299)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.299 (n=1023)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.299)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.448 (n=859)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.445)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.445 (n=852)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.445)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.452 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.445)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.441 (n=406)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.440 (n=280)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.440 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.445 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.460 (n=275)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.451)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.456 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.451)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.455 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.451)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.452 (n=311)

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
- **FILTRO** `hora_utc` < `5.0` → IC=-0.269 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=107)

- **FILTRO** `py_entrada` > `0.735` → IC=-0.386 (n=42)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.137 (n=89)

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
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=107)

- **FILTRO** `py_entrada` > `0.735` → IC=-0.386 (n=42)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.137 (n=89)

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
- **PATRÓN** `drift_60min` |x|≤ `0.473` → IC=+0.138 (n=15751)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.473 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.125 (n=15934)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.125 (n=10962)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.3747` → IC=+0.164 (n=15751)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.3747 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.7752` → IC=+0.279 (n=873)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7752 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.584` → IC=+0.182 (n=7867)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 3.584 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `0.6226` → IC=+0.265 (n=4622)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6226 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.3033` → IC=+0.243 (n=1613)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3033 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` > `2.7312` → IC=+0.229 (n=3752)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7312 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=7973)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `4669.1956` → IC=+0.145 (n=5251)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 4669.1956 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.121 (n=9825)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.006 (IC base=+0.079)

- **PATRÓN** `ibs_20min` < `0.68` → IC=+0.131 (n=22284)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.68 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` > `0.5999` → IC=+0.187 (n=1303)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.5999 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` < `0.1582` → IC=+0.187 (n=7577)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.1582 (IC base=+0.079)

- **PATRÓN** `volumen_regimen` < `0.8629` → IC=+0.190 (n=5248)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.8629 (IC base=+0.079)

- **PATRÓN** `volumen_pendiente_norm` > `0.297` → IC=+0.231 (n=1951)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.297 (IC base=+0.079)

- **PATRÓN** `volumen_spike_ratio` > `2.685` → IC=+0.208 (n=4461)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.685 (IC base=+0.079)

- **PATRÓN** `ballena_activa_n` < `104.0` → IC=+0.225 (n=13284)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 104.0 (IC base=+0.079)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3615` → IC=+0.210 (n=3388)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3615 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.221 (n=1644)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.211 (n=2268)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.9844` → IC=+0.280 (n=1537)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9844 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.617` → IC=+0.280 (n=1505)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.617 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.2834` → IC=+0.260 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2834 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.4364` → IC=+0.208 (n=3243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4364 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.222 (n=3721)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `2059.42` → IC=+0.211 (n=1130)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2059.42 (IC base=+0.207)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.220 (n=3061)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.241 (n=2937)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0096 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.089` → IC=+0.277 (n=980)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.089 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.252 (n=1086)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.240 (n=1354)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.5519` → IC=+0.259 (n=2935)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5519 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` < `0.0956` → IC=+0.242 (n=2654)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0956 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2919` → IC=+0.257 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2919 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.4445` → IC=+0.240 (n=930)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4445 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `1.5514` → IC=+0.241 (n=2492)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5514 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=3375)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1489.6339` → IC=+0.245 (n=2622)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1489.6339 (IC base=+0.239)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.236 (n=934)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.228 (n=934)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.1066` → IC=+0.257 (n=1233)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1066 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.238 (n=2931)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.229 (n=1991)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.9216` → IC=+0.269 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9216 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `0.1842` → IC=+0.234 (n=1312)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1842 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.089` → IC=+0.255 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.089 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` < `1.2254` → IC=+0.228 (n=2803)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2254 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `0.6261` → IC=+0.230 (n=2802)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6261 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2783` → IC=+0.266 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2783 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.4011` → IC=+0.231 (n=922)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4011 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `2.4279` → IC=+0.253 (n=922)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4279 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `8946.8099` → IC=+0.227 (n=2802)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8946.8099 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.149 (n=2992)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0062 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.077` → IC=+0.153 (n=998)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.077 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.150 (n=1111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.7148` → IC=+0.165 (n=2991)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.7148 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.1349` → IC=+0.143 (n=2850)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1349 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.76` → IC=+0.139 (n=488)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 10.76 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.022` → IC=+0.131 (n=2734)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 4.022 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `1.2012` → IC=+0.133 (n=2990)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.2012 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.0974` → IC=+0.151 (n=1089)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.0974 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `2.1376` → IC=+0.134 (n=2522)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.1376 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `1.7941` → IC=+0.127 (n=1911)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.7941 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.127 (n=3877)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `205.0` → IC=+0.164 (n=1236)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 205.0 (IC base=+0.126)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.214 (n=1191)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.199 (n=3747)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.264 (n=1385)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.106` → IC=+0.277 (n=773)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.106 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.097` → IC=+0.196 (n=3185)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.097 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.3534` → IC=+0.217 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3534 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.712` → IC=+0.207 (n=1576)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.712 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=4284)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `1935.0681` → IC=+0.202 (n=1617)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1935.0681 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.225 (n=2867)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.1771` → IC=+0.237 (n=1433)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1771 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=1232)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.222 (n=1478)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` < `0.0379` → IC=+0.269 (n=1086)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0379 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.104` → IC=+0.263 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.104 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.3494` → IC=+0.263 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3494 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.151` → IC=+0.226 (n=2078)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.151 (IC base=+0.219)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=1663)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `1918.06` → IC=+0.221 (n=1477)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1918.06 (IC base=+0.219)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.219 (n=2737)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.219)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.161 (n=181)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=4292)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.159 (n=613)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0038 (IC base=+0.053)

- **PATRÓN** `ibs_20min` > `0.9436` → IC=+0.232 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9436 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` > `0.1359` → IC=+0.335 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1359 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` < `0.3345` → IC=+0.327 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3345 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.086` → IC=+0.196 (n=1330)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 5.086 (IC base=+0.053)

- **PATRÓN** `volumen_regimen` > `1.2462` → IC=+0.354 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2462 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` < `0.0775` → IC=+0.328 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0775 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.3033` → IC=+0.331 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3033 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` < `1.5356` → IC=+0.337 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5356 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` > `2.2606` → IC=+0.332 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2606 (IC base=+0.053)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.333 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 143.0 (IC base=+0.053)

- **PATRÓN** `ibs_20min` < `0.092` → IC=+0.181 (n=1119)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.092 (IC base=+0.045)

- **PATRÓN** `dist_vwap_pct` > `0.7095` → IC=+0.168 (n=269)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.7095 (IC base=+0.045)

- **PATRÓN** `dist_vwap_pct` < `0.1359` → IC=+0.144 (n=1935)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1359 (IC base=+0.045)

- **PATRÓN** `volumen_regimen` < `0.8338` → IC=+0.158 (n=1385)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8338 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.208 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` < `1.7817` → IC=+0.148 (n=1332)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.7817 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` > `2.156` → IC=+0.162 (n=906)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.156 (IC base=+0.045)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.179 (n=129)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=673)

- **FILTRO** `ibs_20min` < `0.2667` → IC=-0.167 (n=199)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2667
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=603)

- **FILTRO** `ibs_20min` > `0.2069` → IC=-0.133 (n=4205)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2069
  - _Potencial_: sin este filtro IC_bueno=+0.149 (n=2081)

- **FILTRO** `sigma_ewma_delta_pct` > `8.44` → IC=-0.223 (n=679)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.44
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=5607)

- **PATRÓN** `ibs_20min` > `0.7586` → IC=+0.173 (n=273)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.7586 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.9658` → IC=+0.277 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9658 (IC base=+0.024)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.045` → IC=+0.160 (n=189)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 5.045 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` < `0.5734` → IC=+0.262 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5734 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` > `1.0454` → IC=+0.286 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0454 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` < `0.1553` → IC=+0.281 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1553 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `2.4897` → IC=+0.285 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4897 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` > `1.449` → IC=+0.263 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.449 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.268 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.024)

- **PATRÓN** `ibs_20min` < `0.2069` → IC=+0.149 (n=2081)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.2069 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` < `0.2932` → IC=+0.276 (n=946)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2932 (IC base=-0.039)

- **PATRÓN** `volumen_regimen` < `0.6963` → IC=+0.306 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6963 (IC base=-0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.1637` → IC=+0.297 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1637 (IC base=-0.039)

- **PATRÓN** `volumen_spike_ratio` < `2.456` → IC=+0.303 (n=829)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.456 (IC base=-0.039)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7692` → IC=-0.153 (n=3124)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7692
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=1618)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.169 (n=1095)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=3647)

- **FILTRO** `ibs_20min` > `0.7463` → IC=-0.197 (n=1672)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7463
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=5024)

- **PATRÓN** `dist_vwap_pct` > `1.0308` → IC=+0.360 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0308 (IC base=-0.063)

- **PATRÓN** `dist_vwap_pct` < `0.2456` → IC=+0.308 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2456 (IC base=-0.063)

- **PATRÓN** `volumen_regimen` > `0.7043` → IC=+0.319 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7043 (IC base=-0.063)

- **PATRÓN** `volumen_pendiente_norm` < `0.1036` → IC=+0.308 (n=816)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1036 (IC base=-0.063)

- **PATRÓN** `volumen_spike_ratio` < `1.4371` → IC=+0.313 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4371 (IC base=-0.063)

- **PATRÓN** `volumen_spike_ratio` > `1.8655` → IC=+0.311 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8655 (IC base=-0.063)

- **PATRÓN** `dist_vwap_pct` > `0.7967` → IC=+0.275 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7967 (IC base=-0.001)

- **PATRÓN** `dist_vwap_pct` < `0.2201` → IC=+0.263 (n=1886)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2201 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` < `0.7243` → IC=+0.272 (n=841)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7243 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` > `1.066` → IC=+0.285 (n=866)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.066 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.1693` → IC=+0.284 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1693 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `2.1776` → IC=+0.265 (n=1571)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1776 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `1.4322` → IC=+0.269 (n=1785)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4322 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.204 (n=6831)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.091)

- **PATRÓN** `ibs_20min` > `0.8747` → IC=+0.287 (n=9274)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8747 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `0.9264` → IC=+0.302 (n=1464)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9264 (IC base=+0.091)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.545` → IC=+0.167 (n=9165)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.545 (IC base=+0.091)

- **PATRÓN** `volumen_regimen` < `1.1742` → IC=+0.269 (n=7488)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1742 (IC base=+0.091)

- **PATRÓN** `volumen_regimen` > `0.6916` → IC=+0.275 (n=6691)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6916 (IC base=+0.091)

- **PATRÓN** `volumen_pendiente_norm` > `0.24` → IC=+0.287 (n=2250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.24 (IC base=+0.091)

- **PATRÓN** `volumen_spike_ratio` < `1.4577` → IC=+0.272 (n=3974)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4577 (IC base=+0.091)

- **PATRÓN** `volumen_spike_ratio` > `2.651` → IC=+0.279 (n=3972)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.651 (IC base=+0.091)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.305 (n=11534)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 91.0 (IC base=+0.091)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.155 (n=6591)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0098 (IC base=+0.078)

- **PATRÓN** `ibs_20min` < `0.6471` → IC=+0.149 (n=19751)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.6471 (IC base=+0.078)

- **PATRÓN** `dist_vwap_pct` < `0.2479` → IC=+0.273 (n=6503)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2479 (IC base=+0.078)

- **PATRÓN** `volumen_regimen` < `0.7037` → IC=+0.273 (n=2818)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7037 (IC base=+0.078)

- **PATRÓN** `volumen_regimen` > `1.1942` → IC=+0.271 (n=2134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1942 (IC base=+0.078)

- **PATRÓN** `volumen_pendiente_norm` > `0.2946` → IC=+0.322 (n=1400)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2946 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` < `1.5778` → IC=+0.296 (n=4119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5778 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` > `2.2821` → IC=+0.292 (n=4244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2821 (IC base=+0.078)

- **PATRÓN** `ballena_activa_n` < `74.0` → IC=+0.303 (n=9298)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 74.0 (IC base=+0.078)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.5801` → IC=-0.160 (n=2792)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5801
  - _Potencial_: sin este filtro IC_bueno=+0.205 (n=2793)

- **FILTRO** `ibs_20min` > `0.7228` → IC=-0.226 (n=1213)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7228
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=3640)

- **FILTRO** `sigma_ewma_delta_pct` > `4.237` → IC=-0.227 (n=1049)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.237
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=3804)

- **PATRÓN** `ibs_20min` > `0.9293` → IC=+0.332 (n=1397)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9293 (IC base=+0.023)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.089` → IC=+0.185 (n=1871)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 3.089 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.2292` → IC=+0.323 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2292 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` < `1.4451` → IC=+0.274 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4451 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` > `2.2496` → IC=+0.292 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2496 (IC base=+0.023)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.310 (n=1220)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.023)

- **PATRÓN** `ibs_20min` < `0.1714` → IC=+0.156 (n=1215)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.1714 (IC base=-0.027)

- **PATRÓN** `volumen_pendiente_norm` < `0.1515` → IC=+0.404 (n=819)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1515 (IC base=-0.027)

- **PATRÓN** `volumen_spike_ratio` < `1.4231` → IC=+0.426 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4231 (IC base=-0.027)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.397 (n=831)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=-0.027)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.6151` → IC=+0.227 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6151 (IC base=+0.016)

- **PATRÓN** `volumen_regimen` < `1.1944` → IC=+0.206 (n=1989)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1944 (IC base=+0.016)

- **PATRÓN** `volumen_regimen` > `0.6937` → IC=+0.209 (n=1777)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6937 (IC base=+0.016)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.246 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.016)

- **PATRÓN** `volumen_spike_ratio` < `1.417` → IC=+0.232 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.417 (IC base=+0.016)

- **PATRÓN** `volumen_spike_ratio` > `2.4449` → IC=+0.209 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4449 (IC base=+0.016)

- **PATRÓN** `ballena_activa_n` < `267.0` → IC=+0.241 (n=1313)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 267.0 (IC base=+0.016)

- **PATRÓN** `dist_vwap_pct` < `0.1262` → IC=+0.247 (n=1381)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1262 (IC base=-0.005)

- **PATRÓN** `volumen_regimen` < `1.1652` → IC=+0.236 (n=1360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1652 (IC base=-0.005)

- **PATRÓN** `volumen_regimen` > `0.6223` → IC=+0.241 (n=1361)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6223 (IC base=-0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2713` → IC=+0.306 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2713 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.5307` → IC=+0.246 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5307 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.1523` → IC=+0.253 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1523 (IC base=-0.005)

- **PATRÓN** `ballena_activa_n` < `214.0` → IC=+0.250 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 214.0 (IC base=-0.005)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.322 (n=1323)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.278)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.287 (n=2919)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.278)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.320 (n=1579)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.278)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.478` → IC=+0.301 (n=1758)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.478 (IC base=+0.278)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.291 (n=2557)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` > `1.7739` → IC=+0.284 (n=2526)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7739 (IC base=+0.278)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.287 (n=3475)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `2036.8884` → IC=+0.296 (n=972)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2036.8884 (IC base=+0.278)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.301 (n=1776)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.278)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.333 (n=1180)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.300)

- **PATRÓN** `drift_60min` |x|≤ `0.1771` → IC=+0.320 (n=1144)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1771 (IC base=+0.300)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.325 (n=994)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.300)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.303 (n=895)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.300)

- **PATRÓN** `ibs_20min` < `0.009` → IC=+0.303 (n=1145)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.009 (IC base=+0.300)

- **PATRÓN** `ibs_20min` > `0.1351` → IC=+0.309 (n=1734)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1351 (IC base=+0.300)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.337` → IC=+0.311 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.337 (IC base=+0.300)

- **PATRÓN** `volumen_pendiente_norm` < `0.1982` → IC=+0.299 (n=2556)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1982 (IC base=+0.300)

- **PATRÓN** `volumen_pendiente_norm` > `0.3444` → IC=+0.311 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3444 (IC base=+0.300)

- **PATRÓN** `volumen_spike_ratio` < `1.7441` → IC=+0.300 (n=1100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7441 (IC base=+0.300)

- **PATRÓN** `volumen_spike_ratio` > `2.7236` → IC=+0.312 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7236 (IC base=+0.300)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.304 (n=1329)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.300)

- **PATRÓN** `libro_liquidez` > `1919.6972` → IC=+0.310 (n=1179)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1919.6972 (IC base=+0.300)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.306 (n=1640)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.300)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7312` → IC=-0.183 (n=1268)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7312
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=3806)

- **PATRÓN** `ibs_20min` > `0.8602` → IC=+0.167 (n=1234)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.8602 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.144` → IC=+0.232 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.144 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` < `0.3574` → IC=+0.235 (n=1728)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3574 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` < `1.0082` → IC=+0.238 (n=1551)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0082 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` > `0.6703` → IC=+0.231 (n=1574)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6703 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.1025` → IC=+0.238 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1025 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `2.1457` → IC=+0.240 (n=1501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1457 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `118.0` → IC=+0.254 (n=1740)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 118.0 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` < `0.1458` → IC=+0.245 (n=1220)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1458 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` < `1.1822` → IC=+0.249 (n=1250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1822 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.306 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.7898` → IC=+0.279 (n=797)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7898 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.4311` → IC=+0.263 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4311 (IC base=+0.003)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.275 (n=1064)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 102.0 (IC base=+0.003)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7451` → IC=-0.238 (n=2120)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7451
  - _Potencial_: sin este filtro IC_bueno=+0.311 (n=2121)

- **FILTRO** `ibs_20min` > `0.6327` → IC=-0.233 (n=1020)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6327
  - _Potencial_: sin este filtro IC_bueno=+0.138 (n=3067)

- **FILTRO** `sigma_ewma_delta_pct` > `8.354` → IC=-0.249 (n=468)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.354
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=3619)

- **PATRÓN** `ibs_20min` > `0.7451` → IC=+0.311 (n=2121)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7451 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` > `0.213` → IC=+0.345 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.213 (IC base=+0.036)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.482` → IC=+0.149 (n=1710)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 2.482 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` < `0.8456` → IC=+0.340 (n=1035)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8456 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` > `0.6974` → IC=+0.334 (n=1387)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6974 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` < `0.1583` → IC=+0.336 (n=1609)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1583 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` > `0.2751` → IC=+0.354 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2751 (IC base=+0.036)

- **PATRÓN** `volumen_spike_ratio` < `1.4313` → IC=+0.361 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4313 (IC base=+0.036)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.354 (n=1334)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.036)

- **PATRÓN** `ibs_20min` < `0.6327` → IC=+0.138 (n=3067)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.6327 (IC base=+0.045)

- **PATRÓN** `dist_vwap_pct` < `0.2118` → IC=+0.255 (n=1420)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2118 (IC base=+0.045)

- **PATRÓN** `volumen_regimen` < `0.6965` → IC=+0.278 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6965 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.272 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` < `2.4528` → IC=+0.259 (n=1416)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4528 (IC base=+0.045)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.273 (n=1434)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.045)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.356 (n=1953)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.312)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.314 (n=2210)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.312)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.317 (n=1032)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.312)

- **PATRÓN** `ibs_20min` > `0.7634` → IC=+0.349 (n=1953)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7634 (IC base=+0.312)

- **PATRÓN** `dist_vwap_pct` > `0.2044` → IC=+0.336 (n=1210)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2044 (IC base=+0.312)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.816` → IC=+0.330 (n=1060)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.816 (IC base=+0.312)

- **PATRÓN** `volumen_regimen` > `0.629` → IC=+0.322 (n=2186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.629 (IC base=+0.312)

- **PATRÓN** `volumen_pendiente_norm` > `0.28` → IC=+0.349 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.28 (IC base=+0.312)

- **PATRÓN** `volumen_spike_ratio` > `1.4264` → IC=+0.325 (n=2101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4264 (IC base=+0.312)

- **PATRÓN** `libro_liquidez` > `2572.5002` → IC=+0.313 (n=1457)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2572.5002 (IC base=+0.312)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.343 (n=1915)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.312)

- **PATRÓN** `sigma_h` > `0.0153` → IC=+0.344 (n=1551)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0153 (IC base=+0.313)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.321 (n=1170)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.313)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.315 (n=1138)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.313)

- **PATRÓN** `ibs_20min` < `0.38` → IC=+0.334 (n=2327)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.38 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` < `0.2329` → IC=+0.319 (n=2241)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2329 (IC base=+0.313)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.628` → IC=+0.330 (n=862)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.628 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` < `0.7226` → IC=+0.320 (n=1024)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7226 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` > `1.213` → IC=+0.342 (n=776)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.213 (IC base=+0.313)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.366 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` < `1.4108` → IC=+0.325 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4108 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` > `2.1339` → IC=+0.316 (n=974)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1339 (IC base=+0.313)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.227 (n=5102)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.1216` → IC=+0.194 (n=6726)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1216 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=15872)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `0.5433` → IC=+0.233 (n=15285)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5433 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.1612` → IC=+0.207 (n=5965)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1612 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.156` → IC=+0.254 (n=3984)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.156 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `1.1851` → IC=+0.159 (n=10169)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1851 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` > `0.6243` → IC=+0.158 (n=10170)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.6243 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.2938` → IC=+0.206 (n=2216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2938 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `2.6062` → IC=+0.188 (n=4952)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6062 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.196 (n=14213)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 90.0 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.190 (n=6566)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0056 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.0802` → IC=+0.222 (n=4962)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0802 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=5598)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.52` → IC=+0.238 (n=14874)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.52 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` < `0.1771` → IC=+0.175 (n=10727)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.1771 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.739` → IC=+0.193 (n=2379)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 9.739 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.586` → IC=+0.185 (n=13216)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 2.586 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.1804` → IC=+0.163 (n=10602)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1804 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2957` → IC=+0.221 (n=2226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2957 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6424` → IC=+0.188 (n=4697)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6424 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `95.0` → IC=+0.195 (n=13847)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 95.0 (IC base=+0.181)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.226 (n=847)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0055 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.1048` → IC=+0.258 (n=1113)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1048 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.241 (n=935)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.229 (n=1709)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.807` → IC=+0.274 (n=2259)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.807 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.697` → IC=+0.329 (n=812)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.697 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.287 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `1.8388` → IC=+0.224 (n=1604)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8388 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `1.4361` → IC=+0.225 (n=2406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4361 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=2801)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.258 (n=2020)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0092 (IC base=+0.254)

- **PATRÓN** `drift_60min` |x|≤ `0.0973` → IC=+0.307 (n=889)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0973 (IC base=+0.254)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.260 (n=2089)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.254)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.256 (n=1839)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.254)

- **PATRÓN** `ibs_20min` < `0.4219` → IC=+0.271 (n=2017)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4219 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` < `0.1008` → IC=+0.259 (n=1774)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1008 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` > `0.3022` → IC=+0.276 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3022 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` < `1.4445` → IC=+0.278 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4445 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` > `2.7246` → IC=+0.256 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7246 (IC base=+0.254)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.257 (n=2320)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.254)

- **PATRÓN** `libro_liquidez` > `1477.8921` → IC=+0.262 (n=1801)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1477.8921 (IC base=+0.254)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.254 (n=926)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.254)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.201 (n=780)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0641` → IC=+0.180 (n=776)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.0641 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.154 (n=2436)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.2772` → IC=+0.212 (n=2325)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2772 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.1836` → IC=+0.214 (n=1199)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1836 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.903` → IC=+0.207 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.903 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.6949` → IC=+0.149 (n=1025)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6949 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `1.061` → IC=+0.140 (n=1055)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 1.061 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.180 (n=360)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.503` → IC=+0.153 (n=1005)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.503 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.4691` → IC=+0.149 (n=761)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 2.4691 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `407.0` → IC=+0.143 (n=2247)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 407.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.172 (n=2460)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0062 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.237` → IC=+0.167 (n=2164)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.237 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.182 (n=1179)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.6154` → IC=+0.204 (n=2457)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6154 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.145` → IC=+0.180 (n=464)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 11.145 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.072` → IC=+0.146 (n=2148)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 4.072 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.1995` → IC=+0.157 (n=2457)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1995 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.0946` → IC=+0.146 (n=2127)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.0946 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.1387` → IC=+0.147 (n=2054)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.1387 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `215.0` → IC=+0.182 (n=1000)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 215.0 (IC base=+0.144)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.237 (n=1177)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.3956` → IC=+0.224 (n=2278)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3956 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.235 (n=944)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=1366)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.293` → IC=+0.307 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.293 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.212 (n=2247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.3534` → IC=+0.233 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3534 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.7614` → IC=+0.212 (n=1110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7614 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.7105` → IC=+0.225 (n=1143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7105 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.217 (n=3108)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `1925.8986` → IC=+0.226 (n=1174)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1925.8986 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.246 (n=1988)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.4192` → IC=+0.261 (n=1985)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4192 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.284 (n=863)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.0299` → IC=+0.289 (n=993)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0299 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.217` → IC=+0.282 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.217 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.3594` → IC=+0.293 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3594 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.1746` → IC=+0.247 (n=1446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1746 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.240 (n=1173)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1912.1584` → IC=+0.252 (n=1023)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1912.1584 (IC base=+0.238)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.244 (n=1465)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.238)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.205 (n=836)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0772` → IC=+0.194 (n=834)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.0772 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.148 (n=2593)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.2701` → IC=+0.200 (n=2499)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2701 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.1376` → IC=+0.186 (n=1481)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1376 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.45` → IC=+0.195 (n=431)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 11.45 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.0214` → IC=+0.143 (n=2200)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.0214 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2887` → IC=+0.176 (n=372)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2887 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.8252` → IC=+0.141 (n=1632)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.8252 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.5248` → IC=+0.155 (n=816)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.5248 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `6872.8229` → IC=+0.200 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6872.8229 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `132.0` → IC=+0.144 (n=2443)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 132.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.164 (n=2331)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0065 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.3933` → IC=+0.141 (n=2648)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3933 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.161 (n=1264)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 15.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.6746` → IC=+0.184 (n=2648)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6746 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.1563` → IC=+0.154 (n=2657)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1563 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.384` → IC=+0.145 (n=638)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 9.384 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8525` → IC=+0.153 (n=1767)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8525 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2971` → IC=+0.181 (n=399)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2971 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.8095` → IC=+0.129 (n=1667)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.8095 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `1.4242` → IC=+0.126 (n=2500)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.4242 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `6169.9124` → IC=+0.180 (n=1201)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 6169.9124 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `110.0` → IC=+0.131 (n=2174)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 110.0 (IC base=+0.126)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.168 (n=1268)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0109 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.160 (n=1347)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 15.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.4767` → IC=+0.211 (n=2796)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4767 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.1961` → IC=+0.190 (n=1540)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1961 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.203` → IC=+0.289 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.203 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.1747` → IC=+0.133 (n=2797)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1747 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.7041` → IC=+0.124 (n=2498)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.7041 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.163` → IC=+0.131 (n=2853)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.163 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.5413` → IC=+0.139 (n=1195)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.5413 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.124 (n=2919)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2638.2977` → IC=+0.199 (n=1268)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2638.2977 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.144 (n=1169)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 21.0 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0115` → IC=+0.141 (n=2900)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0115 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.1101` → IC=+0.161 (n=967)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1101 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.135 (n=2961)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.641` → IC=+0.218 (n=2897)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.641 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` < `0.204` → IC=+0.145 (n=2816)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.204 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.334` → IC=+0.136 (n=2557)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 2.334 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `1.1776` → IC=+0.127 (n=2897)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.1776 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.276` → IC=+0.134 (n=397)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.276 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.4363` → IC=+0.123 (n=908)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.4363 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` > `2.4456` → IC=+0.124 (n=908)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 2.4456 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2522.6175` → IC=+0.179 (n=1314)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2522.6175 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.123 (n=2690)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 46.0 (IC base=+0.117)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.248 (n=2278)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1678` → IC=+0.241 (n=1123)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1678 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.228 (n=2650)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.230 (n=2291)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.6639` → IC=+0.259 (n=2549)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6639 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.1803` → IC=+0.232 (n=1602)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1803 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` < `0.8166` → IC=+0.226 (n=2626)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8166 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.594` → IC=+0.255 (n=1150)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.594 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.6235` → IC=+0.233 (n=2549)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6235 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2323` → IC=+0.268 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2323 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `2.4689` → IC=+0.228 (n=2485)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4689 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.8094` → IC=+0.236 (n=1656)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8094 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2936.2954` → IC=+0.234 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2936.2954 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0128` → IC=+0.241 (n=1145)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0128 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0227` → IC=+0.247 (n=1182)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0227 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.0876` → IC=+0.261 (n=869)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0876 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.252 (n=1270)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.242 (n=1160)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.44` → IC=+0.263 (n=2613)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.44 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `1.1311` → IC=+0.245 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1311 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.232` → IC=+0.269 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.232 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` < `0.8693` → IC=+0.238 (n=1735)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8693 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` > `0.6418` → IC=+0.240 (n=2602)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6418 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.288 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.8359` → IC=+0.234 (n=1627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8359 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `1.4336` → IC=+0.239 (n=2440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4336 (IC base=+0.237)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.206 (n=1286)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.13` → IC=+0.184 (n=1693)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.13 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.186 (n=3443)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.3274` → IC=+0.202 (n=3846)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3274 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.7948` → IC=+0.197 (n=582)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.7948 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.552` → IC=+0.197 (n=1651)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 3.552 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.185 (n=2320)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.8616 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `1.1921` → IC=+0.171 (n=1159)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.1921 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.0739` → IC=+0.174 (n=1555)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.0739 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.4279` → IC=+0.179 (n=1249)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.4279 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.171 (n=4318)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.02 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `8349.8114` → IC=+0.184 (n=1744)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 8349.8114 (IC base=+0.167)

- **PATRÓN** `ibs_20min` < `0.3896` → IC=+0.159 (n=2759)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.3896 (IC base=+0.083)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.127 (n=1752)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 26.0 (IC base=+0.083)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.194 (n=1039)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0058 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.099` → IC=+0.235 (n=458)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.099 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.213 (n=944)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.2225` → IC=+0.217 (n=1038)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2225 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.2987` → IC=+0.212 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2987 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.975` → IC=+0.198 (n=455)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 2.975 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.457` → IC=+0.183 (n=1093)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 6.457 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.8799` → IC=+0.198 (n=693)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.8799 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` < `0.1507` → IC=+0.184 (n=1093)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.1507 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.0915` → IC=+0.186 (n=361)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.0915 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `2.1906` → IC=+0.197 (n=895)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.1906 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `14223.7194` → IC=+0.190 (n=692)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 14223.7194 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.164 (n=560)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0034 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.6346` → IC=+0.137 (n=1115)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.6346 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `163.0` → IC=+0.167 (n=547)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 163.0 (IC base=+0.085)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.244 (n=529)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.2091` → IC=+0.188 (n=802)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.2091 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=1256)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.635` → IC=+0.251 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.635 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.7737` → IC=+0.193 (n=190)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.7737 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` < `0.2032` → IC=+0.180 (n=1085)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.2032 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.838` → IC=+0.216 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.838 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `0.8342` → IC=+0.195 (n=802)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8342 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.1596` → IC=+0.201 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1596 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `1.4274` → IC=+0.186 (n=396)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.4274 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `1.7865` → IC=+0.190 (n=792)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.7865 (IC base=+0.179)

- **PATRÓN** `ibs_20min` < `0.1008` → IC=+0.184 (n=391)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.1008 (IC base=+0.076)

- **PATRÓN** `libro_liquidez` > `8153.6622` → IC=+0.140 (n=531)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 8153.6622 (IC base=+0.076)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.157 (n=423)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.007 (IC base=+0.141)

- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.144 (n=321)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0114 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.174 (n=861)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 8.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.4918` → IC=+0.198 (n=961)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.4918 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.968` → IC=+0.218 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.968 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.01` → IC=+0.237 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.01 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.0549` → IC=+0.152 (n=846)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.0549 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` > `0.7047` → IC=+0.149 (n=859)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.7047 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` < `0.1042` → IC=+0.140 (n=870)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` < 0.1042 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.2267` → IC=+0.163 (n=179)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.2267 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.4277` → IC=+0.167 (n=310)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.4277 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `2.1499` → IC=+0.143 (n=421)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.1499 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.148 (n=1008)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.02 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `2741.5709` → IC=+0.176 (n=436)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2741.5709 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.5732` → IC=+0.135 (n=925)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.5732 (IC base=+0.049)

- **PATRÓN** `libro_liquidez` > `2579.8383` → IC=+0.143 (n=477)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 2579.8383 (IC base=+0.049)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0262` → IC=+0.173 (n=276)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0262 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0165` → IC=+0.215 (n=184)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0165 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.2668` → IC=+0.177 (n=184)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2668 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.220 (n=130)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.7393` → IC=+0.199 (n=184)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.7393 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.3078` → IC=+0.181 (n=142)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.3078 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` < `1.1938` → IC=+0.169 (n=309)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 1.1938 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.349` → IC=+0.195 (n=244)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` < 3.349 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `0.8592` → IC=+0.167 (n=184)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8592 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `1.1567` → IC=+0.192 (n=92)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` > 1.1567 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.1044` → IC=+0.181 (n=89)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1044 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.8264` → IC=+0.191 (n=166)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.8264 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `2.4281` → IC=+0.194 (n=83)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.4281 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.188 (n=325)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.03 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `2675.5939` → IC=+0.209 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2675.5939 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.176 (n=273)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0131 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.3001` → IC=+0.146 (n=204)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3001 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.161 (n=278)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 7.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.1942` → IC=+0.162 (n=134)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.1942 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `1.2011` → IC=+0.264 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2011 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.241` → IC=+0.191 (n=82)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 5.241 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `0.8723` → IC=+0.175 (n=204)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.8723 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` < `0.1149` → IC=+0.146 (n=278)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.1149 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.189 (n=59)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `1.5322` → IC=+0.207 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5322 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `2.7694` → IC=+0.157 (n=97)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.7694 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `1962.6643` → IC=+0.145 (n=305)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 1962.6643 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.162 (n=282)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 19.0 (IC base=+0.142)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.230 (n=6653)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=20810)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.4361` → IC=+0.229 (n=19945)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4361 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.8717` → IC=+0.210 (n=2398)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8717 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.076` → IC=+0.254 (n=4895)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.076 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.2172` → IC=+0.162 (n=13408)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2172 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2413` → IC=+0.205 (n=3593)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2413 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6204` → IC=+0.193 (n=6482)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6204 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.202 (n=18568)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 106.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.198 (n=8043)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0058 (IC base=+0.191)

- **PATRÓN** `sigma_h` > `0.012` → IC=+0.196 (n=6090)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.012 (IC base=+0.191)

- **PATRÓN** `drift_60min` |x|≤ `0.4821` → IC=+0.194 (n=18260)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.4821 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=6802)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` < `0.5909` → IC=+0.242 (n=18265)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5909 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` < `0.1758` → IC=+0.173 (n=11392)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1758 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.598` → IC=+0.204 (n=2495)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.598 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.457` → IC=+0.194 (n=17750)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 3.457 (IC base=+0.191)

- **PATRÓN** `volumen_regimen` < `0.6328` → IC=+0.171 (n=4096)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.6328 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.2923` → IC=+0.254 (n=2500)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2923 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `2.633` → IC=+0.202 (n=5801)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.633 (IC base=+0.191)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.206 (n=17136)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 94.0 (IC base=+0.191)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.247 (n=1558)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.234 (n=2162)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` > `0.8602` → IC=+0.301 (n=2144)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8602 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.71` → IC=+0.337 (n=1042)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.71 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.233` → IC=+0.291 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.233 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` < `1.4446` → IC=+0.232 (n=1034)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4446 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.2835` → IC=+0.237 (n=1406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2835 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.249 (n=3518)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `2057.3966` → IC=+0.236 (n=1072)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2057.3966 (IC base=+0.232)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.255 (n=1089)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.232)

- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.269 (n=2821)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0096 (IC base=+0.265)

- **PATRÓN** `drift_60min` |x|≤ `0.1219` → IC=+0.292 (n=1243)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1219 (IC base=+0.265)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.270 (n=2605)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.265)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.266 (n=2561)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.265)

- **PATRÓN** `ibs_20min` < `0.4421` → IC=+0.294 (n=2483)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4421 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.266 (n=2560)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` > `0.2904` → IC=+0.291 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2904 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` < `1.5652` → IC=+0.264 (n=1186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5652 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` > `2.6632` → IC=+0.277 (n=898)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6632 (IC base=+0.265)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.266 (n=3249)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.265)

- **PATRÓN** `libro_liquidez` > `1761.9` → IC=+0.274 (n=1881)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1761.9 (IC base=+0.265)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.272 (n=969)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.265)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.184 (n=1085)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.003 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.1041` → IC=+0.154 (n=1430)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1041 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=3390)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.2145` → IC=+0.193 (n=3250)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.2145 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.3171` → IC=+0.202 (n=1099)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3171 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.447` → IC=+0.156 (n=682)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 9.447 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.088` → IC=+0.140 (n=2855)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 3.088 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.6358` → IC=+0.161 (n=1085)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.6358 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `1.0731` → IC=+0.142 (n=1474)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.0731 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` < `0.0723` → IC=+0.142 (n=2907)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` < 0.0723 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2723` → IC=+0.176 (n=464)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2723 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.1566` → IC=+0.147 (n=2804)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.1566 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.5212` → IC=+0.142 (n=2848)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.5212 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `425.0` → IC=+0.149 (n=3126)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 425.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.159 (n=2794)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0062 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.0785` → IC=+0.174 (n=931)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0785 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.166 (n=1020)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.6844` → IC=+0.184 (n=2791)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6844 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.1374` → IC=+0.151 (n=2674)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1374 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.846` → IC=+0.149 (n=462)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 10.846 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `1.1907` → IC=+0.145 (n=2791)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.1907 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.2185` → IC=+0.192 (n=520)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2185 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `1.4125` → IC=+0.142 (n=895)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4125 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.7762` → IC=+0.141 (n=1790)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.7762 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=3622)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `317.0` → IC=+0.140 (n=1731)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 317.0 (IC base=+0.135)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.254 (n=1108)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0128 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=3480)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=2975)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=1243)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.184` → IC=+0.323 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.184 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` < `0.1313` → IC=+0.227 (n=3132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1313 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `3.2286` → IC=+0.240 (n=1080)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2286 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.231 (n=3980)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `1933.3484` → IC=+0.239 (n=1506)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1933.3484 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.248 (n=2775)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0109 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.179` → IC=+0.263 (n=1389)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.179 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.265 (n=1196)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.243 (n=1436)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.0526` → IC=+0.305 (n=1053)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0526 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.34` → IC=+0.303 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.34 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.3493` → IC=+0.308 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3493 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `2.1588` → IC=+0.257 (n=2016)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1588 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.249 (n=1625)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `1914.9372` → IC=+0.253 (n=1430)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1914.9372 (IC base=+0.242)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.249 (n=2593)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.242)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.186 (n=1522)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0041 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.4291` → IC=+0.149 (n=3445)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.4291 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=3582)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.8983` → IC=+0.277 (n=1148)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8983 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.1937` → IC=+0.167 (n=1595)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1937 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.963` → IC=+0.155 (n=1544)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 2.963 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.8602` → IC=+0.154 (n=2297)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8602 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2336` → IC=+0.185 (n=607)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2336 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.5208` → IC=+0.156 (n=1481)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.5208 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `7297.3713` → IC=+0.239 (n=1148)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7297.3713 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.151 (n=1470)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 69.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.158 (n=2878)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0077 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.4388` → IC=+0.148 (n=2877)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.4388 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.165 (n=1057)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.7163` → IC=+0.193 (n=2877)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.7163 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1476` → IC=+0.150 (n=2656)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1476 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.982` → IC=+0.166 (n=429)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 10.982 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.6904` → IC=+0.155 (n=1266)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6904 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.295` → IC=+0.223 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.295 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.2207` → IC=+0.140 (n=2442)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.2207 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.5369` → IC=+0.147 (n=2479)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.5369 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `6189.7409` → IC=+0.212 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6189.7409 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `95.0` → IC=+0.146 (n=1886)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 95.0 (IC base=+0.138)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.152 (n=1586)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.011 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.152 (n=2469)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 11.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `0.4333` → IC=+0.193 (n=3487)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.4333 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `1.0088` → IC=+0.207 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0088 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.415` → IC=+0.267 (n=881)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.415 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.8783` → IC=+0.134 (n=2324)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8783 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.101` → IC=+0.124 (n=3305)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.101 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `2.4925` → IC=+0.122 (n=3404)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.4925 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.123 (n=3639)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2692.1276` → IC=+0.244 (n=1162)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2692.1276 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.130 (n=1127)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 21.0 (IC base=+0.120)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.154 (n=2898)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0106 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.136` → IC=+0.152 (n=1099)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.136 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.155 (n=1547)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 15.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.210 (n=3307)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6667 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` < `0.2141` → IC=+0.140 (n=2948)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.2141 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.125` → IC=+0.145 (n=3168)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 3.125 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.6386` → IC=+0.149 (n=1098)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6386 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2255` → IC=+0.170 (n=577)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2255 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.4357` → IC=+0.155 (n=1037)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.4357 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2577.7485` → IC=+0.200 (n=1097)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2577.7485 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.133 (n=3103)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 51.0 (IC base=+0.122)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0139` → IC=+0.258 (n=2885)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0139 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.241 (n=3374)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.240 (n=2896)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` > `0.615` → IC=+0.272 (n=2886)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.615 (IC base=+0.236)

- **PATRÓN** `dist_vwap_pct` > `0.1902` → IC=+0.252 (n=1704)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1902 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.272` → IC=+0.283 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.272 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` < `1.2213` → IC=+0.240 (n=3229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2213 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` > `0.6434` → IC=+0.240 (n=3230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6434 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2371` → IC=+0.260 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2371 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.5001` → IC=+0.256 (n=1051)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5001 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `2936.2954` → IC=+0.242 (n=1077)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2936.2954 (IC base=+0.236)

- **PATRÓN** `sigma_h` > `0.0258` → IC=+0.262 (n=1109)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0258 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.244 (n=3141)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.5214` → IC=+0.271 (n=3325)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5214 (IC base=+0.239)

- **PATRÓN** `dist_vwap_pct` < `0.2159` → IC=+0.245 (n=3131)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2159 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.18` → IC=+0.279 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.18 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` > `1.2151` → IC=+0.260 (n=1109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2151 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2859` → IC=+0.305 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2859 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.8121` → IC=+0.237 (n=2080)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8121 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `1.4285` → IC=+0.240 (n=3120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4285 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.237 (n=3054)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.239)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.199 (n=5633)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.245 (n=1930)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.5011` → IC=+0.224 (n=5778)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5011 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.230 (n=2099)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.9346` → IC=+0.254 (n=1927)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9346 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` < `0.4234` → IC=+0.219 (n=4194)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4234 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.856` → IC=+0.223 (n=950)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.856 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.564` → IC=+0.216 (n=5140)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.564 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` < `0.7071` → IC=+0.227 (n=1878)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7071 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `0.883` → IC=+0.218 (n=2845)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.883 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` < `0.1053` → IC=+0.217 (n=5393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1053 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.1654` → IC=+0.222 (n=1632)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1654 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `1.4524` → IC=+0.224 (n=1896)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4524 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.223 (n=4526)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `3717.9096` → IC=+0.226 (n=3852)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3717.9096 (IC base=+0.216)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.238 (n=1415)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.49` → IC=+0.212 (n=4237)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.49 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=1433)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.212 (n=1883)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` < `0.7304` → IC=+0.205 (n=4238)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7304 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.6483` → IC=+0.209 (n=730)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6483 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` < `0.1763` → IC=+0.194 (n=3756)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1763 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.79` → IC=+0.208 (n=3790)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.79 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` < `1.0967` → IC=+0.203 (n=3550)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0967 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.199 (n=3895)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.2231` → IC=+0.202 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2231 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` < `1.5347` → IC=+0.203 (n=1837)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5347 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `2.1901` → IC=+0.206 (n=1893)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1901 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.199 (n=5633)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `ballena_activa_n` < `171.0` → IC=+0.208 (n=3665)

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

- **PATRÓN** `volumen_spike_ratio` < `1.5242` → IC=+0.268 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5242 (IC base=+0.265)

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
- **PATRÓN** `drift_60min` |x|≤ `0.5868` → IC=+0.203 (n=862)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5868 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.233 (n=328)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` < `0.7078` → IC=+0.197 (n=575)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.7078 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.239 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.494` → IC=+0.241 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.494 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.2084` → IC=+0.239 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2084 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `1.8072` → IC=+0.204 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8072 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `2760.165` → IC=+0.227 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2760.165 (IC base=+0.195)

- **PATRÓN** `ballena_activa_n` < `5.0` → IC=+0.198 (n=385)

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
- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.219 (n=1600)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.4526` → IC=+0.214 (n=1600)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4526 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.224 (n=566)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` < `0.4986` → IC=+0.221 (n=1067)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4986 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` < `0.3965` → IC=+0.216 (n=1606)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3965 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.019` → IC=+0.214 (n=1455)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.019 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `0.707` → IC=+0.212 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.707 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` < `0.1034` → IC=+0.210 (n=1475)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1034 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `2.4455` → IC=+0.214 (n=1567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4455 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=1662)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.240 (n=441)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.4841` → IC=+0.217 (n=1315)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4841 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.208 (n=502)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.211 (n=886)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` < `0.4019` → IC=+0.200 (n=877)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4019 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `0.089` → IC=+0.201 (n=1315)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.089 (IC base=+0.196)

- **PATRÓN** `dist_vwap_pct` > `0.6243` → IC=+0.212 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6243 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.353` → IC=+0.199 (n=1195)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.353 (IC base=+0.196)

- **PATRÓN** `volumen_regimen` < `0.6401` → IC=+0.223 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6401 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.074` → IC=+0.227 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.074 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` < `2.1981` → IC=+0.203 (n=1134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1981 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `2.524` → IC=+0.199 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.524 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `6511.755` → IC=+0.202 (n=1175)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6511.755 (IC base=+0.196)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.215 (n=587)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0096 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.227 (n=594)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.271 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.189)

- **PATRÓN** `dist_vwap_pct` > `0.7224` → IC=+0.236 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7224 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.242` → IC=+0.219 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.242 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` < `0.6386` → IC=+0.236 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6386 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` < `0.1058` → IC=+0.200 (n=788)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1058 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.0795` → IC=+0.194 (n=394)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0795 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` < `1.5721` → IC=+0.198 (n=376)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.5721 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `1.4783` → IC=+0.195 (n=855)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4783 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.198 (n=1037)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.02 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `3561.855` → IC=+0.220 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3561.855 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.218 (n=285)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.216)

- **PATRÓN** `sigma_h` > `0.0116` → IC=+0.219 (n=293)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0116 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.5959` → IC=+0.238 (n=646)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5959 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.247 (n=452)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` < `0.7347` → IC=+0.241 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7347 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `0.4989` → IC=+0.223 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4989 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` < `0.3028` → IC=+0.218 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3028 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.893` → IC=+0.220 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.893 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.823` → IC=+0.225 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.823 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `0.6739` → IC=+0.218 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6739 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` < `0.106` → IC=+0.230 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.106 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `2.1939` → IC=+0.253 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1939 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `2968.4304` → IC=+0.235 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2968.4304 (IC base=+0.216)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.254 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.216)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.152 (n=671)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0036 (IC base=+0.057)

- **PATRÓN** `ibs_20min` > `0.3793` → IC=+0.126 (n=1904)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` > 0.3793 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` > `0.1458` → IC=+0.140 (n=957)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.1458 (IC base=+0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.606` → IC=+0.146 (n=416)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 10.606 (IC base=+0.057)

- **PATRÓN** `ibs_20min` < `0.0476` → IC=+0.262 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0476 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.1456` → IC=+0.134 (n=342)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.1456 (IC base=+0.042)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.126 (n=643)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0059 (IC base=+0.079)

- **PATRÓN** `ibs_20min` > `0.3736` → IC=+0.158 (n=612)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.3736 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` > `0.1188` → IC=+0.174 (n=299)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.1188 (IC base=+0.079)

- **PATRÓN** `ibs_20min` < `0.0659` → IC=+0.281 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0659 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.2162` → IC=+0.167 (n=100)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2162 (IC base=+0.050)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.154 (n=218)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0034 (IC base=+0.075)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.126 (n=319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 15.0 (IC base=+0.075)

- **PATRÓN** `ibs_20min` > `0.7791` → IC=+0.224 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7791 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` > `0.1265` → IC=+0.175 (n=309)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.1265 (IC base=+0.075)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.646` → IC=+0.206 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.646 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.0314` → IC=+0.256 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0314 (IC base=+0.013)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.200 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.7076` → IC=+0.135 (n=154)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.7076 (IC base=+0.021)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.754` → IC=+0.132 (n=142)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 8.754 (IC base=+0.021)

- **PATRÓN** `sigma_h` < `0.0089` → IC=+0.192 (n=238)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0089 (IC base=+0.062)

- **PATRÓN** `ibs_20min` < `0.4545` → IC=+0.172 (n=327)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.4545 (IC base=+0.062)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.928` → IC=+0.300 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.928 (IC base=+0.062)

- **PATRÓN** `volumen_regimen` > `1.1045` → IC=+0.176 (n=109)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.1045 (IC base=+0.062)

- **PATRÓN** `volumen_pendiente_norm` > `0.078` → IC=+0.142 (n=149)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.078 (IC base=+0.062)

- **PATRÓN** `volumen_spike_ratio` > `1.8302` → IC=+0.131 (n=201)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.8302 (IC base=+0.062)

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

- **FILTRO** `ibs_20min` > `0.8119` → IC=-0.325 (n=78)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8119
  - _Potencial_: sin este filtro IC_bueno=-0.276 (n=235)

- **FILTRO** `dist_vwap_pct` > `0.3644` → IC=-0.406 (n=30)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3644
  - _Potencial_: sin este filtro IC_bueno=-0.275 (n=283)

- **FILTRO** `sigma_ewma_delta_pct` > `9.955` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.955
  - _Potencial_: sin este filtro IC_bueno=-0.285 (n=286)

- **FILTRO** `volumen_pendiente_norm` > `0.0453` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0453
  - _Potencial_: sin este filtro IC_bueno=-0.277 (n=195)

- **FILTRO** `libro_liquidez` < `1718.0229` → IC=-0.309 (n=103)

  - _Acción_: SKIP cuando `libro_liquidez` < 1718.0229
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=210)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `volumen_regimen` < `1.2266` → IC=-0.296 (n=52)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2266
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=52)

- **FILTRO** `sigma_h` < `0.004` → IC=-0.268 (n=93)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.004
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=48)

- **FILTRO** `ibs_20min` > `0.7634` → IC=-0.255 (n=47)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7634
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=94)

- **FILTRO** `volumen_regimen` > `0.805` → IC=-0.311 (n=35)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=106)

- **FILTRO** `libro_liquidez` < `4992.5113` → IC=-0.258 (n=93)

  - _Acción_: SKIP cuando `libro_liquidez` < 4992.5113
  - _Potencial_: sin este filtro IC_bueno=-0.240 (n=48)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` < `0.0027` → IC=-0.293 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0027
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=87)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.328 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=87)

- **FILTRO** `volumen_regimen` < `0.7435` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7435
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=86)

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

- **FILTRO** `dist_vwap_pct` < `0.238` → IC=-0.352 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.238
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=25)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.2696` → IC=-0.161 (n=240)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2696
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=723)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.191 (n=318)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 15.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `0.6686` → IC=+0.177 (n=618)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.6686 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.5399` → IC=+0.256 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5399 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.607` → IC=+0.138 (n=338)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 3.607 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.663` → IC=+0.139 (n=566)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 5.663 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.6225` → IC=+0.183 (n=206)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6225 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` < `0.2099` → IC=+0.164 (n=572)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` < 0.2099 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.4169` → IC=+0.160 (n=513)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.4169 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.784` → IC=+0.154 (n=209)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 8.784 (IC base=+0.033)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.7055` → IC=-0.172 (n=59)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7055
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=184)

- **PATRÓN** `dist_vwap_pct` > `0.5497` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5497 (IC base=+0.018)

- **PATRÓN** `ibs_20min` < `0.2374` → IC=+0.171 (n=338)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.2374 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.801` → IC=+0.144 (n=102)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 9.801 (IC base=+0.095)

- **PATRÓN** `volumen_pendiente_norm` > `0.2251` → IC=+0.138 (n=67)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.2251 (IC base=+0.095)

- **PATRÓN** `volumen_spike_ratio` > `1.7729` → IC=+0.131 (n=204)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.7729 (IC base=+0.095)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1261` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1261
  - _Potencial_: sin este filtro IC_bueno=+0.177 (n=196)

- **FILTRO** `ibs_20min` > `0.156` → IC=-0.141 (n=115)

  - _Acción_: SKIP cuando `ibs_20min` > 0.156
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=225)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=115)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.288 (n=168)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` > `0.6818` → IC=+0.275 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6818 (IC base=+0.233)

- **PATRÓN** `dist_vwap_pct` > `0.6667` → IC=+0.389 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6667 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.832` → IC=+0.340 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.832 (IC base=+0.233)

- **PATRÓN** `volumen_regimen` < `0.5837` → IC=+0.290 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5837 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.0951` → IC=+0.298 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0951 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.4665` → IC=+0.315 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4665 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.308` → IC=+0.274 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.308 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `755.5073` → IC=+0.231 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 755.5073 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.977` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.977 (IC base=-0.066)

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
- **PATRÓN** `libro_liquidez` > `2928.7278` → IC=+0.132 (n=498)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2928.7278 (IC base=+0.101)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2928.7278` → IC=+0.132 (n=498)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2928.7278 (IC base=+0.101)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=224)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=224)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=523)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `4006.09` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `liq_usd_total` < 4006.09
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=26)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=35)

- **PATRÓN** `liq_n` > `2.0` → IC=+0.129 (n=95)

  - _Acción_: Kelly boost +0.64€ cuando `liq_n` > 2.0 (IC base=+0.055)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.138 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 8.0 (IC base=+0.055)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=3820)

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
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=1535)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=1489)

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
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=930)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=930)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=1069)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=1069)

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

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=350)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=285)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=381)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=381)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=226)

- **FILTRO** `libro_liquidez` < `654.8772` → IC=-0.142 (n=135)

  - _Acción_: SKIP cuando `libro_liquidez` < 654.8772
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=276)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=308)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `restante_min` < `10.72` → IC=-0.145 (n=29)

  - _Acción_: SKIP cuando `restante_min` < 10.72
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=60)

- **FILTRO** `lag_apertura_s` > `255.1` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `lag_apertura_s` > 255.1
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=59)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.202 (n=65)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=80)

- **FILTRO** `py_entrada` > `0.52` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `py_entrada` > 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=25)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.250 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=49)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.51` → IC=+0.148 (n=268)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.51 (IC base=+0.001)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` > `0.61` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=176)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.125 (n=142)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=572)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.139 (n=286)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=303)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.172 (n=126)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=533)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.145 (n=260)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=538)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.174 (n=6986)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=22522)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.177 (n=7402)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=22937)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.190 (n=1314)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=4112)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.175 (n=1255)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=4133)

- **PATRÓN** `libro_liquidez` > `1043.3164` → IC=+0.140 (n=2713)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 1043.3164 (IC base=+0.042)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.124 (n=2782)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.505 (IC base=+0.012)

- **PATRÓN** `libro_liquidez` > `1140.6472` → IC=+0.150 (n=1832)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1140.6472 (IC base=+0.012)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.183 (n=1047)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=3238)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.206 (n=1324)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=4190)

- **PATRÓN** `ibs_20min` > `0.9643` → IC=+0.130 (n=1852)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.9643 (IC base=+0.035)

- **PATRÓN** `libro_liquidez` > `1739.0784` → IC=+0.122 (n=1848)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1739.0784 (IC base=+0.035)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.155 (n=1356)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=4099)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2418)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=2342)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=3828)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.137 (n=1293)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=2523)

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
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=346)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.133 (n=156)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.120 (n=303)

- **FILTRO** `libro_liquidez` < `3193.0662` → IC=-0.186 (n=151)

  - _Acción_: SKIP cuando `libro_liquidez` < 3193.0662
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=308)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=954)

- **FILTRO** `libro_liquidez` < `1797.2058` → IC=-0.161 (n=243)

  - _Acción_: SKIP cuando `libro_liquidez` < 1797.2058
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=730)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.211 (n=278)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=839)

- **FILTRO** `libro_liquidez` < `1611.167` → IC=-0.164 (n=281)

  - _Acción_: SKIP cuando `libro_liquidez` < 1611.167
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=845)

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
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=45327)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.298 (n=15404)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=50047)

- **FILTRO** `ibs_7min` < `0.2273` → IC=-0.231 (n=16355)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2273
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=49096)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.152 (n=21857)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=43594)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.243 (n=20386)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=61729)

- **FILTRO** `ibs_7min` > `0.2834` → IC=-0.182 (n=20526)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2834
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=61589)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.154 (n=2834)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=8726)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.318 (n=2805)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=8755)

- **FILTRO** `ibs_7min` < `0.7115` → IC=-0.249 (n=3812)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7115
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=7748)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.150 (n=2686)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=8874)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.277 (n=3389)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=10810)

- **FILTRO** `ibs_7min` > `0.7715` → IC=-0.215 (n=3549)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7715
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=10650)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.262 (n=2610)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=8344)

- **FILTRO** `ibs_7min` < `0.7184` → IC=-0.205 (n=2738)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7184
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=8216)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.194 (n=2728)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=8226)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.261 (n=2785)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=8394)

- **FILTRO** `ibs_7min` > `0.2664` → IC=-0.192 (n=2793)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2664
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=8386)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.181 (n=2781)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=8398)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.163 (n=2682)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=8384)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.315 (n=2763)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=8303)

- **FILTRO** `ibs_7min` < `0.2892` → IC=-0.248 (n=3651)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2892
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=7415)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.197 (n=2353)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=8713)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.259 (n=3583)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=11450)

- **FILTRO** `ibs_7min` > `0.7308` → IC=-0.183 (n=3756)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7308
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=11277)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=2581)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=8026)

- **FILTRO** `ibs_7min` < `0.7204` → IC=-0.193 (n=2650)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7204
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=7957)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.187 (n=2643)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=7964)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.258 (n=2541)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=8529)

- **FILTRO** `ibs_7min` > `0.2751` → IC=-0.174 (n=2766)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2751
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=8304)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.168 (n=2765)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=8305)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.295 (n=2446)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=8136)

- **FILTRO** `ibs_7min` < `0.7083` → IC=-0.227 (n=3474)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7083
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=7108)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.222 (n=2474)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=8108)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.193 (n=3785)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=12063)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.127 (n=3419)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=7263)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.309 (n=2460)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=8222)

- **FILTRO** `ibs_7min` < `0.1818` → IC=-0.231 (n=2667)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1818
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=8015)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.202 (n=2474)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=8208)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.227 (n=3683)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=11103)

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
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=596)

- **FILTRO** `libro_liquidez` < `10474.9398` → IC=-0.153 (n=188)

  - _Acción_: SKIP cuando `libro_liquidez` < 10474.9398
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=566)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=873)

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

- **FILTRO** `libro_liquidez` < `3272.2118` → IC=-0.161 (n=187)

  - _Acción_: SKIP cuando `libro_liquidez` < 3272.2118
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=563)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4308` → IC=+0.151 (n=620)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio` |x|> 0.4308 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.134 (n=706)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 6.0 (IC base=+0.123)

- **PATRÓN** `total_vol_5m` < `422.987` → IC=+0.159 (n=455)

  - _Acción_: Kelly boost +0.79€ cuando `total_vol_5m` < 422.987 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `3558.8016` → IC=+0.141 (n=619)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3558.8016 (IC base=+0.123)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.177 (n=153)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 14.0 (IC base=+0.125)

- **PATRÓN** `total_vol_5m` < `372.075` → IC=+0.154 (n=281)

  - _Acción_: Kelly boost +0.77€ cuando `total_vol_5m` < 372.075 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2532.1776` → IC=+0.216 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2532.1776 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.126 (n=153)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 7.0 (IC base=+0.125)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.4307` → IC=+0.141 (n=129)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio` |x|> 0.4307 (IC base=+0.112)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.133 (n=265)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 15.0 (IC base=+0.112)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4162` → IC=+0.195 (n=175)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.97€ cuando `delta_ratio` |x|> 0.4162 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.153 (n=275)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 4.0 (IC base=+0.135)

- **PATRÓN** `total_vol_5m` < `507.685` → IC=+0.178 (n=175)

  - _Acción_: Kelly boost +0.89€ cuando `total_vol_5m` < 507.685 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `5173.4718` → IC=+0.136 (n=262)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 5173.4718 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.206 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 59.0 (IC base=+0.135)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.171 (n=238)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.85€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.190 (n=172)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 12.0 (IC base=+0.146)

- **PATRÓN** `total_vol_5m` < `4679.172` → IC=+0.183 (n=159)

  - _Acción_: Kelly boost +0.92€ cuando `total_vol_5m` < 4679.172 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `3694.6173` → IC=+0.158 (n=159)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3694.6173 (IC base=+0.146)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.126 (n=233)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 13.0 (IC base=+0.095)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=176)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.095)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.6638` → IC=-0.259 (n=52)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.6638
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=158)

- **FILTRO** `sigma_h` > `0.0074` → IC=-0.303 (n=191)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0074
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=575)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.177 (n=193)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0038 (IC base=-0.081)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `4.2538` → IC=-0.293 (n=56)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.2538
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=172)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.256 (n=76)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=-0.035)

- **PATRÓN** `pct_vs_K` |x|≤ `1.632` → IC=+0.154 (n=76)

  - _Acción_: Kelly boost +0.77€ cuando `pct_vs_K` |x|≤ 1.632 (IC base=-0.035)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `pct_vs_K` |x|> `2.327` → IC=-0.195 (n=57)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.327
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0102` → IC=-0.226 (n=71)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0102
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=73)

- **FILTRO** `T_h` < `91.7077` → IC=-0.176 (n=72)

  - _Acción_: SKIP cuando `T_h` < 91.7077
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=72)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0107` → IC=-0.232 (n=528)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0107
  - _Potencial_: sin este filtro IC_bueno=-0.126 (n=177)

- **FILTRO** `T_h` > `99.9926` → IC=-0.229 (n=352)

  - _Acción_: SKIP cuando `T_h` > 99.9926
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=353)

- **FILTRO** `sigma_h` > `0.0099` → IC=-0.255 (n=149)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0099
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=451)

- **FILTRO** `sigma_h` < `0.005` → IC=-0.217 (n=150)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=450)

- **FILTRO** `T_h` > `53.9646` → IC=-0.243 (n=449)

  - _Acción_: SKIP cuando `T_h` > 53.9646
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=151)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.009` → IC=-0.207 (n=172)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.009
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=59)

- **FILTRO** `T_h` > `143.7867` → IC=-0.250 (n=54)

  - _Acción_: SKIP cuando `T_h` > 143.7867
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=163)

- **FILTRO** `pct_vs_K` |x|> `2.6348` → IC=-0.380 (n=73)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.6348
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=144)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `sigma_h` < `0.0085` → IC=-0.250 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.327 (n=131)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.157 (n=68)

- **FILTRO** `T_h` > `99.3756` → IC=-0.292 (n=99)

  - _Acción_: SKIP cuando `T_h` > 99.3756
  - _Potencial_: sin este filtro IC_bueno=-0.245 (n=100)

- **FILTRO** `pct_vs_K` |x|> `3.3706` → IC=-0.458 (n=46)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.3706
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=139)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` < `0.0099` → IC=-0.184 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0099
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0082` → IC=-0.304 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0082
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=150)

- **FILTRO** `T_h` > `70.1391` → IC=-0.215 (n=149)

  - _Acción_: SKIP cuando `T_h` > 70.1391
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=50)

- **FILTRO** `sigma_h` > `0.0137` → IC=-0.330 (n=45)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0137
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=88)

- **FILTRO** `T_h` > `39.1242` → IC=-0.280 (n=89)

  - _Acción_: SKIP cuando `T_h` > 39.1242
  - _Potencial_: sin este filtro IC_bueno=-0.130 (n=44)

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

- **PATRÓN** `edge` > `0.1` → IC=+0.435 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1 (IC base=+0.407)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.428 (n=164)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.407)

- **PATRÓN** `T_h` < `0.6127` → IC=+0.442 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6127 (IC base=+0.407)

- **PATRÓN** `dist_50` > `0.3767` → IC=+0.444 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3767 (IC base=+0.407)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.472 (n=142)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.407)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1497` → IC=+0.256 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1497 (IC base=+0.202)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.271 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.202)

- **PATRÓN** `T_h` < `0.659` → IC=+0.382 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.659 (IC base=+0.202)

- **PATRÓN** `dist_50` > `0.3472` → IC=+0.281 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3472 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.294 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.202)

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
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=360)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=435)

- **PATRÓN** `streak_estiramiento` < `0.293` → IC=+0.167 (n=91)

  - _Acción_: Kelly boost +0.83€ cuando `streak_estiramiento` < 0.293 (IC base=+0.020)

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
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=18)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

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
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=4477)

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
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=2558)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.189 (n=1939)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0057 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.167 (n=1468)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0128 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.2104` → IC=+0.174 (n=4405)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2104 (IC base=+0.161)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3523` → IC=+0.170 (n=4059)

  - _Acción_: Kelly boost +0.85€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3523 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.167 (n=4655)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 4.0 (IC base=+0.161)

- **PATRÓN** `ibs_15` > `0.5122` → IC=+0.232 (n=4403)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5122 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.1301` → IC=+0.156 (n=2090)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1301 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.686` → IC=+0.267 (n=846)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.686 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `5210.4456` → IC=+0.181 (n=1468)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 5210.4456 (IC base=+0.161)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=1740)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.247 (n=314)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.0592` → IC=+0.254 (n=238)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0592 (IC base=+0.204)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2654` → IC=+0.224 (n=237)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2654 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.224 (n=743)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.204)

- **PATRÓN** `ibs_15` > `0.7141` → IC=+0.280 (n=712)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7141 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.3722` → IC=+0.223 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3722 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` < `0.1096` → IC=+0.204 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1096 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.92` → IC=+0.311 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.92 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `8052.1794` → IC=+0.213 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8052.1794 (IC base=+0.204)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.156 (n=871)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0068 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.1507` → IC=+0.149 (n=767)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.1507 (IC base=+0.135)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1428` → IC=+0.136 (n=581)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio_macro` |x|> 0.1428 (IC base=+0.135)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2833` → IC=+0.139 (n=701)

  - _Acción_: Kelly boost +0.69€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2833 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.144 (n=795)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 6.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.139 (n=914)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 17.0 (IC base=+0.135)

- **PATRÓN** `ibs_15` > `0.5034` → IC=+0.226 (n=871)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5034 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.1187` → IC=+0.149 (n=545)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1187 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.4301` → IC=+0.137 (n=926)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.4301 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.063` → IC=+0.284 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.063 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `5810.9052` → IC=+0.165 (n=395)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 5810.9052 (IC base=+0.135)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8727` → IC=+0.220 (n=370)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8727 (IC base=+0.079)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.128 (n=549)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.079)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0194` → IC=+0.191 (n=667)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0194 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.186 (n=893)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0151 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.2079` → IC=+0.195 (n=1000)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.2079 (IC base=+0.182)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3508` → IC=+0.210 (n=898)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3508 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.189 (n=893)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 14.0 (IC base=+0.182)

- **PATRÓN** `ibs_15` > `0.5854` → IC=+0.280 (n=893)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5854 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `0.4987` → IC=+0.220 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4987 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.462` → IC=+0.231 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.462 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `2333.5562` → IC=+0.203 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2333.5562 (IC base=+0.182)

- **PATRÓN** `ibs_15` < `0.1081` → IC=+0.168 (n=853)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.84€ cuando `ibs_15` < 0.1081 (IC base=+0.068)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.388 (n=318)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1503` → IC=+0.379 (n=467)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1503 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1074` → IC=+0.384 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1074 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.376 (n=701)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.8308` → IC=+0.405 (n=626)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8308 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.1521` → IC=+0.383 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1521 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.159` → IC=+0.397 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.159 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.370 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `3489.2833` → IC=+0.372 (n=701)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3489.2833 (IC base=+0.365)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.367 (n=118)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.156` → IC=+0.369 (n=235)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.156 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1441` → IC=+0.394 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1441 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.379 (n=329)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.8077` → IC=+0.387 (n=353)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8077 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.3743` → IC=+0.387 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3743 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.166` → IC=+0.386 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.166 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `9172.6877` → IC=+0.377 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9172.6877 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `489.0` → IC=+0.404 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 489.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.366 (n=350)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.367)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.385 (n=232)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.367)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0842` → IC=+0.379 (n=311)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0842 (IC base=+0.367)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.380 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.367)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.379 (n=163)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.367)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.376 (n=159)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.367)

- **PATRÓN** `ibs_15` > `0.814` → IC=+0.404 (n=311)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.814 (IC base=+0.367)

- **PATRÓN** `dist_vwap_pct` > `0.1227` → IC=+0.376 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1227 (IC base=+0.367)

- **PATRÓN** `dist_vwap_pct` < `0.2918` → IC=+0.370 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2918 (IC base=+0.367)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.408` → IC=+0.406 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.408 (IC base=+0.367)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.372 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.367)

- **PATRÓN** `libro_liquidez` > `4039.5603` → IC=+0.394 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4039.5603 (IC base=+0.367)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.01` → IC=-0.215 (n=1644)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=3192)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.214 (n=1945)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=2891)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1387` → IC=+0.221 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1387 (IC base=-0.073)

- **PATRÓN** `ibs_15` > `0.6326` → IC=+0.281 (n=1134)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6326 (IC base=-0.073)

- **PATRÓN** `dist_vwap_pct` > `0.1122` → IC=+0.203 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1122 (IC base=-0.073)

- **PATRÓN** `dist_vwap_pct` < `0.4229` → IC=+0.200 (n=1116)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4229 (IC base=-0.073)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2339` → IC=+0.268 (n=1430)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2339 (IC base=-0.008)

- **PATRÓN** `ibs_15` < `0.3679` → IC=+0.283 (n=4289)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3679 (IC base=-0.008)

- **PATRÓN** `dist_vwap_pct` > `0.8693` → IC=+0.276 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8693 (IC base=-0.008)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0325` → IC=-0.223 (n=2275)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0325
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=761)

- **FILTRO** `sigma_h` < `0.0036` → IC=-0.221 (n=759)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0036
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=2277)

- **FILTRO** `sigma_ewma_delta_pct` > `22.67` → IC=-0.264 (n=435)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.67
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=2601)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.157 (n=295)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0029 (IC base=+0.077)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1441` → IC=+0.273 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1441 (IC base=+0.077)

- **PATRÓN** `ibs_15` > `0.7639` → IC=+0.330 (n=385)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7639 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` > `0.1051` → IC=+0.282 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1051 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` < `0.3658` → IC=+0.285 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3658 (IC base=+0.077)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.479` → IC=+0.149 (n=257)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 18.479 (IC base=+0.077)

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
  - _Potencial_: sin este filtro IC_bueno=+0.157 (n=738)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.161 (n=500)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0058 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.0733` → IC=+0.188 (n=251)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0733 (IC base=+0.150)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.194 (n=439)

  - _Acción_: Kelly boost +0.97€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.168 (n=410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 11.0 (IC base=+0.150)

- **PATRÓN** `ibs_15` > `0.5784` → IC=+0.243 (n=567)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5784 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.4658` → IC=+0.158 (n=147)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.4658 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.1604` → IC=+0.155 (n=442)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1604 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.049` → IC=+0.259 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.049 (IC base=+0.150)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=738)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `9459.3828` → IC=+0.154 (n=189)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 9459.3828 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.263 (n=543)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.1028` → IC=+0.241 (n=543)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1028 (IC base=+0.241)

- **PATRÓN** `drift_15min` |x|≤ `0.7694` → IC=+0.255 (n=1432)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7694 (IC base=+0.241)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1556` → IC=+0.258 (n=1086)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1556 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.245 (n=602)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.247 (n=610)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.241)

- **PATRÓN** `ibs_15` < `0.3774` → IC=+0.274 (n=1627)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3774 (IC base=+0.241)

- **PATRÓN** `dist_vwap_pct` > `0.6` → IC=+0.269 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.294` → IC=+0.246 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.294 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.226` → IC=+0.247 (n=1697)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.226 (IC base=+0.241)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0474` → IC=-0.207 (n=832)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0474
  - _Potencial_: sin este filtro IC_bueno=-0.129 (n=278)

- **FILTRO** `drift_60min` |x|> `0.1716` → IC=-0.246 (n=376)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1716
  - _Potencial_: sin este filtro IC_bueno=-0.158 (n=734)

- **FILTRO** `drift_15min` |x|> `0.8922` → IC=-0.278 (n=277)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8922
  - _Potencial_: sin este filtro IC_bueno=-0.158 (n=833)

- **FILTRO** `sigma_ewma_delta_pct` > `6.331` → IC=-0.202 (n=260)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.331
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=850)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.188)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.188)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1292 (IC base=-0.188)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=-0.188)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0653` → IC=+0.223 (n=732)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0653 (IC base=-0.034)

- **PATRÓN** `ibs_15` < `0.3939` → IC=+0.292 (n=733)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3939 (IC base=-0.034)

- **PATRÓN** `dist_vwap_pct` < `0.1929` → IC=+0.238 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1929 (IC base=-0.034)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0562` → IC=-0.230 (n=997)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0562
  - _Potencial_: sin este filtro IC_bueno=-0.157 (n=333)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.247 (n=622)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=708)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.212)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.212)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1153` → IC=+0.277 (n=643)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1153 (IC base=-0.024)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1182` → IC=+0.291 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1182 (IC base=-0.024)

- **PATRÓN** `ibs_15` < `0.1351` → IC=+0.308 (n=643)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1351 (IC base=-0.024)

- **PATRÓN** `dist_vwap_pct` > `0.768` → IC=+0.342 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.768 (IC base=-0.024)

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
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.291 (n=1230)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.0543` → IC=+0.318 (n=410)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0543 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1507` → IC=+0.288 (n=819)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1507 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.223` → IC=+0.298 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.223 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.303 (n=1275)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.8395` → IC=+0.317 (n=1230)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8395 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.2663` → IC=+0.317 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2663 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.199` → IC=+0.379 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.199 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `13580.5333` → IC=+0.308 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13580.5333 (IC base=+0.287)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.310 (n=219)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.0593` → IC=+0.319 (n=219)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0593 (IC base=+0.281)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2214` → IC=+0.283 (n=297)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2214 (IC base=+0.281)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3892` → IC=+0.287 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3892 (IC base=+0.281)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.301 (n=685)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.281)

- **PATRÓN** `ibs_15` > `0.8292` → IC=+0.308 (n=654)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8292 (IC base=+0.281)

- **PATRÓN** `dist_vwap_pct` > `0.2516` → IC=+0.314 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2516 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.503` → IC=+0.380 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.503 (IC base=+0.281)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.282 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `12498.3913` → IC=+0.306 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12498.3913 (IC base=+0.281)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.308 (n=576)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.1075` → IC=+0.314 (n=384)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1075 (IC base=+0.293)

- **PATRÓN** `delta_ratio_macro` |x|> `0.145` → IC=+0.295 (n=384)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.145 (IC base=+0.293)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.101` → IC=+0.344 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.101 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.309 (n=553)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.298 (n=524)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.293)

- **PATRÓN** `ibs_15` > `0.8745` → IC=+0.330 (n=514)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8745 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.2815` → IC=+0.319 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2815 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.513` → IC=+0.385 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.513 (IC base=+0.293)

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

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.326 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=12)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2685` → IC=-0.370 (n=21)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2685
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=12)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `sigma_h` < `0.0094` → IC=-0.167 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=18)

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
- **PATRÓN** `ratio` < `0.972` → IC=+0.399 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.972 (IC base=+0.179)

- **PATRÓN** `T_h` > `115.8544` → IC=+0.354 (n=2542)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 115.8544 (IC base=+0.336)

- **PATRÓN** `ratio` > `1.0213` → IC=+0.380 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0213 (IC base=+0.336)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `111.4342` → IC=+0.155 (n=236)

  - _Acción_: Kelly boost +0.78€ cuando `T_h` > 111.4342 (IC base=+0.146)

- **PATRÓN** `ratio` < `0.9802` → IC=+0.326 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9802 (IC base=+0.146)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.312 (n=898)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.299)

- **PATRÓN** `ratio` > `1.0429` → IC=+0.418 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0429 (IC base=+0.299)

### WEEKLY_PRICE#ETH
- **PATRÓN** `ratio` < `0.9854` → IC=+0.394 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.220)

- **PATRÓN** `T_h` > `111.9965` → IC=+0.355 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9965 (IC base=+0.323)

- **PATRÓN** `ratio` > `1.0083` → IC=+0.341 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0083 (IC base=+0.323)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0624` → IC=+0.432 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0624 (IC base=+0.398)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5122 sube el IC de +0.161 a +0.232 en UPDOWN_GBM#15min (n=4403). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7141 sube el IC de +0.204 a +0.280 en UPDOWN_GBM#BTC#15min (n=712). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5034 sube el IC de +0.135 a +0.226 en UPDOWN_GBM#ETH#15min (n=871). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.8727 sube el IC de +0.079 a +0.220 en UPDOWN_GBM#SOL#15min (n=370). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5854 sube el IC de +0.182 a +0.280 en UPDOWN_GBM#XRP#15min (n=893). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1081 sube el IC de +0.068 a +0.168 en UPDOWN_GBM#XRP#15min (n=853). Ya aplicado como kelly_boost=+0.84€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6326 sube el IC de -0.073 a +0.281 en UPDOWN_GBM_15M_TARDIO (n=1134). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3679 sube el IC de -0.008 a +0.283 en UPDOWN_GBM_15M_TARDIO (n=4289). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7639 sube el IC de +0.077 a +0.330 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=385). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6221 sube el IC de -0.188 a +0.319 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=70). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5784 sube el IC de +0.150 a +0.243 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=567). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3774 sube el IC de +0.241 a +0.274 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1627). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.188 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3939 sube el IC de -0.034 a +0.292 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=733). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.212 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.1351 sube el IC de -0.024 a +0.308 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=643). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.093 a +0.364 en UPDOWN_GBM_ETH_15M_HORA7 (n=20). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.093 a +0.364 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=20). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8395 sube el IC de +0.287 a +0.317 en UPDOWN_GBM_IBS_ALTO (n=1230). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8292 sube el IC de +0.281 a +0.308 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=654). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8745 sube el IC de +0.293 a +0.330 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=514). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.8308 sube el IC de +0.365 a +0.405 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=626). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8077 sube el IC de +0.362 a +0.387 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=353). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.814 sube el IC de +0.367 a +0.404 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=311). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

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
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 937 | -0.024 | +79.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 937 | -0.024 | +79.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 718 | -0.046 | +55.15€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 718 | -0.046 | +55.15€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 150 | +0.086 | +25.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 150 | +0.086 | +25.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 63 | -0.038 | -3.29€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 63 | -0.038 | -3.29€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 44405 | -0.085 | -5559.42€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2642 | +0.057 | -283.40€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 41763 | -0.094 | -5276.01€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4648 | -0.116 | -759.61€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4648 | -0.116 | -759.61€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2642 | +0.057 | -283.40€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2642 | +0.057 | -283.40€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4603 | -0.116 | -897.28€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4603 | -0.116 | -897.28€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 11966 | -0.029 | -1048.14€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 11966 | -0.029 | -1048.14€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 12021 | -0.120 | -1205.37€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 12021 | -0.120 | -1205.37€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8525 | -0.126 | -1365.61€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8525 | -0.126 | -1365.61€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 43144 | -0.013 | +3163.33€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 11132 | +0.005 | +1600.56€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 32012 | -0.019 | +1562.77€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 43144 | -0.013 | +3163.33€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 11132 | +0.005 | +1600.56€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 32012 | -0.019 | +1562.77€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 169971 | +0.114 | -6879.62€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 20613 | +0.181 | -668.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 767 | -0.003 | -77.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 138693 | +0.106 | -5779.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 9898 | +0.092 | -353.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 22980 | +0.106 | -1479.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 68 | -0.186 | +4.73€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 22897 | +0.107 | -1472.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 32528 | +0.125 | -517.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5529 | +0.180 | -221.86€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 22968 | +0.121 | -141.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3989 | +0.078 | -131.48€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 23034 | +0.099 | -1647.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 82 | -0.119 | -3.25€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 22937 | +0.100 | -1632.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 36233 | +0.124 | -708.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 9241 | +0.178 | -196.84€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 23317 | +0.106 | -450.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3663 | +0.101 | -52.55€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 32187 | +0.112 | -1513.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5614 | +0.199 | -257.18€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 670 | +0.025 | -23.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 23657 | +0.095 | -1063.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2246 | +0.104 | -169.56€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO#XRP | 23009 | +0.107 | -1013.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 79 | -0.117 | +5.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 22917 | +0.108 | -1018.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 27455 | +0.195 | -1780.16€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 27455 | +0.195 | -1780.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 6205 | +0.177 | -562.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 6205 | +0.177 | -562.82€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 3778 | +0.201 | -110.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 3778 | +0.201 | -110.28€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 6131 | +0.176 | -529.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 6131 | +0.176 | -529.39€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5224 | +0.249 | -187.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5224 | +0.249 | -187.12€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 6038 | +0.186 | -404.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 6038 | +0.186 | -404.31€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1153 | +0.425 | -42.44€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1153 | +0.425 | -42.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 468 | +0.438 | -4.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 468 | +0.438 | -4.97€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 462 | +0.427 | -14.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 462 | +0.427 | -14.73€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 209 | +0.396 | -18.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 209 | +0.396 | -18.87€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 96567 | +0.201 | -6950.72€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 96567 | +0.201 | -6950.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 16635 | +0.182 | -1790.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 16635 | +0.182 | -1790.07€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 15573 | +0.226 | -495.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 15573 | +0.226 | -495.74€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 16576 | +0.181 | -1739.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 16576 | +0.181 | -1739.61€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 15706 | +0.218 | -625.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 15706 | +0.218 | -625.78€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 15989 | +0.203 | -1031.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 15989 | +0.203 | -1031.99€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 16088 | +0.198 | -1267.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 16088 | +0.198 | -1267.53€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 37063 | +0.117 | +303.19€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 37063 | +0.117 | +303.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 18449 | +0.118 | +190.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 18449 | +0.118 | +190.32€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 18614 | +0.116 | +112.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 18614 | +0.116 | +112.87€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2360 | +0.294 | +3.32€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2360 | +0.294 | +3.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1077 | +0.283 | -17.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1077 | +0.283 | -17.67€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1152 | +0.299 | +19.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1152 | +0.299 | +19.03€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 131 | +0.335 | +1.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 131 | +0.335 | +1.96€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1080 | +0.445 | +11.02€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1080 | +0.445 | +11.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 521 | +0.439 | -2.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 521 | +0.439 | -2.00€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 511 | +0.451 | +12.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 511 | +0.451 | +12.15€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 48 | +0.400 | +0.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 48 | +0.400 | +0.86€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1843 | +0.068 | -82.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1118 | +0.081 | -18.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1409 | +0.075 | -37.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1118 | +0.081 | -18.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 74463 | +0.101 | -1794.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 5995 | +0.094 | +99.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 68468 | +0.101 | -1894.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 40778 | +0.106 | -405.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 5995 | +0.094 | +99.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 34783 | +0.108 | -504.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 15635 | +0.109 | -79.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 15635 | +0.109 | -79.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 18050 | +0.082 | -1309.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 18050 | +0.082 | -1309.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 912 | +0.186 | -109.79€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 912 | +0.186 | -109.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 912 | +0.186 | -109.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 912 | +0.186 | -109.79€ | 2 | 4 |
| ✅ GBM_LATE_15M | 50696 | +0.097 | +27682.85€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 50696 | +0.097 | +27682.85€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 8430 | +0.222 | +7154.79€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 8430 | +0.222 | +7154.79€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 7721 | +0.175 | +5982.72€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 7721 | +0.175 | +5982.72€ | 0 | 27 |
| ✅ GBM_LATE_15M#DOGE | 9095 | +0.205 | +7095.18€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 9095 | +0.205 | +7095.18€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 6924 | +0.048 | +2049.50€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 6924 | +0.048 | +2049.50€ | 1 | 18 |
| ✅ GBM_LATE_15M#SOL | 7088 | -0.032 | +1812.03€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 7088 | -0.032 | +1812.03€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 11438 | -0.026 | +3588.63€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 11438 | -0.026 | +3588.63€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 53592 | +0.085 | +30412.35€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 53592 | +0.085 | +30412.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 10438 | -0.000 | +5383.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 10438 | -0.000 | +5383.08€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 11451 | +0.005 | +2918.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 11451 | +0.005 | +2918.37€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 7353 | +0.288 | +8197.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 7353 | +0.288 | +8197.49€ | 0 | 23 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 10007 | +0.013 | +2992.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 10007 | +0.013 | +2992.25€ | 1 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 8328 | +0.041 | +3627.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 8328 | +0.041 | +3627.52€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 6015 | +0.313 | +7293.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 6015 | +0.313 | +7293.66€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 40210 | +0.179 | +32966.78€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 40210 | +0.179 | +32966.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 6059 | +0.238 | +5581.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 6059 | +0.238 | +5581.98€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 6375 | +0.141 | +4706.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 6375 | +0.141 | +4706.27€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 6458 | +0.225 | +5587.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 6458 | +0.225 | +5587.97€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 6862 | +0.132 | +5293.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 6862 | +0.132 | +5293.37€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 7590 | +0.120 | +5630.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 7590 | +0.120 | +5630.42€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 6866 | +0.231 | +6166.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 6866 | +0.231 | +6166.76€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 10643 | +0.124 | +5205.75€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 10643 | +0.124 | +5205.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 461 | +0.157 | +289.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 461 | +0.157 | +289.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3073 | +0.128 | +1659.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3073 | +0.128 | +1659.65€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 491 | +0.153 | +259.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 491 | +0.153 | +259.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3163 | +0.128 | +1539.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3163 | +0.128 | +1539.55€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2682 | +0.093 | +1030.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2682 | +0.093 | +1030.98€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 773 | +0.154 | +426.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 773 | +0.154 | +426.36€ | 0 | 28 |
| ✅ GBM_LATE_15M_TARDIO | 50934 | +0.186 | +41417.59€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 50934 | +0.186 | +41417.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 8049 | +0.247 | +7689.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 8049 | +0.247 | +7689.53€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 8054 | +0.138 | +5527.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 8054 | +0.138 | +5527.45€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 8632 | +0.233 | +7729.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 8632 | +0.233 | +7729.33€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 8427 | +0.139 | +6110.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 8427 | +0.139 | +6110.36€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 9034 | +0.121 | +6363.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 9034 | +0.121 | +6363.03€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 8738 | +0.238 | +7997.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 8738 | +0.238 | +7997.88€ | 0 | 21 |
| ✅ GBM_LATE_5M | 13351 | +0.208 | +10728.99€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 13351 | +0.208 | +10728.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3192 | +0.211 | +2758.98€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3192 | +0.211 | +2758.98€ | 0 | 26 |
| ✅ GBM_LATE_5M#DOGE | 1227 | +0.197 | +915.72€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1227 | +0.197 | +915.72€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 3886 | +0.201 | +2894.89€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3886 | +0.201 | +2894.89€ | 0 | 23 |
| ✅ GBM_LATE_5M#SOL | 2034 | +0.201 | +1623.92€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2034 | +0.201 | +1623.92€ | 0 | 26 |
| ✅ GBM_LATE_5M#XRP | 1958 | +0.209 | +1535.21€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1958 | +0.209 | +1535.21€ | 0 | 0 |
| ✅ GBM_LATE_60M | 4394 | +0.051 | +1220.09€ | 0 | 6 |
| ✅ GBM_LATE_60M#60min | 4394 | +0.051 | +1220.09€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1559 | +0.066 | +509.10€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1559 | +0.066 | +509.10€ | 0 | 5 |
| ✅ GBM_LATE_60M#ETH | 1425 | +0.051 | +437.09€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1425 | +0.051 | +437.09€ | 0 | 6 |
| ✅ GBM_LATE_60M#SOL | 1410 | +0.035 | +273.90€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1410 | +0.035 | +273.90€ | 0 | 9 |
| 🚫 GBM_LATE_60M_FADE | 653 | -0.250 | -32.35€ | 9 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 653 | -0.250 | -32.35€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 245 | -0.249 | -18.41€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 245 | -0.249 | -18.41€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 236 | -0.244 | -6.25€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 236 | -0.244 | -6.25€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 172 | -0.253 | -7.69€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 172 | -0.253 | -7.69€ | 6 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1786 | +0.080 | +445.47€ | 1 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1786 | +0.080 | +445.47€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 693 | +0.068 | +150.50€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 693 | +0.068 | +150.50€ | 1 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 608 | +0.056 | +107.82€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 608 | +0.056 | +107.82€ | 2 | 15 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 485 | +0.126 | +187.15€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 485 | +0.126 | +187.15€ | 1 | 10 |
| ✅ LATE_WINDOW_5MIN | 198 | +0.270 | +203.69€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 198 | +0.270 | +203.69€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 198 | +0.270 | +203.69€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 198 | +0.270 | +203.69€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4045 | +0.099 | +943.29€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4045 | +0.099 | +943.29€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4045 | +0.099 | +943.29€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4045 | +0.099 | +943.29€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 784 | -0.014 | +6.76€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 784 | -0.014 | +6.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 9 | -0.061 | -1.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 9 | -0.061 | -1.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 237 | -0.002 | +7.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 237 | -0.002 | +7.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 27 | -0.155 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 27 | -0.155 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 205 | +0.027 | +12.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 205 | +0.027 | +12.63€ | 2 | 2 |
| ✅ LIQUIDACIONES_15M#SOL | 254 | -0.004 | +2.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 254 | -0.004 | +2.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4043 | +0.017 | +105.66€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 4043 | +0.017 | +105.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 189 | +0.034 | +0.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 189 | +0.034 | +0.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 818 | +0.016 | +41.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 818 | +0.016 | +41.53€ | 1 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 216 | +0.000 | +1.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 216 | +0.000 | +1.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1587 | +0.022 | +30.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1587 | +0.022 | +30.94€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 763 | +0.011 | +1.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 763 | +0.011 | +1.66€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 470 | +0.015 | +29.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 470 | +0.015 | +29.46€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2094 | -0.039 | -27.23€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2094 | -0.039 | -27.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 629 | -0.033 | -13.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 629 | -0.033 | -13.76€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 731 | -0.016 | +9.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 731 | -0.016 | +9.18€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 734 | -0.068 | -22.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 734 | -0.068 | -22.65€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 12369 | -0.031 | -75.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 5930 | -0.034 | -77.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 6439 | -0.027 | +2.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 432 | -0.048 | -21.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 216 | -0.018 | +2.86€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 216 | -0.078 | -24.27€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 3203 | -0.020 | +27.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1525 | -0.021 | +12.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1678 | -0.020 | +14.85€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1277 | -0.021 | +33.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 650 | -0.032 | +2.25€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 627 | -0.010 | +31.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 2756 | -0.037 | -66.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1303 | -0.041 | -45.35€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1453 | -0.033 | -20.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 2381 | -0.030 | -10.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1151 | -0.037 | -20.74€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1230 | -0.024 | +10.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 2320 | -0.039 | -38.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1085 | -0.045 | -29.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1235 | -0.034 | -9.26€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 59847 | -0.000 | +3123.59€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 59847 | -0.000 | +3123.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 10814 | +0.027 | +1436.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 10814 | +0.027 | +1436.47€ | 2 | 3 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 8470 | -0.036 | -114.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 8470 | -0.036 | -114.54€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 10949 | +0.024 | +1137.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 10949 | +0.024 | +1137.38€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 8369 | -0.049 | -175.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 8369 | -0.049 | -175.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 10162 | -0.005 | +277.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 10162 | -0.005 | +277.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 11083 | +0.017 | +562.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 11083 | +0.017 | +562.69€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6964 | -0.056 | -133.25€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6964 | -0.056 | -133.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1239 | -0.002 | -17.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1239 | -0.002 | -17.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1908 | -0.069 | -34.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1908 | -0.069 | -34.40€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 67 | -0.007 | +0.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 67 | -0.007 | +0.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 793 | -0.119 | -33.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 793 | -0.119 | -33.68€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2099 | -0.069 | -22.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2099 | -0.069 | -22.55€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 858 | -0.016 | -26.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 858 | -0.016 | -26.02€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 147566 | -0.077 | +2003.89€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 147566 | -0.077 | +2003.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 25759 | -0.078 | +1380.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 25759 | -0.078 | +1380.83€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 22133 | -0.100 | -1068.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 22133 | -0.100 | -1068.70€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 26099 | -0.069 | +1253.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 26099 | -0.069 | +1253.97€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 21677 | -0.097 | -645.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 21677 | -0.097 | -645.33€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 26430 | -0.057 | +351.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 26430 | -0.057 | +351.92€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 25468 | -0.069 | +731.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 25468 | -0.069 | +731.21€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8950 | -0.035 | -185.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8950 | -0.035 | -185.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1002 | -0.017 | -19.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1002 | -0.017 | -19.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2062 | -0.047 | -28.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2062 | -0.047 | -28.58€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2624 | -0.026 | -39.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2624 | -0.026 | -39.96€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1250 | -0.062 | -33.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1250 | -0.062 | -33.73€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1003 | -0.030 | -32.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1003 | -0.030 | -32.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 1955 | +0.118 | +765.77€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1819 | +0.123 | +753.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 425 | +0.125 | +193.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 425 | +0.125 | +193.17€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 377 | +0.112 | +124.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 377 | +0.112 | +124.54€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 349 | +0.135 | +170.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 349 | +0.135 | +170.30€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 317 | +0.146 | +168.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 317 | +0.146 | +168.10€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 351 | +0.095 | +97.07€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 351 | +0.095 | +97.07€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1838 | -0.018 | -33.34€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1838 | -0.018 | -33.34€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 342 | +0.003 | +12.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 342 | +0.003 | +12.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 333 | -0.037 | -14.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 333 | -0.037 | -14.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 474 | -0.042 | -34.45€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 474 | -0.042 | -34.45€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 379 | +0.001 | +1.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 379 | +0.001 | +1.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 310 | -0.010 | +2.07€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 310 | -0.010 | +2.07€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1043 | -0.077 | -49.89€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 480 | -0.110 | -79.15€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 374 | -0.130 | -63.03€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 106 | -0.037 | -16.12€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 367 | -0.037 | +22.97€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 262 | -0.023 | +28.94€ | 1 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 105 | -0.070 | -5.97€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 196 | -0.071 | +6.29€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 162 | -0.073 | +3.43€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 34 | -0.056 | +2.86€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 798 | -0.084 | -30.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 245 | -0.055 | -19.23€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1305 | -0.210 | -88.06€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 509 | -0.210 | -50.80€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 448 | -0.211 | -48.53€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 61 | -0.198 | -2.27€ | 1 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 438 | -0.216 | -40.34€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 384 | -0.225 | -46.33€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 54 | -0.143 | +5.99€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 358 | -0.200 | +3.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 332 | -0.198 | +0.17€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 26 | -0.214 | +2.91€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1164 | -0.213 | -94.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 141 | -0.185 | +6.63€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 503 | +0.389 | +473.89€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 87 | +0.174 | +63.75€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 87 | +0.174 | +63.75€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#ETH | 116 | +0.364 | +102.68€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 116 | +0.364 | +102.68€ | 0 | 6 |
| ✅ RESOLUTION_SNIPER#SOL | 300 | +0.457 | +307.46€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 300 | +0.457 | +307.46€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 503 | +0.389 | +473.89€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 833 | +0.041 | +73.02€ | 2 | 4 |
| ✅ STREAK_FADE_15M#15min | 833 | +0.041 | +73.02€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 310 | +0.026 | +5.92€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 310 | +0.026 | +5.92€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 69 | +0.007 | +1.00€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 69 | +0.007 | +1.00€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 82 | +0.024 | +7.24€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 82 | +0.024 | +7.24€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 372 | +0.064 | +58.86€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 372 | +0.064 | +58.86€ | 0 | 4 |
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
| ✅ STREAK_FADE_60M | 111 | -0.040 | -7.85€ | 2 | 0 |
| ✅ STREAK_FADE_60M#60min | 111 | -0.040 | -7.85€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 43 | -0.100 | -5.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 43 | -0.100 | -5.07€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 68 | +0.000 | -2.78€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 68 | +0.000 | -2.78€ | 0 | 2 |
| ✅ STREAK_MOM_5M | 11397 | +0.015 | +78.33€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11397 | +0.015 | +78.33€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2949 | +0.018 | +25.53€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2949 | +0.018 | +25.53€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2959 | +0.018 | +37.45€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2959 | +0.018 | +37.45€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2910 | +0.009 | -1.79€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2910 | +0.009 | -1.79€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2579 | +0.013 | +17.14€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2579 | +0.013 | +17.14€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 10718 | +0.014 | -46.12€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 10718 | +0.014 | -46.12€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4496 | +0.019 | -4.80€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4496 | +0.019 | -4.80€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3630 | +0.010 | -28.88€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3630 | +0.010 | -28.88€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2592 | +0.010 | -12.44€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2592 | +0.010 | -12.44€ | 1 | 0 |
| ✅ UPDOWN_GBM | 91779 | +0.058 | +8630.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 22281 | +0.084 | +4849.66€ | 0 | 9 |
| ✅ UPDOWN_GBM#240min | 2867 | +0.001 | +30.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 60859 | +0.058 | +3658.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 5449 | +0.002 | +96.92€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 7564 | +0.101 | +1345.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1703 | +0.165 | +795.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5771 | +0.083 | +551.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 21023 | +0.057 | +1829.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3035 | +0.083 | +688.30€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 799 | +0.003 | +13.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 14619 | +0.065 | +1056.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2453 | -0.000 | +67.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 117 | -0.071 | +3.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 9821 | +0.076 | +1133.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1682 | +0.156 | +714.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 8053 | +0.060 | +419.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 21818 | +0.048 | +1488.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 5376 | +0.072 | +811.75€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 766 | +0.006 | +18.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 13568 | +0.049 | +631.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2000 | +0.005 | +25.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 108 | -0.109 | +1.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 19756 | +0.038 | +1128.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 5757 | +0.037 | +467.97€ | 0 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 729 | -0.010 | +2.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 12178 | +0.046 | +661.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 996 | +0.000 | +3.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 96 | -0.143 | -7.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 11795 | +0.071 | +1707.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4728 | +0.100 | +1371.61€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 6670 | +0.053 | +337.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 321 | -0.107 | -2.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 934 | +0.365 | +343.11€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 934 | +0.365 | +343.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 470 | +0.362 | +165.36€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 470 | +0.362 | +165.36€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 464 | +0.367 | +177.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 464 | +0.367 | +177.75€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 22513 | -0.022 | +5441.91€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 22513 | -0.022 | +5441.91€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1890 | -0.054 | +531.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1890 | -0.054 | +531.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 4213 | -0.114 | +201.68€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 4213 | -0.114 | +201.68€ | 3 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1021 | +0.222 | +857.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1021 | +0.222 | +857.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2924 | +0.217 | +1849.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2924 | +0.217 | +1849.66€ | 1 | 20 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 6369 | -0.061 | +898.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 6369 | -0.061 | +898.70€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 6096 | -0.065 | +1102.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 6096 | -0.065 | +1102.55€ | 2 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 270 | +0.062 | +25.25€ | 0 | 7 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 270 | +0.062 | +25.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 270 | +0.062 | +25.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 270 | +0.062 | +25.25€ | 0 | 7 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1639 | +0.287 | +1379.54€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1639 | +0.287 | +1379.54€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 872 | +0.281 | +688.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 872 | +0.281 | +688.63€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 767 | +0.293 | +690.91€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 767 | +0.293 | +690.91€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 845 | -0.114 | -84.20€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 845 | -0.114 | -84.20€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 259 | -0.086 | -20.70€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 259 | -0.086 | -20.70€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 94 | -0.167 | -10.43€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 94 | -0.167 | -10.43€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 109 | -0.176 | -3.72€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 109 | -0.176 | -3.72€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 4200 | +0.303 | +1949.34€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 1575 | +0.259 | +200.62€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1614 | +0.296 | +700.97€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1011 | +0.381 | +1047.75€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.028 n=1150 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1150 IC=+0.028 PNL=+63.44€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 767 celda(s) pasan gate riguroso completo de 2807 evaluadas (n>=40) y 3908 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.037 < 0.08 — monitorear
  - _Datos_: n=5753 IC=+0.037 PNL=+470.33€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1614/15 IC=+0.296 PNL=+700.97€ | BTC: n=1575/15 IC=+0.259 PNL=+200.62€ | SOL: n=1011/15 IC=+0.381 PNL=+1047.75€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.148 n=977/60 | contraria IC=+0.189 n=1008 | gap=-0.042 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=541, boost estimado=+0.016. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=2000/40 IC=+0.005 PNL=+25.62€ | BTC#60min: n=2453/40 IC=-0.000 PNL=+67.60€ | SOL#60min: n=996/40 IC=+0.000 PNL=+3.70€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.046 n=654155 | tras_1loss IC=+0.098 n=496608 | tras_2loss IC=+0.067 n=199775/40 | gap=-0.021 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.153 > 0.08 con n=1067 PNL=+563.09€
  - _Datos_: n=1067 IC=+0.153 PNL=+563.09€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.334 > 0.1 con n=3431 PNL=+1917.58€
  - _Datos_: n=3431 IC=+0.334 PNL=+1917.58€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=904 IC=+0.070 PNL=+91.66€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=904 IC=+0.070 PNL=+91.66€

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
  - _Estado_: n=3655 IC=+0.004 PNL=-5.71€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3655 IC=+0.004 PNL=-5.71€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1794 IC=-0.003 PNL=+102.63€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1794 IC=-0.003 PNL=+102.63€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1150 IC=+0.028 PNL=+63.44€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1150 IC=+0.028 PNL=+63.44€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.161 > 0.1 con n=5865 PNL=+3351.97€
  - _Datos_: n=5865 IC=+0.161 PNL=+3351.97€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=3031 IC=+0.083 PNL=+687.76€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=3031 IC=+0.083 PNL=+687.76€

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
  - _Estado_: n=1152 IC=+0.037 PNL=+95.76€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1152 IC=+0.037 PNL=+95.76€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=149 IC=+0.003 PNL=+0.04€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=149 IC=+0.003 PNL=+0.04€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.122 > 0.02 con n=1147 PNL=+474.13€
  - _Datos_: n=1147 IC=+0.122 PNL=+474.13€

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
  - _Estado_: n=37068 IC=+0.075 PNL=+5320.90€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=37068 IC=+0.075 PNL=+5320.90€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.137 < -0.1 con n=668 PNL=+91.55€
  - _Datos_: n=668 IC=-0.137 PNL=+91.55€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=3395 IC=+0.068 PNL=+451.07€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=3395 IC=+0.068 PNL=+451.07€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=170 IC=-0.122 PNL=-2.51€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=170 IC=-0.122 PNL=-2.51€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.106 > 0.1 con n=972 PNL=+250.67€
  - _Datos_: n=972 IC=+0.106 PNL=+250.67€

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
  - _Estado_: n=38681 IC=-0.136 PNL=+2631.01€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=38681 IC=-0.136 PNL=+2631.01€

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
  - _Estado_: n=3983 IC=+0.126 PNL=+2524.09€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=3983 IC=+0.126 PNL=+2524.09€

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
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.219 < -0.1 con n=4161 PNL=-331.97€
  - _Datos_: n=4161 IC=-0.219 PNL=-331.97€

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
  - _Estado_: n=84 IC=+0.046 PNL=+14.27€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=84 IC=+0.046 PNL=+14.27€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.096 n=2052) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2052 IC=+0.096 PNL=+417.02€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.410 n=644) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=644 IC=+0.410 PNL=+926.82€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=16629 IC=+0.182 PNL=-1790.40€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=16629 IC=+0.182 PNL=-1790.40€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.227 > 0.1 con n=262 PNL=+179.39€
  - _Datos_: n=262 IC=+0.227 PNL=+179.39€
