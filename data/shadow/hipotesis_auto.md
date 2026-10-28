# Hipótesis automáticas — 2026-10-28 20:04 UTC
_Generado por shadow_postmortem.py sobre 1095518 resoluciones (PNL=+144938.56€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.227 (n=860)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.136)

- **PATRÓN** `n_total_lado` > `64.0` → IC=+0.184 (n=302)

  - _Acción_: Kelly boost +0.92€ cuando `n_total_lado` > 64.0 (IC base=+0.136)

- **PATRÓN** `banda_hit_calibrado` > `0.6174` → IC=+0.261 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6174 (IC base=+0.136)

- **PATRÓN** `banda_z` > `8.894` → IC=+0.212 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.894 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=328)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.136 (n=438)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 8.0 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=980)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `2655.6606` → IC=+0.139 (n=804)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2655.6606 (IC base=+0.136)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.223 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.140)

- **PATRÓN** `n_total_lado` > `67.0` → IC=+0.194 (n=263)

  - _Acción_: Kelly boost +0.97€ cuando `n_total_lado` > 67.0 (IC base=+0.140)

- **PATRÓN** `banda_hit_calibrado` > `0.614` → IC=+0.254 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.614 (IC base=+0.140)

- **PATRÓN** `banda_z` > `9.249` → IC=+0.199 (n=257)

  - _Acción_: Kelly boost +0.99€ cuando `banda_z` > 9.249 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=277)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.149 (n=881)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `3049.8849` → IC=+0.142 (n=689)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 3049.8849 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `9372.1171` → IC=+0.127 (n=210)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 9372.1171 (IC base=+0.012)

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
- **FILTRO** `restante_s_al_confirmar` < `138.25` → IC=-0.209 (n=10784)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 138.25
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=32357)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `127.47` → IC=-0.261 (n=1152)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.47
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=3458)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `118.95` → IC=-0.296 (n=1143)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 118.95
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3431)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `160.65` → IC=-0.241 (n=2889)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 160.65
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=8668)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `132.81` → IC=-0.259 (n=2076)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.81
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=6231)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.214 (n=23871)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.106)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.124 (n=4618)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `8758.4418` → IC=+0.166 (n=2123)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 8758.4418 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.126 (n=20520)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.130 (n=36903)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 11.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.226 (n=19053)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=7640)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `6799.9463` → IC=+0.154 (n=2957)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 6799.9463 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=2111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.364 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.186 (n=2585)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `16451.0129` → IC=+0.185 (n=671)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 16451.0129 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.187 (n=1849)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.185 (n=2069)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` < `0.295` → IC=+0.312 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.295 (IC base=+0.181)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=2651)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `16197.5868` → IC=+0.187 (n=684)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 16197.5868 (IC base=+0.181)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.170 (n=519)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.61 (IC base=+0.078)

- **PATRÓN** `libro_liquidez` > `7474.4764` → IC=+0.163 (n=99)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 7474.4764 (IC base=+0.078)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.140 (n=1220)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.44 (IC base=+0.082)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=4631)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.165 (n=3923)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 15.0 (IC base=+0.162)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.375 (n=1499)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.215 (n=2079)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.207)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.351 (n=770)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.211 (n=2413)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.207)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=1170)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.149 (n=997)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 15.0 (IC base=+0.144)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.263 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.145 (n=1283)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `2222.7955` → IC=+0.156 (n=507)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2222.7955 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.162 (n=152)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.069)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.253 (n=886)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1242)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.146 (n=1344)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=701)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.145)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.286 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=894)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.145)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `py_entrada` > `0.555` → IC=+0.170 (n=431)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.555 (IC base=+0.084)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.132 (n=1294)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.244 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.124)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.297 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=140)

- **FILTRO** `py_entrada` > `0.825` → IC=-0.343 (n=49)

  - _Acción_: SKIP cuando `py_entrada` > 0.825
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=163)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=20462)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.201 (n=17348)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.232 (n=8441)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.181 (n=2220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.179 (n=4676)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 18.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.182 (n=4536)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.177 (n=3877)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` > 0.71 (IC base=+0.177)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.221 (n=2562)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.223 (n=1711)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.298 (n=855)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.219)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=4607)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.181 (n=3918)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.188 (n=3591)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.255 (n=3952)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.247)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.248 (n=3354)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.247)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.358 (n=1324)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=4522)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.190 (n=3858)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.192 (n=3355)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.187)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.431 (n=859)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.426)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.426 (n=868)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.441 (n=874)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.433 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `4341.1458` → IC=+0.443 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4341.1458 (IC base=+0.426)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.436 (n=342)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.438)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.441 (n=352)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.450 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

- **PATRÓN** `libro_liquidez` > `20878.8113` → IC=+0.447 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 20878.8113 (IC base=+0.438)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.436 (n=312)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.428)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.430 (n=340)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.428)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.442 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.428)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.434 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.428)

- **PATRÓN** `libro_liquidez` > `4630.3169` → IC=+0.447 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4630.3169 (IC base=+0.428)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.404 (n=144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.400)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.402 (n=141)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.400)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.428 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.400)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.765` → IC=-0.294 (n=32)

  - _Acción_: SKIP cuando `py_entrada` > 0.765
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=12)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=28)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=26609)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=26856)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.201)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.191 (n=4582)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.185 (n=8508)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 12.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.198 (n=12036)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.71 (IC base=+0.184)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=11185)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.225 (n=5449)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.286 (n=3848)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.188 (n=4568)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.201 (n=9379)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.229 (n=5597)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.274 (n=3781)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.207 (n=10197)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.261 (n=3939)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.207 (n=4424)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=4430)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.248 (n=4642)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=9583)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=9709)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.64` → IC=+0.136 (n=11633)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.64 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=4716)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.144 (n=4417)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.128 (n=5822)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `2.66` → IC=+0.145 (n=4384)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.66 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.190 (n=4867)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.115)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=5292)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.115)

- **PATRÓN** `lag_apertura_s` < `3.26` → IC=+0.137 (n=5847)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.26 (IC base=+0.115)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.302 (n=1806)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.388 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `3842.7655` → IC=+0.294 (n=771)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3842.7655 (IC base=+0.293)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.289 (n=821)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.280)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.363 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `5103.0716` → IC=+0.295 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5103.0716 (IC base=+0.280)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.325 (n=587)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.299)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.302 (n=857)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.299)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.397 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.299)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.300 (n=972)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.299)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.333 (n=88)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.337)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.365 (n=87)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.337)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.388 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.337)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.357 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.337)

- **PATRÓN** `libro_liquidez` > `745.0217` → IC=+0.364 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 745.0217 (IC base=+0.337)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.448 (n=830)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.444)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.445 (n=818)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.444)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.451 (n=794)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.444)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.440 (n=395)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.437)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.437 (n=269)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.438 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.442 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.437)

- **PATRÓN** `libro_liquidez` > `5497.3627` → IC=+0.445 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5497.3627 (IC base=+0.437)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.470 (n=133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.453)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.456 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.453)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.455 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.453)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.452 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.453)

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
- **FILTRO** `hora_utc` < `5.0` → IC=-0.283 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=100)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.287 (n=59)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=62)

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
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=100)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.287 (n=59)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=62)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4714` → IC=+0.140 (n=14957)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4714 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.126 (n=15123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=10427)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.9804` → IC=+0.248 (n=4988)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9804 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.776` → IC=+0.277 (n=831)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.776 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.626` → IC=+0.182 (n=7451)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 3.626 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6217` → IC=+0.267 (n=4386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6217 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.3044` → IC=+0.246 (n=1543)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3044 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.3569` → IC=+0.231 (n=4845)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3569 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=7671)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `4457.7867` → IC=+0.151 (n=4985)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4457.7867 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.567` → IC=+0.142 (n=18552)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.567 (IC base=+0.078)

- **PATRÓN** `dist_vwap_pct` > `0.6039` → IC=+0.187 (n=1219)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.6039 (IC base=+0.078)

- **PATRÓN** `volumen_regimen` < `0.6977` → IC=+0.191 (n=3259)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.6977 (IC base=+0.078)

- **PATRÓN** `volumen_pendiente_norm` > `0.2976` → IC=+0.229 (n=1829)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2976 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` > `2.6905` → IC=+0.207 (n=4189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6905 (IC base=+0.078)

- **PATRÓN** `ballena_activa_n` < `105.0` → IC=+0.224 (n=12444)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 105.0 (IC base=+0.078)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.209 (n=1077)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.3551` → IC=+0.208 (n=3230)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3551 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.217 (n=1569)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.212 (n=2166)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `0.9846` → IC=+0.280 (n=1465)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9846 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.693` → IC=+0.281 (n=1430)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.693 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.2838` → IC=+0.259 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2838 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `1.5518` → IC=+0.209 (n=2760)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5518 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=3515)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `2046.45` → IC=+0.208 (n=1077)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2046.45 (IC base=+0.206)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.226 (n=2012)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.244 (n=2755)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0093 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.0873` → IC=+0.278 (n=920)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0873 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.255 (n=1013)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.5484` → IC=+0.259 (n=2756)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5484 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` < `0.0961` → IC=+0.245 (n=2482)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0961 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.2932` → IC=+0.260 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2932 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.447` → IC=+0.243 (n=871)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.447 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `1.8746` → IC=+0.244 (n=1742)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8746 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.243 (n=3140)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1527.7502` → IC=+0.243 (n=2461)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1527.7502 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.240 (n=1179)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.241)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.239 (n=891)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.229)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.232 (n=1216)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.1057` → IC=+0.257 (n=1176)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1057 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.241 (n=2797)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` > `0.9314` → IC=+0.273 (n=891)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9314 (IC base=+0.229)

- **PATRÓN** `dist_vwap_pct` > `0.187` → IC=+0.236 (n=1265)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.187 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.216` → IC=+0.261 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.216 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` < `1.231` → IC=+0.229 (n=2673)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.231 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` > `0.6235` → IC=+0.233 (n=2673)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6235 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.2805` → IC=+0.276 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2805 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `2.4384` → IC=+0.258 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4384 (IC base=+0.229)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.151 (n=2825)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0059 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.0761` → IC=+0.166 (n=940)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0761 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.155 (n=1052)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.7204` → IC=+0.171 (n=2820)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.7204 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.908` → IC=+0.140 (n=459)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 10.908 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.076` → IC=+0.136 (n=2574)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 4.076 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `1.2046` → IC=+0.139 (n=2821)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.2046 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.154 (n=1023)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `2.4537` → IC=+0.140 (n=2697)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.4537 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `208.0` → IC=+0.173 (n=1162)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 208.0 (IC base=+0.130)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.215 (n=1130)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=3557)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.266 (n=1307)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.146` → IC=+0.279 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.146 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.198 (n=3012)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.3528` → IC=+0.219 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3528 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.712` → IC=+0.210 (n=1493)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.712 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.199 (n=4049)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `2029.82` → IC=+0.203 (n=1128)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2029.82 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.222 (n=2708)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0109 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.1771` → IC=+0.232 (n=1354)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1771 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=1155)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.0323` → IC=+0.268 (n=1026)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0323 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.156` → IC=+0.256 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.156 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3488` → IC=+0.261 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3488 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.7601` → IC=+0.225 (n=1331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7601 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.222 (n=1544)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `1916.24` → IC=+0.218 (n=1393)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1916.24 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.217 (n=2557)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.141 (n=165)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=4094)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.146 (n=772)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0043 (IC base=+0.059)

- **PATRÓN** `ibs_20min` > `0.9538` → IC=+0.234 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9538 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.137` → IC=+0.336 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.137 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.218` → IC=+0.198 (n=1267)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 5.218 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` > `0.693` → IC=+0.341 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.693 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` < `0.0777` → IC=+0.331 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0777 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.3054` → IC=+0.340 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3054 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` < `1.4175` → IC=+0.347 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4175 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` > `2.2749` → IC=+0.338 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2749 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `144.0` → IC=+0.335 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 144.0 (IC base=+0.059)

- **PATRÓN** `ibs_20min` < `0.0921` → IC=+0.182 (n=1065)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.0921 (IC base=+0.042)

- **PATRÓN** `dist_vwap_pct` > `0.7306` → IC=+0.160 (n=245)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.7306 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` < `0.8397` → IC=+0.155 (n=1307)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8397 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.2866` → IC=+0.210 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2866 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` < `1.7849` → IC=+0.144 (n=1256)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.7849 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` > `2.1656` → IC=+0.162 (n=854)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.1656 (IC base=+0.042)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.169 (n=119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=633)

- **FILTRO** `ibs_20min` > `0.2105` → IC=-0.134 (n=3995)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2105
  - _Potencial_: sin este filtro IC_bueno=+0.149 (n=1973)

- **FILTRO** `sigma_ewma_delta_pct` > `8.557` → IC=-0.231 (n=638)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.557
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=5330)

- **PATRÓN** `ibs_20min` > `0.8889` → IC=+0.196 (n=189)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.8889 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` > `0.9817` → IC=+0.293 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9817 (IC base=+0.028)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.1` → IC=+0.140 (n=234)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 3.1 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` > `1.0454` → IC=+0.297 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0454 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` < `0.1622` → IC=+0.288 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1622 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` < `2.4948` → IC=+0.297 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4948 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` > `1.5504` → IC=+0.269 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5504 (IC base=+0.028)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.279 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.028)

- **PATRÓN** `ibs_20min` < `0.2105` → IC=+0.149 (n=1973)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.2105 (IC base=-0.040)

- **PATRÓN** `volumen_regimen` < `0.6932` → IC=+0.305 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6932 (IC base=-0.040)

- **PATRÓN** `volumen_pendiente_norm` < `0.1046` → IC=+0.289 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1046 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` < `2.4345` → IC=+0.303 (n=771)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4345 (IC base=-0.040)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.5954` → IC=-0.177 (n=1117)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.5954
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3353)

- **FILTRO** `ibs_20min` < `0.7634` → IC=-0.153 (n=2949)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7634
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=1521)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.166 (n=1047)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=3423)

- **FILTRO** `ibs_20min` > `0.7479` → IC=-0.200 (n=1588)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7479
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=4765)

- **PATRÓN** `dist_vwap_pct` > `0.7251` → IC=+0.343 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7251 (IC base=-0.064)

- **PATRÓN** `dist_vwap_pct` < `0.2444` → IC=+0.306 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2444 (IC base=-0.064)

- **PATRÓN** `volumen_regimen` > `0.7047` → IC=+0.319 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7047 (IC base=-0.064)

- **PATRÓN** `volumen_pendiente_norm` < `0.1024` → IC=+0.305 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1024 (IC base=-0.064)

- **PATRÓN** `volumen_pendiente_norm` > `0.1669` → IC=+0.301 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1669 (IC base=-0.064)

- **PATRÓN** `volumen_spike_ratio` < `1.4239` → IC=+0.318 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4239 (IC base=-0.064)

- **PATRÓN** `volumen_spike_ratio` > `1.8567` → IC=+0.312 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8567 (IC base=-0.064)

- **PATRÓN** `dist_vwap_pct` > `0.8075` → IC=+0.284 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8075 (IC base=-0.002)

- **PATRÓN** `volumen_regimen` < `0.725` → IC=+0.267 (n=789)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.725 (IC base=-0.002)

- **PATRÓN** `volumen_regimen` > `1.0669` → IC=+0.284 (n=813)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0669 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.1688` → IC=+0.287 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1688 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` < `2.1737` → IC=+0.265 (n=1468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1737 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.264 (n=1668)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=-0.002)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.209 (n=6518)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.093)

- **PATRÓN** `ibs_20min` > `0.3103` → IC=+0.167 (n=19531)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.3103 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.9319` → IC=+0.301 (n=1403)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9319 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.572` → IC=+0.165 (n=8738)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 3.572 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` < `1.1737` → IC=+0.267 (n=7190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1737 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` > `0.6916` → IC=+0.275 (n=6425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6916 (IC base=+0.093)

- **PATRÓN** `volumen_pendiente_norm` > `0.2404` → IC=+0.286 (n=2160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2404 (IC base=+0.093)

- **PATRÓN** `volumen_spike_ratio` > `2.2806` → IC=+0.278 (n=5181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2806 (IC base=+0.093)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.302 (n=11016)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 91.0 (IC base=+0.093)

- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.156 (n=6292)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0096 (IC base=+0.076)

- **PATRÓN** `ibs_20min` < `0.65` → IC=+0.147 (n=18860)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.65 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` < `0.7044` → IC=+0.268 (n=2675)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7044 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` > `1.195` → IC=+0.266 (n=2026)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.195 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.295` → IC=+0.319 (n=1316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.295 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` < `1.5813` → IC=+0.295 (n=3878)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5813 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` > `2.2822` → IC=+0.287 (n=3994)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2822 (IC base=+0.076)

- **PATRÓN** `ballena_activa_n` < `76.0` → IC=+0.299 (n=8771)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 76.0 (IC base=+0.076)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.5794` → IC=-0.152 (n=2651)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5794
  - _Potencial_: sin este filtro IC_bueno=+0.203 (n=2652)

- **FILTRO** `ibs_20min` > `0.7286` → IC=-0.221 (n=1143)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7286
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=3431)

- **FILTRO** `sigma_ewma_delta_pct` > `4.293` → IC=-0.220 (n=991)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.293
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=3583)

- **PATRÓN** `ibs_20min` > `0.9275` → IC=+0.331 (n=1327)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9275 (IC base=+0.025)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.111` → IC=+0.183 (n=1777)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 3.111 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.2294` → IC=+0.315 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2294 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.449` → IC=+0.263 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.449 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` > `2.2629` → IC=+0.290 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2629 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.306 (n=1161)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.025)

- **PATRÓN** `ibs_20min` < `0.1702` → IC=+0.162 (n=1147)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.1702 (IC base=-0.028)

- **PATRÓN** `volumen_pendiente_norm` < `0.0738` → IC=+0.416 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0738 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` < `2.6875` → IC=+0.410 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6875 (IC base=-0.028)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.404 (n=716)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=-0.028)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.2954` → IC=+0.222 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2954 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` < `1.1961` → IC=+0.204 (n=1921)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1961 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` > `0.6925` → IC=+0.208 (n=1717)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6925 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.2788` → IC=+0.251 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2788 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` < `1.4262` → IC=+0.229 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4262 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` > `2.4623` → IC=+0.207 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4623 (IC base=+0.020)

- **PATRÓN** `ballena_activa_n` < `268.0` → IC=+0.239 (n=1268)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 268.0 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` < `1.1685` → IC=+0.235 (n=1295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1685 (IC base=-0.003)

- **PATRÓN** `volumen_regimen` > `0.6209` → IC=+0.239 (n=1295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6209 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2716` → IC=+0.299 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2716 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.5381` → IC=+0.249 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5381 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.1598` → IC=+0.251 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1598 (IC base=-0.003)

- **PATRÓN** `ballena_activa_n` < `194.0` → IC=+0.244 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 194.0 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.323 (n=936)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.275)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.283 (n=2803)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.275)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.316 (n=1510)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.275)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.672` → IC=+0.305 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.672 (IC base=+0.275)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.288 (n=2446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.275)

- **PATRÓN** `volumen_spike_ratio` > `1.6104` → IC=+0.280 (n=2713)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6104 (IC base=+0.275)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.284 (n=3326)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.275)

- **PATRÓN** `libro_liquidez` > `2028.6484` → IC=+0.289 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2028.6484 (IC base=+0.275)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.295 (n=1716)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.275)

- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.323 (n=1648)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0087 (IC base=+0.296)

- **PATRÓN** `drift_60min` |x|≤ `0.1781` → IC=+0.315 (n=1087)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1781 (IC base=+0.296)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.321 (n=938)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.296)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.299 (n=854)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.296)

- **PATRÓN** `ibs_20min` < `0.376` → IC=+0.297 (n=2469)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.376 (IC base=+0.296)

- **PATRÓN** `ibs_20min` > `0.1304` → IC=+0.303 (n=1650)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1304 (IC base=+0.296)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.364` → IC=+0.306 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.364 (IC base=+0.296)

- **PATRÓN** `volumen_pendiente_norm` < `0.1975` → IC=+0.295 (n=2425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1975 (IC base=+0.296)

- **PATRÓN** `volumen_pendiente_norm` > `0.3431` → IC=+0.312 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3431 (IC base=+0.296)

- **PATRÓN** `volumen_spike_ratio` < `1.7322` → IC=+0.302 (n=1042)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7322 (IC base=+0.296)

- **PATRÓN** `volumen_spike_ratio` > `2.7006` → IC=+0.309 (n=1074)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7006 (IC base=+0.296)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.298 (n=1247)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.296)

- **PATRÓN** `libro_liquidez` > `1918.1184` → IC=+0.303 (n=1119)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1918.1184 (IC base=+0.296)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.305 (n=1101)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.296)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7352` → IC=-0.184 (n=1202)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7352
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=3618)

- **PATRÓN** `ibs_20min` > `0.8669` → IC=+0.165 (n=1166)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.8669 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.1489` → IC=+0.230 (n=866)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1489 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.2131` → IC=+0.232 (n=1435)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2131 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `1.0082` → IC=+0.236 (n=1457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0082 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `0.6686` → IC=+0.233 (n=1479)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6686 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.1021` → IC=+0.244 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1021 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.4665` → IC=+0.236 (n=1603)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4665 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `119.0` → IC=+0.252 (n=1634)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 119.0 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `1.0212` → IC=+0.243 (n=1020)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0212 (IC base=+0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2825` → IC=+0.300 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2825 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.794` → IC=+0.274 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.794 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.4415` → IC=+0.260 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4415 (IC base=+0.002)

- **PATRÓN** `ballena_activa_n` < `121.0` → IC=+0.263 (n=1124)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 121.0 (IC base=+0.002)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.75` → IC=-0.232 (n=2018)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.310 (n=2046)

- **FILTRO** `ibs_20min` > `0.6364` → IC=-0.234 (n=984)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6364
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=2960)

- **FILTRO** `sigma_ewma_delta_pct` > `8.409` → IC=-0.252 (n=453)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.409
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=3491)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.310 (n=2046)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.75 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` > `0.213` → IC=+0.343 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.213 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.357` → IC=+0.192 (n=634)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 9.357 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` < `0.8491` → IC=+0.339 (n=1002)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8491 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` > `0.7014` → IC=+0.335 (n=1343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7014 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` < `0.1601` → IC=+0.331 (n=1556)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1601 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.354 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.353 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.041)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.349 (n=1292)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 47.0 (IC base=+0.041)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.129 (n=2960)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.6364 (IC base=+0.038)

- **PATRÓN** `volumen_regimen` < `0.6965` → IC=+0.272 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6965 (IC base=+0.038)

- **PATRÓN** `volumen_pendiente_norm` < `0.1591` → IC=+0.242 (n=1434)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1591 (IC base=+0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.259 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` < `2.4528` → IC=+0.253 (n=1331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4528 (IC base=+0.038)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.268 (n=1364)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=+0.038)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.353 (n=1887)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.309)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.314 (n=819)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.309)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.316 (n=1005)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.309)

- **PATRÓN** `ibs_20min` > `0.7632` → IC=+0.345 (n=1887)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7632 (IC base=+0.309)

- **PATRÓN** `dist_vwap_pct` > `0.2028` → IC=+0.334 (n=1175)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2028 (IC base=+0.309)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.847` → IC=+0.327 (n=1022)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.847 (IC base=+0.309)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.14` → IC=+0.310 (n=2406)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.14 (IC base=+0.309)

- **PATRÓN** `volumen_regimen` > `0.8688` → IC=+0.330 (n=1408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8688 (IC base=+0.309)

- **PATRÓN** `volumen_pendiente_norm` > `0.2809` → IC=+0.350 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2809 (IC base=+0.309)

- **PATRÓN** `volumen_spike_ratio` > `1.4319` → IC=+0.322 (n=2028)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4319 (IC base=+0.309)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.342 (n=1648)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.309)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.341 (n=1497)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.310)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.318 (n=1125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.310)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.311 (n=1100)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.310)

- **PATRÓN** `ibs_20min` < `0.3778` → IC=+0.332 (n=2244)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3778 (IC base=+0.310)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.619` → IC=+0.325 (n=834)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.619 (IC base=+0.310)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.095` → IC=+0.311 (n=2669)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.095 (IC base=+0.310)

- **PATRÓN** `volumen_regimen` < `0.7229` → IC=+0.315 (n=988)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7229 (IC base=+0.310)

- **PATRÓN** `volumen_regimen` > `1.2164` → IC=+0.340 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2164 (IC base=+0.310)

- **PATRÓN** `volumen_pendiente_norm` > `0.2843` → IC=+0.363 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2843 (IC base=+0.310)

- **PATRÓN** `volumen_spike_ratio` < `1.4152` → IC=+0.323 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4152 (IC base=+0.310)

- **PATRÓN** `volumen_spike_ratio` > `2.1375` → IC=+0.310 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1375 (IC base=+0.310)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.227 (n=4848)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.1211` → IC=+0.196 (n=6393)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1211 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=15076)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `0.5517` → IC=+0.233 (n=14525)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5517 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `0.1627` → IC=+0.207 (n=5740)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1627 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.235` → IC=+0.255 (n=3779)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.235 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `1.1872` → IC=+0.162 (n=9646)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1872 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` > `0.6248` → IC=+0.160 (n=9645)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6248 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2946` → IC=+0.207 (n=2111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2946 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `2.6126` → IC=+0.191 (n=4704)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6126 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.196 (n=13442)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 90.0 (IC base=+0.178)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.189 (n=6184)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0055 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.0793` → IC=+0.226 (n=4676)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0793 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=5218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.5135` → IC=+0.238 (n=14028)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5135 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.857` → IC=+0.196 (n=2270)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 9.857 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.52` → IC=+0.185 (n=13098)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 3.52 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `1.1825` → IC=+0.165 (n=10004)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1825 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2959` → IC=+0.223 (n=2086)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2959 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `1.5644` → IC=+0.181 (n=5830)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.5644 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6495` → IC=+0.188 (n=4417)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6495 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.195 (n=12991)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 96.0 (IC base=+0.182)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.224 (n=810)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.3404` → IC=+0.235 (n=2420)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3404 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.233 (n=896)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.229 (n=1640)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.9352` → IC=+0.296 (n=1614)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9352 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.749` → IC=+0.330 (n=769)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.749 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.2817` → IC=+0.281 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2817 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `1.8416` → IC=+0.219 (n=1533)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8416 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `1.5436` → IC=+0.225 (n=2053)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5436 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.234 (n=2656)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.233 (n=1433)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.0932` → IC=+0.305 (n=834)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0932 (IC base=+0.255)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.261 (n=1958)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.255)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.255 (n=1744)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.255)

- **PATRÓN** `ibs_20min` < `0.0333` → IC=+0.303 (n=834)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0333 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` < `0.1008` → IC=+0.261 (n=1661)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1008 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` > `0.3012` → IC=+0.280 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3012 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` < `1.4441` → IC=+0.276 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4441 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` > `2.7271` → IC=+0.256 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7271 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.258 (n=2162)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `1526.2954` → IC=+0.259 (n=1692)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1526.2954 (IC base=+0.255)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.261 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.255)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.208 (n=731)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.064` → IC=+0.192 (n=732)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.064 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=2298)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.314` → IC=+0.217 (n=2189)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.314 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.1859` → IC=+0.219 (n=1157)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1859 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.113` → IC=+0.214 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.113 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.6938` → IC=+0.159 (n=963)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.6938 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` > `1.0626` → IC=+0.151 (n=993)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.0626 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.2838` → IC=+0.189 (n=342)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2838 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `1.413` → IC=+0.169 (n=717)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.413 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `2.4826` → IC=+0.162 (n=716)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.4826 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `412.0` → IC=+0.151 (n=2110)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 412.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.174 (n=2302)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0059 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.2345` → IC=+0.175 (n=2024)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2345 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.185 (n=1096)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.6153` → IC=+0.208 (n=2299)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6153 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.302` → IC=+0.187 (n=436)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 11.302 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.171` → IC=+0.150 (n=1999)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.171 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.204` → IC=+0.163 (n=2300)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.204 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` < `0.0938` → IC=+0.153 (n=1977)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.0938 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.4919` → IC=+0.153 (n=2177)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4919 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `221.0` → IC=+0.183 (n=936)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 221.0 (IC base=+0.148)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.237 (n=1117)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.3972` → IC=+0.224 (n=2165)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3972 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.234 (n=903)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=1291)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.287` → IC=+0.303 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.287 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.212 (n=2129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.3532` → IC=+0.232 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3532 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.766` → IC=+0.211 (n=1053)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.766 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.7141` → IC=+0.225 (n=1085)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7141 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.216 (n=2939)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `1919.72` → IC=+0.224 (n=1116)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1919.72 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.241 (n=1874)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.4185` → IC=+0.256 (n=1873)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4185 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.278 (n=800)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0243` → IC=+0.290 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0243 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.274` → IC=+0.277 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.274 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.3585` → IC=+0.287 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3585 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.7621` → IC=+0.235 (n=899)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7621 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.1717` → IC=+0.239 (n=1361)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1717 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.234 (n=1092)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1911.8798` → IC=+0.243 (n=965)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1911.8798 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.239 (n=1392)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.234)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.199 (n=1042)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.0783` → IC=+0.198 (n=789)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.0783 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=2454)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.2902` → IC=+0.203 (n=2367)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2902 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.142` → IC=+0.191 (n=1404)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.142 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.649` → IC=+0.194 (n=538)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 9.649 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.0223` → IC=+0.147 (n=2083)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.0223 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.1028` → IC=+0.174 (n=963)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1028 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.83` → IC=+0.143 (n=1547)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.83 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `2.5287` → IC=+0.162 (n=774)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.5287 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `7047.0195` → IC=+0.198 (n=1073)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 7047.0195 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `133.0` → IC=+0.147 (n=2304)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 133.0 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.156 (n=2506)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0073 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.3903` → IC=+0.146 (n=2503)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3903 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.168 (n=1190)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 15.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.6746` → IC=+0.187 (n=2503)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6746 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.53` → IC=+0.153 (n=607)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 9.53 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.8551` → IC=+0.159 (n=1669)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8551 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.3002` → IC=+0.193 (n=379)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.3002 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.8129` → IC=+0.139 (n=1572)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.8129 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `2.5558` → IC=+0.135 (n=786)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.5558 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `6451.777` → IC=+0.186 (n=1135)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 6451.777 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `111.0` → IC=+0.137 (n=2039)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 111.0 (IC base=+0.130)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.174 (n=1202)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0107 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.162 (n=1275)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 15.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.4815` → IC=+0.213 (n=2653)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4815 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.1937` → IC=+0.190 (n=1497)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1937 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.305` → IC=+0.287 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.305 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `1.1761` → IC=+0.135 (n=2652)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.1761 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.7063` → IC=+0.125 (n=2369)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.7063 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` < `0.1638` → IC=+0.131 (n=2709)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1638 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.549` → IC=+0.138 (n=1134)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.549 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.126 (n=2762)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2658.6025` → IC=+0.202 (n=1202)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2658.6025 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.141 (n=1132)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 22.0 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0113` → IC=+0.143 (n=2732)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0113 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.1087` → IC=+0.169 (n=911)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1087 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=2786)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.6235` → IC=+0.218 (n=2728)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6235 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.411` → IC=+0.137 (n=2404)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 2.411 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.1845` → IC=+0.129 (n=2729)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.1845 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.1651` → IC=+0.123 (n=2657)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1651 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.278` → IC=+0.135 (n=376)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.278 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4426` → IC=+0.127 (n=854)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.4426 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `2.4628` → IC=+0.125 (n=853)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 2.4628 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2531.8614` → IC=+0.185 (n=1237)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2531.8614 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.124 (n=2523)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 47.0 (IC base=+0.119)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.247 (n=2179)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.1682` → IC=+0.236 (n=1074)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1682 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.226 (n=2531)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=2187)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.6604` → IC=+0.255 (n=2440)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6604 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` > `0.1805` → IC=+0.230 (n=1544)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1805 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.643` → IC=+0.258 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.643 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `1.1704` → IC=+0.223 (n=2440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1704 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `0.6235` → IC=+0.230 (n=2439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6235 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.2322` → IC=+0.268 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2322 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `2.4647` → IC=+0.225 (n=2377)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4647 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `1.8099` → IC=+0.234 (n=1585)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8099 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.224 (n=3178)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `2109.3296` → IC=+0.225 (n=2439)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2109.3296 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.237 (n=1090)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.234)

- **PATRÓN** `sigma_h` > `0.0226` → IC=+0.243 (n=1125)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0226 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.0881` → IC=+0.260 (n=826)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0881 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.253 (n=1202)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.237 (n=1109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.4309` → IC=+0.262 (n=2476)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4309 (IC base=+0.234)

- **PATRÓN** `dist_vwap_pct` > `0.3041` → IC=+0.247 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3041 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.312` → IC=+0.270 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.312 (IC base=+0.234)

- **PATRÓN** `volumen_regimen` < `0.8693` → IC=+0.237 (n=1651)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8693 (IC base=+0.234)

- **PATRÓN** `volumen_regimen` > `0.6419` → IC=+0.238 (n=2476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6419 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2794` → IC=+0.291 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2794 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `2.5137` → IC=+0.232 (n=2317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5137 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `1.4363` → IC=+0.236 (n=2316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4363 (IC base=+0.234)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.209 (n=1213)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.13` → IC=+0.205 (n=1589)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.13 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.194 (n=3621)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 6.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.3442` → IC=+0.211 (n=3612)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3442 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.7873` → IC=+0.203 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7873 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.597` → IC=+0.211 (n=1564)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.597 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.8641` → IC=+0.202 (n=2165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8641 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` > `1.1975` → IC=+0.184 (n=1082)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 1.1975 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.0739` → IC=+0.189 (n=1459)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.0739 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `1.4295` → IC=+0.194 (n=1172)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4295 (IC base=+0.181)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.188 (n=4071)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.02 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `2623.3812` → IC=+0.187 (n=3227)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2623.3812 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.395` → IC=+0.150 (n=2644)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.395 (IC base=+0.077)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.200 (n=864)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.3249` → IC=+0.212 (n=979)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3249 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.220 (n=895)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` > `0.6435` → IC=+0.250 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6435 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` > `0.3052` → IC=+0.211 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3052 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.068` → IC=+0.209 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.068 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.272` → IC=+0.192 (n=1121)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 9.272 (IC base=+0.192)

- **PATRÓN** `volumen_regimen` < `0.8784` → IC=+0.214 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8784 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` < `0.1536` → IC=+0.195 (n=1027)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.1536 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.196 (n=393)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` < `2.1894` → IC=+0.206 (n=844)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1894 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `14609.6219` → IC=+0.195 (n=653)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 14609.6219 (IC base=+0.192)

- **PATRÓN** `ballena_activa_n` < `163.0` → IC=+0.208 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 163.0 (IC base=+0.192)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.168 (n=404)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0029 (IC base=+0.086)

- **PATRÓN** `ibs_20min` < `0.6431` → IC=+0.139 (n=1061)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.6431 (IC base=+0.086)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.172 (n=517)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 164.0 (IC base=+0.086)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.235 (n=763)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.1262` → IC=+0.219 (n=503)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1262 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.214 (n=1192)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `0.365` → IC=+0.238 (n=1022)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.365 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` > `0.7874` → IC=+0.210 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7874 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` < `0.2075` → IC=+0.199 (n=1030)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.2075 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.884` → IC=+0.237 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.884 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `1.0194` → IC=+0.207 (n=1007)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0194 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.1588` → IC=+0.225 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1588 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `1.4274` → IC=+0.207 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4274 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `1.7865` → IC=+0.207 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7865 (IC base=+0.197)

- **PATRÓN** `ibs_20min` < `0.1095` → IC=+0.166 (n=381)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.1095 (IC base=+0.070)

- **PATRÓN** `libro_liquidez` > `8288.2304` → IC=+0.142 (n=518)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 8288.2304 (IC base=+0.070)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.191 (n=299)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.011 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.193 (n=809)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 8.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.5357` → IC=+0.210 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5357 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.9532` → IC=+0.241 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9532 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.072` → IC=+0.246 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.072 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `0.8887` → IC=+0.184 (n=599)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.8887 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` > `0.714` → IC=+0.173 (n=802)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 0.714 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.2307` → IC=+0.188 (n=168)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2307 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `1.4335` → IC=+0.194 (n=289)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4335 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `2.1499` → IC=+0.168 (n=393)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.1499 (IC base=+0.165)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.175 (n=931)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.02 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `2769.7981` → IC=+0.190 (n=407)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2769.7981 (IC base=+0.165)

- **PATRÓN** `ibs_20min` < `0.2222` → IC=+0.186 (n=451)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.2222 (IC base=+0.035)

- **PATRÓN** `libro_liquidez` > `2590.446` → IC=+0.140 (n=462)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2590.446 (IC base=+0.035)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0242` → IC=+0.157 (n=228)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0242 (IC base=+0.146)

- **PATRÓN** `sigma_h` > `0.0146` → IC=+0.195 (n=152)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0146 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.254` → IC=+0.169 (n=152)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.254 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.189 (n=120)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 8.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.56` → IC=+0.180 (n=204)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.56 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.301` → IC=+0.161 (n=113)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.301 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `1.1352` → IC=+0.151 (n=262)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 1.1352 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.251` → IC=+0.180 (n=195)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 3.251 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` > `0.6182` → IC=+0.157 (n=228)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.6182 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` < `0.2439` → IC=+0.170 (n=228)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.2439 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.4483` → IC=+0.200 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4483 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.5669` → IC=+0.167 (n=67)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.5669 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.172 (n=266)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.03 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `2464.3002` → IC=+0.169 (n=152)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2464.3002 (IC base=+0.146)

- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.150 (n=264)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0103 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.142 (n=191)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 10.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.599` → IC=+0.133 (n=265)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.599 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `1.1597` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1597 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.225` → IC=+0.171 (n=71)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 5.225 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `0.9016` → IC=+0.142 (n=177)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.9016 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `1.0671` → IC=+0.123 (n=120)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` > 1.0671 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` < `0.1161` → IC=+0.133 (n=243)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.1161 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.2383` → IC=+0.173 (n=50)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2383 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` > `2.3673` → IC=+0.129 (n=114)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.3673 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2005.7135` → IC=+0.124 (n=264)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2005.7135 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.136 (n=245)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 19.0 (IC base=+0.121)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.231 (n=6314)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=19734)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `0.4429` → IC=+0.230 (n=18924)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4429 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `0.8763` → IC=+0.209 (n=2284)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8763 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.148` → IC=+0.253 (n=4615)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.148 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `1.2204` → IC=+0.165 (n=12710)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2204 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2417` → IC=+0.206 (n=3432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2417 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6215` → IC=+0.195 (n=6147)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6215 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `108.0` → IC=+0.202 (n=17575)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 108.0 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.196 (n=7621)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0057 (IC base=+0.189)

- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.191 (n=5776)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0118 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.3722` → IC=+0.194 (n=15231)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.3722 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=6427)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` < `0.59` → IC=+0.241 (n=17308)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.59 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.689` → IC=+0.203 (n=2382)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.689 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.488` → IC=+0.193 (n=16795)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 3.488 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` < `1.0582` → IC=+0.163 (n=10275)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.0582 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.2921` → IC=+0.252 (n=2348)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2921 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `2.6337` → IC=+0.200 (n=5488)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6337 (IC base=+0.189)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.238 (n=5616)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.189)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3528` → IC=+0.231 (n=3065)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3528 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.243 (n=1485)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.230)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.235 (n=2065)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.230)

- **PATRÓN** `ibs_20min` > `0.9709` → IC=+0.322 (n=1390)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9709 (IC base=+0.230)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.178` → IC=+0.346 (n=718)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.178 (IC base=+0.230)

- **PATRÓN** `volumen_pendiente_norm` > `0.2333` → IC=+0.286 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2333 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` < `1.4481` → IC=+0.232 (n=985)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4481 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` > `2.2917` → IC=+0.240 (n=1339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2917 (IC base=+0.230)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.248 (n=3321)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.230)

- **PATRÓN** `libro_liquidez` > `2045.8902` → IC=+0.233 (n=1022)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2045.8902 (IC base=+0.230)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.256 (n=1851)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.230)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.269 (n=2655)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0092 (IC base=+0.266)

- **PATRÓN** `drift_60min` |x|≤ `0.1186` → IC=+0.292 (n=1167)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1186 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.272 (n=2442)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` < `0.529` → IC=+0.289 (n=2653)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.529 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` < `0.097` → IC=+0.269 (n=2397)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.097 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` > `0.2892` → IC=+0.289 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2892 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` < `1.569` → IC=+0.269 (n=1112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.569 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` > `2.6807` → IC=+0.276 (n=843)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6807 (IC base=+0.266)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.267 (n=3029)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.266)

- **PATRÓN** `libro_liquidez` > `1769.6091` → IC=+0.271 (n=1768)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1769.6091 (IC base=+0.266)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.274 (n=1106)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.266)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.189 (n=1025)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0029 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.104` → IC=+0.160 (n=1351)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.104 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=3195)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.2315` → IC=+0.202 (n=3067)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2315 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.3202` → IC=+0.201 (n=1061)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3202 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.551` → IC=+0.158 (n=647)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 9.551 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.184` → IC=+0.150 (n=2840)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.184 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.6328` → IC=+0.171 (n=1024)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.6328 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` > `1.0768` → IC=+0.150 (n=1391)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 1.0768 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.2735` → IC=+0.189 (n=441)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2735 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.1714` → IC=+0.155 (n=2644)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.1714 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.5326` → IC=+0.153 (n=2685)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.5326 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `232.0` → IC=+0.179 (n=991)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 232.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.162 (n=2637)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0059 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.0778` → IC=+0.183 (n=879)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.0778 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=973)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.6911` → IC=+0.190 (n=2636)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6911 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.065` → IC=+0.154 (n=434)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 11.065 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.0505` → IC=+0.155 (n=2320)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0505 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2189` → IC=+0.195 (n=490)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2189 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.4315` → IC=+0.145 (n=2530)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4315 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.7783` → IC=+0.146 (n=1687)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.7783 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=3421)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `236.0` → IC=+0.154 (n=818)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 236.0 (IC base=+0.140)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.251 (n=1051)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0127 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=3301)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=2820)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=1181)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.195` → IC=+0.323 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.195 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` < `0.1316` → IC=+0.227 (n=2965)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1316 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `1.6213` → IC=+0.230 (n=3069)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6213 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.232 (n=3760)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `2028.6484` → IC=+0.240 (n=1051)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2028.6484 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.245 (n=2628)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0109 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.179` → IC=+0.258 (n=1313)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.179 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=1123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.0476` → IC=+0.303 (n=995)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0476 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.727` → IC=+0.294 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.727 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.3488` → IC=+0.307 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3488 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.1493` → IC=+0.250 (n=1901)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1493 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.246 (n=1513)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1912.5584` → IC=+0.249 (n=1351)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1912.5584 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.249 (n=1906)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.241)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.197 (n=1091)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0035 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.4269` → IC=+0.153 (n=3264)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4269 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.155 (n=3387)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.8116` → IC=+0.262 (n=1479)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8116 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.1421` → IC=+0.167 (n=1683)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1421 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.058` → IC=+0.157 (n=1461)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.058 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `0.8612` → IC=+0.157 (n=2176)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8612 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2346` → IC=+0.192 (n=579)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2346 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `1.5231` → IC=+0.159 (n=1403)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.5231 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `2.1875` → IC=+0.148 (n=1445)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 2.1875 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `5395.5281` → IC=+0.232 (n=1479)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5395.5281 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.154 (n=1403)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 70.0 (IC base=+0.143)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.156 (n=2731)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0076 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.4355` → IC=+0.143 (n=2727)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.4355 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.158 (n=995)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.5885` → IC=+0.204 (n=2400)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5885 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.108` → IC=+0.168 (n=413)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.108 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.143` → IC=+0.134 (n=2380)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 3.143 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.6926` → IC=+0.150 (n=1200)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6926 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2956` → IC=+0.223 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2956 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.5372` → IC=+0.142 (n=2350)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.5372 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `6335.5572` → IC=+0.207 (n=909)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6335.5572 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `97.0` → IC=+0.139 (n=1794)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 97.0 (IC base=+0.133)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.155 (n=1495)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0107 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.153 (n=2330)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 11.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `0.4359` → IC=+0.194 (n=3299)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.4359 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `1.0094` → IC=+0.204 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0094 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.522` → IC=+0.265 (n=835)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.522 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.8803` → IC=+0.138 (n=2198)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.8803 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1638` → IC=+0.122 (n=3438)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1638 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.831` → IC=+0.126 (n=2148)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.831 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.123 (n=3435)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2705.1503` → IC=+0.245 (n=1099)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2705.1503 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.128 (n=1077)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 22.0 (IC base=+0.120)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.152 (n=2767)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0104 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.1345` → IC=+0.151 (n=1048)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1345 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.129 (n=3246)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.207 (n=3157)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6667 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.18` → IC=+0.140 (n=3013)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 3.18 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.6403` → IC=+0.145 (n=1049)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.6403 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2255` → IC=+0.161 (n=543)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2255 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.4386` → IC=+0.149 (n=987)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4386 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2572.0411` → IC=+0.197 (n=1048)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2572.0411 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.131 (n=2633)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 45.0 (IC base=+0.117)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0138` → IC=+0.257 (n=2756)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0138 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.238 (n=3222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.237 (n=2764)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` > `0.6127` → IC=+0.271 (n=2755)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6127 (IC base=+0.234)

- **PATRÓN** `dist_vwap_pct` > `0.1901` → IC=+0.249 (n=1642)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1901 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.302` → IC=+0.280 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.302 (IC base=+0.234)

- **PATRÓN** `volumen_regimen` < `1.2206` → IC=+0.238 (n=3084)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2206 (IC base=+0.234)

- **PATRÓN** `volumen_regimen` > `0.6427` → IC=+0.238 (n=3084)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6427 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2365` → IC=+0.255 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2365 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.4826` → IC=+0.252 (n=1003)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4826 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=4006)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2109.9208` → IC=+0.234 (n=3084)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2109.9208 (IC base=+0.234)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.259 (n=1060)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.242 (n=2991)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.5188` → IC=+0.269 (n=3173)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5188 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.239` → IC=+0.277 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.239 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` > `1.2206` → IC=+0.259 (n=1058)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2206 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2835` → IC=+0.299 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2835 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `1.813` → IC=+0.234 (n=1980)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.813 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `1.4305` → IC=+0.238 (n=2969)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4305 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.234 (n=2887)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.236)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.199 (n=5401)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.247 (n=1875)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.3937` → IC=+0.223 (n=4936)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3937 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=2051)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `0.9369` → IC=+0.253 (n=1871)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9369 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `0.1711` → IC=+0.217 (n=2113)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1711 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` < `0.4272` → IC=+0.220 (n=4044)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4272 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.623` → IC=+0.222 (n=1835)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.623 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.59` → IC=+0.216 (n=4992)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.59 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` < `0.706` → IC=+0.227 (n=1811)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.706 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `0.8827` → IC=+0.217 (n=2743)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8827 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` < `0.1063` → IC=+0.217 (n=5241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1063 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.1656` → IC=+0.221 (n=1585)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1656 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.4538` → IC=+0.223 (n=1842)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4538 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.222 (n=4348)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `3702.1843` → IC=+0.224 (n=3739)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3702.1843 (IC base=+0.215)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.237 (n=1362)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.3855` → IC=+0.217 (n=3575)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3855 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=1369)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.215 (n=1800)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` < `0.7333` → IC=+0.204 (n=4065)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7333 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.6561` → IC=+0.207 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6561 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` < `0.238` → IC=+0.195 (n=3736)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.238 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.806` → IC=+0.208 (n=3642)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.806 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` < `1.0952` → IC=+0.204 (n=3401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0952 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` < `0.0984` → IC=+0.201 (n=3739)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0984 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.0741` → IC=+0.200 (n=1812)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0741 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` < `1.5371` → IC=+0.203 (n=1762)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5371 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `2.1944` → IC=+0.204 (n=1815)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1944 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.199 (n=5401)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.216 (n=1774)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.198)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.277 (n=750)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0055 (IC base=+0.266)

- **PATRÓN** `drift_60min` |x|≤ `0.0822` → IC=+0.297 (n=284)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0822 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.276 (n=855)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` < `0.4742` → IC=+0.282 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4742 (IC base=+0.266)

- **PATRÓN** `dist_vwap_pct` < `0.1949` → IC=+0.280 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1949 (IC base=+0.266)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.035` → IC=+0.285 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.035 (IC base=+0.266)

- **PATRÓN** `volumen_regimen` < `1.2246` → IC=+0.272 (n=852)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2246 (IC base=+0.266)

- **PATRÓN** `volumen_regimen` > `0.8748` → IC=+0.281 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8748 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` > `0.2875` → IC=+0.343 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2875 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` < `1.8118` → IC=+0.272 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8118 (IC base=+0.266)

- **PATRÓN** `libro_liquidez` > `15982.9994` → IC=+0.273 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15982.9994 (IC base=+0.266)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.255 (n=479)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.3723` → IC=+0.194 (n=1429)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.3723 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=517)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.195 (n=523)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` < `0.1385` → IC=+0.203 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1385 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.6811` → IC=+0.202 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6811 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.329` → IC=+0.204 (n=1405)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.329 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.642` → IC=+0.209 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.642 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.1532` → IC=+0.196 (n=436)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1532 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `2.4927` → IC=+0.188 (n=1420)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.4927 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `1.8072` → IC=+0.184 (n=947)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.8072 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `12998.3043` → IC=+0.182 (n=952)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 12998.3043 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `686.0` → IC=+0.193 (n=1382)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 686.0 (IC base=+0.180)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.218 (n=388)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.5868` → IC=+0.203 (n=853)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5868 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.238 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` < `0.7077` → IC=+0.195 (n=569)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.7077 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.240 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.492` → IC=+0.239 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.492 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.2085` → IC=+0.235 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2085 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `1.825` → IC=+0.203 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.825 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `2757.065` → IC=+0.221 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2757.065 (IC base=+0.195)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.199 (n=570)

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

- **PATRÓN** `libro_liquidez` > `2388.306` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2388.306 (IC base=+0.228)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.228)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.008` → IC=+0.219 (n=1533)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.1462` → IC=+0.218 (n=673)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1462 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.225 (n=551)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` < `0.5048` → IC=+0.217 (n=1020)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5048 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.8652` → IC=+0.207 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8652 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.4035` → IC=+0.216 (n=1534)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4035 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.099` → IC=+0.213 (n=1389)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.099 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `1.0544` → IC=+0.207 (n=1346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0544 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` < `0.105` → IC=+0.208 (n=1411)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.105 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `2.4598` → IC=+0.211 (n=1499)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4598 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=1583)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.008` → IC=+0.209 (n=1248)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.194)

- **PATRÓN** `drift_60min` |x|≤ `0.3813` → IC=+0.219 (n=1097)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3813 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.206 (n=481)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.205 (n=836)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` < `0.3985` → IC=+0.201 (n=832)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3985 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `0.0884` → IC=+0.197 (n=1247)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.0884 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` > `0.6371` → IC=+0.208 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6371 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` < `0.2256` → IC=+0.195 (n=1213)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.2256 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.229` → IC=+0.196 (n=586)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 3.229 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.759` → IC=+0.196 (n=1276)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` < 6.759 (IC base=+0.194)

- **PATRÓN** `volumen_regimen` < `0.6378` → IC=+0.232 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6378 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.0756` → IC=+0.224 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0756 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` < `2.2019` → IC=+0.197 (n=1075)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.2019 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.5301` → IC=+0.199 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5301 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `4977.7816` → IC=+0.197 (n=1247)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 4977.7816 (IC base=+0.194)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.215 (n=566)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.217 (n=821)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.268 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` > `0.7227` → IC=+0.235 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7227 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.252` → IC=+0.218 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.252 (IC base=+0.190)

- **PATRÓN** `volumen_regimen` < `0.6342` → IC=+0.240 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6342 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` < `0.1064` → IC=+0.201 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1064 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.0792` → IC=+0.195 (n=378)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0792 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` < `1.5718` → IC=+0.198 (n=362)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.5718 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.4925` → IC=+0.203 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4925 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.196 (n=998)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.02 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `4265.5976` → IC=+0.232 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4265.5976 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.226 (n=279)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.4938` → IC=+0.239 (n=542)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4938 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.255 (n=434)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` < `0.7308` → IC=+0.241 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7308 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `0.8326` → IC=+0.220 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8326 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` < `0.7551` → IC=+0.225 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7551 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `0.9314` → IC=+0.218 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9314 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` < `0.1073` → IC=+0.234 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1073 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `2.2063` → IC=+0.251 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2063 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `2968.4304` → IC=+0.234 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2968.4304 (IC base=+0.216)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.259 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 28.0 (IC base=+0.216)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.144 (n=836)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0042 (IC base=+0.063)

- **PATRÓN** `ibs_20min` > `0.7662` → IC=+0.198 (n=1205)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.7662 (IC base=+0.063)

- **PATRÓN** `dist_vwap_pct` > `0.1457` → IC=+0.142 (n=924)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1457 (IC base=+0.063)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.809` → IC=+0.148 (n=396)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 10.809 (IC base=+0.063)

- **PATRÓN** `ibs_20min` < `0.0454` → IC=+0.264 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0454 (IC base=+0.048)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.934` → IC=+0.167 (n=178)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.934 (IC base=+0.048)

- **PATRÓN** `volumen_pendiente_norm` > `0.1467` → IC=+0.154 (n=313)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.1467 (IC base=+0.048)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.3596` → IC=-0.150 (n=195)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3596
  - _Potencial_: sin este filtro IC_bueno=+0.165 (n=586)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.128 (n=617)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0057 (IC base=+0.085)

- **PATRÓN** `ibs_20min` > `0.3596` → IC=+0.165 (n=586)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.3596 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.119` → IC=+0.175 (n=293)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.119 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.0674` → IC=+0.289 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0674 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.2162` → IC=+0.184 (n=93)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2162 (IC base=+0.057)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.140 (n=415)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.005 (IC base=+0.083)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.135 (n=305)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 15.0 (IC base=+0.083)

- **PATRÓN** `ibs_20min` > `0.5536` → IC=+0.183 (n=528)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.5536 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` > `0.1265` → IC=+0.185 (n=296)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1265 (IC base=+0.083)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.029` → IC=+0.210 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.029 (IC base=+0.083)

- **PATRÓN** `ibs_20min` < `0.0314` → IC=+0.248 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0314 (IC base=+0.017)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.617` → IC=+0.210 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.617 (IC base=+0.017)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.196 (n=218)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 1.0 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` > `0.7109` → IC=+0.133 (n=148)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.7109 (IC base=+0.023)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.982` → IC=+0.142 (n=135)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 8.982 (IC base=+0.023)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.155 (n=276)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0105 (IC base=+0.073)

- **PATRÓN** `ibs_20min` < `0.0714` → IC=+0.254 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0714 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.1744` → IC=+0.138 (n=269)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1744 (IC base=+0.073)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.114` → IC=+0.348 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.114 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` > `1.1084` → IC=+0.188 (n=94)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 1.1084 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.1522` → IC=+0.190 (n=85)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.1522 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` < `2.2371` → IC=+0.126 (n=228)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 2.2371 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` > `1.8521` → IC=+0.149 (n=172)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.8521 (IC base=+0.073)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0054` → IC=-0.235 (n=168)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0054
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=168)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.336 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=265)

- **FILTRO** `dist_vwap_pct` > `0.2351` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2351
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=320)

- **FILTRO** `volumen_regimen` < `0.7738` → IC=-0.302 (n=84)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7738
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=252)

- **FILTRO** `drift_60min` |x|> `0.1941` → IC=-0.338 (n=72)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1941
  - _Potencial_: sin este filtro IC_bueno=-0.270 (n=220)

- **FILTRO** `dist_vwap_pct` > `0.3644` → IC=-0.406 (n=30)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3644
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=268)

- **FILTRO** `sigma_ewma_delta_pct` > `10.034` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 10.034
  - _Potencial_: sin este filtro IC_bueno=-0.288 (n=272)

- **FILTRO** `volumen_pendiente_norm` > `0.0435` → IC=-0.382 (n=32)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0435
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=178)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `volumen_regimen` < `1.2175` → IC=-0.292 (n=51)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2175
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=52)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.279 (n=66)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=67)

- **FILTRO** `volumen_regimen` > `0.8213` → IC=-0.329 (n=33)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8213
  - _Potencial_: sin este filtro IC_bueno=-0.226 (n=100)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` < `0.0027` → IC=-0.293 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0027
  - _Potencial_: sin este filtro IC_bueno=-0.114 (n=86)

- **FILTRO** `ibs_20min` < `0.5843` → IC=-0.467 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5843
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=85)

- **FILTRO** `volumen_regimen` > `1.1691` → IC=-0.167 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.1691
  - _Potencial_: sin este filtro IC_bueno=-0.155 (n=85)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.375 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=93)

- **FILTRO** `ibs_20min` > `0.7113` → IC=-0.402 (n=39)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7113
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=76)

- **FILTRO** `dist_vwap_pct` > `0.1281` → IC=-0.371 (n=29)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1281
  - _Potencial_: sin este filtro IC_bueno=-0.295 (n=86)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.314 (n=100)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `drift_60min` |x|> `0.2366` → IC=-0.371 (n=29)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2366
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=90)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.400 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=102)

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
- **FILTRO** `ibs_20min` > `0.1414` → IC=-0.122 (n=310)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1414
  - _Potencial_: sin este filtro IC_bueno=+0.126 (n=603)

- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.206 (n=199)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.199 (n=227)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `0.6686` → IC=+0.169 (n=597)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.6686 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `0.5388` → IC=+0.240 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5388 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.618` → IC=+0.136 (n=328)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 3.618 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.697` → IC=+0.134 (n=438)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 2.697 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.6195` → IC=+0.178 (n=200)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.6195 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` < `0.069` → IC=+0.169 (n=424)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.069 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.3996` → IC=+0.189 (n=165)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.3996 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.1414` → IC=+0.126 (n=603)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.1414 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.023` → IC=+0.162 (n=199)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 9.023 (IC base=+0.042)

- **PATRÓN** `libro_liquidez` > `4894.8429` → IC=+0.123 (n=311)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 4894.8429 (IC base=+0.042)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.74` → IC=-0.163 (n=78)

  - _Acción_: SKIP cuando `ibs_20min` < 0.74
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=161)

- **PATRÓN** `ibs_20min` < `0.1761` → IC=+0.177 (n=320)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.1761 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` < `0.1046` → IC=+0.125 (n=329)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` < 0.1046 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.216` → IC=+0.145 (n=136)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 7.216 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` > `1.0363` → IC=+0.160 (n=145)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 1.0363 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.2687` → IC=+0.148 (n=52)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2687 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` > `1.786` → IC=+0.144 (n=192)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.786 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `5391.3885` → IC=+0.133 (n=213)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 5391.3885 (IC base=+0.115)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1263` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1263
  - _Potencial_: sin este filtro IC_bueno=+0.170 (n=192)

- **FILTRO** `ibs_20min` > `0.1628` → IC=-0.137 (n=111)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1628
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=218)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.144 (n=133)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.004 (IC base=+0.120)

- **PATRÓN** `sigma_h` > `0.003` → IC=+0.131 (n=177)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` > 0.003 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1024` → IC=+0.133 (n=88)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.1024 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.196 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `0.8015` → IC=+0.161 (n=178)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.8015 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.0953` → IC=+0.147 (n=165)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.0953 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.217` → IC=+0.155 (n=207)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 9.217 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.6229` → IC=+0.196 (n=67)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.6229 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1263` → IC=+0.170 (n=192)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.1263 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.7967` → IC=+0.190 (n=114)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.7967 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=167)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `1623.6709` → IC=+0.180 (n=198)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 1623.6709 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.828` → IC=+0.205 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.828 (IC base=+0.002)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2308` → IC=-0.264 (n=53)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2308
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=105)

- **FILTRO** `dist_vwap_pct` > `0.3368` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3368
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=133)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.275 (n=100)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.299 (n=157)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` > `0.6053` → IC=+0.265 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6053 (IC base=+0.231)

- **PATRÓN** `dist_vwap_pct` > `0.6667` → IC=+0.382 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6667 (IC base=+0.231)

- **PATRÓN** `dist_vwap_pct` < `0.2453` → IC=+0.231 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2453 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.006` → IC=+0.341 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.006 (IC base=+0.231)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.272 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.285 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` < `1.4814` → IC=+0.340 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4814 (IC base=+0.231)

- **PATRÓN** `libro_liquidez` > `738.2599` → IC=+0.232 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 738.2599 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.321` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.321 (IC base=-0.069)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.317 (n=80)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3447` → IC=+0.318 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3447 (IC base=+0.305)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.366 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.305)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.417 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.305)

- **PATRÓN** `drift_60min` |x|≤ `0.9307` → IC=+0.364 (n=64)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9307 (IC base=+0.305)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.375 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.305)

- **PATRÓN** `ballena_activa_n` < `1071.0` → IC=+0.375 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1071.0 (IC base=+0.305)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3474` → IC=+0.261 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3474 (IC base=+0.237)

- **PATRÓN** `elapsed_s` > `187.9` → IC=+0.261 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 187.9 (IC base=+0.237)

- **PATRÓN** `elapsed_s` < `216.8` → IC=+0.246 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 216.8 (IC base=+0.237)

- **PATRÓN** `drift_15min` |x|≤ `2.3682` → IC=+0.306 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3682 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.6424` → IC=+0.304 (n=49)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6424 (IC base=+0.237)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.317 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `1814.0` → IC=+0.287 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1814.0 (IC base=+0.237)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.317 (n=80)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3447` → IC=+0.318 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3447 (IC base=+0.305)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.366 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.305)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.417 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.305)

- **PATRÓN** `drift_60min` |x|≤ `0.9307` → IC=+0.364 (n=64)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9307 (IC base=+0.305)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.375 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.305)

- **PATRÓN** `ballena_activa_n` < `1071.0` → IC=+0.375 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1071.0 (IC base=+0.305)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3474` → IC=+0.261 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3474 (IC base=+0.237)

- **PATRÓN** `elapsed_s` > `187.9` → IC=+0.261 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 187.9 (IC base=+0.237)

- **PATRÓN** `elapsed_s` < `216.8` → IC=+0.246 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 216.8 (IC base=+0.237)

- **PATRÓN** `drift_15min` |x|≤ `2.3682` → IC=+0.306 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3682 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.6424` → IC=+0.304 (n=49)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6424 (IC base=+0.237)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.317 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `1814.0` → IC=+0.287 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1814.0 (IC base=+0.237)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=214)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=214)

- **FILTRO** `libro_liquidez` < `5951.6129` → IC=-0.150 (n=115)

  - _Acción_: SKIP cuando `libro_liquidez` < 5951.6129
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=115)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=462)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `4006.09` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `liq_usd_total` < 4006.09
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=26)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=35)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.176 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 7.0 (IC base=+0.059)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=3734)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.135 (n=113)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=70)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=100)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.135 (n=113)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.133 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=132)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=21)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=14)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.126 (n=263)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=+0.023)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=1458)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=1412)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.286 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.140 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=712)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=720)

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
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=896)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=896)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.132 (n=275)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=701)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=981)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=981)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=234)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=234)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.130 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=178)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.192 (n=50)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=290)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=325)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=277)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=370)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=370)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=215)

- **FILTRO** `libro_liquidez` < `642.4226` → IC=-0.134 (n=132)

  - _Acción_: SKIP cuando `libro_liquidez` < 642.4226
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=268)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=285)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.129 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=213)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `restante_min` < `9.67` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `restante_min` < 9.67
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=77)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.148 (n=69)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=40)

- **FILTRO** `py_entrada` > `0.53` → IC=-0.150 (n=38)

  - _Acción_: SKIP cuando `py_entrada` > 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=20)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.250 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=40)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.51` → IC=+0.157 (n=246)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` < 0.51 (IC base=+0.008)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.126 (n=129)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=505)

- **FILTRO** `profundidad_ratio` < `43.4` → IC=-0.144 (n=158)

  - _Acción_: SKIP cuando `profundidad_ratio` < 43.4
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=476)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.129 (n=251)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=275)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.123 (n=189)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=401)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` > `0.61` → IC=-0.130 (n=90)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=280)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.139 (n=156)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=569)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.165 (n=6958)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=20986)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.177 (n=6996)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=21749)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.192 (n=1246)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=3891)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.178 (n=1195)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=3914)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.139 (n=1344)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 1.0 (IC base=+0.042)

- **PATRÓN** `libro_liquidez` > `1064.929` → IC=+0.138 (n=2569)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 1064.929 (IC base=+0.042)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.132 (n=2398)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.5 (IC base=+0.011)

- **PATRÓN** `libro_liquidez` > `1200.847` → IC=+0.151 (n=1738)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1200.847 (IC base=+0.011)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.184 (n=992)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=3082)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.205 (n=1247)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=3984)

- **PATRÓN** `ibs_20min` > `0.9652` → IC=+0.128 (n=1747)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` > 0.9652 (IC base=+0.035)

- **PATRÓN** `libro_liquidez` > `1366.0282` → IC=+0.121 (n=2569)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 1366.0282 (IC base=+0.035)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.153 (n=1265)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=3877)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2410)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=2334)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.189 (n=911)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=2840)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=3730)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `14.0` → IC=-0.157 (n=135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=437)

- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=447)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.234 (n=287)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=1014)

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
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=342)

- **FILTRO** `drift_20min_pct` |x|> `0.2047` → IC=-0.143 (n=113)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.2047
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=342)

- **FILTRO** `libro_liquidez` < `3186.5516` → IC=-0.184 (n=150)

  - _Acción_: SKIP cuando `libro_liquidez` < 3186.5516
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=305)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=946)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.197 (n=354)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=712)

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

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.138 (n=45)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 17.0 (IC base=+0.030)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.133 (n=19110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=42937)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.296 (n=14471)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=47576)

- **FILTRO** `ibs_7min` < `0.2294` → IC=-0.231 (n=15508)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2294
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=46539)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.152 (n=20938)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=41109)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.243 (n=19272)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=58648)

- **FILTRO** `ibs_7min` > `0.2837` → IC=-0.180 (n=19479)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2837
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=58441)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.154 (n=2695)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=8254)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.316 (n=2660)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=8289)

- **FILTRO** `ibs_7min` < `0.7115` → IC=-0.249 (n=3610)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7115
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=7339)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.149 (n=2615)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=8334)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.278 (n=3206)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=10249)

- **FILTRO** `ibs_7min` > `0.7719` → IC=-0.213 (n=3363)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7719
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=10092)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.127 (n=2481)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=7920)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.261 (n=2465)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=7936)

- **FILTRO** `ibs_7min` < `0.7177` → IC=-0.204 (n=2600)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7177
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=7801)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.193 (n=2584)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=7817)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.259 (n=2636)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=7975)

- **FILTRO** `ibs_7min` > `0.2662` → IC=-0.192 (n=2652)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2662
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=7959)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.179 (n=2634)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=7977)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.162 (n=2547)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=7885)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.312 (n=2586)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=7846)

- **FILTRO** `ibs_7min` < `0.2901` → IC=-0.247 (n=3442)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2901
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=6990)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.196 (n=2298)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=8134)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.260 (n=3377)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=10911)

- **FILTRO** `ibs_7min` > `0.7333` → IC=-0.179 (n=3565)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7333
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=10723)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.123 (n=3283)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=6790)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=2430)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=7643)

- **FILTRO** `ibs_7min` < `0.7217` → IC=-0.194 (n=2518)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7217
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=7555)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.188 (n=2462)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=7611)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.262 (n=2390)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=8094)

- **FILTRO** `ibs_7min` > `0.2747` → IC=-0.172 (n=2619)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2747
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=7865)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.175 (n=2562)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=7922)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=2489)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=7582)

- **FILTRO** `ibs_7min` < `0.7111` → IC=-0.224 (n=3320)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7111
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=6751)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.221 (n=2378)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=7693)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.194 (n=3568)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=11465)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.297 (n=2482)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=7639)

- **FILTRO** `ibs_7min` < `0.1887` → IC=-0.229 (n=2530)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1887
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=7591)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.201 (n=2406)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=7715)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.224 (n=3488)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=10561)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.160 (n=301)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=1005)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1291)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.122 (n=215)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=528)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.156 (n=158)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=585)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=863)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.122 (n=220)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=279)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.143 (n=166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=332)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=449)

- **FILTRO** `libro_liquidez` < `3267.213` → IC=-0.154 (n=183)

  - _Acción_: SKIP cuando `libro_liquidez` < 3267.213
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=551)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3983` → IC=+0.136 (n=1299)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.3983 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.136 (n=679)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 6.0 (IC base=+0.127)

- **PATRÓN** `total_vol_5m` < `4062.477` → IC=+0.146 (n=867)

  - _Acción_: Kelly boost +0.73€ cuando `total_vol_5m` < 4062.477 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `3472.2489` → IC=+0.146 (n=589)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3472.2489 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.128 (n=441)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 10.0 (IC base=+0.127)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.171 (n=147)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 14.0 (IC base=+0.127)

- **PATRÓN** `total_vol_5m` < `280.725` → IC=+0.149 (n=203)

  - _Acción_: Kelly boost +0.74€ cuando `total_vol_5m` < 280.725 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `2522.0946` → IC=+0.211 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2522.0946 (IC base=+0.127)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3994` → IC=+0.126 (n=271)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.63€ cuando `delta_ratio` |x|> 0.3994 (IC base=+0.112)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.134 (n=241)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 14.0 (IC base=+0.112)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.121 (n=325)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.04 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `2304.0306` → IC=+0.137 (n=180)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2304.0306 (IC base=+0.112)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4161` → IC=+0.192 (n=167)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio` |x|> 0.4161 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.155 (n=262)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 4.0 (IC base=+0.142)

- **PATRÓN** `total_vol_5m` < `381.6269` → IC=+0.214 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 381.6269 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `5192.827` → IC=+0.143 (n=250)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 5192.827 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `60.0` → IC=+0.193 (n=86)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 60.0 (IC base=+0.142)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4318` → IC=+0.217 (n=104)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4318 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.200 (n=108)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.152)

- **PATRÓN** `total_vol_5m` < `4761.643` → IC=+0.195 (n=152)

  - _Acción_: Kelly boost +0.97€ cuando `total_vol_5m` < 4761.643 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `3102.7214` → IC=+0.180 (n=204)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 3102.7214 (IC base=+0.152)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.128 (n=221)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 13.0 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.172 (n=169)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `3728.089` → IC=+0.147 (n=83)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3728.089 (IC base=+0.102)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.7861` → IC=-0.284 (n=49)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.7861
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=148)

- **FILTRO** `sigma_h` > `0.0074` → IC=-0.311 (n=183)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0074
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=552)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.177 (n=184)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0037 (IC base=-0.082)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0072` → IC=-0.304 (n=54)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0072
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=164)

- **FILTRO** `T_h` > `87.9901` → IC=-0.232 (n=54)

  - _Acción_: SKIP cuando `T_h` > 87.9901
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=164)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.289 (n=55)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=-0.036)

- **PATRÓN** `pct_vs_K` |x|≤ `1.5815` → IC=+0.149 (n=72)

  - _Acción_: Kelly boost +0.74€ cuando `pct_vs_K` |x|≤ 1.5815 (IC base=-0.036)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `pct_vs_K` |x|> `9.1619` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 9.1619
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=53)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `T_h` < `92.8406` → IC=-0.186 (n=68)

  - _Acción_: SKIP cuando `T_h` < 92.8406
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=68)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.238 (n=440)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=227)

- **FILTRO** `T_h` > `79.6334` → IC=-0.214 (n=446)

  - _Acción_: SKIP cuando `T_h` > 79.6334
  - _Potencial_: sin este filtro IC_bueno=-0.155 (n=221)

- **FILTRO** `sigma_h` > `0.0095` → IC=-0.250 (n=142)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.213 (n=430)

- **FILTRO** `T_h` > `54.2183` → IC=-0.256 (n=428)

  - _Acción_: SKIP cuando `T_h` > 54.2183
  - _Potencial_: sin este filtro IC_bueno=-0.123 (n=144)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0082` → IC=-0.207 (n=165)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0082
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=55)

- **FILTRO** `pct_vs_K` |x|> `2.9616` → IC=-0.424 (n=51)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9616
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=155)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `sigma_h` < `0.0085` → IC=-0.250 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0096` → IC=-0.320 (n=126)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0096
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=65)

- **FILTRO** `T_h` > `69.4221` → IC=-0.272 (n=143)

  - _Acción_: SKIP cuando `T_h` > 69.4221
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=48)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.348 (n=44)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=134)

- **FILTRO** `T_h` > `57.1769` → IC=-0.252 (n=119)

  - _Acción_: SKIP cuando `T_h` > 57.1769
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=59)

- **PATRÓN** `pct_vs_K` |x|≤ `0.7908` → IC=+0.181 (n=45)

  - _Acción_: Kelly boost +0.90€ cuando `pct_vs_K` |x|≤ 0.7908 (IC base=-0.178)

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
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=141)

- **FILTRO** `T_h` > `71.5417` → IC=-0.197 (n=140)

  - _Acción_: SKIP cuando `T_h` > 71.5417
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=48)

- **FILTRO** `sigma_h` > `0.015` → IC=-0.379 (n=31)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.015
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=95)

- **FILTRO** `sigma_h` < `0.0087` → IC=-0.291 (n=41)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0087
  - _Potencial_: sin este filtro IC_bueno=-0.213 (n=85)

- **FILTRO** `T_h` > `33.8406` → IC=-0.271 (n=94)

  - _Acción_: SKIP cuando `T_h` > 33.8406
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=32)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1208` → IC=+0.468 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1208 (IC base=+0.338)

- **PATRÓN** `sigma_h` < `0.0146` → IC=+0.357 (n=103)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0146 (IC base=+0.338)

- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.371 (n=68)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.338)

- **PATRÓN** `T_h` > `0.7452` → IC=+0.386 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7452 (IC base=+0.338)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.480 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.338)

- **PATRÓN** `edge` > `0.1005` → IC=+0.437 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1005 (IC base=+0.409)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.414 (n=79)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.409)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.431 (n=158)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.409)

- **PATRÓN** `T_h` < `0.6127` → IC=+0.439 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6127 (IC base=+0.409)

- **PATRÓN** `T_h` > `1.484` → IC=+0.414 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.484 (IC base=+0.409)

- **PATRÓN** `dist_50` > `0.376` → IC=+0.446 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.376 (IC base=+0.409)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.471 (n=138)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.409)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1506` → IC=+0.257 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1506 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.281 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.205)

- **PATRÓN** `T_h` < `1.484` → IC=+0.257 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.484 (IC base=+0.205)

- **PATRÓN** `dist_50` > `0.346` → IC=+0.284 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.346 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.281 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.205)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1023` → IC=+0.460 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.409)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.411 (n=54)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0101 (IC base=+0.409)

- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.395 (n=55)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.409)

- **PATRÓN** `T_h` < `1.2716` → IC=+0.429 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.2716 (IC base=+0.409)

- **PATRÓN** `dist_50` > `0.3502` → IC=+0.446 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3502 (IC base=+0.409)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.400 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.409)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.409)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.1745` → IC=+0.485 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1745 (IC base=+0.433)

- **PATRÓN** `sigma_h` < `0.0161` → IC=+0.455 (n=65)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0161 (IC base=+0.433)

- **PATRÓN** `T_h` > `0.3968` → IC=+0.455 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.3968 (IC base=+0.433)

- **PATRÓN** `dist_50` > `0.3326` → IC=+0.470 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3326 (IC base=+0.433)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.433)

- **PATRÓN** `edge` > `0.2005` → IC=+0.469 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2005 (IC base=+0.461)

- **PATRÓN** `sigma_h` < `0.0156` → IC=+0.473 (n=145)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0156 (IC base=+0.461)

- **PATRÓN** `T_h` < `0.8279` → IC=+0.455 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.8279 (IC base=+0.461)

- **PATRÓN** `T_h` > `1.486` → IC=+0.481 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.486 (IC base=+0.461)

- **PATRÓN** `dist_50` > `0.4597` → IC=+0.492 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4597 (IC base=+0.461)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.466 (n=146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.461)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=346)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=418)

- **PATRÓN** `streak_estiramiento` < `0.3028` → IC=+0.167 (n=88)

  - _Acción_: Kelly boost +0.83€ cuando `streak_estiramiento` < 0.3028 (IC base=+0.018)

- **PATRÓN** `streak_estiramiento` < `0.2796` → IC=+0.263 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.2796 (IC base=+0.060)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.137 (n=213)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 33.0 (IC base=+0.060)

- **PATRÓN** `libro_liquidez` > `2502.8663` → IC=+0.132 (n=150)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2502.8663 (IC base=+0.060)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=29)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=20)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.136 (n=20)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.495 (IC base=+0.013)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `streak_estiramiento` > `0.4392` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4392
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=109)

- **PATRÓN** `streak_estiramiento` < `0.3906` → IC=+0.122 (n=96)

  - _Acción_: Kelly boost +0.61€ cuando `streak_estiramiento` < 0.3906 (IC base=+0.026)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.108)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.131 (n=109)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` < 0.495 (IC base=+0.108)

- **PATRÓN** `regimen_ma_toques` > `2.0` → IC=+0.120 (n=177)

  - _Acción_: Kelly boost +0.60€ cuando `regimen_ma_toques` > 2.0 (IC base=+0.108)

- **PATRÓN** `streak_estiramiento` < `0.2939` → IC=+0.242 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.2939 (IC base=+0.108)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.187 (n=129)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 34.0 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `2519.037` → IC=+0.163 (n=99)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2519.037 (IC base=+0.108)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=98)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=107)

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
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=35)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=34)

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
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `streak_estiramiento` > `1.2307` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `streak_estiramiento` > 1.2307
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=49)

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
- **PATRÓN** `py_entrada` < `0.475` → IC=+0.136 (n=20)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.475 (IC base=+0.065)

- **PATRÓN** `regimen_ma_toques` > `4.0` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.065)

- **PATRÓN** `volumen_racha` < `24607.606` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_racha` < 24607.606 (IC base=+0.065)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=1045)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1335)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1244)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1292)

### STRUCT_NO_15M
- **FILTRO** `hora_utc` < `16.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=23)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=30)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=4325)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `hora_utc` < `16.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=23)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=30)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=2453)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.189 (n=1771)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0055 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.176 (n=1342)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0124 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.1785` → IC=+0.184 (n=3541)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1785 (IC base=+0.166)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0993` → IC=+0.174 (n=1230)

  - _Acción_: Kelly boost +0.87€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0993 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.175 (n=3717)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 6.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.168 (n=3722)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 15.0 (IC base=+0.166)

- **PATRÓN** `ibs_15` > `0.5333` → IC=+0.239 (n=4029)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5333 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.1296` → IC=+0.164 (n=1954)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1296 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` < `0.3153` → IC=+0.151 (n=3251)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.3153 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.11` → IC=+0.263 (n=781)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.11 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `4564.5735` → IC=+0.181 (n=1342)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 4564.5735 (IC base=+0.166)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1622)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.222 (n=686)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.0769` → IC=+0.253 (n=302)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0769 (IC base=+0.206)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2638` → IC=+0.227 (n=229)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2638 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.226 (n=718)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.206)

- **PATRÓN** `ibs_15` > `0.7223` → IC=+0.273 (n=686)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7223 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.2377` → IC=+0.222 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2377 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` < `0.5186` → IC=+0.211 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5186 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.537` → IC=+0.304 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.537 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `8089.1776` → IC=+0.217 (n=686)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8089.1776 (IC base=+0.206)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.160 (n=822)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0067 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.1522` → IC=+0.152 (n=723)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1522 (IC base=+0.143)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1412` → IC=+0.153 (n=548)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio_macro` |x|> 0.1412 (IC base=+0.143)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.125` → IC=+0.153 (n=329)

  - _Acción_: Kelly boost +0.76€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.125 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.152 (n=749)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 6.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.146 (n=860)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 17.0 (IC base=+0.143)

- **PATRÓN** `ibs_15` > `0.5178` → IC=+0.233 (n=822)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5178 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.1187` → IC=+0.164 (n=504)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1187 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.285` → IC=+0.279 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.285 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `5808.0125` → IC=+0.167 (n=373)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 5808.0125 (IC base=+0.143)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `ibs_15` > `0.2239` → IC=-0.120 (n=156)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2239
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=303)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.878` → IC=+0.238 (n=326)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.878 (IC base=+0.080)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.126 (n=509)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.080)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0242` → IC=+0.228 (n=299)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0242 (IC base=+0.194)

- **PATRÓN** `drift_60min` |x|≤ `0.2012` → IC=+0.205 (n=899)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2012 (IC base=+0.194)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3432` → IC=+0.223 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3432 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.204 (n=806)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.194)

- **PATRÓN** `ibs_15` > `0.5156` → IC=+0.273 (n=897)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5156 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` > `0.1316` → IC=+0.213 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1316 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.324` → IC=+0.234 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.324 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.195 (n=615)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.02 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `2948.5144` → IC=+0.291 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2948.5144 (IC base=+0.194)

- **PATRÓN** `ibs_15` < `0.1071` → IC=+0.169 (n=808)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.85€ cuando `ibs_15` < 0.1071 (IC base=+0.070)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.388 (n=311)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1501` → IC=+0.378 (n=456)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1501 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1371` → IC=+0.383 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1371 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.376 (n=685)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.397 (n=686)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.1521` → IC=+0.382 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1521 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.219` → IC=+0.394 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.219 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.369 (n=831)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `3840.073` → IC=+0.373 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3840.073 (IC base=+0.364)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.363 (n=305)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.360)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.398 (n=116)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.360)

- **PATRÓN** `drift_60min` |x|≤ `0.0547` → IC=+0.364 (n=116)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0547 (IC base=+0.360)

- **PATRÓN** `drift_15min` |x|≤ `0.5204` → IC=+0.358 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5204 (IC base=+0.360)

- **PATRÓN** `delta_ratio_macro` |x|> `0.156` → IC=+0.366 (n=230)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.156 (IC base=+0.360)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1441` → IC=+0.392 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1441 (IC base=+0.360)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.377 (n=324)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.360)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.385 (n=346)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.360)

- **PATRÓN** `dist_vwap_pct` > `0.3751` → IC=+0.384 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3751 (IC base=+0.360)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.255` → IC=+0.385 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.255 (IC base=+0.360)

- **PATRÓN** `libro_liquidez` > `8119.484` → IC=+0.382 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8119.484 (IC base=+0.360)

- **PATRÓN** `ballena_activa_n` < `499.0` → IC=+0.398 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 499.0 (IC base=+0.360)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.368 (n=339)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.367)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.382 (n=227)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.367)

- **PATRÓN** `drift_60min` |x|≤ `0.1062` → IC=+0.368 (n=226)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1062 (IC base=+0.367)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0824` → IC=+0.379 (n=303)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0824 (IC base=+0.367)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.384 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.367)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.388 (n=159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.367)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.374 (n=157)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.367)

- **PATRÓN** `ibs_15` > `0.7601` → IC=+0.406 (n=339)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7601 (IC base=+0.367)

- **PATRÓN** `dist_vwap_pct` > `0.1212` → IC=+0.376 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1212 (IC base=+0.367)

- **PATRÓN** `dist_vwap_pct` < `0.2918` → IC=+0.370 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2918 (IC base=+0.367)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.356` → IC=+0.403 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.356 (IC base=+0.367)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.374 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.367)

- **PATRÓN** `libro_liquidez` > `4039.5603` → IC=+0.397 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4039.5603 (IC base=+0.367)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.176 (n=2304)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=2306)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.213 (n=1809)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=2801)

- **FILTRO** `libro_liquidez` < `4253.4042` → IC=-0.154 (n=3042)

  - _Acción_: SKIP cuando `libro_liquidez` < 4253.4042
  - _Potencial_: sin este filtro IC_bueno=+0.099 (n=1568)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.138` → IC=+0.218 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.138 (IC base=-0.068)

- **PATRÓN** `ibs_15` > `0.6335` → IC=+0.280 (n=1113)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6335 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1122` → IC=+0.207 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1122 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` < `0.266` → IC=+0.199 (n=951)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.266 (IC base=-0.068)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2301` → IC=+0.272 (n=1328)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2301 (IC base=-0.011)

- **PATRÓN** `ibs_15` < `0.3677` → IC=+0.282 (n=3980)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3677 (IC base=-0.011)

- **PATRÓN** `dist_vwap_pct` > `0.8802` → IC=+0.275 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8802 (IC base=-0.011)

- **PATRÓN** `dist_vwap_pct` < `0.1655` → IC=+0.247 (n=2988)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1655 (IC base=-0.011)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0334` → IC=-0.223 (n=2146)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0334
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=718)

- **FILTRO** `sigma_h` > `0.0067` → IC=-0.211 (n=715)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=2149)

- **FILTRO** `sigma_h` < `0.0035` → IC=-0.227 (n=716)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=2148)

- **FILTRO** `sigma_ewma_delta_pct` > `23.13` → IC=-0.265 (n=411)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.13
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=2453)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.155 (n=279)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0029 (IC base=+0.086)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1441` → IC=+0.267 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1441 (IC base=+0.086)

- **PATRÓN** `ibs_15` > `0.7639` → IC=+0.328 (n=375)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7639 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.1068` → IC=+0.288 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1068 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` < `0.3659` → IC=+0.288 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3659 (IC base=+0.086)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.239` → IC=+0.148 (n=245)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 19.239 (IC base=+0.086)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1026` → IC=+0.230 (n=61)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1026 (IC base=-0.191)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1323` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1323 (IC base=-0.191)

- **PATRÓN** `ibs_15` < `0.618` → IC=+0.314 (n=68)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.618 (IC base=-0.191)

- **PATRÓN** `dist_vwap_pct` < `0.0415` → IC=+0.325 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0415 (IC base=-0.191)

- **PATRÓN** `ballena_activa_n` < `288.0` → IC=+0.372 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 288.0 (IC base=-0.191)

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

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.262 (n=506)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.3539` → IC=+0.246 (n=1335)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3539 (IC base=+0.245)

- **PATRÓN** `drift_15min` |x|≤ `0.7686` → IC=+0.256 (n=1336)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7686 (IC base=+0.245)

- **PATRÓN** `delta_ratio_macro` |x|> `0.214` → IC=+0.273 (n=688)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.214 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.246 (n=558)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.248 (n=1028)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.245)

- **PATRÓN** `ibs_15` < `0.3769` → IC=+0.277 (n=1517)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3769 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` > `0.1544` → IC=+0.262 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1544 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.389` → IC=+0.253 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.389 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.448` → IC=+0.250 (n=1586)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.448 (IC base=+0.245)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1723` → IC=-0.247 (n=361)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1723
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=701)

- **FILTRO** `drift_15min` |x|> `0.8879` → IC=-0.283 (n=265)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8879
  - _Potencial_: sin este filtro IC_bueno=-0.157 (n=797)

- **FILTRO** `sigma_ewma_delta_pct` > `6.65` → IC=-0.207 (n=244)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.65
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=818)

- **FILTRO** `sigma_ewma_delta_pct` > `17.595` → IC=-0.145 (n=559)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.595
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=4463)

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

- **PATRÓN** `ibs_15` < `0.3902` → IC=+0.291 (n=676)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3902 (IC base=-0.036)

- **PATRÓN** `dist_vwap_pct` < `0.2623` → IC=+0.234 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2623 (IC base=-0.036)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.1514` → IC=-0.222 (n=315)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1514
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=948)

- **FILTRO** `drift_15min` |x|> `0.7503` → IC=-0.247 (n=631)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.7503
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=632)

- **FILTRO** `sigma_ewma_delta_pct` > `7.442` → IC=-0.211 (n=396)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.442
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=867)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=1244)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.210)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.210)

- **PATRÓN** `delta_ratio_macro` |x|> `0.07` → IC=+0.274 (n=820)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.07 (IC base=-0.024)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1173` → IC=+0.290 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1173 (IC base=-0.024)

- **PATRÓN** `ibs_15` < `0.1368` → IC=+0.312 (n=611)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1368 (IC base=-0.024)

- **PATRÓN** `dist_vwap_pct` > `0.7764` → IC=+0.347 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7764 (IC base=-0.024)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.177 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0049 (IC base=+0.103)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.177 (n=29)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.103)

- **PATRÓN** `drift_15min` |x|≤ `0.3696` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3696 (IC base=+0.103)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2338` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2338 (IC base=+0.103)

- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.364 (n=20)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` < `0.0951` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0951 (IC base=+0.103)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 49.0 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` > `0.1533` → IC=+0.125 (n=70)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.1533 (IC base=+0.053)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.177 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0049 (IC base=+0.103)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.177 (n=29)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.103)

- **PATRÓN** `drift_15min` |x|≤ `0.3696` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3696 (IC base=+0.103)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2338` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2338 (IC base=+0.103)

- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.364 (n=20)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` < `0.0951` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0951 (IC base=+0.103)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 49.0 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` > `0.1533` → IC=+0.125 (n=70)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.1533 (IC base=+0.053)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.290 (n=1198)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.0538` → IC=+0.318 (n=400)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0538 (IC base=+0.285)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1505` → IC=+0.286 (n=798)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1505 (IC base=+0.285)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2237` → IC=+0.297 (n=721)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2237 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.301 (n=1243)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.285)

- **PATRÓN** `ibs_15` > `0.8389` → IC=+0.315 (n=1198)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8389 (IC base=+0.285)

- **PATRÓN** `dist_vwap_pct` > `0.2631` → IC=+0.315 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2631 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.379` → IC=+0.384 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.379 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `11995.5068` → IC=+0.304 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11995.5068 (IC base=+0.285)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.303 (n=282)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.278)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.288 (n=290)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.278)

- **PATRÓN** `drift_60min` |x|≤ `0.0587` → IC=+0.315 (n=214)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0587 (IC base=+0.278)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2672` → IC=+0.281 (n=213)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2672 (IC base=+0.278)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3917` → IC=+0.283 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3917 (IC base=+0.278)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.298 (n=671)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.278)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.303 (n=639)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.829 (IC base=+0.278)

- **PATRÓN** `dist_vwap_pct` > `0.2516` → IC=+0.313 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2516 (IC base=+0.278)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.582` → IC=+0.377 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.582 (IC base=+0.278)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.278 (n=827)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `12699.259` → IC=+0.304 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12699.259 (IC base=+0.278)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.306 (n=559)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.1076` → IC=+0.313 (n=373)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1076 (IC base=+0.292)

- **PATRÓN** `delta_ratio_macro` |x|> `0.145` → IC=+0.297 (n=373)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.145 (IC base=+0.292)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.101` → IC=+0.345 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.101 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.309 (n=537)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.292)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.296 (n=509)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.292)

- **PATRÓN** `ibs_15` > `0.8516` → IC=+0.324 (n=559)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8516 (IC base=+0.292)

- **PATRÓN** `dist_vwap_pct` > `0.2797` → IC=+0.319 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2797 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.387` → IC=+0.380 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.387 (IC base=+0.292)

### UPDOWN_OU_5M
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1259` → IC=-0.156 (n=88)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1259
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=267)

- **FILTRO** `ballena_activa_n` > `36.0` → IC=-0.134 (n=241)

  - _Acción_: SKIP cuando `ballena_activa_n` > 36.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=82)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1228` → IC=-0.211 (n=119)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1228
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=368)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.183 (n=121)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=366)

- **FILTRO** `drift_15min` |x|> `0.3082` → IC=-0.141 (n=243)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3082
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=244)

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

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `sigma_h` < `0.0056` → IC=-0.154 (n=24)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0056
  - _Potencial_: sin este filtro IC_bueno=-0.130 (n=25)

- **FILTRO** `ballena_activa_n` > `19.0` → IC=-0.206 (n=32)

  - _Acción_: SKIP cuando `ballena_activa_n` > 19.0
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
- **PATRÓN** `T_h` > `103.5964` → IC=+0.180 (n=479)

  - _Acción_: Kelly boost +0.90€ cuando `T_h` > 103.5964 (IC base=+0.177)

- **PATRÓN** `ratio` < `0.973` → IC=+0.394 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.177)

- **PATRÓN** `T_h` > `115.2222` → IC=+0.355 (n=2471)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 115.2222 (IC base=+0.335)

- **PATRÓN** `ratio` > `1.0219` → IC=+0.378 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0219 (IC base=+0.335)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `111.2289` → IC=+0.161 (n=225)

  - _Acción_: Kelly boost +0.80€ cuando `T_h` > 111.2289 (IC base=+0.144)

- **PATRÓN** `ratio` < `0.9828` → IC=+0.324 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9828 (IC base=+0.144)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.311 (n=861)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.296)

- **PATRÓN** `ratio` > `1.0427` → IC=+0.415 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0427 (IC base=+0.296)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `83.3501` → IC=+0.222 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.219)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.393 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.219)

- **PATRÓN** `T_h` > `111.996` → IC=+0.352 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.996 (IC base=+0.322)

- **PATRÓN** `ratio` > `1.0314` → IC=+0.392 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0314 (IC base=+0.322)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0625` → IC=+0.437 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0625 (IC base=+0.398)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5333 sube el IC de +0.166 a +0.239 en UPDOWN_GBM#15min (n=4029). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7223 sube el IC de +0.206 a +0.273 en UPDOWN_GBM#BTC#15min (n=686). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5178 sube el IC de +0.143 a +0.233 en UPDOWN_GBM#ETH#15min (n=822). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.878 sube el IC de +0.080 a +0.238 en UPDOWN_GBM#SOL#15min (n=326). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5156 sube el IC de +0.194 a +0.273 en UPDOWN_GBM#XRP#15min (n=897). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1071 sube el IC de +0.070 a +0.169 en UPDOWN_GBM#XRP#15min (n=808). Ya aplicado como kelly_boost=+0.85€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6335 sube el IC de -0.068 a +0.280 en UPDOWN_GBM_15M_TARDIO (n=1113). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3677 sube el IC de -0.011 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=3980). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7639 sube el IC de +0.086 a +0.328 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=375). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.618 sube el IC de -0.191 a +0.314 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=68). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5874 sube el IC de +0.153 a +0.247 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=556). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3769 sube el IC de +0.245 a +0.277 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1517). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.189 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3902 sube el IC de -0.036 a +0.291 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=676). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.210 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.1368 sube el IC de -0.024 a +0.312 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=611). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.103 a +0.364 en UPDOWN_GBM_ETH_15M_HORA7 (n=20). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.103 a +0.364 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=20). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8389 sube el IC de +0.285 a +0.315 en UPDOWN_GBM_IBS_ALTO (n=1198). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.278 a +0.303 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=639). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8516 sube el IC de +0.292 a +0.324 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=559). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.364 a +0.397 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=686). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.360 a +0.385 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=346). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7601 sube el IC de +0.367 a +0.406 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=339). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2036 | +0.089 | +220.15€ | 0 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2036 | +0.089 | +220.15€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1644 | +0.092 | +191.42€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1644 | +0.092 | +191.42€ | 0 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 284 | +0.070 | +11.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 284 | +0.070 | +11.30€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 77 | +0.108 | +17.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 77 | +0.108 | +17.77€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 843 | -0.015 | +81.73€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 843 | -0.015 | +81.73€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 649 | -0.041 | +49.51€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 649 | -0.041 | +49.51€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 150 | +0.086 | +25.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 150 | +0.086 | +25.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 38 | +0.025 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 38 | +0.025 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 43141 | -0.083 | -5576.08€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2532 | +0.059 | -275.53€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 40609 | -0.091 | -5300.54€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4610 | -0.117 | -762.28€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4610 | -0.117 | -762.28€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2532 | +0.059 | -275.53€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2532 | +0.059 | -275.53€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4574 | -0.114 | -875.95€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4574 | -0.114 | -875.95€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 11561 | -0.023 | -1186.66€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 11561 | -0.023 | -1186.66€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 11557 | -0.118 | -1112.20€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 11557 | -0.118 | -1112.20€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8307 | -0.124 | -1363.46€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8307 | -0.124 | -1363.46€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 40570 | -0.013 | +3160.81€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 10462 | +0.004 | +1610.53€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 30108 | -0.019 | +1550.28€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 40570 | -0.013 | +3160.81€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 10462 | +0.004 | +1610.53€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 30108 | -0.019 | +1550.28€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 162060 | +0.115 | -6476.61€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 19977 | +0.181 | -663.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 726 | -0.007 | -75.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 131837 | +0.106 | -5414.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 9520 | +0.096 | -323.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 21849 | +0.107 | -1359.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 66 | -0.176 | +7.07€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 21768 | +0.108 | -1354.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 31114 | +0.126 | -496.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5417 | +0.182 | -219.09€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 21839 | +0.120 | -144.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3816 | +0.080 | -110.91€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 21903 | +0.099 | -1527.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 80 | -0.122 | -5.27€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 21808 | +0.101 | -1510.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 34521 | +0.124 | -675.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 8842 | +0.177 | -190.27€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 22155 | +0.106 | -426.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3512 | +0.101 | -49.85€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 30798 | +0.114 | -1452.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5497 | +0.198 | -262.65€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 629 | +0.023 | -21.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 22480 | +0.096 | -1005.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2192 | +0.114 | -162.68€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#XRP | 21875 | +0.107 | -965.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 75 | -0.110 | +6.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 21787 | +0.108 | -971.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 26151 | +0.195 | -1660.72€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 26151 | +0.195 | -1660.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 5926 | +0.177 | -527.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 5926 | +0.177 | -527.90€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 3518 | +0.203 | -89.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 3518 | +0.203 | -89.75€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 5851 | +0.178 | -487.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 5851 | +0.178 | -487.10€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5010 | +0.247 | -184.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5010 | +0.247 | -184.31€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 5767 | +0.186 | -385.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 5767 | +0.186 | -385.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1113 | +0.426 | -38.66€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1113 | +0.426 | -38.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 448 | +0.438 | -5.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 448 | +0.438 | -5.17€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 444 | +0.428 | -12.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 444 | +0.428 | -12.62€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 207 | +0.400 | -17.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 207 | +0.400 | -17.00€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 91795 | +0.201 | -6565.55€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 91795 | +0.201 | -6565.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 15792 | +0.184 | -1650.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 15792 | +0.184 | -1650.67€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 14810 | +0.225 | -493.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 14810 | +0.225 | -493.23€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 15743 | +0.181 | -1649.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 15743 | +0.181 | -1649.59€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 14928 | +0.218 | -594.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 14928 | +0.218 | -594.15€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 15219 | +0.203 | -980.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 15219 | +0.203 | -980.30€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 15303 | +0.198 | -1197.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 15303 | +0.198 | -1197.61€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 35211 | +0.117 | +274.11€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 35211 | +0.117 | +274.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 17511 | +0.119 | +201.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 17511 | +0.119 | +201.10€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 17700 | +0.115 | +73.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 17700 | +0.115 | +73.01€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2266 | +0.293 | -8.15€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2266 | +0.293 | -8.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1040 | +0.280 | -27.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1040 | +0.280 | -27.96€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1099 | +0.299 | +17.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1099 | +0.299 | +17.57€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 127 | +0.337 | +2.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 127 | +0.337 | +2.24€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1038 | +0.444 | +10.16€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1038 | +0.444 | +10.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 504 | +0.437 | -3.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 504 | +0.437 | -3.99€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 486 | +0.453 | +13.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 486 | +0.453 | +13.28€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 48 | +0.400 | +0.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 48 | +0.400 | +0.86€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1783 | +0.069 | -75.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 704 | +0.048 | -60.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1079 | +0.083 | -15.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1362 | +0.076 | -34.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 283 | +0.051 | -19.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1079 | +0.083 | -15.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 339 | +0.031 | -44.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 339 | +0.031 | -44.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 70400 | +0.101 | -1694.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 5676 | +0.092 | +73.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 64724 | +0.102 | -1767.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 38603 | +0.105 | -402.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 5676 | +0.092 | +73.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 32927 | +0.108 | -475.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 14700 | +0.110 | -66.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 14700 | +0.110 | -66.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 17097 | +0.083 | -1225.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 17097 | +0.083 | -1225.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 902 | +0.190 | -109.94€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 902 | +0.190 | -109.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 902 | +0.190 | -109.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 902 | +0.190 | -109.94€ | 2 | 4 |
| ✅ GBM_LATE_15M | 48049 | +0.097 | +25689.61€ | 0 | 17 |
| ✅ GBM_LATE_15M#15min | 48049 | +0.097 | +25689.61€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 7979 | +0.222 | +6770.43€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 7979 | +0.222 | +6770.43€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 7322 | +0.178 | +5696.24€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 7322 | +0.178 | +5696.24€ | 0 | 21 |
| ✅ GBM_LATE_15M#DOGE | 8609 | +0.205 | +6694.90€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 8609 | +0.205 | +6694.90€ | 0 | 19 |
| ✅ GBM_LATE_15M#ETH | 6596 | +0.048 | +1945.86€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 6596 | +0.048 | +1945.86€ | 1 | 16 |
| ✅ GBM_LATE_15M#SOL | 6720 | -0.032 | +1469.78€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 6720 | -0.032 | +1469.78€ | 3 | 12 |
| ✅ GBM_LATE_15M#XRP | 10823 | -0.028 | +3112.40€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 10823 | -0.028 | +3112.40€ | 4 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 51173 | +0.085 | +28307.36€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 51173 | +0.085 | +28307.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 9877 | +0.001 | +5008.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 9877 | +0.001 | +5008.05€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 10975 | +0.008 | +2767.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 10975 | +0.008 | +2767.32€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 7024 | +0.285 | +7724.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 7024 | +0.285 | +7724.78€ | 0 | 23 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 9482 | +0.014 | +2486.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 9482 | +0.014 | +2486.73€ | 1 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 8008 | +0.040 | +3345.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 8008 | +0.040 | +3345.75€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5807 | +0.310 | +6974.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5807 | +0.310 | +6974.74€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 38065 | +0.180 | +31137.00€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 38065 | +0.180 | +31137.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 5750 | +0.237 | +5271.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 5750 | +0.237 | +5271.96€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 5983 | +0.148 | +4495.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 5983 | +0.148 | +4495.77€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 6117 | +0.222 | +5223.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 6117 | +0.222 | +5223.46€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 6491 | +0.136 | +5045.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 6491 | +0.136 | +5045.11€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 7171 | +0.121 | +5292.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 7171 | +0.121 | +5292.06€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 6553 | +0.229 | +5808.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 6553 | +0.229 | +5808.64€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 10102 | +0.126 | +4876.16€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 10102 | +0.126 | +4876.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 455 | +0.161 | +292.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 455 | +0.161 | +292.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2912 | +0.134 | +1602.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2912 | +0.134 | +1602.84€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 481 | +0.152 | +249.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 481 | +0.152 | +249.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3045 | +0.134 | +1456.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3045 | +0.134 | +1456.03€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2554 | +0.096 | +971.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2554 | +0.096 | +971.77€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 655 | +0.133 | +302.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 655 | +0.133 | +302.80€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO | 48309 | +0.186 | +39103.07€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#15min | 48309 | +0.186 | +39103.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 7622 | +0.247 | +7270.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 7622 | +0.247 | +7270.78€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 7603 | +0.145 | +5308.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 7603 | +0.145 | +5308.42€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 8174 | +0.233 | +7291.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 8174 | +0.233 | +7291.89€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 7985 | +0.138 | +5728.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 7985 | +0.138 | +5728.12€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 8584 | +0.118 | +5963.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 8584 | +0.118 | +5963.03€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 8341 | +0.235 | +7540.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 8341 | +0.235 | +7540.82€ | 0 | 21 |
| ✅ GBM_LATE_5M | 12894 | +0.208 | +10337.94€ | 1 | 30 |
| ✅ GBM_LATE_5M#5min | 12894 | +0.208 | +10337.94€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1038 | +0.245 | +980.84€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1038 | +0.245 | +980.84€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3038 | +0.212 | +2644.53€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3038 | +0.212 | +2644.53€ | 0 | 24 |
| ✅ GBM_LATE_5M#DOGE | 1216 | +0.197 | +905.95€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1216 | +0.197 | +905.95€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 3701 | +0.200 | +2711.01€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3701 | +0.200 | +2711.01€ | 0 | 26 |
| ✅ GBM_LATE_5M#SOL | 1948 | +0.202 | +1566.13€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1948 | +0.202 | +1566.13€ | 0 | 23 |
| ✅ GBM_LATE_5M#XRP | 1953 | +0.209 | +1529.48€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1953 | +0.209 | +1529.48€ | 0 | 0 |
| ✅ GBM_LATE_60M | 4115 | +0.057 | +1200.51€ | 0 | 7 |
| ✅ GBM_LATE_60M#60min | 4115 | +0.057 | +1200.51€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1479 | +0.073 | +494.06€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1479 | +0.073 | +494.06€ | 1 | 5 |
| ✅ GBM_LATE_60M#ETH | 1337 | +0.058 | +417.57€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1337 | +0.058 | +417.57€ | 0 | 7 |
| ✅ GBM_LATE_60M#SOL | 1299 | +0.039 | +288.88€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1299 | +0.039 | +288.88€ | 0 | 11 |
| 🚫 GBM_LATE_60M_FADE | 634 | -0.250 | -30.50€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 634 | -0.250 | -30.50€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 236 | -0.248 | -17.12€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 236 | -0.248 | -17.12€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 228 | -0.243 | -5.46€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 228 | -0.243 | -5.46€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 170 | -0.256 | -7.92€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 170 | -0.256 | -7.92€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1708 | +0.083 | +416.05€ | 1 | 12 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1708 | +0.083 | +416.05€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 665 | +0.077 | +155.88€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 665 | +0.077 | +155.88€ | 1 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 593 | +0.055 | +92.25€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 593 | +0.055 | +92.25€ | 2 | 13 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 450 | +0.126 | +167.92€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 450 | +0.126 | +167.92€ | 2 | 11 |
| ✅ LATE_WINDOW_5MIN | 182 | +0.272 | +176.44€ | 1 | 13 |
| ✅ LATE_WINDOW_5MIN#5min | 182 | +0.272 | +176.44€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 182 | +0.272 | +176.44€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 182 | +0.272 | +176.44€ | 1 | 13 |
| ✅ LEADLAG_BTC_XRP_15M | 3825 | +0.099 | +905.74€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3825 | +0.099 | +905.74€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3825 | +0.099 | +905.74€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3825 | +0.099 | +905.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 713 | -0.018 | -3.53€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 713 | -0.018 | -3.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 6 | -0.037 | -1.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 6 | -0.037 | -1.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 216 | -0.009 | +4.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 216 | -0.009 | +4.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 27 | -0.155 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 27 | -0.155 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 177 | +0.025 | +6.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 177 | +0.025 | +6.00€ | 2 | 1 |
| ✅ LIQUIDACIONES_15M#SOL | 235 | -0.002 | +2.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 235 | -0.002 | +2.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 3953 | +0.017 | +98.38€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3953 | +0.017 | +98.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 185 | +0.029 | -0.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 185 | +0.029 | -0.77€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 814 | +0.015 | +39.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 814 | +0.015 | +39.58€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 214 | -0.005 | -1.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 214 | -0.005 | -1.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1509 | +0.022 | +30.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1509 | +0.022 | +30.04€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 761 | +0.011 | +1.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 761 | +0.011 | +1.65€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 470 | +0.015 | +29.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 470 | +0.015 | +29.46€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1972 | -0.038 | -26.19€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1972 | -0.038 | -26.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 589 | -0.030 | -12.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 589 | -0.030 | -12.21€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 683 | -0.015 | +7.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 683 | -0.015 | +7.12€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 700 | -0.067 | -21.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 700 | -0.067 | -21.10€ | 6 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 11100 | -0.029 | -22.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 5313 | -0.033 | -59.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 5787 | -0.025 | +36.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 341 | -0.036 | -7.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 174 | -0.011 | +5.31€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 167 | -0.062 | -13.02€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 2864 | -0.018 | +37.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1360 | -0.021 | +10.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1504 | -0.016 | +26.94€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1167 | -0.024 | +19.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 594 | -0.032 | +0.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 573 | -0.017 | +18.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 2463 | -0.039 | -64.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1160 | -0.046 | -50.91€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1303 | -0.032 | -13.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 2143 | -0.023 | +27.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1034 | -0.028 | +2.71€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1109 | -0.018 | +24.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 2122 | -0.039 | -35.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 991 | -0.046 | -27.78€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1131 | -0.033 | -7.41€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 56689 | -0.000 | +2902.84€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 56689 | -0.000 | +2902.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 10246 | +0.027 | +1325.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 10246 | +0.027 | +1325.90€ | 2 | 4 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 8063 | -0.035 | -124.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 8063 | -0.035 | -124.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 10369 | +0.024 | +1066.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 10369 | +0.024 | +1066.26€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 7949 | -0.047 | -143.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 7949 | -0.047 | -143.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 9608 | -0.005 | +254.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 9608 | -0.005 | +254.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 10454 | +0.017 | +523.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 10454 | +0.017 | +523.86€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6858 | -0.057 | -148.14€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6858 | -0.057 | -148.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1235 | -0.002 | -17.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1235 | -0.002 | -17.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1873 | -0.071 | -36.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1873 | -0.071 | -36.08€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 63 | -0.038 | -1.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 63 | -0.038 | -1.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 789 | -0.119 | -34.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 789 | -0.119 | -34.09€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2040 | -0.070 | -33.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2040 | -0.070 | -33.04€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 858 | -0.016 | -26.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 858 | -0.016 | -26.02€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3372 | +0.004 | -0.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3372 | +0.004 | -0.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 132 | -0.037 | -1.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 132 | -0.037 | -1.23€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 194 | +0.010 | -0.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 194 | +0.010 | -0.77€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1325 | +0.006 | +6.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1325 | +0.006 | +6.88€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1391 | +0.007 | -0.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1391 | +0.007 | -0.19€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 191 | -0.008 | -2.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 191 | -0.008 | -2.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 139967 | -0.077 | +1800.93€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 139967 | -0.077 | +1800.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 24404 | -0.079 | +1290.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 24404 | -0.079 | +1290.43€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 21012 | -0.100 | -1007.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 21012 | -0.100 | -1007.42€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 24720 | -0.069 | +1214.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 24720 | -0.069 | +1214.24€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 20557 | -0.097 | -645.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 20557 | -0.097 | -645.05€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 25104 | -0.057 | +304.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 25104 | -0.057 | +304.32€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 24170 | -0.069 | +644.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 24170 | -0.069 | +644.41€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8903 | -0.034 | -182.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8903 | -0.034 | -182.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1002 | -0.017 | -19.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1002 | -0.017 | -19.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2049 | -0.048 | -29.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2049 | -0.048 | -29.48€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2614 | -0.026 | -40.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2614 | -0.026 | -40.42€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1233 | -0.059 | -29.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1233 | -0.059 | -29.17€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 996 | -0.030 | -31.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 996 | -0.030 | -31.63€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 1868 | +0.122 | +755.26€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 1732 | +0.127 | +742.67€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 405 | +0.127 | +185.47€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 405 | +0.127 | +185.47€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 359 | +0.112 | +118.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 359 | +0.112 | +118.24€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#ETH | 333 | +0.142 | +170.51€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 333 | +0.142 | +170.51€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 303 | +0.152 | +168.78€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 303 | +0.152 | +168.78€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 332 | +0.102 | +99.67€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 332 | +0.102 | +99.67€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1730 | -0.017 | -24.63€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1730 | -0.017 | -24.63€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 330 | -0.003 | +6.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 330 | -0.003 | +6.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 312 | -0.032 | -8.58€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 312 | -0.032 | -8.58€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 437 | -0.047 | -34.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 437 | -0.047 | -34.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 363 | +0.007 | +5.16€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 363 | +0.007 | +5.16€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 288 | -0.003 | +7.56€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 288 | -0.003 | +7.56€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 999 | -0.074 | -48.57€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 463 | -0.109 | -79.28€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 361 | -0.134 | -65.20€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 102 | -0.019 | -14.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 350 | -0.034 | +23.81€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 252 | -0.024 | +27.39€ | 2 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 98 | -0.060 | -3.59€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 186 | -0.064 | +6.91€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 154 | -0.070 | +3.03€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 32 | -0.029 | +3.88€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 767 | -0.085 | -34.78€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 232 | -0.038 | -13.79€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1239 | -0.208 | -79.67€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 484 | -0.210 | -48.32€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 426 | -0.213 | -47.58€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 58 | -0.183 | -0.74€ | 1 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 418 | -0.212 | -36.30€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 369 | -0.222 | -42.80€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 49 | -0.128 | +6.50€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 337 | -0.199 | +4.95€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 314 | -0.196 | +2.23€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 23 | -0.220 | +2.71€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1109 | -0.212 | -88.14€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 130 | -0.174 | +8.47€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 485 | +0.389 | +464.78€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#BTC | 80 | +0.171 | +63.15€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 80 | +0.171 | +63.15€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#ETH | 112 | +0.360 | +101.13€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 112 | +0.360 | +101.13€ | 0 | 7 |
| ✅ RESOLUTION_SNIPER#SOL | 293 | +0.456 | +300.51€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 293 | +0.456 | +300.51€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 485 | +0.389 | +464.78€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 802 | +0.041 | +74.49€ | 2 | 4 |
| ✅ STREAK_FADE_15M#15min | 802 | +0.041 | +74.49€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 309 | +0.024 | +4.68€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 309 | +0.024 | +4.68€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 67 | -0.007 | -1.40€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 67 | -0.007 | -1.40€ | 1 | 0 |
| ✅ STREAK_FADE_15M#SOL | 79 | +0.006 | +4.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 79 | +0.006 | +4.43€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 347 | +0.073 | +66.77€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 347 | +0.073 | +66.77€ | 1 | 7 |
| ✅ STREAK_FADE_5M | 3533 | -0.023 | -141.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3533 | -0.023 | -141.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 599 | -0.029 | -27.49€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 599 | -0.029 | -27.49€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 168 | -0.041 | -14.30€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 168 | -0.041 | -14.30€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1639 | -0.019 | -59.97€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1639 | -0.019 | -59.97€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 104 | -0.047 | -7.89€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 104 | -0.047 | -7.89€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 43 | -0.100 | -5.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 43 | -0.100 | -5.07€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 61 | -0.008 | -2.82€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 61 | -0.008 | -2.82€ | 0 | 3 |
| ✅ STREAK_MOM_5M | 11328 | +0.015 | +74.62€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11328 | +0.015 | +74.62€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2905 | +0.019 | +25.69€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2905 | +0.019 | +25.69€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2938 | +0.017 | +34.69€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2938 | +0.017 | +34.69€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2907 | +0.008 | -3.40€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2907 | +0.008 | -3.40€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2578 | +0.014 | +17.65€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2578 | +0.014 | +17.65€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 10455 | +0.013 | -49.83€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 10455 | +0.013 | -49.83€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4344 | +0.019 | -4.40€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4344 | +0.019 | -4.40€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3624 | +0.010 | -29.12€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3624 | +0.010 | -29.12€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2487 | +0.009 | -16.31€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2487 | +0.009 | -16.31€ | 1 | 0 |
| ✅ UPDOWN_GBM | 85931 | +0.056 | +7745.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 20822 | +0.083 | +4488.69€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2717 | +0.003 | +32.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 56954 | +0.054 | +3133.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 5129 | +0.004 | +96.29€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 7014 | +0.093 | +1136.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1576 | +0.156 | +698.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5361 | +0.076 | +439.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 19628 | +0.057 | +1697.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2849 | +0.085 | +661.89€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 756 | +0.005 | +14.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 13603 | +0.064 | +950.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2309 | +0.002 | +68.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 111 | -0.075 | +1.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 9084 | +0.071 | +951.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1555 | +0.147 | +610.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 7451 | +0.055 | +342.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 20403 | +0.047 | +1376.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 5088 | +0.072 | +784.76€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 727 | +0.007 | +18.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 12628 | +0.046 | +553.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1856 | +0.006 | +18.67€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 104 | -0.104 | +1.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 18657 | +0.036 | +1000.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 5331 | +0.035 | +425.60€ | 0 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 691 | -0.009 | +2.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 11579 | +0.042 | +571.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 964 | +0.005 | +9.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 92 | -0.138 | -7.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 11143 | +0.069 | +1582.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4423 | +0.104 | +1307.40€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 6332 | +0.048 | +275.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 307 | -0.105 | -3.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 912 | +0.364 | +328.48€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 912 | +0.364 | +328.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 461 | +0.360 | +154.81€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 461 | +0.360 | +154.81€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 451 | +0.367 | +173.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 451 | +0.367 | +173.67€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 21336 | -0.023 | +5059.55€ | 3 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 21336 | -0.023 | +5059.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3976 | -0.114 | +149.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3976 | -0.114 | +149.53€ | 4 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2763 | +0.220 | +1786.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2763 | +0.220 | +1786.89€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 6084 | -0.063 | +795.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 6084 | -0.063 | +795.35€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5847 | -0.064 | +1054.51€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5847 | -0.064 | +1054.51€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 260 | +0.065 | +27.24€ | 0 | 8 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 260 | +0.065 | +27.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 260 | +0.065 | +27.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 260 | +0.065 | +27.24€ | 0 | 8 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1597 | +0.285 | +1326.76€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1597 | +0.285 | +1326.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 852 | +0.278 | +660.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 852 | +0.278 | +660.45€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 745 | +0.292 | +666.31€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 745 | +0.292 | +666.31€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 842 | -0.114 | -84.99€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#5min | 842 | -0.114 | -84.99€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 259 | -0.086 | -20.70€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 259 | -0.086 | -20.70€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 94 | -0.167 | -10.43€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 94 | -0.167 | -10.43€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 106 | -0.176 | -4.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 106 | -0.176 | -4.51€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 4028 | +0.301 | +1862.38€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1507 | +0.256 | +178.97€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1546 | +0.295 | +672.43€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 975 | +0.380 | +1010.98€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.023 n=1076 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1076 IC=+0.023 PNL=+50.15€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 755 celda(s) pasan gate riguroso completo de 2777 evaluadas (n>=40) y 3851 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.035 < 0.08 — monitorear
  - _Datos_: n=5330 IC=+0.035 PNL=+423.67€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1546/15 IC=+0.295 PNL=+672.43€ | BTC: n=1507/15 IC=+0.256 PNL=+178.97€ | SOL: n=975/15 IC=+0.380 PNL=+1010.98€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.141 n=882/60 | contraria IC=+0.188 n=912 | gap=-0.047 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=512, boost estimado=+0.017. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1856/40 IC=+0.006 PNL=+18.67€ | BTC#60min: n=2309/40 IC=+0.002 PNL=+68.60€ | SOL#60min: n=964/40 IC=+0.005 PNL=+9.03€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.047 n=622360 | tras_1loss IC=+0.097 n=472355 | tras_2loss IC=+0.067 n=190301/40 | gap=-0.020 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.189 > 0.08 con n=837 PNL=+602.55€
  - _Datos_: n=837 IC=+0.189 PNL=+602.55€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.158 > 0.08 con n=963 PNL=+521.09€
  - _Datos_: n=963 IC=+0.158 PNL=+521.09€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.162 > 0.08 con n=69 PNL=+34.91€
  - _Datos_: n=69 IC=+0.162 PNL=+34.91€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.332 > 0.1 con n=3290 PNL=+1825.23€
  - _Datos_: n=3290 IC=+0.332 PNL=+1825.23€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=836 IC=+0.069 PNL=+85.67€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=836 IC=+0.069 PNL=+85.67€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=94 IC=+0.198 PNL=+68.74€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=94 IC=+0.198 PNL=+68.74€

**⏳ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: 30
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

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
  - _Estado_: n=3453 IC=+0.006 PNL=+4.83€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3453 IC=+0.006 PNL=+4.83€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1676 IC=+0.000 PNL=+91.46€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1676 IC=+0.000 PNL=+91.46€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1076 IC=+0.023 PNL=+50.15€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1076 IC=+0.023 PNL=+50.15€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.166 > 0.1 con n=5363 PNL=+3151.04€
  - _Datos_: n=5363 IC=+0.166 PNL=+3151.04€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=2846 IC=+0.086 PNL=+660.91€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=2846 IC=+0.086 PNL=+660.91€

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
  - _Estado_: n=1093 IC=+0.041 PNL=+91.39€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1093 IC=+0.041 PNL=+91.39€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=140 IC=+0.000 PNL=-0.29€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=140 IC=+0.000 PNL=-0.29€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.272 n=182) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=182 IC=+0.272 PNL=+176.44€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.123 > 0.02 con n=1087 PNL=+449.53€
  - _Datos_: n=1087 IC=+0.123 PNL=+449.53€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=226 IC=-0.097 PNL=+16.29€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=226 IC=-0.097 PNL=+16.29€

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
  - _Estado_: n=34339 IC=+0.073 PNL=+4840.94€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=34339 IC=+0.073 PNL=+4840.94€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.135 < -0.1 con n=600 PNL=+84.60€
  - _Datos_: n=600 IC=-0.135 PNL=+84.60€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=3227 IC=+0.070 PNL=+431.26€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=3227 IC=+0.070 PNL=+431.26€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=162 IC=-0.104 PNL=+1.68€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=162 IC=-0.104 PNL=+1.68€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.111 > 0.1 con n=915 PNL=+247.96€
  - _Datos_: n=915 IC=+0.111 PNL=+247.96€

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
  - _Estado_: n=36617 IC=-0.135 PNL=+2658.96€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=36617 IC=-0.135 PNL=+2658.96€

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
  - _Estado_: n=3758 IC=+0.131 PNL=+2391.21€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=3758 IC=+0.131 PNL=+2391.21€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=8848 IC=+0.054 PNL=+723.24€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=8848 IC=+0.054 PNL=+723.24€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.099 > 0.08 con n=3913 PNL=+2184.21€
  - _Datos_: n=3913 IC=+0.099 PNL=+2184.21€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.220 < -0.1 con n=3870 PNL=-315.66€
  - _Datos_: n=3870 IC=-0.220 PNL=-315.66€

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
  - _Estado_: n=77 IC=+0.032 PNL=+11.84€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=77 IC=+0.032 PNL=+11.84€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.099 n=1937) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1937 IC=+0.099 PNL=+408.30€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.407 n=625) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=625 IC=+0.407 PNL=+892.67€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=15782 IC=+0.184 PNL=-1649.51€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=15782 IC=+0.184 PNL=-1649.51€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.231 > 0.1 con n=251 PNL=+175.16€
  - _Datos_: n=251 IC=+0.231 PNL=+175.16€
