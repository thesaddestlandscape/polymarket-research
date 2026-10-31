# Hipótesis automáticas — 2026-10-31 04:23 UTC
_Generado por shadow_postmortem.py sobre 1129051 resoluciones (PNL=+151307.28€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.224 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.133)

- **PATRÓN** `n_total_lado` > `63.0` → IC=+0.185 (n=312)

  - _Acción_: Kelly boost +0.92€ cuando `n_total_lado` > 63.0 (IC base=+0.133)

- **PATRÓN** `banda_hit_calibrado` > `0.6162` → IC=+0.252 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6162 (IC base=+0.133)

- **PATRÓN** `banda_z` > `8.831` → IC=+0.211 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.831 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.156 (n=338)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=996)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `2306.7816` → IC=+0.138 (n=917)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2306.7816 (IC base=+0.133)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.219 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.137)

- **PATRÓN** `n_total_lado` > `67.0` → IC=+0.192 (n=264)

  - _Acción_: Kelly boost +0.96€ cuando `n_total_lado` > 67.0 (IC base=+0.137)

- **PATRÓN** `banda_hit_calibrado` > `0.6117` → IC=+0.243 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6117 (IC base=+0.137)

- **PATRÓN** `banda_z` > `9.122` → IC=+0.204 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.122 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.163 (n=286)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=896)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `3054.6814` → IC=+0.139 (n=702)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3054.6814 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `9072.653` → IC=+0.121 (n=217)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 9072.653 (IC base=+0.005)

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

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.49 (IC base=+0.161)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.5 (IC base=+0.161)

- **PATRÓN** `n_ballena_banda` > `30.0` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 30.0 (IC base=+0.161)

- **PATRÓN** `n_total_lado` > `43.0` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 43.0 (IC base=+0.161)

- **PATRÓN** `banda_hit_calibrado` > `0.6044` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `banda_hit_calibrado` > 0.6044 (IC base=+0.161)

- **PATRÓN** `banda_z` > `2.518` → IC=+0.244 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 2.518 (IC base=+0.161)

- **PATRÓN** `ballenas_wallet_edge_medio` > `2.641` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `ballenas_wallet_edge_medio` > 2.641 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.235 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.161)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.214 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `2434.9249` → IC=+0.198 (n=41)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2434.9249 (IC base=+0.161)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `137.33` → IC=-0.209 (n=10960)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 137.33
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=32886)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `127.45` → IC=-0.259 (n=1155)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.45
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=3468)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `117.67` → IC=-0.303 (n=1148)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 117.67
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3447)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `159.7` → IC=-0.237 (n=2957)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 159.7
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=8873)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `131.64` → IC=-0.260 (n=2104)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.64
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=6314)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.212 (n=24625)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.120 (n=4714)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `8668.3588` → IC=+0.162 (n=2176)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 8668.3588 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.127 (n=21132)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.131 (n=25721)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.225 (n=19502)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=7772)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6754.6293` → IC=+0.152 (n=3006)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 6754.6293 (IC base=+0.124)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=2142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.364 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.184 (n=2621)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `9438.8389` → IC=+0.183 (n=1824)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 9438.8389 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.187 (n=1867)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.184 (n=2085)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` < `0.295` → IC=+0.312 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.295 (IC base=+0.181)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=2675)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `16148.5591` → IC=+0.185 (n=690)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 16148.5591 (IC base=+0.181)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.172 (n=526)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` > 0.61 (IC base=+0.076)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.142 (n=1257)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.44 (IC base=+0.082)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=4749)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.164 (n=4028)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 15.0 (IC base=+0.162)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.373 (n=1554)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.214 (n=2135)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.349 (n=780)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=2481)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=1203)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.150 (n=1021)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 15.0 (IC base=+0.143)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.261 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.144 (n=1323)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `3079.6088` → IC=+0.134 (n=230)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 3079.6088 (IC base=+0.070)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.254 (n=909)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1267)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.147 (n=1359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=710)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.145)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.286 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=904)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.145)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `py_entrada` > `0.555` → IC=+0.170 (n=431)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.555 (IC base=+0.062)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.132 (n=1295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.244 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.123)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.297 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.226 (n=144)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=21058)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.199 (n=17850)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.229 (n=8709)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.197)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.182 (n=2286)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.177 (n=4800)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 18.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.182 (n=4642)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.176 (n=4004)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.217 (n=2674)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.218 (n=2378)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.215)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.292 (n=905)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.215)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=4739)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.179 (n=4032)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.177 (n=4929)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=3692)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.255 (n=4049)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.247)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.248 (n=3434)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.247)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.358 (n=1368)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.79 (IC base=+0.247)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.247)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=4648)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.190 (n=3960)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.189 (n=3455)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.186)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.429 (n=796)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.428 (n=885)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=896)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=932)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `4387.5246` → IC=+0.442 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4387.5246 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.443 (n=363)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

- **PATRÓN** `libro_liquidez` > `12485.1016` → IC=+0.446 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12485.1016 (IC base=+0.438)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.432 (n=234)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.426)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.431 (n=346)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.433 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `4655.9741` → IC=+0.440 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4655.9741 (IC base=+0.426)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.398 (n=145)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.395)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.402 (n=141)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.395)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.412 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.395)

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

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.210 (n=23653)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.245 (n=27662)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.201)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.192 (n=4094)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 18.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.183 (n=8766)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 12.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.195 (n=12439)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=5727)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.225 (n=5626)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.286 (n=3952)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.194 (n=4063)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 18.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.200 (n=9682)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.229 (n=3856)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=4413)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.272 (n=3885)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.212 (n=3920)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.259 (n=4061)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=4582)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.200 (n=4573)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.246 (n=4771)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=9817)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=10066)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.38` → IC=+0.139 (n=9123)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.38 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=4819)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.118)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.144 (n=4576)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=6034)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.118)

- **PATRÓN** `lag_apertura_s` < `2.64` → IC=+0.144 (n=4521)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 2.64 (IC base=+0.118)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.191 (n=4998)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.115)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=5490)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.115)

- **PATRÓN** `lag_apertura_s` < `3.25` → IC=+0.137 (n=6044)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.25 (IC base=+0.115)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.313 (n=1241)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.295)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.388 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.295)

- **PATRÓN** `libro_liquidez` > `3871.3378` → IC=+0.296 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3871.3378 (IC base=+0.295)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.290 (n=836)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.282)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.364 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `5134.0872` → IC=+0.302 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5134.0872 (IC base=+0.282)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.325 (n=602)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.301)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.304 (n=876)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.301)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.399 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.301)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.301 (n=998)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.301)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` < `16.0` → IC=+0.367 (n=88)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.339)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.389 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.339)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.361 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.339)

- **PATRÓN** `libro_liquidez` > `761.0655` → IC=+0.364 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 761.0655 (IC base=+0.339)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.448 (n=846)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.445)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.445 (n=840)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.445)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.452 (n=815)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.445)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.440 (n=401)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.438)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.439 (n=276)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.440 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.443 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.438)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.471 (n=135)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.452)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.455 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.452)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.457 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.452)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.454 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.452)

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
- **FILTRO** `hora_utc` < `5.0` → IC=-0.292 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=103)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.246 (n=61)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=64)

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
- **FILTRO** `hora_utc` < `5.0` → IC=-0.292 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=103)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.246 (n=61)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=64)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4783` → IC=+0.139 (n=15444)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4783 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.126 (n=15592)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.125 (n=10763)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.375` → IC=+0.165 (n=15444)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.375 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.7851` → IC=+0.280 (n=860)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7851 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.816` → IC=+0.191 (n=5861)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 5.816 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6213` → IC=+0.265 (n=4538)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6213 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.3027` → IC=+0.246 (n=1590)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3027 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.3455` → IC=+0.228 (n=5008)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3455 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=7859)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `4436.6463` → IC=+0.151 (n=5148)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4436.6463 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.121 (n=9613)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0059 (IC base=+0.079)

- **PATRÓN** `ibs_20min` < `0.566` → IC=+0.142 (n=19218)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.566 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` > `0.6084` → IC=+0.188 (n=1289)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.6084 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` < `0.1611` → IC=+0.187 (n=7403)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.1611 (IC base=+0.079)

- **PATRÓN** `volumen_regimen` < `0.6256` → IC=+0.194 (n=2573)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.6256 (IC base=+0.079)

- **PATRÓN** `volumen_pendiente_norm` > `0.2966` → IC=+0.229 (n=1903)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2966 (IC base=+0.079)

- **PATRÓN** `volumen_spike_ratio` > `2.6796` → IC=+0.208 (n=4368)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6796 (IC base=+0.079)

- **PATRÓN** `ballena_activa_n` < `104.0` → IC=+0.223 (n=12986)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 104.0 (IC base=+0.079)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3622` → IC=+0.209 (n=3328)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3622 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.221 (n=1249)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.209 (n=2228)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `0.9839` → IC=+0.280 (n=1509)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9839 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.666` → IC=+0.280 (n=1478)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.666 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.2833` → IC=+0.259 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2833 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `1.4363` → IC=+0.207 (n=3184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4363 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.220 (n=3642)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `2044.3` → IC=+0.207 (n=1109)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2044.3 (IC base=+0.206)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.222 (n=1990)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0095` → IC=+0.243 (n=2877)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0095 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.0889` → IC=+0.276 (n=959)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0889 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.242 (n=2995)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.551` → IC=+0.259 (n=2876)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.551 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` < `0.0956` → IC=+0.241 (n=2598)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0956 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2921` → IC=+0.258 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2921 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.4444` → IC=+0.243 (n=912)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4444 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `2.6901` → IC=+0.243 (n=911)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6901 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.240 (n=3297)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1464.4` → IC=+0.244 (n=2569)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1464.4 (IC base=+0.239)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.237 (n=921)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.3447` → IC=+0.238 (n=2759)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3447 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.239 (n=2882)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.9263` → IC=+0.270 (n=920)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9263 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `0.1888` → IC=+0.233 (n=1293)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1888 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.165` → IC=+0.260 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.165 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` < `1.226` → IC=+0.227 (n=2759)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.226 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `0.6248` → IC=+0.230 (n=2759)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6248 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.272 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.4018` → IC=+0.230 (n=908)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4018 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `2.4279` → IC=+0.255 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4279 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.171 (n=1962)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0042 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.0782` → IC=+0.165 (n=979)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.0782 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.154 (n=1093)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.7169` → IC=+0.169 (n=2936)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.7169 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.1401` → IC=+0.147 (n=2797)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1401 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.885` → IC=+0.138 (n=479)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 10.885 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.045` → IC=+0.136 (n=2680)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 4.045 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `1.204` → IC=+0.136 (n=2937)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.204 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.0967` → IC=+0.152 (n=1069)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.0967 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.5221` → IC=+0.141 (n=1238)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.5221 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.7903` → IC=+0.131 (n=1875)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.7903 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=3807)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `206.0` → IC=+0.171 (n=1208)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 206.0 (IC base=+0.130)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.211 (n=1589)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.198 (n=3671)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.264 (n=1355)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.118` → IC=+0.280 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.118 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.196 (n=3117)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` > `0.3517` → IC=+0.219 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3517 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `1.5896` → IC=+0.197 (n=3406)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.5896 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=4196)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `1922.7184` → IC=+0.202 (n=1586)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1922.7184 (IC base=+0.192)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.221 (n=2806)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0111 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.179` → IC=+0.233 (n=1403)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.179 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=1203)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.220 (n=1457)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.0357` → IC=+0.270 (n=1064)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0357 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.119` → IC=+0.260 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.119 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3492` → IC=+0.259 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3492 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.1455` → IC=+0.223 (n=2033)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1455 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=1624)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `1910.86` → IC=+0.222 (n=1445)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1910.86 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.218 (n=2033)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.149 (n=172)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=4223)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.159 (n=608)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0038 (IC base=+0.058)

- **PATRÓN** `ibs_20min` > `0.9502` → IC=+0.238 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9502 (IC base=+0.058)

- **PATRÓN** `dist_vwap_pct` > `0.14` → IC=+0.334 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.14 (IC base=+0.058)

- **PATRÓN** `dist_vwap_pct` < `0.3359` → IC=+0.327 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3359 (IC base=+0.058)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.226` → IC=+0.197 (n=1307)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 5.226 (IC base=+0.058)

- **PATRÓN** `volumen_regimen` < `0.8653` → IC=+0.326 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8653 (IC base=+0.058)

- **PATRÓN** `volumen_regimen` > `0.6977` → IC=+0.337 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6977 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` < `0.0775` → IC=+0.326 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0775 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` > `0.3033` → IC=+0.335 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3033 (IC base=+0.058)

- **PATRÓN** `volumen_spike_ratio` < `1.4167` → IC=+0.340 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4167 (IC base=+0.058)

- **PATRÓN** `volumen_spike_ratio` > `2.2606` → IC=+0.331 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2606 (IC base=+0.058)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.331 (n=692)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 143.0 (IC base=+0.058)

- **PATRÓN** `ibs_20min` < `0.0911` → IC=+0.184 (n=1099)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.0911 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` > `0.7252` → IC=+0.165 (n=261)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.7252 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` < `0.1377` → IC=+0.143 (n=1894)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1377 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` < `0.833` → IC=+0.157 (n=1358)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.833 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` > `1.1651` → IC=+0.143 (n=679)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.1651 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.2837` → IC=+0.209 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2837 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` < `1.7746` → IC=+0.148 (n=1306)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.7746 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` > `2.1494` → IC=+0.163 (n=888)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.1494 (IC base=+0.046)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.175 (n=124)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=657)

- **FILTRO** `ibs_20min` < `0.2667` → IC=-0.170 (n=195)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2667
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=586)

- **FILTRO** `ibs_20min` > `0.2069` → IC=-0.132 (n=4122)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2069
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=2038)

- **FILTRO** `sigma_ewma_delta_pct` > `8.5` → IC=-0.226 (n=665)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.5
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=5495)

- **PATRÓN** `ibs_20min` > `0.7606` → IC=+0.172 (n=266)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.7606 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `1.672` → IC=+0.281 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.672 (IC base=+0.024)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.844` → IC=+0.167 (n=91)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 8.844 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` > `1.0359` → IC=+0.293 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0359 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` < `0.1586` → IC=+0.281 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1586 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `2.4897` → IC=+0.287 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4897 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` > `1.4528` → IC=+0.263 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4528 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.270 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.024)

- **PATRÓN** `ibs_20min` < `0.2069` → IC=+0.150 (n=2038)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.2069 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` < `0.1985` → IC=+0.276 (n=886)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1985 (IC base=-0.039)

- **PATRÓN** `volumen_regimen` < `0.6963` → IC=+0.309 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6963 (IC base=-0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.0783` → IC=+0.295 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0783 (IC base=-0.039)

- **PATRÓN** `volumen_spike_ratio` < `2.4396` → IC=+0.303 (n=810)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4396 (IC base=-0.039)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.5999` → IC=-0.181 (n=1157)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.5999
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=3473)

- **FILTRO** `ibs_20min` < `0.7664` → IC=-0.153 (n=3055)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7664
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=1575)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.169 (n=1072)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=3558)

- **FILTRO** `ibs_20min` > `0.7458` → IC=-0.196 (n=1641)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7458
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=4924)

- **PATRÓN** `dist_vwap_pct` > `1.0694` → IC=+0.362 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0694 (IC base=-0.063)

- **PATRÓN** `dist_vwap_pct` < `0.1849` → IC=+0.307 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1849 (IC base=-0.063)

- **PATRÓN** `volumen_regimen` > `0.704` → IC=+0.322 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.704 (IC base=-0.063)

- **PATRÓN** `volumen_pendiente_norm` < `0.1022` → IC=+0.308 (n=790)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1022 (IC base=-0.063)

- **PATRÓN** `volumen_spike_ratio` < `1.4239` → IC=+0.321 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4239 (IC base=-0.063)

- **PATRÓN** `volumen_spike_ratio` > `1.8567` → IC=+0.312 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8567 (IC base=-0.063)

- **PATRÓN** `dist_vwap_pct` > `0.8075` → IC=+0.274 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8075 (IC base=-0.001)

- **PATRÓN** `dist_vwap_pct` < `0.2233` → IC=+0.259 (n=1835)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2233 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` < `0.7259` → IC=+0.269 (n=824)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7259 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` > `1.064` → IC=+0.281 (n=848)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.064 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.1045` → IC=+0.276 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1045 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `2.1724` → IC=+0.263 (n=1536)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1724 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `1.4259` → IC=+0.264 (n=1745)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4259 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.206 (n=6720)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.092)

- **PATRÓN** `ibs_20min` > `0.875` → IC=+0.286 (n=9155)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.875 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` > `0.9362` → IC=+0.302 (n=1452)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9362 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.562` → IC=+0.166 (n=9027)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.562 (IC base=+0.092)

- **PATRÓN** `volumen_regimen` < `1.1739` → IC=+0.268 (n=7402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1739 (IC base=+0.092)

- **PATRÓN** `volumen_regimen` > `0.6921` → IC=+0.275 (n=6614)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6921 (IC base=+0.092)

- **PATRÓN** `volumen_pendiente_norm` > `0.2941` → IC=+0.288 (n=1674)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2941 (IC base=+0.092)

- **PATRÓN** `volumen_spike_ratio` > `2.645` → IC=+0.279 (n=3918)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.645 (IC base=+0.092)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.304 (n=11361)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 91.0 (IC base=+0.092)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.156 (n=6496)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0098 (IC base=+0.078)

- **PATRÓN** `ibs_20min` < `0.6468` → IC=+0.148 (n=19478)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.6468 (IC base=+0.078)

- **PATRÓN** `dist_vwap_pct` < `0.2491` → IC=+0.271 (n=6407)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2491 (IC base=+0.078)

- **PATRÓN** `volumen_regimen` < `0.7039` → IC=+0.271 (n=2784)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7039 (IC base=+0.078)

- **PATRÓN** `volumen_regimen` > `1.1948` → IC=+0.268 (n=2109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1948 (IC base=+0.078)

- **PATRÓN** `volumen_pendiente_norm` > `0.2937` → IC=+0.319 (n=1369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2937 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` < `1.5756` → IC=+0.294 (n=4053)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5756 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` > `2.2719` → IC=+0.289 (n=4174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2719 (IC base=+0.078)

- **PATRÓN** `ballena_activa_n` < `75.0` → IC=+0.300 (n=9158)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 75.0 (IC base=+0.078)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.5792` → IC=-0.157 (n=2742)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5792
  - _Potencial_: sin este filtro IC_bueno=+0.205 (n=2742)

- **FILTRO** `ibs_20min` > `0.7228` → IC=-0.221 (n=1189)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7228
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=3568)

- **FILTRO** `sigma_ewma_delta_pct` > `4.259` → IC=-0.224 (n=1026)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.259
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=3731)

- **PATRÓN** `ibs_20min` > `0.9286` → IC=+0.331 (n=1371)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9286 (IC base=+0.024)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.105` → IC=+0.182 (n=1843)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 3.105 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.2287` → IC=+0.320 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2287 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `1.4484` → IC=+0.269 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4484 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` > `2.2584` → IC=+0.290 (n=808)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2584 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.309 (n=1199)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.024)

- **PATRÓN** `ibs_20min` < `0.1691` → IC=+0.158 (n=1190)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.1691 (IC base=-0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.1514` → IC=+0.404 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1514 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.6499` → IC=+0.404 (n=767)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6499 (IC base=-0.026)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.396 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=-0.026)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1694` → IC=+0.222 (n=885)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1694 (IC base=+0.017)

- **PATRÓN** `volumen_regimen` < `1.195` → IC=+0.205 (n=1972)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.195 (IC base=+0.017)

- **PATRÓN** `volumen_regimen` > `0.693` → IC=+0.209 (n=1761)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.693 (IC base=+0.017)

- **PATRÓN** `volumen_pendiente_norm` > `0.277` → IC=+0.251 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.277 (IC base=+0.017)

- **PATRÓN** `volumen_spike_ratio` < `1.4206` → IC=+0.231 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4206 (IC base=+0.017)

- **PATRÓN** `volumen_spike_ratio` > `2.4449` → IC=+0.211 (n=648)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4449 (IC base=+0.017)

- **PATRÓN** `ballena_activa_n` < `267.0` → IC=+0.239 (n=1303)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 267.0 (IC base=+0.017)

- **PATRÓN** `dist_vwap_pct` < `0.1263` → IC=+0.246 (n=1373)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1263 (IC base=-0.002)

- **PATRÓN** `volumen_regimen` < `1.1685` → IC=+0.236 (n=1352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1685 (IC base=-0.002)

- **PATRÓN** `volumen_regimen` > `0.6223` → IC=+0.241 (n=1353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6223 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2707` → IC=+0.303 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2707 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.5333` → IC=+0.244 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5333 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.1537` → IC=+0.253 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1537 (IC base=-0.002)

- **PATRÓN** `ballena_activa_n` < `214.0` → IC=+0.250 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 214.0 (IC base=-0.002)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.321 (n=1303)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.277)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.285 (n=2870)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.277)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.318 (n=1552)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.277)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.681` → IC=+0.309 (n=948)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.681 (IC base=+0.277)

- **PATRÓN** `volumen_pendiente_norm` < `0.0977` → IC=+0.289 (n=2506)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0977 (IC base=+0.277)

- **PATRÓN** `volumen_spike_ratio` > `1.6075` → IC=+0.282 (n=2781)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6075 (IC base=+0.277)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.286 (n=3416)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `2024.7794` → IC=+0.290 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2024.7794 (IC base=+0.277)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.299 (n=1728)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.277)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.334 (n=1159)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0105 (IC base=+0.297)

- **PATRÓN** `drift_60min` |x|≤ `0.1799` → IC=+0.315 (n=1123)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1799 (IC base=+0.297)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.324 (n=975)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.300 (n=884)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.297)

- **PATRÓN** `ibs_20min` < `0.0073` → IC=+0.301 (n=1123)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0073 (IC base=+0.297)

- **PATRÓN** `ibs_20min` > `0.1333` → IC=+0.305 (n=1703)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1333 (IC base=+0.297)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.337` → IC=+0.309 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.337 (IC base=+0.297)

- **PATRÓN** `volumen_pendiente_norm` < `0.1976` → IC=+0.297 (n=2511)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1976 (IC base=+0.297)

- **PATRÓN** `volumen_pendiente_norm` > `0.3433` → IC=+0.306 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3433 (IC base=+0.297)

- **PATRÓN** `volumen_spike_ratio` < `1.5862` → IC=+0.300 (n=818)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5862 (IC base=+0.297)

- **PATRÓN** `volumen_spike_ratio` > `2.712` → IC=+0.309 (n=1112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.712 (IC base=+0.297)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.300 (n=1306)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.297)

- **PATRÓN** `libro_liquidez` > `1912.48` → IC=+0.303 (n=1158)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1912.48 (IC base=+0.297)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.303 (n=1670)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.297)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7325` → IC=-0.181 (n=1244)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7325
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=3747)

- **PATRÓN** `ibs_20min` > `0.864` → IC=+0.165 (n=1211)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.864 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.1514` → IC=+0.234 (n=912)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1514 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.3626` → IC=+0.233 (n=1686)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3626 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `1.0072` → IC=+0.239 (n=1517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0072 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `0.669` → IC=+0.232 (n=1539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.669 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.1016` → IC=+0.240 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1016 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.4521` → IC=+0.238 (n=1667)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4521 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `118.0` → IC=+0.253 (n=1699)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 118.0 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.1468` → IC=+0.238 (n=1188)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1468 (IC base=+0.004)

- **PATRÓN** `volumen_regimen` < `1.1942` → IC=+0.243 (n=1223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1942 (IC base=+0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.297 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.783` → IC=+0.276 (n=779)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.783 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.4173` → IC=+0.260 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4173 (IC base=+0.004)

- **PATRÓN** `ballena_activa_n` < `121.0` → IC=+0.264 (n=1191)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 121.0 (IC base=+0.004)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.75` → IC=-0.235 (n=2088)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.312 (n=2100)

- **FILTRO** `ibs_20min` > `0.6333` → IC=-0.232 (n=1010)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6333
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=3044)

- **FILTRO** `sigma_ewma_delta_pct` > `8.389` → IC=-0.253 (n=464)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.389
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=3590)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.312 (n=2100)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.75 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` > `0.2124` → IC=+0.345 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2124 (IC base=+0.039)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.309` → IC=+0.194 (n=655)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 9.309 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` < `0.8471` → IC=+0.340 (n=1028)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8471 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` > `0.7014` → IC=+0.335 (n=1377)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7014 (IC base=+0.039)

- **PATRÓN** `volumen_pendiente_norm` < `0.159` → IC=+0.334 (n=1597)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.159 (IC base=+0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.353 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` < `1.4339` → IC=+0.361 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4339 (IC base=+0.039)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.353 (n=1321)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.039)

- **PATRÓN** `ibs_20min` < `0.6333` → IC=+0.134 (n=3044)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.6333 (IC base=+0.043)

- **PATRÓN** `dist_vwap_pct` < `0.2096` → IC=+0.252 (n=1389)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2096 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` < `0.6968` → IC=+0.279 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6968 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.0706` → IC=+0.267 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0706 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `2.4505` → IC=+0.258 (n=1393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4505 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.271 (n=1410)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.043)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.355 (n=1936)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.311)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.312 (n=2189)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.311)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.313 (n=2275)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.311)

- **PATRÓN** `ibs_20min` > `0.7628` → IC=+0.347 (n=1936)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7628 (IC base=+0.311)

- **PATRÓN** `dist_vwap_pct` > `0.2079` → IC=+0.335 (n=1206)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2079 (IC base=+0.311)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.824` → IC=+0.328 (n=1053)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.824 (IC base=+0.311)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.098` → IC=+0.311 (n=2468)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.098 (IC base=+0.311)

- **PATRÓN** `volumen_regimen` > `0.8703` → IC=+0.329 (n=1445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8703 (IC base=+0.311)

- **PATRÓN** `volumen_pendiente_norm` > `0.2797` → IC=+0.347 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2797 (IC base=+0.311)

- **PATRÓN** `volumen_spike_ratio` > `1.4265` → IC=+0.323 (n=2082)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4265 (IC base=+0.311)

- **PATRÓN** `libro_liquidez` > `2569.1156` → IC=+0.311 (n=1445)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2569.1156 (IC base=+0.311)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.342 (n=1898)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.311)

- **PATRÓN** `sigma_h` > `0.0153` → IC=+0.343 (n=1539)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0153 (IC base=+0.312)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.320 (n=1160)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.312)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.314 (n=1130)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.312)

- **PATRÓN** `ibs_20min` < `0.3784` → IC=+0.333 (n=2308)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3784 (IC base=+0.312)

- **PATRÓN** `dist_vwap_pct` < `0.232` → IC=+0.317 (n=2217)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.232 (IC base=+0.312)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.619` → IC=+0.328 (n=856)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.619 (IC base=+0.312)

- **PATRÓN** `volumen_regimen` < `0.7226` → IC=+0.319 (n=1016)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7226 (IC base=+0.312)

- **PATRÓN** `volumen_regimen` > `1.212` → IC=+0.341 (n=770)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.212 (IC base=+0.312)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.364 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.312)

- **PATRÓN** `volumen_spike_ratio` < `1.4108` → IC=+0.324 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4108 (IC base=+0.312)

- **PATRÓN** `volumen_spike_ratio` > `2.1339` → IC=+0.314 (n=965)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1339 (IC base=+0.312)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.226 (n=4997)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.1232` → IC=+0.196 (n=6597)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1232 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=15540)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `0.5459` → IC=+0.233 (n=14989)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5459 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.1641` → IC=+0.206 (n=5911)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1641 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.23` → IC=+0.255 (n=3909)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.23 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `1.1852` → IC=+0.160 (n=9973)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1852 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` > `0.6239` → IC=+0.159 (n=9973)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.6239 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.293` → IC=+0.208 (n=2176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.293 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `2.5988` → IC=+0.189 (n=4857)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.5988 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.196 (n=13906)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 90.0 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0115` → IC=+0.185 (n=14595)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0115 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.0808` → IC=+0.224 (n=4865)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0808 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=5477)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.5167` → IC=+0.238 (n=14594)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5167 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` < `0.1787` → IC=+0.177 (n=10472)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.1787 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.8` → IC=+0.197 (n=2342)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 9.8 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.606` → IC=+0.185 (n=12952)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 2.606 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.1819` → IC=+0.164 (n=10400)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1819 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2952` → IC=+0.223 (n=2169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2952 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.639` → IC=+0.189 (n=4603)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.639 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `95.0` → IC=+0.195 (n=13550)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 95.0 (IC base=+0.181)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.224 (n=829)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.1044` → IC=+0.259 (n=1092)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1044 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.238 (n=925)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.228 (n=1674)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.9371` → IC=+0.297 (n=1654)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9371 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.749` → IC=+0.329 (n=794)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.749 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.289 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `1.8388` → IC=+0.221 (n=1573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8388 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `1.4355` → IC=+0.224 (n=2359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4355 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=2739)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.255 (n=1985)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0091 (IC base=+0.252)

- **PATRÓN** `drift_60min` |x|≤ `0.0971` → IC=+0.305 (n=872)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0971 (IC base=+0.252)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=2049)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.252)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.255 (n=1813)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.252)

- **PATRÓN** `ibs_20min` < `0.4214` → IC=+0.270 (n=1981)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4214 (IC base=+0.252)

- **PATRÓN** `volumen_pendiente_norm` < `0.1008` → IC=+0.257 (n=1740)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1008 (IC base=+0.252)

- **PATRÓN** `volumen_pendiente_norm` > `0.3017` → IC=+0.279 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3017 (IC base=+0.252)

- **PATRÓN** `volumen_spike_ratio` < `1.4432` → IC=+0.274 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4432 (IC base=+0.252)

- **PATRÓN** `volumen_spike_ratio` > `2.7181` → IC=+0.256 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7181 (IC base=+0.252)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.254 (n=2274)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.252)

- **PATRÓN** `libro_liquidez` > `1458.1` → IC=+0.259 (n=1770)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1458.1 (IC base=+0.252)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.253 (n=909)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.252)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.204 (n=762)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.1615` → IC=+0.172 (n=1521)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1615 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.159 (n=2385)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` > `0.2897` → IC=+0.212 (n=2277)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2897 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.1364` → IC=+0.209 (n=1299)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1364 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.074` → IC=+0.208 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.074 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `0.6938` → IC=+0.153 (n=1003)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6938 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `1.0611` → IC=+0.144 (n=1033)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.0611 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.2815` → IC=+0.188 (n=350)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2815 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `1.5049` → IC=+0.157 (n=984)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.5049 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `2.4691` → IC=+0.155 (n=745)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.4691 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `409.0` → IC=+0.147 (n=2200)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 409.0 (IC base=+0.142)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.175 (n=2411)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0061 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.2402` → IC=+0.173 (n=2119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2402 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.184 (n=1153)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.6154` → IC=+0.208 (n=2408)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6154 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.21` → IC=+0.183 (n=453)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 11.21 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.132` → IC=+0.152 (n=2098)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.132 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.2014` → IC=+0.161 (n=2408)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2014 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` < `0.0702` → IC=+0.152 (n=1987)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.0702 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.4801` → IC=+0.151 (n=2285)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4801 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `216.0` → IC=+0.189 (n=980)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 216.0 (IC base=+0.148)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.240 (n=1150)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.4045` → IC=+0.225 (n=2232)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4045 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.235 (n=930)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=1336)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.299` → IC=+0.307 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.299 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.213 (n=2197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.3519` → IC=+0.238 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3519 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.7589` → IC=+0.213 (n=1087)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7589 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.703` → IC=+0.225 (n=1119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.703 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.217 (n=3039)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `1915.5084` → IC=+0.225 (n=1150)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1915.5084 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0119` → IC=+0.240 (n=2211)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0119 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.2464` → IC=+0.266 (n=1474)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2464 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.280 (n=840)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.0278` → IC=+0.289 (n=974)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0278 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.234` → IC=+0.282 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.234 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.359` → IC=+0.288 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.359 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` < `1.7612` → IC=+0.234 (n=935)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7612 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.1719` → IC=+0.243 (n=1416)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1719 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.238 (n=1151)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `1904.0224` → IC=+0.245 (n=1002)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1904.0224 (IC base=+0.235)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.240 (n=1423)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.235)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.199 (n=1080)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0041 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0789` → IC=+0.198 (n=818)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.0789 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=2539)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.2786` → IC=+0.201 (n=2451)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2786 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.1434` → IC=+0.189 (n=1458)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1434 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.572` → IC=+0.191 (n=425)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 11.572 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.0194` → IC=+0.145 (n=2157)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.0194 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.1015` → IC=+0.168 (n=992)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.1015 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.8246` → IC=+0.141 (n=1602)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.8246 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.5111` → IC=+0.159 (n=801)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.5111 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `6882.1647` → IC=+0.198 (n=1112)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 6882.1647 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `133.0` → IC=+0.144 (n=2399)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 133.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.165 (n=2290)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0065 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.398` → IC=+0.145 (n=2600)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.398 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.163 (n=1238)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 15.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.6789` → IC=+0.186 (n=2600)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6789 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.1594` → IC=+0.156 (n=2607)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1594 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.432` → IC=+0.149 (n=628)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 9.432 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.8509` → IC=+0.155 (n=1735)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8509 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2969` → IC=+0.191 (n=393)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2969 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.8043` → IC=+0.132 (n=1636)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.8043 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `1.4214` → IC=+0.129 (n=2454)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.4214 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `6178.8421` → IC=+0.181 (n=1179)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 6178.8421 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `111.0` → IC=+0.133 (n=2141)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 111.0 (IC base=+0.128)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.171 (n=1242)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0109 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=2802)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.4783` → IC=+0.212 (n=2739)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4783 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.1947` → IC=+0.190 (n=1545)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1947 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.286` → IC=+0.291 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.286 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `1.1741` → IC=+0.134 (n=2740)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.1741 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.7056` → IC=+0.126 (n=2447)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.7056 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` < `0.1632` → IC=+0.131 (n=2798)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.1632 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.5435` → IC=+0.143 (n=1171)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.5435 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.126 (n=2859)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2634.7685` → IC=+0.199 (n=1242)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2634.7685 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.145 (n=1138)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 21.0 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0115` → IC=+0.144 (n=2829)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0115 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1102` → IC=+0.170 (n=943)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1102 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=2883)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.6316` → IC=+0.220 (n=2831)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6316 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.1993` → IC=+0.149 (n=2714)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1993 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.384` → IC=+0.138 (n=2497)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 2.384 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.1824` → IC=+0.129 (n=2829)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.1824 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1636` → IC=+0.124 (n=2761)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1636 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2758` → IC=+0.136 (n=388)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.2758 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.5398` → IC=+0.127 (n=1169)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.5398 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `1.7985` → IC=+0.126 (n=1771)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.7985 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2510.4678` → IC=+0.181 (n=1283)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2510.4678 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.127 (n=2643)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 47.0 (IC base=+0.120)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.247 (n=2238)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.169` → IC=+0.237 (n=1103)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.169 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.226 (n=2601)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2250)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.661` → IC=+0.256 (n=2505)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.661 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` > `0.1826` → IC=+0.232 (n=1592)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1826 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` < `0.8399` → IC=+0.224 (n=2580)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8399 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.606` → IC=+0.253 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.606 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `1.1694` → IC=+0.224 (n=2506)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1694 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `0.6942` → IC=+0.232 (n=2238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6942 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.2843` → IC=+0.268 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2843 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `1.5258` → IC=+0.226 (n=1075)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5258 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `1.8029` → IC=+0.232 (n=1628)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8029 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `2082.5016` → IC=+0.226 (n=2505)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2082.5016 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0128` → IC=+0.239 (n=1129)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0128 (IC base=+0.235)

- **PATRÓN** `sigma_h` > `0.0228` → IC=+0.246 (n=1163)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0228 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.5795` → IC=+0.243 (n=2565)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5795 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.250 (n=1250)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.240 (n=1150)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.4375` → IC=+0.262 (n=2566)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4375 (IC base=+0.235)

- **PATRÓN** `dist_vwap_pct` > `0.3055` → IC=+0.242 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3055 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.3` → IC=+0.274 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.3 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` < `0.8679` → IC=+0.236 (n=1710)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8679 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` > `1.0401` → IC=+0.241 (n=1163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0401 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2803` → IC=+0.285 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2803 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` < `2.5137` → IC=+0.232 (n=2404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5137 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.235 (n=2403)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=+0.235)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.206 (n=1659)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.1322` → IC=+0.197 (n=1653)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.1322 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.192 (n=3357)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 8.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.4648` → IC=+0.216 (n=3356)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4648 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.8093` → IC=+0.195 (n=575)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.8093 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.599` → IC=+0.204 (n=1617)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.599 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `0.8609` → IC=+0.190 (n=2258)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.8609 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.0739` → IC=+0.182 (n=1514)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.0739 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `1.4277` → IC=+0.184 (n=1219)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.4277 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.4786` → IC=+0.175 (n=1219)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.4786 (IC base=+0.173)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.178 (n=4222)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.02 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `8471.0872` → IC=+0.189 (n=1703)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 8471.0872 (IC base=+0.173)

- **PATRÓN** `ibs_20min` < `0.3902` → IC=+0.157 (n=2722)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.3902 (IC base=+0.081)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.124 (n=1731)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 26.0 (IC base=+0.081)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.198 (n=1013)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0056 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.0998` → IC=+0.240 (n=445)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0998 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.220 (n=918)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` > `0.6361` → IC=+0.248 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6361 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` > `0.3087` → IC=+0.216 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3087 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.046` → IC=+0.208 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.046 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.627` → IC=+0.187 (n=1069)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 6.627 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `0.8791` → IC=+0.206 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8791 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` < `0.1532` → IC=+0.190 (n=1063)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.1532 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.0712` → IC=+0.194 (n=406)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0712 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` < `2.1853` → IC=+0.201 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1853 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `10307.1442` → IC=+0.191 (n=1011)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 10307.1442 (IC base=+0.187)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.197 (n=437)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 162.0 (IC base=+0.187)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.162 (n=551)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0033 (IC base=+0.084)

- **PATRÓN** `ibs_20min` < `0.6399` → IC=+0.137 (n=1096)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.6399 (IC base=+0.084)

- **PATRÓN** `ballena_activa_n` < `165.0` → IC=+0.164 (n=537)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 165.0 (IC base=+0.084)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.245 (n=524)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.2132` → IC=+0.203 (n=789)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2132 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=1232)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` > `0.6455` → IC=+0.252 (n=788)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6455 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` > `0.7873` → IC=+0.197 (n=186)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.7873 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` < `0.2061` → IC=+0.188 (n=1066)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.2061 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.882` → IC=+0.215 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.882 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` < `1.0194` → IC=+0.196 (n=1042)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 1.0194 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.1588` → IC=+0.210 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1588 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` < `1.4253` → IC=+0.194 (n=390)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4253 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `1.7846` → IC=+0.195 (n=778)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.7846 (IC base=+0.186)

- **PATRÓN** `ibs_20min` < `0.1012` → IC=+0.181 (n=387)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.1012 (IC base=+0.076)

- **PATRÓN** `libro_liquidez` > `8196.9139` → IC=+0.140 (n=526)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 8196.9139 (IC base=+0.076)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.151 (n=414)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0069 (IC base=+0.151)

- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.160 (n=313)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0114 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.184 (n=842)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 8.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.204 (n=947)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.9831` → IC=+0.216 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9831 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.081` → IC=+0.242 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.081 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.884` → IC=+0.164 (n=626)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.884 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` > `0.7057` → IC=+0.161 (n=839)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.7057 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2298` → IC=+0.176 (n=174)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2298 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.4313` → IC=+0.178 (n=302)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.4313 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `2.1481` → IC=+0.154 (n=411)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.1481 (IC base=+0.151)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.160 (n=980)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.02 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `2758.0268` → IC=+0.182 (n=426)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2758.0268 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.575` → IC=+0.131 (n=919)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.575 (IC base=+0.046)

- **PATRÓN** `libro_liquidez` > `2589.7365` → IC=+0.143 (n=474)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2589.7365 (IC base=+0.046)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0261` → IC=+0.167 (n=256)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0261 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.2792` → IC=+0.171 (n=171)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.2792 (IC base=+0.158)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.215 (n=121)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `0.7368` → IC=+0.186 (n=170)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.7368 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.6353` → IC=+0.173 (n=96)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.6353 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` < `1.2261` → IC=+0.160 (n=286)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 1.2261 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.394` → IC=+0.178 (n=225)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 3.394 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `1.0007` → IC=+0.161 (n=225)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.0007 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` > `0.6893` → IC=+0.170 (n=228)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 0.6893 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.1036` → IC=+0.171 (n=83)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1036 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `1.806` → IC=+0.190 (n=153)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.806 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `2.3726` → IC=+0.167 (n=76)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.3726 (IC base=+0.158)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.182 (n=303)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.03 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `2591.9144` → IC=+0.178 (n=116)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 2591.9144 (IC base=+0.158)

- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.165 (n=261)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0131 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.146 (n=261)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.3393` → IC=+0.148 (n=194)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.3393 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `1.2291` → IC=+0.288 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2291 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.338` → IC=+0.179 (n=79)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 5.338 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.701` → IC=+0.162 (n=128)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.701 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` < `0.1134` → IC=+0.139 (n=267)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` < 0.1134 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2833` → IC=+0.138 (n=45)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.2833 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.5247` → IC=+0.192 (n=92)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.5247 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `2.7332` → IC=+0.138 (n=92)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.7332 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `2027.646` → IC=+0.130 (n=260)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2027.646 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.150 (n=272)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 19.0 (IC base=+0.130)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.229 (n=6521)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=20373)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.4385` → IC=+0.229 (n=19560)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4385 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.8845` → IC=+0.212 (n=2362)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8845 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.126` → IC=+0.254 (n=4791)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.126 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.2172` → IC=+0.163 (n=13151)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2172 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2407` → IC=+0.207 (n=3536)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2407 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6119` → IC=+0.192 (n=6357)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6119 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `107.0` → IC=+0.202 (n=18200)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 107.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.193 (n=15792)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0101 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.012` → IC=+0.194 (n=5983)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.012 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.4869` → IC=+0.193 (n=17934)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.4869 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=6673)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` < `0.59` → IC=+0.242 (n=17934)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.59 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` < `0.1783` → IC=+0.172 (n=11157)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1783 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.649` → IC=+0.205 (n=2449)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.649 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.475` → IC=+0.194 (n=17418)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 3.475 (IC base=+0.190)

- **PATRÓN** `volumen_regimen` < `1.0571` → IC=+0.165 (n=10633)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.0571 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.2916` → IC=+0.252 (n=2441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2916 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.6295` → IC=+0.201 (n=5696)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6295 (IC base=+0.190)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.221 (n=11358)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.190)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3604` → IC=+0.232 (n=3157)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3604 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.245 (n=1534)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.231)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.233 (n=2123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` > `0.8591` → IC=+0.299 (n=2108)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8591 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.756` → IC=+0.338 (n=1019)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.756 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.2321` → IC=+0.294 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2321 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` < `1.4439` → IC=+0.232 (n=1015)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4439 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` > `2.2767` → IC=+0.238 (n=1381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2767 (IC base=+0.231)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.248 (n=3441)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.231)

- **PATRÓN** `libro_liquidez` > `2043.02` → IC=+0.233 (n=1053)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2043.02 (IC base=+0.231)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.252 (n=1932)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.231)

- **PATRÓN** `sigma_h` < `0.0095` → IC=+0.269 (n=2764)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0095 (IC base=+0.265)

- **PATRÓN** `drift_60min` |x|≤ `0.088` → IC=+0.296 (n=922)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.088 (IC base=+0.265)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.270 (n=2541)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.265)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.267 (n=2510)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.265)

- **PATRÓN** `ibs_20min` < `0.5314` → IC=+0.286 (n=2764)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5314 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` < `0.097` → IC=+0.266 (n=2504)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.097 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` > `0.2895` → IC=+0.291 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2895 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` < `1.5615` → IC=+0.266 (n=1160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5615 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` > `2.6658` → IC=+0.275 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6658 (IC base=+0.265)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.266 (n=3173)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.265)

- **PATRÓN** `libro_liquidez` > `1467.11` → IC=+0.270 (n=2469)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1467.11 (IC base=+0.265)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.272 (n=942)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.265)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.188 (n=1067)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.003 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.0787` → IC=+0.156 (n=1062)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0787 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.154 (n=3311)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.2201` → IC=+0.195 (n=3183)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.2201 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.3229` → IC=+0.198 (n=1079)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.3229 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.52` → IC=+0.158 (n=668)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 9.52 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.6329` → IC=+0.167 (n=1062)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.6329 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `1.0726` → IC=+0.146 (n=1443)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.0726 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.2726` → IC=+0.185 (n=455)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2726 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.1554` → IC=+0.150 (n=2745)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.1554 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.5231` → IC=+0.146 (n=2787)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.5231 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `256.0` → IC=+0.171 (n=1355)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 256.0 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.162 (n=2741)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.006 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0796` → IC=+0.182 (n=914)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.0796 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=1003)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.6865` → IC=+0.189 (n=2740)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6865 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.1427` → IC=+0.156 (n=2621)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1427 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.987` → IC=+0.148 (n=452)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 10.987 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.0502` → IC=+0.153 (n=2411)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.0502 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2184` → IC=+0.199 (n=509)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2184 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.4126` → IC=+0.144 (n=878)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4126 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.7756` → IC=+0.146 (n=1756)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.7756 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=3556)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `234.0` → IC=+0.158 (n=857)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 234.0 (IC base=+0.139)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.253 (n=1085)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=3406)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=2912)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=1216)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.194` → IC=+0.326 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.194 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` < `0.0955` → IC=+0.227 (n=2892)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0955 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `1.6125` → IC=+0.229 (n=3172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6125 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.232 (n=3894)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `1331.2962` → IC=+0.230 (n=3254)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1331.2962 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.244 (n=2722)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.1802` → IC=+0.259 (n=1360)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1802 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.264 (n=1169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.241 (n=1416)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.049` → IC=+0.305 (n=1031)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.049 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.337` → IC=+0.300 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.337 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.3488` → IC=+0.306 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3488 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.1533` → IC=+0.253 (n=1974)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1533 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.248 (n=1589)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1908.1032` → IC=+0.252 (n=1401)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1908.1032 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.247 (n=1978)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.241)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.191 (n=1492)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0041 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.131` → IC=+0.164 (n=1487)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.131 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=3508)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.9047` → IC=+0.276 (n=1127)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9047 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.1424` → IC=+0.165 (n=1758)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1424 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.027` → IC=+0.155 (n=1512)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.027 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.8592` → IC=+0.156 (n=2255)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8592 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.2331` → IC=+0.187 (n=598)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2331 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.5199` → IC=+0.157 (n=1454)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.5199 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `2.1776` → IC=+0.145 (n=1496)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.1776 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `7336.8828` → IC=+0.238 (n=1127)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7336.8828 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.151 (n=1431)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 69.0 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.156 (n=2828)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0076 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4447` → IC=+0.147 (n=2827)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.4447 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.162 (n=1034)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.7205` → IC=+0.190 (n=2827)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.7205 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1512` → IC=+0.148 (n=2610)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1512 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.029` → IC=+0.171 (n=424)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 11.029 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6909` → IC=+0.153 (n=1244)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6909 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.221 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.2105` → IC=+0.139 (n=2400)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.2105 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.5338` → IC=+0.146 (n=2437)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.5338 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `6171.4117` → IC=+0.203 (n=942)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6171.4117 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `95.0` → IC=+0.143 (n=1835)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 95.0 (IC base=+0.136)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.154 (n=1551)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0109 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.152 (n=2410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 11.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `0.4342` → IC=+0.193 (n=3412)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.4342 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `1.0151` → IC=+0.209 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0151 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.484` → IC=+0.269 (n=859)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.484 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.8787` → IC=+0.135 (n=2276)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8787 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1006` → IC=+0.124 (n=3241)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1006 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `2.4875` → IC=+0.122 (n=3335)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.4875 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.123 (n=3560)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2688.8375` → IC=+0.244 (n=1138)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2688.8375 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.128 (n=1096)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 21.0 (IC base=+0.120)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.154 (n=2851)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0105 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1359` → IC=+0.155 (n=1080)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1359 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.153 (n=1520)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 15.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.210 (n=3260)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6667 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.2123` → IC=+0.138 (n=2871)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.2123 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.168` → IC=+0.143 (n=3114)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 3.168 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.6401` → IC=+0.149 (n=1080)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.6401 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2253` → IC=+0.168 (n=567)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2253 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4343` → IC=+0.151 (n=1019)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4343 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2559.8802` → IC=+0.197 (n=1079)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2559.8802 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.135 (n=2706)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 44.0 (IC base=+0.120)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0139` → IC=+0.257 (n=2839)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0139 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.239 (n=3316)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.238 (n=2846)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` > `0.9971` → IC=+0.314 (n=1059)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9971 (IC base=+0.234)

- **PATRÓN** `dist_vwap_pct` > `0.1931` → IC=+0.251 (n=1692)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1931 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.328` → IC=+0.285 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.328 (IC base=+0.234)

- **PATRÓN** `volumen_regimen` < `1.2206` → IC=+0.238 (n=3176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2206 (IC base=+0.234)

- **PATRÓN** `volumen_regimen` > `0.6424` → IC=+0.239 (n=3176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6424 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2359` → IC=+0.254 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2359 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `1.5411` → IC=+0.241 (n=2768)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5411 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=4128)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2077.2844` → IC=+0.235 (n=3176)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2077.2844 (IC base=+0.234)

- **PATRÓN** `sigma_h` > `0.0258` → IC=+0.259 (n=1093)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0258 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.241 (n=3089)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.52` → IC=+0.269 (n=3285)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.52 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` < `0.2983` → IC=+0.242 (n=3202)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2983 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.223` → IC=+0.277 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.223 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` > `1.2152` → IC=+0.259 (n=1093)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2152 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2845` → IC=+0.296 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2845 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.8098` → IC=+0.235 (n=2050)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8098 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `1.4259` → IC=+0.237 (n=3074)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4259 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.235 (n=3005)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.237)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.199 (n=5606)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.246 (n=1920)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.5025` → IC=+0.225 (n=5752)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5025 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.231 (n=2091)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.9346` → IC=+0.254 (n=1918)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9346 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` < `0.4253` → IC=+0.220 (n=4172)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4253 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.856` → IC=+0.222 (n=945)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.856 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.575` → IC=+0.217 (n=5118)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.575 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` < `0.7067` → IC=+0.226 (n=1869)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7067 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `0.8828` → IC=+0.218 (n=2831)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8828 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` < `0.1055` → IC=+0.218 (n=5369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1055 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.1654` → IC=+0.222 (n=1624)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1654 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `1.4515` → IC=+0.224 (n=1888)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4515 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.223 (n=4501)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `3710.5594` → IC=+0.225 (n=3835)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3710.5594 (IC base=+0.216)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.238 (n=1414)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.4923` → IC=+0.212 (n=4216)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4923 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=1429)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.211 (n=1873)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` < `0.7304` → IC=+0.205 (n=4216)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7304 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` > `0.6524` → IC=+0.209 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6524 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` < `0.238` → IC=+0.194 (n=3895)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.238 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.803` → IC=+0.208 (n=3773)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.803 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `1.0969` → IC=+0.203 (n=3532)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0969 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.199 (n=3880)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.0737` → IC=+0.201 (n=1885)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0737 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `1.5338` → IC=+0.203 (n=1831)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5338 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `2.1885` → IC=+0.206 (n=1884)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1885 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.199 (n=5606)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `ballena_activa_n` < `171.0` → IC=+0.207 (n=3645)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 171.0 (IC base=+0.197)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.273 (n=792)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.264)

- **PATRÓN** `drift_60min` |x|≤ `0.1129` → IC=+0.289 (n=396)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1129 (IC base=+0.264)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.271 (n=951)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.264)

- **PATRÓN** `ibs_20min` < `0.2427` → IC=+0.287 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2427 (IC base=+0.264)

- **PATRÓN** `dist_vwap_pct` < `0.1966` → IC=+0.278 (n=834)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1966 (IC base=+0.264)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.122` → IC=+0.286 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.122 (IC base=+0.264)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.694` → IC=+0.266 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.694 (IC base=+0.264)

- **PATRÓN** `volumen_regimen` < `1.2234` → IC=+0.267 (n=899)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2234 (IC base=+0.264)

- **PATRÓN** `volumen_regimen` > `0.868` → IC=+0.284 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.868 (IC base=+0.264)

- **PATRÓN** `volumen_pendiente_norm` > `0.2866` → IC=+0.343 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2866 (IC base=+0.264)

- **PATRÓN** `volumen_spike_ratio` < `2.4907` → IC=+0.269 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4907 (IC base=+0.264)

- **PATRÓN** `volumen_spike_ratio` > `2.189` → IC=+0.267 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.189 (IC base=+0.264)

- **PATRÓN** `libro_liquidez` > `12817.5218` → IC=+0.274 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12817.5218 (IC base=+0.264)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.261 (n=499)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.3833` → IC=+0.194 (n=1489)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.3833 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.218 (n=545)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.189 (n=554)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` < `0.1373` → IC=+0.201 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1373 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.6887` → IC=+0.199 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6887 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.329` → IC=+0.203 (n=1461)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.329 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.0921` → IC=+0.192 (n=1311)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 1.0921 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.0681` → IC=+0.196 (n=689)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.0681 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `1.4122` → IC=+0.200 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4122 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `1.8038` → IC=+0.184 (n=988)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.8038 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `14608.6008` → IC=+0.187 (n=675)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 14608.6008 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `685.0` → IC=+0.192 (n=1444)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 685.0 (IC base=+0.180)

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
- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.219 (n=1588)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.4532` → IC=+0.214 (n=1588)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4532 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.224 (n=564)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` < `0.4996` → IC=+0.221 (n=1059)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4996 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.4016` → IC=+0.216 (n=1592)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4016 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.026` → IC=+0.215 (n=1443)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.026 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `0.7067` → IC=+0.210 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7067 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `1.2214` → IC=+0.210 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2214 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` < `0.1034` → IC=+0.209 (n=1464)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1034 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `2.1434` → IC=+0.216 (n=1369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1434 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=1649)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.240 (n=436)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.194)

- **PATRÓN** `drift_60min` |x|≤ `0.4865` → IC=+0.215 (n=1306)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4865 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.207 (n=500)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.208 (n=877)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` < `0.3986` → IC=+0.199 (n=871)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.3986 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `0.0884` → IC=+0.198 (n=1306)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.0884 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` > `0.6317` → IC=+0.210 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6317 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.387` → IC=+0.197 (n=1187)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 4.387 (IC base=+0.194)

- **PATRÓN** `volumen_regimen` < `0.6394` → IC=+0.224 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6394 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.0738` → IC=+0.223 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0738 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` < `2.1949` → IC=+0.200 (n=1126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1949 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `1.7867` → IC=+0.195 (n=853)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.7867 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `6470.4651` → IC=+0.199 (n=1167)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 6470.4651 (IC base=+0.194)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.227 (n=291)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.226 (n=593)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.272 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` > `0.7276` → IC=+0.238 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7276 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.261` → IC=+0.218 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.261 (IC base=+0.191)

- **PATRÓN** `volumen_regimen` < `0.6342` → IC=+0.237 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6342 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` < `0.1062` → IC=+0.203 (n=782)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1062 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.0801` → IC=+0.194 (n=390)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0801 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` < `2.1715` → IC=+0.197 (n=746)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.1715 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `2.4746` → IC=+0.205 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4746 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.199 (n=1028)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `4251.7342` → IC=+0.237 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4251.7342 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.0128` → IC=+0.216 (n=643)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0128 (IC base=+0.216)

- **PATRÓN** `sigma_h` > `0.0116` → IC=+0.218 (n=292)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0116 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.5971` → IC=+0.238 (n=643)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5971 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.245 (n=449)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` < `0.7347` → IC=+0.241 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7347 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `0.512` → IC=+0.226 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.512 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` < `0.3028` → IC=+0.217 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3028 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.91` → IC=+0.218 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.91 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.825` → IC=+0.225 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.825 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `0.7477` → IC=+0.217 (n=575)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7477 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` < `0.106` → IC=+0.231 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.106 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `2.1932` → IC=+0.255 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1932 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `2965.6586` → IC=+0.233 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2965.6586 (IC base=+0.216)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.243 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.216)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.152 (n=654)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0036 (IC base=+0.061)

- **PATRÓN** `ibs_20min` > `0.7579` → IC=+0.196 (n=1245)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.7579 (IC base=+0.061)

- **PATRÓN** `dist_vwap_pct` > `0.1482` → IC=+0.141 (n=954)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1482 (IC base=+0.061)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.746` → IC=+0.145 (n=409)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 10.746 (IC base=+0.061)

- **PATRÓN** `ibs_20min` < `0.0455` → IC=+0.257 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0455 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.1449` → IC=+0.148 (n=330)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.1449 (IC base=+0.045)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.3688` → IC=-0.153 (n=200)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3688
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=603)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.130 (n=636)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0058 (IC base=+0.082)

- **PATRÓN** `ibs_20min` > `0.3688` → IC=+0.161 (n=603)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.3688 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` > `0.1218` → IC=+0.171 (n=296)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1218 (IC base=+0.082)

- **PATRÓN** `ibs_20min` < `0.0602` → IC=+0.280 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0602 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.2135` → IC=+0.177 (n=97)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2135 (IC base=+0.055)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.7041` → IC=-0.159 (n=127)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7041
  - _Potencial_: sin este filtro IC_bueno=+0.099 (n=382)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.133 (n=428)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.005 (IC base=+0.080)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.135 (n=313)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 15.0 (IC base=+0.080)

- **PATRÓN** `ibs_20min` > `0.5378` → IC=+0.178 (n=545)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.5378 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` > `0.1265` → IC=+0.179 (n=306)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1265 (IC base=+0.080)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.791` → IC=+0.204 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.791 (IC base=+0.080)

- **PATRÓN** `ibs_20min` < `0.0314` → IC=+0.254 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0314 (IC base=+0.015)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.617` → IC=+0.219 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.617 (IC base=+0.015)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.198 (n=223)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 1.0 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.712` → IC=+0.135 (n=154)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.712 (IC base=+0.024)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.150 (n=298)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0108 (IC base=+0.065)

- **PATRÓN** `ibs_20min` < `0.4333` → IC=+0.174 (n=308)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.4333 (IC base=+0.065)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.988` → IC=+0.338 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.988 (IC base=+0.065)

- **PATRÓN** `volumen_regimen` > `1.105` → IC=+0.186 (n=103)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 1.105 (IC base=+0.065)

- **PATRÓN** `volumen_pendiente_norm` > `0.152` → IC=+0.184 (n=93)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.152 (IC base=+0.065)

- **PATRÓN** `volumen_spike_ratio` > `1.5274` → IC=+0.135 (n=253)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.5274 (IC base=+0.065)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0054` → IC=-0.235 (n=168)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0054
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=171)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.336 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=268)

- **FILTRO** `dist_vwap_pct` > `0.2351` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2351
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=323)

- **FILTRO** `volumen_regimen` < `0.7738` → IC=-0.302 (n=84)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7738
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=255)

- **FILTRO** `ibs_20min` > `0.5142` → IC=-0.313 (n=153)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5142
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=154)

- **FILTRO** `dist_vwap_pct` > `0.4722` → IC=-0.450 (n=18)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4722
  - _Potencial_: sin este filtro IC_bueno=-0.280 (n=289)

- **FILTRO** `sigma_ewma_delta_pct` > `9.983` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.983
  - _Potencial_: sin este filtro IC_bueno=-0.288 (n=281)

- **FILTRO** `volumen_pendiente_norm` > `0.0435` → IC=-0.382 (n=32)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0435
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=187)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `volumen_regimen` < `1.2266` → IC=-0.296 (n=52)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2266
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=52)

- **FILTRO** `volumen_regimen` > `0.807` → IC=-0.333 (n=34)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.807
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=104)

- **FILTRO** `volumen_spike_ratio` > `1.4782` → IC=-0.315 (n=52)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.4782
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=53)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` < `0.0027` → IC=-0.293 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0027
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=87)

- **FILTRO** `ibs_20min` < `0.5843` → IC=-0.467 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5843
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=86)

- **FILTRO** `volumen_regimen` > `1.1691` → IC=-0.167 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.1691
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=86)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.375 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.308 (n=97)

- **FILTRO** `ibs_20min` > `0.702` → IC=-0.405 (n=40)

  - _Acción_: SKIP cuando `ibs_20min` > 0.702
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=79)

- **FILTRO** `dist_vwap_pct` > `0.1284` → IC=-0.371 (n=29)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1284
  - _Potencial_: sin este filtro IC_bueno=-0.304 (n=90)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.321 (n=104)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.400 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=103)

- **FILTRO** `volumen_regimen` < `0.7553` → IC=-0.344 (n=30)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7553
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=91)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.242 (n=29)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.213 (n=92)

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
- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.214 (n=204)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0079 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.193 (n=317)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 15.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.176 (n=612)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.6667 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.5443` → IC=+0.256 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5443 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.614` → IC=+0.138 (n=335)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 3.614 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.697` → IC=+0.142 (n=450)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 2.697 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.6225` → IC=+0.180 (n=204)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6225 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` < `0.0701` → IC=+0.175 (n=438)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.0701 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.4169` → IC=+0.161 (n=505)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.4169 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.1388` → IC=+0.121 (n=613)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.1388 (IC base=+0.039)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.069` → IC=+0.155 (n=204)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 9.069 (IC base=+0.039)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.75` → IC=-0.154 (n=79)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=163)

- **PATRÓN** `dist_vwap_pct` > `0.5497` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5497 (IC base=+0.016)

- **PATRÓN** `ibs_20min` < `0.1796` → IC=+0.174 (n=323)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.1796 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.158` → IC=+0.140 (n=137)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 7.158 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` > `1.0364` → IC=+0.151 (n=147)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.0364 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.2687` → IC=+0.148 (n=52)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2687 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` > `1.7759` → IC=+0.143 (n=194)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.7759 (IC base=+0.111)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1263` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1263
  - _Potencial_: sin este filtro IC_bueno=+0.175 (n=195)

- **FILTRO** `ibs_20min` > `0.1597` → IC=-0.143 (n=113)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1597
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=221)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.132 (n=202)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0062 (IC base=+0.124)

- **PATRÓN** `sigma_h` > `0.003` → IC=+0.135 (n=179)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.003 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.1025` → IC=+0.126 (n=89)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.1025 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.200 (n=68)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.8015` → IC=+0.163 (n=179)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.8015 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.0953` → IC=+0.147 (n=165)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.0953 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.217` → IC=+0.160 (n=210)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 9.217 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `0.6229` → IC=+0.196 (n=67)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.6229 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` < `0.1263` → IC=+0.175 (n=195)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.1263 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `2.1409` → IC=+0.169 (n=152)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 2.1409 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=169)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `1623.6709` → IC=+0.185 (n=201)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1623.6709 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.957` → IC=+0.194 (n=60)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 10.957 (IC base=+0.000)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `dist_vwap_pct` > `0.1415` → IC=-0.146 (n=46)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1415
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=118)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.296 (n=165)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` > `0.6818` → IC=+0.277 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6818 (IC base=+0.235)

- **PATRÓN** `dist_vwap_pct` > `0.6827` → IC=+0.387 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6827 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.903` → IC=+0.347 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.903 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` < `0.7975` → IC=+0.274 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7975 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` < `0.2669` → IC=+0.262 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2669 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.0951` → IC=+0.293 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0951 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` < `1.4721` → IC=+0.333 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4721 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.309` → IC=+0.267 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.309 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.256` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.256 (IC base=-0.072)

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

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=223)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=223)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=499)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `4006.09` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `liq_usd_total` < 4006.09
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=26)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=35)

- **PATRÓN** `liq_n` > `2.0` → IC=+0.134 (n=91)

  - _Acción_: Kelly boost +0.67€ cuando `liq_n` > 2.0 (IC base=+0.065)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.143 (n=54)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 8.0 (IC base=+0.065)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=3796)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=117)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=74)

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

- **FILTRO** `hora_utc` > `10.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=15)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.126 (n=263)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=+0.023)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=1514)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=1468)

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
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=915)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=915)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=1043)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=1043)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=245)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=245)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=344)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=280)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=375)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=375)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=220)

- **FILTRO** `libro_liquidez` < `649.4605` → IC=-0.137 (n=133)

  - _Acción_: SKIP cuando `libro_liquidez` < 649.4605
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=272)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=298)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `restante_min` < `10.72` → IC=-0.145 (n=29)

  - _Acción_: SKIP cuando `restante_min` < 10.72
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=59)

- **FILTRO** `lag_apertura_s` > `256.96` → IC=-0.145 (n=29)

  - _Acción_: SKIP cuando `lag_apertura_s` > 256.96
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=59)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.197 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=79)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.250 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=48)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.51` → IC=+0.148 (n=262)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.51 (IC base=-0.001)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` > `0.61` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=175)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.127 (n=140)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=560)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.137 (n=276)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=298)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.164 (n=123)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=519)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.149 (n=257)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=529)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.174 (n=6826)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=22025)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.177 (n=7199)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=22481)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.190 (n=1291)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=4017)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.176 (n=1226)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=4051)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.139 (n=1393)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 1.0 (IC base=+0.041)

- **PATRÓN** `libro_liquidez` > `1038.58` → IC=+0.140 (n=2654)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 1038.58 (IC base=+0.041)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.132 (n=2484)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.5 (IC base=+0.013)

- **PATRÓN** `libro_liquidez` > `1144.325` → IC=+0.150 (n=1795)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1144.325 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.182 (n=1024)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3180)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.205 (n=1287)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=4107)

- **PATRÓN** `ibs_20min` > `0.965` → IC=+0.128 (n=1807)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` > 0.965 (IC base=+0.035)

- **PATRÓN** `libro_liquidez` > `1728.84` → IC=+0.122 (n=1807)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1728.84 (IC base=+0.035)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.154 (n=1316)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=3999)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2417)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=2341)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.188 (n=922)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=2885)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=3786)

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
- **FILTRO** `py_entrada` > `0.495` → IC=-0.146 (n=80)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=254)

- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

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
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=953)

- **FILTRO** `libro_liquidez` < `1797.2058` → IC=-0.161 (n=243)

  - _Acción_: SKIP cuando `libro_liquidez` < 1797.2058
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=729)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.196 (n=366)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=717)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.133 (n=19788)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=44236)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.297 (n=15026)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=48998)

- **FILTRO** `ibs_7min` < `0.225` → IC=-0.231 (n=16005)

  - _Acción_: SKIP cuando `ibs_7min` < 0.225
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=48019)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.152 (n=21446)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=42578)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.243 (n=19939)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=60503)

- **FILTRO** `ibs_7min` > `0.283` → IC=-0.181 (n=20108)

  - _Acción_: SKIP cuando `ibs_7min` > 0.283
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=60334)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.154 (n=2794)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=8508)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.317 (n=2757)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=8545)

- **FILTRO** `ibs_7min` < `0.7105` → IC=-0.249 (n=3725)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7105
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=7577)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.149 (n=2653)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=8649)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.277 (n=3326)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=10577)

- **FILTRO** `ibs_7min` > `0.7722` → IC=-0.214 (n=3475)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7722
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=10428)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.261 (n=2555)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=8162)

- **FILTRO** `ibs_7min` < `0.7168` → IC=-0.203 (n=2679)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7168
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=8038)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.194 (n=2670)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=8047)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.260 (n=2727)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=8231)

- **FILTRO** `ibs_7min` > `0.2649` → IC=-0.191 (n=2739)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2649
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=8219)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.179 (n=2726)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=8232)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.163 (n=2637)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=8152)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.314 (n=2690)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=8099)

- **FILTRO** `ibs_7min` < `0.2867` → IC=-0.248 (n=3560)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2867
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=7229)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.197 (n=2326)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=8463)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.260 (n=3510)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=11226)

- **FILTRO** `ibs_7min` > `0.7315` → IC=-0.182 (n=3683)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7315
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=11053)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.265 (n=2513)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=7876)

- **FILTRO** `ibs_7min` < `0.72` → IC=-0.194 (n=2595)

  - _Acción_: SKIP cuando `ibs_7min` < 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=7794)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.188 (n=2514)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=7875)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.259 (n=2478)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=8353)

- **FILTRO** `ibs_7min` > `0.2748` → IC=-0.172 (n=2707)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2748
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=8124)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.174 (n=2617)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=8214)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.285 (n=2578)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=7786)

- **FILTRO** `ibs_7min` < `0.7083` → IC=-0.227 (n=3402)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7083
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=6962)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.221 (n=2429)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=7935)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.194 (n=3685)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=11845)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.299 (n=2603)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=7860)

- **FILTRO** `ibs_7min` < `0.18` → IC=-0.230 (n=2615)

  - _Acción_: SKIP cuando `ibs_7min` < 0.18
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=7848)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.203 (n=2442)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=8021)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.226 (n=3599)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=10885)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.160 (n=301)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=1006)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1292)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.156 (n=158)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=592)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=872)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.143 (n=166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=333)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=450)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.130 (n=90)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=652)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3983` → IC=+0.135 (n=1325)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.3983 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.131 (n=586)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 5.0 (IC base=+0.125)

- **PATRÓN** `total_vol_5m` < `437.371` → IC=+0.153 (n=442)

  - _Acción_: Kelly boost +0.77€ cuando `total_vol_5m` < 437.371 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `3448.6944` → IC=+0.145 (n=601)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3448.6944 (IC base=+0.125)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.169 (n=149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 14.0 (IC base=+0.120)

- **PATRÓN** `total_vol_5m` < `372.075` → IC=+0.146 (n=275)

  - _Acción_: Kelly boost +0.73€ cuando `total_vol_5m` < 372.075 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2522.0946` → IC=+0.217 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2522.0946 (IC base=+0.120)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.4378` → IC=+0.139 (n=95)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio` |x|> 0.4378 (IC base=+0.115)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.136 (n=248)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 14.0 (IC base=+0.115)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.122 (n=334)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.04 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `2304.5801` → IC=+0.142 (n=185)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2304.5801 (IC base=+0.115)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4161` → IC=+0.190 (n=169)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.95€ cuando `delta_ratio` |x|> 0.4161 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.155 (n=265)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 4.0 (IC base=+0.138)

- **PATRÓN** `total_vol_5m` < `381.6269` → IC=+0.210 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 381.6269 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `5094.6188` → IC=+0.144 (n=254)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 5094.6188 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `67.0` → IC=+0.190 (n=111)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 67.0 (IC base=+0.138)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.174 (n=231)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.196 (n=110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 6.0 (IC base=+0.150)

- **PATRÓN** `total_vol_5m` < `4901.52` → IC=+0.199 (n=154)

  - _Acción_: Kelly boost +0.99€ cuando `total_vol_5m` < 4901.52 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `3140.095` → IC=+0.178 (n=206)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 3140.095 (IC base=+0.150)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `10.0` → IC=+0.142 (n=174)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 10.0 (IC base=+0.104)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.174 (n=170)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `3728.089` → IC=+0.151 (n=84)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3728.089 (IC base=+0.104)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.7861` → IC=-0.284 (n=49)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.7861
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=148)

- **FILTRO** `pct_vs_K` |x|> `3.4286` → IC=-0.193 (n=255)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4286
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=497)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.175 (n=189)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0037 (IC base=-0.081)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0072` → IC=-0.289 (n=55)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0072
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=169)

- **FILTRO** `T_h` > `87.9901` → IC=-0.237 (n=55)

  - _Acción_: SKIP cuando `T_h` > 87.9901
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=169)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.297 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=-0.035)

- **PATRÓN** `pct_vs_K` |x|≤ `1.6038` → IC=+0.145 (n=74)

  - _Acción_: Kelly boost +0.72€ cuando `pct_vs_K` |x|≤ 1.6038 (IC base=-0.035)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0105` → IC=-0.180 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=47)

- **FILTRO** `pct_vs_K` |x|> `9.1619` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 9.1619
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=53)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `pct_vs_K` |x|> `2.97` → IC=-0.204 (n=69)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.97
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=71)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0096` → IC=-0.240 (n=448)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0096
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=232)

- **FILTRO** `T_h` > `77.6652` → IC=-0.218 (n=455)

  - _Acción_: SKIP cuando `T_h` > 77.6652
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=225)

- **FILTRO** `sigma_h` < `0.005` → IC=-0.235 (n=145)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=438)

- **FILTRO** `pct_vs_K` |x|> `2.0455` → IC=-0.367 (n=291)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.0455
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=292)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0085` → IC=-0.206 (n=168)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=57)

- **FILTRO** `T_h` > `64.5217` → IC=-0.197 (n=150)

  - _Acción_: SKIP cuando `T_h` > 64.5217
  - _Potencial_: sin este filtro IC_bueno=-0.123 (n=75)

- **FILTRO** `T_h` > `72.749` → IC=-0.256 (n=158)

  - _Acción_: SKIP cuando `T_h` > 72.749
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=53)

- **FILTRO** `pct_vs_K` |x|> `1.9209` → IC=-0.397 (n=105)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 1.9209
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=106)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `sigma_h` < `0.0085` → IC=-0.250 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0096` → IC=-0.323 (n=128)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0096
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=66)

- **FILTRO** `T_h` > `102.4593` → IC=-0.286 (n=96)

  - _Acción_: SKIP cuando `T_h` > 102.4593
  - _Potencial_: sin este filtro IC_bueno=-0.240 (n=98)

- **FILTRO** `sigma_h` < `0.0058` → IC=-0.205 (n=59)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0058
  - _Potencial_: sin este filtro IC_bueno=-0.161 (n=122)

- **FILTRO** `pct_vs_K` |x|> `2.3708` → IC=-0.413 (n=90)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.3708
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=91)

- **PATRÓN** `pct_vs_K` |x|≤ `0.7908` → IC=+0.188 (n=46)

  - _Acción_: Kelly boost +0.94€ cuando `pct_vs_K` |x|≤ 0.7908 (IC base=-0.178)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` < `0.0099` → IC=-0.222 (n=16)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0099
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `T_h` > `126.9278` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `T_h` > 126.9278
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0082` → IC=-0.296 (n=47)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0082
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=146)

- **FILTRO** `T_h` > `70.6078` → IC=-0.205 (n=144)

  - _Acción_: SKIP cuando `T_h` > 70.6078
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=49)

- **FILTRO** `sigma_h` < `0.0088` → IC=-0.295 (n=42)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0088
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=87)

- **FILTRO** `pct_vs_K` |x|> `3.2571` → IC=-0.432 (n=42)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.2571
  - _Potencial_: sin este filtro IC_bueno=-0.129 (n=87)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1208` → IC=+0.469 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1208 (IC base=+0.343)

- **PATRÓN** `sigma_h` < `0.0147` → IC=+0.361 (n=106)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0147 (IC base=+0.343)

- **PATRÓN** `T_h` < `0.3439` → IC=+0.395 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3439 (IC base=+0.343)

- **PATRÓN** `T_h` > `0.7258` → IC=+0.377 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7258 (IC base=+0.343)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.481 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.343)

- **PATRÓN** `edge` > `0.0997` → IC=+0.439 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.0997 (IC base=+0.408)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.432 (n=161)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.408)

- **PATRÓN** `T_h` < `0.608` → IC=+0.440 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.608 (IC base=+0.408)

- **PATRÓN** `T_h` > `1.4832` → IC=+0.416 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4832 (IC base=+0.408)

- **PATRÓN** `dist_50` > `0.3765` → IC=+0.447 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3765 (IC base=+0.408)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.472 (n=140)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.408)

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
- **PATRÓN** `edge` > `0.1015` → IC=+0.461 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1015 (IC base=+0.410)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.412 (n=55)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.410)

- **PATRÓN** `T_h` < `1.2716` → IC=+0.430 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.2716 (IC base=+0.410)

- **PATRÓN** `dist_50` > `0.3792` → IC=+0.461 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3792 (IC base=+0.410)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.403 (n=29)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.410)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.410)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=357)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=425)

- **PATRÓN** `streak_estiramiento` < `0.2813` → IC=+0.258 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.2813 (IC base=+0.058)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.132 (n=218)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 33.0 (IC base=+0.058)

- **PATRÓN** `libro_liquidez` > `2493.7311` → IC=+0.132 (n=153)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2493.7311 (IC base=+0.058)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.495 (IC base=+0.053)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=30)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=21)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.495 (IC base=+0.026)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.128 (n=162)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.098)

- **PATRÓN** `streak_estiramiento` < `0.555` → IC=+0.176 (n=134)

  - _Acción_: Kelly boost +0.88€ cuando `streak_estiramiento` < 0.555 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.174 (n=133)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 34.0 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `2222.8358` → IC=+0.138 (n=136)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2222.8358 (IC base=+0.098)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=99)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=108)

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
- **PATRÓN** `volumen_racha` < `16919.513` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_racha` < 16919.513 (IC base=+0.060)

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
- **FILTRO** `hora_utc` > `5.0` → IC=-0.158 (n=36)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=34)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=4402)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.158 (n=36)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=34)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=2532)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.189 (n=1834)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0056 (IC base=+0.163)

- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.172 (n=1389)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0127 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.2082` → IC=+0.176 (n=4165)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2082 (IC base=+0.163)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3485` → IC=+0.172 (n=3821)

  - _Acción_: Kelly boost +0.86€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3485 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.173 (n=3837)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.164 (n=3840)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 15.0 (IC base=+0.163)

- **PATRÓN** `ibs_15` > `0.527` → IC=+0.236 (n=4165)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.527 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.1308` → IC=+0.159 (n=2032)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1308 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` < `0.4973` → IC=+0.149 (n=3824)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.4973 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.96` → IC=+0.264 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.96 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `2495.2936` → IC=+0.171 (n=3721)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2495.2936 (IC base=+0.163)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1696)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.244 (n=310)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.0592` → IC=+0.254 (n=234)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0592 (IC base=+0.205)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2638` → IC=+0.229 (n=234)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2638 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.226 (n=731)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.205)

- **PATRÓN** `ibs_15` > `0.7193` → IC=+0.278 (n=701)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7193 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.2385` → IC=+0.219 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2385 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.385` → IC=+0.309 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.385 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `8049.1341` → IC=+0.214 (n=701)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8049.1341 (IC base=+0.205)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.159 (n=850)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0068 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.1083` → IC=+0.155 (n=567)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1083 (IC base=+0.137)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1428` → IC=+0.140 (n=567)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio_macro` |x|> 0.1428 (IC base=+0.137)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.125` → IC=+0.144 (n=341)

  - _Acción_: Kelly boost +0.72€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.125 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.146 (n=774)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 6.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.141 (n=889)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 17.0 (IC base=+0.137)

- **PATRÓN** `ibs_15` > `0.5144` → IC=+0.228 (n=850)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5144 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.1197` → IC=+0.153 (n=526)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.1197 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.194` → IC=+0.280 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.194 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `5772.1737` → IC=+0.168 (n=386)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 5772.1737 (IC base=+0.137)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8772` → IC=+0.234 (n=347)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8772 (IC base=+0.079)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=540)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.079)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0194` → IC=+0.191 (n=617)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0194 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.0244` → IC=+0.213 (n=308)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0244 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.2026` → IC=+0.205 (n=925)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2026 (IC base=+0.190)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3444` → IC=+0.223 (n=824)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3444 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.192 (n=841)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 6.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.199 (n=828)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 14.0 (IC base=+0.190)

- **PATRÓN** `ibs_15` > `0.5111` → IC=+0.271 (n=924)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5111 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` > `0.1328` → IC=+0.214 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1328 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.497` → IC=+0.229 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.497 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.193 (n=636)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `2957.7936` → IC=+0.281 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2957.7936 (IC base=+0.190)

- **PATRÓN** `ibs_15` < `0.1071` → IC=+0.171 (n=824)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.85€ cuando `ibs_15` < 0.1071 (IC base=+0.069)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.386 (n=315)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1503` → IC=+0.379 (n=462)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1503 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1379` → IC=+0.385 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1379 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.376 (n=694)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.7881` → IC=+0.398 (n=694)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7881 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.1523` → IC=+0.384 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1523 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.204` → IC=+0.396 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.204 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.369 (n=841)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `3837.2318` → IC=+0.375 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3837.2318 (IC base=+0.365)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.361 (n=308)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.361)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.365 (n=117)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.361)

- **PATRÓN** `drift_15min` |x|≤ `0.5207` → IC=+0.360 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5207 (IC base=+0.361)

- **PATRÓN** `delta_ratio_macro` |x|> `0.156` → IC=+0.368 (n=233)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.156 (IC base=+0.361)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1413` → IC=+0.392 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1413 (IC base=+0.361)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.378 (n=327)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.361)

- **PATRÓN** `ibs_15` > `0.8077` → IC=+0.386 (n=350)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8077 (IC base=+0.361)

- **PATRÓN** `dist_vwap_pct` > `0.3743` → IC=+0.386 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3743 (IC base=+0.361)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.244` → IC=+0.385 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.244 (IC base=+0.361)

- **PATRÓN** `libro_liquidez` > `8041.1866` → IC=+0.384 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8041.1866 (IC base=+0.361)

- **PATRÓN** `ballena_activa_n` < `493.0` → IC=+0.403 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 493.0 (IC base=+0.361)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.367 (n=345)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.368)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.384 (n=230)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.368)

- **PATRÓN** `drift_60min` |x|≤ `0.1062` → IC=+0.371 (n=230)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1062 (IC base=+0.368)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0833` → IC=+0.381 (n=308)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0833 (IC base=+0.368)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.383 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.368)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.383 (n=161)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.368)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.376 (n=159)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.368)

- **PATRÓN** `ibs_15` > `0.8123` → IC=+0.406 (n=308)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8123 (IC base=+0.368)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.374 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.368)

- **PATRÓN** `dist_vwap_pct` < `0.2918` → IC=+0.372 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2918 (IC base=+0.368)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.356` → IC=+0.405 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.356 (IC base=+0.368)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.373 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.368)

- **PATRÓN** `libro_liquidez` > `4019.374` → IC=+0.399 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4019.374 (IC base=+0.368)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.181 (n=2334)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=2336)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.214 (n=1839)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=2831)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.138` → IC=+0.219 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.138 (IC base=-0.070)

- **PATRÓN** `ibs_15` > `0.6335` → IC=+0.281 (n=1119)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6335 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1113` → IC=+0.207 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1113 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` < `0.5662` → IC=+0.204 (n=1181)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5662 (IC base=-0.070)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2327` → IC=+0.269 (n=1374)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2327 (IC base=-0.009)

- **PATRÓN** `ibs_15` < `0.3704` → IC=+0.281 (n=4124)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3704 (IC base=-0.009)

- **PATRÓN** `dist_vwap_pct` > `0.6602` → IC=+0.274 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6602 (IC base=-0.009)

- **PATRÓN** `dist_vwap_pct` < `0.1667` → IC=+0.245 (n=3078)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1667 (IC base=-0.009)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0335` → IC=-0.223 (n=2224)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0335
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=743)

- **FILTRO** `sigma_h` < `0.0036` → IC=-0.223 (n=741)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0036
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=2226)

- **FILTRO** `sigma_ewma_delta_pct` > `22.967` → IC=-0.269 (n=423)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.967
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=2544)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.156 (n=286)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0029 (IC base=+0.081)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1441` → IC=+0.271 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1441 (IC base=+0.081)

- **PATRÓN** `ibs_15` > `0.7639` → IC=+0.330 (n=381)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7639 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.1051` → IC=+0.283 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1051 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` < `0.3659` → IC=+0.286 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3659 (IC base=+0.081)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.868` → IC=+0.149 (n=249)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 18.868 (IC base=+0.081)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0674` → IC=+0.246 (n=69)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0674 (IC base=-0.189)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1389` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1389 (IC base=-0.189)

- **PATRÓN** `ibs_15` < `0.6221` → IC=+0.319 (n=70)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6221 (IC base=-0.189)

- **PATRÓN** `dist_vwap_pct` < `0.0459` → IC=+0.310 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0459 (IC base=-0.189)

- **PATRÓN** `ballena_activa_n` < `288.0` → IC=+0.375 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 288.0 (IC base=-0.189)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=724)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.165 (n=490)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.0721` → IC=+0.188 (n=245)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0721 (IC base=+0.153)

- **PATRÓN** `drift_15min` |x|≤ `0.4011` → IC=+0.154 (n=186)

  - _Acción_: Kelly boost +0.77€ cuando `drift_15min` |x|≤ 0.4011 (IC base=+0.153)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.194 (n=430)

  - _Acción_: Kelly boost +0.97€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.174 (n=400)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 11.0 (IC base=+0.153)

- **PATRÓN** `ibs_15` > `0.5874` → IC=+0.247 (n=556)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5874 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.4691` → IC=+0.164 (n=144)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.4691 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.1597` → IC=+0.156 (n=437)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1597 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.12` → IC=+0.257 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.12 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.160 (n=724)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `9534.8435` → IC=+0.154 (n=186)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 9534.8435 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.266 (n=531)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.1036` → IC=+0.245 (n=531)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1036 (IC base=+0.243)

- **PATRÓN** `drift_15min` |x|≤ `0.7736` → IC=+0.257 (n=1400)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7736 (IC base=+0.243)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1564` → IC=+0.262 (n=1060)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1564 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.247 (n=587)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.247 (n=1077)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.243)

- **PATRÓN** `ibs_15` < `0.3781` → IC=+0.275 (n=1591)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3781 (IC base=+0.243)

- **PATRÓN** `dist_vwap_pct` > `0.617` → IC=+0.272 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.617 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.434` → IC=+0.246 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.434 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.472` → IC=+0.250 (n=1662)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.472 (IC base=+0.243)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1729` → IC=-0.246 (n=364)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1729
  - _Potencial_: sin este filtro IC_bueno=-0.157 (n=713)

- **FILTRO** `drift_15min` |x|> `0.8925` → IC=-0.279 (n=269)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8925
  - _Potencial_: sin este filtro IC_bueno=-0.157 (n=808)

- **FILTRO** `sigma_ewma_delta_pct` > `6.585` → IC=-0.204 (n=248)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.585
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=829)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.188)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.188)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.188)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 29.0 (IC base=-0.188)

- **PATRÓN** `ibs_15` < `0.4062` → IC=+0.291 (n=708)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.4062 (IC base=-0.034)

- **PATRÓN** `dist_vwap_pct` < `0.2722` → IC=+0.233 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2722 (IC base=-0.034)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0589` → IC=-0.228 (n=957)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0589
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=320)

- **FILTRO** `drift_15min` |x|> `0.7519` → IC=-0.250 (n=638)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.7519
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=639)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.211)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.211)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0515` → IC=+0.270 (n=934)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0515 (IC base=-0.024)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1173` → IC=+0.289 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1173 (IC base=-0.024)

- **PATRÓN** `ibs_15` < `0.137` → IC=+0.309 (n=622)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.137 (IC base=-0.024)

- **PATRÓN** `dist_vwap_pct` > `0.7901` → IC=+0.337 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7901 (IC base=-0.024)

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

- **PATRÓN** `dist_vwap_pct` > `0.1565` → IC=+0.135 (n=72)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.1565 (IC base=+0.054)

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

- **PATRÓN** `dist_vwap_pct` > `0.1565` → IC=+0.135 (n=72)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.1565 (IC base=+0.054)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.291 (n=1219)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.0542` → IC=+0.319 (n=407)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0542 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1511` → IC=+0.289 (n=812)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1511 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.223` → IC=+0.299 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.223 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.302 (n=1263)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.8395` → IC=+0.317 (n=1219)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8395 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.2663` → IC=+0.317 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2663 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.379` → IC=+0.386 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.379 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `13583.6664` → IC=+0.307 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13583.6664 (IC base=+0.287)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.308 (n=217)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.281)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.298 (n=295)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.0592` → IC=+0.317 (n=217)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0592 (IC base=+0.281)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2673` → IC=+0.284 (n=216)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2673 (IC base=+0.281)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3906` → IC=+0.287 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3906 (IC base=+0.281)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.301 (n=680)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.281)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.306 (n=649)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.829 (IC base=+0.281)

- **PATRÓN** `dist_vwap_pct` > `0.2516` → IC=+0.316 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2516 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.55` → IC=+0.379 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.55 (IC base=+0.281)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.281 (n=838)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `16045.3097` → IC=+0.317 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16045.3097 (IC base=+0.281)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.308 (n=571)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.1075` → IC=+0.315 (n=381)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1075 (IC base=+0.293)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1451` → IC=+0.296 (n=380)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1451 (IC base=+0.293)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1009` → IC=+0.343 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1009 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.308 (n=546)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.297 (n=520)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.293)

- **PATRÓN** `ibs_15` > `0.8527` → IC=+0.323 (n=570)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8527 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.2815` → IC=+0.316 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2815 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.513` → IC=+0.383 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.513 (IC base=+0.293)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2669` → IC=-0.122 (n=88)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2669
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=268)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.126` → IC=-0.159 (n=89)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.126
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=267)

- **FILTRO** `ballena_activa_n` > `36.0` → IC=-0.134 (n=241)

  - _Acción_: SKIP cuando `ballena_activa_n` > 36.0
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
- **FILTRO** `sigma_h` < `0.0061` → IC=-0.167 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0061
  - _Potencial_: sin este filtro IC_bueno=-0.130 (n=25)

- **FILTRO** `drift_60min` |x|> `0.2521` → IC=-0.222 (n=16)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2521
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=34)

- **FILTRO** `ballena_activa_n` > `19.0` → IC=-0.206 (n=32)

  - _Acción_: SKIP cuando `ballena_activa_n` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

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
- **PATRÓN** `T_h` > `87.9922` → IC=+0.178 (n=547)

  - _Acción_: Kelly boost +0.89€ cuando `T_h` > 87.9922 (IC base=+0.178)

- **PATRÓN** `ratio` < `0.973` → IC=+0.397 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.178)

- **PATRÓN** `T_h` > `115.9373` → IC=+0.354 (n=2484)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 115.9373 (IC base=+0.336)

- **PATRÓN** `ratio` > `1.0213` → IC=+0.378 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0213 (IC base=+0.336)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `111.4342` → IC=+0.160 (n=230)

  - _Acción_: Kelly boost +0.80€ cuando `T_h` > 111.4342 (IC base=+0.145)

- **PATRÓN** `ratio` < `0.9819` → IC=+0.322 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9819 (IC base=+0.145)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.312 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.297)

- **PATRÓN** `ratio` > `1.0422` → IC=+0.417 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0422 (IC base=+0.297)

### WEEKLY_PRICE#ETH
- **PATRÓN** `ratio` < `0.9854` → IC=+0.391 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.218)

- **PATRÓN** `T_h` > `111.996` → IC=+0.352 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.996 (IC base=+0.322)

- **PATRÓN** `ratio` > `1.0083` → IC=+0.337 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0083 (IC base=+0.322)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0624` → IC=+0.435 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0624 (IC base=+0.398)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.527 sube el IC de +0.163 a +0.236 en UPDOWN_GBM#15min (n=4165). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7193 sube el IC de +0.205 a +0.278 en UPDOWN_GBM#BTC#15min (n=701). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5144 sube el IC de +0.137 a +0.228 en UPDOWN_GBM#ETH#15min (n=850). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.8772 sube el IC de +0.079 a +0.234 en UPDOWN_GBM#SOL#15min (n=347). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5111 sube el IC de +0.190 a +0.271 en UPDOWN_GBM#XRP#15min (n=924). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1071 sube el IC de +0.069 a +0.171 en UPDOWN_GBM#XRP#15min (n=824). Ya aplicado como kelly_boost=+0.85€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6335 sube el IC de -0.070 a +0.281 en UPDOWN_GBM_15M_TARDIO (n=1119). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3704 sube el IC de -0.009 a +0.281 en UPDOWN_GBM_15M_TARDIO (n=4124). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7639 sube el IC de +0.081 a +0.330 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=381). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6221 sube el IC de -0.189 a +0.319 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=70). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5874 sube el IC de +0.153 a +0.247 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=556). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3781 sube el IC de +0.243 a +0.275 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1591). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.188 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.4062 sube el IC de -0.034 a +0.291 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=708). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.211 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.137 sube el IC de -0.024 a +0.309 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=622). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.093 a +0.364 en UPDOWN_GBM_ETH_15M_HORA7 (n=20). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.093 a +0.364 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=20). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8395 sube el IC de +0.287 a +0.317 en UPDOWN_GBM_IBS_ALTO (n=1219). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.281 a +0.306 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=649). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8527 sube el IC de +0.293 a +0.323 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=570). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7881 sube el IC de +0.365 a +0.398 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=694). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8077 sube el IC de +0.361 a +0.386 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=350). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.8123 sube el IC de +0.368 a +0.406 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=308). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2083 | +0.086 | +218.81€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2083 | +0.086 | +218.81€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1684 | +0.087 | +183.17€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1684 | +0.087 | +183.17€ | 0 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 284 | +0.070 | +11.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 284 | +0.070 | +11.30€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 84 | +0.128 | +24.67€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 84 | +0.128 | +24.67€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 915 | -0.019 | +88.93€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 915 | -0.019 | +88.93€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 708 | -0.041 | +62.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 708 | -0.041 | +62.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 150 | +0.086 | +25.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 150 | +0.086 | +25.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 51 | -0.028 | -1.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 51 | -0.028 | -1.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 43846 | -0.083 | -5581.96€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2598 | +0.059 | -288.92€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 41248 | -0.092 | -5293.03€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4623 | -0.116 | -757.73€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4623 | -0.116 | -757.73€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2598 | +0.059 | -288.92€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2598 | +0.059 | -288.92€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4595 | -0.115 | -892.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4595 | -0.115 | -892.30€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 11782 | -0.024 | -1139.71€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 11782 | -0.024 | -1139.71€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 11830 | -0.117 | -1124.04€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 11830 | -0.117 | -1124.04€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8418 | -0.127 | -1379.27€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8418 | -0.127 | -1379.27€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 42114 | -0.013 | +3123.35€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 10860 | +0.005 | +1625.28€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 31254 | -0.019 | +1498.08€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 42114 | -0.013 | +3123.35€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 10860 | +0.005 | +1625.28€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 31254 | -0.019 | +1498.08€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 166810 | +0.114 | -6832.24€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 20361 | +0.180 | -684.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 752 | -0.004 | -77.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 135950 | +0.106 | -5734.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 9747 | +0.094 | -335.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 22527 | +0.106 | -1428.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 68 | -0.186 | +4.73€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 22444 | +0.108 | -1421.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 31956 | +0.125 | -526.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5479 | +0.181 | -226.11€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 22516 | +0.120 | -159.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3919 | +0.079 | -118.20€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 22581 | +0.099 | -1611.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 82 | -0.119 | -3.25€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 22484 | +0.100 | -1597.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 35551 | +0.123 | -721.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 9084 | +0.176 | -208.07€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 22852 | +0.106 | -455.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3603 | +0.101 | -50.00€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 31641 | +0.112 | -1517.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5570 | +0.198 | -258.87€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 655 | +0.025 | -23.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 23191 | +0.095 | -1067.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2225 | +0.107 | -167.56€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#XRP | 22554 | +0.106 | -1025.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 78 | -0.113 | +6.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 22463 | +0.107 | -1032.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 26943 | +0.194 | -1769.29€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 26943 | +0.194 | -1769.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 6094 | +0.176 | -555.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 6094 | +0.176 | -555.95€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 3674 | +0.199 | -114.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 3674 | +0.199 | -114.68€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 6027 | +0.176 | -517.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 6027 | +0.176 | -517.88€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5138 | +0.247 | -192.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5138 | +0.247 | -192.33€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 5931 | +0.186 | -402.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 5931 | +0.186 | -402.20€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1142 | +0.425 | -43.68€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1142 | +0.425 | -43.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 463 | +0.438 | -5.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 463 | +0.438 | -5.47€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 457 | +0.426 | -15.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 457 | +0.426 | -15.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 208 | +0.395 | -19.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 208 | +0.395 | -19.04€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 94622 | +0.201 | -6844.41€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 94622 | +0.201 | -6844.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 16295 | +0.182 | -1749.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 16295 | +0.182 | -1749.84€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 15257 | +0.225 | -502.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 15257 | +0.225 | -502.79€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 16230 | +0.181 | -1700.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 16230 | +0.181 | -1700.46€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 15388 | +0.218 | -621.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 15388 | +0.218 | -621.86€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 15680 | +0.202 | -1015.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 15680 | +0.202 | -1015.75€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 15772 | +0.197 | -1253.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 15772 | +0.197 | -1253.71€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 36340 | +0.117 | +303.11€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 36340 | +0.117 | +303.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 18078 | +0.118 | +200.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 18078 | +0.118 | +200.12€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 18262 | +0.115 | +102.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 18262 | +0.115 | +102.99€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2314 | +0.295 | +5.22€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2314 | +0.295 | +5.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1059 | +0.282 | -20.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1059 | +0.282 | -20.95€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1127 | +0.301 | +23.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1127 | +0.301 | +23.31€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 128 | +0.339 | +2.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 128 | +0.339 | +2.86€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1063 | +0.445 | +11.22€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1063 | +0.445 | +11.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 514 | +0.438 | -2.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 514 | +0.438 | -2.90€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 501 | +0.452 | +13.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 501 | +0.452 | +13.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 48 | +0.400 | +0.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 48 | +0.400 | +0.86€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1822 | +0.069 | -78.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 720 | +0.046 | -64.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1102 | +0.083 | -13.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1391 | +0.076 | -34.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 289 | +0.050 | -20.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1102 | +0.083 | -13.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 349 | +0.027 | -47.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 349 | +0.027 | -47.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 72865 | +0.101 | -1760.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 5872 | +0.094 | +97.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 66993 | +0.101 | -1857.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 39922 | +0.105 | -406.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 5872 | +0.094 | +97.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 34050 | +0.107 | -503.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 15270 | +0.109 | -67.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 15270 | +0.109 | -67.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 17673 | +0.082 | -1286.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 17673 | +0.082 | -1286.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 906 | +0.188 | -110.09€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 906 | +0.188 | -110.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 906 | +0.188 | -110.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 906 | +0.188 | -110.09€ | 2 | 4 |
| ✅ GBM_LATE_15M | 49707 | +0.097 | +27125.19€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 49707 | +0.097 | +27125.19€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 8270 | +0.221 | +6989.18€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 8270 | +0.221 | +6989.18€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 7592 | +0.177 | +5921.60€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 7592 | +0.177 | +5921.60€ | 0 | 24 |
| ✅ GBM_LATE_15M#DOGE | 8912 | +0.204 | +6912.62€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 8912 | +0.204 | +6912.62€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 6797 | +0.050 | +2037.87€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 6797 | +0.050 | +2037.87€ | 1 | 20 |
| ✅ GBM_LATE_15M#SOL | 6941 | -0.032 | +1770.97€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 6941 | -0.032 | +1770.97€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 11195 | -0.027 | +3492.95€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 11195 | -0.027 | +3492.95€ | 4 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 52838 | +0.085 | +29933.98€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 52838 | +0.085 | +29933.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 10241 | +0.001 | +5293.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 10241 | +0.001 | +5293.96€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 11327 | +0.007 | +2928.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 11327 | +0.007 | +2928.79€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 7228 | +0.286 | +7996.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 7228 | +0.286 | +7996.60€ | 0 | 23 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 9834 | +0.014 | +2942.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 9834 | +0.014 | +2942.61€ | 1 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 8242 | +0.041 | +3570.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 8242 | +0.041 | +3570.54€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5966 | +0.311 | +7201.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5966 | +0.311 | +7201.48€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 39438 | +0.179 | +32335.52€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 39438 | +0.179 | +32335.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 5949 | +0.236 | +5440.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 5949 | +0.236 | +5440.34€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 6246 | +0.145 | +4710.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 6246 | +0.145 | +4710.96€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 6327 | +0.223 | +5435.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 6327 | +0.223 | +5435.25€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 6734 | +0.133 | +5216.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 6734 | +0.133 | +5216.76€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 7423 | +0.122 | +5528.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 7423 | +0.122 | +5528.90€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 6759 | +0.229 | +6003.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 6759 | +0.229 | +6003.32€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 10448 | +0.125 | +5113.73€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 10448 | +0.125 | +5113.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 457 | +0.158 | +289.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 457 | +0.158 | +289.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3008 | +0.130 | +1637.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3008 | +0.130 | +1637.35€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 491 | +0.153 | +259.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 491 | +0.153 | +259.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3122 | +0.132 | +1530.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3122 | +0.132 | +1530.06€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2643 | +0.096 | +1028.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2643 | +0.096 | +1028.97€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 727 | +0.143 | +367.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 727 | +0.143 | +367.98€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO | 49991 | +0.185 | +40572.40€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 49991 | +0.185 | +40572.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 7893 | +0.247 | +7519.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 7893 | +0.247 | +7519.72€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 7897 | +0.142 | +5516.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 7897 | +0.142 | +5516.90€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 8457 | +0.232 | +7542.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 8457 | +0.232 | +7542.45€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 8274 | +0.139 | +5984.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 8274 | +0.139 | +5984.38€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 8865 | +0.120 | +6212.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 8865 | +0.120 | +6212.89€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 8605 | +0.236 | +7796.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 8605 | +0.236 | +7796.06€ | 0 | 22 |
| ✅ GBM_LATE_5M | 13290 | +0.208 | +10682.97€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 13290 | +0.208 | +10682.97€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3183 | +0.212 | +2762.38€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3183 | +0.212 | +2762.38€ | 0 | 26 |
| ✅ GBM_LATE_5M#DOGE | 1222 | +0.198 | +913.92€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1222 | +0.198 | +913.92€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 3858 | +0.200 | +2855.30€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3858 | +0.200 | +2855.30€ | 0 | 24 |
| ✅ GBM_LATE_5M#SOL | 2020 | +0.202 | +1621.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2020 | +0.202 | +1621.62€ | 0 | 26 |
| ✅ GBM_LATE_5M#XRP | 1953 | +0.209 | +1529.48€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1953 | +0.209 | +1529.48€ | 0 | 0 |
| ✅ GBM_LATE_60M | 4284 | +0.055 | +1206.01€ | 0 | 6 |
| ✅ GBM_LATE_60M#60min | 4284 | +0.055 | +1206.01€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1528 | +0.070 | +497.25€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1528 | +0.070 | +497.25€ | 1 | 5 |
| ✅ GBM_LATE_60M#ETH | 1391 | +0.055 | +424.22€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1391 | +0.055 | +424.22€ | 1 | 7 |
| ✅ GBM_LATE_60M#SOL | 1365 | +0.038 | +284.54€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1365 | +0.038 | +284.54€ | 0 | 8 |
| 🚫 GBM_LATE_60M_FADE | 646 | -0.250 | -32.08€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 646 | -0.250 | -32.08€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 242 | -0.246 | -16.88€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 242 | -0.246 | -16.88€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 233 | -0.249 | -8.01€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 233 | -0.249 | -8.01€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 171 | -0.251 | -7.18€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 171 | -0.251 | -7.18€ | 6 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1741 | +0.084 | +434.92€ | 0 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1741 | +0.084 | +434.92€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 672 | +0.077 | +159.04€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 672 | +0.077 | +159.04€ | 1 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 601 | +0.056 | +97.71€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 601 | +0.056 | +97.71€ | 2 | 13 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 468 | +0.128 | +178.17€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 468 | +0.128 | +178.17€ | 1 | 10 |
| ✅ LATE_WINDOW_5MIN | 198 | +0.270 | +203.69€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 198 | +0.270 | +203.69€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 198 | +0.270 | +203.69€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 198 | +0.270 | +203.69€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3945 | +0.098 | +919.85€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3945 | +0.098 | +919.85€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3945 | +0.098 | +919.85€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3945 | +0.098 | +919.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 759 | -0.013 | +7.89€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 759 | -0.013 | +7.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 7 | -0.058 | -1.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 7 | -0.058 | -1.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 229 | +0.002 | +8.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 229 | +0.002 | +8.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 27 | -0.155 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 27 | -0.155 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 197 | +0.033 | +14.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 197 | +0.033 | +14.23€ | 2 | 2 |
| ✅ LIQUIDACIONES_15M#SOL | 247 | -0.006 | +1.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 247 | -0.006 | +1.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4019 | +0.017 | +104.83€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 4019 | +0.017 | +104.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 189 | +0.034 | +0.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 189 | +0.034 | +0.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 815 | +0.015 | +40.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 815 | +0.015 | +40.20€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 216 | +0.000 | +1.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 216 | +0.000 | +1.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1566 | +0.022 | +31.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1566 | +0.022 | +31.44€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 763 | +0.011 | +1.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 763 | +0.011 | +1.66€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 470 | +0.015 | +29.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 470 | +0.015 | +29.46€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2053 | -0.038 | -25.37€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2053 | -0.038 | -25.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 619 | -0.031 | -13.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 619 | -0.031 | -13.01€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 716 | -0.013 | +11.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 716 | -0.013 | +11.29€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 718 | -0.069 | -23.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 718 | -0.069 | -23.65€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 12154 | -0.031 | -88.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 5812 | -0.035 | -81.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 6342 | -0.028 | -6.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 424 | -0.045 | -16.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 211 | -0.016 | +4.28€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 213 | -0.072 | -21.06€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 3152 | -0.022 | +22.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1494 | -0.023 | +9.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1658 | -0.021 | +13.06€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1256 | -0.025 | +22.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 639 | -0.032 | +2.73€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 617 | -0.017 | +19.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 2700 | -0.037 | -64.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1274 | -0.042 | -46.34€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1426 | -0.033 | -17.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 2340 | -0.031 | -11.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1128 | -0.038 | -22.26€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1212 | -0.024 | +10.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 2282 | -0.040 | -40.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1066 | -0.046 | -29.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1216 | -0.035 | -11.33€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 58531 | -0.000 | +3021.57€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 58531 | -0.000 | +3021.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 10585 | +0.027 | +1389.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 10585 | +0.027 | +1389.58€ | 2 | 4 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 8307 | -0.036 | -118.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 8307 | -0.036 | -118.58€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 10707 | +0.024 | +1111.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 10707 | +0.024 | +1111.71€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 8194 | -0.048 | -166.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 8194 | -0.048 | -166.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 9924 | -0.004 | +260.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 9924 | -0.004 | +260.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 10814 | +0.017 | +545.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 10814 | +0.017 | +545.43€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6921 | -0.056 | -141.12€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6921 | -0.056 | -141.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1237 | -0.002 | -17.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1237 | -0.002 | -17.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1905 | -0.069 | -33.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1905 | -0.069 | -33.92€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 66 | -0.015 | -0.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 66 | -0.015 | -0.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 791 | -0.119 | -33.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 791 | -0.119 | -33.96€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2064 | -0.070 | -29.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2064 | -0.070 | -29.98€ | 3 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 144466 | -0.077 | +1957.02€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 144466 | -0.077 | +1957.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 25205 | -0.078 | +1356.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 25205 | -0.078 | +1356.18€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 21675 | -0.100 | -1048.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 21675 | -0.100 | -1048.49€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 25525 | -0.069 | +1213.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 25525 | -0.069 | +1213.33€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 21220 | -0.097 | -628.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 21220 | -0.097 | -628.89€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 25894 | -0.057 | +349.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 25894 | -0.057 | +349.21€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 24947 | -0.069 | +715.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 24947 | -0.069 | +715.69€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8936 | -0.035 | -185.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8936 | -0.035 | -185.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1002 | -0.017 | -19.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1002 | -0.017 | -19.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2057 | -0.047 | -29.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2057 | -0.047 | -29.28€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2623 | -0.026 | -40.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2623 | -0.026 | -40.54€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1242 | -0.061 | -32.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1242 | -0.061 | -32.36€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1003 | -0.030 | -32.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1003 | -0.030 | -32.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 1902 | +0.120 | +758.01€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1766 | +0.125 | +745.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 416 | +0.120 | +179.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 416 | +0.120 | +179.53€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 369 | +0.115 | +125.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 369 | +0.115 | +125.43€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#ETH | 338 | +0.138 | +168.70€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 338 | +0.138 | +168.70€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 307 | +0.150 | +168.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 307 | +0.150 | +168.50€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 336 | +0.104 | +103.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 336 | +0.104 | +103.26€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1783 | -0.017 | -19.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1783 | -0.017 | -19.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 339 | +0.002 | +12.11€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 339 | +0.002 | +12.11€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 324 | -0.037 | -13.06€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 324 | -0.037 | -13.06€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 454 | -0.040 | -29.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 454 | -0.040 | -29.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 371 | +0.004 | +3.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 371 | +0.004 | +3.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 295 | -0.005 | +6.82€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 295 | -0.005 | +6.82€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1016 | -0.074 | -46.99€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 470 | -0.108 | -79.05€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 368 | -0.132 | -64.97€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 102 | -0.019 | -14.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 356 | -0.034 | +24.17€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 258 | -0.023 | +27.75€ | 2 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 98 | -0.060 | -3.59€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 190 | -0.062 | +7.89€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 158 | -0.069 | +4.02€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 32 | -0.029 | +3.88€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 784 | -0.084 | -33.20€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 232 | -0.038 | -13.79€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1263 | -0.208 | -81.23€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 494 | -0.210 | -48.82€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 436 | -0.212 | -48.08€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 58 | -0.183 | -0.74€ | 1 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 424 | -0.214 | -37.57€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 375 | -0.224 | -44.07€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 49 | -0.128 | +6.50€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 345 | -0.197 | +5.16€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 322 | -0.194 | +2.44€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 23 | -0.220 | +2.71€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1133 | -0.212 | -89.70€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 130 | -0.174 | +8.47€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 497 | +0.390 | +469.54€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 84 | +0.174 | +61.71€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 84 | +0.174 | +61.71€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#ETH | 114 | +0.362 | +101.57€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 114 | +0.362 | +101.57€ | 0 | 6 |
| ✅ RESOLUTION_SNIPER#SOL | 299 | +0.457 | +306.27€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 299 | +0.457 | +306.27€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 497 | +0.390 | +469.54€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 820 | +0.039 | +68.02€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 820 | +0.039 | +68.02€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 310 | +0.026 | +5.92€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 310 | +0.026 | +5.92€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 68 | +0.000 | -0.29€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 68 | +0.000 | -0.29€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 81 | +0.018 | +6.10€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 81 | +0.018 | +6.10€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 361 | +0.062 | +56.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 361 | +0.062 | +56.30€ | 0 | 4 |
| ✅ STREAK_FADE_5M | 3537 | -0.023 | -142.97€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3537 | -0.023 | -142.97€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 600 | -0.030 | -28.00€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 600 | -0.030 | -28.00€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 169 | -0.038 | -13.78€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 169 | -0.038 | -13.78€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1641 | -0.020 | -60.99€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1641 | -0.020 | -60.99€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 109 | -0.041 | -8.88€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 109 | -0.041 | -8.88€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 43 | -0.100 | -5.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 43 | -0.100 | -5.07€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 66 | +0.000 | -3.81€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 66 | +0.000 | -3.81€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 11384 | +0.015 | +78.79€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11384 | +0.015 | +78.79€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2941 | +0.019 | +26.58€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2941 | +0.019 | +26.58€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2954 | +0.018 | +36.86€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2954 | +0.018 | +36.86€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2910 | +0.009 | -1.79€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2910 | +0.009 | -1.79€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2579 | +0.013 | +17.14€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2579 | +0.013 | +17.14€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 10615 | +0.014 | -43.85€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 10615 | +0.014 | -43.85€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4421 | +0.020 | -1.85€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4421 | +0.020 | -1.85€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3628 | +0.010 | -28.96€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3628 | +0.010 | -28.96€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2566 | +0.010 | -13.04€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2566 | +0.010 | -13.04€ | 1 | 0 |
| ✅ UPDOWN_GBM | 88822 | +0.056 | +8034.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 21480 | +0.083 | +4595.64€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2795 | +0.002 | +31.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 58915 | +0.055 | +3316.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 5317 | +0.003 | +93.62€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 7166 | +0.093 | +1168.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1601 | +0.159 | +719.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 79 | -0.006 | -1.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5486 | +0.076 | +450.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 20437 | +0.057 | +1774.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2970 | +0.085 | +683.50€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 784 | +0.004 | +14.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 14171 | +0.065 | +1006.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2399 | +0.001 | +67.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 113 | -0.074 | +2.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 9390 | +0.072 | +990.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1580 | +0.147 | +621.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 7732 | +0.057 | +370.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 21198 | +0.048 | +1435.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 5276 | +0.072 | +801.13€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 752 | +0.007 | +18.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 13119 | +0.048 | +594.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1945 | +0.005 | +18.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 106 | -0.102 | +2.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 19215 | +0.036 | +1048.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 5534 | +0.036 | +444.56€ | 0 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 713 | -0.011 | +2.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 11901 | +0.043 | +599.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 973 | +0.004 | +7.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 94 | -0.135 | -6.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 11414 | +0.069 | +1619.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4519 | +0.102 | +1325.41€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 389 | +0.009 | -0.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 6506 | +0.049 | +294.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 313 | -0.103 | -0.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 925 | +0.365 | +338.24€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 925 | +0.365 | +338.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 466 | +0.361 | +160.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 466 | +0.361 | +160.58€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 459 | +0.368 | +177.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 459 | +0.368 | +177.65€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 21838 | -0.022 | +5241.88€ | 2 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 21838 | -0.022 | +5241.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1752 | -0.054 | +517.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1752 | -0.054 | +517.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 4106 | -0.114 | +184.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 4106 | -0.114 | +184.20€ | 3 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 964 | +0.215 | +782.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 964 | +0.215 | +782.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2861 | +0.220 | +1837.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2861 | +0.220 | +1837.71€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 6225 | -0.061 | +857.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 6225 | -0.061 | +857.76€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5930 | -0.064 | +1062.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5930 | -0.064 | +1062.70€ | 2 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 266 | +0.063 | +25.42€ | 0 | 7 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 266 | +0.063 | +25.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 266 | +0.063 | +25.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 266 | +0.063 | +25.42€ | 0 | 7 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1625 | +0.287 | +1368.07€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1625 | +0.287 | +1368.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 865 | +0.281 | +681.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 865 | +0.281 | +681.44€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 760 | +0.293 | +686.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 760 | +0.293 | +686.63€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 843 | -0.114 | -85.50€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#5min | 843 | -0.114 | -85.50€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 259 | -0.086 | -20.70€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 259 | -0.086 | -20.70€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 94 | -0.167 | -10.43€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 94 | -0.167 | -10.43€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 107 | -0.179 | -5.02€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 107 | -0.179 | -5.02€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 4106 | +0.302 | +1898.98€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1536 | +0.258 | +185.68€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1577 | +0.295 | +682.40€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 993 | +0.380 | +1030.90€ | 0 | 1 |