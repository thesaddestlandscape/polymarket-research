# Hipótesis automáticas — 2026-10-30 14:08 UTC
_Generado por shadow_postmortem.py sobre 1120340 resoluciones (PNL=+149935.62€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.224 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.133)

- **PATRÓN** `n_total_lado` > `63.0` → IC=+0.187 (n=311)

  - _Acción_: Kelly boost +0.93€ cuando `n_total_lado` > 63.0 (IC base=+0.133)

- **PATRÓN** `banda_hit_calibrado` > `0.6165` → IC=+0.254 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6165 (IC base=+0.133)

- **PATRÓN** `banda_z` > `8.854` → IC=+0.212 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.854 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.157 (n=333)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=992)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `2299.9574` → IC=+0.137 (n=912)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2299.9574 (IC base=+0.133)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.219 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.137)

- **PATRÓN** `n_total_lado` > `67.0` → IC=+0.194 (n=263)

  - _Acción_: Kelly boost +0.97€ cuando `n_total_lado` > 67.0 (IC base=+0.137)

- **PATRÓN** `banda_hit_calibrado` > `0.6119` → IC=+0.246 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6119 (IC base=+0.137)

- **PATRÓN** `banda_z` > `9.174` → IC=+0.203 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.174 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=281)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=892)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2713.1399` → IC=+0.139 (n=781)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2713.1399 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `9129.2915` → IC=+0.124 (n=216)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 9129.2915 (IC base=+0.009)

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
- **FILTRO** `restante_s_al_confirmar` < `137.69` → IC=-0.208 (n=10927)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 137.69
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=32781)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `127.3` → IC=-0.260 (n=1154)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.3
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=3465)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `117.67` → IC=-0.303 (n=1148)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 117.67
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3447)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `160.38` → IC=-0.234 (n=2943)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 160.38
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=8829)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `131.73` → IC=-0.260 (n=2100)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.73
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=6303)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.212 (n=24457)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=4692)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `8682.2161` → IC=+0.163 (n=2165)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 8682.2161 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.127 (n=20892)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=25563)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.225 (n=19402)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=7740)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6747.5472` → IC=+0.152 (n=2994)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 6747.5472 (IC base=+0.124)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=2136)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.364 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.181)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.185 (n=2612)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `9416.0594` → IC=+0.183 (n=1818)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 9416.0594 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.187 (n=1863)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.184 (n=2082)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` < `0.295` → IC=+0.312 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.295 (IC base=+0.181)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=2668)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `16179.5763` → IC=+0.187 (n=688)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 16179.5763 (IC base=+0.181)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.171 (n=523)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.61 (IC base=+0.076)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.141 (n=1250)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.44 (IC base=+0.083)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=4719)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.164 (n=4010)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 15.0 (IC base=+0.161)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.373 (n=1538)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.213 (n=2121)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.349 (n=778)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=2466)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=1194)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.150 (n=1016)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 15.0 (IC base=+0.144)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.264 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.145 (n=1311)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `2240.1708` → IC=+0.157 (n=517)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2240.1708 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `3079.6088` → IC=+0.132 (n=229)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 3079.6088 (IC base=+0.070)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.251 (n=895)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.226)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1258)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.147 (n=1357)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.153 (n=708)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.145)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.286 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=901)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.145)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `py_entrada` > `0.555` → IC=+0.170 (n=431)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.555 (IC base=+0.067)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.132 (n=1295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.244 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.123)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.297 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=142)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=20910)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.200 (n=17759)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.229 (n=8641)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.197)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.181 (n=2258)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.177 (n=4769)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 18.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.182 (n=4610)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.176)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.217 (n=2644)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.218 (n=2359)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.215)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.293 (n=896)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.215)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.182 (n=4711)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.179 (n=4013)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.177 (n=4897)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.73 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=3666)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.255 (n=4023)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.247)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.248 (n=3420)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.247)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.357 (n=1355)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=4616)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.190 (n=3942)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.189 (n=3431)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.186)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.428 (n=787)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.424)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.427 (n=878)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.424)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=887)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.424)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=922)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.424)

- **PATRÓN** `libro_liquidez` > `4364.3671` → IC=+0.442 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4364.3671 (IC base=+0.424)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.442 (n=359)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

- **PATRÓN** `libro_liquidez` > `12510.8319` → IC=+0.445 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12510.8319 (IC base=+0.437)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.431 (n=229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.430 (n=343)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `4630.8744` → IC=+0.439 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4630.8744 (IC base=+0.425)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=27189)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.245 (n=27467)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.201)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=4690)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.183 (n=8730)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 12.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.196 (n=12343)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.71 (IC base=+0.183)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=5654)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.225 (n=5591)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.286 (n=3927)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.186 (n=4669)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.199 (n=9606)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=5712)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=4378)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.272 (n=3858)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `12.0` → IC=+0.206 (n=7826)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.259 (n=4038)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=4522)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.201 (n=4541)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=4734)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=9774)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=9984)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.38` → IC=+0.138 (n=9050)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.38 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=4804)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.118)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.144 (n=4544)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=5991)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.118)

- **PATRÓN** `lag_apertura_s` < `2.64` → IC=+0.144 (n=4489)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 2.64 (IC base=+0.118)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.191 (n=4970)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.115)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.135 (n=5440)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.115)

- **PATRÓN** `lag_apertura_s` < `3.25` → IC=+0.136 (n=5986)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.25 (IC base=+0.115)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.303 (n=1834)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.295)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.388 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.295)

- **PATRÓN** `libro_liquidez` > `3872.2908` → IC=+0.295 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3872.2908 (IC base=+0.295)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.289 (n=833)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.282)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.364 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `5132.4682` → IC=+0.301 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5132.4682 (IC base=+0.282)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.326 (n=595)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.301)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.304 (n=870)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.301)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.399 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.301)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.301 (n=989)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.301)

- **PATRÓN** `libro_liquidez` > `2156.9758` → IC=+0.323 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2156.9758 (IC base=+0.301)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.448 (n=841)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.444)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.445 (n=832)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.444)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.452 (n=809)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.444)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.440 (n=399)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.438)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.439 (n=275)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.439 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.441 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.438)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.471 (n=134)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.452)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.454 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.452)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.456 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.452)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.453 (n=297)

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
- **FILTRO** `py_entrada` > `0.735` → IC=-0.381 (n=40)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=83)

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
- **FILTRO** `py_entrada` > `0.735` → IC=-0.381 (n=40)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=83)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4777` → IC=+0.139 (n=15317)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4777 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.125 (n=15466)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.125 (n=10721)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.375` → IC=+0.165 (n=15319)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.375 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.7827` → IC=+0.279 (n=856)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7827 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.829` → IC=+0.190 (n=5809)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 5.829 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `0.6217` → IC=+0.265 (n=4497)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6217 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.3034` → IC=+0.246 (n=1579)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3034 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` > `2.3495` → IC=+0.229 (n=4966)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3495 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=7807)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `4381.0798` → IC=+0.151 (n=5106)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4381.0798 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.122 (n=9537)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0059 (IC base=+0.080)

- **PATRÓN** `ibs_20min` < `0.5658` → IC=+0.143 (n=19058)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5658 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` > `0.6084` → IC=+0.189 (n=1279)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.6084 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` < `0.1607` → IC=+0.189 (n=7340)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.1607 (IC base=+0.080)

- **PATRÓN** `volumen_regimen` < `0.864` → IC=+0.190 (n=5102)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.864 (IC base=+0.080)

- **PATRÓN** `volumen_pendiente_norm` > `0.2969` → IC=+0.231 (n=1886)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2969 (IC base=+0.080)

- **PATRÓN** `volumen_spike_ratio` > `2.6832` → IC=+0.208 (n=4327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6832 (IC base=+0.080)

- **PATRÓN** `ballena_activa_n` < `105.0` → IC=+0.225 (n=12870)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 105.0 (IC base=+0.080)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3611` → IC=+0.210 (n=3301)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3611 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.218 (n=1599)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.210 (n=2218)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `0.9831` → IC=+0.280 (n=1497)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9831 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.683` → IC=+0.280 (n=1465)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.683 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.2834` → IC=+0.259 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2834 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `1.4375` → IC=+0.207 (n=3159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4375 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.220 (n=3608)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `2042.9486` → IC=+0.206 (n=1101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2042.9486 (IC base=+0.206)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.224 (n=1971)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0095` → IC=+0.242 (n=2846)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0095 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.0884` → IC=+0.276 (n=949)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0884 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.244 (n=2965)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.5504` → IC=+0.259 (n=2845)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5504 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` < `0.0955` → IC=+0.243 (n=2568)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0955 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.2919` → IC=+0.261 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2919 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `2.2793` → IC=+0.240 (n=2377)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2793 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `1.8644` → IC=+0.243 (n=1801)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8644 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.242 (n=3255)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1475.9` → IC=+0.243 (n=2541)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1475.9 (IC base=+0.240)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.238 (n=913)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.0799` → IC=+0.259 (n=912)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0799 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.238 (n=2861)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.227 (n=1951)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.9278` → IC=+0.269 (n=912)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9278 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `0.1308` → IC=+0.233 (n=1431)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1308 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.181` → IC=+0.258 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.181 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` < `1.2278` → IC=+0.227 (n=2737)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2278 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `0.6236` → IC=+0.230 (n=2736)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6236 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2788` → IC=+0.273 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2788 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.4025` → IC=+0.228 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4025 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `2.4315` → IC=+0.255 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4315 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.170 (n=1950)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0042 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.0778` → IC=+0.164 (n=973)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.0778 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.155 (n=1083)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.718` → IC=+0.171 (n=2919)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.718 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.1394` → IC=+0.149 (n=2772)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1394 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.904` → IC=+0.139 (n=475)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 10.904 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.062` → IC=+0.137 (n=2663)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 4.062 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `1.204` → IC=+0.138 (n=2919)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.204 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.0973` → IC=+0.154 (n=1062)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.0973 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.523` → IC=+0.142 (n=1230)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.523 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.7941` → IC=+0.132 (n=1863)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.7941 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=3785)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `206.0` → IC=+0.171 (n=1202)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 206.0 (IC base=+0.130)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.210 (n=1573)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.198 (n=3644)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=3113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.264 (n=1343)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.118` → IC=+0.280 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.118 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` < `0.0969` → IC=+0.195 (n=3090)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0969 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` > `0.352` → IC=+0.218 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.352 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `2.7032` → IC=+0.208 (n=1532)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7032 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.197 (n=4160)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `1920.54` → IC=+0.202 (n=1573)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1920.54 (IC base=+0.192)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.221 (n=2781)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.1786` → IC=+0.232 (n=1390)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1786 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=1186)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.219 (n=1445)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` < `0.0347` → IC=+0.269 (n=1053)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0347 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.125` → IC=+0.260 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.125 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.3492` → IC=+0.262 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3492 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.7601` → IC=+0.227 (n=1370)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7601 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.225 (n=1594)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `1910.02` → IC=+0.223 (n=1432)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1910.02 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.220 (n=1996)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.218)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.149 (n=169)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=4187)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.159 (n=599)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0037 (IC base=+0.059)

- **PATRÓN** `ibs_20min` > `0.9509` → IC=+0.237 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9509 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.1401` → IC=+0.335 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1401 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` < `0.3359` → IC=+0.329 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3359 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.227` → IC=+0.198 (n=1301)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 5.227 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` > `0.6945` → IC=+0.339 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6945 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.3037` → IC=+0.339 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3037 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` < `1.8675` → IC=+0.336 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8675 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` > `2.2614` → IC=+0.336 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2614 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.333 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 143.0 (IC base=+0.059)

- **PATRÓN** `ibs_20min` < `0.0911` → IC=+0.184 (n=1090)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.0911 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` > `0.7312` → IC=+0.165 (n=258)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.7312 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` < `0.1361` → IC=+0.144 (n=1877)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1361 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` < `0.8365` → IC=+0.159 (n=1345)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8365 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.211 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` < `1.7775` → IC=+0.149 (n=1293)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.7775 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` > `2.1558` → IC=+0.165 (n=879)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.1558 (IC base=+0.046)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.177 (n=122)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=646)

- **FILTRO** `ibs_20min` < `0.2647` → IC=-0.168 (n=191)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2647
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=577)

- **FILTRO** `ibs_20min` > `0.2063` → IC=-0.132 (n=4095)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2063
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=2018)

- **FILTRO** `sigma_ewma_delta_pct` > `8.51` → IC=-0.227 (n=658)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.51
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=5455)

- **PATRÓN** `ibs_20min` > `0.7619` → IC=+0.171 (n=262)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.7619 (IC base=+0.019)

- **PATRÓN** `dist_vwap_pct` > `0.9803` → IC=+0.286 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9803 (IC base=+0.019)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.099` → IC=+0.129 (n=238)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 3.099 (IC base=+0.019)

- **PATRÓN** `volumen_regimen` < `0.871` → IC=+0.261 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.871 (IC base=+0.019)

- **PATRÓN** `volumen_regimen` > `1.0359` → IC=+0.290 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0359 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` < `0.1597` → IC=+0.280 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1597 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` < `2.4948` → IC=+0.288 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4948 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` > `1.5504` → IC=+0.263 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5504 (IC base=+0.019)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.270 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.019)

- **PATRÓN** `ibs_20min` < `0.2063` → IC=+0.152 (n=2018)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.2063 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` < `0.1963` → IC=+0.278 (n=875)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1963 (IC base=-0.038)

- **PATRÓN** `volumen_regimen` < `0.695` → IC=+0.310 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.695 (IC base=-0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.0793` → IC=+0.296 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0793 (IC base=-0.038)

- **PATRÓN** `volumen_spike_ratio` < `2.456` → IC=+0.306 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.456 (IC base=-0.038)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.5999` → IC=-0.183 (n=1147)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.5999
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=3443)

- **FILTRO** `ibs_20min` < `0.7664` → IC=-0.155 (n=3029)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7664
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=1561)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.168 (n=1067)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=3523)

- **FILTRO** `ibs_20min` > `0.7458` → IC=-0.197 (n=1627)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7458
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=4885)

- **PATRÓN** `dist_vwap_pct` > `1.0623` → IC=+0.352 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0623 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` < `0.2524` → IC=+0.307 (n=730)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2524 (IC base=-0.065)

- **PATRÓN** `volumen_regimen` > `0.7043` → IC=+0.322 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7043 (IC base=-0.065)

- **PATRÓN** `volumen_pendiente_norm` < `0.1024` → IC=+0.306 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1024 (IC base=-0.065)

- **PATRÓN** `volumen_spike_ratio` < `1.4259` → IC=+0.316 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4259 (IC base=-0.065)

- **PATRÓN** `volumen_spike_ratio` > `1.8567` → IC=+0.313 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8567 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` > `0.8099` → IC=+0.279 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8099 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` < `0.7265` → IC=+0.269 (n=815)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7265 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` > `1.064` → IC=+0.285 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.064 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.1051` → IC=+0.282 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1051 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `2.1725` → IC=+0.266 (n=1519)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1725 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `1.4281` → IC=+0.266 (n=1726)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4281 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.205 (n=6670)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.092)

- **PATRÓN** `ibs_20min` > `0.875` → IC=+0.286 (n=9090)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.875 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` > `0.9388` → IC=+0.302 (n=1441)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9388 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.565` → IC=+0.165 (n=8958)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.565 (IC base=+0.092)

- **PATRÓN** `volumen_regimen` < `1.1737` → IC=+0.267 (n=7351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1737 (IC base=+0.092)

- **PATRÓN** `volumen_regimen` > `0.6916` → IC=+0.275 (n=6568)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6916 (IC base=+0.092)

- **PATRÓN** `volumen_pendiente_norm` > `0.24` → IC=+0.287 (n=2205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.24 (IC base=+0.092)

- **PATRÓN** `volumen_spike_ratio` > `2.6488` → IC=+0.279 (n=3892)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6488 (IC base=+0.092)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.303 (n=11276)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 91.0 (IC base=+0.092)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.158 (n=6458)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0098 (IC base=+0.078)

- **PATRÓN** `ibs_20min` < `0.6471` → IC=+0.149 (n=19345)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.6471 (IC base=+0.078)

- **PATRÓN** `volumen_regimen` < `0.7051` → IC=+0.268 (n=2763)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7051 (IC base=+0.078)

- **PATRÓN** `volumen_regimen` > `1.1951` → IC=+0.270 (n=2091)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1951 (IC base=+0.078)

- **PATRÓN** `volumen_pendiente_norm` > `0.2941` → IC=+0.321 (n=1358)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2941 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` < `1.5781` → IC=+0.295 (n=4014)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5781 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` > `2.2761` → IC=+0.289 (n=4133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2761 (IC base=+0.078)

- **PATRÓN** `ballena_activa_n` < `75.0` → IC=+0.301 (n=9053)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 75.0 (IC base=+0.078)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.5792` → IC=-0.156 (n=2719)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5792
  - _Potencial_: sin este filtro IC_bueno=+0.203 (n=2720)

- **FILTRO** `ibs_20min` > `0.7241` → IC=-0.221 (n=1177)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7241
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=3534)

- **FILTRO** `sigma_ewma_delta_pct` > `4.287` → IC=-0.224 (n=1017)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.287
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=3694)

- **PATRÓN** `ibs_20min` > `0.9275` → IC=+0.331 (n=1360)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9275 (IC base=+0.024)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.105` → IC=+0.182 (n=1827)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 3.105 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.2294` → IC=+0.319 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2294 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `1.4484` → IC=+0.267 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4484 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` > `2.2535` → IC=+0.290 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2535 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.309 (n=1190)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.024)

- **PATRÓN** `ibs_20min` < `0.1685` → IC=+0.159 (n=1178)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.1685 (IC base=-0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.0729` → IC=+0.410 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0729 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.6476` → IC=+0.411 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6476 (IC base=-0.026)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.402 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=-0.026)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1193` → IC=+0.221 (n=978)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1193 (IC base=+0.018)

- **PATRÓN** `volumen_regimen` < `1.1951` → IC=+0.204 (n=1963)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1951 (IC base=+0.018)

- **PATRÓN** `volumen_regimen` > `0.6925` → IC=+0.209 (n=1755)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6925 (IC base=+0.018)

- **PATRÓN** `volumen_pendiente_norm` > `0.2774` → IC=+0.251 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2774 (IC base=+0.018)

- **PATRÓN** `volumen_spike_ratio` < `1.4212` → IC=+0.232 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4212 (IC base=+0.018)

- **PATRÓN** `volumen_spike_ratio` > `2.4465` → IC=+0.210 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4465 (IC base=+0.018)

- **PATRÓN** `ballena_activa_n` < `267.0` → IC=+0.238 (n=1296)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 267.0 (IC base=+0.018)

- **PATRÓN** `dist_vwap_pct` < `0.1261` → IC=+0.247 (n=1360)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1261 (IC base=-0.002)

- **PATRÓN** `volumen_regimen` < `1.1702` → IC=+0.237 (n=1344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1702 (IC base=-0.002)

- **PATRÓN** `volumen_regimen` > `0.623` → IC=+0.242 (n=1344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.623 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2713` → IC=+0.302 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2713 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.5357` → IC=+0.243 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5357 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.1545` → IC=+0.253 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1545 (IC base=-0.002)

- **PATRÓN** `ballena_activa_n` < `214.0` → IC=+0.249 (n=575)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 214.0 (IC base=-0.002)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.320 (n=1295)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.276)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.284 (n=2854)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.276)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.317 (n=1542)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.276)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.678` → IC=+0.308 (n=941)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.678 (IC base=+0.276)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.288 (n=2492)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.276)

- **PATRÓN** `volumen_spike_ratio` > `3.2217` → IC=+0.289 (n=922)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2217 (IC base=+0.276)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.286 (n=3395)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.276)

- **PATRÓN** `libro_liquidez` > `2023.9976` → IC=+0.287 (n=951)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2023.9976 (IC base=+0.276)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.298 (n=1709)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.276)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.335 (n=1148)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0105 (IC base=+0.297)

- **PATRÓN** `drift_60min` |x|≤ `0.1801` → IC=+0.314 (n=1114)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1801 (IC base=+0.297)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.325 (n=962)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.300 (n=875)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.297)

- **PATRÓN** `ibs_20min` < `0.0057` → IC=+0.301 (n=1114)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0057 (IC base=+0.297)

- **PATRÓN** `ibs_20min` > `0.1333` → IC=+0.305 (n=1688)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1333 (IC base=+0.297)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.337` → IC=+0.309 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.337 (IC base=+0.297)

- **PATRÓN** `volumen_pendiente_norm` < `0.198` → IC=+0.297 (n=2489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.198 (IC base=+0.297)

- **PATRÓN** `volumen_pendiente_norm` > `0.3434` → IC=+0.307 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3434 (IC base=+0.297)

- **PATRÓN** `volumen_spike_ratio` < `1.7379` → IC=+0.299 (n=1070)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7379 (IC base=+0.297)

- **PATRÓN** `volumen_spike_ratio` > `2.7131` → IC=+0.309 (n=1102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7131 (IC base=+0.297)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.300 (n=1285)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.297)

- **PATRÓN** `libro_liquidez` > `1911.8798` → IC=+0.305 (n=1148)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1911.8798 (IC base=+0.297)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.304 (n=1645)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.297)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7325` → IC=-0.180 (n=1236)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7325
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=3716)

- **PATRÓN** `ibs_20min` > `0.8646` → IC=+0.163 (n=1200)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.8646 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.1494` → IC=+0.230 (n=899)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1494 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.2121` → IC=+0.231 (n=1472)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2121 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `1.0079` → IC=+0.237 (n=1501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0079 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `0.6696` → IC=+0.231 (n=1524)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6696 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.0746` → IC=+0.240 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0746 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.4586` → IC=+0.236 (n=1651)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4586 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `118.0` → IC=+0.252 (n=1681)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 118.0 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `1.0214` → IC=+0.243 (n=1061)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0214 (IC base=+0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.307 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.7891` → IC=+0.274 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7891 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.4311` → IC=+0.259 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4311 (IC base=+0.004)

- **PATRÓN** `ballena_activa_n` < `121.0` → IC=+0.263 (n=1171)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 121.0 (IC base=+0.004)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.75` → IC=-0.235 (n=2073)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.312 (n=2083)

- **FILTRO** `ibs_20min` > `0.6341` → IC=-0.235 (n=1004)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6341
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=3027)

- **FILTRO** `sigma_ewma_delta_pct` > `8.409` → IC=-0.252 (n=461)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.409
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=3570)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.312 (n=2083)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.75 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` > `0.213` → IC=+0.345 (n=896)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.213 (IC base=+0.039)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.332` → IC=+0.193 (n=649)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 9.332 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` < `0.8471` → IC=+0.342 (n=1020)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8471 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` > `0.6975` → IC=+0.336 (n=1366)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6975 (IC base=+0.039)

- **PATRÓN** `volumen_pendiente_norm` < `0.1597` → IC=+0.334 (n=1583)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1597 (IC base=+0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.352 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` < `1.4413` → IC=+0.357 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4413 (IC base=+0.039)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.354 (n=1308)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.039)

- **PATRÓN** `ibs_20min` < `0.6341` → IC=+0.134 (n=3027)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.6341 (IC base=+0.042)

- **PATRÓN** `dist_vwap_pct` < `0.2877` → IC=+0.252 (n=1436)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2877 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` < `0.6968` → IC=+0.277 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6968 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.0703` → IC=+0.267 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0703 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` < `2.4553` → IC=+0.258 (n=1380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4553 (IC base=+0.042)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.273 (n=1409)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.042)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.354 (n=1926)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.310)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.311 (n=2174)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.310)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.317 (n=1026)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.310)

- **PATRÓN** `ibs_20min` > `0.7624` → IC=+0.347 (n=1925)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7624 (IC base=+0.310)

- **PATRÓN** `dist_vwap_pct` > `0.2079` → IC=+0.334 (n=1193)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2079 (IC base=+0.310)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.842` → IC=+0.328 (n=1046)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.842 (IC base=+0.310)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.113` → IC=+0.311 (n=2453)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.113 (IC base=+0.310)

- **PATRÓN** `volumen_regimen` > `0.6296` → IC=+0.320 (n=2154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6296 (IC base=+0.310)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.349 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.310)

- **PATRÓN** `volumen_spike_ratio` > `1.429` → IC=+0.322 (n=2070)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.429 (IC base=+0.310)

- **PATRÓN** `libro_liquidez` > `2569.8954` → IC=+0.311 (n=1436)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2569.8954 (IC base=+0.310)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.341 (n=1882)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.310)

- **PATRÓN** `sigma_h` > `0.0153` → IC=+0.344 (n=1528)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0153 (IC base=+0.312)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.321 (n=1146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.312)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.313 (n=1126)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.312)

- **PATRÓN** `ibs_20min` < `0.3778` → IC=+0.333 (n=2293)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3778 (IC base=+0.312)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.621` → IC=+0.328 (n=849)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.621 (IC base=+0.312)

- **PATRÓN** `volumen_regimen` < `0.723` → IC=+0.318 (n=1009)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.723 (IC base=+0.312)

- **PATRÓN** `volumen_regimen` > `1.212` → IC=+0.343 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.212 (IC base=+0.312)

- **PATRÓN** `volumen_pendiente_norm` > `0.2824` → IC=+0.363 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2824 (IC base=+0.312)

- **PATRÓN** `volumen_spike_ratio` < `1.4109` → IC=+0.325 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4109 (IC base=+0.312)

- **PATRÓN** `volumen_spike_ratio` > `2.1353` → IC=+0.314 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1353 (IC base=+0.312)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.226 (n=4958)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.1229` → IC=+0.196 (n=6541)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1229 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=15407)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `0.5478` → IC=+0.233 (n=14860)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5478 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `0.1637` → IC=+0.206 (n=5876)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1637 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.239` → IC=+0.255 (n=3875)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.239 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `1.1852` → IC=+0.161 (n=9880)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1852 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` > `0.6235` → IC=+0.159 (n=9881)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.6235 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2937` → IC=+0.207 (n=2158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2937 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` < `1.5615` → IC=+0.176 (n=6354)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.5615 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `2.6054` → IC=+0.189 (n=4815)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6054 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.196 (n=13782)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 90.0 (IC base=+0.178)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.190 (n=6362)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0055 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.0806` → IC=+0.225 (n=4820)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0806 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=5384)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` < `0.5156` → IC=+0.239 (n=14450)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5156 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.821` → IC=+0.196 (n=2324)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 9.821 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.51` → IC=+0.186 (n=13503)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 3.51 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `1.1823` → IC=+0.166 (n=10304)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1823 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2955` → IC=+0.225 (n=2149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2955 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.6419` → IC=+0.189 (n=4556)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6419 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.196 (n=13428)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 96.0 (IC base=+0.183)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.226 (n=826)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.1042` → IC=+0.258 (n=1085)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1042 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.235 (n=911)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.229 (n=1669)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.9355` → IC=+0.297 (n=1644)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9355 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.755` → IC=+0.329 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.755 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.288 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `1.8383` → IC=+0.221 (n=1563)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8383 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `1.4352` → IC=+0.224 (n=2343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4352 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=2716)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.223)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.233 (n=1472)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.009` → IC=+0.254 (n=1961)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.009 (IC base=+0.254)

- **PATRÓN** `drift_60min` |x|≤ `0.0967` → IC=+0.308 (n=864)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0967 (IC base=+0.254)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.260 (n=2029)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.254)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.256 (n=1802)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.254)

- **PATRÓN** `ibs_20min` < `0.4187` → IC=+0.272 (n=1960)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4187 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` < `0.1008` → IC=+0.259 (n=1723)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1008 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` > `0.3012` → IC=+0.281 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3012 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` < `2.2893` → IC=+0.263 (n=1643)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2893 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` > `2.7129` → IC=+0.255 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7129 (IC base=+0.254)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.257 (n=2246)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.254)

- **PATRÓN** `libro_liquidez` > `1462.0972` → IC=+0.258 (n=1751)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1462.0972 (IC base=+0.254)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.257 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.254)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.203 (n=751)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.1592` → IC=+0.174 (n=1500)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.1592 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=2359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.2967` → IC=+0.214 (n=2250)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2967 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1875` → IC=+0.214 (n=1181)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1875 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.082` → IC=+0.210 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.082 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.6937` → IC=+0.158 (n=990)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.6937 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `1.061` → IC=+0.145 (n=1020)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.061 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.2823` → IC=+0.186 (n=348)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2823 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.5085` → IC=+0.159 (n=972)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.5085 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `2.4789` → IC=+0.155 (n=737)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.4789 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `410.0` → IC=+0.149 (n=2172)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 410.0 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.175 (n=2381)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.006 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.2388` → IC=+0.174 (n=2095)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2388 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.185 (n=1130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 15.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.6155` → IC=+0.209 (n=2381)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6155 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.236` → IC=+0.185 (n=449)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 11.236 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.141` → IC=+0.153 (n=2071)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.141 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `1.2014` → IC=+0.162 (n=2381)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2014 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` < `0.0941` → IC=+0.153 (n=2057)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.0941 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.4845` → IC=+0.153 (n=2258)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4845 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `217.0` → IC=+0.191 (n=966)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 217.0 (IC base=+0.149)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.238 (n=1145)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.4024` → IC=+0.224 (n=2216)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4024 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.233 (n=916)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=1325)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.293` → IC=+0.307 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.293 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.212 (n=2179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.3519` → IC=+0.236 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3519 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.7635` → IC=+0.213 (n=1079)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7635 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.7054` → IC=+0.226 (n=1111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7054 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.217 (n=3015)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2009.87` → IC=+0.227 (n=840)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2009.87 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0119` → IC=+0.240 (n=2188)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0119 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.4252` → IC=+0.256 (n=1925)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4252 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.281 (n=827)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.027` → IC=+0.290 (n=963)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.027 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.234` → IC=+0.282 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.234 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.3592` → IC=+0.290 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3592 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `1.7622` → IC=+0.236 (n=926)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7622 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.1736` → IC=+0.243 (n=1401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1736 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.239 (n=1126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `1903.6181` → IC=+0.244 (n=992)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1903.6181 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.241 (n=1394)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.236)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.199 (n=1069)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.0787` → IC=+0.201 (n=810)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0787 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=2514)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.2823` → IC=+0.203 (n=2427)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2823 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.1422` → IC=+0.191 (n=1443)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1422 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.651` → IC=+0.193 (n=552)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 9.651 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.0211` → IC=+0.148 (n=2136)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.0211 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.1021` → IC=+0.170 (n=983)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1021 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.8287` → IC=+0.147 (n=1586)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.8287 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `2.5215` → IC=+0.158 (n=793)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.5215 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `6913.8034` → IC=+0.197 (n=1101)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 6913.8034 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `133.0` → IC=+0.147 (n=2372)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 133.0 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.156 (n=2578)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0074 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.397` → IC=+0.146 (n=2577)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.397 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=1219)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.6749` → IC=+0.187 (n=2577)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6749 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.505` → IC=+0.149 (n=624)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 9.505 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.8521` → IC=+0.157 (n=1719)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8521 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2982` → IC=+0.193 (n=389)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2982 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.8098` → IC=+0.135 (n=1621)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.8098 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `2.5475` → IC=+0.133 (n=810)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.5475 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `6194.147` → IC=+0.184 (n=1168)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 6194.147 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `111.0` → IC=+0.135 (n=2117)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 111.0 (IC base=+0.129)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.173 (n=1231)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0108 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=2776)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.4783` → IC=+0.212 (n=2713)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4783 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.1947` → IC=+0.189 (n=1540)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1947 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.3` → IC=+0.289 (n=575)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.3 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `1.1715` → IC=+0.133 (n=2713)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.1715 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.7044` → IC=+0.123 (n=2424)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.7044 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` < `0.1636` → IC=+0.131 (n=2770)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1636 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.5481` → IC=+0.139 (n=1160)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.5481 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.125 (n=2827)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2632.0205` → IC=+0.200 (n=1230)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2632.0205 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.144 (n=1124)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 21.0 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0114` → IC=+0.146 (n=2806)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0114 (IC base=+0.121)

- **PATRÓN** `drift_60min` |x|≤ `0.1101` → IC=+0.172 (n=936)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1101 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=2859)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.6286` → IC=+0.220 (n=2805)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6286 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` < `0.1993` → IC=+0.151 (n=2683)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1993 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.412` → IC=+0.140 (n=2476)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 2.412 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.1824` → IC=+0.131 (n=2803)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1824 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` < `0.1648` → IC=+0.126 (n=2736)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1648 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.2773` → IC=+0.138 (n=385)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.2773 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.4406` → IC=+0.130 (n=878)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.4406 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` > `1.8044` → IC=+0.126 (n=1755)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.8044 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2505.6184` → IC=+0.183 (n=1271)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2505.6184 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.129 (n=2613)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 47.0 (IC base=+0.121)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.246 (n=2225)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.169` → IC=+0.236 (n=1095)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.169 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.225 (n=2582)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.227 (n=2242)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.6606` → IC=+0.255 (n=2489)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6606 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` > `0.1821` → IC=+0.231 (n=1575)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1821 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.613` → IC=+0.253 (n=1124)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.613 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `1.1677` → IC=+0.223 (n=2489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1677 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `0.6234` → IC=+0.231 (n=2489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6234 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.269 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `2.461` → IC=+0.225 (n=2425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.461 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `1.8058` → IC=+0.232 (n=1617)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8058 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.224 (n=3244)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `2079.3306` → IC=+0.225 (n=2489)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2079.3306 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0128` → IC=+0.239 (n=1120)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0128 (IC base=+0.236)

- **PATRÓN** `sigma_h` > `0.0228` → IC=+0.248 (n=1153)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0228 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.0887` → IC=+0.261 (n=848)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0887 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.252 (n=1234)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.240 (n=1141)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.4359` → IC=+0.263 (n=2544)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4359 (IC base=+0.236)

- **PATRÓN** `dist_vwap_pct` > `0.3055` → IC=+0.244 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3055 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.307` → IC=+0.273 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.307 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` < `0.8698` → IC=+0.237 (n=1696)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8698 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` > `1.0419` → IC=+0.243 (n=1153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0419 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2797` → IC=+0.288 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2797 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `2.5121` → IC=+0.234 (n=2383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5121 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `1.4331` → IC=+0.236 (n=2382)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4331 (IC base=+0.236)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.207 (n=1637)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.1322` → IC=+0.202 (n=1635)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1322 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.194 (n=3320)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 8.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` > `0.3396` → IC=+0.207 (n=3712)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3396 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.8085` → IC=+0.194 (n=574)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.8085 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.597` → IC=+0.208 (n=1602)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.597 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` < `0.8606` → IC=+0.194 (n=2229)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.8606 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` > `0.0739` → IC=+0.185 (n=1501)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.0739 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` < `1.4312` → IC=+0.189 (n=1205)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.4312 (IC base=+0.175)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.181 (n=4169)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.02 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `8468.5183` → IC=+0.191 (n=1683)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 8468.5183 (IC base=+0.175)

- **PATRÓN** `ibs_20min` < `0.3908` → IC=+0.156 (n=2709)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.3908 (IC base=+0.080)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.123 (n=1727)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 26.0 (IC base=+0.080)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.208 (n=440)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.3269` → IC=+0.211 (n=994)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3269 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.220 (n=907)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `0.6402` → IC=+0.249 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6402 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` > `0.3087` → IC=+0.216 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3087 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.03` → IC=+0.210 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.03 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.243` → IC=+0.190 (n=1137)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 9.243 (IC base=+0.190)

- **PATRÓN** `volumen_regimen` < `0.8772` → IC=+0.210 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8772 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` < `0.1532` → IC=+0.192 (n=1044)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.1532 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.0712` → IC=+0.195 (n=401)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0712 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` < `2.1871` → IC=+0.202 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1871 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `10454.9515` → IC=+0.194 (n=994)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 10454.9515 (IC base=+0.190)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.203 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 162.0 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.162 (n=546)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0033 (IC base=+0.083)

- **PATRÓN** `ibs_20min` < `0.6403` → IC=+0.137 (n=1091)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.6403 (IC base=+0.083)

- **PATRÓN** `ballena_activa_n` < `165.0` → IC=+0.165 (n=532)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 165.0 (IC base=+0.083)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.245 (n=515)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.191)

- **PATRÓN** `drift_60min` |x|≤ `0.1272` → IC=+0.214 (n=515)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1272 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.208 (n=1218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `0.3538` → IC=+0.232 (n=1044)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3538 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` > `0.7903` → IC=+0.199 (n=184)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.7903 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` < `0.2068` → IC=+0.193 (n=1055)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.2068 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.87` → IC=+0.229 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.87 (IC base=+0.191)

- **PATRÓN** `volumen_regimen` < `1.0194` → IC=+0.203 (n=1029)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0194 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.159` → IC=+0.216 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.159 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` < `1.4277` → IC=+0.203 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4277 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `1.7865` → IC=+0.200 (n=770)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7865 (IC base=+0.191)

- **PATRÓN** `ibs_20min` < `0.1012` → IC=+0.181 (n=387)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.1012 (IC base=+0.075)

- **PATRÓN** `libro_liquidez` > `8203.5587` → IC=+0.141 (n=525)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 8203.5587 (IC base=+0.075)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.168 (n=311)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0112 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.185 (n=832)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 8.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.5098` → IC=+0.205 (n=929)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5098 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.9739` → IC=+0.216 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9739 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.072` → IC=+0.244 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.072 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.8819` → IC=+0.167 (n=620)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.8819 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `0.7057` → IC=+0.162 (n=830)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.7057 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2307` → IC=+0.176 (n=174)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2307 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `1.4413` → IC=+0.178 (n=299)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.4413 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `2.1532` → IC=+0.155 (n=407)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.1532 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.161 (n=970)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.02 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `2760.8656` → IC=+0.183 (n=421)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2760.8656 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.5769` → IC=+0.127 (n=913)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.5769 (IC base=+0.043)

- **PATRÓN** `libro_liquidez` > `2590.1864` → IC=+0.146 (n=470)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 2590.1864 (IC base=+0.043)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0261` → IC=+0.163 (n=253)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0261 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.2773` → IC=+0.172 (n=169)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.2773 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.211 (n=119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.7368` → IC=+0.182 (n=168)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.7368 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.2422` → IC=+0.164 (n=147)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.2422 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `1.2261` → IC=+0.156 (n=283)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 1.2261 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.369` → IC=+0.176 (n=220)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` < 3.369 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `1.0007` → IC=+0.156 (n=222)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0007 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `0.6843` → IC=+0.167 (n=226)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6843 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.1044` → IC=+0.167 (n=82)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1044 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.8148` → IC=+0.186 (n=151)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.8148 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `2.3815` → IC=+0.175 (n=75)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.3815 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.178 (n=299)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.03 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `2587.3393` → IC=+0.175 (n=115)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2587.3393 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.160 (n=257)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0132 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.146 (n=261)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.3333` → IC=+0.149 (n=192)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.3333 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `1.2295` → IC=+0.304 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2295 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.354` → IC=+0.175 (n=78)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 5.354 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.7125` → IC=+0.167 (n=127)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.7125 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` < `0.0833` → IC=+0.141 (n=249)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` < 0.0833 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2833` → IC=+0.138 (n=45)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.2833 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.5247` → IC=+0.199 (n=91)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.5247 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `2.7332` → IC=+0.134 (n=91)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.7332 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `2026.6384` → IC=+0.129 (n=257)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2026.6384 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.151 (n=270)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 19.0 (IC base=+0.129)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.228 (n=6468)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=20202)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.4397` → IC=+0.229 (n=19389)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4397 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.8845` → IC=+0.211 (n=2348)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8845 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.143` → IC=+0.254 (n=4734)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.143 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.2177` → IC=+0.164 (n=13028)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2177 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2411` → IC=+0.206 (n=3504)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2411 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6155` → IC=+0.192 (n=6299)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6155 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `107.0` → IC=+0.202 (n=18026)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 107.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.196 (n=7833)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0058 (IC base=+0.191)

- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.195 (n=5931)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0119 (IC base=+0.191)

- **PATRÓN** `drift_60min` |x|≤ `0.4859` → IC=+0.194 (n=17788)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.4859 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=6587)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` < `0.59` → IC=+0.242 (n=17792)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.59 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.668` → IC=+0.204 (n=2437)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.668 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.477` → IC=+0.195 (n=17260)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 3.477 (IC base=+0.191)

- **PATRÓN** `volumen_regimen` < `1.058` → IC=+0.165 (n=10554)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.058 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.2919` → IC=+0.254 (n=2422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2919 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `2.6321` → IC=+0.201 (n=5648)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6321 (IC base=+0.191)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.222 (n=11218)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.191)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3586` → IC=+0.231 (n=3133)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3586 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.244 (n=1514)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.231)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.234 (n=2113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` > `0.9703` → IC=+0.321 (n=1420)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9703 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.168` → IC=+0.346 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.168 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.2321` → IC=+0.292 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2321 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` < `1.4443` → IC=+0.230 (n=1007)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4443 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` > `2.2767` → IC=+0.238 (n=1369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2767 (IC base=+0.231)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.248 (n=3409)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.231)

- **PATRÓN** `libro_liquidez` > `2042.27` → IC=+0.234 (n=1044)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2042.27 (IC base=+0.231)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.253 (n=1912)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.231)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.268 (n=2736)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.266)

- **PATRÓN** `drift_60min` |x|≤ `0.0873` → IC=+0.298 (n=913)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0873 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.272 (n=2515)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.266)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.267 (n=2492)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` < `0.5301` → IC=+0.288 (n=2735)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5301 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` < `0.0966` → IC=+0.268 (n=2476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0966 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` > `0.2895` → IC=+0.292 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2895 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` < `1.5594` → IC=+0.266 (n=1148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5594 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` > `2.6647` → IC=+0.275 (n=870)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6647 (IC base=+0.266)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.267 (n=3135)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.266)

- **PATRÓN** `libro_liquidez` > `1749.78` → IC=+0.271 (n=1823)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1749.78 (IC base=+0.266)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.272 (n=1171)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.266)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.190 (n=1058)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0029 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.1056` → IC=+0.158 (n=1387)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1056 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.155 (n=3278)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.2228` → IC=+0.197 (n=3148)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.2228 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.3225` → IC=+0.199 (n=1080)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.3225 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.549` → IC=+0.158 (n=662)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 9.549 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `0.6328` → IC=+0.169 (n=1051)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.6328 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `1.2404` → IC=+0.147 (n=1050)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 1.2404 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.2732` → IC=+0.187 (n=452)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2732 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.1664` → IC=+0.151 (n=2716)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.1664 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.5264` → IC=+0.149 (n=2758)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.5264 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `256.0` → IC=+0.171 (n=1332)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 256.0 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.162 (n=2726)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.006 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.0791` → IC=+0.183 (n=909)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.0791 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=994)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.6888` → IC=+0.191 (n=2725)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6888 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.1425` → IC=+0.158 (n=2598)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1425 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.038` → IC=+0.147 (n=449)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 11.038 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.352` → IC=+0.141 (n=2747)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 6.352 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.0503` → IC=+0.154 (n=2398)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.0503 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2185` → IC=+0.197 (n=507)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2185 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.4128` → IC=+0.146 (n=873)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4128 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.7762` → IC=+0.147 (n=1745)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.7762 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=3535)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `234.0` → IC=+0.158 (n=852)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 234.0 (IC base=+0.140)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.251 (n=1077)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=3380)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=2896)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=1204)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.195` → IC=+0.327 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.195 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` < `0.1312` → IC=+0.226 (n=3039)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1312 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `1.615` → IC=+0.229 (n=3146)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.615 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.231 (n=3860)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `1344.941` → IC=+0.230 (n=3228)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1344.941 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.244 (n=2696)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.241)

- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.242 (n=1022)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.1797` → IC=+0.259 (n=1348)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1797 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.265 (n=1153)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.241 (n=1404)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.0486` → IC=+0.306 (n=1021)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0486 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.685` → IC=+0.298 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.685 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.3492` → IC=+0.305 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3492 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.1537` → IC=+0.253 (n=1955)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1537 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.249 (n=1561)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1906.6798` → IC=+0.253 (n=1388)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1906.6798 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.249 (n=1944)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.241)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.189 (n=1478)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0041 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.4327` → IC=+0.151 (n=3349)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4327 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.153 (n=3475)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` > `0.9051` → IC=+0.275 (n=1116)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9051 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.1421` → IC=+0.166 (n=1735)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1421 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.028` → IC=+0.157 (n=1499)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.028 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.053` → IC=+0.153 (n=2947)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.053 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.2333` → IC=+0.189 (n=592)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2333 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `1.5208` → IC=+0.159 (n=1439)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.5208 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `5331.7049` → IC=+0.226 (n=1518)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5331.7049 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.153 (n=1458)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 70.0 (IC base=+0.142)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.157 (n=2803)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0076 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4443` → IC=+0.146 (n=2802)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.4443 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.160 (n=1019)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.7229` → IC=+0.189 (n=2802)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.7229 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.069` → IC=+0.170 (n=422)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 11.069 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.692` → IC=+0.152 (n=1233)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.692 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.295` → IC=+0.225 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.295 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.2177` → IC=+0.138 (n=2379)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.2177 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.5366` → IC=+0.146 (n=2415)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.5366 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `6135.1381` → IC=+0.205 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6135.1381 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.142 (n=1830)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 96.0 (IC base=+0.136)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.154 (n=1540)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0108 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.151 (n=2377)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.4333` → IC=+0.192 (n=3382)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.4333 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `1.0166` → IC=+0.208 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0166 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.523` → IC=+0.267 (n=852)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.523 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `0.8787` → IC=+0.136 (n=2253)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8787 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.1638` → IC=+0.121 (n=3528)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1638 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `2.4927` → IC=+0.121 (n=3303)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.4927 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.121 (n=3520)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2683.9525` → IC=+0.244 (n=1126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2683.9525 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.128 (n=1080)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 21.0 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.154 (n=2831)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0105 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1353` → IC=+0.153 (n=1073)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1353 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.154 (n=1503)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 15.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.210 (n=3240)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6667 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.2122` → IC=+0.139 (n=2843)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.2122 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.178` → IC=+0.143 (n=3091)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 3.178 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.6396` → IC=+0.147 (n=1073)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.6396 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2255` → IC=+0.168 (n=561)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2255 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4381` → IC=+0.153 (n=1012)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4381 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2559.146` → IC=+0.197 (n=1072)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2559.146 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.136 (n=2680)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 44.0 (IC base=+0.120)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0139` → IC=+0.256 (n=2819)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0139 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.238 (n=3293)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.241 (n=2106)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` > `0.9938` → IC=+0.313 (n=1052)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9938 (IC base=+0.234)

- **PATRÓN** `dist_vwap_pct` > `0.1931` → IC=+0.249 (n=1673)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1931 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.328` → IC=+0.283 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.328 (IC base=+0.234)

- **PATRÓN** `volumen_regimen` < `1.2203` → IC=+0.237 (n=3155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2203 (IC base=+0.234)

- **PATRÓN** `volumen_regimen` > `0.6424` → IC=+0.238 (n=3154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6424 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.236` → IC=+0.254 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.236 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.4759` → IC=+0.250 (n=1026)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4759 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=4099)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2074.4784` → IC=+0.234 (n=3154)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2074.4784 (IC base=+0.234)

- **PATRÓN** `sigma_h` > `0.0257` → IC=+0.261 (n=1085)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0257 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.243 (n=3063)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.5188` → IC=+0.269 (n=3252)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5188 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.228` → IC=+0.275 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.228 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` > `1.2189` → IC=+0.260 (n=1084)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2189 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2836` → IC=+0.299 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2836 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.8103` → IC=+0.236 (n=2033)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8103 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `1.427` → IC=+0.238 (n=3047)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.427 (IC base=+0.238)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.236 (n=2972)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.238)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.198 (n=5581)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.246 (n=1920)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.5025` → IC=+0.225 (n=5740)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5025 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.231 (n=2084)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.9346` → IC=+0.255 (n=1913)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9346 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` < `0.4256` → IC=+0.219 (n=4163)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4256 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.868` → IC=+0.223 (n=942)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.868 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.576` → IC=+0.217 (n=5107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.576 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` < `0.706` → IC=+0.227 (n=1863)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.706 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `0.8828` → IC=+0.219 (n=2823)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8828 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.218 (n=5358)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.1655` → IC=+0.222 (n=1620)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1655 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `1.4526` → IC=+0.224 (n=1884)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4526 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.223 (n=4486)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `3706.6498` → IC=+0.226 (n=3826)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3706.6498 (IC base=+0.216)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.239 (n=1404)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.4928` → IC=+0.212 (n=4198)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4928 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=1417)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.212 (n=1867)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` < `0.7304` → IC=+0.204 (n=4198)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7304 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` > `0.6554` → IC=+0.209 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6554 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` < `0.238` → IC=+0.194 (n=3876)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.238 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.806` → IC=+0.207 (n=3753)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.806 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `1.0974` → IC=+0.203 (n=3516)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0974 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.199 (n=3861)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.0738` → IC=+0.200 (n=1879)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0738 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `1.5361` → IC=+0.202 (n=1821)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5361 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `2.1901` → IC=+0.206 (n=1876)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1901 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=5581)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `ballena_activa_n` < `173.0` → IC=+0.206 (n=3630)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 173.0 (IC base=+0.197)

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
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.3831` → IC=+0.196 (n=1486)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.3831 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.220 (n=544)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.191 (n=552)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.1373` → IC=+0.201 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1373 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.6858` → IC=+0.202 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6858 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.334` → IC=+0.203 (n=1458)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.334 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.0921` → IC=+0.193 (n=1308)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 1.0921 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.1518` → IC=+0.200 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1518 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `1.412` → IC=+0.199 (n=493)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.412 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `1.8038` → IC=+0.185 (n=986)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.8038 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `14605.0565` → IC=+0.188 (n=674)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 14605.0565 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `684.0` → IC=+0.193 (n=1441)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 684.0 (IC base=+0.181)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `drift_60min` |x|≤ `0.587` → IC=+0.204 (n=857)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.587 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.238 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` < `0.3897` → IC=+0.198 (n=286)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.3897 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.240 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.492` → IC=+0.239 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.492 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.2085` → IC=+0.238 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2085 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `1.8086` → IC=+0.205 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8086 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `2759.465` → IC=+0.229 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2759.465 (IC base=+0.196)

- **PATRÓN** `ballena_activa_n` < `5.0` → IC=+0.199 (n=380)

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
- **PATRÓN** `sigma_h` < `0.008` → IC=+0.218 (n=1578)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.4532` → IC=+0.215 (n=1578)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4532 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.224 (n=560)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` < `0.4996` → IC=+0.221 (n=1052)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4996 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `0.8591` → IC=+0.206 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8591 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` < `0.4017` → IC=+0.217 (n=1585)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4017 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.055` → IC=+0.216 (n=1433)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.055 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `0.7054` → IC=+0.212 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7054 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `1.2214` → IC=+0.210 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2214 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` < `0.1034` → IC=+0.209 (n=1453)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1034 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `2.4431` → IC=+0.214 (n=1545)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4431 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=1637)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.234 (n=576)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.4873` → IC=+0.214 (n=1295)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4873 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.204 (n=491)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.207 (n=873)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.3962` → IC=+0.199 (n=864)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.3962 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `0.0864` → IC=+0.196 (n=1295)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.0864 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.6348` → IC=+0.209 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6348 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.995` → IC=+0.194 (n=207)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 10.995 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.387` → IC=+0.195 (n=1175)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 4.387 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `0.6391` → IC=+0.224 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6391 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.0742` → IC=+0.223 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0742 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `2.1958` → IC=+0.200 (n=1117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1958 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.52` → IC=+0.194 (n=423)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.52 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `6540.7204` → IC=+0.198 (n=1157)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 6540.7204 (IC base=+0.193)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.227 (n=291)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.226 (n=590)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.274 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` > `0.7276` → IC=+0.238 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7276 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.261` → IC=+0.219 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.261 (IC base=+0.191)

- **PATRÓN** `volumen_regimen` < `0.7034` → IC=+0.230 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7034 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` < `0.1064` → IC=+0.203 (n=779)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1064 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` < `2.1734` → IC=+0.197 (n=744)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.1734 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `1.478` → IC=+0.198 (n=845)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.478 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.199 (n=1025)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `4248.0752` → IC=+0.236 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4248.0752 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.0128` → IC=+0.216 (n=639)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0128 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.5998` → IC=+0.235 (n=639)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5998 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.245 (n=449)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` < `0.7344` → IC=+0.239 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7344 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `0.5012` → IC=+0.223 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5012 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.91` → IC=+0.218 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.91 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.825` → IC=+0.223 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.825 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` > `0.928` → IC=+0.217 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.928 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` < `0.1067` → IC=+0.229 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1067 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.1983` → IC=+0.254 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1983 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `2953.4632` → IC=+0.229 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2953.4632 (IC base=+0.214)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.240 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.214)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.151 (n=651)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0036 (IC base=+0.061)

- **PATRÓN** `ibs_20min` > `0.7595` → IC=+0.197 (n=1233)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.7595 (IC base=+0.061)

- **PATRÓN** `dist_vwap_pct` > `0.1469` → IC=+0.142 (n=950)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1469 (IC base=+0.061)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.758` → IC=+0.145 (n=406)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 10.758 (IC base=+0.061)

- **PATRÓN** `ibs_20min` < `0.0426` → IC=+0.260 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0426 (IC base=+0.047)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.87` → IC=+0.170 (n=183)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.87 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.1459` → IC=+0.143 (n=326)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.1459 (IC base=+0.047)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.368` → IC=-0.152 (n=199)

  - _Acción_: SKIP cuando `ibs_20min` < 0.368
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=597)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.129 (n=628)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0057 (IC base=+0.082)

- **PATRÓN** `ibs_20min` > `0.368` → IC=+0.161 (n=597)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.368 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.172 (n=297)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.082)

- **PATRÓN** `ibs_20min` < `0.0617` → IC=+0.281 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0617 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.2162` → IC=+0.173 (n=96)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2162 (IC base=+0.056)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.7073` → IC=-0.153 (n=125)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7073
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=376)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.134 (n=424)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.005 (IC base=+0.080)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.137 (n=309)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 15.0 (IC base=+0.080)

- **PATRÓN** `ibs_20min` > `0.5456` → IC=+0.181 (n=540)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.5456 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` > `0.1265` → IC=+0.182 (n=303)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1265 (IC base=+0.080)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.939` → IC=+0.202 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.939 (IC base=+0.080)

- **PATRÓN** `ibs_20min` < `0.0289` → IC=+0.258 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0289 (IC base=+0.017)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.686` → IC=+0.219 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.686 (IC base=+0.017)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.198 (n=220)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 1.0 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.7109` → IC=+0.135 (n=154)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.7109 (IC base=+0.024)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.903` → IC=+0.138 (n=136)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 8.903 (IC base=+0.024)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.159 (n=291)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0106 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.0882` → IC=+0.254 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0882 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` < `0.1829` → IC=+0.134 (n=282)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1829 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.043` → IC=+0.361 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.043 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` > `1.1045` → IC=+0.186 (n=100)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 1.1045 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` > `0.1523` → IC=+0.188 (n=91)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1523 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` > `1.8481` → IC=+0.154 (n=183)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.8481 (IC base=+0.070)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0054` → IC=-0.235 (n=168)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0054
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=169)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.336 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=266)

- **FILTRO** `dist_vwap_pct` > `0.2352` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2352
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=321)

- **FILTRO** `volumen_regimen` < `0.7738` → IC=-0.302 (n=84)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7738
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=253)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.293 (n=90)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.290 (n=212)

- **FILTRO** `ibs_20min` > `0.7227` → IC=-0.317 (n=102)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7227
  - _Potencial_: sin este filtro IC_bueno=-0.277 (n=200)

- **FILTRO** `dist_vwap_pct` > `0.4704` → IC=-0.450 (n=18)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4704
  - _Potencial_: sin este filtro IC_bueno=-0.280 (n=284)

- **FILTRO** `sigma_ewma_delta_pct` > `9.983` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.983
  - _Potencial_: sin este filtro IC_bueno=-0.288 (n=276)

- **FILTRO** `volumen_pendiente_norm` > `0.0435` → IC=-0.382 (n=32)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0435
  - _Potencial_: sin este filtro IC_bueno=-0.277 (n=182)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `volumen_regimen` < `1.2266` → IC=-0.296 (n=52)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2266
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=52)

- **FILTRO** `sigma_h` < `0.0038` → IC=-0.258 (n=89)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0038
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=46)

- **FILTRO** `ibs_20min` < `0.3442` → IC=-0.283 (n=44)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3442
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=91)

- **FILTRO** `volumen_regimen` > `0.8213` → IC=-0.329 (n=33)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8213
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=102)

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
  - _Potencial_: sin este filtro IC_bueno=-0.304 (n=95)

- **FILTRO** `ibs_20min` > `0.7113` → IC=-0.402 (n=39)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7113
  - _Potencial_: sin este filtro IC_bueno=-0.275 (n=78)

- **FILTRO** `dist_vwap_pct` > `0.1281` → IC=-0.371 (n=29)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1281
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=88)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.317 (n=102)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.400 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=102)

- **FILTRO** `volumen_regimen` < `0.7553` → IC=-0.344 (n=30)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7553
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=90)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.242 (n=29)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=91)

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
- **FILTRO** `ibs_20min` > `0.1414` → IC=-0.125 (n=313)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1414
  - _Potencial_: sin este filtro IC_bueno=+0.124 (n=609)

- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.211 (n=202)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.201 (n=229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` > `0.6686` → IC=+0.173 (n=603)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.6686 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.5398` → IC=+0.256 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5398 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.614` → IC=+0.138 (n=332)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 3.614 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.697` → IC=+0.139 (n=444)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 2.697 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.6225` → IC=+0.181 (n=202)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6225 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` < `0.069` → IC=+0.174 (n=431)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` < 0.069 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `1.3996` → IC=+0.192 (n=167)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.3996 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.1414` → IC=+0.124 (n=609)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.1414 (IC base=+0.039)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.069` → IC=+0.157 (n=202)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 9.069 (IC base=+0.039)

- **PATRÓN** `libro_liquidez` > `4894.8429` → IC=+0.120 (n=314)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 4894.8429 (IC base=+0.039)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.75` → IC=-0.154 (n=79)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=163)

- **PATRÓN** `dist_vwap_pct` > `0.5497` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5497 (IC base=+0.016)

- **PATRÓN** `ibs_20min` < `0.1796` → IC=+0.176 (n=322)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.1796 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.118` → IC=+0.140 (n=137)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 7.118 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` > `1.0364` → IC=+0.155 (n=146)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.0364 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.2687` → IC=+0.148 (n=52)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2687 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `1.7759` → IC=+0.143 (n=194)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.7759 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `5391.3885` → IC=+0.127 (n=215)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 5391.3885 (IC base=+0.113)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1261` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1261
  - _Potencial_: sin este filtro IC_bueno=+0.173 (n=194)

- **FILTRO** `ibs_20min` > `0.1597` → IC=-0.143 (n=113)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1597
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=220)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.135 (n=176)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0052 (IC base=+0.123)

- **PATRÓN** `sigma_h` > `0.003` → IC=+0.135 (n=179)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.003 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.1024` → IC=+0.133 (n=88)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.1024 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.200 (n=68)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.798` → IC=+0.158 (n=179)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.798 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` < `0.0953` → IC=+0.147 (n=165)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.0953 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.217` → IC=+0.159 (n=209)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 9.217 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `0.6229` → IC=+0.196 (n=67)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.6229 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` < `0.1261` → IC=+0.173 (n=194)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` < 0.1261 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `2.1537` → IC=+0.169 (n=152)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 2.1537 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=169)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `1623.6709` → IC=+0.183 (n=200)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1623.6709 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.906` → IC=+0.177 (n=60)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 10.906 (IC base=-0.002)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2121` → IC=-0.250 (n=54)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2121
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=106)

- **FILTRO** `dist_vwap_pct` > `0.1699` → IC=-0.150 (n=38)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1699
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=122)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.300 (n=158)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` > `0.6818` → IC=+0.271 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6818 (IC base=+0.235)

- **PATRÓN** `dist_vwap_pct` > `0.6843` → IC=+0.387 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6843 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.006` → IC=+0.343 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.006 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` < `0.7975` → IC=+0.275 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7975 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` < `0.2182` → IC=+0.263 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2182 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.0951` → IC=+0.287 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0951 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` < `1.4814` → IC=+0.342 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4814 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.321` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.321 (IC base=-0.074)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.330 (n=86)

- **PATRÓN** `drift_ventana_pct` |x|> `0.349` → IC=+0.312 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.349 (IC base=+0.302)

- **PATRÓN** `elapsed_s` > `187.1` → IC=+0.355 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 187.1 (IC base=+0.302)

- **PATRÓN** `drift_15min` |x|≤ `2.6528` → IC=+0.341 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.6528 (IC base=+0.302)

- **PATRÓN** `drift_60min` |x|≤ `0.9568` → IC=+0.370 (n=67)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9568 (IC base=+0.302)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.378 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.302)

- **PATRÓN** `ballena_activa_n` < `1071.0` → IC=+0.380 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1071.0 (IC base=+0.302)

- **PATRÓN** `drift_ventana_pct` |x|> `0.4341` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4341 (IC base=+0.252)

- **PATRÓN** `elapsed_s` > `185.9` → IC=+0.278 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 185.9 (IC base=+0.252)

- **PATRÓN** `elapsed_s` < `202.5` → IC=+0.278 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 202.5 (IC base=+0.252)

- **PATRÓN** `drift_15min` |x|≤ `2.3354` → IC=+0.314 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3354 (IC base=+0.252)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.315 (n=52)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.252)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.330 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.252)

- **PATRÓN** `ballena_activa_n` < `1636.0` → IC=+0.329 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1636.0 (IC base=+0.252)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.330 (n=86)

- **PATRÓN** `drift_ventana_pct` |x|> `0.349` → IC=+0.312 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.349 (IC base=+0.302)

- **PATRÓN** `elapsed_s` > `187.1` → IC=+0.355 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 187.1 (IC base=+0.302)

- **PATRÓN** `drift_15min` |x|≤ `2.6528` → IC=+0.341 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.6528 (IC base=+0.302)

- **PATRÓN** `drift_60min` |x|≤ `0.9568` → IC=+0.370 (n=67)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9568 (IC base=+0.302)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.378 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.302)

- **PATRÓN** `ballena_activa_n` < `1071.0` → IC=+0.380 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1071.0 (IC base=+0.302)

- **PATRÓN** `drift_ventana_pct` |x|> `0.4341` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4341 (IC base=+0.252)

- **PATRÓN** `elapsed_s` > `185.9` → IC=+0.278 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 185.9 (IC base=+0.252)

- **PATRÓN** `elapsed_s` < `202.5` → IC=+0.278 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 202.5 (IC base=+0.252)

- **PATRÓN** `drift_15min` |x|≤ `2.3354` → IC=+0.314 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3354 (IC base=+0.252)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.315 (n=52)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.252)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.330 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.252)

- **PATRÓN** `ballena_activa_n` < `1636.0` → IC=+0.329 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1636.0 (IC base=+0.252)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=218)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=218)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=494)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `4006.09` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `liq_usd_total` < 4006.09
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=26)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=35)

- **PATRÓN** `liq_n` > `2.0` → IC=+0.141 (n=90)

  - _Acción_: Kelly boost +0.71€ cuando `liq_n` > 2.0 (IC base=+0.072)

- **PATRÓN** `liq_usd_total` > `1248.04` → IC=+0.127 (n=108)

  - _Acción_: Kelly boost +0.64€ cuando `liq_usd_total` > 1248.04 (IC base=+0.072)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.154 (n=53)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 8.0 (IC base=+0.072)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=3784)

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
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=1504)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=1458)

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
- **FILTRO** `py_entrada` > `0.505` → IC=-0.140 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=713)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=721)

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
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=909)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=909)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=1022)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=1022)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=242)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=242)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.135 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=185)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.191 (n=53)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=299)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=337)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=279)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=373)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=373)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=218)

- **FILTRO** `libro_liquidez` < `642.4226` → IC=-0.134 (n=132)

  - _Acción_: SKIP cuando `libro_liquidez` < 642.4226
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=271)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=293)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `restante_min` < `10.72` → IC=-0.167 (n=28)

  - _Acción_: SKIP cuando `restante_min` < 10.72
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=58)

- **FILTRO** `lag_apertura_s` > `255.1` → IC=-0.145 (n=29)

  - _Acción_: SKIP cuando `lag_apertura_s` > 255.1
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=57)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.198 (n=61)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=79)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.250 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=48)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.51` → IC=+0.147 (n=259)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.51 (IC base=+0.001)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` > `0.61` → IC=-0.130 (n=44)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=173)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.155 (n=137)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=286)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.127 (n=140)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=548)

- **FILTRO** `profundidad_ratio` < `60.5` → IC=-0.123 (n=226)

  - _Acción_: SKIP cuando `profundidad_ratio` < 60.5
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=462)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.196 (n=110)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=449)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` > `0.58` → IC=-0.124 (n=264)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=322)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.169 (n=122)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=510)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` > `0.61` → IC=-0.135 (n=94)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=295)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.152 (n=254)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=519)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.175 (n=6763)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=21834)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.177 (n=7143)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=22319)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.191 (n=1284)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=3980)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.176 (n=1217)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=4021)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.140 (n=1380)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 1.0 (IC base=+0.041)

- **PATRÓN** `libro_liquidez` > `1035.2534` → IC=+0.140 (n=2632)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 1035.2534 (IC base=+0.041)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.132 (n=2468)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.5 (IC base=+0.013)

- **PATRÓN** `libro_liquidez` > `1145.769` → IC=+0.150 (n=1781)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1145.769 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.182 (n=1018)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3158)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.204 (n=1278)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=4079)

- **PATRÓN** `ibs_20min` > `0.9645` → IC=+0.128 (n=1792)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` > 0.9645 (IC base=+0.035)

- **PATRÓN** `libro_liquidez` > `1728.3955` → IC=+0.122 (n=1792)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1728.3955 (IC base=+0.035)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.156 (n=1300)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=3968)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2417)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=2341)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.188 (n=922)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=2876)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=3777)

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

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.196 (n=366)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=716)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.132 (n=19637)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=43843)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.297 (n=14887)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=48593)

- **FILTRO** `ibs_7min` < `0.2254` → IC=-0.231 (n=15870)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2254
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=47610)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.152 (n=21314)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=42166)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.243 (n=19764)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=60057)

- **FILTRO** `ibs_7min` > `0.2826` → IC=-0.181 (n=19940)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2826
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=59881)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.154 (n=2774)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=8435)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.317 (n=2730)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=8479)

- **FILTRO** `ibs_7min` < `0.7108` → IC=-0.249 (n=3698)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7108
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=7511)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.150 (n=2635)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=8574)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.277 (n=3296)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=10484)

- **FILTRO** `ibs_7min` > `0.7717` → IC=-0.215 (n=3444)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7717
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=10336)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.261 (n=2537)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=8094)

- **FILTRO** `ibs_7min` < `0.7166` → IC=-0.203 (n=2656)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7166
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=7975)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.194 (n=2651)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=7980)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.259 (n=2702)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=8172)

- **FILTRO** `ibs_7min` > `0.2644` → IC=-0.190 (n=2718)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2644
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=8156)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.178 (n=2700)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=8174)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.162 (n=2617)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=8067)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.313 (n=2661)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=8023)

- **FILTRO** `ibs_7min` < `0.2884` → IC=-0.247 (n=3525)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2884
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=7159)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.196 (n=2317)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=8367)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.260 (n=3482)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=11146)

- **FILTRO** `ibs_7min` > `0.7298` → IC=-0.181 (n=3656)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7298
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=10972)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=2491)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=7811)

- **FILTRO** `ibs_7min` < `0.7198` → IC=-0.193 (n=2574)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7198
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=7728)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.188 (n=2503)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=7799)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.259 (n=2458)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=8290)

- **FILTRO** `ibs_7min` > `0.2747` → IC=-0.172 (n=2685)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2747
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=8063)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.174 (n=2608)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=8140)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=2557)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=7732)

- **FILTRO** `ibs_7min` < `0.7093` → IC=-0.225 (n=3395)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7093
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=6894)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.221 (n=2413)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=7876)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.194 (n=3641)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=11770)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.299 (n=2576)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=7789)

- **FILTRO** `ibs_7min` < `0.18` → IC=-0.231 (n=2588)

  - _Acción_: SKIP cuando `ibs_7min` < 0.18
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=7777)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.203 (n=2435)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=7930)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.225 (n=3568)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=10812)

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
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=590)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=870)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.143 (n=166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=333)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=450)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.130 (n=90)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=651)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3983` → IC=+0.135 (n=1320)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.3983 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.129 (n=583)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 5.0 (IC base=+0.124)

- **PATRÓN** `total_vol_5m` < `437.4823` → IC=+0.152 (n=441)

  - _Acción_: Kelly boost +0.76€ cuando `total_vol_5m` < 437.4823 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `3445.295` → IC=+0.142 (n=599)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 3445.295 (IC base=+0.124)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.173 (n=148)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 14.0 (IC base=+0.119)

- **PATRÓN** `total_vol_5m` < `372.075` → IC=+0.144 (n=273)

  - _Acción_: Kelly boost +0.72€ cuando `total_vol_5m` < 372.075 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2517.123` → IC=+0.217 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2517.123 (IC base=+0.119)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.4381` → IC=+0.138 (n=92)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio` |x|> 0.4381 (IC base=+0.114)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.136 (n=248)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 14.0 (IC base=+0.114)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.121 (n=333)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.04 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `2304.5801` → IC=+0.140 (n=184)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2304.5801 (IC base=+0.114)

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
- **PATRÓN** `hora_utc` < `10.0` → IC=+0.140 (n=173)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 10.0 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.172 (n=169)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `3725.3423` → IC=+0.140 (n=84)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3725.3423 (IC base=+0.101)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.7861` → IC=-0.284 (n=49)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.7861
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=148)

- **FILTRO** `pct_vs_K` |x|> `3.4286` → IC=-0.193 (n=252)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4286
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=492)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.177 (n=187)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0037 (IC base=-0.085)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `87.9901` → IC=-0.237 (n=55)

  - _Acción_: SKIP cuando `T_h` > 87.9901
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=166)

- **FILTRO** `pct_vs_K` |x|> `4.2515` → IC=-0.307 (n=55)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.2515
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=166)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.293 (n=56)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=-0.038)

- **PATRÓN** `pct_vs_K` |x|≤ `1.6038` → IC=+0.140 (n=73)

  - _Acción_: Kelly boost +0.70€ cuando `pct_vs_K` |x|≤ 1.6038 (IC base=-0.038)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `pct_vs_K` |x|> `9.1619` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 9.1619
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=53)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `T_h` < `63.9936` → IC=-0.181 (n=45)

  - _Acción_: SKIP cuando `T_h` < 63.9936
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=93)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0096` → IC=-0.239 (n=443)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0096
  - _Potencial_: sin este filtro IC_bueno=-0.106 (n=229)

- **FILTRO** `T_h` > `78.3586` → IC=-0.217 (n=450)

  - _Acción_: SKIP cuando `T_h` > 78.3586
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=222)

- **FILTRO** `sigma_h` < `0.005` → IC=-0.247 (n=144)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=432)

- **FILTRO** `pct_vs_K` |x|> `3.2571` → IC=-0.431 (n=142)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.2571
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=434)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0083` → IC=-0.208 (n=166)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=56)

- **FILTRO** `T_h` > `68.7654` → IC=-0.200 (n=148)

  - _Acción_: SKIP cuando `T_h` > 68.7654
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=74)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.257 (n=68)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.254 (n=140)

- **FILTRO** `pct_vs_K` |x|> `1.95` → IC=-0.404 (n=102)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 1.95
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=106)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `sigma_h` < `0.0085` → IC=-0.250 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0096` → IC=-0.320 (n=126)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0096
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=66)

- **FILTRO** `T_h` > `69.4221` → IC=-0.272 (n=143)

  - _Acción_: SKIP cuando `T_h` > 69.4221
  - _Potencial_: sin este filtro IC_bueno=-0.226 (n=49)

- **FILTRO** `sigma_h` < `0.0058` → IC=-0.205 (n=59)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0058
  - _Potencial_: sin este filtro IC_bueno=-0.164 (n=120)

- **FILTRO** `pct_vs_K` |x|> `2.3708` → IC=-0.412 (n=89)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.3708
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=90)

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
  - _Potencial_: sin este filtro IC_bueno=-0.114 (n=143)

- **FILTRO** `T_h` > `71.2713` → IC=-0.201 (n=142)

  - _Acción_: SKIP cuando `T_h` > 71.2713
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=48)

- **FILTRO** `sigma_h` > `0.015` → IC=-0.379 (n=31)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.015
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=96)

- **FILTRO** `sigma_h` < `0.0087` → IC=-0.291 (n=41)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0087
  - _Potencial_: sin este filtro IC_bueno=-0.216 (n=86)

- **FILTRO** `T_h` > `39.1242` → IC=-0.282 (n=85)

  - _Acción_: SKIP cuando `T_h` > 39.1242
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=42)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1208` → IC=+0.468 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1208 (IC base=+0.340)

- **PATRÓN** `sigma_h` < `0.013` → IC=+0.362 (n=92)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.013 (IC base=+0.340)

- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.373 (n=69)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.340)

- **PATRÓN** `T_h` < `0.3439` → IC=+0.392 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3439 (IC base=+0.340)

- **PATRÓN** `T_h` > `0.8789` → IC=+0.380 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8789 (IC base=+0.340)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.480 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.340)

- **PATRÓN** `edge` > `0.0997` → IC=+0.438 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.0997 (IC base=+0.407)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.432 (n=160)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.407)

- **PATRÓN** `T_h` < `0.6127` → IC=+0.441 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6127 (IC base=+0.407)

- **PATRÓN** `T_h` > `1.4833` → IC=+0.415 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4833 (IC base=+0.407)

- **PATRÓN** `dist_50` > `0.3765` → IC=+0.446 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3765 (IC base=+0.407)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.472 (n=140)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.407)

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
- **PATRÓN** `edge` > `0.1745` → IC=+0.485 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1745 (IC base=+0.434)

- **PATRÓN** `sigma_h` < `0.0161` → IC=+0.456 (n=66)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0161 (IC base=+0.434)

- **PATRÓN** `T_h` > `0.5264` → IC=+0.451 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.5264 (IC base=+0.434)

- **PATRÓN** `dist_50` > `0.3326` → IC=+0.471 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3326 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.434)

- **PATRÓN** `edge` > `0.1961` → IC=+0.470 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1961 (IC base=+0.462)

- **PATRÓN** `sigma_h` < `0.0157` → IC=+0.473 (n=146)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0157 (IC base=+0.462)

- **PATRÓN** `T_h` < `0.8279` → IC=+0.455 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.8279 (IC base=+0.462)

- **PATRÓN** `T_h` > `1.486` → IC=+0.481 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.486 (IC base=+0.462)

- **PATRÓN** `dist_50` > `0.4605` → IC=+0.492 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4605 (IC base=+0.462)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.467 (n=148)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.462)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=354)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=422)

- **PATRÓN** `streak_estiramiento` < `0.2958` → IC=+0.152 (n=90)

  - _Acción_: Kelly boost +0.76€ cuando `streak_estiramiento` < 0.2958 (IC base=+0.015)

- **PATRÓN** `streak_estiramiento` < `0.2811` → IC=+0.265 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.2811 (IC base=+0.057)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.133 (n=216)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 33.0 (IC base=+0.057)

- **PATRÓN** `libro_liquidez` > `2493.7311` → IC=+0.130 (n=152)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2493.7311 (IC base=+0.057)

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
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=21)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.495 (IC base=+0.026)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `streak_estiramiento` > `0.4361` → IC=-0.192 (n=37)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4361
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=114)

- **PATRÓN** `streak_estiramiento` < `0.2356` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `streak_estiramiento` < 0.2356 (IC base=+0.016)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.130 (n=160)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.099)

- **PATRÓN** `streak_estiramiento` < `0.4376` → IC=+0.206 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.4376 (IC base=+0.099)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.177 (n=131)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 34.0 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `2222.8358` → IC=+0.140 (n=134)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2222.8358 (IC base=+0.099)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=1050)

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
- **FILTRO** `hora_utc` > `6.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=15)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=33)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=4381)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=15)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=33)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=2514)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.188 (n=1804)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0055 (IC base=+0.164)

- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.176 (n=1366)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0125 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.1795` → IC=+0.183 (n=3605)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1795 (IC base=+0.164)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0986` → IC=+0.174 (n=1253)

  - _Acción_: Kelly boost +0.87€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0986 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.172 (n=3778)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.167 (n=3798)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 15.0 (IC base=+0.164)

- **PATRÓN** `ibs_15` > `0.5312` → IC=+0.238 (n=4097)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5312 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.1304` → IC=+0.160 (n=2007)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1304 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` < `0.3195` → IC=+0.151 (n=3314)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.3195 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.1` → IC=+0.264 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.1 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `2488.522` → IC=+0.172 (n=3660)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2488.522 (IC base=+0.164)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1673)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.221 (n=697)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.206)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.207 (n=316)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.0592` → IC=+0.257 (n=233)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0592 (IC base=+0.206)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2638` → IC=+0.231 (n=232)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2638 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.226 (n=728)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.206)

- **PATRÓN** `ibs_15` > `0.7223` → IC=+0.277 (n=696)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7223 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.2399` → IC=+0.221 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2399 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.394` → IC=+0.307 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.394 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=902)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `8041.1866` → IC=+0.216 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8041.1866 (IC base=+0.206)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.160 (n=840)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0068 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.1091` → IC=+0.160 (n=560)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1091 (IC base=+0.141)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1412` → IC=+0.148 (n=560)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio_macro` |x|> 0.1412 (IC base=+0.141)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0901` → IC=+0.150 (n=255)

  - _Acción_: Kelly boost +0.75€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0901 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.148 (n=765)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 6.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.145 (n=880)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 17.0 (IC base=+0.141)

- **PATRÓN** `ibs_15` > `0.622` → IC=+0.258 (n=751)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.622 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.1202` → IC=+0.157 (n=517)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1202 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.285` → IC=+0.285 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.285 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `5753.161` → IC=+0.168 (n=381)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 5753.161 (IC base=+0.141)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8788` → IC=+0.232 (n=338)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8788 (IC base=+0.078)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=525)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.078)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0243` → IC=+0.224 (n=302)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0243 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.1782` → IC=+0.209 (n=796)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1782 (IC base=+0.192)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.093` → IC=+0.249 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.093 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.203 (n=814)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.192)

- **PATRÓN** `ibs_15` > `0.5135` → IC=+0.272 (n=905)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5135 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` > `0.1316` → IC=+0.212 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1316 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.332` → IC=+0.233 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.332 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.196 (n=617)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.02 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `2947.5126` → IC=+0.289 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2947.5126 (IC base=+0.192)

- **PATRÓN** `ibs_15` < `0.1068` → IC=+0.173 (n=812)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.87€ cuando `ibs_15` < 0.1068 (IC base=+0.070)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.387 (n=316)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1501` → IC=+0.377 (n=463)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1501 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1379` → IC=+0.385 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1379 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.376 (n=693)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.7883` → IC=+0.398 (n=693)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7883 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.1521` → IC=+0.382 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1521 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.204` → IC=+0.396 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.204 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.369 (n=840)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `3836.614` → IC=+0.375 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3836.614 (IC base=+0.365)

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

- **PATRÓN** `ibs_15` > `0.9198` → IC=+0.406 (n=233)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9198 (IC base=+0.361)

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
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.367)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.383 (n=229)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.367)

- **PATRÓN** `drift_60min` |x|≤ `0.1062` → IC=+0.371 (n=230)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1062 (IC base=+0.367)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0833` → IC=+0.380 (n=307)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0833 (IC base=+0.367)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.382 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.367)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.383 (n=160)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.367)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.376 (n=159)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.367)

- **PATRÓN** `ibs_15` > `0.7604` → IC=+0.405 (n=344)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7604 (IC base=+0.367)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.374 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.367)

- **PATRÓN** `dist_vwap_pct` < `0.2918` → IC=+0.372 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2918 (IC base=+0.367)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.408` → IC=+0.404 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.408 (IC base=+0.367)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.373 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.367)

- **PATRÓN** `libro_liquidez` > `4019.374` → IC=+0.399 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4019.374 (IC base=+0.367)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.178 (n=2318)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=2319)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.215 (n=1817)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=2820)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.138` → IC=+0.219 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.138 (IC base=-0.069)

- **PATRÓN** `ibs_15` > `0.6335` → IC=+0.281 (n=1119)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6335 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` > `0.1113` → IC=+0.207 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1113 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` < `0.4246` → IC=+0.203 (n=1101)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4246 (IC base=-0.069)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2301` → IC=+0.272 (n=1358)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2301 (IC base=-0.010)

- **PATRÓN** `ibs_15` < `0.3703` → IC=+0.282 (n=4067)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3703 (IC base=-0.010)

- **PATRÓN** `dist_vwap_pct` > `0.6602` → IC=+0.275 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6602 (IC base=-0.010)

- **PATRÓN** `dist_vwap_pct` < `0.167` → IC=+0.246 (n=3051)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.167 (IC base=-0.010)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0335` → IC=-0.223 (n=2198)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0335
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=736)

- **FILTRO** `sigma_h` < `0.0036` → IC=-0.222 (n=733)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0036
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=2201)

- **FILTRO** `sigma_ewma_delta_pct` > `23.13` → IC=-0.267 (n=419)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.13
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=2515)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.153 (n=283)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0029 (IC base=+0.085)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1441` → IC=+0.271 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1441 (IC base=+0.085)

- **PATRÓN** `ibs_15` > `0.7639` → IC=+0.330 (n=381)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7639 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.1051` → IC=+0.283 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1051 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` < `0.3659` → IC=+0.286 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3659 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.871` → IC=+0.148 (n=248)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 18.871 (IC base=+0.085)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0674` → IC=+0.246 (n=69)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0674 (IC base=-0.190)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1389` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1389 (IC base=-0.190)

- **PATRÓN** `ibs_15` < `0.6221` → IC=+0.317 (n=69)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6221 (IC base=-0.190)

- **PATRÓN** `dist_vwap_pct` < `0.0415` → IC=+0.325 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0415 (IC base=-0.190)

- **PATRÓN** `ballena_activa_n` < `291.0` → IC=+0.378 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 291.0 (IC base=-0.190)

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

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.267 (n=525)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.1036` → IC=+0.244 (n=525)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1036 (IC base=+0.243)

- **PATRÓN** `drift_15min` |x|≤ `0.7764` → IC=+0.257 (n=1385)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7764 (IC base=+0.243)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2139` → IC=+0.272 (n=713)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2139 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=577)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.247 (n=1072)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.243)

- **PATRÓN** `ibs_15` < `0.3774` → IC=+0.275 (n=1574)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3774 (IC base=+0.243)

- **PATRÓN** `dist_vwap_pct` > `0.6193` → IC=+0.267 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6193 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.423` → IC=+0.249 (n=694)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.423 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.457` → IC=+0.249 (n=1642)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.457 (IC base=+0.243)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1724` → IC=-0.248 (n=363)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1724
  - _Potencial_: sin este filtro IC_bueno=-0.161 (n=705)

- **FILTRO** `drift_15min` |x|> `0.8922` → IC=-0.284 (n=266)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8922
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=802)

- **FILTRO** `sigma_ewma_delta_pct` > `6.602` → IC=-0.206 (n=246)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.602
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=822)

- **FILTRO** `sigma_ewma_delta_pct` > `17.553` → IC=-0.142 (n=565)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.553
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=4536)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.191)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.191)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.191)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=-0.191)

- **PATRÓN** `ibs_15` < `0.4068` → IC=+0.291 (n=703)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.4068 (IC base=-0.034)

- **PATRÓN** `dist_vwap_pct` < `0.4491` → IC=+0.231 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4491 (IC base=-0.034)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.245 (n=579)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=687)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.211)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.211)

- **PATRÓN** `delta_ratio_macro` |x|> `0.07` → IC=+0.275 (n=824)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.07 (IC base=-0.024)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1165` → IC=+0.293 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1165 (IC base=-0.024)

- **PATRÓN** `ibs_15` < `0.137` → IC=+0.314 (n=615)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.137 (IC base=-0.024)

- **PATRÓN** `dist_vwap_pct` > `0.7832` → IC=+0.347 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7832 (IC base=-0.024)

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
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.291 (n=1213)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.0721` → IC=+0.316 (n=535)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0721 (IC base=+0.286)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1505` → IC=+0.288 (n=809)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1505 (IC base=+0.286)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2235` → IC=+0.299 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2235 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.302 (n=1258)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.286)

- **PATRÓN** `ibs_15` > `0.8393` → IC=+0.317 (n=1213)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8393 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.2663` → IC=+0.316 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2663 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.387` → IC=+0.386 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.387 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `11977.5569` → IC=+0.306 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11977.5569 (IC base=+0.286)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.307 (n=216)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.280)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.294 (n=294)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.280)

- **PATRÓN** `drift_60min` |x|≤ `0.0588` → IC=+0.317 (n=216)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0588 (IC base=+0.280)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2672` → IC=+0.284 (n=216)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2672 (IC base=+0.280)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3917` → IC=+0.286 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3917 (IC base=+0.280)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.300 (n=678)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.280)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.306 (n=647)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.829 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.2522` → IC=+0.316 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2522 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.55` → IC=+0.379 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.55 (IC base=+0.280)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.280 (n=836)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `12659.8064` → IC=+0.306 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12659.8064 (IC base=+0.280)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.308 (n=567)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.1076` → IC=+0.316 (n=378)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1076 (IC base=+0.293)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1442` → IC=+0.295 (n=378)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1442 (IC base=+0.293)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1009` → IC=+0.347 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1009 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.307 (n=543)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.298 (n=518)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.293)

- **PATRÓN** `ibs_15` > `0.8516` → IC=+0.324 (n=567)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8516 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.2815` → IC=+0.314 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2815 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.52` → IC=+0.382 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.52 (IC base=+0.293)

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

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.326 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=12)

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
- **PATRÓN** `T_h` > `103.6389` → IC=+0.180 (n=483)

  - _Acción_: Kelly boost +0.90€ cuando `T_h` > 103.6389 (IC base=+0.179)

- **PATRÓN** `ratio` < `0.973` → IC=+0.396 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.179)

- **PATRÓN** `T_h` > `115.9003` → IC=+0.353 (n=2457)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 115.9003 (IC base=+0.335)

- **PATRÓN** `ratio` > `1.0213` → IC=+0.376 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0213 (IC base=+0.335)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `111.4342` → IC=+0.164 (n=227)

  - _Acción_: Kelly boost +0.82€ cuando `T_h` > 111.4342 (IC base=+0.147)

- **PATRÓN** `ratio` < `0.9823` → IC=+0.326 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9823 (IC base=+0.147)

- **PATRÓN** `T_h` > `111.9838` → IC=+0.309 (n=864)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9838 (IC base=+0.295)

- **PATRÓN** `ratio` > `1.0422` → IC=+0.416 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0422 (IC base=+0.295)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `85.7585` → IC=+0.218 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 85.7585 (IC base=+0.219)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.394 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.219)

- **PATRÓN** `T_h` > `111.996` → IC=+0.352 (n=890)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.996 (IC base=+0.322)

- **PATRÓN** `ratio` > `1.0083` → IC=+0.336 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0083 (IC base=+0.322)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0625` → IC=+0.437 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0625 (IC base=+0.398)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5312 sube el IC de +0.164 a +0.238 en UPDOWN_GBM#15min (n=4097). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7223 sube el IC de +0.206 a +0.277 en UPDOWN_GBM#BTC#15min (n=696). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.622 sube el IC de +0.141 a +0.258 en UPDOWN_GBM#ETH#15min (n=751). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.8788 sube el IC de +0.078 a +0.232 en UPDOWN_GBM#SOL#15min (n=338). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5135 sube el IC de +0.192 a +0.272 en UPDOWN_GBM#XRP#15min (n=905). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1068 sube el IC de +0.070 a +0.173 en UPDOWN_GBM#XRP#15min (n=812). Ya aplicado como kelly_boost=+0.87€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6335 sube el IC de -0.069 a +0.281 en UPDOWN_GBM_15M_TARDIO (n=1119). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3703 sube el IC de -0.010 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=4067). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7639 sube el IC de +0.085 a +0.330 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=381). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6221 sube el IC de -0.190 a +0.317 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=69). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5874 sube el IC de +0.153 a +0.247 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=556). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3774 sube el IC de +0.243 a +0.275 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1574). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.191 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.4068 sube el IC de -0.034 a +0.291 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=703). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.211 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.137 sube el IC de -0.024 a +0.314 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=615). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.093 a +0.364 en UPDOWN_GBM_ETH_15M_HORA7 (n=20). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.093 a +0.364 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=20). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8393 sube el IC de +0.286 a +0.317 en UPDOWN_GBM_IBS_ALTO (n=1213). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.280 a +0.306 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=647). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8516 sube el IC de +0.293 a +0.324 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=567). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7883 sube el IC de +0.365 a +0.398 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=693). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.9198 sube el IC de +0.361 a +0.406 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=233). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7604 sube el IC de +0.367 a +0.405 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=344). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2073 | +0.087 | +217.91€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2073 | +0.087 | +217.91€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1674 | +0.088 | +182.26€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1674 | +0.088 | +182.26€ | 0 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 284 | +0.070 | +11.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 284 | +0.070 | +11.30€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 84 | +0.128 | +24.67€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 84 | +0.128 | +24.67€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 894 | -0.016 | +92.54€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 894 | -0.016 | +92.54€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 690 | -0.038 | +65.67€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 690 | -0.038 | +65.67€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 150 | +0.086 | +25.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 150 | +0.086 | +25.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 48 | -0.020 | -0.59€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 48 | -0.020 | -0.59€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 43708 | -0.083 | -5561.27€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2584 | +0.060 | -288.63€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 41124 | -0.092 | -5272.64€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4619 | -0.117 | -762.83€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4619 | -0.117 | -762.83€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2584 | +0.060 | -288.63€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2584 | +0.060 | -288.63€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4595 | -0.115 | -892.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4595 | -0.115 | -892.30€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 11735 | -0.024 | -1141.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 11735 | -0.024 | -1141.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 11772 | -0.116 | -1099.23€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 11772 | -0.116 | -1099.23€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8403 | -0.127 | -1376.53€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8403 | -0.127 | -1376.53€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 41727 | -0.013 | +3136.41€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 10761 | +0.005 | +1618.10€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 30966 | -0.019 | +1518.31€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 41727 | -0.013 | +3136.41€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 10761 | +0.005 | +1618.10€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 30966 | -0.019 | +1518.31€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 165606 | +0.114 | -6801.88€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 20258 | +0.180 | -689.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 745 | -0.005 | -77.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 134912 | +0.106 | -5703.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 9691 | +0.094 | -331.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 22355 | +0.106 | -1422.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 67 | -0.181 | +5.90€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 22273 | +0.108 | -1416.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 31741 | +0.125 | -533.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5463 | +0.181 | -224.71€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 22345 | +0.120 | -169.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3891 | +0.080 | -117.69€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 22410 | +0.099 | -1592.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 82 | -0.119 | -3.25€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 22313 | +0.100 | -1578.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 35294 | +0.123 | -730.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 9024 | +0.176 | -212.44€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 22678 | +0.106 | -460.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3580 | +0.101 | -49.43€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 31424 | +0.113 | -1501.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5545 | +0.198 | -263.09€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 648 | +0.025 | -23.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 23011 | +0.095 | -1050.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2220 | +0.109 | -164.25€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#XRP | 22382 | +0.106 | -1019.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 77 | -0.108 | +7.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 22292 | +0.107 | -1027.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 26734 | +0.194 | -1756.22€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 26734 | +0.194 | -1756.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 6047 | +0.176 | -547.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 6047 | +0.176 | -547.88€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 3632 | +0.200 | -110.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 3632 | +0.200 | -110.81€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 5986 | +0.176 | -517.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 5986 | +0.176 | -517.47€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5103 | +0.247 | -189.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5103 | +0.247 | -189.74€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 5887 | +0.185 | -404.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 5887 | +0.185 | -404.08€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1130 | +0.424 | -45.26€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1130 | +0.424 | -45.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 457 | +0.437 | -6.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 457 | +0.437 | -6.21€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 451 | +0.425 | -16.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 451 | +0.425 | -16.14€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 208 | +0.395 | -19.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 208 | +0.395 | -19.04€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 93913 | +0.200 | -6805.69€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 93913 | +0.200 | -6805.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 16169 | +0.183 | -1732.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 16169 | +0.183 | -1732.03€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 15140 | +0.225 | -503.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 15140 | +0.225 | -503.70€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 16110 | +0.181 | -1694.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 16110 | +0.181 | -1694.92€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 15275 | +0.218 | -618.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 15275 | +0.218 | -618.41€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 15563 | +0.202 | -1013.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 15563 | +0.202 | -1013.01€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 15656 | +0.197 | -1243.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 15656 | +0.197 | -1243.62€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 36052 | +0.117 | +295.59€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 36052 | +0.117 | +295.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 17933 | +0.118 | +202.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 17933 | +0.118 | +202.93€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 18119 | +0.115 | +92.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 18119 | +0.115 | +92.66€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2302 | +0.295 | +3.02€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2302 | +0.295 | +3.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1056 | +0.282 | -22.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1056 | +0.282 | -22.83€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1118 | +0.301 | +22.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1118 | +0.301 | +22.98€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 128 | +0.339 | +2.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 128 | +0.339 | +2.86€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1055 | +0.444 | +10.05€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1055 | +0.444 | +10.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 511 | +0.438 | -3.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 511 | +0.438 | -3.30€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 496 | +0.452 | +12.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 496 | +0.452 | +12.49€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 48 | +0.400 | +0.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 48 | +0.400 | +0.86€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1813 | +0.069 | -75.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 715 | +0.047 | -62.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1098 | +0.084 | -13.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1385 | +0.077 | -33.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 287 | +0.050 | -20.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1098 | +0.084 | -13.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 346 | +0.029 | -46.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 346 | +0.029 | -46.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 72239 | +0.101 | -1753.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 5821 | +0.094 | +96.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 66418 | +0.101 | -1849.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 39588 | +0.105 | -404.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 5821 | +0.094 | +96.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 33767 | +0.107 | -500.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 15125 | +0.109 | -70.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 15125 | +0.109 | -70.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 17526 | +0.082 | -1277.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 17526 | +0.082 | -1277.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 904 | +0.189 | -110.96€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 904 | +0.189 | -110.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 904 | +0.189 | -110.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 904 | +0.189 | -110.96€ | 1 | 4 |
| ✅ GBM_LATE_15M | 49296 | +0.097 | +26891.37€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 49296 | +0.097 | +26891.37€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 8193 | +0.222 | +6937.83€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 8193 | +0.222 | +6937.83€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 7538 | +0.177 | +5870.25€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 7538 | +0.177 | +5870.25€ | 0 | 25 |
| ✅ GBM_LATE_15M#DOGE | 8836 | +0.204 | +6855.65€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 8836 | +0.204 | +6855.65€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 6746 | +0.051 | +2027.08€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 6746 | +0.051 | +2027.08€ | 1 | 17 |
| ✅ GBM_LATE_15M#SOL | 6881 | -0.032 | +1744.73€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 6881 | -0.032 | +1744.73€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 11102 | -0.027 | +3455.83€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 11102 | -0.027 | +3455.83€ | 4 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 52451 | +0.085 | +29664.86€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 52451 | +0.085 | +29664.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 10150 | +0.001 | +5247.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 10150 | +0.001 | +5247.18€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 11257 | +0.008 | +2886.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 11257 | +0.008 | +2886.94€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 7179 | +0.286 | +7936.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 7179 | +0.286 | +7936.56€ | 0 | 23 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 9750 | +0.014 | +2906.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 9750 | +0.014 | +2906.42€ | 1 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 8187 | +0.041 | +3532.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 8187 | +0.041 | +3532.76€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5928 | +0.311 | +7155.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5928 | +0.311 | +7155.00€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 39078 | +0.180 | +32117.69€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 39078 | +0.180 | +32117.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 5898 | +0.237 | +5415.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 5898 | +0.237 | +5415.41€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 6173 | +0.147 | +4645.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 6173 | +0.147 | +4645.76€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 6273 | +0.223 | +5389.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 6273 | +0.223 | +5389.33€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 6671 | +0.135 | +5214.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 6671 | +0.135 | +5214.74€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 7354 | +0.122 | +5483.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 7354 | +0.122 | +5483.33€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 6709 | +0.229 | +5969.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 6709 | +0.229 | +5969.11€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 10366 | +0.126 | +5059.35€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 10366 | +0.126 | +5059.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 456 | +0.159 | +291.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 456 | +0.159 | +291.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2978 | +0.131 | +1625.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2978 | +0.131 | +1625.20€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 491 | +0.153 | +259.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 491 | +0.153 | +259.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3102 | +0.133 | +1521.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3102 | +0.133 | +1521.57€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2620 | +0.095 | +1005.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2620 | +0.095 | +1005.32€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 719 | +0.141 | +356.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 719 | +0.141 | +356.21€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO | 49566 | +0.186 | +40196.37€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#15min | 49566 | +0.186 | +40196.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 7822 | +0.247 | +7465.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 7822 | +0.247 | +7465.99€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 7828 | +0.143 | +5455.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 7828 | +0.143 | +5455.92€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 8385 | +0.232 | +7477.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 8385 | +0.232 | +7477.32€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 8199 | +0.139 | +5917.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 8199 | +0.139 | +5917.95€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 8792 | +0.120 | +6138.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 8792 | +0.120 | +6138.58€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 8540 | +0.236 | +7740.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 8540 | +0.236 | +7740.60€ | 0 | 21 |
| ✅ GBM_LATE_5M | 13247 | +0.208 | +10642.97€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 13247 | +0.208 | +10642.97€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3179 | +0.213 | +2760.78€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3179 | +0.213 | +2760.78€ | 0 | 26 |
| ✅ GBM_LATE_5M#DOGE | 1221 | +0.198 | +915.96€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1221 | +0.198 | +915.96€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 3829 | +0.200 | +2830.96€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3829 | +0.200 | +2830.96€ | 0 | 26 |
| ✅ GBM_LATE_5M#SOL | 2011 | +0.201 | +1605.51€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2011 | +0.201 | +1605.51€ | 0 | 23 |
| ✅ GBM_LATE_5M#XRP | 1953 | +0.209 | +1529.48€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1953 | +0.209 | +1529.48€ | 0 | 0 |
| ✅ GBM_LATE_60M | 4233 | +0.056 | +1207.07€ | 0 | 7 |
| ✅ GBM_LATE_60M#60min | 4233 | +0.056 | +1207.07€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1513 | +0.070 | +495.74€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1513 | +0.070 | +495.74€ | 1 | 5 |
| ✅ GBM_LATE_60M#ETH | 1376 | +0.056 | +422.04€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1376 | +0.056 | +422.04€ | 1 | 7 |
| ✅ GBM_LATE_60M#SOL | 1344 | +0.039 | +289.28€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1344 | +0.039 | +289.28€ | 0 | 10 |
| 🚫 GBM_LATE_60M_FADE | 639 | -0.250 | -31.17€ | 9 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 639 | -0.250 | -31.17€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 239 | -0.247 | -16.76€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 239 | -0.247 | -16.76€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 230 | -0.246 | -6.48€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 230 | -0.246 | -6.48€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 170 | -0.256 | -7.92€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 170 | -0.256 | -7.92€ | 6 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1726 | +0.083 | +426.15€ | 1 | 12 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1726 | +0.083 | +426.15€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 671 | +0.078 | +161.08€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 671 | +0.078 | +161.08€ | 1 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 599 | +0.054 | +92.58€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 599 | +0.054 | +92.58€ | 2 | 13 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 456 | +0.127 | +172.49€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 456 | +0.127 | +172.49€ | 2 | 9 |
| ✅ LATE_WINDOW_5MIN | 192 | +0.278 | +203.97€ | 1 | 13 |
| ✅ LATE_WINDOW_5MIN#5min | 192 | +0.278 | +203.97€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 192 | +0.278 | +203.97€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 192 | +0.278 | +203.97€ | 1 | 13 |
| ✅ LEADLAG_BTC_XRP_15M | 3906 | +0.100 | +927.38€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3906 | +0.100 | +927.38€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3906 | +0.100 | +927.38€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3906 | +0.100 | +927.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 749 | -0.013 | +9.18€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 749 | -0.013 | +9.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 7 | -0.058 | -1.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 7 | -0.058 | -1.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 222 | -0.004 | +5.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 222 | -0.004 | +5.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 27 | -0.155 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 27 | -0.155 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 195 | +0.038 | +17.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 195 | +0.038 | +17.32€ | 2 | 3 |
| ✅ LIQUIDACIONES_15M#SOL | 246 | -0.004 | +2.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 246 | -0.004 | +2.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4007 | +0.017 | +102.82€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 4007 | +0.017 | +102.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 188 | +0.032 | -0.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 188 | +0.032 | -0.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 815 | +0.015 | +40.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 815 | +0.015 | +40.20€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 216 | +0.000 | +1.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 216 | +0.000 | +1.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1556 | +0.021 | +29.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1556 | +0.021 | +29.44€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 762 | +0.012 | +2.17€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 762 | +0.012 | +2.17€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 470 | +0.015 | +29.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 470 | +0.015 | +29.46€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2026 | -0.038 | -26.75€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2026 | -0.038 | -26.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 609 | -0.032 | -13.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 609 | -0.032 | -13.45€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 706 | -0.013 | +10.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 706 | -0.013 | +10.16€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 711 | -0.069 | -23.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 711 | -0.069 | -23.46€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 11916 | -0.033 | -140.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 5694 | -0.036 | -105.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 6222 | -0.030 | -34.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 416 | -0.048 | -21.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 206 | -0.024 | -0.65€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 210 | -0.071 | -20.47€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 3081 | -0.022 | +11.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1461 | -0.022 | +6.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1620 | -0.023 | +4.80€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1239 | -0.025 | +19.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 630 | -0.033 | +0.08€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 609 | -0.017 | +19.13€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 2648 | -0.040 | -78.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1247 | -0.046 | -53.90€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1401 | -0.035 | -24.74€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 2291 | -0.032 | -17.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1103 | -0.038 | -21.61€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1188 | -0.026 | +3.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 2241 | -0.042 | -53.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1047 | -0.048 | -36.08€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1194 | -0.037 | -17.28€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 58059 | -0.000 | +3006.80€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 58059 | -0.000 | +3006.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 10502 | +0.027 | +1367.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 10502 | +0.027 | +1367.98€ | 2 | 4 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 8244 | -0.035 | -113.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 8244 | -0.035 | -113.41€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 10625 | +0.024 | +1106.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 10625 | +0.024 | +1106.30€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 8132 | -0.048 | -151.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 8132 | -0.048 | -151.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 9838 | -0.005 | +260.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 9838 | -0.005 | +260.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 10718 | +0.017 | +537.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 10718 | +0.017 | +537.12€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6912 | -0.056 | -140.87€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6912 | -0.056 | -140.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1237 | -0.002 | -17.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1237 | -0.002 | -17.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1897 | -0.069 | -33.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1897 | -0.069 | -33.04€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 66 | -0.015 | -0.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 66 | -0.015 | -0.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 791 | -0.119 | -33.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 791 | -0.119 | -33.96€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2063 | -0.070 | -30.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2063 | -0.070 | -30.61€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 143301 | -0.077 | +1964.36€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 143301 | -0.077 | +1964.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 24989 | -0.079 | +1335.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 24989 | -0.079 | +1335.50€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 21505 | -0.099 | -1015.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 21505 | -0.099 | -1015.74€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 25312 | -0.069 | +1224.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 25312 | -0.069 | +1224.88€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 21050 | -0.096 | -594.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 21050 | -0.096 | -594.62€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 25700 | -0.056 | +349.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 25700 | -0.056 | +349.35€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 24745 | -0.069 | +664.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 24745 | -0.069 | +664.97€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8931 | -0.035 | -186.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8931 | -0.035 | -186.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1002 | -0.017 | -19.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1002 | -0.017 | -19.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2055 | -0.048 | -30.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2055 | -0.048 | -30.39€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2621 | -0.026 | -39.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2621 | -0.026 | -39.52€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1241 | -0.061 | -33.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1241 | -0.061 | -33.25€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1003 | -0.030 | -32.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1003 | -0.030 | -32.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 1896 | +0.120 | +750.68€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1760 | +0.124 | +738.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 413 | +0.119 | +177.61€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 413 | +0.119 | +177.61€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 368 | +0.114 | +123.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 368 | +0.114 | +123.66€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#ETH | 338 | +0.138 | +168.70€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 338 | +0.138 | +168.70€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 307 | +0.150 | +168.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 307 | +0.150 | +168.50€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 334 | +0.101 | +99.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 334 | +0.101 | +99.62€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1771 | -0.018 | -25.44€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1771 | -0.018 | -25.44€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 337 | -0.002 | +8.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 337 | -0.002 | +8.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 322 | -0.037 | -12.80€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 322 | -0.037 | -12.80€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 449 | -0.045 | -35.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 449 | -0.045 | -35.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 371 | +0.004 | +3.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 371 | +0.004 | +3.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 292 | +0.000 | +10.03€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 292 | +0.000 | +10.03€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1008 | -0.076 | -51.55€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 467 | -0.110 | -80.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 365 | -0.135 | -66.31€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 102 | -0.019 | -14.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 353 | -0.035 | +22.95€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 255 | -0.025 | +26.53€ | 2 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 98 | -0.060 | -3.59€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 188 | -0.068 | +5.89€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 156 | -0.076 | +2.01€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 32 | -0.029 | +3.88€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 776 | -0.087 | -37.77€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 232 | -0.038 | -13.79€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1248 | -0.209 | -82.15€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 488 | -0.210 | -49.36€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 430 | -0.213 | -48.62€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 58 | -0.183 | -0.74€ | 1 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 420 | -0.213 | -37.32€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 371 | -0.224 | -43.82€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 49 | -0.128 | +6.50€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 340 | -0.199 | +4.53€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 317 | -0.196 | +1.81€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 23 | -0.220 | +2.71€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1118 | -0.212 | -90.62€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 130 | -0.174 | +8.47€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 492 | +0.389 | +465.74€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#BTC | 84 | +0.174 | +61.71€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 84 | +0.174 | +61.71€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#ETH | 112 | +0.360 | +101.13€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 112 | +0.360 | +101.13€ | 0 | 7 |
| ✅ RESOLUTION_SNIPER#SOL | 296 | +0.456 | +302.91€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 296 | +0.456 | +302.91€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 492 | +0.389 | +465.74€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 814 | +0.038 | +67.27€ | 2 | 4 |
| ✅ STREAK_FADE_15M#15min | 814 | +0.038 | +67.27€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 310 | +0.026 | +5.92€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 310 | +0.026 | +5.92€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 67 | -0.007 | -1.40€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 67 | -0.007 | -1.40€ | 1 | 0 |
| ✅ STREAK_FADE_15M#SOL | 80 | +0.012 | +5.58€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 80 | +0.012 | +5.58€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 357 | +0.063 | +57.17€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 357 | +0.063 | +57.17€ | 1 | 5 |
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
| ✅ STREAK_FADE_60M | 109 | -0.041 | -8.88€ | 2 | 0 |
| ✅ STREAK_FADE_60M#60min | 109 | -0.041 | -8.88€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 43 | -0.100 | -5.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 43 | -0.100 | -5.07€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 66 | +0.000 | -3.81€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 66 | +0.000 | -3.81€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 11377 | +0.015 | +80.34€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11377 | +0.015 | +80.34€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2936 | +0.019 | +27.11€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2936 | +0.019 | +27.11€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2952 | +0.018 | +37.88€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2952 | +0.018 | +37.88€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2910 | +0.009 | -1.79€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2910 | +0.009 | -1.79€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2579 | +0.013 | +17.14€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2579 | +0.013 | +17.14€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 10575 | +0.014 | -41.98€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 10575 | +0.014 | -41.98€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4400 | +0.019 | -1.75€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4400 | +0.019 | -1.75€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3627 | +0.010 | -28.45€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3627 | +0.010 | -28.45€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2548 | +0.011 | -11.78€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2548 | +0.011 | -11.78€ | 1 | 0 |
| ✅ UPDOWN_GBM | 87891 | +0.056 | +7927.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 21193 | +0.083 | +4539.11€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2770 | +0.002 | +32.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 58350 | +0.054 | +3265.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 5263 | +0.003 | +92.76€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 7059 | +0.093 | +1142.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1576 | +0.156 | +698.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5406 | +0.076 | +445.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 20245 | +0.057 | +1755.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2938 | +0.085 | +678.82€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 777 | +0.004 | +14.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 14041 | +0.064 | +992.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2376 | +0.001 | +67.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 113 | -0.074 | +2.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 9279 | +0.072 | +977.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1555 | +0.147 | +610.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 7646 | +0.057 | +368.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 20987 | +0.047 | +1418.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 5225 | +0.072 | +798.77€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 744 | +0.007 | +18.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 12993 | +0.047 | +581.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1919 | +0.005 | +17.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 106 | -0.102 | +2.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 19032 | +0.036 | +1028.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 5449 | +0.037 | +436.14€ | 0 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 706 | -0.010 | +2.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 11815 | +0.043 | +587.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 968 | +0.004 | +7.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 94 | -0.135 | -6.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 11287 | +0.069 | +1606.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4450 | +0.103 | +1316.34€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 6449 | +0.049 | +290.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 313 | -0.103 | -0.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 924 | +0.365 | +336.80€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 924 | +0.365 | +336.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 466 | +0.361 | +160.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 466 | +0.361 | +160.58€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 458 | +0.367 | +176.22€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 458 | +0.367 | +176.22€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 21607 | -0.022 | +5174.75€ | 2 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 21607 | -0.022 | +5174.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 4064 | -0.113 | +182.81€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 4064 | -0.113 | +182.81€ | 3 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2838 | +0.220 | +1822.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2838 | +0.220 | +1822.89€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 6169 | -0.061 | +834.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 6169 | -0.061 | +834.45€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5870 | -0.064 | +1061.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5870 | -0.064 | +1061.33€ | 1 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 266 | +0.063 | +25.42€ | 0 | 7 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 266 | +0.063 | +25.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 266 | +0.063 | +25.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 266 | +0.063 | +25.42€ | 0 | 7 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1617 | +0.286 | +1350.79€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1617 | +0.286 | +1350.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 862 | +0.280 | +675.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 862 | +0.280 | +675.67€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 755 | +0.293 | +675.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 755 | +0.293 | +675.12€ | 0 | 9 |
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
| ✅ WEEKLY_PRICE | 4064 | +0.301 | +1877.65€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1519 | +0.257 | +180.53€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1561 | +0.295 | +675.33€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 984 | +0.380 | +1021.79€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.022 n=1095 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1095 IC=+0.022 PNL=+47.60€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 765 celda(s) pasan gate riguroso completo de 2788 evaluadas (n>=40) y 3876 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.038 < 0.08 — monitorear
  - _Datos_: n=5443 IC=+0.038 PNL=+439.89€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1561/15 IC=+0.295 PNL=+675.33€ | BTC: n=1519/15 IC=+0.257 PNL=+180.53€ | SOL: n=984/15 IC=+0.380 PNL=+1021.79€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.141 n=907/60 | contraria IC=+0.188 n=938 | gap=-0.047 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=520, boost estimado=+0.017. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1917/40 IC=+0.005 PNL=+17.64€ | BTC#60min: n=2375/40 IC=+0.001 PNL=+67.55€ | SOL#60min: n=968/40 IC=+0.004 PNL=+7.98€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.047 n=636369 | tras_1loss IC=+0.097 n=483107 | tras_2loss IC=+0.067 n=194522/40 | gap=-0.020 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.185 > 0.08 con n=849 PNL=+596.32€
  - _Datos_: n=849 IC=+0.185 PNL=+596.32€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.155 > 0.08 con n=974 PNL=+512.97€
  - _Datos_: n=974 IC=+0.155 PNL=+512.97€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.167 > 0.08 con n=70 PNL=+36.69€
  - _Datos_: n=70 IC=+0.167 PNL=+36.69€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.332 > 0.1 con n=3320 PNL=+1840.37€
  - _Datos_: n=3320 IC=+0.332 PNL=+1840.37€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=850 IC=+0.069 PNL=+87.01€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=850 IC=+0.069 PNL=+87.01€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=95 IC=+0.191 PNL=+66.70€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=95 IC=+0.191 PNL=+66.70€

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
  - _Estado_: n=3534 IC=+0.004 PNL=-4.08€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3534 IC=+0.004 PNL=-4.08€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1726 IC=+0.001 PNL=+97.25€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1726 IC=+0.001 PNL=+97.25€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1095 IC=+0.022 PNL=+47.60€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1095 IC=+0.022 PNL=+47.60€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.165 > 0.1 con n=5458 PNL=+3167.45€
  - _Datos_: n=5458 IC=+0.165 PNL=+3167.45€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=2937 IC=+0.085 PNL=+678.32€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=2937 IC=+0.085 PNL=+678.32€

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
  - _Estado_: n=1111 IC=+0.038 PNL=+89.24€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1111 IC=+0.038 PNL=+89.24€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=144 IC=+0.007 PNL=+0.59€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=144 IC=+0.007 PNL=+0.59€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.278 n=192) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=192 IC=+0.278 PNL=+203.97€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.123 > 0.02 con n=1104 PNL=+458.49€
  - _Datos_: n=1104 IC=+0.123 PNL=+458.49€

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
  - _Estado_: n=35188 IC=+0.073 PNL=+4919.04€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=35188 IC=+0.073 PNL=+4919.04€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.137 < -0.1 con n=635 PNL=+90.40€
  - _Datos_: n=635 IC=-0.137 PNL=+90.40€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=3243 IC=+0.070 PNL=+438.91€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=3243 IC=+0.070 PNL=+438.91€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=165 IC=-0.111 PNL=+0.04€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=165 IC=-0.111 PNL=+0.04€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.108 > 0.1 con n=946 PNL=+250.85€
  - _Datos_: n=946 IC=+0.108 PNL=+250.85€

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
  - _Estado_: n=37545 IC=-0.136 PNL=+2620.01€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=37545 IC=-0.136 PNL=+2620.01€

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
  - _Estado_: n=3889 IC=+0.130 PNL=+2510.51€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=3889 IC=+0.130 PNL=+2510.51€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=9079 IC=+0.055 PNL=+766.65€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=9079 IC=+0.055 PNL=+766.65€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.098 > 0.08 con n=4027 PNL=+2242.83€
  - _Datos_: n=4027 IC=+0.098 PNL=+2242.83€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.221 < -0.1 con n=3991 PNL=-337.88€
  - _Datos_: n=3991 IC=-0.221 PNL=-337.88€

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
  - _Estado_: n=78 IC=+0.025 PNL=+11.12€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=78 IC=+0.025 PNL=+11.12€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.101 n=1978) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1978 IC=+0.101 PNL=+422.96€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.408 n=630) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=630 IC=+0.408 PNL=+901.05€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=16160 IC=+0.183 PNL=-1728.05€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=16160 IC=+0.183 PNL=-1728.05€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.227 > 0.1 con n=254 PNL=+173.35€
  - _Datos_: n=254 IC=+0.227 PNL=+173.35€
