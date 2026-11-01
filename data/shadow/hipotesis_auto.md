# Hipótesis automáticas — 2026-11-01 18:55 UTC
_Generado por shadow_postmortem.py sobre 1150384 resoluciones (PNL=+154687.33€)_

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
- **FILTRO** `restante_s_al_confirmar` < `136.24` → IC=-0.215 (n=11096)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 136.24
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=33293)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `127.57` → IC=-0.258 (n=1162)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.57
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=3486)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `117.81` → IC=-0.303 (n=1150)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 117.81
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3452)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `156.75` → IC=-0.247 (n=3005)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 156.75
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=9015)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.212 (n=25092)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `8608.3515` → IC=+0.163 (n=2209)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 8608.3515 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.127 (n=21420)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=26075)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.225 (n=19792)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=7850)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6778.717` → IC=+0.150 (n=3033)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 6778.717 (IC base=+0.124)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=2164)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.364 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=2645)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `9415.8912` → IC=+0.182 (n=1841)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 9415.8912 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.187 (n=1884)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.183 (n=2104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` < `0.295` → IC=+0.312 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.295 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=2695)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `16115.8854` → IC=+0.186 (n=695)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 16115.8854 (IC base=+0.180)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.173 (n=539)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` > 0.61 (IC base=+0.076)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.141 (n=1278)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.44 (IC base=+0.080)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=4836)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.166 (n=4099)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 15.0 (IC base=+0.163)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.375 (n=1598)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.215 (n=2174)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.349 (n=784)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=2520)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=1228)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.150 (n=1041)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 15.0 (IC base=+0.143)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.260 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=981)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `3079.6088` → IC=+0.134 (n=230)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 3079.6088 (IC base=+0.070)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.255 (n=916)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1278)

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

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=21474)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.201 (n=18194)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.229 (n=8908)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.198)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.182 (n=2321)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.178 (n=4892)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 18.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.182 (n=4705)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.177 (n=4076)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.218 (n=2754)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.220 (n=2448)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.216)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.292 (n=927)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.216)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=4823)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.179 (n=4102)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.177 (n=5001)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=3754)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=4122)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.249 (n=3496)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.249)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.358 (n=1403)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=4736)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=4030)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.188 (n=3620)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.71 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=3521)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=28017)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.245 (n=28308)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.201)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.190 (n=4161)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 18.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.184 (n=8937)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 12.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.195 (n=12715)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=5838)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.288 (n=4023)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=4808)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.200 (n=9900)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.228 (n=3916)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.223 (n=4477)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.271 (n=3979)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.207 (n=10706)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.259 (n=4157)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=4660)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.201 (n=4634)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=4872)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=10004)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=10245)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.38` → IC=+0.139 (n=9289)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.38 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=4894)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.118)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.144 (n=4634)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=6127)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.118)

- **PATRÓN** `lag_apertura_s` < `2.67` → IC=+0.145 (n=4610)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 2.67 (IC base=+0.118)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.190 (n=5110)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=5611)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `3.24` → IC=+0.137 (n=6152)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.24 (IC base=+0.116)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.312 (n=1265)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.295)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.388 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.295)

- **PATRÓN** `libro_liquidez` > `3872.2908` → IC=+0.296 (n=803)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3872.2908 (IC base=+0.295)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.290 (n=849)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.283)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.364 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.283)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.324 (n=616)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.300)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.304 (n=897)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.300)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.398 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.300)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.300 (n=1022)

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

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.444 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.439)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4731` → IC=+0.138 (n=15735)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.4731 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.125 (n=15912)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.125 (n=10962)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.3747` → IC=+0.164 (n=15737)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.3747 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.775` → IC=+0.279 (n=874)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.775 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.586` → IC=+0.182 (n=7856)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 3.586 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `0.6226` → IC=+0.265 (n=4616)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6226 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.3033` → IC=+0.243 (n=1611)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3033 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` > `2.3504` → IC=+0.228 (n=5099)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3504 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=7968)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `4669.1956` → IC=+0.145 (n=5245)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 4669.1956 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.121 (n=9820)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.006 (IC base=+0.079)

- **PATRÓN** `ibs_20min` < `0.68` → IC=+0.131 (n=22258)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.68 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` > `0.5999` → IC=+0.187 (n=1303)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.5999 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` < `0.1578` → IC=+0.187 (n=7563)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.1578 (IC base=+0.079)

- **PATRÓN** `volumen_regimen` < `0.8628` → IC=+0.190 (n=5241)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.8628 (IC base=+0.079)

- **PATRÓN** `volumen_pendiente_norm` > `0.2969` → IC=+0.230 (n=1948)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2969 (IC base=+0.079)

- **PATRÓN** `volumen_spike_ratio` > `2.6842` → IC=+0.208 (n=4455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6842 (IC base=+0.079)

- **PATRÓN** `ballena_activa_n` < `104.0` → IC=+0.225 (n=13262)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 104.0 (IC base=+0.079)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3617` → IC=+0.210 (n=3387)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3617 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.221 (n=1642)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.211 (n=2268)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.9844` → IC=+0.280 (n=1536)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9844 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.618` → IC=+0.280 (n=1505)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.618 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.2834` → IC=+0.259 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2834 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.4363` → IC=+0.208 (n=3243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4363 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=3720)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `2059.4978` → IC=+0.211 (n=1129)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2059.4978 (IC base=+0.207)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.220 (n=3060)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.241 (n=2936)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0096 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.089` → IC=+0.278 (n=978)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.089 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.252 (n=1081)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.240 (n=1354)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.5519` → IC=+0.259 (n=2932)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5519 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` < `0.0956` → IC=+0.243 (n=2651)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0956 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2917` → IC=+0.257 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2917 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.4444` → IC=+0.240 (n=929)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4444 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `1.5513` → IC=+0.240 (n=2489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5513 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=3371)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1489.1` → IC=+0.245 (n=2619)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1489.1 (IC base=+0.239)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.236 (n=934)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.228 (n=933)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.1066` → IC=+0.257 (n=1232)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1066 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.238 (n=2928)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.229 (n=1991)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.9219` → IC=+0.270 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9219 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `0.1841` → IC=+0.235 (n=1313)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1841 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.089` → IC=+0.255 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.089 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` < `1.2254` → IC=+0.228 (n=2801)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2254 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `0.6261` → IC=+0.230 (n=2799)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6261 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.266 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.4011` → IC=+0.230 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4011 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `2.4278` → IC=+0.254 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4278 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.149 (n=2988)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0061 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.077` → IC=+0.154 (n=996)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.077 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=1106)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.7148` → IC=+0.165 (n=2986)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.7148 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.1349` → IC=+0.144 (n=2845)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1349 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.76` → IC=+0.139 (n=488)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 10.76 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.023` → IC=+0.131 (n=2731)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 4.023 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `1.2004` → IC=+0.133 (n=2986)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.2004 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.0974` → IC=+0.150 (n=1088)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.0974 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `2.1376` → IC=+0.134 (n=2519)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.1376 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `1.7941` → IC=+0.128 (n=1908)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.7941 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.127 (n=3872)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `205.0` → IC=+0.165 (n=1231)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 205.0 (IC base=+0.126)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.213 (n=1188)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.199 (n=3743)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.264 (n=1384)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.101` → IC=+0.278 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.101 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.097` → IC=+0.196 (n=3182)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.097 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.3534` → IC=+0.218 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3534 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.7128` → IC=+0.207 (n=1574)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7128 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=4281)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `1935.4984` → IC=+0.201 (n=1615)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1935.4984 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.224 (n=2862)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.1771` → IC=+0.237 (n=1432)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1771 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=1225)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.222 (n=1478)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` < `0.0377` → IC=+0.270 (n=1084)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0377 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.104` → IC=+0.263 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.104 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.3494` → IC=+0.263 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3494 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.1509` → IC=+0.226 (n=2075)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1509 (IC base=+0.219)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=1661)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `1918.7584` → IC=+0.221 (n=1474)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1918.7584 (IC base=+0.219)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.219 (n=2731)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.219)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.161 (n=181)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=4288)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.160 (n=613)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0038 (IC base=+0.053)

- **PATRÓN** `ibs_20min` > `0.944` → IC=+0.233 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.944 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` > `0.1359` → IC=+0.335 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1359 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` < `0.3345` → IC=+0.327 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3345 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.086` → IC=+0.196 (n=1328)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 5.086 (IC base=+0.053)

- **PATRÓN** `volumen_regimen` > `1.2441` → IC=+0.349 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2441 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` < `0.0777` → IC=+0.328 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0777 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.3037` → IC=+0.331 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3037 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` < `1.5356` → IC=+0.337 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5356 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` > `2.2606` → IC=+0.332 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2606 (IC base=+0.053)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.333 (n=698)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 143.0 (IC base=+0.053)

- **PATRÓN** `ibs_20min` < `0.0918` → IC=+0.180 (n=1118)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.0918 (IC base=+0.044)

- **PATRÓN** `dist_vwap_pct` > `0.7099` → IC=+0.168 (n=269)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.7099 (IC base=+0.044)

- **PATRÓN** `dist_vwap_pct` < `0.1359` → IC=+0.144 (n=1931)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1359 (IC base=+0.044)

- **PATRÓN** `volumen_regimen` < `0.8345` → IC=+0.158 (n=1383)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8345 (IC base=+0.044)

- **PATRÓN** `volumen_regimen` > `1.1666` → IC=+0.144 (n=691)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.1666 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.208 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` < `1.7843` → IC=+0.148 (n=1330)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.7843 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` > `2.1569` → IC=+0.162 (n=904)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.1569 (IC base=+0.044)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.179 (n=129)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=669)

- **FILTRO** `ibs_20min` < `0.2667` → IC=-0.170 (n=198)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2667
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=600)

- **FILTRO** `ibs_20min` > `0.2069` → IC=-0.133 (n=4203)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2069
  - _Potencial_: sin este filtro IC_bueno=+0.149 (n=2076)

- **FILTRO** `sigma_ewma_delta_pct` > `8.441` → IC=-0.223 (n=679)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.441
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=5600)

- **PATRÓN** `ibs_20min` > `0.7593` → IC=+0.175 (n=272)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.7593 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.9638` → IC=+0.277 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9638 (IC base=+0.024)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.045` → IC=+0.158 (n=188)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 5.045 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` > `1.0267` → IC=+0.298 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0267 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` < `0.1558` → IC=+0.284 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1558 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `2.4484` → IC=+0.287 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4484 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` > `1.449` → IC=+0.262 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.449 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.271 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.024)

- **PATRÓN** `ibs_20min` < `0.2069` → IC=+0.149 (n=2076)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.2069 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` < `0.2931` → IC=+0.276 (n=944)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2931 (IC base=-0.040)

- **PATRÓN** `volumen_regimen` < `0.695` → IC=+0.308 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.695 (IC base=-0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.0787` → IC=+0.295 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0787 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` < `2.456` → IC=+0.302 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.456 (IC base=-0.040)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7692` → IC=-0.152 (n=3120)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7692
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=1616)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.169 (n=1094)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=3642)

- **FILTRO** `ibs_20min` > `0.7463` → IC=-0.197 (n=1670)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7463
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=5021)

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

- **PATRÓN** `dist_vwap_pct` > `0.7968` → IC=+0.274 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7968 (IC base=-0.001)

- **PATRÓN** `dist_vwap_pct` < `0.2201` → IC=+0.263 (n=1883)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2201 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` < `0.7243` → IC=+0.272 (n=841)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7243 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` > `1.0657` → IC=+0.283 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0657 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.1689` → IC=+0.282 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1689 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `2.1776` → IC=+0.265 (n=1569)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1776 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.268 (n=1783)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.204 (n=6811)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.091)

- **PATRÓN** `ibs_20min` > `0.875` → IC=+0.287 (n=9265)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.875 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `0.9264` → IC=+0.302 (n=1464)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9264 (IC base=+0.091)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.546` → IC=+0.167 (n=9160)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.546 (IC base=+0.091)

- **PATRÓN** `volumen_regimen` < `1.1737` → IC=+0.269 (n=7483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1737 (IC base=+0.091)

- **PATRÓN** `volumen_regimen` > `0.6916` → IC=+0.275 (n=6687)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6916 (IC base=+0.091)

- **PATRÓN** `volumen_pendiente_norm` > `0.24` → IC=+0.287 (n=2248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.24 (IC base=+0.091)

- **PATRÓN** `volumen_spike_ratio` < `1.4576` → IC=+0.272 (n=3970)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4576 (IC base=+0.091)

- **PATRÓN** `volumen_spike_ratio` > `2.6489` → IC=+0.279 (n=3970)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6489 (IC base=+0.091)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.305 (n=11525)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 91.0 (IC base=+0.091)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.155 (n=6586)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0098 (IC base=+0.078)

- **PATRÓN** `ibs_20min` < `0.6471` → IC=+0.149 (n=19734)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.6471 (IC base=+0.078)

- **PATRÓN** `dist_vwap_pct` < `0.2473` → IC=+0.273 (n=6490)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2473 (IC base=+0.078)

- **PATRÓN** `volumen_regimen` < `0.7037` → IC=+0.272 (n=2814)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7037 (IC base=+0.078)

- **PATRÓN** `volumen_regimen` > `1.1942` → IC=+0.271 (n=2131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1942 (IC base=+0.078)

- **PATRÓN** `volumen_pendiente_norm` > `0.2944` → IC=+0.322 (n=1401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2944 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` < `1.5776` → IC=+0.296 (n=4114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5776 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` > `2.2804` → IC=+0.292 (n=4238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2804 (IC base=+0.078)

- **PATRÓN** `ballena_activa_n` < `75.0` → IC=+0.302 (n=9319)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 75.0 (IC base=+0.078)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.5796` → IC=-0.159 (n=2790)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5796
  - _Potencial_: sin este filtro IC_bueno=+0.206 (n=2790)

- **FILTRO** `ibs_20min` > `0.7231` → IC=-0.227 (n=1212)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7231
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=3637)

- **FILTRO** `sigma_ewma_delta_pct` > `4.242` → IC=-0.227 (n=1048)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.242
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=3801)

- **PATRÓN** `ibs_20min` > `0.9307` → IC=+0.333 (n=1395)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9307 (IC base=+0.023)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.091` → IC=+0.185 (n=1869)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 3.091 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.2292` → IC=+0.323 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2292 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` < `1.4451` → IC=+0.274 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4451 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` > `2.2463` → IC=+0.292 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2463 (IC base=+0.023)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.310 (n=1220)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.023)

- **PATRÓN** `ibs_20min` < `0.1714` → IC=+0.155 (n=1214)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.1714 (IC base=-0.028)

- **PATRÓN** `volumen_pendiente_norm` < `0.1514` → IC=+0.404 (n=817)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1514 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` < `1.4225` → IC=+0.425 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4225 (IC base=-0.028)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.398 (n=814)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=-0.028)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.6151` → IC=+0.227 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6151 (IC base=+0.016)

- **PATRÓN** `volumen_regimen` < `1.1937` → IC=+0.206 (n=1987)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1937 (IC base=+0.016)

- **PATRÓN** `volumen_regimen` > `0.6937` → IC=+0.209 (n=1775)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6937 (IC base=+0.016)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.246 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.016)

- **PATRÓN** `volumen_spike_ratio` < `1.4174` → IC=+0.232 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4174 (IC base=+0.016)

- **PATRÓN** `volumen_spike_ratio` > `2.4426` → IC=+0.207 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4426 (IC base=+0.016)

- **PATRÓN** `ballena_activa_n` < `267.0` → IC=+0.240 (n=1312)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 267.0 (IC base=+0.016)

- **PATRÓN** `dist_vwap_pct` < `0.1262` → IC=+0.247 (n=1380)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1262 (IC base=-0.005)

- **PATRÓN** `volumen_regimen` < `1.1652` → IC=+0.236 (n=1360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1652 (IC base=-0.005)

- **PATRÓN** `volumen_regimen` > `0.6223` → IC=+0.241 (n=1360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6223 (IC base=-0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2707` → IC=+0.306 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2707 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.5307` → IC=+0.246 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5307 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.1516` → IC=+0.251 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1516 (IC base=-0.005)

- **PATRÓN** `ballena_activa_n` < `214.0` → IC=+0.249 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 214.0 (IC base=-0.005)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.322 (n=1321)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.278)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.287 (n=2915)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.278)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.320 (n=1578)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.278)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.473` → IC=+0.301 (n=1758)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.473 (IC base=+0.278)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.291 (n=2554)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` > `1.6095` → IC=+0.283 (n=2825)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6095 (IC base=+0.278)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.288 (n=3472)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `2037.1984` → IC=+0.295 (n=971)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2037.1984 (IC base=+0.278)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.302 (n=1774)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.278)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.333 (n=1180)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.300)

- **PATRÓN** `drift_60min` |x|≤ `0.1771` → IC=+0.320 (n=1143)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1771 (IC base=+0.300)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.325 (n=991)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.300)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.303 (n=895)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.300)

- **PATRÓN** `ibs_20min` < `0.009` → IC=+0.303 (n=1145)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.009 (IC base=+0.300)

- **PATRÓN** `ibs_20min` > `0.1351` → IC=+0.308 (n=1731)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1351 (IC base=+0.300)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.337` → IC=+0.311 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.337 (IC base=+0.300)

- **PATRÓN** `volumen_pendiente_norm` < `0.1982` → IC=+0.299 (n=2553)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1982 (IC base=+0.300)

- **PATRÓN** `volumen_pendiente_norm` > `0.3441` → IC=+0.311 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3441 (IC base=+0.300)

- **PATRÓN** `volumen_spike_ratio` < `1.7441` → IC=+0.300 (n=1099)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7441 (IC base=+0.300)

- **PATRÓN** `volumen_spike_ratio` > `2.7236` → IC=+0.312 (n=1132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7236 (IC base=+0.300)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.304 (n=1328)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.300)

- **PATRÓN** `libro_liquidez` > `1919.8432` → IC=+0.310 (n=1178)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1919.8432 (IC base=+0.300)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.305 (n=1638)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.300)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7324` → IC=-0.183 (n=1266)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7324
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=3801)

- **PATRÓN** `ibs_20min` > `0.8604` → IC=+0.166 (n=1232)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.8604 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.1439` → IC=+0.232 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1439 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` < `0.3564` → IC=+0.235 (n=1725)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3564 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` < `1.0082` → IC=+0.238 (n=1550)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0082 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` > `0.6703` → IC=+0.231 (n=1573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6703 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.1025` → IC=+0.238 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1025 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `2.4586` → IC=+0.239 (n=1705)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4586 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `118.0` → IC=+0.253 (n=1738)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 118.0 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` < `0.1458` → IC=+0.244 (n=1216)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1458 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` < `1.1864` → IC=+0.248 (n=1247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1864 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.306 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.7891` → IC=+0.278 (n=795)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7891 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.4276` → IC=+0.263 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4276 (IC base=+0.003)

- **PATRÓN** `ballena_activa_n` < `103.0` → IC=+0.274 (n=1067)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 103.0 (IC base=+0.003)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7451` → IC=-0.238 (n=2118)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7451
  - _Potencial_: sin este filtro IC_bueno=+0.311 (n=2120)

- **FILTRO** `ibs_20min` > `0.6327` → IC=-0.233 (n=1020)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6327
  - _Potencial_: sin este filtro IC_bueno=+0.137 (n=3063)

- **FILTRO** `sigma_ewma_delta_pct` > `8.354` → IC=-0.249 (n=468)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.354
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=3615)

- **PATRÓN** `ibs_20min` > `0.7451` → IC=+0.311 (n=2120)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7451 (IC base=+0.037)

- **PATRÓN** `dist_vwap_pct` > `0.213` → IC=+0.345 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.213 (IC base=+0.037)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.482` → IC=+0.149 (n=1709)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 2.482 (IC base=+0.037)

- **PATRÓN** `volumen_regimen` < `0.8458` → IC=+0.340 (n=1035)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8458 (IC base=+0.037)

- **PATRÓN** `volumen_regimen` > `0.6975` → IC=+0.335 (n=1386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6975 (IC base=+0.037)

- **PATRÓN** `volumen_pendiente_norm` < `0.1583` → IC=+0.335 (n=1608)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1583 (IC base=+0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.354 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.037)

- **PATRÓN** `volumen_spike_ratio` < `1.4313` → IC=+0.361 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4313 (IC base=+0.037)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.354 (n=1333)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.037)

- **PATRÓN** `ibs_20min` < `0.6327` → IC=+0.137 (n=3063)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.6327 (IC base=+0.045)

- **PATRÓN** `dist_vwap_pct` < `0.2117` → IC=+0.254 (n=1415)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2117 (IC base=+0.045)

- **PATRÓN** `volumen_regimen` < `0.6964` → IC=+0.277 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6964 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.272 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` < `2.4528` → IC=+0.258 (n=1413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4528 (IC base=+0.045)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.273 (n=1432)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.045)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.356 (n=1952)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.312)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.314 (n=2209)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.312)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.317 (n=1032)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.312)

- **PATRÓN** `ibs_20min` > `0.7634` → IC=+0.348 (n=1952)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7634 (IC base=+0.312)

- **PATRÓN** `dist_vwap_pct` > `0.2044` → IC=+0.336 (n=1210)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2044 (IC base=+0.312)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.816` → IC=+0.330 (n=1060)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.816 (IC base=+0.312)

- **PATRÓN** `volumen_regimen` > `0.629` → IC=+0.322 (n=2185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.629 (IC base=+0.312)

- **PATRÓN** `volumen_pendiente_norm` > `0.28` → IC=+0.349 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.28 (IC base=+0.312)

- **PATRÓN** `volumen_spike_ratio` > `1.4264` → IC=+0.325 (n=2100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4264 (IC base=+0.312)

- **PATRÓN** `libro_liquidez` > `2572.5002` → IC=+0.313 (n=1457)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2572.5002 (IC base=+0.312)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.343 (n=1915)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.312)

- **PATRÓN** `sigma_h` > `0.0153` → IC=+0.344 (n=1550)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0153 (IC base=+0.313)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.321 (n=1168)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.313)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.315 (n=1138)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.313)

- **PATRÓN** `ibs_20min` < `0.38` → IC=+0.334 (n=2326)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.38 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` < `0.2328` → IC=+0.318 (n=2239)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2328 (IC base=+0.313)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.628` → IC=+0.330 (n=861)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.628 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` < `0.7226` → IC=+0.320 (n=1023)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7226 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` > `1.2131` → IC=+0.342 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2131 (IC base=+0.313)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.366 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` < `1.4109` → IC=+0.325 (n=716)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4109 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` > `2.1343` → IC=+0.315 (n=973)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1343 (IC base=+0.313)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.227 (n=5093)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.1217` → IC=+0.194 (n=6725)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1217 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=15860)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `0.5435` → IC=+0.233 (n=15276)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5435 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.161` → IC=+0.207 (n=5966)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.161 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.153` → IC=+0.254 (n=3983)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.153 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `1.1851` → IC=+0.159 (n=10162)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1851 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` > `0.6243` → IC=+0.158 (n=10162)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.6243 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.2938` → IC=+0.206 (n=2213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2938 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `2.6056` → IC=+0.188 (n=4949)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6056 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.196 (n=14205)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 90.0 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.190 (n=6536)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0056 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.0802` → IC=+0.222 (n=4953)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0802 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=5566)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.52` → IC=+0.238 (n=14856)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.52 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` < `0.1768` → IC=+0.175 (n=10704)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.1768 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.74` → IC=+0.194 (n=2377)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 9.74 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.588` → IC=+0.185 (n=13195)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 2.588 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.1803` → IC=+0.163 (n=10586)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1803 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2957` → IC=+0.221 (n=2224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2957 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6423` → IC=+0.189 (n=4688)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6423 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `95.0` → IC=+0.195 (n=13822)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 95.0 (IC base=+0.181)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.226 (n=847)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0055 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.1048` → IC=+0.258 (n=1113)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1048 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.240 (n=934)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.229 (n=1709)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.807` → IC=+0.274 (n=2258)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.807 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.705` → IC=+0.329 (n=811)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.705 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.287 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `1.8388` → IC=+0.224 (n=1604)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8388 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `1.4361` → IC=+0.225 (n=2405)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4361 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=2800)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.257 (n=2014)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0092 (IC base=+0.254)

- **PATRÓN** `drift_60min` |x|≤ `0.0973` → IC=+0.307 (n=888)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0973 (IC base=+0.254)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.260 (n=2085)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.254)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.256 (n=1839)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.254)

- **PATRÓN** `ibs_20min` < `0.4216` → IC=+0.271 (n=2014)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4216 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` < `0.1007` → IC=+0.258 (n=1769)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1007 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` > `0.3022` → IC=+0.276 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3022 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` < `1.4444` → IC=+0.277 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4444 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` > `2.7246` → IC=+0.256 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7246 (IC base=+0.254)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.256 (n=2317)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.254)

- **PATRÓN** `libro_liquidez` > `1475.9` → IC=+0.262 (n=1799)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1475.9 (IC base=+0.254)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.254 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.254)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.201 (n=780)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0641` → IC=+0.179 (n=775)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.0641 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.154 (n=2432)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.2783` → IC=+0.212 (n=2322)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2783 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.1836` → IC=+0.214 (n=1199)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1836 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.924` → IC=+0.208 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.924 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.6943` → IC=+0.150 (n=1022)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6943 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `1.061` → IC=+0.140 (n=1054)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 1.061 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.180 (n=360)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.5038` → IC=+0.154 (n=1004)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.5038 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.4691` → IC=+0.150 (n=760)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.4691 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `408.0` → IC=+0.143 (n=2247)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 408.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.172 (n=2452)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0062 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.237` → IC=+0.167 (n=2159)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.237 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.182 (n=1172)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.6155` → IC=+0.205 (n=2452)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6155 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.153` → IC=+0.180 (n=463)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 11.153 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.076` → IC=+0.145 (n=2142)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 4.076 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.1995` → IC=+0.157 (n=2452)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1995 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.0946` → IC=+0.147 (n=2122)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.0946 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.1387` → IC=+0.147 (n=2049)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.1387 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.4259` → IC=+0.143 (n=2329)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4259 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `215.0` → IC=+0.183 (n=995)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 215.0 (IC base=+0.144)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.237 (n=1177)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.3959` → IC=+0.224 (n=2277)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3959 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.235 (n=942)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=1365)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.269` → IC=+0.307 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.269 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.212 (n=2246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.3534` → IC=+0.235 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3534 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.7614` → IC=+0.212 (n=1109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7614 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.71` → IC=+0.226 (n=1143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.71 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.217 (n=3106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `1926.1784` → IC=+0.226 (n=1173)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1926.1784 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.246 (n=1981)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.4197` → IC=+0.261 (n=1981)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4197 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.284 (n=856)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.0291` → IC=+0.290 (n=992)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0291 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.221` → IC=+0.285 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.221 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.3594` → IC=+0.293 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3594 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.7646` → IC=+0.237 (n=952)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7646 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.1746` → IC=+0.247 (n=1442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1746 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.240 (n=1171)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1912.48` → IC=+0.252 (n=1020)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1912.48 (IC base=+0.238)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.244 (n=1459)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.238)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.205 (n=833)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0772` → IC=+0.193 (n=833)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.0772 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.148 (n=2592)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.2699` → IC=+0.200 (n=2499)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2699 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.1371` → IC=+0.187 (n=1482)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1371 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.45` → IC=+0.195 (n=431)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 11.45 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.0214` → IC=+0.142 (n=2199)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.0214 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2887` → IC=+0.176 (n=372)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2887 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.8252` → IC=+0.141 (n=1632)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.8252 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.5248` → IC=+0.155 (n=816)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.5248 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `6872.8229` → IC=+0.200 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6872.8229 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `132.0` → IC=+0.144 (n=2442)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 132.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.164 (n=2333)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0065 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.3937` → IC=+0.141 (n=2644)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.3937 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.161 (n=1259)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 15.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.6735` → IC=+0.184 (n=2644)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6735 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.1561` → IC=+0.153 (n=2652)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1561 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.384` → IC=+0.145 (n=638)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 9.384 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8521` → IC=+0.154 (n=1763)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8521 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2975` → IC=+0.180 (n=398)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2975 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.8098` → IC=+0.129 (n=1665)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.8098 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `1.5265` → IC=+0.125 (n=2230)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.5265 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `6171.4117` → IC=+0.179 (n=1199)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 6171.4117 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `110.0` → IC=+0.131 (n=2170)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 110.0 (IC base=+0.126)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.168 (n=1268)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0109 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.160 (n=1344)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 15.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.4769` → IC=+0.211 (n=2794)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4769 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.1959` → IC=+0.190 (n=1540)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1959 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.202` → IC=+0.288 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.202 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.1741` → IC=+0.133 (n=2794)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1741 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.7041` → IC=+0.124 (n=2496)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.7041 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1632` → IC=+0.131 (n=2851)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1632 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.5401` → IC=+0.139 (n=1194)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.5401 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.124 (n=2918)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2638.8758` → IC=+0.200 (n=1267)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2638.8758 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.143 (n=1167)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 21.0 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0115` → IC=+0.141 (n=2894)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0115 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.11` → IC=+0.160 (n=965)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.11 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=2955)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.6429` → IC=+0.218 (n=2897)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6429 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` < `0.2029` → IC=+0.145 (n=2809)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.2029 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.332` → IC=+0.136 (n=2553)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 2.332 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `1.1776` → IC=+0.127 (n=2893)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.1776 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.276` → IC=+0.134 (n=397)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.276 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.4363` → IC=+0.123 (n=907)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 1.4363 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` > `2.4432` → IC=+0.125 (n=907)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 2.4432 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2522.1712` → IC=+0.180 (n=1312)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2522.1712 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.123 (n=2685)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 46.0 (IC base=+0.117)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.248 (n=2277)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1678` → IC=+0.241 (n=1123)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1678 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.228 (n=2649)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.230 (n=2291)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.6639` → IC=+0.258 (n=2548)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6639 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.1803` → IC=+0.232 (n=1602)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1803 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` < `0.817` → IC=+0.226 (n=2625)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.817 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.594` → IC=+0.255 (n=1150)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.594 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` < `1.1691` → IC=+0.226 (n=2548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1691 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.6235` → IC=+0.233 (n=2548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6235 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2323` → IC=+0.268 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2323 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `2.4668` → IC=+0.228 (n=2484)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4668 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.8092` → IC=+0.235 (n=1656)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8092 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2936.2954` → IC=+0.234 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2936.2954 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0128` → IC=+0.241 (n=1146)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0128 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0227` → IC=+0.247 (n=1181)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0227 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.0876` → IC=+0.261 (n=867)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0876 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.252 (n=1267)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.242 (n=1160)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.4398` → IC=+0.263 (n=2599)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4398 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `1.1311` → IC=+0.245 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1311 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.234` → IC=+0.269 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.234 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` < `0.8693` → IC=+0.238 (n=1734)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8693 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` > `0.6418` → IC=+0.240 (n=2599)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6418 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.288 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.836` → IC=+0.233 (n=1626)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.836 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `1.4336` → IC=+0.238 (n=2438)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4336 (IC base=+0.237)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.206 (n=1286)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.1297` → IC=+0.183 (n=1689)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1297 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.185 (n=3434)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.3277` → IC=+0.202 (n=3839)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3277 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.7962` → IC=+0.197 (n=582)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.7962 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.552` → IC=+0.197 (n=1648)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 3.552 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `0.8609` → IC=+0.185 (n=2313)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.8609 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `1.1917` → IC=+0.170 (n=1157)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.1917 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.0995` → IC=+0.173 (n=1382)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.0995 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.4279` → IC=+0.179 (n=1246)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.4279 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.171 (n=4311)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.02 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `2579.2684` → IC=+0.175 (n=3430)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2579.2684 (IC base=+0.167)

- **PATRÓN** `ibs_20min` < `0.3896` → IC=+0.159 (n=2754)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.3896 (IC base=+0.083)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.127 (n=1749)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 26.0 (IC base=+0.083)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.195 (n=1037)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0057 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.099` → IC=+0.234 (n=457)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.099 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.214 (n=941)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.2232` → IC=+0.218 (n=1036)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2232 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.2987` → IC=+0.212 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2987 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.001` → IC=+0.198 (n=455)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 3.001 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.457` → IC=+0.183 (n=1090)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 6.457 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.8791` → IC=+0.198 (n=691)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.8791 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` < `0.1507` → IC=+0.184 (n=1090)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.1507 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.0915` → IC=+0.186 (n=361)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.0915 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `2.1906` → IC=+0.197 (n=893)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.1906 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `10160.0205` → IC=+0.185 (n=1036)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 10160.0205 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.165 (n=556)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0033 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.6363` → IC=+0.139 (n=1112)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.6363 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `163.0` → IC=+0.169 (n=542)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 163.0 (IC base=+0.085)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.244 (n=529)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.2091` → IC=+0.187 (n=801)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.2091 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=1254)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `0.6357` → IC=+0.251 (n=800)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6357 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `0.7802` → IC=+0.196 (n=189)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.7802 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` < `0.2032` → IC=+0.179 (n=1083)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.2032 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.838` → IC=+0.214 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.838 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `0.8342` → IC=+0.195 (n=801)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.8342 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.1596` → IC=+0.200 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1596 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` < `1.4273` → IC=+0.188 (n=395)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.4273 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `1.7865` → IC=+0.189 (n=790)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.7865 (IC base=+0.178)

- **PATRÓN** `ibs_20min` < `0.1008` → IC=+0.184 (n=390)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.1008 (IC base=+0.075)

- **PATRÓN** `libro_liquidez` > `8161.2198` → IC=+0.141 (n=530)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 8161.2198 (IC base=+0.075)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.157 (n=423)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.007 (IC base=+0.141)

- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.143 (n=320)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.0114 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.174 (n=860)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 8.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.4953` → IC=+0.199 (n=960)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.4953 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.968` → IC=+0.218 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.968 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.01` → IC=+0.237 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.01 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.0549` → IC=+0.152 (n=845)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.0549 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` > `0.7047` → IC=+0.149 (n=858)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.7047 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.2267` → IC=+0.163 (n=179)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.2267 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.4277` → IC=+0.167 (n=310)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.4277 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `2.1481` → IC=+0.141 (n=421)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 2.1481 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.148 (n=1007)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.02 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `2741.5709` → IC=+0.176 (n=436)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2741.5709 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.5732` → IC=+0.135 (n=925)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.5732 (IC base=+0.049)

- **PATRÓN** `libro_liquidez` > `2579.8383` → IC=+0.143 (n=477)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 2579.8383 (IC base=+0.049)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0261` → IC=+0.174 (n=274)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0261 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0165` → IC=+0.212 (n=182)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0165 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.2668` → IC=+0.181 (n=183)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.2668 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.220 (n=130)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.5738` → IC=+0.203 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5738 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.3078` → IC=+0.181 (n=142)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.3078 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` < `1.1958` → IC=+0.169 (n=306)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 1.1958 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.349` → IC=+0.193 (n=242)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 3.349 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `1.0007` → IC=+0.167 (n=241)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.0007 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `1.1497` → IC=+0.188 (n=91)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 1.1497 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.1044` → IC=+0.178 (n=88)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1044 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.8264` → IC=+0.195 (n=165)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.8264 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `2.4009` → IC=+0.191 (n=82)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.4009 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.189 (n=323)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.03 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `2675.5939` → IC=+0.206 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2675.5939 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.176 (n=273)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0131 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.3001` → IC=+0.144 (n=203)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3001 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.168 (n=221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 10.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.195` → IC=+0.154 (n=134)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.195 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.51` → IC=+0.141 (n=140)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 0.51 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `1.2011` → IC=+0.264 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2011 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.232` → IC=+0.187 (n=81)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 5.232 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.872` → IC=+0.173 (n=203)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.872 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` < `0.1158` → IC=+0.146 (n=278)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.1158 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.2383` → IC=+0.189 (n=59)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2383 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.5346` → IC=+0.197 (n=97)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.5346 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `2.7694` → IC=+0.157 (n=97)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.7694 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `1962.6643` → IC=+0.144 (n=304)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 1962.6643 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.161 (n=281)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 19.0 (IC base=+0.141)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.229 (n=6651)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=20788)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.4364` → IC=+0.229 (n=19928)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4364 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.8716` → IC=+0.211 (n=2400)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8716 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.077` → IC=+0.254 (n=4891)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.077 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.2171` → IC=+0.162 (n=13396)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2171 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2414` → IC=+0.205 (n=3590)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2414 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6202` → IC=+0.192 (n=6478)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6202 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.202 (n=18552)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 106.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.197 (n=8038)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0058 (IC base=+0.191)

- **PATRÓN** `sigma_h` > `0.012` → IC=+0.196 (n=6083)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.012 (IC base=+0.191)

- **PATRÓN** `drift_60min` |x|≤ `0.4823` → IC=+0.194 (n=18237)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.4823 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=6774)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` < `0.5909` → IC=+0.242 (n=18242)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5909 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` < `0.1756` → IC=+0.173 (n=11372)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1756 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.598` → IC=+0.204 (n=2495)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.598 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.459` → IC=+0.194 (n=17728)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 3.459 (IC base=+0.191)

- **PATRÓN** `volumen_regimen` < `1.0562` → IC=+0.165 (n=10798)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.0562 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.2923` → IC=+0.254 (n=2498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2923 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `2.6329` → IC=+0.202 (n=5794)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6329 (IC base=+0.191)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.206 (n=17112)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 94.0 (IC base=+0.191)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.247 (n=1556)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.234 (n=2162)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` > `0.8602` → IC=+0.300 (n=2143)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8602 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.71` → IC=+0.337 (n=1042)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.71 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.233` → IC=+0.291 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.233 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` < `1.4446` → IC=+0.232 (n=1034)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4446 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.2835` → IC=+0.237 (n=1405)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2835 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.248 (n=3517)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `2057.3966` → IC=+0.236 (n=1072)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2057.3966 (IC base=+0.232)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.255 (n=1089)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.232)

- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.269 (n=2820)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0096 (IC base=+0.265)

- **PATRÓN** `drift_60min` |x|≤ `0.1219` → IC=+0.292 (n=1241)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1219 (IC base=+0.265)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.270 (n=2600)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.265)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.266 (n=2561)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.265)

- **PATRÓN** `ibs_20min` < `0.4416` → IC=+0.294 (n=2479)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4416 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.266 (n=2557)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` > `0.2895` → IC=+0.290 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2895 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` < `1.5651` → IC=+0.265 (n=1184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5651 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` > `2.6632` → IC=+0.276 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6632 (IC base=+0.265)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.266 (n=3245)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.265)

- **PATRÓN** `libro_liquidez` > `1489.6339` → IC=+0.271 (n=2517)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1489.6339 (IC base=+0.265)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.272 (n=969)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.265)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.184 (n=1082)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.003 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.1041` → IC=+0.153 (n=1428)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1041 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=3384)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.2145` → IC=+0.193 (n=3247)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.2145 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.3171` → IC=+0.202 (n=1099)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3171 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.447` → IC=+0.156 (n=682)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 9.447 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.091` → IC=+0.140 (n=2851)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 3.091 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.6354` → IC=+0.161 (n=1082)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.6354 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `1.0726` → IC=+0.143 (n=1472)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.0726 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` < `0.0722` → IC=+0.142 (n=2903)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` < 0.0722 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2724` → IC=+0.176 (n=464)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2724 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.1558` → IC=+0.147 (n=2800)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.1558 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.5212` → IC=+0.142 (n=2844)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.5212 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `426.0` → IC=+0.149 (n=3125)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 426.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.160 (n=2789)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0062 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.0785` → IC=+0.175 (n=930)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0785 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.168 (n=1015)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.6852` → IC=+0.184 (n=2788)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6852 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.1373` → IC=+0.151 (n=2669)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1373 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.863` → IC=+0.148 (n=461)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 10.863 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `1.1913` → IC=+0.145 (n=2788)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.1913 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.2185` → IC=+0.191 (n=519)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2185 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `1.4123` → IC=+0.142 (n=894)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4123 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.7759` → IC=+0.141 (n=1787)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.7759 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=3617)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `231.0` → IC=+0.144 (n=864)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 231.0 (IC base=+0.135)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.254 (n=1108)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0128 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=3476)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=2975)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=1242)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.182` → IC=+0.324 (n=730)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.182 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` < `0.1313` → IC=+0.226 (n=3129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1313 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `3.2286` → IC=+0.241 (n=1079)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2286 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.231 (n=3977)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `1933.909` → IC=+0.240 (n=1505)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1933.909 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.247 (n=2771)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0109 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.1789` → IC=+0.263 (n=1386)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1789 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.264 (n=1190)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.243 (n=1436)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.0526` → IC=+0.305 (n=1053)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0526 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.337` → IC=+0.303 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.337 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.3493` → IC=+0.308 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3493 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `2.1588` → IC=+0.256 (n=2013)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1588 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.248 (n=1623)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `1915.34` → IC=+0.252 (n=1428)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1915.34 (IC base=+0.242)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.249 (n=2588)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.242)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.186 (n=1522)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0041 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.4291` → IC=+0.148 (n=3443)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.4291 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.150 (n=3580)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.898` → IC=+0.277 (n=1148)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.898 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.1937` → IC=+0.167 (n=1595)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1937 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.963` → IC=+0.155 (n=1543)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 2.963 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.8602` → IC=+0.154 (n=2296)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8602 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2336` → IC=+0.185 (n=607)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2336 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.5208` → IC=+0.156 (n=1481)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.5208 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `7297.3713` → IC=+0.239 (n=1148)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7297.3713 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.151 (n=1469)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 69.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.158 (n=2874)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0077 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.4395` → IC=+0.148 (n=2874)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.4395 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=1053)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.7166` → IC=+0.193 (n=2874)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.7166 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1474` → IC=+0.150 (n=2652)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1474 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.978` → IC=+0.166 (n=429)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 10.978 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.6905` → IC=+0.153 (n=1265)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6905 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2949` → IC=+0.223 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2949 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.22` → IC=+0.141 (n=2439)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.22 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.5369` → IC=+0.146 (n=2476)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.5369 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `6189.7409` → IC=+0.211 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6189.7409 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `95.0` → IC=+0.145 (n=1882)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 95.0 (IC base=+0.137)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.151 (n=1583)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.011 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.152 (n=2464)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 11.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `0.4333` → IC=+0.193 (n=3485)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.4333 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `1.0061` → IC=+0.208 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0061 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.416` → IC=+0.267 (n=881)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.416 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.8777` → IC=+0.134 (n=2321)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8777 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.164` → IC=+0.123 (n=3636)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.164 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `2.4923` → IC=+0.122 (n=3400)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.4923 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.122 (n=3635)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2690.7725` → IC=+0.243 (n=1161)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2690.7725 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.129 (n=1124)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 21.0 (IC base=+0.120)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.154 (n=2894)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0106 (IC base=+0.121)

- **PATRÓN** `drift_60min` |x|≤ `0.1359` → IC=+0.153 (n=1096)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1359 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.155 (n=1542)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 15.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.210 (n=3302)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6667 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` < `0.2138` → IC=+0.140 (n=2943)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.2138 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.124` → IC=+0.145 (n=3164)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 3.124 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `0.6386` → IC=+0.149 (n=1097)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.6386 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.2255` → IC=+0.170 (n=577)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2255 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.4353` → IC=+0.155 (n=1035)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4353 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2576.7029` → IC=+0.200 (n=1096)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2576.7029 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.133 (n=3099)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 51.0 (IC base=+0.121)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0139` → IC=+0.258 (n=2883)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0139 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.241 (n=3371)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.240 (n=2896)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` > `0.6152` → IC=+0.271 (n=2883)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6152 (IC base=+0.236)

- **PATRÓN** `dist_vwap_pct` > `0.1902` → IC=+0.252 (n=1704)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1902 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.272` → IC=+0.283 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.272 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` < `1.2209` → IC=+0.240 (n=3227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2209 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` > `0.6434` → IC=+0.240 (n=3227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6434 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2372` → IC=+0.260 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2372 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.5001` → IC=+0.256 (n=1050)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5001 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `2936.8323` → IC=+0.243 (n=1076)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2936.8323 (IC base=+0.236)

- **PATRÓN** `sigma_h` > `0.0258` → IC=+0.261 (n=1108)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0258 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.244 (n=3138)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.521` → IC=+0.271 (n=3323)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.521 (IC base=+0.239)

- **PATRÓN** `dist_vwap_pct` < `0.2157` → IC=+0.245 (n=3127)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2157 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.187` → IC=+0.279 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.187 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` > `1.2151` → IC=+0.260 (n=1108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2151 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.286` → IC=+0.305 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.286 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.8128` → IC=+0.237 (n=2080)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8128 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `1.4292` → IC=+0.240 (n=3117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4292 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.237 (n=3051)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.239)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.199 (n=5632)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.245 (n=1929)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.5012` → IC=+0.224 (n=5774)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5012 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.230 (n=2094)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.9342` → IC=+0.254 (n=1925)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9342 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` < `0.4234` → IC=+0.219 (n=4193)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4234 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.606` → IC=+0.221 (n=1890)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.606 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.569` → IC=+0.216 (n=5137)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.569 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` < `0.7071` → IC=+0.227 (n=1878)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7071 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `0.883` → IC=+0.218 (n=2845)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.883 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` < `0.1054` → IC=+0.218 (n=5388)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1054 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.1654` → IC=+0.222 (n=1632)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1654 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `1.4526` → IC=+0.224 (n=1895)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4526 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.223 (n=4525)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `3721.1308` → IC=+0.225 (n=3849)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3721.1308 (IC base=+0.216)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.238 (n=1414)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.49` → IC=+0.212 (n=4236)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.49 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=1432)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.212 (n=1883)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` < `0.7304` → IC=+0.205 (n=4237)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7304 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.6483` → IC=+0.209 (n=730)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6483 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` < `0.1763` → IC=+0.194 (n=3755)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1763 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.79` → IC=+0.208 (n=3789)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.79 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` < `1.0967` → IC=+0.203 (n=3549)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0967 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.199 (n=3894)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.2231` → IC=+0.202 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2231 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` < `1.5347` → IC=+0.203 (n=1837)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5347 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `2.1894` → IC=+0.206 (n=1893)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1894 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.199 (n=5632)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `ballena_activa_n` < `171.0` → IC=+0.208 (n=3664)

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
- **PATRÓN** `drift_60min` |x|≤ `0.587` → IC=+0.204 (n=859)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.587 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.236 (n=324)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` < `0.3898` → IC=+0.199 (n=287)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.3898 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.240 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.494` → IC=+0.239 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.494 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.2085` → IC=+0.239 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2085 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `1.8086` → IC=+0.204 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8086 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `2760.165` → IC=+0.226 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2760.165 (IC base=+0.196)

- **PATRÓN** `ballena_activa_n` < `5.0` → IC=+0.198 (n=382)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 5.0 (IC base=+0.196)

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
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.4848` → IC=+0.217 (n=1315)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4848 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.208 (n=501)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.211 (n=886)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` < `0.4046` → IC=+0.200 (n=877)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4046 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `0.0897` → IC=+0.201 (n=1314)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0897 (IC base=+0.196)

- **PATRÓN** `dist_vwap_pct` > `0.6251` → IC=+0.212 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6251 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.353` → IC=+0.199 (n=1194)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 4.353 (IC base=+0.196)

- **PATRÓN** `volumen_regimen` < `0.6402` → IC=+0.223 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6402 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.074` → IC=+0.227 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.074 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` < `2.1981` → IC=+0.203 (n=1134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1981 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `1.7867` → IC=+0.197 (n=859)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.7867 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `6511.755` → IC=+0.202 (n=1174)

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
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.153 (n=670)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0036 (IC base=+0.058)

- **PATRÓN** `ibs_20min` > `0.3793` → IC=+0.127 (n=1900)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` > 0.3793 (IC base=+0.058)

- **PATRÓN** `dist_vwap_pct` > `0.1457` → IC=+0.140 (n=957)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.1457 (IC base=+0.058)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.621` → IC=+0.146 (n=416)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 10.621 (IC base=+0.058)

- **PATRÓN** `ibs_20min` < `0.0478` → IC=+0.261 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0478 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.1456` → IC=+0.133 (n=341)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.1456 (IC base=+0.041)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.128 (n=641)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0059 (IC base=+0.081)

- **PATRÓN** `ibs_20min` > `0.3736` → IC=+0.160 (n=610)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.3736 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.1188` → IC=+0.174 (n=299)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.1188 (IC base=+0.081)

- **PATRÓN** `ibs_20min` < `0.0659` → IC=+0.281 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0659 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.2162` → IC=+0.167 (n=100)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2162 (IC base=+0.050)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.7025` → IC=-0.162 (n=131)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7025
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=395)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.128 (n=434)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0051 (IC base=+0.075)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.128 (n=318)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 15.0 (IC base=+0.075)

- **PATRÓN** `ibs_20min` > `0.7791` → IC=+0.225 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7791 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` > `0.1265` → IC=+0.175 (n=309)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.1265 (IC base=+0.075)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.646` → IC=+0.206 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.646 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.0314` → IC=+0.254 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0314 (IC base=+0.012)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.200 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.7073` → IC=+0.135 (n=154)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.7073 (IC base=+0.021)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.754` → IC=+0.132 (n=142)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 8.754 (IC base=+0.021)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.148 (n=313)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0109 (IC base=+0.061)

- **PATRÓN** `ibs_20min` < `0.4545` → IC=+0.171 (n=326)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.4545 (IC base=+0.061)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.982` → IC=+0.300 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.982 (IC base=+0.061)

- **PATRÓN** `volumen_regimen` > `1.1045` → IC=+0.176 (n=109)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.1045 (IC base=+0.061)

- **PATRÓN** `volumen_pendiente_norm` > `0.1522` → IC=+0.157 (n=97)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.1522 (IC base=+0.061)

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

- **FILTRO** `hora_utc` > `11.0` → IC=-0.367 (n=58)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.258 (n=64)

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
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=722)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.211 (n=206)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.135)

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

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 8.784 (IC base=+0.032)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.7055` → IC=-0.172 (n=59)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7055
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=184)

- **PATRÓN** `dist_vwap_pct` > `0.5497` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5497 (IC base=+0.018)

- **PATRÓN** `ibs_20min` < `0.2374` → IC=+0.170 (n=337)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.2374 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.801` → IC=+0.144 (n=102)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 9.801 (IC base=+0.094)

- **PATRÓN** `volumen_pendiente_norm` > `0.2251` → IC=+0.138 (n=67)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.2251 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` > `1.7729` → IC=+0.131 (n=204)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.7729 (IC base=+0.094)

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

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2928.7278 (IC base=+0.100)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2928.7278` → IC=+0.132 (n=498)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2928.7278 (IC base=+0.100)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=224)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=224)

- **FILTRO** `libro_liquidez` < `6113.1051` → IC=-0.147 (n=120)

  - _Acción_: SKIP cuando `libro_liquidez` < 6113.1051
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=120)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=516)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `4006.09` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `liq_usd_total` < 4006.09
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=26)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=35)

- **PATRÓN** `liq_n` > `2.0` → IC=+0.132 (n=93)

  - _Acción_: Kelly boost +0.66€ cuando `liq_n` > 2.0 (IC base=+0.059)

- **PATRÓN** `liq_usd_total` > `7175.1` → IC=+0.123 (n=75)

  - _Acción_: Kelly boost +0.62€ cuando `liq_usd_total` > 7175.1 (IC base=+0.059)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.138 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 8.0 (IC base=+0.059)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=3819)

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
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=1534)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=1488)

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
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=928)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=928)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=1065)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=1065)

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
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=308)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=349)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=285)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=379)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=379)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=224)

- **FILTRO** `libro_liquidez` < `652.2458` → IC=-0.140 (n=134)

  - _Acción_: SKIP cuando `libro_liquidez` < 652.2458
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=275)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=307)

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
- **FILTRO** `py_entrada` < `0.39` → IC=-0.129 (n=141)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=570)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.139 (n=286)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=303)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.172 (n=126)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=530)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.145 (n=260)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=535)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.174 (n=6979)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=22500)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.178 (n=7387)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=22913)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.190 (n=1314)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=4106)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.175 (n=1252)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=4129)

- **PATRÓN** `libro_liquidez` > `1041.5682` → IC=+0.141 (n=2710)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 1041.5682 (IC base=+0.042)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.131 (n=2523)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.5 (IC base=+0.013)

- **PATRÓN** `libro_liquidez` > `1140.6472` → IC=+0.150 (n=1830)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1140.6472 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.184 (n=1045)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3235)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.206 (n=1322)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=4185)

- **PATRÓN** `ibs_20min` > `0.9643` → IC=+0.130 (n=1850)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.9643 (IC base=+0.035)

- **PATRÓN** `libro_liquidez` > `1739.0784` → IC=+0.122 (n=1846)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1739.0784 (IC base=+0.035)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.155 (n=1354)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=4095)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2418)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=2342)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=3826)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.137 (n=1293)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=2521)

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
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=45249)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.297 (n=15384)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=49989)

- **FILTRO** `ibs_7min` < `0.2273` → IC=-0.231 (n=16338)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2273
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=49035)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.152 (n=21841)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=43532)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.243 (n=20361)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=61663)

- **FILTRO** `ibs_7min` > `0.2834` → IC=-0.182 (n=20502)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2834
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=61522)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.154 (n=2834)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=8709)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.318 (n=2804)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=8739)

- **FILTRO** `ibs_7min` < `0.7115` → IC=-0.249 (n=3808)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7115
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=7735)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.150 (n=2686)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=8857)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.277 (n=3386)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=10801)

- **FILTRO** `ibs_7min` > `0.7715` → IC=-0.214 (n=3546)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7715
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=10641)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.262 (n=2607)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=8337)

- **FILTRO** `ibs_7min` < `0.7184` → IC=-0.205 (n=2735)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7184
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=8209)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.194 (n=2726)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=8218)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.261 (n=2781)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=8385)

- **FILTRO** `ibs_7min` > `0.2661` → IC=-0.192 (n=2791)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2661
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=8375)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.180 (n=2777)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=8389)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.163 (n=2682)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=8367)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.314 (n=2759)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=8290)

- **FILTRO** `ibs_7min` < `0.2886` → IC=-0.247 (n=3646)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2886
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=7403)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.197 (n=2353)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=8696)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.259 (n=3578)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=11437)

- **FILTRO** `ibs_7min` > `0.7305` → IC=-0.183 (n=3753)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7305
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=11262)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=2578)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=8019)

- **FILTRO** `ibs_7min` < `0.7204` → IC=-0.193 (n=2649)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7204
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=7948)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.187 (n=2642)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=7955)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.258 (n=2539)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=8517)

- **FILTRO** `ibs_7min` > `0.2752` → IC=-0.174 (n=2763)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2752
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=8293)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.168 (n=2762)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=8294)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.295 (n=2442)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=8128)

- **FILTRO** `ibs_7min` < `0.7083` → IC=-0.227 (n=3469)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7083
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=7101)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.222 (n=2473)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=8097)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.192 (n=3779)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=12052)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.127 (n=3419)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=7251)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.309 (n=2455)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=8215)

- **FILTRO** `ibs_7min` < `0.1818` → IC=-0.230 (n=2664)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1818
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=8006)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.202 (n=2471)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=8199)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.226 (n=3679)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=11090)

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
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=562)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4308` → IC=+0.152 (n=619)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio` |x|> 0.4308 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.134 (n=706)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 6.0 (IC base=+0.123)

- **PATRÓN** `total_vol_5m` < `422.987` → IC=+0.159 (n=455)

  - _Acción_: Kelly boost +0.79€ cuando `total_vol_5m` < 422.987 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `3558.8016` → IC=+0.142 (n=618)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 3558.8016 (IC base=+0.123)

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
- **PATRÓN** `delta_ratio` |x|> `0.4309` → IC=+0.139 (n=128)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio` |x|> 0.4309 (IC base=+0.111)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.133 (n=265)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 15.0 (IC base=+0.111)

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
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 13.0 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=176)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.097)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.6638` → IC=-0.259 (n=52)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.6638
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=158)

- **FILTRO** `pct_vs_K` |x|> `2.74` → IC=-0.167 (n=382)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.74
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=384)

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
- **FILTRO** `pct_vs_K` |x|> `6.9241` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.9241
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=51)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0102` → IC=-0.226 (n=71)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0102
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=73)

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
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=19)

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
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=4476)

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
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=2556)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.190 (n=1935)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0057 (IC base=+0.162)

- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.167 (n=1465)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0128 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.21` → IC=+0.174 (n=4394)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.21 (IC base=+0.162)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3523` → IC=+0.171 (n=4049)

  - _Acción_: Kelly boost +0.85€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3523 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.167 (n=4643)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 4.0 (IC base=+0.162)

- **PATRÓN** `ibs_15` > `0.5122` → IC=+0.232 (n=4395)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5122 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `0.13` → IC=+0.155 (n=2091)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.13 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.69` → IC=+0.268 (n=844)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.69 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `5218.8685` → IC=+0.181 (n=1465)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 5218.8685 (IC base=+0.162)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=1737)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.220 (n=712)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.0592` → IC=+0.254 (n=238)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0592 (IC base=+0.204)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2654` → IC=+0.224 (n=237)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2654 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.223 (n=742)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.204)

- **PATRÓN** `ibs_15` > `0.7141` → IC=+0.280 (n=711)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7141 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.3722` → IC=+0.223 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3722 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.92` → IC=+0.311 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.92 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=920)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `8052.1794` → IC=+0.212 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8052.1794 (IC base=+0.204)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.156 (n=871)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0068 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.1507` → IC=+0.148 (n=766)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.1507 (IC base=+0.135)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1432` → IC=+0.136 (n=580)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio_macro` |x|> 0.1432 (IC base=+0.135)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2833` → IC=+0.138 (n=700)

  - _Acción_: Kelly boost +0.69€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2833 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.143 (n=794)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 6.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.139 (n=914)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 17.0 (IC base=+0.135)

- **PATRÓN** `ibs_15` > `0.5034` → IC=+0.226 (n=870)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5034 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.1187` → IC=+0.149 (n=545)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1187 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.4301` → IC=+0.137 (n=925)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.4301 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.066` → IC=+0.284 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.066 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `5810.9052` → IC=+0.165 (n=395)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 5810.9052 (IC base=+0.135)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.875` → IC=+0.220 (n=369)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.875 (IC base=+0.080)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=547)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.080)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0194` → IC=+0.192 (n=664)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0194 (IC base=+0.183)

- **PATRÓN** `sigma_h` > `0.0227` → IC=+0.192 (n=452)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0227 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.207` → IC=+0.195 (n=996)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.207 (IC base=+0.183)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3508` → IC=+0.211 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3508 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.189 (n=893)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 14.0 (IC base=+0.183)

- **PATRÓN** `ibs_15` > `0.5849` → IC=+0.281 (n=890)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5849 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.4973` → IC=+0.220 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4973 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.462` → IC=+0.234 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.462 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `2330.8132` → IC=+0.204 (n=996)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2330.8132 (IC base=+0.183)

- **PATRÓN** `ibs_15` < `0.1076` → IC=+0.172 (n=848)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.86€ cuando `ibs_15` < 0.1076 (IC base=+0.068)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.387 (n=317)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1505` → IC=+0.378 (n=466)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1505 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1073` → IC=+0.384 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1073 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.376 (n=699)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.7883` → IC=+0.397 (n=699)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7883 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.1521` → IC=+0.383 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1521 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.204` → IC=+0.397 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.204 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.369 (n=848)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `3840.073` → IC=+0.374 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3840.073 (IC base=+0.365)

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

- **PATRÓN** `libro_liquidez` > `9161.247` → IC=+0.377 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9161.247 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `489.0` → IC=+0.403 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 489.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.366 (n=349)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.367)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.385 (n=232)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.367)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0833` → IC=+0.379 (n=311)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0833 (IC base=+0.367)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.380 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.367)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.378 (n=162)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.367)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.376 (n=159)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.367)

- **PATRÓN** `ibs_15` > `0.8138` → IC=+0.404 (n=311)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8138 (IC base=+0.367)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.376 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.367)

- **PATRÓN** `dist_vwap_pct` < `0.2918` → IC=+0.370 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2918 (IC base=+0.367)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.408` → IC=+0.406 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.408 (IC base=+0.367)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.372 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.367)

- **PATRÓN** `libro_liquidez` > `4039.5603` → IC=+0.394 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4039.5603 (IC base=+0.367)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0099` → IC=-0.216 (n=1641)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0099
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=3189)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.215 (n=1940)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=2890)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1392` → IC=+0.221 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1392 (IC base=-0.073)

- **PATRÓN** `ibs_15` > `0.6324` → IC=+0.281 (n=1134)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6324 (IC base=-0.073)

- **PATRÓN** `dist_vwap_pct` > `0.1115` → IC=+0.203 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1115 (IC base=-0.073)

- **PATRÓN** `dist_vwap_pct` < `0.4229` → IC=+0.200 (n=1115)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4229 (IC base=-0.073)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2339` → IC=+0.268 (n=1428)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2339 (IC base=-0.008)

- **PATRÓN** `ibs_15` < `0.3682` → IC=+0.283 (n=4284)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3682 (IC base=-0.008)

- **PATRÓN** `dist_vwap_pct` > `0.8693` → IC=+0.276 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8693 (IC base=-0.008)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0325` → IC=-0.223 (n=2274)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0325
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=760)

- **FILTRO** `sigma_h` < `0.0036` → IC=-0.222 (n=757)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0036
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=2277)

- **FILTRO** `sigma_ewma_delta_pct` > `22.67` → IC=-0.264 (n=435)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.67
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=2599)

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
  - _Potencial_: sin este filtro IC_bueno=+0.156 (n=737)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.161 (n=499)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0058 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.0722` → IC=+0.185 (n=249)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.0722 (IC base=+0.149)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.193 (n=438)

  - _Acción_: Kelly boost +0.97€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.167 (n=409)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 11.0 (IC base=+0.149)

- **PATRÓN** `ibs_15` > `0.5784` → IC=+0.243 (n=566)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5784 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.4658` → IC=+0.158 (n=147)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.4658 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.1598` → IC=+0.155 (n=441)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1598 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.049` → IC=+0.259 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.049 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=737)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `9459.3828` → IC=+0.154 (n=189)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 9459.3828 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.263 (n=542)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.1026` → IC=+0.243 (n=542)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1026 (IC base=+0.241)

- **PATRÓN** `drift_15min` |x|≤ `0.7701` → IC=+0.255 (n=1431)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7701 (IC base=+0.241)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1556` → IC=+0.259 (n=1085)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1556 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.246 (n=600)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.247 (n=610)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.241)

- **PATRÓN** `ibs_15` < `0.3777` → IC=+0.275 (n=1626)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3777 (IC base=+0.241)

- **PATRÓN** `dist_vwap_pct` > `0.6007` → IC=+0.269 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6007 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.291` → IC=+0.246 (n=718)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.291 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.226` → IC=+0.247 (n=1695)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.226 (IC base=+0.241)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0474` → IC=-0.208 (n=831)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0474
  - _Potencial_: sin este filtro IC_bueno=-0.129 (n=278)

- **FILTRO** `drift_60min` |x|> `0.1716` → IC=-0.246 (n=376)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1716
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=733)

- **FILTRO** `drift_15min` |x|> `0.8922` → IC=-0.278 (n=277)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8922
  - _Potencial_: sin este filtro IC_bueno=-0.158 (n=832)

- **FILTRO** `sigma_ewma_delta_pct` > `6.328` → IC=-0.200 (n=261)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.328
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=848)

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

- **PATRÓN** `delta_ratio_macro` |x|> `0.0652` → IC=+0.223 (n=731)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0652 (IC base=-0.034)

- **PATRÓN** `ibs_15` < `0.3939` → IC=+0.293 (n=731)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3939 (IC base=-0.034)

- **PATRÓN** `dist_vwap_pct` < `0.2722` → IC=+0.238 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2722 (IC base=-0.034)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0565` → IC=-0.231 (n=994)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0565
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=332)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.248 (n=618)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=708)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.212)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.212)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0516` → IC=+0.273 (n=964)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0516 (IC base=-0.024)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1182` → IC=+0.291 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1182 (IC base=-0.024)

- **PATRÓN** `ibs_15` < `0.1351` → IC=+0.309 (n=642)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1351 (IC base=-0.024)

- **PATRÓN** `dist_vwap_pct` > `0.7681` → IC=+0.341 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7681 (IC base=-0.024)

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
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.291 (n=1228)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.0543` → IC=+0.318 (n=410)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0543 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1511` → IC=+0.288 (n=818)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1511 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.223` → IC=+0.298 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.223 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.302 (n=1273)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.8395` → IC=+0.316 (n=1228)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8395 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.2663` → IC=+0.317 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2663 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.204` → IC=+0.379 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.204 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `13580.5333` → IC=+0.308 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13580.5333 (IC base=+0.287)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.309 (n=218)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.0592` → IC=+0.318 (n=218)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0592 (IC base=+0.281)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2673` → IC=+0.283 (n=219)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2673 (IC base=+0.281)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3892` → IC=+0.287 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3892 (IC base=+0.281)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.300 (n=684)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.281)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.306 (n=654)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.829 (IC base=+0.281)

- **PATRÓN** `dist_vwap_pct` > `0.2516` → IC=+0.314 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2516 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.503` → IC=+0.380 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.503 (IC base=+0.281)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.281 (n=844)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `12498.3913` → IC=+0.306 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12498.3913 (IC base=+0.281)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.308 (n=575)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.1075` → IC=+0.314 (n=384)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1075 (IC base=+0.293)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1451` → IC=+0.295 (n=383)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1451 (IC base=+0.293)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.101` → IC=+0.344 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.101 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.309 (n=552)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.298 (n=524)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.293)

- **PATRÓN** `ibs_15` > `0.8743` → IC=+0.328 (n=515)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8743 (IC base=+0.293)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5122 sube el IC de +0.162 a +0.232 en UPDOWN_GBM#15min (n=4395). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7141 sube el IC de +0.204 a +0.280 en UPDOWN_GBM#BTC#15min (n=711). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5034 sube el IC de +0.135 a +0.226 en UPDOWN_GBM#ETH#15min (n=870). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.875 sube el IC de +0.080 a +0.220 en UPDOWN_GBM#SOL#15min (n=369). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5849 sube el IC de +0.183 a +0.281 en UPDOWN_GBM#XRP#15min (n=890). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1076 sube el IC de +0.068 a +0.172 en UPDOWN_GBM#XRP#15min (n=848). Ya aplicado como kelly_boost=+0.86€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6324 sube el IC de -0.073 a +0.281 en UPDOWN_GBM_15M_TARDIO (n=1134). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3682 sube el IC de -0.008 a +0.283 en UPDOWN_GBM_15M_TARDIO (n=4284). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7639 sube el IC de +0.077 a +0.330 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=385). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6221 sube el IC de -0.188 a +0.319 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=70). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5784 sube el IC de +0.149 a +0.243 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=566). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3777 sube el IC de +0.241 a +0.275 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1626). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.189 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3939 sube el IC de -0.034 a +0.293 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=731). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.212 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.1351 sube el IC de -0.024 a +0.309 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=642). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.093 a +0.364 en UPDOWN_GBM_ETH_15M_HORA7 (n=20). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.093 a +0.364 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=20). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8395 sube el IC de +0.287 a +0.316 en UPDOWN_GBM_IBS_ALTO (n=1228). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.281 a +0.306 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=654). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8743 sube el IC de +0.293 a +0.328 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=515). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7883 sube el IC de +0.365 a +0.397 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=699). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8077 sube el IC de +0.362 a +0.387 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=352). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.8138 sube el IC de +0.367 a +0.404 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=311). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

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
| ✅ BALLENAS_TARDIAS | 44389 | -0.085 | -5550.24€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2639 | +0.057 | -283.59€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 41750 | -0.094 | -5266.66€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4648 | -0.116 | -759.61€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4648 | -0.116 | -759.61€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2639 | +0.057 | -283.59€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2639 | +0.057 | -283.59€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4602 | -0.116 | -897.77€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4602 | -0.116 | -897.77€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 11955 | -0.029 | -1039.36€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 11955 | -0.029 | -1039.36€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 12020 | -0.120 | -1204.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 12020 | -0.120 | -1204.30€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8525 | -0.126 | -1365.61€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8525 | -0.126 | -1365.61€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 43094 | -0.013 | +3158.53€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 11117 | +0.005 | +1597.62€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 31977 | -0.019 | +1560.90€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 43094 | -0.013 | +3158.53€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 11117 | +0.005 | +1597.62€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 31977 | -0.019 | +1560.90€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 169818 | +0.114 | -6891.70€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 20602 | +0.180 | -675.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 767 | -0.003 | -77.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 138558 | +0.106 | -5785.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 9891 | +0.092 | -352.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 22958 | +0.106 | -1478.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 68 | -0.186 | +4.73€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 22875 | +0.107 | -1470.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 32500 | +0.125 | -527.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5527 | +0.180 | -224.75€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 22946 | +0.120 | -149.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3985 | +0.078 | -130.95€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 23012 | +0.098 | -1647.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 82 | -0.119 | -3.25€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 22915 | +0.100 | -1632.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 36200 | +0.124 | -716.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 9234 | +0.178 | -199.94€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 23294 | +0.106 | -455.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3660 | +0.101 | -52.19€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 32162 | +0.112 | -1512.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5612 | +0.198 | -257.90€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 670 | +0.025 | -23.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 23634 | +0.095 | -1061.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2246 | +0.104 | -169.56€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO#XRP | 22986 | +0.107 | -1009.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 79 | -0.117 | +5.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 22894 | +0.108 | -1015.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 27431 | +0.195 | -1776.77€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 27431 | +0.195 | -1776.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 6198 | +0.177 | -560.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 6198 | +0.177 | -560.40€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 3772 | +0.201 | -109.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 3772 | +0.201 | -109.75€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 6126 | +0.176 | -528.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 6126 | +0.176 | -528.49€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5222 | +0.249 | -187.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5222 | +0.249 | -187.40€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 6034 | +0.186 | -404.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 6034 | +0.186 | -404.48€ | 0 | 4 |
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
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 96472 | +0.201 | -6943.85€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 96472 | +0.201 | -6943.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 16621 | +0.182 | -1788.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 16621 | +0.182 | -1788.63€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 15558 | +0.225 | -498.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 15558 | +0.225 | -498.31€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 16559 | +0.181 | -1736.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 16559 | +0.181 | -1736.57€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 15688 | +0.218 | -623.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 15688 | +0.218 | -623.88€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 15973 | +0.202 | -1032.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 15973 | +0.202 | -1032.11€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 16073 | +0.198 | -1264.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 16073 | +0.198 | -1264.36€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 37027 | +0.117 | +294.95€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 37027 | +0.117 | +294.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 18432 | +0.118 | +187.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 18432 | +0.118 | +187.59€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 18595 | +0.116 | +107.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 18595 | +0.116 | +107.36€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2359 | +0.295 | +5.36€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2359 | +0.295 | +5.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1077 | +0.283 | -17.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1077 | +0.283 | -17.67€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1151 | +0.300 | +21.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1151 | +0.300 | +21.07€ | 0 | 4 |
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
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1842 | +0.068 | -81.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1117 | +0.082 | -17.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1408 | +0.076 | -36.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1117 | +0.082 | -17.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 74383 | +0.101 | -1798.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 5989 | +0.094 | +98.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 68394 | +0.101 | -1897.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 40736 | +0.106 | -407.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 5989 | +0.094 | +98.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 34747 | +0.108 | -506.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 15615 | +0.109 | -78.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 15615 | +0.109 | -78.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 18032 | +0.082 | -1311.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 18032 | +0.082 | -1311.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 912 | +0.186 | -109.79€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 912 | +0.186 | -109.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 912 | +0.186 | -109.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 912 | +0.186 | -109.79€ | 2 | 4 |
| ✅ GBM_LATE_15M | 50641 | +0.096 | +27655.74€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 50641 | +0.096 | +27655.74€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 8423 | +0.222 | +7144.79€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 8423 | +0.222 | +7144.79€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 7713 | +0.175 | +5983.39€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 7713 | +0.175 | +5983.39€ | 0 | 26 |
| ✅ GBM_LATE_15M#DOGE | 9084 | +0.205 | +7085.66€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 9084 | +0.205 | +7085.66€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 6917 | +0.048 | +2046.99€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 6917 | +0.048 | +2046.99€ | 1 | 19 |
| ✅ GBM_LATE_15M#SOL | 7077 | -0.032 | +1807.39€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 7077 | -0.032 | +1807.39€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 11427 | -0.026 | +3587.52€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 11427 | -0.026 | +3587.52€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 53544 | +0.085 | +30390.62€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 53544 | +0.085 | +30390.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 10429 | -0.000 | +5382.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 10429 | -0.000 | +5382.30€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 11443 | +0.005 | +2920.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 11443 | +0.005 | +2920.14€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 7346 | +0.288 | +8187.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 7346 | +0.288 | +8187.81€ | 0 | 23 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 9993 | +0.014 | +2991.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 9993 | +0.014 | +2991.06€ | 1 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 8321 | +0.041 | +3621.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 8321 | +0.041 | +3621.58€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 6012 | +0.313 | +7287.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 6012 | +0.313 | +7287.74€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 40166 | +0.179 | +32913.93€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 40166 | +0.179 | +32913.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 6054 | +0.237 | +5571.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 6054 | +0.237 | +5571.64€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 6364 | +0.141 | +4699.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 6364 | +0.141 | +4699.95€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 6449 | +0.225 | +5582.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 6449 | +0.225 | +5582.33€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 6856 | +0.132 | +5283.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 6856 | +0.132 | +5283.95€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 7581 | +0.120 | +5617.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 7581 | +0.120 | +5617.10€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 6862 | +0.231 | +6158.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 6862 | +0.231 | +6158.96€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 10624 | +0.124 | +5189.26€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 10624 | +0.124 | +5189.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 461 | +0.157 | +289.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 461 | +0.157 | +289.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3065 | +0.128 | +1660.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3065 | +0.128 | +1660.02€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 491 | +0.153 | +259.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 491 | +0.153 | +259.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3157 | +0.128 | +1532.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3157 | +0.128 | +1532.65€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2681 | +0.093 | +1024.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2681 | +0.093 | +1024.86€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 769 | +0.154 | +422.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 769 | +0.154 | +422.51€ | 0 | 29 |
| ✅ GBM_LATE_15M_TARDIO | 50884 | +0.185 | +41356.16€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 50884 | +0.185 | +41356.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 8042 | +0.247 | +7679.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 8042 | +0.247 | +7679.53€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 8043 | +0.138 | +5522.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 8043 | +0.138 | +5522.11€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 8622 | +0.233 | +7717.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 8622 | +0.233 | +7717.77€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 8421 | +0.139 | +6098.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 8421 | +0.139 | +6098.84€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 9024 | +0.120 | +6347.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 9024 | +0.120 | +6347.67€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 8732 | +0.238 | +7990.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 8732 | +0.238 | +7990.23€ | 0 | 21 |
| ✅ GBM_LATE_5M | 13345 | +0.208 | +10725.23€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 13345 | +0.208 | +10725.23€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3192 | +0.211 | +2758.98€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3192 | +0.211 | +2758.98€ | 0 | 26 |
| ✅ GBM_LATE_5M#DOGE | 1223 | +0.198 | +915.88€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1223 | +0.198 | +915.88€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 3884 | +0.201 | +2890.97€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3884 | +0.201 | +2890.97€ | 0 | 24 |
| ✅ GBM_LATE_5M#SOL | 2034 | +0.201 | +1623.92€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2034 | +0.201 | +1623.92€ | 0 | 26 |
| ✅ GBM_LATE_5M#XRP | 1958 | +0.209 | +1535.21€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1958 | +0.209 | +1535.21€ | 0 | 0 |
| ✅ GBM_LATE_60M | 4387 | +0.051 | +1222.73€ | 0 | 6 |
| ✅ GBM_LATE_60M#60min | 4387 | +0.051 | +1222.73€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1557 | +0.067 | +512.38€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1557 | +0.067 | +512.38€ | 0 | 5 |
| ✅ GBM_LATE_60M#ETH | 1422 | +0.051 | +436.33€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1422 | +0.051 | +436.33€ | 1 | 6 |
| ✅ GBM_LATE_60M#SOL | 1408 | +0.035 | +274.02€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1408 | +0.035 | +274.02€ | 0 | 8 |
| 🚫 GBM_LATE_60M_FADE | 653 | -0.250 | -32.35€ | 9 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 653 | -0.250 | -32.35€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 245 | -0.249 | -18.41€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 245 | -0.249 | -18.41€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 236 | -0.244 | -6.25€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 236 | -0.244 | -6.25€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 172 | -0.253 | -7.69€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 172 | -0.253 | -7.69€ | 6 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1785 | +0.080 | +443.61€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1785 | +0.080 | +443.61€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 692 | +0.068 | +148.64€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 692 | +0.068 | +148.64€ | 1 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 608 | +0.056 | +107.82€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 608 | +0.056 | +107.82€ | 2 | 15 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 485 | +0.126 | +187.15€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 485 | +0.126 | +187.15€ | 1 | 10 |
| ✅ LATE_WINDOW_5MIN | 198 | +0.270 | +203.69€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 198 | +0.270 | +203.69€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 198 | +0.270 | +203.69€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 198 | +0.270 | +203.69€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4040 | +0.098 | +940.35€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4040 | +0.098 | +940.35€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4040 | +0.098 | +940.35€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4040 | +0.098 | +940.35€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 777 | -0.012 | +8.93€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 777 | -0.012 | +8.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 7 | -0.058 | -1.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 7 | -0.058 | -1.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 236 | +0.000 | +7.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 236 | +0.000 | +7.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 27 | -0.155 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 27 | -0.155 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 202 | +0.029 | +13.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 202 | +0.029 | +13.84€ | 2 | 3 |
| ✅ LIQUIDACIONES_15M#SOL | 253 | -0.002 | +3.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 253 | -0.002 | +3.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4042 | +0.017 | +106.17€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 4042 | +0.017 | +106.17€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 189 | +0.034 | +0.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 189 | +0.034 | +0.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 818 | +0.016 | +41.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 818 | +0.016 | +41.53€ | 1 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 216 | +0.000 | +1.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 216 | +0.000 | +1.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1586 | +0.022 | +31.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1586 | +0.022 | +31.45€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 763 | +0.011 | +1.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 763 | +0.011 | +1.66€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 470 | +0.015 | +29.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 470 | +0.015 | +29.46€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2088 | -0.040 | -28.42€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2088 | -0.040 | -28.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 628 | -0.033 | -14.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 628 | -0.033 | -14.28€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 729 | -0.017 | +8.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 729 | -0.017 | +8.04€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 731 | -0.068 | -22.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 731 | -0.068 | -22.18€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 12343 | -0.031 | -80.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 5916 | -0.035 | -81.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 6427 | -0.027 | +1.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 430 | -0.049 | -21.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 215 | -0.021 | +2.18€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 215 | -0.076 | -23.20€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 3198 | -0.021 | +25.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1522 | -0.022 | +11.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1676 | -0.020 | +14.60€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1274 | -0.022 | +32.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 648 | -0.032 | +2.25€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 626 | -0.011 | +29.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 2750 | -0.037 | -68.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1300 | -0.042 | -46.62€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1450 | -0.034 | -22.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 2376 | -0.030 | -11.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1148 | -0.037 | -22.21€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1228 | -0.024 | +10.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 2315 | -0.039 | -36.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1083 | -0.046 | -28.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1232 | -0.033 | -8.19€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 59779 | -0.000 | +3122.35€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 59779 | -0.000 | +3122.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 10801 | +0.027 | +1431.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 10801 | +0.027 | +1431.33€ | 2 | 3 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 8461 | -0.036 | -114.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 8461 | -0.036 | -114.66€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 10936 | +0.024 | +1139.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 10936 | +0.024 | +1139.82€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 8361 | -0.049 | -175.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 8361 | -0.049 | -175.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 10149 | -0.005 | +277.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 10149 | -0.005 | +277.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 11071 | +0.017 | +564.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 11071 | +0.017 | +564.23€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6962 | -0.056 | -133.31€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6962 | -0.056 | -133.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1237 | -0.002 | -17.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1237 | -0.002 | -17.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1908 | -0.069 | -34.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1908 | -0.069 | -34.40€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 67 | -0.007 | +0.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 67 | -0.007 | +0.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 793 | -0.119 | -33.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 793 | -0.119 | -33.68€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2099 | -0.069 | -22.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2099 | -0.069 | -22.55€ | 4 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 147397 | -0.077 | +2026.51€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 147397 | -0.077 | +2026.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 25730 | -0.078 | +1385.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 25730 | -0.078 | +1385.49€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 22110 | -0.100 | -1060.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 22110 | -0.100 | -1060.56€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 26064 | -0.069 | +1252.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 26064 | -0.069 | +1252.85€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 21653 | -0.097 | -644.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 21653 | -0.097 | -644.14€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 26401 | -0.057 | +354.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 26401 | -0.057 | +354.84€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 25439 | -0.069 | +738.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 25439 | -0.069 | +738.03€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8949 | -0.035 | -185.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8949 | -0.035 | -185.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1002 | -0.017 | -19.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1002 | -0.017 | -19.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2062 | -0.047 | -28.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2062 | -0.047 | -28.58€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2624 | -0.026 | -39.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2624 | -0.026 | -39.96€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1249 | -0.062 | -33.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1249 | -0.062 | -33.22€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1003 | -0.030 | -32.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1003 | -0.030 | -32.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 1953 | +0.118 | +766.45€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1817 | +0.123 | +753.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 425 | +0.125 | +193.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 425 | +0.125 | +193.17€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 376 | +0.111 | +123.45€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 376 | +0.111 | +123.45€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 349 | +0.135 | +170.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 349 | +0.135 | +170.30€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 317 | +0.146 | +168.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 317 | +0.146 | +168.10€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 350 | +0.097 | +98.83€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 350 | +0.097 | +98.83€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1837 | -0.019 | -33.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1837 | -0.019 | -33.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 342 | +0.003 | +12.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 342 | +0.003 | +12.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 333 | -0.037 | -14.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 333 | -0.037 | -14.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 474 | -0.042 | -34.45€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 474 | -0.042 | -34.45€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 379 | +0.001 | +1.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 379 | +0.001 | +1.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 309 | -0.011 | +1.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 309 | -0.011 | +1.48€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1043 | -0.077 | -49.89€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 480 | -0.110 | -79.15€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 374 | -0.130 | -63.03€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 106 | -0.037 | -16.12€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 367 | -0.037 | +22.97€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 262 | -0.023 | +28.94€ | 1 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 105 | -0.070 | -5.97€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 196 | -0.071 | +6.29€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 162 | -0.073 | +3.43€ | 1 | 0 |
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
| ✅ STREAK_FADE_60M | 110 | -0.036 | -7.34€ | 2 | 0 |
| ✅ STREAK_FADE_60M#60min | 110 | -0.036 | -7.34€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 43 | -0.100 | -5.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 43 | -0.100 | -5.07€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 67 | +0.007 | -2.27€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 67 | +0.007 | -2.27€ | 0 | 2 |
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
| ✅ STRUCT_NO_15M | 10715 | +0.014 | -46.57€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 10715 | +0.014 | -46.57€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4495 | +0.019 | -5.28€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4495 | +0.019 | -5.28€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3630 | +0.010 | -28.88€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3630 | +0.010 | -28.88€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2590 | +0.010 | -12.41€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2590 | +0.010 | -12.41€ | 1 | 0 |
| ✅ UPDOWN_GBM | 91636 | +0.058 | +8617.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 22247 | +0.084 | +4853.89€ | 0 | 9 |
| ✅ UPDOWN_GBM#240min | 2867 | +0.001 | +30.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 60759 | +0.057 | +3639.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 5440 | +0.002 | +98.50€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 7553 | +0.100 | +1338.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1703 | +0.165 | +795.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5760 | +0.083 | +544.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 20987 | +0.057 | +1822.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3028 | +0.083 | +687.44€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 799 | +0.003 | +13.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 14593 | +0.065 | +1049.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2450 | +0.000 | +68.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 117 | -0.071 | +3.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 9806 | +0.076 | +1131.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1682 | +0.156 | +714.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 8038 | +0.060 | +418.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 21783 | +0.048 | +1486.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 5371 | +0.072 | +811.16€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 766 | +0.006 | +18.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 13541 | +0.049 | +629.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1997 | +0.005 | +26.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 108 | -0.109 | +1.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 19727 | +0.038 | +1131.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 5745 | +0.037 | +471.04€ | 0 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 729 | -0.010 | +2.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 12164 | +0.046 | +660.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 993 | +0.001 | +4.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 96 | -0.143 | -7.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 11778 | +0.071 | +1709.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4718 | +0.101 | +1374.22€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 6663 | +0.053 | +337.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 321 | -0.107 | -2.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 932 | +0.365 | +341.58€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 932 | +0.365 | +341.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 469 | +0.362 | +164.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 469 | +0.362 | +164.30€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 463 | +0.367 | +177.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 463 | +0.367 | +177.27€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 22490 | -0.022 | +5436.04€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 22490 | -0.022 | +5436.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1890 | -0.054 | +531.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1890 | -0.054 | +531.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 4211 | -0.114 | +201.49€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 4211 | -0.114 | +201.49€ | 3 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1021 | +0.222 | +857.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1021 | +0.222 | +857.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2921 | +0.217 | +1849.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2921 | +0.217 | +1849.19€ | 1 | 20 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 6361 | -0.061 | +896.32€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 6361 | -0.061 | +896.32€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 6086 | -0.065 | +1099.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 6086 | -0.065 | +1099.72€ | 2 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 270 | +0.062 | +25.25€ | 0 | 7 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 270 | +0.062 | +25.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 270 | +0.062 | +25.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 270 | +0.062 | +25.25€ | 0 | 7 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1637 | +0.287 | +1378.00€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1637 | +0.287 | +1378.00€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 871 | +0.281 | +687.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 871 | +0.281 | +687.56€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 766 | +0.293 | +690.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 766 | +0.293 | +690.44€ | 0 | 9 |
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
| ✅ WEEKLY_PRICE | 4200 | +0.303 | +1949.34€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 1575 | +0.259 | +200.62€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1614 | +0.296 | +700.97€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1011 | +0.381 | +1047.75€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.039) — sin ventaja clara. oversold(IBS<0.3): IC=+0.069 n=31897 | neutral: IC=+0.061 n=33895 | overbought(IBS>0.7): IC=+0.100 n=31867
  - _Datos_: n=101588 IC=+0.077 PNL=+15451.09€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 767 celda(s) pasan gate riguroso completo de 2807 evaluadas (n>=40) y 3908 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.037 < 0.08 — monitorear
  - _Datos_: n=5741 IC=+0.037 PNL=+471.18€

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

**⏳ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: 15
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: Falta 11 ops más en GBM@18h (IC actual=-0.067)
  - _Datos_: n=4 IC=-0.067 PNL=-3.02€

**⏳ H-HORA-GBM** — hora_utc causal automático en GBM (forward)
  - _Umbral_: n≥20 forward con hora_utc + alguna hora con n≥15 IC<-0.10 o >+0.10
  - _Acción_: El sistema lo aplica automáticamente vía FEATURE_RULES. Verificar en strategy_params.json.
  - _Estado_: 91538 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.148 n=977/60 | contraria IC=+0.189 n=1007 | gap=-0.041 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=540, boost estimado=+0.016. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 317 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1995/40 IC=+0.005 PNL=+25.84€ | BTC#60min: n=2449/40 IC=+0.000 PNL=+68.61€ | SOL#60min: n=991/40 IC=+0.001 PNL=+4.10€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.046 n=653456 | tras_1loss IC=+0.098 n=496058 | tras_2loss IC=+0.067 n=199576/40 | gap=-0.021 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.042 n=13470 | contrario_BTC IC=+0.054 n=11834/40 | gap=+0.013 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.154 > 0.08 con n=1061 PNL=+563.38€
  - _Datos_: n=1061 IC=+0.154 PNL=+563.38€

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
  - _Estado_: n=902 IC=+0.070 PNL=+91.70€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=902 IC=+0.070 PNL=+91.70€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=98 IC=+0.190 PNL=+68.62€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=98 IC=+0.190 PNL=+68.62€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=87563 IC=+0.058 PNL=+8314.29€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=87563 IC=+0.058 PNL=+8314.29€

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
  - _Estado_: n=3646 IC=+0.005 PNL=-0.97€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3646 IC=+0.005 PNL=-0.97€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1789 IC=-0.004 PNL=+99.51€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1789 IC=-0.004 PNL=+99.51€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.162 > 0.1 con n=5855 PNL=+3356.57€
  - _Datos_: n=5855 IC=+0.162 PNL=+3356.57€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=2930 IC=+0.068 PNL=+220.21€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2930 IC=+0.068 PNL=+220.21€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=3028 IC=+0.083 PNL=+687.44€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=3028 IC=+0.083 PNL=+687.44€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 1/50 ops en el filtro definido (IC actual=+0.008 PNL=+1.17€)
  - _Datos_: n=1 IC=+0.008 PNL=+1.17€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: confirmada 2026-07-01 (IC=-0.037 n=52) e implementada en shadow_predict.py (skip si drift_15min∈[-0.3,0.3)) -- verificado 26-Ago con 2177 filas post-TWAP reales, 0 caen en la zona filtrada. Frozen by design, no falta n

**🟡 H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.098 > 0.08 con n=12927 PNL=+3548.48€
  - _Datos_: n=12927 IC=+0.098 PNL=+3548.48€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=578 IC=-0.233 PNL=-8.86€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=578 IC=-0.233 PNL=-8.86€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=519 IC=-0.022 PNL=-7.23€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=519 IC=-0.022 PNL=-7.23€

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

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=10791 IC=+0.034 PNL=+476.20€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=10791 IC=+0.034 PNL=+476.20€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.108 > 0.08 con n=480 PNL=+92.46€
  - _Datos_: n=480 IC=+0.108 PNL=+92.46€

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.270 n=198) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=198 IC=+0.270 PNL=+203.69€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=14707 IC=+0.056 PNL=+1364.29€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=14707 IC=+0.056 PNL=+1364.29€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=5501 IC=+0.061 PNL=+823.02€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=5501 IC=+0.061 PNL=+823.02€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.109 > 0.08 con n=645 PNL=+207.38€
  - _Datos_: n=645 IC=+0.109 PNL=+207.38€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.132 > 0.08 con n=1462 PNL=+399.83€
  - _Datos_: n=1462 IC=+0.132 PNL=+399.83€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.090 > 0.08 con n=1181 PNL=+481.05€
  - _Datos_: n=1181 IC=+0.090 PNL=+481.05€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=94138 IC=+0.125 PNL=+38016.83€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=94138 IC=+0.125 PNL=+38016.83€

**〰️ H-CUSTOM-MERCURY-RETROGRADO** — Mercurio retrógrado: ¿rendimiento peor durante la ventana?
  - _Hipótesis_: Mismo origen que H-CUSTOM-MOON-LLENA (paper de Fornero, 43 Jornadas SADAF 2023). Qi, Wang & Zhang (2022, 48 mercados, 1973-2019): rendimientos 3.33%/año más bajos durante Mercurio retrógrado. Kou & Ma (2022) en China (99.8% cuentas retail): hasta -31% anualizado. Ambos estudios confirman que el mecanismo es la creencia/superstición de inversores retail (mayor efecto cuanto más retail y más supersticioso el mercado), no un efecto astral literal — Polymarket encaja en ese perfil. Ventanas 2026 (fuente pública, actualizar cada año): 26-feb a 20-mar, 29-jun a 23-jul, 24-oct a 13-nov.
  - _Umbral_: n≥100 PERO ADEMÁS necesita cubrir al menos 2-3 ventanas de retrogradación distintas (no solo la de jun-jul 2026) — esperar mínimo hasta después de la ventana de oct-nov 2026
  - _Acción_: Si IC en mercury_retrogrado=1 < IC en mercury_retrogrado=0 con margen ≥0.05 y ≥2 ventanas distintas cubiertas → considerar boost/filtro. No implementar tras una sola ventana (jun-jul 2026) por more que n sea alto — sería solo un evento, no un patrón.
  - _Estado_: n=45766 IC=+0.139 PNL=+21002.52€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=45766 IC=+0.139 PNL=+21002.52€

**〰️ H-CUSTOM-SMART-MONEY-CONSENSUS** — Consenso de wallets 'smart money' — ¿confirma nuestra dirección?
  - _Hipótesis_: Javi propuso estudiar bots/wallets que operan bien en nuestros mismos mercados. En vez de creer artículos (ya verificamos 2 veces esta semana que las narrativas no aguantan el cruce con datos reales), smart_money_tracker.py mide el track record REAL de wallets activas en BTC/ETH/SOL/XRP Up-or-Down 5/15/60min vía data-api.polymarket.com/positions, filtrado a posiciones 'Up or Down'. Clasifica como 'smart' las wallets con n>=10 posiciones, win_rate>=0.55 y pnl_total>0. smart_money_consensus es el sesgo direccional reciente (Up-Down)/(Up+Down) de esas wallets 'smart' por activo. Hipótesis: si nuestra decisión (BUY_YES/BUY_NO) coincide con el consenso smart money, mejor IC que cuando diverge. RESET METODOLOGICO 2026-07-02: la clasificacion 'smart' original via /positions estaba INVERTIDA para wallets de alta frecuencia (el endpoint solo retiene el residuo perdedor sin redimir; verificado: 'wowitsamazing' figuraba como -$478k y es +$10k/mes en el leaderboard oficial). Desde 2026-07-02T06:12Z el consenso se construye solo con wallets verificadas en el leaderboard oficial (pnl_mes>=$1000, 24 wallets). Los valores de smart_money_consensus capturados en features ANTES de esa fecha provienen de la clasificacion rota — descontar ese tramo al evaluar.
  - _Umbral_: n≥40 y IC>+0.08 — además necesita que existan wallets 'smart' acumuladas (0 al empezar, se van descubriendo cada ciclo)
  - _Acción_: Si IC en confluencia (decisión coincide con signo de smart_money_consensus) supera en >=0.05 al IC en divergencia, con n≥40 en cada lado → boost ×1.1-1.2 cuando coincide, considerar reducir stake cuando diverge fuerte.
  - _Estado_: n=13737 IC=+0.059 PNL=+1393.75€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=13737 IC=+0.059 PNL=+1393.75€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.123 > 0.02 con n=1146 PNL=+476.17€
  - _Datos_: n=1146 IC=+0.123 PNL=+476.17€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=239 IC=-0.110 PNL=+10.85€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=239 IC=-0.110 PNL=+10.85€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.451 > 0.1 con n=1926 PNL=+1881.34€
  - _Datos_: n=1926 IC=+0.451 PNL=+1881.34€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=37012 IC=+0.075 PNL=+5323.69€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=37012 IC=+0.075 PNL=+5323.69€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.201 > 0.1 con n=8040 PNL=+4638.70€
  - _Datos_: n=8040 IC=+0.201 PNL=+4638.70€

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
  - _Estado_: n=3388 IC=+0.068 PNL=+450.01€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=3388 IC=+0.068 PNL=+450.01€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.106 > 0.1 con n=969 PNL=+250.35€
  - _Datos_: n=969 IC=+0.106 PNL=+250.35€

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
  - _Estado_: n=38648 IC=-0.136 PNL=+2651.69€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=38648 IC=-0.136 PNL=+2651.69€

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
  - _Estado_: n=3979 IC=+0.126 PNL=+2520.12€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=3979 IC=+0.126 PNL=+2520.12€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.196 > 0.08 con n=4821 PNL=+3399.98€
  - _Datos_: n=4821 IC=+0.196 PNL=+3399.98€

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

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.204 > 0.08 con n=946 PNL=+516.82€
  - _Datos_: n=946 IC=+0.204 PNL=+516.82€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.220 < -0.1 con n=4147 PNL=-328.51€
  - _Datos_: n=4147 IC=-0.220 PNL=-328.51€

**🟡 H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.218 > 0.2 con n=10342 PNL=+8457.70€
  - _Datos_: n=10342 IC=+0.218 PNL=+8457.70€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.113 > 0.08 con n=140 PNL=+57.18€
  - _Datos_: n=140 IC=+0.113 PNL=+57.18€

**🟡 H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.086 > 0.08 con n=3724 PNL=+1359.89€
  - _Datos_: n=3724 IC=+0.086 PNL=+1359.89€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.172 > 0.08 con n=3575 PNL=+2763.42€
  - _Datos_: n=3575 IC=+0.172 PNL=+2763.42€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=5972 IC=-0.022 PNL=+1811.75€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=5972 IC=-0.022 PNL=+1811.75€

**〰️ H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: n=728 IC=+0.073 PNL=-37.45€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=728 IC=+0.073 PNL=-37.45€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.242 > 0.08 con n=5418 PNL=-430.34€
  - _Datos_: n=5418 IC=+0.242 PNL=-430.34€

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.096 n=2049) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2049 IC=+0.096 PNL=+416.10€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.301 > 0.08 con n=592 PNL=+153.56€
  - _Datos_: n=592 IC=+0.301 PNL=+153.56€

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
  - _Estado_: n=16611 IC=+0.183 PNL=-1784.90€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=16611 IC=+0.183 PNL=-1784.90€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.226 > 0.1 con n=261 PNL=+177.93€
  - _Datos_: n=261 IC=+0.226 PNL=+177.93€
