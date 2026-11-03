# Hipótesis automáticas — 2026-11-03 16:51 UTC
_Generado por shadow_postmortem.py sobre 1177942 resoluciones (PNL=+160008.53€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **PATRÓN** `py_entrada` > `0.505` → IC=+0.202 (n=990)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.134)

- **PATRÓN** `n_total_lado` > `63.0` → IC=+0.185 (n=312)

  - _Acción_: Kelly boost +0.92€ cuando `n_total_lado` > 63.0 (IC base=+0.134)

- **PATRÓN** `banda_hit_calibrado` > `0.6159` → IC=+0.252 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6159 (IC base=+0.134)

- **PATRÓN** `banda_z` > `8.822` → IC=+0.209 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.822 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.157 (n=339)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.149 (n=1002)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `3328.7097` → IC=+0.138 (n=614)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 3328.7097 (IC base=+0.134)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.505` → IC=+0.200 (n=855)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.138)

- **PATRÓN** `n_total_lado` > `67.0` → IC=+0.192 (n=264)

  - _Acción_: Kelly boost +0.96€ cuando `n_total_lado` > 67.0 (IC base=+0.138)

- **PATRÓN** `banda_hit_calibrado` > `0.6106` → IC=+0.239 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6106 (IC base=+0.138)

- **PATRÓN** `banda_z` > `9.04` → IC=+0.207 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.04 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=287)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=902)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `3054.6814` → IC=+0.140 (n=706)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3054.6814 (IC base=+0.138)

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

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.5 (IC base=+0.151)

- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 26.0 (IC base=+0.151)

- **PATRÓN** `n_total_lado` > `43.0` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 43.0 (IC base=+0.151)

- **PATRÓN** `banda_hit_calibrado` > `0.6054` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `banda_hit_calibrado` > 0.6054 (IC base=+0.151)

- **PATRÓN** `banda_z` > `2.495` → IC=+0.220 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 2.495 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.269 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.151)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.214 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `2453.7234` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2453.7234 (IC base=+0.151)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `135.31` → IC=-0.215 (n=11240)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 135.31
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=33723)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `127.47` → IC=-0.254 (n=1175)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.47
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=3526)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `117.35` → IC=-0.308 (n=1162)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 117.35
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=3491)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `119.07` → IC=-0.151 (n=3055)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 119.07
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=9168)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `156.62` → IC=-0.242 (n=3038)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 156.62
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=9121)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `131.84` → IC=-0.255 (n=2141)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.84
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=6423)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.212 (n=25604)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `8541.8866` → IC=+0.161 (n=2235)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 8541.8866 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=21793)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=26698)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.224 (n=20226)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=7943)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6754.6293` → IC=+0.150 (n=3068)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 6754.6293 (IC base=+0.124)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=2073)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.364 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.179)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=2660)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `9413.2764` → IC=+0.182 (n=1851)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 9413.2764 (IC base=+0.179)

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
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=2055)

- **PATRÓN** `py_entrada` > `0.61` → IC=+0.172 (n=553)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` > 0.61 (IC base=+0.074)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.142 (n=1307)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.44 (IC base=+0.081)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=4923)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.167 (n=4175)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 15.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.374 (n=1560)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.215 (n=2216)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` < `0.27` → IC=+0.344 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.27 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=2574)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.149 (n=1069)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 15.0 (IC base=+0.142)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.258 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.143 (n=1388)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `3079.6088` → IC=+0.135 (n=231)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 3079.6088 (IC base=+0.070)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.256 (n=920)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.421 (n=1284)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.149 (n=1376)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=712)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.146)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.286 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.146)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `py_entrada` > `0.55` → IC=+0.159 (n=452)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` > 0.55 (IC base=+0.051)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.133 (n=1174)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 7.0 (IC base=+0.122)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.244 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.122)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.297 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.228 (n=145)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=21952)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.200 (n=18614)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.228 (n=9143)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.197)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.178 (n=4490)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.175 (n=4994)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 18.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.182 (n=4784)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.175 (n=4182)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` > 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.215 (n=2845)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.216 (n=2535)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.213)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.292 (n=956)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.213)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=4921)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.179 (n=4187)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.177 (n=5093)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=3848)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=4198)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.250 (n=3566)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.249)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.356 (n=1445)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=4836)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=4117)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=3596)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.187)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.429 (n=909)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.428 (n=909)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=922)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=962)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `4389.547` → IC=+0.444 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4389.547 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.444 (n=375)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.458 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.440)

- **PATRÓN** `libro_liquidez` > `12430.0394` → IC=+0.447 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12430.0394 (IC base=+0.440)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.431 (n=358)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.424)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.428 (n=357)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.424)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.424)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.430 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.424)

- **PATRÓN** `libro_liquidez` > `4630.8744` → IC=+0.442 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4630.8744 (IC base=+0.424)

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
  - _Potencial_: sin este filtro IC_bueno=-0.243 (n=33)

- **FILTRO** `py_entrada` > `0.765` → IC=-0.294 (n=32)

  - _Acción_: SKIP cuando `py_entrada` > 0.765
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=16)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=32)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=28598)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.244 (n=28957)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.201)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.184 (n=11415)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 8.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.183 (n=9151)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 12.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.194 (n=13032)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.227 (n=12008)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.226)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.288 (n=4114)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.226)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.186 (n=4913)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.199 (n=10140)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=6018)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=4588)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.270 (n=4056)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `libro_liquidez` < `3254.1654` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 3254.1654
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.206 (n=10937)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.259 (n=4234)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=4754)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.200 (n=4752)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.246 (n=4994)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=10271)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=10561)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.57` → IC=+0.137 (n=12521)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.57 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=5013)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.118)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.144 (n=4775)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=6285)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.118)

- **PATRÓN** `lag_apertura_s` < `2.64` → IC=+0.145 (n=4720)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 2.64 (IC base=+0.118)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.190 (n=5258)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.137 (n=5786)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `3.22` → IC=+0.138 (n=6291)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.22 (IC base=+0.116)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.309 (n=1289)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.386 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.293)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.285 (n=865)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.280)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.365 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.280)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.322 (n=627)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.298)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.302 (n=916)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.298)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.392 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.298)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.298 (n=1045)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.298)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` < `16.0` → IC=+0.360 (n=91)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.336)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.382 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.336)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.365 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.336)

- **PATRÓN** `libro_liquidez` > `720.8183` → IC=+0.368 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 720.8183 (IC base=+0.336)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.444 (n=875)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.442 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.443 (n=1011)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.442)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.437 (n=412)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.440 (n=283)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.437 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.442 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.436)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.465 (n=139)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.449)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.452 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.449)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.451 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.449)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.450 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.449)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.414 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.402)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.417 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.402)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.433 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.402)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.715` → IC=-0.351 (n=65)

  - _Acción_: SKIP cuando `py_entrada` > 0.715
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=68)

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
- **FILTRO** `py_entrada` > `0.715` → IC=-0.351 (n=65)

  - _Acción_: SKIP cuando `py_entrada` > 0.715
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=68)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4724` → IC=+0.138 (n=16139)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.4724 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.126 (n=16319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.125 (n=11259)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.375` → IC=+0.164 (n=16139)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.375 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.7705` → IC=+0.278 (n=884)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7705 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.562` → IC=+0.183 (n=8058)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 3.562 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `0.6973` → IC=+0.265 (n=4254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6973 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.3036` → IC=+0.244 (n=1666)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3036 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` > `2.3533` → IC=+0.229 (n=5235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3533 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.132 (n=8135)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `4696.3122` → IC=+0.145 (n=5380)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 4696.3122 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.121 (n=10058)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.006 (IC base=+0.080)

- **PATRÓN** `ibs_20min` < `0.6791` → IC=+0.132 (n=22825)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.6791 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` > `0.5986` → IC=+0.188 (n=1325)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.5986 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` < `0.1596` → IC=+0.188 (n=7841)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.1596 (IC base=+0.080)

- **PATRÓN** `volumen_regimen` < `0.8623` → IC=+0.191 (n=5402)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.8623 (IC base=+0.080)

- **PATRÓN** `volumen_pendiente_norm` > `0.2959` → IC=+0.230 (n=1998)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2959 (IC base=+0.080)

- **PATRÓN** `volumen_spike_ratio` > `1.4561` → IC=+0.204 (n=13763)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4561 (IC base=+0.080)

- **PATRÓN** `ballena_activa_n` < `103.0` → IC=+0.226 (n=13672)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 103.0 (IC base=+0.080)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.362` → IC=+0.210 (n=3461)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.362 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.223 (n=1675)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.210 (n=2322)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.9844` → IC=+0.281 (n=1569)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9844 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.588` → IC=+0.279 (n=1535)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.588 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.2832` → IC=+0.261 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2832 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `1.4361` → IC=+0.210 (n=3314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4361 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.222 (n=3818)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2067.92` → IC=+0.211 (n=1155)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2067.92 (IC base=+0.208)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.221 (n=3114)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 28.0 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.0099` → IC=+0.243 (n=3013)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0099 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.089` → IC=+0.274 (n=1004)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.089 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.252 (n=1107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.242 (n=1394)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.553` → IC=+0.259 (n=3011)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.553 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` < `0.0949` → IC=+0.245 (n=2719)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0949 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.2886` → IC=+0.257 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2886 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.4445` → IC=+0.244 (n=955)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4445 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `1.8606` → IC=+0.242 (n=1908)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8606 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.242 (n=3474)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1511.3592` → IC=+0.247 (n=2690)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1511.3592 (IC base=+0.240)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.231 (n=1920)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.0804` → IC=+0.262 (n=959)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0804 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=3005)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.225 (n=2047)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.9161` → IC=+0.264 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9161 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.1844` → IC=+0.234 (n=1328)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1844 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.037` → IC=+0.261 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.037 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` < `1.2274` → IC=+0.225 (n=2875)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2274 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.7001` → IC=+0.228 (n=2569)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7001 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2786` → IC=+0.271 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2786 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.4263` → IC=+0.252 (n=946)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4263 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.149 (n=3060)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0062 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.077` → IC=+0.152 (n=1020)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.077 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.150 (n=1131)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.7113` → IC=+0.166 (n=3056)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.7113 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` < `0.1366` → IC=+0.144 (n=2931)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1366 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.727` → IC=+0.134 (n=495)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 10.727 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.002` → IC=+0.132 (n=2800)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 4.002 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `1.2025` → IC=+0.134 (n=3056)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.2025 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.148 (n=1116)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `2.1354` → IC=+0.135 (n=2580)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.1354 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.128 (n=3964)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `205.0` → IC=+0.165 (n=1270)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 205.0 (IC base=+0.127)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.216 (n=1216)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=3831)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.265 (n=1413)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.1` → IC=+0.277 (n=795)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.1 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.196 (n=3259)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.3532` → IC=+0.214 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3532 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.7252` → IC=+0.206 (n=1613)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7252 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=4392)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `1941.7448` → IC=+0.201 (n=1654)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1941.7448 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.225 (n=2937)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.2959` → IC=+0.234 (n=2225)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2959 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.245 (n=1255)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.222 (n=1518)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` < `0.0397` → IC=+0.270 (n=1113)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0397 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.06` → IC=+0.263 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.06 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.3492` → IC=+0.260 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3492 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` < `1.7614` → IC=+0.217 (n=1407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7614 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.1534` → IC=+0.228 (n=2132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1534 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.225 (n=1695)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `1925.4429` → IC=+0.223 (n=1513)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1925.4429 (IC base=+0.220)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.223 (n=3151)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.220)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.165 (n=183)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=4405)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.162 (n=628)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0038 (IC base=+0.057)

- **PATRÓN** `ibs_20min` > `0.9435` → IC=+0.233 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9435 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` > `0.137` → IC=+0.336 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.137 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` < `0.3349` → IC=+0.330 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3349 (IC base=+0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.071` → IC=+0.200 (n=1362)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.071 (IC base=+0.057)

- **PATRÓN** `volumen_regimen` < `0.869` → IC=+0.330 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.869 (IC base=+0.057)

- **PATRÓN** `volumen_regimen` > `1.2431` → IC=+0.353 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2431 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` < `0.0775` → IC=+0.332 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0775 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.3033` → IC=+0.335 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3033 (IC base=+0.057)

- **PATRÓN** `volumen_spike_ratio` < `1.5398` → IC=+0.338 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5398 (IC base=+0.057)

- **PATRÓN** `volumen_spike_ratio` > `2.2709` → IC=+0.340 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2709 (IC base=+0.057)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.335 (n=721)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 143.0 (IC base=+0.057)

- **PATRÓN** `ibs_20min` < `0.092` → IC=+0.181 (n=1148)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.092 (IC base=+0.045)

- **PATRÓN** `dist_vwap_pct` > `0.3312` → IC=+0.164 (n=551)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.3312 (IC base=+0.045)

- **PATRÓN** `dist_vwap_pct` < `0.1381` → IC=+0.144 (n=2010)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1381 (IC base=+0.045)

- **PATRÓN** `volumen_regimen` < `0.8353` → IC=+0.158 (n=1431)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8353 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.2825` → IC=+0.205 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2825 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` < `1.7746` → IC=+0.150 (n=1376)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.7746 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` > `2.1494` → IC=+0.157 (n=936)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.1494 (IC base=+0.045)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.184 (n=131)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=685)

- **FILTRO** `ibs_20min` < `0.2692` → IC=-0.165 (n=204)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2692
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=612)

- **FILTRO** `ibs_20min` > `0.2055` → IC=-0.132 (n=4317)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2055
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=2127)

- **FILTRO** `sigma_ewma_delta_pct` > `8.412` → IC=-0.225 (n=695)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.412
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=5749)

- **PATRÓN** `ibs_20min` > `0.7547` → IC=+0.175 (n=278)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.7547 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.9754` → IC=+0.277 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9754 (IC base=+0.021)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.045` → IC=+0.153 (n=191)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 5.045 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` > `1.0359` → IC=+0.288 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0359 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` < `0.1586` → IC=+0.279 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1586 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` < `2.4897` → IC=+0.283 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4897 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` > `1.4523` → IC=+0.263 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4523 (IC base=+0.021)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.269 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.021)

- **PATRÓN** `ibs_20min` < `0.2055` → IC=+0.154 (n=2127)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.2055 (IC base=-0.037)

- **PATRÓN** `dist_vwap_pct` > `0.2105` → IC=+0.280 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2105 (IC base=-0.037)

- **PATRÓN** `dist_vwap_pct` < `0.2963` → IC=+0.279 (n=995)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2963 (IC base=-0.037)

- **PATRÓN** `volumen_regimen` < `0.6941` → IC=+0.309 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6941 (IC base=-0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.0782` → IC=+0.293 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0782 (IC base=-0.037)

- **PATRÓN** `volumen_spike_ratio` < `2.4388` → IC=+0.305 (n=866)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4388 (IC base=-0.037)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7746` → IC=-0.155 (n=3226)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7746
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=1662)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.168 (n=1114)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=3774)

- **FILTRO** `ibs_20min` > `0.7458` → IC=-0.198 (n=1715)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7458
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=5149)

- **PATRÓN** `dist_vwap_pct` > `0.9844` → IC=+0.361 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9844 (IC base=-0.062)

- **PATRÓN** `dist_vwap_pct` < `0.2422` → IC=+0.303 (n=811)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2422 (IC base=-0.062)

- **PATRÓN** `volumen_regimen` > `0.7065` → IC=+0.317 (n=812)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7065 (IC base=-0.062)

- **PATRÓN** `volumen_pendiente_norm` < `0.1041` → IC=+0.302 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1041 (IC base=-0.062)

- **PATRÓN** `volumen_pendiente_norm` > `0.0758` → IC=+0.302 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0758 (IC base=-0.062)

- **PATRÓN** `volumen_spike_ratio` < `1.572` → IC=+0.304 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.572 (IC base=-0.062)

- **PATRÓN** `volumen_spike_ratio` > `1.8714` → IC=+0.306 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8714 (IC base=-0.062)

- **PATRÓN** `dist_vwap_pct` > `0.7832` → IC=+0.279 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7832 (IC base=+0.000)

- **PATRÓN** `volumen_regimen` < `0.722` → IC=+0.272 (n=866)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.722 (IC base=+0.000)

- **PATRÓN** `volumen_regimen` > `1.0651` → IC=+0.285 (n=893)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0651 (IC base=+0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.1693` → IC=+0.286 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1693 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` < `2.1737` → IC=+0.267 (n=1622)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1737 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` > `1.4366` → IC=+0.271 (n=1843)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4366 (IC base=+0.000)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.198 (n=6977)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0104 (IC base=+0.090)

- **PATRÓN** `ibs_20min` > `0.8733` → IC=+0.286 (n=9488)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8733 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` > `0.9254` → IC=+0.302 (n=1480)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9254 (IC base=+0.090)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.528` → IC=+0.167 (n=9370)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.528 (IC base=+0.090)

- **PATRÓN** `volumen_regimen` < `1.1763` → IC=+0.268 (n=7667)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1763 (IC base=+0.090)

- **PATRÓN** `volumen_regimen` > `0.6929` → IC=+0.275 (n=6849)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6929 (IC base=+0.090)

- **PATRÓN** `volumen_pendiente_norm` > `0.2401` → IC=+0.288 (n=2308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2401 (IC base=+0.090)

- **PATRÓN** `volumen_spike_ratio` > `2.6532` → IC=+0.281 (n=4061)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6532 (IC base=+0.090)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.306 (n=11781)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.090)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.157 (n=6747)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0099 (IC base=+0.079)

- **PATRÓN** `ibs_20min` < `0.6449` → IC=+0.151 (n=20193)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.6449 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` < `0.2512` → IC=+0.276 (n=6720)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2512 (IC base=+0.079)

- **PATRÓN** `volumen_regimen` < `0.702` → IC=+0.277 (n=2895)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.702 (IC base=+0.079)

- **PATRÓN** `volumen_regimen` > `1.1928` → IC=+0.273 (n=2193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1928 (IC base=+0.079)

- **PATRÓN** `volumen_pendiente_norm` > `0.2941` → IC=+0.325 (n=1441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2941 (IC base=+0.079)

- **PATRÓN** `volumen_spike_ratio` < `1.5758` → IC=+0.298 (n=4240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5758 (IC base=+0.079)

- **PATRÓN** `volumen_spike_ratio` > `2.2768` → IC=+0.295 (n=4368)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2768 (IC base=+0.079)

- **PATRÓN** `ballena_activa_n` < `74.0` → IC=+0.306 (n=9594)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 74.0 (IC base=+0.079)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.5794` → IC=-0.166 (n=2851)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5794
  - _Potencial_: sin este filtro IC_bueno=+0.207 (n=2851)

- **FILTRO** `ibs_20min` > `0.7217` → IC=-0.228 (n=1242)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7217
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=3730)

- **FILTRO** `sigma_ewma_delta_pct` > `4.193` → IC=-0.228 (n=1075)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.193
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=3897)

- **PATRÓN** `ibs_20min` > `0.9318` → IC=+0.334 (n=1426)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9318 (IC base=+0.021)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.058` → IC=+0.188 (n=1909)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 3.058 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.2287` → IC=+0.324 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2287 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` < `1.4484` → IC=+0.274 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4484 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` > `2.242` → IC=+0.295 (n=838)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.242 (IC base=+0.021)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.312 (n=1240)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.021)

- **PATRÓN** `ibs_20min` < `0.1723` → IC=+0.161 (n=1244)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1723 (IC base=-0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.1514` → IC=+0.405 (n=864)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1514 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.4209` → IC=+0.426 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4209 (IC base=-0.026)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.401 (n=866)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=-0.026)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1694` → IC=+0.222 (n=902)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1694 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` < `1.1961` → IC=+0.206 (n=2032)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1961 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` > `0.6955` → IC=+0.210 (n=1815)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6955 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.251 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` < `1.4174` → IC=+0.232 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4174 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` > `2.4465` → IC=+0.209 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4465 (IC base=+0.014)

- **PATRÓN** `ballena_activa_n` < `267.0` → IC=+0.240 (n=1343)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 267.0 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` < `0.1268` → IC=+0.249 (n=1419)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1268 (IC base=-0.005)

- **PATRÓN** `volumen_regimen` < `1.1652` → IC=+0.239 (n=1392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1652 (IC base=-0.005)

- **PATRÓN** `volumen_regimen` > `0.6228` → IC=+0.243 (n=1392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6228 (IC base=-0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2707` → IC=+0.312 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2707 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.5285` → IC=+0.247 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5285 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.1503` → IC=+0.255 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1503 (IC base=-0.005)

- **PATRÓN** `ballena_activa_n` < `214.0` → IC=+0.256 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 214.0 (IC base=-0.005)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.322 (n=1349)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.280)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.289 (n=2972)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.280)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.322 (n=1612)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.464` → IC=+0.302 (n=1797)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.464 (IC base=+0.280)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.292 (n=2601)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` > `1.6095` → IC=+0.285 (n=2880)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6095 (IC base=+0.280)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.289 (n=3545)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `2043.2212` → IC=+0.295 (n=990)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2043.2212 (IC base=+0.280)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.303 (n=1834)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.280)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.337 (n=1206)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0105 (IC base=+0.302)

- **PATRÓN** `drift_60min` |x|≤ `0.1775` → IC=+0.322 (n=1169)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1775 (IC base=+0.302)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.326 (n=1012)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.302)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.304 (n=1201)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.302)

- **PATRÓN** `ibs_20min` < `0.0106` → IC=+0.302 (n=1169)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0106 (IC base=+0.302)

- **PATRÓN** `ibs_20min` > `0.1366` → IC=+0.312 (n=1771)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1366 (IC base=+0.302)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.325` → IC=+0.313 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.325 (IC base=+0.302)

- **PATRÓN** `volumen_pendiente_norm` < `0.1982` → IC=+0.302 (n=2614)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1982 (IC base=+0.302)

- **PATRÓN** `volumen_pendiente_norm` > `0.3444` → IC=+0.312 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3444 (IC base=+0.302)

- **PATRÓN** `volumen_spike_ratio` > `2.7258` → IC=+0.317 (n=1159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7258 (IC base=+0.302)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.305 (n=1356)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.302)

- **PATRÓN** `libro_liquidez` > `1926.76` → IC=+0.316 (n=1205)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1926.76 (IC base=+0.302)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.308 (n=2216)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.302)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7288` → IC=-0.181 (n=1303)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7288
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=3912)

- **PATRÓN** `ibs_20min` > `0.8581` → IC=+0.164 (n=1270)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.8581 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.1439` → IC=+0.232 (n=952)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1439 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` < `0.3574` → IC=+0.234 (n=1788)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3574 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` < `1.1628` → IC=+0.232 (n=1820)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1628 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` > `0.6712` → IC=+0.230 (n=1626)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6712 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` < `0.1623` → IC=+0.234 (n=1912)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1623 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.1029` → IC=+0.237 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1029 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `2.4598` → IC=+0.236 (n=1762)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4598 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `117.0` → IC=+0.253 (n=1799)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 117.0 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` < `0.1483` → IC=+0.244 (n=1277)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1483 (IC base=+0.004)

- **PATRÓN** `volumen_regimen` < `1.1889` → IC=+0.249 (n=1301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1889 (IC base=+0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2815` → IC=+0.305 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2815 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.7856` → IC=+0.280 (n=831)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7856 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.4276` → IC=+0.263 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4276 (IC base=+0.004)

- **PATRÓN** `ballena_activa_n` < `101.0` → IC=+0.275 (n=1111)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 101.0 (IC base=+0.004)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7436` → IC=-0.242 (n=2171)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7436
  - _Potencial_: sin este filtro IC_bueno=+0.311 (n=2172)

- **FILTRO** `ibs_20min` > `0.6296` → IC=-0.233 (n=1041)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6296
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=3134)

- **FILTRO** `sigma_ewma_delta_pct` > `8.329` → IC=-0.251 (n=479)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.329
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=3696)

- **PATRÓN** `ibs_20min` > `0.7436` → IC=+0.311 (n=2172)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7436 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` > `0.2146` → IC=+0.345 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2146 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.482` → IC=+0.149 (n=1749)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 2.482 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` < `0.8488` → IC=+0.339 (n=1059)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8488 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` > `0.6975` → IC=+0.335 (n=1418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6975 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` < `0.1583` → IC=+0.335 (n=1642)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1583 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.359 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `1.4333` → IC=+0.361 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4333 (IC base=+0.035)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.353 (n=1376)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.035)

- **PATRÓN** `ibs_20min` < `0.6296` → IC=+0.143 (n=3134)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.6296 (IC base=+0.050)

- **PATRÓN** `dist_vwap_pct` < `0.2187` → IC=+0.262 (n=1483)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2187 (IC base=+0.050)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.034` → IC=+0.123 (n=2939)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` < 3.034 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` < `0.6964` → IC=+0.284 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6964 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.0705` → IC=+0.274 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0705 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` < `2.4388` → IC=+0.265 (n=1467)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4388 (IC base=+0.050)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.279 (n=1496)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.050)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.356 (n=1992)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.312)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.314 (n=2254)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.312)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.315 (n=2342)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.312)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.342 (n=2234)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.312)

- **PATRÓN** `dist_vwap_pct` > `0.2017` → IC=+0.337 (n=1228)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2017 (IC base=+0.312)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.996` → IC=+0.331 (n=833)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.996 (IC base=+0.312)

- **PATRÓN** `volumen_regimen` > `0.6307` → IC=+0.321 (n=2230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6307 (IC base=+0.312)

- **PATRÓN** `volumen_pendiente_norm` > `0.2809` → IC=+0.345 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2809 (IC base=+0.312)

- **PATRÓN** `volumen_spike_ratio` > `1.4273` → IC=+0.324 (n=2145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4273 (IC base=+0.312)

- **PATRÓN** `libro_liquidez` > `2961.5054` → IC=+0.315 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2961.5054 (IC base=+0.312)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.342 (n=1965)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.312)

- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.346 (n=1579)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.315)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.323 (n=1194)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.315)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.317 (n=1158)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.315)

- **PATRÓN** `ibs_20min` < `0.381` → IC=+0.334 (n=2370)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.381 (IC base=+0.315)

- **PATRÓN** `dist_vwap_pct` < `0.2353` → IC=+0.320 (n=2289)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2353 (IC base=+0.315)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.624` → IC=+0.330 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.624 (IC base=+0.315)

- **PATRÓN** `volumen_regimen` < `0.719` → IC=+0.321 (n=1042)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.719 (IC base=+0.315)

- **PATRÓN** `volumen_regimen` > `1.2103` → IC=+0.342 (n=790)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2103 (IC base=+0.315)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.366 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.315)

- **PATRÓN** `volumen_spike_ratio` < `1.412` → IC=+0.325 (n=730)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.412 (IC base=+0.315)

- **PATRÓN** `volumen_spike_ratio` > `2.1339` → IC=+0.319 (n=992)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1339 (IC base=+0.315)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.228 (n=5218)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.0873` → IC=+0.196 (n=5217)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.0873 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=16220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `0.541` → IC=+0.233 (n=15651)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.541 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.1616` → IC=+0.207 (n=6053)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1616 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.112` → IC=+0.254 (n=4086)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.112 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `1.1865` → IC=+0.157 (n=10422)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1865 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` > `0.6262` → IC=+0.156 (n=10423)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.6262 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.2943` → IC=+0.207 (n=2273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2943 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `2.6076` → IC=+0.189 (n=5072)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.6076 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.196 (n=14595)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 90.0 (IC base=+0.176)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.190 (n=6720)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0057 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.08` → IC=+0.222 (n=5082)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.08 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.210 (n=7251)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.52` → IC=+0.239 (n=15245)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.52 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.1783` → IC=+0.176 (n=11033)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1783 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.695` → IC=+0.194 (n=2431)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 9.695 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.578` → IC=+0.187 (n=13563)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 2.578 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `1.1816` → IC=+0.164 (n=10861)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1816 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2944` → IC=+0.219 (n=2283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2944 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6379` → IC=+0.189 (n=4817)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6379 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.197 (n=14211)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 94.0 (IC base=+0.182)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1047` → IC=+0.258 (n=1135)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1047 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=2682)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.228 (n=1747)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.8085` → IC=+0.274 (n=2305)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8085 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.033` → IC=+0.335 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.033 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.290 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `1.8326` → IC=+0.221 (n=1638)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8326 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `1.4352` → IC=+0.226 (n=2456)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4352 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=2869)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.259 (n=2072)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0093 (IC base=+0.255)

- **PATRÓN** `drift_60min` |x|≤ `0.0973` → IC=+0.308 (n=914)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0973 (IC base=+0.255)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.262 (n=2146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.255)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.257 (n=1893)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.255)

- **PATRÓN** `ibs_20min` < `0.4232` → IC=+0.272 (n=2072)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4232 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` < `0.1002` → IC=+0.259 (n=1816)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1002 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` > `0.3015` → IC=+0.281 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3015 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` < `1.4445` → IC=+0.279 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4445 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` > `2.7171` → IC=+0.256 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7171 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.258 (n=2393)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `1506.6954` → IC=+0.265 (n=1851)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1506.6954 (IC base=+0.255)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.255 (n=1750)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.255)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.197 (n=801)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.003 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.1586` → IC=+0.163 (n=1593)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1586 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=2499)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.2688` → IC=+0.211 (n=2389)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2688 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.1843` → IC=+0.214 (n=1210)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1843 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.786` → IC=+0.208 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.786 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.6967` → IC=+0.142 (n=1052)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.6967 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` > `1.0626` → IC=+0.138 (n=1083)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 1.0626 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.2815` → IC=+0.180 (n=373)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2815 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `1.5024` → IC=+0.148 (n=1033)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.5024 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `2.4689` → IC=+0.147 (n=782)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.4689 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `405.0` → IC=+0.138 (n=2311)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 405.0 (IC base=+0.134)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.171 (n=2524)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0063 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.2365` → IC=+0.168 (n=2218)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.2365 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.182 (n=1203)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.6112` → IC=+0.205 (n=2521)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6112 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.077` → IC=+0.181 (n=474)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 11.077 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.054` → IC=+0.146 (n=2208)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 4.054 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.2024` → IC=+0.159 (n=2521)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2024 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.0938` → IC=+0.148 (n=2182)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.0938 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.1286` → IC=+0.149 (n=2110)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.1286 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `214.0` → IC=+0.183 (n=1025)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 214.0 (IC base=+0.144)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.236 (n=1201)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.395` → IC=+0.224 (n=2332)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.395 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.234 (n=963)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=1396)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.249` → IC=+0.304 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.249 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` < `0.0991` → IC=+0.211 (n=2295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0991 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.3534` → IC=+0.229 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3534 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.7635` → IC=+0.211 (n=1136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7635 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.7141` → IC=+0.221 (n=1171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7141 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.216 (n=3188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `1931.1232` → IC=+0.221 (n=1201)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1931.1232 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.246 (n=2036)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.4175` → IC=+0.261 (n=2035)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4175 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.283 (n=880)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.0312` → IC=+0.290 (n=1019)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0312 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.203` → IC=+0.282 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.203 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.3585` → IC=+0.288 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3585 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.766` → IC=+0.237 (n=979)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.766 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `2.1786` → IC=+0.248 (n=1483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1786 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.240 (n=1195)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1917.7236` → IC=+0.248 (n=1048)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1917.7236 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.243 (n=1523)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.239)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.204 (n=855)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0784` → IC=+0.193 (n=855)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.0784 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=2652)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.2662` → IC=+0.199 (n=2562)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2662 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.1386` → IC=+0.189 (n=1509)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1386 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.402` → IC=+0.198 (n=439)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 11.402 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.8476` → IC=+0.144 (n=1709)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.8476 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `1.1857` → IC=+0.140 (n=854)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 1.1857 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2887` → IC=+0.180 (n=382)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2887 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.8257` → IC=+0.138 (n=1673)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.8257 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.5272` → IC=+0.158 (n=837)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.5272 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `6877.2097` → IC=+0.201 (n=1162)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6877.2097 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `131.0` → IC=+0.144 (n=2506)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 131.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.165 (n=2388)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0066 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.3945` → IC=+0.143 (n=2713)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3945 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.163 (n=1293)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.6727` → IC=+0.185 (n=2713)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6727 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` < `0.1585` → IC=+0.155 (n=2729)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1585 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.343` → IC=+0.148 (n=657)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 9.343 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.8525` → IC=+0.154 (n=1810)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8525 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2961` → IC=+0.176 (n=409)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2961 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.8074` → IC=+0.130 (n=1709)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.8074 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `1.4232` → IC=+0.127 (n=2563)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.4232 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `6194.147` → IC=+0.185 (n=1230)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 6194.147 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `109.0` → IC=+0.133 (n=2232)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 109.0 (IC base=+0.127)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.171 (n=1300)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0111 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=2926)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.4737` → IC=+0.210 (n=2862)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4737 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.1965` → IC=+0.191 (n=1558)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1965 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.173` → IC=+0.293 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.173 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `1.1752` → IC=+0.134 (n=2860)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.1752 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.7045` → IC=+0.124 (n=2555)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.7045 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` < `0.1632` → IC=+0.130 (n=2916)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1632 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.5419` → IC=+0.138 (n=1222)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.5419 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.125 (n=2984)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2652.8351` → IC=+0.201 (n=1297)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2652.8351 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.144 (n=1225)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 21.0 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0117` → IC=+0.142 (n=2970)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0117 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1104` → IC=+0.164 (n=991)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1104 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.135 (n=3037)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.6429` → IC=+0.219 (n=2974)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6429 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.2083` → IC=+0.146 (n=2903)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.2083 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.318` → IC=+0.138 (n=2621)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 2.318 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.1765` → IC=+0.129 (n=2970)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1765 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` < `0.1625` → IC=+0.122 (n=2906)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1625 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.135 (n=409)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4336` → IC=+0.129 (n=932)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.4336 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` > `2.4408` → IC=+0.124 (n=932)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 2.4408 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2530.5689` → IC=+0.184 (n=1347)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2530.5689 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.124 (n=2781)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 46.0 (IC base=+0.118)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.249 (n=2334)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0131 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.1657` → IC=+0.241 (n=1150)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1657 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.228 (n=2711)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.230 (n=2352)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.258 (n=2612)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` > `0.1784` → IC=+0.234 (n=1628)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1784 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` < `0.8037` → IC=+0.225 (n=2693)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8037 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.577` → IC=+0.253 (n=1175)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.577 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.6249` → IC=+0.233 (n=2614)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6249 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2338` → IC=+0.266 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2338 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `2.4718` → IC=+0.228 (n=2546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4718 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `1.8139` → IC=+0.234 (n=1697)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8139 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `2101.6605` → IC=+0.228 (n=2612)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2101.6605 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.240 (n=1171)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0227` → IC=+0.250 (n=1206)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0227 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.0846` → IC=+0.266 (n=887)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0846 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.255 (n=1298)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.244 (n=1190)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.44` → IC=+0.264 (n=2670)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.44 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `0.2992` → IC=+0.242 (n=673)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2992 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.031` → IC=+0.270 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.031 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` < `0.8653` → IC=+0.242 (n=1773)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8653 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` > `0.641` → IC=+0.241 (n=2659)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.641 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.289 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `2.5237` → IC=+0.234 (n=2497)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5237 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `1.4358` → IC=+0.240 (n=2496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4358 (IC base=+0.238)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.207 (n=1324)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.131` → IC=+0.182 (n=1743)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.131 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.185 (n=3539)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `0.327` → IC=+0.201 (n=3960)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.327 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.7901` → IC=+0.197 (n=598)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.7901 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.692` → IC=+0.206 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.692 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `0.8638` → IC=+0.183 (n=2394)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.8638 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` > `1.1979` → IC=+0.173 (n=1197)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 1.1979 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.0741` → IC=+0.175 (n=1602)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.0741 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `1.4274` → IC=+0.174 (n=1287)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.4274 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `2.482` → IC=+0.168 (n=1286)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.482 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.169 (n=4441)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.02 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `2614.8932` → IC=+0.177 (n=3538)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2614.8932 (IC base=+0.166)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.188 (n=1884)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.2 (IC base=+0.086)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.128 (n=1810)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 26.0 (IC base=+0.086)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.196 (n=1076)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.006 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.1007` → IC=+0.231 (n=473)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1007 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.212 (n=975)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.2201` → IC=+0.214 (n=1075)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2201 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.2992` → IC=+0.212 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2992 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.957` → IC=+0.200 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.957 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.414` → IC=+0.180 (n=1131)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 6.414 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `0.8809` → IC=+0.195 (n=717)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8809 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` < `0.1502` → IC=+0.181 (n=1130)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` < 0.1502 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.0708` → IC=+0.190 (n=430)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.0708 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `2.1853` → IC=+0.194 (n=928)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.1853 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `15950.0664` → IC=+0.196 (n=488)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 15950.0664 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.169 (n=442)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.003 (IC base=+0.093)

- **PATRÓN** `ibs_20min` < `0.1952` → IC=+0.193 (n=578)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.1952 (IC base=+0.093)

- **PATRÓN** `volumen_pendiente_norm` > `0.1608` → IC=+0.139 (n=341)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.1608 (IC base=+0.093)

- **PATRÓN** `ballena_activa_n` < `161.0` → IC=+0.173 (n=564)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 161.0 (IC base=+0.093)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.243 (n=538)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.2082` → IC=+0.189 (n=815)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.2082 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=1277)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.6333` → IC=+0.251 (n=814)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6333 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.7812` → IC=+0.194 (n=194)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.7812 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` < `0.2037` → IC=+0.183 (n=1101)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.2037 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.882` → IC=+0.216 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.882 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.8342` → IC=+0.198 (n=815)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.8342 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.1597` → IC=+0.206 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1597 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `1.4275` → IC=+0.186 (n=402)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.4275 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `1.7873` → IC=+0.196 (n=803)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.7873 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.1051` → IC=+0.177 (n=401)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.1051 (IC base=+0.071)

- **PATRÓN** `libro_liquidez` > `8064.6274` → IC=+0.143 (n=545)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 8064.6274 (IC base=+0.071)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.156 (n=434)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.007 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.177 (n=701)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 11.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.4758` → IC=+0.195 (n=983)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.4758 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.968` → IC=+0.218 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.968 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.01` → IC=+0.238 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.01 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `1.0509` → IC=+0.146 (n=865)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.0509 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` > `0.7047` → IC=+0.142 (n=878)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.7047 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.2267` → IC=+0.165 (n=183)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.2267 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `1.4241` → IC=+0.152 (n=317)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4241 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.8014` → IC=+0.133 (n=633)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.8014 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.140 (n=1034)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.02 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `2730.6754` → IC=+0.174 (n=446)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2730.6754 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.3793` → IC=+0.177 (n=711)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.3793 (IC base=+0.053)

- **PATRÓN** `libro_liquidez` > `2850.5747` → IC=+0.155 (n=355)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2850.5747 (IC base=+0.053)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0164` → IC=+0.224 (n=208)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0164 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.2637` → IC=+0.174 (n=210)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2637 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.233 (n=148)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` > `0.7393` → IC=+0.205 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7393 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.2993` → IC=+0.197 (n=153)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.2993 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` < `0.5121` → IC=+0.175 (n=300)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.5121 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.349` → IC=+0.207 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.349 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` > `1.1751` → IC=+0.226 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1751 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` < `0.1109` → IC=+0.185 (n=274)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.1109 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` > `0.1871` → IC=+0.196 (n=77)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1871 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` < `1.8264` → IC=+0.193 (n=190)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.8264 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `2.4339` → IC=+0.201 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4339 (IC base=+0.175)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.189 (n=355)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.03 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `2497.2192` → IC=+0.200 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2497.2192 (IC base=+0.175)

- **PATRÓN** `sigma_h` > `0.0237` → IC=+0.209 (n=156)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0237 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.2745` → IC=+0.152 (n=228)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.2745 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.204 (n=157)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.51` → IC=+0.155 (n=302)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.51 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `1.1297` → IC=+0.238 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1297 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.1803` → IC=+0.141 (n=282)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.1803 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.17` → IC=+0.181 (n=92)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 5.17 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.872` → IC=+0.183 (n=228)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.872 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` < `0.1126` → IC=+0.145 (n=311)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.1126 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.182 (n=64)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.5288` → IC=+0.203 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5288 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `2.6761` → IC=+0.158 (n=109)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.6761 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `2005.7135` → IC=+0.142 (n=342)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2005.7135 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.160 (n=327)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 20.0 (IC base=+0.141)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.232 (n=6811)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=21298)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.434` → IC=+0.229 (n=20429)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.434 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.8705` → IC=+0.210 (n=2425)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8705 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.037` → IC=+0.254 (n=5012)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.037 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.2185` → IC=+0.160 (n=13742)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2185 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2415` → IC=+0.205 (n=3691)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2415 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6204` → IC=+0.192 (n=6642)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6204 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.202 (n=19063)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 106.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.198 (n=8241)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0059 (IC base=+0.192)

- **PATRÓN** `sigma_h` > `0.012` → IC=+0.198 (n=6247)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.012 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.4811` → IC=+0.196 (n=18716)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.4811 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=6936)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` < `0.5909` → IC=+0.242 (n=18721)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5909 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` < `0.1771` → IC=+0.174 (n=11729)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.1771 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.553` → IC=+0.202 (n=2546)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.553 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.44` → IC=+0.196 (n=18216)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` < 3.44 (IC base=+0.192)

- **PATRÓN** `volumen_regimen` < `1.0564` → IC=+0.167 (n=11077)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.0564 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` > `0.2917` → IC=+0.252 (n=2556)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2917 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `2.6295` → IC=+0.203 (n=5952)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6295 (IC base=+0.192)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.208 (n=17588)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.192)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.249 (n=1589)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.234 (n=2215)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` > `0.8602` → IC=+0.302 (n=2191)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8602 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.67` → IC=+0.335 (n=1066)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.67 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.2331` → IC=+0.292 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2331 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.4461` → IC=+0.231 (n=1057)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4461 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.2896` → IC=+0.237 (n=1438)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2896 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.249 (n=3612)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `2066.52` → IC=+0.235 (n=1096)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2066.52 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.256 (n=1120)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.233)

- **PATRÓN** `sigma_h` < `0.0098` → IC=+0.268 (n=2899)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0098 (IC base=+0.266)

- **PATRÓN** `drift_60min` |x|≤ `0.1223` → IC=+0.290 (n=1275)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1223 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.271 (n=2667)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.266)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.267 (n=2636)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` < `0.5344` → IC=+0.286 (n=2896)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5344 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` < `0.0964` → IC=+0.268 (n=2628)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0964 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` > `0.2886` → IC=+0.292 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2886 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` < `1.5615` → IC=+0.267 (n=1218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5615 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` > `2.6564` → IC=+0.273 (n=923)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6564 (IC base=+0.266)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.270 (n=2003)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.266)

- **PATRÓN** `libro_liquidez` > `1777.62` → IC=+0.274 (n=1931)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1777.62 (IC base=+0.266)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.273 (n=1257)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.266)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.182 (n=1118)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.003 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.1059` → IC=+0.148 (n=1471)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.1059 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=3483)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.2061` → IC=+0.189 (n=3343)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.2061 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.3179` → IC=+0.201 (n=1104)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3179 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.241` → IC=+0.159 (n=537)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 11.241 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6368` → IC=+0.154 (n=1115)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6368 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.2381` → IC=+0.138 (n=1115)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 1.2381 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2719` → IC=+0.180 (n=483)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2719 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.1558` → IC=+0.142 (n=2886)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.1558 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.5175` → IC=+0.139 (n=2930)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.5175 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `227.0` → IC=+0.158 (n=1084)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 227.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.161 (n=2854)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0063 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0786` → IC=+0.175 (n=951)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0786 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=1037)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.6835` → IC=+0.184 (n=2854)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6835 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.043` → IC=+0.143 (n=1361)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 3.043 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.1933` → IC=+0.147 (n=2853)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.1933 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2185` → IC=+0.190 (n=531)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2185 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.4115` → IC=+0.142 (n=916)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4115 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.7707` → IC=+0.141 (n=1830)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.7707 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=3703)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `229.0` → IC=+0.153 (n=887)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 229.0 (IC base=+0.136)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.253 (n=1134)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=3560)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=3050)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=1270)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.155` → IC=+0.320 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.155 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` < `0.1319` → IC=+0.226 (n=3210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1319 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.7332` → IC=+0.237 (n=1505)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7332 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.231 (n=4084)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `1373.0584` → IC=+0.229 (n=3400)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1373.0584 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.248 (n=2847)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.1791` → IC=+0.264 (n=1423)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1791 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.266 (n=1217)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.243 (n=1476)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.243)

- **PATRÓN** `ibs_20min` < `0.0551` → IC=+0.304 (n=1079)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0551 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.311` → IC=+0.301 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.311 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` > `0.3487` → IC=+0.305 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3487 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` > `2.1662` → IC=+0.257 (n=2069)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1662 (IC base=+0.243)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.249 (n=1657)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.243)

- **PATRÓN** `libro_liquidez` > `1919.6972` → IC=+0.253 (n=1466)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1919.6972 (IC base=+0.243)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.250 (n=2693)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.243)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.193 (n=1177)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0036 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.4311` → IC=+0.148 (n=3526)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.4311 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.150 (n=3663)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.8948` → IC=+0.277 (n=1175)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8948 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.1952` → IC=+0.167 (n=1622)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1952 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.995` → IC=+0.158 (n=1576)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 2.995 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.8612` → IC=+0.155 (n=2351)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8612 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2331` → IC=+0.185 (n=624)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2331 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.5199` → IC=+0.155 (n=1517)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.5199 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `5407.3472` → IC=+0.228 (n=1598)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5407.3472 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.151 (n=1527)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 69.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.159 (n=2965)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0077 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.4386` → IC=+0.149 (n=2965)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4386 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=1085)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.7153` → IC=+0.193 (n=2965)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.7153 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.1508` → IC=+0.152 (n=2755)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1508 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.93` → IC=+0.161 (n=443)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 10.93 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.103` → IC=+0.140 (n=2583)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 3.103 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.6142` → IC=+0.158 (n=989)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.6142 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.217 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.215` → IC=+0.143 (n=2517)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.215 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.5362` → IC=+0.148 (n=2555)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.5362 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `6297.4839` → IC=+0.212 (n=988)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6297.4839 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.150 (n=1949)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 94.0 (IC base=+0.139)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.150 (n=1620)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0111 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.151 (n=2526)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 11.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.4324` → IC=+0.193 (n=3570)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.4324 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `1.0123` → IC=+0.207 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0123 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.37` → IC=+0.265 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.37 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `0.8787` → IC=+0.134 (n=2380)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8787 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.1012` → IC=+0.123 (n=3385)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1012 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `2.4864` → IC=+0.122 (n=3487)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.4864 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.121 (n=3725)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2708.4534` → IC=+0.241 (n=1190)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2708.4534 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.129 (n=1189)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 21.0 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.154 (n=2972)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0107 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.1373` → IC=+0.153 (n=1126)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1373 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.159 (n=1583)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 15.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.213 (n=3397)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6667 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.2165` → IC=+0.144 (n=3045)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.2165 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.097` → IC=+0.149 (n=3255)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 3.097 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `0.6396` → IC=+0.153 (n=1125)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6396 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2252` → IC=+0.173 (n=588)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2252 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.4337` → IC=+0.159 (n=1064)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4337 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2597.7875` → IC=+0.206 (n=1125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2597.7875 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.138 (n=3209)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 51.0 (IC base=+0.125)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0138` → IC=+0.258 (n=2954)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0138 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.241 (n=3451)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.241 (n=2967)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` > `0.615` → IC=+0.272 (n=2952)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.615 (IC base=+0.236)

- **PATRÓN** `dist_vwap_pct` > `0.1891` → IC=+0.253 (n=1727)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1891 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.245` → IC=+0.284 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.245 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` < `1.2214` → IC=+0.239 (n=3304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2214 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` > `0.6442` → IC=+0.240 (n=3304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6442 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2382` → IC=+0.260 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2382 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.5063` → IC=+0.255 (n=1076)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5063 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `2953.9004` → IC=+0.245 (n=1102)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2953.9004 (IC base=+0.236)

- **PATRÓN** `sigma_h` > `0.0258` → IC=+0.263 (n=1133)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0258 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.252 (n=1662)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.5222` → IC=+0.273 (n=3397)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5222 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.167` → IC=+0.279 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.167 (IC base=+0.240)

- **PATRÓN** `volumen_regimen` > `1.2176` → IC=+0.260 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2176 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.2857` → IC=+0.303 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2857 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `1.4324` → IC=+0.241 (n=3189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4324 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.239 (n=3140)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.240)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=5727)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.244 (n=1961)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.5006` → IC=+0.225 (n=5866)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5006 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=2121)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` > `0.9331` → IC=+0.254 (n=1956)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9331 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` < `0.4266` → IC=+0.221 (n=4296)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4266 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.574` → IC=+0.224 (n=1920)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.574 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` < `0.7088` → IC=+0.229 (n=1910)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7088 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` > `0.8843` → IC=+0.219 (n=2893)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8843 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` < `0.1054` → IC=+0.218 (n=5467)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1054 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.1653` → IC=+0.222 (n=1661)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1653 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `1.4515` → IC=+0.226 (n=1925)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4515 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.224 (n=4594)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `3752.2865` → IC=+0.226 (n=3911)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3752.2865 (IC base=+0.217)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.237 (n=1437)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.4907` → IC=+0.212 (n=4307)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4907 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=1449)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.213 (n=1902)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.7292` → IC=+0.206 (n=4307)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7292 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.6563` → IC=+0.209 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6563 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.2381` → IC=+0.195 (n=4007)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.2381 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.786` → IC=+0.211 (n=3864)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.786 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `1.0954` → IC=+0.205 (n=3612)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0954 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.200 (n=3967)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2222` → IC=+0.201 (n=863)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2222 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `1.5316` → IC=+0.202 (n=1868)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5316 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.1857` → IC=+0.207 (n=1925)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1857 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=5727)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.215 (n=2836)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 65.0 (IC base=+0.199)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.276 (n=801)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.266)

- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.266 (n=302)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0066 (IC base=+0.266)

- **PATRÓN** `drift_60min` |x|≤ `0.1117` → IC=+0.293 (n=400)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1117 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.277 (n=907)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` < `0.462` → IC=+0.282 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.462 (IC base=+0.266)

- **PATRÓN** `dist_vwap_pct` < `0.3193` → IC=+0.281 (n=932)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3193 (IC base=+0.266)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.118` → IC=+0.290 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.118 (IC base=+0.266)

- **PATRÓN** `volumen_regimen` < `1.2269` → IC=+0.269 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2269 (IC base=+0.266)

- **PATRÓN** `volumen_regimen` > `0.8749` → IC=+0.287 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8749 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` > `0.2875` → IC=+0.346 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2875 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` < `2.4928` → IC=+0.271 (n=902)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4928 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` > `2.1972` → IC=+0.269 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1972 (IC base=+0.266)

- **PATRÓN** `libro_liquidez` > `12892.0448` → IC=+0.277 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12892.0448 (IC base=+0.266)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.262 (n=502)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.3831` → IC=+0.189 (n=1506)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3831 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=551)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.183 (n=559)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 5.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` < `0.1373` → IC=+0.195 (n=663)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.1373 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.6858` → IC=+0.202 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6858 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.315` → IC=+0.197 (n=1475)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 6.315 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` < `1.0935` → IC=+0.188 (n=1326)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 1.0935 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` > `0.1519` → IC=+0.195 (n=457)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1519 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` < `2.496` → IC=+0.182 (n=1498)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.496 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `1.8038` → IC=+0.179 (n=998)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.8038 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `14611.4186` → IC=+0.179 (n=683)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 14611.4186 (IC base=+0.175)

- **PATRÓN** `ballena_activa_n` < `686.0` → IC=+0.187 (n=1461)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 686.0 (IC base=+0.175)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.215 (n=585)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.5864` → IC=+0.203 (n=878)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5864 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.233 (n=339)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` < `0.712` → IC=+0.199 (n=586)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.712 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.239 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.494` → IC=+0.244 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.494 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.2073` → IC=+0.232 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2073 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `1.8074` → IC=+0.203 (n=782)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8074 (IC base=+0.195)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.202 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0116` → IC=+0.242 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0116 (IC base=+0.228)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.286 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.009 (IC base=+0.228)

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

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.219 (n=1618)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.4532` → IC=+0.214 (n=1617)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4532 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.224 (n=567)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` < `0.4996` → IC=+0.218 (n=1078)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4996 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `0.857` → IC=+0.206 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.857 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` < `0.3955` → IC=+0.217 (n=1620)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3955 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.504` → IC=+0.211 (n=1644)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.504 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `0.7064` → IC=+0.214 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7064 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `1.2263` → IC=+0.206 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2263 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` < `0.103` → IC=+0.211 (n=1485)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.103 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `2.4455` → IC=+0.214 (n=1582)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4455 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=1679)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.242 (n=448)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.4841` → IC=+0.221 (n=1336)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4841 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.211 (n=506)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.215 (n=902)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.7503` → IC=+0.201 (n=1336)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7503 (IC base=+0.199)

- **PATRÓN** `ibs_20min` > `0.0937` → IC=+0.205 (n=1335)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0937 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.6221` → IC=+0.211 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6221 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.2204` → IC=+0.199 (n=1311)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2204 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.351` → IC=+0.204 (n=1217)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.351 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `0.6394` → IC=+0.228 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6394 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.074` → IC=+0.226 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.074 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `2.1913` → IC=+0.205 (n=1152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1913 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `1.7831` → IC=+0.201 (n=873)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7831 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `6551.6127` → IC=+0.205 (n=1193)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6551.6127 (IC base=+0.199)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0097` → IC=+0.222 (n=620)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0097 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.232 (n=643)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.274 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` > `0.7494` → IC=+0.240 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7494 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.218` → IC=+0.223 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.218 (IC base=+0.195)

- **PATRÓN** `volumen_regimen` < `0.6428` → IC=+0.244 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6428 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` < `0.1062` → IC=+0.204 (n=837)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1062 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.0801` → IC=+0.201 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0801 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` < `2.1486` → IC=+0.200 (n=795)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1486 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `1.4746` → IC=+0.201 (n=903)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4746 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.203 (n=1103)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `4317.1276` → IC=+0.237 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4317.1276 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.013` → IC=+0.223 (n=685)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.013 (IC base=+0.224)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.239 (n=458)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.5971` → IC=+0.242 (n=685)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5971 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.223 (n=638)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.253 (n=476)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` < `0.7308` → IC=+0.251 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7308 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.5335` → IC=+0.226 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5335 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` < `0.3164` → IC=+0.230 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3164 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.797` → IC=+0.237 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.797 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` < `1.0973` → IC=+0.227 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0973 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `1.2815` → IC=+0.232 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2815 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` < `0.0825` → IC=+0.240 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0825 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.5701` → IC=+0.264 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5701 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `2993.9452` → IC=+0.244 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2993.9452 (IC base=+0.224)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.260 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=+0.224)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.150 (n=683)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0037 (IC base=+0.053)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.190 (n=1304)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.75 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` > `0.1474` → IC=+0.141 (n=968)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1474 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.565` → IC=+0.146 (n=428)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 10.565 (IC base=+0.053)

- **PATRÓN** `ibs_20min` < `0.049` → IC=+0.263 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.049 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.1445` → IC=+0.129 (n=359)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.1445 (IC base=+0.044)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.3811` → IC=-0.152 (n=208)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3811
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=625)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.180 (n=289)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0031 (IC base=+0.072)

- **PATRÓN** `ibs_20min` > `0.3811` → IC=+0.147 (n=625)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.3811 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` > `0.1195` → IC=+0.169 (n=300)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1195 (IC base=+0.072)

- **PATRÓN** `ibs_20min` < `0.0653` → IC=+0.284 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0653 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.2132` → IC=+0.160 (n=104)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2132 (IC base=+0.051)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.5189` → IC=-0.120 (n=277)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5189
  - _Potencial_: sin este filtro IC_bueno=+0.172 (n=565)

- **FILTRO** `ibs_20min` > `0.7006` → IC=-0.176 (n=137)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7006
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=415)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.155 (n=221)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0034 (IC base=+0.072)

- **PATRÓN** `ibs_20min` > `0.7783` → IC=+0.223 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7783 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` > `0.1265` → IC=+0.177 (n=311)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1265 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.646` → IC=+0.198 (n=137)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 11.646 (IC base=+0.072)

- **PATRÓN** `ibs_20min` < `0.0296` → IC=+0.259 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0296 (IC base=+0.016)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.482` → IC=+0.214 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.482 (IC base=+0.016)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.981` → IC=+0.203 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.981 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` > `0.7109` → IC=+0.139 (n=156)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.7109 (IC base=+0.020)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.239` → IC=+0.128 (n=194)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 7.239 (IC base=+0.020)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.146 (n=329)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0111 (IC base=+0.066)

- **PATRÓN** `ibs_20min` < `0.4634` → IC=+0.171 (n=344)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.4634 (IC base=+0.066)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.903` → IC=+0.300 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.903 (IC base=+0.066)

- **PATRÓN** `volumen_regimen` > `1.1045` → IC=+0.167 (n=115)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.1045 (IC base=+0.066)

- **PATRÓN** `volumen_pendiente_norm` > `0.1517` → IC=+0.160 (n=104)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.1517 (IC base=+0.066)

- **PATRÓN** `volumen_spike_ratio` > `1.4436` → IC=+0.121 (n=317)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_spike_ratio` > 1.4436 (IC base=+0.066)

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

- **FILTRO** `ibs_20min` > `0.8039` → IC=-0.327 (n=79)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8039
  - _Potencial_: sin este filtro IC_bueno=-0.272 (n=239)

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

- **FILTRO** `hora_utc` < `13.0` → IC=-0.297 (n=72)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=73)

- **FILTRO** `volumen_regimen` > `0.805` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.230 (n=109)

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

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.400 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=108)

- **FILTRO** `volumen_regimen` < `0.8232` → IC=-0.314 (n=41)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8232
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=85)

- **FILTRO** `sigma_h` < `0.0107` → IC=-0.325 (n=38)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0107
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=36)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.426 (n=25)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=26)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.254` → IC=-0.152 (n=248)

  - _Acción_: SKIP cuando `ibs_20min` > 0.254
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=747)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.213 (n=214)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.189 (n=323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 15.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `0.6774` → IC=+0.176 (n=631)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.6774 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.5399` → IC=+0.252 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5399 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.618` → IC=+0.140 (n=345)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 3.618 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.686` → IC=+0.138 (n=576)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 5.686 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.6249` → IC=+0.176 (n=211)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6249 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` < `0.2694` → IC=+0.158 (n=618)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` < 0.2694 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.4027` → IC=+0.157 (n=526)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.4027 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.53` → IC=+0.157 (n=170)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 10.53 (IC base=+0.034)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.7091` → IC=-0.156 (n=62)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7091
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=188)

- **PATRÓN** `dist_vwap_pct` > `0.5453` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5453 (IC base=+0.024)

- **PATRÓN** `ibs_20min` < `0.2252` → IC=+0.165 (n=350)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.2252 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.348` → IC=+0.130 (n=79)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 11.348 (IC base=+0.094)

- **PATRÓN** `volumen_pendiente_norm` > `0.2254` → IC=+0.130 (n=71)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.2254 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` > `1.7675` → IC=+0.131 (n=212)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.7675 (IC base=+0.094)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1257` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1257
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=202)

- **FILTRO** `ibs_20min` > `0.1468` → IC=-0.123 (n=120)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1468
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=233)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.150 (n=138)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.004 (IC base=+0.120)

- **PATRÓN** `sigma_h` > `0.0031` → IC=+0.129 (n=184)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` > 0.0031 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1051` → IC=+0.124 (n=91)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.1051 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.181 (n=70)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 18.0 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.139 (n=70)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `0.8015` → IC=+0.156 (n=184)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.8015 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.0967` → IC=+0.142 (n=171)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.0967 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.217` → IC=+0.154 (n=215)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 9.217 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.6242` → IC=+0.176 (n=69)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6242 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1257` → IC=+0.167 (n=202)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.1257 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `2.1273` → IC=+0.160 (n=157)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1273 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=175)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `1625.9386` → IC=+0.173 (n=206)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 1625.9386 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.619` → IC=+0.197 (n=64)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.619 (IC base=+0.004)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2` → IC=-0.233 (n=58)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=118)

- **FILTRO** `dist_vwap_pct` > `0.1813` → IC=-0.167 (n=37)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1813
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=139)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.291 (n=170)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` > `0.6053` → IC=+0.271 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6053 (IC base=+0.234)

- **PATRÓN** `dist_vwap_pct` > `0.6827` → IC=+0.389 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6827 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.903` → IC=+0.342 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.903 (IC base=+0.234)

- **PATRÓN** `volumen_regimen` < `0.5849` → IC=+0.293 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5849 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.302 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.48` → IC=+0.319 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.48 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.3425` → IC=+0.278 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3425 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.977` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.977 (IC base=-0.067)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.308 (n=92)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3447` → IC=+0.317 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3447 (IC base=+0.306)

- **PATRÓN** `elapsed_s` > `187.1` → IC=+0.359 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 187.1 (IC base=+0.306)

- **PATRÓN** `drift_15min` |x|≤ `2.6528` → IC=+0.345 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.6528 (IC base=+0.306)

- **PATRÓN** `drift_60min` |x|≤ `0.9568` → IC=+0.373 (n=69)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9568 (IC base=+0.306)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.382 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.306)

- **PATRÓN** `ballena_activa_n` < `1067.0` → IC=+0.380 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1067.0 (IC base=+0.306)

- **PATRÓN** `drift_ventana_pct` |x|> `0.4341` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4341 (IC base=+0.239)

- **PATRÓN** `elapsed_s` > `227.0` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 227.0 (IC base=+0.239)

- **PATRÓN** `elapsed_s` < `203.6` → IC=+0.254 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 203.6 (IC base=+0.239)

- **PATRÓN** `drift_15min` |x|≤ `2.3044` → IC=+0.297 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3044 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.6365` → IC=+0.272 (n=55)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6365 (IC base=+0.239)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.308 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `1770.0` → IC=+0.286 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1770.0 (IC base=+0.239)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.308 (n=92)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3447` → IC=+0.317 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3447 (IC base=+0.306)

- **PATRÓN** `elapsed_s` > `187.1` → IC=+0.359 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 187.1 (IC base=+0.306)

- **PATRÓN** `drift_15min` |x|≤ `2.6528` → IC=+0.345 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.6528 (IC base=+0.306)

- **PATRÓN** `drift_60min` |x|≤ `0.9568` → IC=+0.373 (n=69)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9568 (IC base=+0.306)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.382 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.306)

- **PATRÓN** `ballena_activa_n` < `1067.0` → IC=+0.380 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1067.0 (IC base=+0.306)

- **PATRÓN** `drift_ventana_pct` |x|> `0.4341` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4341 (IC base=+0.239)

- **PATRÓN** `elapsed_s` > `227.0` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 227.0 (IC base=+0.239)

- **PATRÓN** `elapsed_s` < `203.6` → IC=+0.254 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 203.6 (IC base=+0.239)

- **PATRÓN** `drift_15min` |x|≤ `2.3044` → IC=+0.297 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3044 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.6365` → IC=+0.272 (n=55)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6365 (IC base=+0.239)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.308 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `1770.0` → IC=+0.286 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1770.0 (IC base=+0.239)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=237)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=237)

- **FILTRO** `libro_liquidez` < `2998.5952` → IC=-0.177 (n=63)

  - _Acción_: SKIP cuando `libro_liquidez` < 2998.5952
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=190)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=569)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `4139.65` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `liq_usd_total` < 4139.65
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=27)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=30)

- **PATRÓN** `liq_n` > `2.0` → IC=+0.133 (n=107)

  - _Acción_: Kelly boost +0.67€ cuando `liq_n` > 2.0 (IC base=+0.063)

- **PATRÓN** `liq_usd_total` > `5433.99` → IC=+0.136 (n=86)

  - _Acción_: Kelly boost +0.68€ cuando `liq_usd_total` > 5433.99 (IC base=+0.063)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.167 (n=52)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 6.0 (IC base=+0.063)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=3873)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=117)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=117)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.128 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=136)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.124 (n=269)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.495 (IC base=+0.023)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1583)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=1537)

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
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=943)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=943)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.128 (n=294)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=729)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1117)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1117)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=254)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=254)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.141 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=320)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=367)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=289)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=385)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=385)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=230)

- **FILTRO** `libro_liquidez` < `655.65` → IC=-0.138 (n=136)

  - _Acción_: SKIP cuando `libro_liquidez` < 655.65
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=279)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=319)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.145 (n=29)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=68)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.186 (n=68)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=82)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.250 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=51)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.47` → IC=+0.157 (n=211)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` < 0.47 (IC base=-0.006)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.130 (n=244)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=508)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.133 (n=300)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=316)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.167 (n=127)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=559)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.124 (n=461)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=244)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.138 (n=103)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=319)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.126 (n=129)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=293)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.152 (n=268)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=564)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.173 (n=7161)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=23053)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.174 (n=7663)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=23467)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.185 (n=1384)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=4179)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.148 (n=1846)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=3684)

- **PATRÓN** `libro_liquidez` > `1870.3252` → IC=+0.140 (n=1391)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 1870.3252 (IC base=+0.042)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.125 (n=2842)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.505 (IC base=+0.013)

- **PATRÓN** `libro_liquidez` > `1136.4628` → IC=+0.152 (n=1881)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1136.4628 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.182 (n=1086)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=3311)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.205 (n=1369)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=4287)

- **PATRÓN** `ibs_20min` > `0.9643` → IC=+0.130 (n=1897)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.9643 (IC base=+0.034)

- **PATRÓN** `libro_liquidez` > `1750.3436` → IC=+0.121 (n=1895)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1750.3436 (IC base=+0.034)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.155 (n=1389)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=4214)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2423)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=2347)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=2923)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=3875)

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
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=349)

- **FILTRO** `drift_20min_pct` |x|> `0.1569` → IC=-0.148 (n=157)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1569
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=305)

- **FILTRO** `libro_liquidez` < `3195.1545` → IC=-0.182 (n=152)

  - _Acción_: SKIP cuando `libro_liquidez` < 3195.1545
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=310)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=959)

- **FILTRO** `libro_liquidez` < `1811.4604` → IC=-0.163 (n=244)

  - _Acción_: SKIP cuando `libro_liquidez` < 1811.4604
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=734)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.211 (n=278)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=864)

- **FILTRO** `libro_liquidez` < `1612.2849` → IC=-0.154 (n=287)

  - _Acción_: SKIP cuando `libro_liquidez` < 1612.2849
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=864)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.133 (n=20654)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=46395)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.297 (n=15900)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=51149)

- **FILTRO** `ibs_7min` < `0.2222` → IC=-0.232 (n=16719)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2222
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=50330)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.152 (n=22267)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=44782)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.244 (n=20935)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=63078)

- **FILTRO** `ibs_7min` > `0.2836` → IC=-0.183 (n=20998)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2836
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=63015)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.155 (n=2907)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=8969)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.318 (n=2887)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=8989)

- **FILTRO** `ibs_7min` < `0.7103` → IC=-0.249 (n=3918)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7103
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=7958)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.151 (n=2711)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=9165)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.277 (n=3484)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=11048)

- **FILTRO** `ibs_7min` > `0.7722` → IC=-0.214 (n=3632)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7722
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=10900)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.261 (n=2678)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=8528)

- **FILTRO** `ibs_7min` < `0.717` → IC=-0.205 (n=2801)

  - _Acción_: SKIP cuando `ibs_7min` < 0.717
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=8405)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.196 (n=2783)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=8423)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.269 (n=2610)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=8825)

- **FILTRO** `ibs_7min` > `0.2661` → IC=-0.193 (n=2858)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2661
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=8577)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.181 (n=2854)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=8581)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.164 (n=2758)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=8604)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.322 (n=2688)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=8674)

- **FILTRO** `ibs_7min` < `0.2857` → IC=-0.248 (n=3738)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=7624)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.198 (n=2379)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=8983)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.259 (n=3673)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=11703)

- **FILTRO** `ibs_7min` > `0.7308` → IC=-0.183 (n=3841)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7308
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=11535)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=2671)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=8187)

- **FILTRO** `ibs_7min` < `0.7188` → IC=-0.193 (n=2714)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7188
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=8144)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.189 (n=2701)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=8157)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.258 (n=2602)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=8723)

- **FILTRO** `ibs_7min` > `0.275` → IC=-0.174 (n=2830)

  - _Acción_: SKIP cuando `ibs_7min` > 0.275
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=8495)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.170 (n=2812)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=8513)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.296 (n=2519)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=8293)

- **FILTRO** `ibs_7min` < `0.7059` → IC=-0.229 (n=3541)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7059
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=7271)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.219 (n=2702)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=8110)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.195 (n=3907)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=12326)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=3507)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=7428)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.309 (n=2558)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=8377)

- **FILTRO** `ibs_7min` < `0.1743` → IC=-0.231 (n=2733)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1743
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=8202)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.203 (n=2505)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=8430)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.234 (n=3503)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=11609)

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
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=600)

- **FILTRO** `libro_liquidez` < `10478.3164` → IC=-0.154 (n=189)

  - _Acción_: SKIP cuando `libro_liquidez` < 10478.3164
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=569)

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
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=877)

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
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=667)

- **FILTRO** `libro_liquidez` < `3298.5458` → IC=-0.153 (n=191)

  - _Acción_: SKIP cuando `libro_liquidez` < 3298.5458
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=573)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4307` → IC=+0.154 (n=634)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio` |x|> 0.4307 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.135 (n=715)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 6.0 (IC base=+0.126)

- **PATRÓN** `total_vol_5m` < `418.1817` → IC=+0.168 (n=465)

  - _Acción_: Kelly boost +0.84€ cuando `total_vol_5m` < 418.1817 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `3556.2094` → IC=+0.144 (n=633)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 3556.2094 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.132 (n=621)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 13.0 (IC base=+0.126)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.193 (n=164)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 14.0 (IC base=+0.135)

- **PATRÓN** `total_vol_5m` < `377.422` → IC=+0.159 (n=294)

  - _Acción_: Kelly boost +0.79€ cuando `total_vol_5m` < 377.422 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `2532.1776` → IC=+0.226 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2532.1776 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.138 (n=147)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 6.0 (IC base=+0.135)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.4309` → IC=+0.144 (n=130)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio` |x|> 0.4309 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.137 (n=268)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.117)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4162` → IC=+0.194 (n=178)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.97€ cuando `delta_ratio` |x|> 0.4162 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.149 (n=280)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 4.0 (IC base=+0.133)

- **PATRÓN** `total_vol_5m` < `502.4124` → IC=+0.178 (n=178)

  - _Acción_: Kelly boost +0.89€ cuando `total_vol_5m` < 502.4124 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `5192.827` → IC=+0.136 (n=267)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 5192.827 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.195 (n=93)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 59.0 (IC base=+0.133)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.432` → IC=+0.212 (n=109)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.432 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.190 (n=172)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 12.0 (IC base=+0.147)

- **PATRÓN** `total_vol_5m` < `6100.528` → IC=+0.174 (n=210)

  - _Acción_: Kelly boost +0.87€ cuando `total_vol_5m` < 6100.528 (IC base=+0.147)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.123 (n=250)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 14.0 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=183)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.097)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.4417` → IC=-0.272 (n=55)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.4417
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=167)

- **FILTRO** `T_h` > `53.8669` → IC=-0.121 (n=581)

  - _Acción_: SKIP cuando `T_h` > 53.8669
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=195)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.144 (n=259)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0044 (IC base=-0.081)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `87.9936` → IC=-0.212 (n=57)

  - _Acción_: SKIP cuando `T_h` > 87.9936
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=173)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.256 (n=76)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=-0.035)

- **PATRÓN** `pct_vs_K` |x|≤ `1.632` → IC=+0.154 (n=76)

  - _Acción_: Kelly boost +0.77€ cuando `pct_vs_K` |x|≤ 1.632 (IC base=-0.035)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `T_h` > `88.6` → IC=-0.145 (n=60)

  - _Acción_: SKIP cuando `T_h` > 88.6
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=21)

- **FILTRO** `pct_vs_K` |x|> `6.9241` → IC=-0.259 (n=27)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.9241
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=54)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `T_h` < `90.336` → IC=-0.180 (n=73)

  - _Acción_: SKIP cuando `T_h` < 90.336
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=73)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `T_h` < `146.0708` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `T_h` < 146.0708
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0109` → IC=-0.232 (n=538)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0109
  - _Potencial_: sin este filtro IC_bueno=-0.137 (n=180)

- **FILTRO** `T_h` > `98.1124` → IC=-0.228 (n=358)

  - _Acción_: SKIP cuando `T_h` > 98.1124
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=360)

- **FILTRO** `sigma_h` > `0.01` → IC=-0.245 (n=151)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=459)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.221 (n=152)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=458)

- **FILTRO** `T_h` > `53.9898` → IC=-0.236 (n=457)

  - _Acción_: SKIP cuando `T_h` > 53.9898
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=153)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.009` → IC=-0.207 (n=172)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.009
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=61)

- **FILTRO** `T_h` > `63.9952` → IC=-0.203 (n=156)

  - _Acción_: SKIP cuando `T_h` > 63.9952
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=77)

- **FILTRO** `T_h` > `143.7867` → IC=-0.250 (n=54)

  - _Acción_: SKIP cuando `T_h` > 143.7867
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=166)

- **FILTRO** `pct_vs_K` |x|> `2.9616` → IC=-0.393 (n=54)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9616
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=166)

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
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=69)

- **FILTRO** `T_h` > `99.3756` → IC=-0.292 (n=99)

  - _Acción_: SKIP cuando `T_h` > 99.3756
  - _Potencial_: sin este filtro IC_bueno=-0.248 (n=101)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.354 (n=46)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=141)

- **FILTRO** `sigma_h` < `0.0053` → IC=-0.188 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.164 (n=141)

- **FILTRO** `T_h` > `57.2198` → IC=-0.232 (n=125)

  - _Acción_: SKIP cuando `T_h` > 57.2198
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=62)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.152 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0082` → IC=-0.308 (n=50)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0082
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=151)

- **FILTRO** `T_h` > `70.3179` → IC=-0.215 (n=149)

  - _Acción_: SKIP cuando `T_h` > 70.3179
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=52)

- **FILTRO** `sigma_h` > `0.0139` → IC=-0.330 (n=45)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0139
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=90)

- **FILTRO** `sigma_h` < `0.0081` → IC=-0.271 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0081
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=102)

- **FILTRO** `T_h` > `39.628` → IC=-0.272 (n=90)

  - _Acción_: SKIP cuando `T_h` > 39.628
  - _Potencial_: sin este filtro IC_bueno=-0.138 (n=45)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1208` → IC=+0.469 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1208 (IC base=+0.345)

- **PATRÓN** `sigma_h` < `0.013` → IC=+0.366 (n=95)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.013 (IC base=+0.345)

- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.378 (n=72)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.345)

- **PATRÓN** `T_h` < `0.3439` → IC=+0.395 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3439 (IC base=+0.345)

- **PATRÓN** `T_h` > `0.7285` → IC=+0.378 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7285 (IC base=+0.345)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.481 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.345)

- **PATRÓN** `edge` > `0.0997` → IC=+0.437 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.0997 (IC base=+0.406)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.429 (n=167)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.406)

- **PATRÓN** `T_h` < `0.6127` → IC=+0.442 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6127 (IC base=+0.406)

- **PATRÓN** `dist_50` > `0.4237` → IC=+0.451 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4237 (IC base=+0.406)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.472 (n=142)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.406)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1161` → IC=+0.296 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1161 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.278 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.204)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.237 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.204)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.265 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.289 (n=36)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.204)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1023` → IC=+0.462 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.415)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.417 (n=58)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0102 (IC base=+0.415)

- **PATRÓN** `T_h` < `1.2618` → IC=+0.433 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.2618 (IC base=+0.415)

- **PATRÓN** `dist_50` > `0.4084` → IC=+0.481 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4084 (IC base=+0.415)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.409 (n=31)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.415)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.444 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.415)

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
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=369)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=443)

- **PATRÓN** `streak_estiramiento` < `0.2918` → IC=+0.174 (n=93)

  - _Acción_: Kelly boost +0.87€ cuando `streak_estiramiento` < 0.2918 (IC base=+0.026)

- **PATRÓN** `streak_estiramiento` < `0.5383` → IC=+0.176 (n=202)

  - _Acción_: Kelly boost +0.88€ cuando `streak_estiramiento` < 0.5383 (IC base=+0.058)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.130 (n=225)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 32.0 (IC base=+0.058)

- **PATRÓN** `libro_liquidez` > `2537.4695` → IC=+0.127 (n=159)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 2537.4695 (IC base=+0.058)

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

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.129 (n=149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 7.0 (IC base=+0.094)

- **PATRÓN** `streak_estiramiento` < `0.4354` → IC=+0.185 (n=128)

  - _Acción_: Kelly boost +0.92€ cuando `streak_estiramiento` < 0.4354 (IC base=+0.094)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.164 (n=138)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 32.0 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `2230.4824` → IC=+0.128 (n=146)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 2230.4824 (IC base=+0.094)

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
- **PATRÓN** `volumen_racha` < `16919.513` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_racha` < 16919.513 (IC base=+0.058)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=1052)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=4543)

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
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=2621)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.188 (n=2038)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0059 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.2126` → IC=+0.169 (n=4632)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.2126 (IC base=+0.156)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3534` → IC=+0.165 (n=4284)

  - _Acción_: Kelly boost +0.82€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3534 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.166 (n=4278)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 6.0 (IC base=+0.156)

- **PATRÓN** `ibs_15` > `0.5` → IC=+0.223 (n=4656)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.1299` → IC=+0.150 (n=2173)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1299 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.528` → IC=+0.265 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.528 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `4936.1722` → IC=+0.180 (n=1544)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 4936.1722 (IC base=+0.156)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=1792)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.222 (n=732)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0055 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.0596` → IC=+0.252 (n=244)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0596 (IC base=+0.204)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2672` → IC=+0.224 (n=244)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2672 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.225 (n=762)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.204)

- **PATRÓN** `ibs_15` > `0.713` → IC=+0.279 (n=732)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.713 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.3735` → IC=+0.230 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3735 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` < `0.507` → IC=+0.208 (n=826)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.507 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.778` → IC=+0.312 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.778 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=947)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `15935.6674` → IC=+0.228 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15935.6674 (IC base=+0.204)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.154 (n=892)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0069 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.152 (n=595)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.136)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1424` → IC=+0.137 (n=595)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio_macro` |x|> 0.1424 (IC base=+0.136)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2839` → IC=+0.139 (n=719)

  - _Acción_: Kelly boost +0.70€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2839 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.142 (n=813)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 6.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.139 (n=937)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_15` > `0.5006` → IC=+0.225 (n=892)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5006 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.1187` → IC=+0.149 (n=556)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1187 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.4285` → IC=+0.138 (n=948)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.4285 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.929` → IC=+0.289 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.929 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `5808.0125` → IC=+0.166 (n=405)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 5808.0125 (IC base=+0.136)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `ibs_15` > `0.2506` → IC=-0.121 (n=180)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2506
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=352)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8684` → IC=+0.202 (n=397)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8684 (IC base=+0.069)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0194` → IC=+0.182 (n=715)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0194 (IC base=+0.177)

- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.187 (n=1071)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0127 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.0656` → IC=+0.214 (n=358)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0656 (IC base=+0.177)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.352` → IC=+0.201 (n=970)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.352 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.180 (n=982)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.184 (n=963)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 14.0 (IC base=+0.177)

- **PATRÓN** `ibs_15` > `0.5728` → IC=+0.272 (n=957)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5728 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.4758` → IC=+0.216 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4758 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.892` → IC=+0.231 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.892 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `2947.1379` → IC=+0.213 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2947.1379 (IC base=+0.177)

- **PATRÓN** `ibs_15` < `0.1099` → IC=+0.164 (n=886)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.82€ cuando `ibs_15` < 0.1099 (IC base=+0.068)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.388 (n=238)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.364)

- **PATRÓN** `drift_60min` |x|≤ `0.1115` → IC=+0.364 (n=476)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1115 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1505` → IC=+0.381 (n=475)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1505 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1077` → IC=+0.382 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1077 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.372 (n=756)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.7883` → IC=+0.395 (n=713)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7883 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.1523` → IC=+0.383 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1523 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.204` → IC=+0.399 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.204 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.368 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `3859.8614` → IC=+0.373 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3859.8614 (IC base=+0.364)

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
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.369 (n=356)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.365)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.379 (n=237)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.365)

- **PATRÓN** `drift_60min` |x|≤ `0.1077` → IC=+0.367 (n=238)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1077 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0824` → IC=+0.375 (n=318)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0824 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2929` → IC=+0.379 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2929 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.367 (n=358)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.365)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.378 (n=162)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.8138` → IC=+0.400 (n=318)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8138 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.374 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` < `0.6543` → IC=+0.371 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6543 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.577` → IC=+0.409 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.577 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.370 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `4045.1116` → IC=+0.390 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4045.1116 (IC base=+0.365)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0102` → IC=-0.222 (n=1696)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0102
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=3293)

- **FILTRO** `drift_15min` |x|> `0.9075` → IC=-0.137 (n=1245)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9075
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=3743)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.215 (n=2040)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=2949)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1398` → IC=+0.223 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1398 (IC base=-0.075)

- **PATRÓN** `ibs_15` > `0.6307` → IC=+0.280 (n=1159)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6307 (IC base=-0.075)

- **PATRÓN** `dist_vwap_pct` > `0.1109` → IC=+0.201 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1109 (IC base=-0.075)

- **PATRÓN** `dist_vwap_pct` < `0.4198` → IC=+0.200 (n=1140)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4198 (IC base=-0.075)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2361` → IC=+0.267 (n=1493)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2361 (IC base=-0.006)

- **PATRÓN** `ibs_15` < `0.3679` → IC=+0.283 (n=4479)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3679 (IC base=-0.006)

- **PATRÓN** `dist_vwap_pct` > `0.8625` → IC=+0.281 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8625 (IC base=-0.006)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0322` → IC=-0.224 (n=2335)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0322
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=782)

- **FILTRO** `sigma_h` < `0.0036` → IC=-0.216 (n=779)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0036
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=2338)

- **FILTRO** `sigma_ewma_delta_pct` > `22.473` → IC=-0.263 (n=449)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.473
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=2668)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.158 (n=302)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.003 (IC base=+0.076)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2667` → IC=+0.269 (n=132)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2667 (IC base=+0.076)

- **PATRÓN** `ibs_15` > `0.7609` → IC=+0.329 (n=396)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7609 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` > `0.1043` → IC=+0.280 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1043 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` < `0.3659` → IC=+0.284 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3659 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.802` → IC=+0.144 (n=206)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 22.802 (IC base=+0.076)

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
  - _Potencial_: sin este filtro IC_bueno=+0.156 (n=757)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.159 (n=511)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0058 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.157` → IC=+0.167 (n=511)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.157 (IC base=+0.149)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2995` → IC=+0.200 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2995 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.164 (n=417)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 11.0 (IC base=+0.149)

- **PATRÓN** `ibs_15` > `0.5756` → IC=+0.243 (n=581)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5756 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.1135` → IC=+0.149 (n=360)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1135 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.1594` → IC=+0.153 (n=451)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1594 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.049` → IC=+0.265 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.049 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=757)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `5063.7944` → IC=+0.153 (n=387)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 5063.7944 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.255 (n=1122)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.3568` → IC=+0.244 (n=1481)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3568 (IC base=+0.242)

- **PATRÓN** `drift_15min` |x|≤ `0.7706` → IC=+0.256 (n=1481)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7706 (IC base=+0.242)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1571` → IC=+0.256 (n=1122)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1571 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.246 (n=1213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.242 (n=1495)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.242)

- **PATRÓN** `ibs_15` < `0.3774` → IC=+0.273 (n=1684)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3774 (IC base=+0.242)

- **PATRÓN** `dist_vwap_pct` > `0.7978` → IC=+0.271 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7978 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.363` → IC=+0.246 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.363 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.251` → IC=+0.248 (n=1756)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.251 (IC base=+0.242)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1822` → IC=-0.253 (n=285)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1822
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=859)

- **FILTRO** `drift_60min` |x|> `0.1726` → IC=-0.251 (n=388)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1726
  - _Potencial_: sin este filtro IC_bueno=-0.161 (n=756)

- **FILTRO** `drift_15min` |x|> `0.9075` → IC=-0.284 (n=285)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9075
  - _Potencial_: sin este filtro IC_bueno=-0.161 (n=859)

- **FILTRO** `sigma_ewma_delta_pct` > `6.328` → IC=-0.206 (n=267)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.328
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=877)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.192)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.192)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1292 (IC base=-0.192)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 29.0 (IC base=-0.192)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0658` → IC=+0.232 (n=763)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0658 (IC base=-0.031)

- **PATRÓN** `ibs_15` < `0.3926` → IC=+0.296 (n=763)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3926 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` < `0.1951` → IC=+0.245 (n=692)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1951 (IC base=-0.031)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.1502` → IC=-0.229 (n=345)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1502
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=1039)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.242 (n=665)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=719)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.212)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.212)

- **PATRÓN** `delta_ratio_macro` |x|> `0.119` → IC=+0.273 (n=673)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.119 (IC base=-0.021)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.119` → IC=+0.289 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.119 (IC base=-0.021)

- **PATRÓN** `ibs_15` < `0.1346` → IC=+0.308 (n=674)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1346 (IC base=-0.021)

- **PATRÓN** `dist_vwap_pct` > `0.7312` → IC=+0.334 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7312 (IC base=-0.021)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.159 (n=39)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.006 (IC base=+0.090)

- **PATRÓN** `drift_60min` |x|≤ `0.1106` → IC=+0.188 (n=30)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.1106 (IC base=+0.090)

- **PATRÓN** `drift_15min` |x|≤ `0.3696` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3696 (IC base=+0.090)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2386` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2386 (IC base=+0.090)

- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.370 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` < `0.0949` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0949 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` > `0.1526` → IC=+0.127 (n=73)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` > 0.1526 (IC base=+0.055)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.159 (n=39)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.006 (IC base=+0.090)

- **PATRÓN** `drift_60min` |x|≤ `0.1106` → IC=+0.188 (n=30)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.1106 (IC base=+0.090)

- **PATRÓN** `drift_15min` |x|≤ `0.3696` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3696 (IC base=+0.090)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2386` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2386 (IC base=+0.090)

- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.370 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` < `0.0949` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0949 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` > `0.1526` → IC=+0.127 (n=73)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` > 0.1526 (IC base=+0.055)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.291 (n=1257)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.0733` → IC=+0.313 (n=554)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0733 (IC base=+0.286)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1516` → IC=+0.290 (n=838)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1516 (IC base=+0.286)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2237` → IC=+0.295 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2237 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.302 (n=1300)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.286)

- **PATRÓN** `ibs_15` > `0.8399` → IC=+0.315 (n=1257)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8399 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.2676` → IC=+0.314 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2676 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.334` → IC=+0.387 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.334 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `13500.5638` → IC=+0.305 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13500.5638 (IC base=+0.286)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.311 (n=225)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.280)

- **PATRÓN** `drift_60min` |x|≤ `0.0596` → IC=+0.314 (n=224)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0596 (IC base=+0.280)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3948` → IC=+0.284 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3948 (IC base=+0.280)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.301 (n=700)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.280)

- **PATRÓN** `ibs_15` > `0.8292` → IC=+0.305 (n=669)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8292 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.2516` → IC=+0.311 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2516 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.101` → IC=+0.388 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.101 (IC base=+0.280)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.280 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `15953.0262` → IC=+0.318 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15953.0262 (IC base=+0.280)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.310 (n=588)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.0524` → IC=+0.323 (n=196)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0524 (IC base=+0.294)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0665` → IC=+0.297 (n=588)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0665 (IC base=+0.294)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1019` → IC=+0.337 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1019 (IC base=+0.294)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.307 (n=563)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.294)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.301 (n=536)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.294)

- **PATRÓN** `ibs_15` > `0.8516` → IC=+0.322 (n=588)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8516 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` > `0.1243` → IC=+0.311 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1243 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` < `0.6569` → IC=+0.295 (n=666)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6569 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.513` → IC=+0.388 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.513 (IC base=+0.294)

### UPDOWN_OU_5M
- **FILTRO** `delta_ratio_macro` |x|≤ `0.126` → IC=-0.159 (n=89)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.126
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=272)

- **FILTRO** `ballena_activa_n` > `34.0` → IC=-0.129 (n=246)

  - _Acción_: SKIP cuando `ballena_activa_n` > 34.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=83)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1387` → IC=-0.141 (n=51)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1387
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

- **FILTRO** `delta_ratio_macro` |x|≤ `0.306` → IC=-0.385 (n=24)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.306
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

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
- **PATRÓN** `ratio` < `0.9711` → IC=+0.389 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9711 (IC base=+0.175)

- **PATRÓN** `T_h` > `115.5985` → IC=+0.353 (n=2589)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 115.5985 (IC base=+0.335)

- **PATRÓN** `ratio` > `1.0203` → IC=+0.378 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0203 (IC base=+0.335)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `111.9836` → IC=+0.138 (n=241)

  - _Acción_: Kelly boost +0.69€ cuando `T_h` > 111.9836 (IC base=+0.137)

- **PATRÓN** `ratio` < `0.9933` → IC=+0.260 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9933 (IC base=+0.137)

- **PATRÓN** `T_h` > `111.9824` → IC=+0.312 (n=919)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9824 (IC base=+0.299)

- **PATRÓN** `ratio` > `1.0177` → IC=+0.353 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0177 (IC base=+0.299)

### WEEKLY_PRICE#ETH
- **PATRÓN** `ratio` < `0.985` → IC=+0.419 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.985 (IC base=+0.222)

- **PATRÓN** `T_h` > `111.996` → IC=+0.352 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.996 (IC base=+0.321)

- **PATRÓN** `ratio` > `1.0298` → IC=+0.400 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0298 (IC base=+0.321)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0625` → IC=+0.431 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0625 (IC base=+0.398)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5 sube el IC de +0.156 a +0.223 en UPDOWN_GBM#15min (n=4656). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.713 sube el IC de +0.204 a +0.279 en UPDOWN_GBM#BTC#15min (n=732). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5006 sube el IC de +0.136 a +0.225 en UPDOWN_GBM#ETH#15min (n=892). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.8684 sube el IC de +0.069 a +0.202 en UPDOWN_GBM#SOL#15min (n=397). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5728 sube el IC de +0.177 a +0.272 en UPDOWN_GBM#XRP#15min (n=957). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1099 sube el IC de +0.068 a +0.164 en UPDOWN_GBM#XRP#15min (n=886). Ya aplicado como kelly_boost=+0.82€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6307 sube el IC de -0.075 a +0.280 en UPDOWN_GBM_15M_TARDIO (n=1159). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3679 sube el IC de -0.006 a +0.283 en UPDOWN_GBM_15M_TARDIO (n=4479). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7609 sube el IC de +0.076 a +0.329 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=396). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.186 a +0.322 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=71). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5756 sube el IC de +0.149 a +0.243 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=581). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3774 sube el IC de +0.242 a +0.273 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1684). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.192 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3926 sube el IC de -0.031 a +0.296 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=763). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.212 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.1346 sube el IC de -0.021 a +0.308 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=674). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.090 a +0.370 en UPDOWN_GBM_ETH_15M_HORA7 (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.090 a +0.370 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8399 sube el IC de +0.286 a +0.315 en UPDOWN_GBM_IBS_ALTO (n=1257). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8292 sube el IC de +0.280 a +0.305 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=669). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8516 sube el IC de +0.294 a +0.322 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=588). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7883 sube el IC de +0.364 a +0.395 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=713). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.362 a +0.386 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=357). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.8138 sube el IC de +0.365 a +0.400 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=318). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2099 | +0.085 | +226.57€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2099 | +0.085 | +226.57€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1696 | +0.087 | +191.12€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1696 | +0.087 | +191.12€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 284 | +0.070 | +11.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 284 | +0.070 | +11.30€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 88 | +0.122 | +24.47€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 88 | +0.122 | +24.47€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 954 | -0.026 | +71.37€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 954 | -0.026 | +71.37€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 727 | -0.049 | +48.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 727 | -0.049 | +48.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 150 | +0.086 | +25.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 150 | +0.086 | +25.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 71 | -0.034 | -4.85€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 71 | -0.034 | -4.85€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 44963 | -0.085 | -5577.51€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2663 | +0.057 | -283.07€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 42300 | -0.093 | -5294.45€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4701 | -0.112 | -761.79€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4701 | -0.112 | -761.79€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2663 | +0.057 | -283.07€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2663 | +0.057 | -283.07€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4653 | -0.116 | -897.83€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4653 | -0.116 | -897.83€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 12223 | -0.034 | -1051.28€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 12223 | -0.034 | -1051.28€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 12159 | -0.116 | -1216.98€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 12159 | -0.116 | -1216.98€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8564 | -0.124 | -1366.56€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8564 | -0.124 | -1366.56€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 44294 | -0.013 | +3093.06€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 11437 | +0.005 | +1598.67€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 32857 | -0.019 | +1494.38€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 44294 | -0.013 | +3093.06€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 11437 | +0.005 | +1598.67€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 32857 | -0.019 | +1494.38€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 173405 | +0.114 | -7018.85€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 20845 | +0.181 | -643.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 784 | +0.000 | -75.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 141717 | +0.106 | -5923.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 10059 | +0.092 | -376.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 23482 | +0.105 | -1528.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 70 | -0.167 | +13.96€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 23397 | +0.106 | -1530.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 33137 | +0.125 | -551.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5558 | +0.180 | -218.40€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 23467 | +0.120 | -166.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4070 | +0.077 | -144.01€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 23534 | +0.098 | -1681.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 83 | -0.112 | +7.08€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 23436 | +0.100 | -1676.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 36985 | +0.124 | -712.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 9410 | +0.178 | -204.15€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 23827 | +0.106 | -442.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3736 | +0.101 | -57.91€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#SOL | 32757 | +0.112 | -1512.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5643 | +0.199 | -250.73€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 687 | +0.028 | -21.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 24174 | +0.096 | -1065.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2253 | +0.103 | -174.24€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#XRP | 23510 | +0.107 | -1032.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 81 | -0.115 | +8.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 23416 | +0.108 | -1041.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 28038 | +0.194 | -1859.63€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 28038 | +0.194 | -1859.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 6334 | +0.175 | -591.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 6334 | +0.175 | -591.76€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 3895 | +0.199 | -130.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 3895 | +0.199 | -130.37€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 6251 | +0.175 | -544.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 6251 | +0.175 | -544.30€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5319 | +0.249 | -191.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5319 | +0.249 | -191.83€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 6160 | +0.186 | -415.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 6160 | +0.186 | -415.13€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1174 | +0.425 | -44.32€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1174 | +0.425 | -44.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 479 | +0.440 | -3.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 479 | +0.440 | -3.74€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 472 | +0.424 | -17.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 472 | +0.424 | -17.84€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 209 | +0.396 | -18.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 209 | +0.396 | -18.87€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 98680 | +0.201 | -7154.39€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 98680 | +0.201 | -7154.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 17002 | +0.182 | -1841.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 17002 | +0.182 | -1841.92€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 15912 | +0.226 | -504.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 15912 | +0.226 | -504.15€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 16942 | +0.180 | -1792.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 16942 | +0.180 | -1792.25€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 16051 | +0.218 | -644.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 16051 | +0.218 | -644.86€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 16327 | +0.202 | -1057.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 16327 | +0.202 | -1057.80€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 16446 | +0.197 | -1313.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 16446 | +0.197 | -1313.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 37914 | +0.117 | +317.12€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 37914 | +0.117 | +317.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 18875 | +0.118 | +200.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 18875 | +0.118 | +200.61€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 19039 | +0.116 | +116.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 19039 | +0.116 | +116.51€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2406 | +0.293 | -8.74€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2406 | +0.293 | -8.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1100 | +0.280 | -27.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1100 | +0.280 | -27.08€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1174 | +0.298 | +16.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1174 | +0.298 | +16.27€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 132 | +0.336 | +2.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 132 | +0.336 | +2.06€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1103 | +0.442 | +5.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1103 | +0.442 | +5.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 530 | +0.436 | -5.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 530 | +0.436 | -5.16€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 524 | +0.449 | +9.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 524 | +0.449 | +9.44€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 49 | +0.402 | +0.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 49 | +0.402 | +0.96€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1864 | +0.068 | -83.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1139 | +0.081 | -18.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1430 | +0.075 | -37.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1139 | +0.081 | -18.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 76310 | +0.101 | -1831.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 6147 | +0.095 | +117.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 70163 | +0.101 | -1949.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 41784 | +0.106 | -410.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 6147 | +0.095 | +117.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 35637 | +0.107 | -528.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 16061 | +0.109 | -77.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 16061 | +0.109 | -77.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 18465 | +0.082 | -1343.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 18465 | +0.082 | -1343.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 1 | 4 |
| ✅ GBM_LATE_15M | 51951 | +0.097 | +28534.64€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 51951 | +0.097 | +28534.64€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 8628 | +0.223 | +7370.00€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 8628 | +0.223 | +7370.00€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 7907 | +0.174 | +6139.14€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 7907 | +0.174 | +6139.14€ | 0 | 23 |
| ✅ GBM_LATE_15M#DOGE | 9312 | +0.206 | +7292.20€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 9312 | +0.206 | +7292.20€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 7092 | +0.050 | +2149.99€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 7092 | +0.050 | +2149.99€ | 1 | 19 |
| ✅ GBM_LATE_15M#SOL | 7260 | -0.031 | +1888.25€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 7260 | -0.031 | +1888.25€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 11752 | -0.026 | +3695.06€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 11752 | -0.026 | +3695.06€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 54827 | +0.085 | +31455.73€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 54827 | +0.085 | +31455.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 10674 | -0.001 | +5683.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 10674 | -0.001 | +5683.47€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 11713 | +0.005 | +3038.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 11713 | +0.005 | +3038.38€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 7500 | +0.290 | +8432.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 7500 | +0.290 | +8432.36€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 10292 | +0.014 | +3107.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 10292 | +0.014 | +3107.20€ | 1 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 8518 | +0.042 | +3745.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 8518 | +0.042 | +3745.03€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 6130 | +0.314 | +7449.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 6130 | +0.314 | +7449.29€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 41190 | +0.179 | +33892.21€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 41190 | +0.179 | +33892.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 6201 | +0.239 | +5757.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 6201 | +0.239 | +5757.06€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 6545 | +0.139 | +4803.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 6545 | +0.139 | +4803.53€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 6614 | +0.224 | +5729.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 6614 | +0.224 | +5729.88€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 7032 | +0.132 | +5476.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 7032 | +0.132 | +5476.14€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 7771 | +0.121 | +5806.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 7771 | +0.121 | +5806.06€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 7027 | +0.232 | +6319.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 7027 | +0.232 | +6319.54€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 10962 | +0.125 | +5419.12€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 10962 | +0.125 | +5419.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 462 | +0.157 | +298.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 462 | +0.157 | +298.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3181 | +0.132 | +1743.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3181 | +0.132 | +1743.56€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 491 | +0.153 | +259.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 491 | +0.153 | +259.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3230 | +0.127 | +1575.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3230 | +0.127 | +1575.06€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2727 | +0.092 | +1047.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2727 | +0.092 | +1047.47€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 871 | +0.158 | +494.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 871 | +0.158 | +494.43€ | 0 | 28 |
| ✅ GBM_LATE_15M_TARDIO | 52189 | +0.186 | +42592.98€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 52189 | +0.186 | +42592.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 8243 | +0.248 | +7926.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 8243 | +0.248 | +7926.30€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 8260 | +0.136 | +5635.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 8260 | +0.136 | +5635.98€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 8843 | +0.233 | +7933.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 8843 | +0.233 | +7933.93€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 8652 | +0.139 | +6340.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 8652 | +0.139 | +6340.86€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 9257 | +0.122 | +6557.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 9257 | +0.122 | +6557.60€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 8934 | +0.238 | +8198.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 8934 | +0.238 | +8198.32€ | 0 | 19 |
| ✅ GBM_LATE_5M | 13563 | +0.209 | +10954.35€ | 1 | 28 |
| ✅ GBM_LATE_5M#5min | 13563 | +0.209 | +10954.35€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3215 | +0.209 | +2746.87€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3215 | +0.209 | +2746.87€ | 0 | 26 |
| ✅ GBM_LATE_5M#DOGE | 1249 | +0.198 | +934.84€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1249 | +0.198 | +934.84€ | 0 | 17 |
| ✅ GBM_LATE_5M#ETH | 3935 | +0.203 | +2957.58€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3935 | +0.203 | +2957.58€ | 0 | 26 |
| ✅ GBM_LATE_5M#SOL | 2152 | +0.207 | +1779.58€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2152 | +0.207 | +1779.58€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1958 | +0.209 | +1535.21€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1958 | +0.209 | +1535.21€ | 0 | 0 |
| ✅ GBM_LATE_60M | 4523 | +0.050 | +1230.17€ | 0 | 6 |
| ✅ GBM_LATE_60M#60min | 4523 | +0.050 | +1230.17€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1601 | +0.063 | +505.12€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1601 | +0.063 | +505.12€ | 1 | 5 |
| ✅ GBM_LATE_60M#ETH | 1464 | +0.050 | +436.30€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1464 | +0.050 | +436.30€ | 2 | 6 |
| ✅ GBM_LATE_60M#SOL | 1458 | +0.036 | +288.75€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1458 | +0.036 | +288.75€ | 0 | 9 |
| 🚫 GBM_LATE_60M_FADE | 667 | -0.250 | -35.29€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 667 | -0.250 | -35.29€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 251 | -0.251 | -20.27€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 251 | -0.251 | -20.27€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 239 | -0.247 | -7.78€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 239 | -0.247 | -7.78€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 177 | -0.249 | -7.24€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 177 | -0.249 | -7.24€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1836 | +0.080 | +460.39€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1836 | +0.080 | +460.39€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 716 | +0.070 | +165.64€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 716 | +0.070 | +165.64€ | 1 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 627 | +0.055 | +107.34€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 627 | +0.055 | +107.34€ | 2 | 14 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 493 | +0.126 | +187.41€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 493 | +0.126 | +187.41€ | 2 | 9 |
| ✅ LATE_WINDOW_5MIN | 200 | +0.272 | +207.61€ | 1 | 13 |
| ✅ LATE_WINDOW_5MIN#5min | 200 | +0.272 | +207.61€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 200 | +0.272 | +207.61€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 200 | +0.272 | +207.61€ | 1 | 13 |
| ✅ LEADLAG_BTC_XRP_15M | 4156 | +0.097 | +953.06€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4156 | +0.097 | +953.06€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4156 | +0.097 | +953.06€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4156 | +0.097 | +953.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 843 | -0.017 | +7.49€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 843 | -0.017 | +7.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 20 | -0.091 | -2.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 20 | -0.091 | -2.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 251 | -0.018 | +3.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 251 | -0.018 | +3.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 29 | -0.145 | -4.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 29 | -0.145 | -4.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 226 | +0.031 | +17.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 226 | +0.031 | +17.62€ | 2 | 3 |
| ✅ LIQUIDACIONES_15M#SOL | 265 | -0.006 | +2.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 265 | -0.006 | +2.89€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4096 | +0.016 | +101.29€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 4096 | +0.016 | +101.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 191 | +0.034 | +0.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 191 | +0.034 | +0.28€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 821 | +0.015 | +40.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 821 | +0.015 | +40.39€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 216 | +0.000 | +1.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 216 | +0.000 | +1.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1635 | +0.019 | +27.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1635 | +0.019 | +27.71€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 763 | +0.011 | +1.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 763 | +0.011 | +1.66€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 470 | +0.015 | +29.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 470 | +0.015 | +29.46€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2155 | -0.036 | -20.67€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2155 | -0.036 | -20.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 651 | -0.028 | -10.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 651 | -0.028 | -10.39€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 755 | -0.015 | +10.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 755 | -0.015 | +10.10€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 749 | -0.065 | -20.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 749 | -0.065 | -20.37€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 12898 | -0.032 | -107.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 6193 | -0.035 | -90.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 6705 | -0.029 | -16.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 455 | -0.038 | -12.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 232 | -0.004 | +11.19€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 223 | -0.073 | -23.63€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 3357 | -0.024 | +5.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1600 | -0.024 | +6.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1757 | -0.025 | -1.36€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1310 | -0.022 | +31.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 666 | -0.030 | +4.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 644 | -0.014 | +26.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 2892 | -0.036 | -65.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1368 | -0.041 | -47.27€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1524 | -0.032 | -17.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 2476 | -0.029 | -5.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1200 | -0.037 | -22.31€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1276 | -0.022 | +16.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 2408 | -0.043 | -60.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1127 | -0.051 | -43.36€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1281 | -0.035 | -16.86€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 61344 | +0.000 | +3372.04€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 61344 | +0.000 | +3372.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 11093 | +0.028 | +1523.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 11093 | +0.028 | +1523.08€ | 2 | 3 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 8657 | -0.035 | -91.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 8657 | -0.035 | -91.57€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 11228 | +0.025 | +1214.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 11228 | +0.025 | +1214.16€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 8554 | -0.049 | -160.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 8554 | -0.049 | -160.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 10427 | -0.005 | +290.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 10427 | -0.005 | +290.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 11385 | +0.018 | +596.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 11385 | +0.018 | +596.62€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7016 | -0.055 | -119.61€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7016 | -0.055 | -119.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1242 | -0.002 | -15.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1242 | -0.002 | -15.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1922 | -0.068 | -32.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1922 | -0.068 | -32.87€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 69 | -0.007 | +0.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 69 | -0.007 | +0.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 796 | -0.119 | -34.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 796 | -0.119 | -34.03€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2129 | -0.068 | -11.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2129 | -0.068 | -11.52€ | 4 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 151062 | -0.077 | +2116.08€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 151062 | -0.077 | +2116.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 26408 | -0.078 | +1446.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 26408 | -0.078 | +1446.34€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 22641 | -0.100 | -1064.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 22641 | -0.100 | -1064.94€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 26738 | -0.069 | +1287.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 26738 | -0.069 | +1287.84€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 22183 | -0.097 | -637.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 22183 | -0.097 | -637.23€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 27045 | -0.057 | +326.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 27045 | -0.057 | +326.51€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 26047 | -0.069 | +757.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 26047 | -0.069 | +757.57€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8973 | -0.035 | -185.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8973 | -0.035 | -185.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1002 | -0.017 | -19.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1002 | -0.017 | -19.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2066 | -0.047 | -29.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2066 | -0.047 | -29.54€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2628 | -0.026 | -39.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2628 | -0.026 | -39.75€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1264 | -0.064 | -31.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1264 | -0.064 | -31.96€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1004 | -0.031 | -32.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1004 | -0.031 | -32.55€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 1995 | +0.121 | +804.79€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 1859 | +0.126 | +792.20€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 444 | +0.135 | +217.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 444 | +0.135 | +217.31€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 382 | +0.117 | +132.37€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 382 | +0.117 | +132.37€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 355 | +0.133 | +170.19€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 355 | +0.133 | +170.19€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 318 | +0.147 | +170.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 318 | +0.147 | +170.02€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 360 | +0.097 | +102.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 360 | +0.097 | +102.31€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1905 | -0.015 | -16.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1905 | -0.015 | -16.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 359 | +0.010 | +18.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 359 | +0.010 | +18.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 344 | -0.035 | -13.70€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 344 | -0.035 | -13.70€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 485 | -0.042 | -32.78€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 485 | -0.042 | -32.78€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 384 | +0.000 | -0.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 384 | +0.000 | -0.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 333 | -0.002 | +12.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 333 | -0.002 | +12.26€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1065 | -0.079 | -53.39€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 490 | -0.112 | -79.35€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 378 | -0.129 | -60.89€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 112 | -0.053 | -18.46€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 375 | -0.038 | +20.37€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 264 | -0.023 | +29.81€ | 1 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 111 | -0.075 | -9.44€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 200 | -0.074 | +5.60€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 164 | -0.072 | +3.76€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 36 | -0.079 | +1.84€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 806 | -0.083 | -27.32€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 259 | -0.067 | -26.07€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1328 | -0.210 | -89.14€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 520 | -0.211 | -51.46€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 453 | -0.210 | -47.15€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 67 | -0.210 | -4.31€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 445 | -0.214 | -39.79€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 387 | -0.225 | -46.70€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 58 | -0.133 | +6.91€ | 1 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 363 | -0.201 | +2.11€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 336 | -0.198 | -0.29€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 27 | -0.224 | +2.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1176 | -0.212 | -94.14€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 152 | -0.188 | +5.00€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 511 | +0.389 | +478.63€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 92 | +0.181 | +67.23€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 92 | +0.181 | +67.23€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#ETH | 119 | +0.368 | +103.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 119 | +0.368 | +103.94€ | 0 | 6 |
| ✅ RESOLUTION_SNIPER#SOL | 300 | +0.457 | +307.46€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 300 | +0.457 | +307.46€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 511 | +0.389 | +478.63€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 850 | +0.043 | +76.36€ | 2 | 4 |
| ✅ STREAK_FADE_15M#15min | 850 | +0.043 | +76.36€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 315 | +0.030 | +7.53€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 315 | +0.030 | +7.53€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 69 | +0.007 | +1.00€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 69 | +0.007 | +1.00€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 83 | +0.018 | +6.06€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 83 | +0.018 | +6.06€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 383 | +0.066 | +61.77€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 383 | +0.066 | +61.77€ | 1 | 5 |
| ✅ STREAK_FADE_5M | 3540 | -0.023 | -141.35€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3540 | -0.023 | -141.35€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 602 | -0.028 | -26.89€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 602 | -0.028 | -26.89€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 169 | -0.038 | -13.78€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 169 | -0.038 | -13.78€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1642 | -0.019 | -60.48€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1642 | -0.019 | -60.48€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 112 | -0.044 | -9.57€ | 2 | 0 |
| ✅ STREAK_FADE_60M#60min | 112 | -0.044 | -9.57€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 43 | -0.100 | -5.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 43 | -0.100 | -5.07€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 69 | -0.007 | -4.51€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 69 | -0.007 | -4.51€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 11416 | +0.015 | +77.86€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11416 | +0.015 | +77.86€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2962 | +0.018 | +24.97€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2962 | +0.018 | +24.97€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2965 | +0.018 | +37.54€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2965 | +0.018 | +37.54€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2910 | +0.009 | -1.79€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2910 | +0.009 | -1.79€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2579 | +0.013 | +17.14€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2579 | +0.013 | +17.14€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 10924 | +0.015 | -35.24€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 10924 | +0.015 | -35.24€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4562 | +0.020 | -0.47€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4562 | +0.020 | -0.47€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3707 | +0.011 | -24.86€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3707 | +0.011 | -24.86€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2655 | +0.011 | -9.91€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2655 | +0.011 | -9.91€ | 1 | 0 |
| ✅ UPDOWN_GBM | 94905 | +0.059 | +9041.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 23168 | +0.083 | +4985.88€ | 0 | 8 |
| ✅ UPDOWN_GBM#240min | 2923 | +0.001 | +28.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 62864 | +0.059 | +3934.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 5621 | +0.001 | +97.99€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 7929 | +0.103 | +1446.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1779 | +0.164 | +820.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 6060 | +0.087 | +628.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 21692 | +0.057 | +1908.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3125 | +0.084 | +720.72€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 816 | +0.001 | +12.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 15111 | +0.066 | +1104.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2521 | -0.001 | +67.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 119 | -0.070 | +3.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 10163 | +0.078 | +1192.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1761 | +0.154 | +738.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 8316 | +0.062 | +454.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 22521 | +0.049 | +1558.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 5522 | +0.072 | +844.91€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 786 | +0.006 | +18.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 14043 | +0.050 | +670.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2060 | +0.004 | +24.38€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 110 | -0.107 | +1.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 20357 | +0.038 | +1145.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 6012 | +0.035 | +439.72€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 748 | -0.011 | +2.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 12459 | +0.047 | +704.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1040 | +0.002 | +5.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 98 | -0.140 | -7.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 12241 | +0.072 | +1791.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4969 | +0.099 | +1421.87€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 6875 | +0.056 | +370.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 327 | -0.105 | -2.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 950 | +0.364 | +345.31€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 950 | +0.364 | +345.31€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 476 | +0.362 | +165.49€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 476 | +0.362 | +165.49€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 474 | +0.365 | +179.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 474 | +0.365 | +179.82€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 23244 | -0.021 | +5767.55€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 23244 | -0.021 | +5767.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 4324 | -0.113 | +230.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 4324 | -0.113 | +230.97€ | 3 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3017 | +0.218 | +1921.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3017 | +0.218 | +1921.79€ | 1 | 20 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 6548 | -0.059 | +955.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 6548 | -0.059 | +955.07€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 6303 | -0.063 | +1198.68€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 6303 | -0.063 | +1198.68€ | 2 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 275 | +0.063 | +26.65€ | 0 | 7 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 275 | +0.063 | +26.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 275 | +0.063 | +26.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 275 | +0.063 | +26.65€ | 0 | 7 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1675 | +0.286 | +1413.25€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1675 | +0.286 | +1413.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 892 | +0.280 | +702.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 892 | +0.280 | +702.78€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 783 | +0.294 | +710.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 783 | +0.294 | +710.47€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 848 | -0.113 | -83.75€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 848 | -0.113 | -83.75€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 262 | -0.083 | -20.25€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 262 | -0.083 | -20.25€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 94 | -0.167 | -10.43€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 94 | -0.167 | -10.43€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 109 | -0.176 | -3.72€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 109 | -0.176 | -3.72€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 4278 | +0.301 | +1975.14€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 1613 | +0.257 | +203.51€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1645 | +0.295 | +715.03€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1020 | +0.381 | +1056.60€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.024 n=1167 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1167 IC=+0.024 PNL=+56.87€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 782 celda(s) pasan gate riguroso completo de 2825 evaluadas (n>=40) y 3930 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.035 < 0.08 — monitorear
  - _Datos_: n=6005 IC=+0.035 PNL=+439.09€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1645/15 IC=+0.295 PNL=+715.03€ | BTC: n=1613/15 IC=+0.257 PNL=+203.51€ | SOL: n=1020/15 IC=+0.381 PNL=+1056.60€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.146 n=1007/60 | contraria IC=+0.187 n=1049 | gap=-0.041 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=547, boost estimado=+0.014. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=2058/40 IC=+0.004 PNL=+24.37€ | BTC#60min: n=2519/40 IC=-0.001 PNL=+67.94€ | SOL#60min: n=1039/40 IC=+0.001 PNL=+5.08€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.046 n=669266 | tras_1loss IC=+0.098 n=507770 | tras_2loss IC=+0.068 n=203932/40 | gap=-0.022 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.175 > 0.08 con n=922 PNL=+611.57€
  - _Datos_: n=922 IC=+0.175 PNL=+611.57€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.150 > 0.08 con n=1092 PNL=+566.00€
  - _Datos_: n=1092 IC=+0.150 PNL=+566.00€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.158 > 0.08 con n=74 PNL=+36.32€
  - _Datos_: n=74 IC=+0.158 PNL=+36.32€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.333 > 0.1 con n=3495 PNL=+1948.89€
  - _Datos_: n=3495 IC=+0.333 PNL=+1948.89€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=923 IC=+0.070 PNL=+93.46€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=923 IC=+0.070 PNL=+93.46€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=99 IC=+0.193 PNL=+70.54€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=99 IC=+0.193 PNL=+70.54€

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
  - _Estado_: n=3772 IC=+0.003 PNL=-11.65€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3772 IC=+0.003 PNL=-11.65€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1844 IC=-0.002 PNL=+109.04€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1844 IC=-0.002 PNL=+109.04€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1167 IC=+0.024 PNL=+56.87€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1167 IC=+0.024 PNL=+56.87€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.156 > 0.1 con n=6168 PNL=+3413.50€
  - _Datos_: n=6168 IC=+0.156 PNL=+3413.50€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=3123 IC=+0.084 PNL=+719.23€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=3123 IC=+0.084 PNL=+719.23€

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
  - _Estado_: n=1198 IC=+0.037 PNL=+103.33€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1198 IC=+0.037 PNL=+103.33€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=155 IC=+0.003 PNL=-0.07€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=155 IC=+0.003 PNL=-0.07€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.272 n=200) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=200 IC=+0.272 PNL=+207.61€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.124 > 0.02 con n=1169 PNL=+493.01€
  - _Datos_: n=1169 IC=+0.124 PNL=+493.01€

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
  - _Estado_: n=38467 IC=+0.074 PNL=+5491.73€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=38467 IC=+0.074 PNL=+5491.73€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.134 < -0.1 con n=691 PNL=+101.11€
  - _Datos_: n=691 IC=-0.134 PNL=+101.11€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=3536 IC=+0.068 PNL=+464.32€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=3536 IC=+0.068 PNL=+464.32€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.106 > 0.1 con n=993 PNL=+256.92€
  - _Datos_: n=993 IC=+0.106 PNL=+256.92€

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
  - _Estado_: n=39591 IC=-0.136 PNL=+2650.21€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=39591 IC=-0.136 PNL=+2650.21€

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
  - _Estado_: n=4072 IC=+0.127 PNL=+2620.42€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=4072 IC=+0.127 PNL=+2620.42€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=9740 IC=+0.059 PNL=+861.24€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=9740 IC=+0.059 PNL=+861.24€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.099 > 0.08 con n=4209 PNL=+2345.84€
  - _Datos_: n=4209 IC=+0.099 PNL=+2345.84€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.219 < -0.1 con n=4274 PNL=-336.87€
  - _Datos_: n=4274 IC=-0.219 PNL=-336.87€

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
  - _Estado_: n=86 IC=+0.045 PNL=+14.24€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=86 IC=+0.045 PNL=+14.24€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.096 n=2110) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2110 IC=+0.096 PNL=+425.47€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.411 n=649) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=649 IC=+0.411 PNL=+936.10€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=16995 IC=+0.182 PNL=-1840.10€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=16995 IC=+0.182 PNL=-1840.10€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.228 > 0.1 con n=266 PNL=+182.35€
  - _Datos_: n=266 IC=+0.228 PNL=+182.35€
