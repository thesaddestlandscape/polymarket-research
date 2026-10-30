# Hipótesis automáticas — 2026-10-30 07:35 UTC
_Generado por shadow_postmortem.py sobre 1116556 resoluciones (PNL=+149230.67€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.224 (n=871)

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

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=990)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `3310.5904` → IC=+0.140 (n=607)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3310.5904 (IC base=+0.133)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.219 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.137)

- **PATRÓN** `n_total_lado` > `67.0` → IC=+0.194 (n=263)

  - _Acción_: Kelly boost +0.97€ cuando `n_total_lado` > 67.0 (IC base=+0.137)

- **PATRÓN** `banda_hit_calibrado` > `0.6121` → IC=+0.249 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6121 (IC base=+0.137)

- **PATRÓN** `banda_z` > `9.189` → IC=+0.202 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.189 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=281)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=890)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `3044.446` → IC=+0.140 (n=697)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3044.446 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `9140.8813` → IC=+0.122 (n=215)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 9140.8813 (IC base=+0.009)

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

- **PATRÓN** `n_ballena_banda` > `30.0` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 30.0 (IC base=+0.156)

- **PATRÓN** `n_total_lado` > `43.0` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 43.0 (IC base=+0.156)

- **PATRÓN** `banda_hit_calibrado` > `0.6044` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `banda_hit_calibrado` > 0.6044 (IC base=+0.156)

- **PATRÓN** `banda_z` > `2.518` → IC=+0.238 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 2.518 (IC base=+0.156)

- **PATRÓN** `ballenas_wallet_edge_medio` > `2.641` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `ballenas_wallet_edge_medio` > 2.641 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.227 (n=31)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.156)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.207 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `2452.7664` → IC=+0.214 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2452.7664 (IC base=+0.156)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `137.84` → IC=-0.209 (n=10901)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 137.84
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=32703)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `127.45` → IC=-0.261 (n=1152)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.45
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=3459)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `117.67` → IC=-0.303 (n=1148)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 117.67
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3445)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `160.48` → IC=-0.236 (n=2935)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 160.48
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=8808)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `131.97` → IC=-0.261 (n=2097)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.97
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=6291)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.212 (n=24389)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.122 (n=4678)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `8687.4558` → IC=+0.163 (n=2157)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 8687.4558 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.127 (n=20892)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=25537)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.225 (n=19369)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=7726)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6748.6729` → IC=+0.153 (n=2989)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 6748.6729 (IC base=+0.124)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=2130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.364 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.185 (n=2606)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `9429.1216` → IC=+0.183 (n=1814)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 9429.1216 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.187 (n=1862)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.184 (n=2081)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` < `0.295` → IC=+0.312 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.295 (IC base=+0.181)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=2667)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `16179.5763` → IC=+0.187 (n=688)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 16179.5763 (IC base=+0.181)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.170 (n=522)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.61 (IC base=+0.077)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.140 (n=1243)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.44 (IC base=+0.082)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=4703)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.164 (n=3994)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 15.0 (IC base=+0.161)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.374 (n=1533)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.214 (n=2109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.348 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=2456)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=1190)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.151 (n=1012)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 15.0 (IC base=+0.144)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.264 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.145 (n=1307)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `2237.492` → IC=+0.158 (n=516)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2237.492 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `3079.6088` → IC=+0.132 (n=229)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 3079.6088 (IC base=+0.069)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.251 (n=895)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.226)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1257)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.147 (n=1355)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.153 (n=708)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.145)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.286 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=899)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.145)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `py_entrada` > `0.555` → IC=+0.170 (n=431)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.555 (IC base=+0.069)

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

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=20823)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.200 (n=17672)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.230 (n=8606)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.198)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.181 (n=2258)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.178 (n=4753)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 18.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.183 (n=4603)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.177)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.218 (n=2629)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.219 (n=2344)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.216)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.292 (n=877)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.216)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=4688)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.180 (n=3990)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.177 (n=4878)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.186 (n=3650)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.255 (n=4009)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.247)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.248 (n=3406)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.247)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.357 (n=1351)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=4597)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.190 (n=3923)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.189 (n=3419)

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

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.245 (n=27396)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.201)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.192 (n=4041)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 18.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.184 (n=8689)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 12.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.196 (n=12300)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.71 (IC base=+0.183)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=5654)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.226 (n=5579)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.286 (n=3921)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.186 (n=4669)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.200 (n=9570)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.229 (n=3808)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=4378)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.272 (n=3848)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `12.0` → IC=+0.206 (n=7813)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.259 (n=4027)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=4522)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.201 (n=4541)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.243 (n=5692)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=9743)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=9937)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.38` → IC=+0.138 (n=9009)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.38 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=4792)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.118)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.143 (n=4520)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=5984)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.118)

- **PATRÓN** `lag_apertura_s` < `2.64` → IC=+0.144 (n=4466)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 2.64 (IC base=+0.118)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.191 (n=4951)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.115)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.135 (n=5417)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.115)

- **PATRÓN** `lag_apertura_s` < `3.25` → IC=+0.137 (n=5963)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.25 (IC base=+0.115)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.313 (n=1230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.294)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.388 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `3872.2908` → IC=+0.295 (n=782)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3872.2908 (IC base=+0.294)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.289 (n=832)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.281)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.364 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `5132.4682` → IC=+0.301 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5132.4682 (IC base=+0.281)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.326 (n=595)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.301)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.304 (n=869)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.301)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.399 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.301)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.301 (n=988)

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
- **FILTRO** `hora_utc` < `5.0` → IC=-0.292 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=101)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.287 (n=59)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=64)

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
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=101)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.287 (n=59)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=64)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4771` → IC=+0.139 (n=15265)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4771 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.125 (n=15397)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.125 (n=10659)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.375` → IC=+0.166 (n=15273)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.375 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.7815` → IC=+0.278 (n=849)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7815 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.829` → IC=+0.190 (n=5787)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 5.829 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6213` → IC=+0.265 (n=4482)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6213 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.3035` → IC=+0.246 (n=1575)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3035 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.3507` → IC=+0.229 (n=4948)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3507 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=7787)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `4385.6554` → IC=+0.151 (n=5088)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4385.6554 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.122 (n=9502)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0059 (IC base=+0.079)

- **PATRÓN** `ibs_20min` < `0.5667` → IC=+0.143 (n=18979)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5667 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` > `0.6071` → IC=+0.188 (n=1259)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.6071 (IC base=+0.079)

- **PATRÓN** `volumen_regimen` < `0.864` → IC=+0.190 (n=5074)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.864 (IC base=+0.079)

- **PATRÓN** `volumen_pendiente_norm` > `0.2973` → IC=+0.230 (n=1874)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2973 (IC base=+0.079)

- **PATRÓN** `volumen_spike_ratio` > `2.6859` → IC=+0.208 (n=4304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6859 (IC base=+0.079)

- **PATRÓN** `ballena_activa_n` < `105.0` → IC=+0.224 (n=12794)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 105.0 (IC base=+0.079)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3609` → IC=+0.210 (n=3293)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3609 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.218 (n=1599)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.212 (n=2210)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `0.9831` → IC=+0.280 (n=1495)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9831 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.673` → IC=+0.281 (n=1460)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.673 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.2834` → IC=+0.259 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2834 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `1.4375` → IC=+0.208 (n=3150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4375 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=3596)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `2043.15` → IC=+0.206 (n=1098)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2043.15 (IC base=+0.206)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.225 (n=1962)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.242 (n=2831)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.0883` → IC=+0.275 (n=944)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0883 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.243 (n=2944)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.5506` → IC=+0.259 (n=2829)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5506 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` < `0.0954` → IC=+0.243 (n=2554)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0954 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2919` → IC=+0.260 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2919 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.4424` → IC=+0.242 (n=896)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4424 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `1.8649` → IC=+0.242 (n=1790)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8649 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=3234)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1489.1` → IC=+0.243 (n=2527)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1489.1 (IC base=+0.239)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.237 (n=910)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.342` → IC=+0.237 (n=2728)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.342 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.238 (n=2851)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.9284` → IC=+0.270 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9284 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `0.1308` → IC=+0.233 (n=1427)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1308 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.188` → IC=+0.258 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.188 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` < `1.2278` → IC=+0.227 (n=2729)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2278 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `0.6236` → IC=+0.230 (n=2728)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6236 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.273 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.403` → IC=+0.228 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.403 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `2.4324` → IC=+0.254 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4324 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.150 (n=2904)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0059 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.0775` → IC=+0.163 (n=969)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.0775 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.155 (n=1083)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.72` → IC=+0.171 (n=2904)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.72 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.904` → IC=+0.139 (n=471)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 10.904 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.067` → IC=+0.137 (n=2649)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 4.067 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `1.2035` → IC=+0.138 (n=2904)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.2035 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.0973` → IC=+0.153 (n=1056)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.0973 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `2.4451` → IC=+0.139 (n=2780)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.4451 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=3765)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `207.0` → IC=+0.172 (n=1204)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 207.0 (IC base=+0.130)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.215 (n=1157)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.198 (n=3625)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=3094)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.266 (n=1337)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.118` → IC=+0.280 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.118 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.0969` → IC=+0.196 (n=3077)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0969 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.3526` → IC=+0.218 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3526 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.7037` → IC=+0.209 (n=1525)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7037 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=4141)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `1922.7184` → IC=+0.202 (n=1567)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1922.7184 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.222 (n=2771)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.1782` → IC=+0.231 (n=1383)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1782 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=1186)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.219 (n=1443)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` < `0.0345` → IC=+0.270 (n=1048)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0345 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.131` → IC=+0.260 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.131 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.3494` → IC=+0.261 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3494 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.7662` → IC=+0.226 (n=1363)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7662 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=1581)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `1911.16` → IC=+0.223 (n=1425)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1911.16 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.220 (n=1976)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.218)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.149 (n=169)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=4169)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.159 (n=599)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0037 (IC base=+0.059)

- **PATRÓN** `ibs_20min` > `0.9523` → IC=+0.236 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9523 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.1401` → IC=+0.336 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1401 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.227` → IC=+0.199 (n=1295)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 5.227 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` > `0.6945` → IC=+0.341 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6945 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.3037` → IC=+0.344 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3037 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` < `1.4169` → IC=+0.342 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4169 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` > `2.2614` → IC=+0.339 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2614 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.334 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 143.0 (IC base=+0.059)

- **PATRÓN** `ibs_20min` < `0.0909` → IC=+0.184 (n=1085)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.0909 (IC base=+0.045)

- **PATRÓN** `dist_vwap_pct` > `0.7317` → IC=+0.165 (n=255)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.7317 (IC base=+0.045)

- **PATRÓN** `volumen_regimen` < `0.8367` → IC=+0.158 (n=1338)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8367 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.2857` → IC=+0.211 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2857 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` < `1.7817` → IC=+0.148 (n=1287)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.7817 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` > `2.1577` → IC=+0.165 (n=875)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.1577 (IC base=+0.045)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.177 (n=122)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=646)

- **FILTRO** `ibs_20min` < `0.2647` → IC=-0.168 (n=191)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2647
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=577)

- **FILTRO** `ibs_20min` > `0.2069` → IC=-0.133 (n=4080)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2069
  - _Potencial_: sin este filtro IC_bueno=+0.151 (n=2011)

- **FILTRO** `sigma_ewma_delta_pct` > `8.527` → IC=-0.227 (n=654)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.527
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=5437)

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

- **PATRÓN** `ibs_20min` < `0.2069` → IC=+0.151 (n=2011)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.2069 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` < `0.1948` → IC=+0.277 (n=873)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1948 (IC base=-0.039)

- **PATRÓN** `volumen_regimen` < `0.6941` → IC=+0.308 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6941 (IC base=-0.039)

- **PATRÓN** `volumen_pendiente_norm` < `0.1046` → IC=+0.287 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1046 (IC base=-0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.0793` → IC=+0.295 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0793 (IC base=-0.039)

- **PATRÓN** `volumen_spike_ratio` < `2.4676` → IC=+0.306 (n=796)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4676 (IC base=-0.039)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.5999` → IC=-0.184 (n=1142)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.5999
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=3428)

- **FILTRO** `ibs_20min` < `0.764` → IC=-0.156 (n=3016)

  - _Acción_: SKIP cuando `ibs_20min` < 0.764
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=1554)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.168 (n=1065)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=3505)

- **FILTRO** `ibs_20min` > `0.7458` → IC=-0.198 (n=1621)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7458
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=4866)

- **PATRÓN** `dist_vwap_pct` > `0.7251` → IC=+0.346 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7251 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` < `0.2511` → IC=+0.307 (n=730)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2511 (IC base=-0.065)

- **PATRÓN** `volumen_regimen` > `0.7047` → IC=+0.321 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7047 (IC base=-0.065)

- **PATRÓN** `volumen_pendiente_norm` < `0.1024` → IC=+0.306 (n=778)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1024 (IC base=-0.065)

- **PATRÓN** `volumen_spike_ratio` < `1.4259` → IC=+0.318 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4259 (IC base=-0.065)

- **PATRÓN** `volumen_spike_ratio` > `1.8546` → IC=+0.312 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8546 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` > `0.8075` → IC=+0.280 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8075 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` < `0.7264` → IC=+0.269 (n=810)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7264 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` > `1.0657` → IC=+0.286 (n=835)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0657 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.1687` → IC=+0.286 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1687 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `2.1737` → IC=+0.266 (n=1511)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1737 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `1.4298` → IC=+0.266 (n=1717)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4298 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.207 (n=6647)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.093)

- **PATRÓN** `ibs_20min` > `0.3069` → IC=+0.166 (n=19926)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.3069 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.9369` → IC=+0.302 (n=1434)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9369 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.567` → IC=+0.166 (n=8919)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.567 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` < `1.1739` → IC=+0.267 (n=7333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1739 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` > `0.6915` → IC=+0.275 (n=6551)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6915 (IC base=+0.093)

- **PATRÓN** `volumen_pendiente_norm` > `0.2401` → IC=+0.287 (n=2199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2401 (IC base=+0.093)

- **PATRÓN** `volumen_spike_ratio` > `2.6493` → IC=+0.279 (n=3883)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6493 (IC base=+0.093)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.303 (n=11244)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 91.0 (IC base=+0.093)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.157 (n=6420)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0097 (IC base=+0.078)

- **PATRÓN** `ibs_20min` < `0.6479` → IC=+0.148 (n=19257)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.6479 (IC base=+0.078)

- **PATRÓN** `volumen_regimen` < `0.7045` → IC=+0.268 (n=2744)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7045 (IC base=+0.078)

- **PATRÓN** `volumen_regimen` > `1.1955` → IC=+0.270 (n=2078)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1955 (IC base=+0.078)

- **PATRÓN** `volumen_pendiente_norm` > `0.2946` → IC=+0.320 (n=1350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2946 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` < `1.5796` → IC=+0.295 (n=3985)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5796 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` > `2.2822` → IC=+0.289 (n=4106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2822 (IC base=+0.078)

- **PATRÓN** `ballena_activa_n` < `75.0` → IC=+0.300 (n=8989)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 75.0 (IC base=+0.078)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.5801` → IC=-0.155 (n=2706)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5801
  - _Potencial_: sin este filtro IC_bueno=+0.205 (n=2708)

- **FILTRO** `ibs_20min` > `0.7253` → IC=-0.222 (n=1172)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7253
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=3518)

- **FILTRO** `sigma_ewma_delta_pct` > `4.289` → IC=-0.223 (n=1013)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.289
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=3677)

- **PATRÓN** `ibs_20min` > `0.9283` → IC=+0.332 (n=1354)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9283 (IC base=+0.025)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.107` → IC=+0.183 (n=1816)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 3.107 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.2294` → IC=+0.318 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2294 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.4472` → IC=+0.268 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4472 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` > `2.2535` → IC=+0.290 (n=800)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2535 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.309 (n=1185)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.025)

- **PATRÓN** `ibs_20min` < `0.1688` → IC=+0.160 (n=1173)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1688 (IC base=-0.027)

- **PATRÓN** `volumen_pendiente_norm` < `0.0939` → IC=+0.408 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0939 (IC base=-0.027)

- **PATRÓN** `volumen_spike_ratio` < `2.6507` → IC=+0.410 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6507 (IC base=-0.027)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.402 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=-0.027)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1192` → IC=+0.220 (n=976)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1192 (IC base=+0.018)

- **PATRÓN** `volumen_regimen` < `1.1951` → IC=+0.203 (n=1959)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1951 (IC base=+0.018)

- **PATRÓN** `volumen_regimen` > `0.6925` → IC=+0.208 (n=1750)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6925 (IC base=+0.018)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.251 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.018)

- **PATRÓN** `volumen_spike_ratio` < `1.4214` → IC=+0.231 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4214 (IC base=+0.018)

- **PATRÓN** `volumen_spike_ratio` > `2.4465` → IC=+0.209 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4465 (IC base=+0.018)

- **PATRÓN** `ballena_activa_n` < `267.0` → IC=+0.237 (n=1290)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 267.0 (IC base=+0.018)

- **PATRÓN** `volumen_regimen` < `1.1702` → IC=+0.236 (n=1336)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1702 (IC base=-0.002)

- **PATRÓN** `volumen_regimen` > `0.623` → IC=+0.240 (n=1335)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.623 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2707` → IC=+0.300 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2707 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.5357` → IC=+0.242 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5357 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.1553` → IC=+0.253 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1553 (IC base=-0.002)

- **PATRÓN** `ballena_activa_n` < `214.0` → IC=+0.246 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 214.0 (IC base=-0.002)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.320 (n=1293)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.276)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.284 (n=2988)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.276)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.317 (n=1536)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.276)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.672` → IC=+0.308 (n=935)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.672 (IC base=+0.276)

- **PATRÓN** `volumen_pendiente_norm` < `0.1312` → IC=+0.287 (n=2624)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1312 (IC base=+0.276)

- **PATRÓN** `volumen_spike_ratio` > `3.222` → IC=+0.289 (n=919)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.222 (IC base=+0.276)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.285 (n=3383)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.276)

- **PATRÓN** `libro_liquidez` > `2024.5984` → IC=+0.288 (n=948)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2024.5984 (IC base=+0.276)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.298 (n=1700)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.276)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.325 (n=1680)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.297)

- **PATRÓN** `drift_60min` |x|≤ `0.1801` → IC=+0.313 (n=1109)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1801 (IC base=+0.297)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.325 (n=962)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.300 (n=875)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.297)

- **PATRÓN** `ibs_20min` < `0.0055` → IC=+0.300 (n=1109)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0055 (IC base=+0.297)

- **PATRÓN** `ibs_20min` > `0.1331` → IC=+0.306 (n=1680)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1331 (IC base=+0.297)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.352` → IC=+0.309 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.352 (IC base=+0.297)

- **PATRÓN** `volumen_pendiente_norm` < `0.198` → IC=+0.297 (n=2477)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.198 (IC base=+0.297)

- **PATRÓN** `volumen_pendiente_norm` > `0.3436` → IC=+0.306 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3436 (IC base=+0.297)

- **PATRÓN** `volumen_spike_ratio` < `1.739` → IC=+0.301 (n=1065)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.739 (IC base=+0.297)

- **PATRÓN** `volumen_spike_ratio` > `2.7146` → IC=+0.309 (n=1097)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7146 (IC base=+0.297)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.299 (n=1275)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.297)

- **PATRÓN** `libro_liquidez` > `1912.5061` → IC=+0.304 (n=1143)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1912.5061 (IC base=+0.297)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.307 (n=1150)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.297)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7328` → IC=-0.181 (n=1232)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7328
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=3698)

- **PATRÓN** `ibs_20min` > `0.8653` → IC=+0.165 (n=1194)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.8653 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.1489` → IC=+0.231 (n=891)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1489 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.2118` → IC=+0.231 (n=1470)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2118 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `1.0078` → IC=+0.237 (n=1495)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0078 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `0.669` → IC=+0.231 (n=1517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.669 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.1022` → IC=+0.241 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1022 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.4628` → IC=+0.238 (n=1645)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4628 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `119.0` → IC=+0.253 (n=1681)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 119.0 (IC base=+0.025)

- **PATRÓN** `ibs_20min` < `0.0952` → IC=+0.154 (n=1233)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.0952 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` < `1.0229` → IC=+0.242 (n=1053)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0229 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.306 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.7916` → IC=+0.274 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7916 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.4356` → IC=+0.260 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4356 (IC base=+0.003)

- **PATRÓN** `ballena_activa_n` < `121.0` → IC=+0.263 (n=1159)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 121.0 (IC base=+0.003)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.75` → IC=-0.236 (n=2060)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.312 (n=2081)

- **FILTRO** `ibs_20min` > `0.6341` → IC=-0.234 (n=1003)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6341
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=3012)

- **FILTRO** `sigma_ewma_delta_pct` > `8.409` → IC=-0.251 (n=460)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.409
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=3555)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.312 (n=2081)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.75 (IC base=+0.040)

- **PATRÓN** `dist_vwap_pct` > `0.213` → IC=+0.345 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.213 (IC base=+0.040)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.332` → IC=+0.193 (n=649)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 9.332 (IC base=+0.040)

- **PATRÓN** `volumen_regimen` < `0.8478` → IC=+0.341 (n=1019)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8478 (IC base=+0.040)

- **PATRÓN** `volumen_regimen` > `0.6975` → IC=+0.335 (n=1365)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6975 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` < `0.1597` → IC=+0.334 (n=1582)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1597 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.352 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` < `1.4413` → IC=+0.357 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4413 (IC base=+0.040)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.354 (n=1306)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.040)

- **PATRÓN** `ibs_20min` < `0.6341` → IC=+0.133 (n=3012)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.6341 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` < `0.2867` → IC=+0.252 (n=1434)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2867 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` < `0.6964` → IC=+0.276 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6964 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.0707` → IC=+0.267 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0707 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` < `2.4559` → IC=+0.258 (n=1371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4559 (IC base=+0.041)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.273 (n=1397)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.041)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.354 (n=1922)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.310)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.311 (n=2168)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.310)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.318 (n=1024)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.310)

- **PATRÓN** `ibs_20min` > `0.7628` → IC=+0.347 (n=1921)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7628 (IC base=+0.310)

- **PATRÓN** `dist_vwap_pct` > `0.2054` → IC=+0.335 (n=1188)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2054 (IC base=+0.310)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.842` → IC=+0.329 (n=1042)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.842 (IC base=+0.310)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.11` → IC=+0.311 (n=2449)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.11 (IC base=+0.310)

- **PATRÓN** `volumen_regimen` > `0.6291` → IC=+0.320 (n=2150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6291 (IC base=+0.310)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.349 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.310)

- **PATRÓN** `volumen_spike_ratio` > `1.4303` → IC=+0.322 (n=2065)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4303 (IC base=+0.310)

- **PATRÓN** `libro_liquidez` > `2570.5216` → IC=+0.310 (n=1433)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2570.5216 (IC base=+0.310)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.341 (n=1876)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.310)

- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.343 (n=1522)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.312)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.321 (n=1146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.312)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.313 (n=1123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.312)

- **PATRÓN** `ibs_20min` < `0.3784` → IC=+0.333 (n=2283)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3784 (IC base=+0.312)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.618` → IC=+0.328 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.618 (IC base=+0.312)

- **PATRÓN** `volumen_regimen` < `0.723` → IC=+0.317 (n=1005)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.723 (IC base=+0.312)

- **PATRÓN** `volumen_regimen` > `1.2138` → IC=+0.343 (n=761)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2138 (IC base=+0.312)

- **PATRÓN** `volumen_pendiente_norm` > `0.2833` → IC=+0.363 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2833 (IC base=+0.312)

- **PATRÓN** `volumen_spike_ratio` < `1.4124` → IC=+0.325 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4124 (IC base=+0.312)

- **PATRÓN** `volumen_spike_ratio` > `2.1367` → IC=+0.313 (n=954)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1367 (IC base=+0.312)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.220 (n=6723)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.0877` → IC=+0.199 (n=4940)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.0877 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=15352)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `0.5489` → IC=+0.233 (n=14819)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5489 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `0.1636` → IC=+0.207 (n=5850)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1636 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.234` → IC=+0.255 (n=3860)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.234 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `1.1856` → IC=+0.161 (n=9851)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1856 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` > `0.6234` → IC=+0.159 (n=9850)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6234 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2938` → IC=+0.207 (n=2151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2938 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `2.6062` → IC=+0.189 (n=4800)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6062 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.196 (n=13743)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 90.0 (IC base=+0.178)

- **PATRÓN** `sigma_h` < `0.0114` → IC=+0.186 (n=14373)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0114 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.0803` → IC=+0.225 (n=4791)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0803 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=5384)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.5158` → IC=+0.239 (n=14369)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5158 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.832` → IC=+0.195 (n=2314)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 9.832 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.622` → IC=+0.186 (n=12737)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 2.622 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `1.1823` → IC=+0.165 (n=10250)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1823 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.223 (n=2135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.645` → IC=+0.188 (n=4530)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.645 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.195 (n=13340)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 96.0 (IC base=+0.182)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.225 (n=821)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.1043` → IC=+0.258 (n=1083)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1043 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.235 (n=911)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.229 (n=1667)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.9353` → IC=+0.297 (n=1640)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9353 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.738` → IC=+0.330 (n=784)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.738 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.287 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `1.8357` → IC=+0.220 (n=1560)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8357 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `1.4343` → IC=+0.224 (n=2339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4343 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=2711)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.223)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.232 (n=1469)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.009` → IC=+0.254 (n=1948)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.009 (IC base=+0.253)

- **PATRÓN** `drift_60min` |x|≤ `0.096` → IC=+0.308 (n=857)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.096 (IC base=+0.253)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.259 (n=2009)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.253)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.255 (n=1782)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.253)

- **PATRÓN** `ibs_20min` < `0.4187` → IC=+0.271 (n=1945)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4187 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` < `0.1008` → IC=+0.258 (n=1710)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1008 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` > `0.3012` → IC=+0.280 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3012 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` < `2.2944` → IC=+0.262 (n=1630)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2944 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` > `2.7171` → IC=+0.257 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7171 (IC base=+0.253)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.256 (n=2226)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.253)

- **PATRÓN** `libro_liquidez` > `1482.952` → IC=+0.259 (n=1738)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1482.952 (IC base=+0.253)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.257 (n=881)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.253)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.203 (n=751)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.0652` → IC=+0.188 (n=748)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0652 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=2348)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.3038` → IC=+0.215 (n=2241)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3038 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1875` → IC=+0.215 (n=1180)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1875 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.085` → IC=+0.210 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.085 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `0.6938` → IC=+0.159 (n=988)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.6938 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `1.0613` → IC=+0.147 (n=1016)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 1.0613 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.186 (n=348)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.5094` → IC=+0.159 (n=969)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.5094 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.4794` → IC=+0.155 (n=734)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.4794 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `411.0` → IC=+0.150 (n=2168)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 411.0 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.175 (n=2369)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.006 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.2376` → IC=+0.174 (n=2083)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2376 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.185 (n=1130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 15.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.6184` → IC=+0.208 (n=2369)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6184 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.269` → IC=+0.183 (n=446)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 11.269 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.144` → IC=+0.153 (n=2059)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.144 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.2012` → IC=+0.161 (n=2368)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2012 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` < `0.0941` → IC=+0.152 (n=2043)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.0941 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.4845` → IC=+0.152 (n=2246)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4845 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `218.0` → IC=+0.188 (n=957)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 218.0 (IC base=+0.148)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.239 (n=1139)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.4031` → IC=+0.224 (n=2208)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4031 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.233 (n=916)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=1320)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.269` → IC=+0.307 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.269 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.212 (n=2170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.352` → IC=+0.235 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.352 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.7649` → IC=+0.212 (n=1075)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7649 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.7054` → IC=+0.227 (n=1107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7054 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.217 (n=3003)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `1915.305` → IC=+0.225 (n=1138)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1915.305 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.242 (n=1915)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.4239` → IC=+0.256 (n=1915)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4239 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.281 (n=827)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.027` → IC=+0.290 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.027 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.242` → IC=+0.282 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.242 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.3592` → IC=+0.289 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3592 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `1.7621` → IC=+0.236 (n=920)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7621 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.1738` → IC=+0.243 (n=1393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1738 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.238 (n=1115)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `1904.5592` → IC=+0.244 (n=986)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1904.5592 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.241 (n=1379)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.236)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.199 (n=1069)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.0787` → IC=+0.201 (n=808)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0787 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=2505)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.2846` → IC=+0.203 (n=2421)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2846 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.1419` → IC=+0.192 (n=1437)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1419 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.649` → IC=+0.194 (n=551)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 9.649 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.0211` → IC=+0.148 (n=2130)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.0211 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.2887` → IC=+0.180 (n=360)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2887 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.8297` → IC=+0.146 (n=1582)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.8297 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `2.5248` → IC=+0.157 (n=791)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.5248 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `6924.983` → IC=+0.196 (n=1098)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6924.983 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `133.0` → IC=+0.147 (n=2364)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 133.0 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.166 (n=2259)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0064 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.3967` → IC=+0.145 (n=2563)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3967 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=1219)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.6789` → IC=+0.187 (n=2563)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6789 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.519` → IC=+0.150 (n=621)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 9.519 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.8521` → IC=+0.156 (n=1709)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8521 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2993` → IC=+0.193 (n=386)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2993 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.811` → IC=+0.136 (n=1612)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.811 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `2.5483` → IC=+0.134 (n=806)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.5483 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `6239.7898` → IC=+0.184 (n=1162)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 6239.7898 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `111.0` → IC=+0.135 (n=2102)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 111.0 (IC base=+0.129)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.173 (n=1229)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0108 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=2766)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.48` → IC=+0.212 (n=2707)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.48 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.1944` → IC=+0.189 (n=1530)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1944 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.3` → IC=+0.288 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.3 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `1.1724` → IC=+0.134 (n=2706)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.1724 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.7045` → IC=+0.123 (n=2417)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.7045 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` < `0.1636` → IC=+0.131 (n=2764)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1636 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.5481` → IC=+0.139 (n=1157)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.5481 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.125 (n=2818)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2634.7685` → IC=+0.200 (n=1227)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2634.7685 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.144 (n=1118)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 21.0 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0114` → IC=+0.146 (n=2793)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0114 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.170 (n=930)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=2841)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.6296` → IC=+0.219 (n=2790)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6296 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.1983` → IC=+0.151 (n=2678)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1983 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.411` → IC=+0.138 (n=2461)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 2.411 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.1845` → IC=+0.129 (n=2791)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1845 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1651` → IC=+0.124 (n=2721)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1651 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2777` → IC=+0.139 (n=383)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.2777 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4407` → IC=+0.126 (n=874)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.4407 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `1.809` → IC=+0.125 (n=1745)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.809 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2511.9136` → IC=+0.183 (n=1265)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2511.9136 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.127 (n=2595)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 47.0 (IC base=+0.120)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.246 (n=2218)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.1691` → IC=+0.237 (n=1093)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1691 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.225 (n=2574)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2234)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.6606` → IC=+0.256 (n=2483)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6606 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` > `0.1821` → IC=+0.231 (n=1567)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1821 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.613` → IC=+0.252 (n=1121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.613 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `1.1691` → IC=+0.224 (n=2483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1691 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `0.6232` → IC=+0.231 (n=2483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6232 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.2849` → IC=+0.267 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2849 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `2.4631` → IC=+0.225 (n=2420)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4631 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `1.8078` → IC=+0.232 (n=1613)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8078 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.224 (n=3236)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `2082.425` → IC=+0.225 (n=2483)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2082.425 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0128` → IC=+0.239 (n=1114)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0128 (IC base=+0.236)

- **PATRÓN** `sigma_h` > `0.0227` → IC=+0.246 (n=1150)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0227 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.0884` → IC=+0.260 (n=844)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0884 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.252 (n=1234)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.240 (n=1138)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.4359` → IC=+0.263 (n=2532)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4359 (IC base=+0.236)

- **PATRÓN** `dist_vwap_pct` > `0.3042` → IC=+0.246 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3042 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.304` → IC=+0.271 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.304 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` > `1.042` → IC=+0.244 (n=1148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.042 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.288 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `2.5151` → IC=+0.234 (n=2371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5151 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `1.4348` → IC=+0.237 (n=2370)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4348 (IC base=+0.236)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.209 (n=1625)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.1316` → IC=+0.202 (n=1626)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1316 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.195 (n=3297)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 8.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `0.3409` → IC=+0.208 (n=3690)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3409 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.7982` → IC=+0.199 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7982 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.58` → IC=+0.209 (n=1590)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.58 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `0.8615` → IC=+0.196 (n=2216)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8615 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.0739` → IC=+0.185 (n=1490)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.0739 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` < `1.4308` → IC=+0.190 (n=1198)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.4308 (IC base=+0.176)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.181 (n=4152)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.02 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `8580.3325` → IC=+0.191 (n=1673)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 8580.3325 (IC base=+0.176)

- **PATRÓN** `ibs_20min` < `0.3926` → IC=+0.155 (n=2695)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.3926 (IC base=+0.079)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.121 (n=1710)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 26.0 (IC base=+0.079)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.208 (n=440)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.3269` → IC=+0.211 (n=992)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3269 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.221 (n=905)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `0.6435` → IC=+0.250 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6435 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` > `0.3086` → IC=+0.215 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3086 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.034` → IC=+0.209 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.034 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.269` → IC=+0.191 (n=1134)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 9.269 (IC base=+0.190)

- **PATRÓN** `volumen_regimen` < `0.8784` → IC=+0.211 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8784 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` < `0.1532` → IC=+0.193 (n=1041)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.1532 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.0712` → IC=+0.194 (n=400)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0712 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` < `2.1894` → IC=+0.204 (n=855)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1894 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `10454.9515` → IC=+0.195 (n=992)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 10454.9515 (IC base=+0.190)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.204 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 162.0 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.161 (n=544)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0033 (IC base=+0.083)

- **PATRÓN** `ibs_20min` < `0.6428` → IC=+0.136 (n=1087)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.6428 (IC base=+0.083)

- **PATRÓN** `ballena_activa_n` < `165.0` → IC=+0.165 (n=532)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 165.0 (IC base=+0.083)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.245 (n=515)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.191)

- **PATRÓN** `drift_60min` |x|≤ `0.127` → IC=+0.215 (n=513)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.127 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.209 (n=1213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `0.3538` → IC=+0.232 (n=1041)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3538 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` > `0.7904` → IC=+0.199 (n=184)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.7904 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` < `0.2068` → IC=+0.193 (n=1052)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.2068 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.859` → IC=+0.233 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.859 (IC base=+0.191)

- **PATRÓN** `volumen_regimen` < `1.0194` → IC=+0.203 (n=1026)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0194 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.27` → IC=+0.222 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.27 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` < `1.4277` → IC=+0.205 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4277 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `1.7865` → IC=+0.200 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7865 (IC base=+0.191)

- **PATRÓN** `ibs_20min` < `0.1034` → IC=+0.178 (n=386)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.1034 (IC base=+0.074)

- **PATRÓN** `libro_liquidez` > `8206.9846` → IC=+0.141 (n=524)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 8206.9846 (IC base=+0.074)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.7` → IC=-0.168 (n=344)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=1033)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.174 (n=308)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0112 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.186 (n=824)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.5172` → IC=+0.204 (n=923)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5172 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.9532` → IC=+0.223 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9532 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.072` → IC=+0.245 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.072 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `1.0562` → IC=+0.165 (n=812)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.0562 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` > `0.7057` → IC=+0.165 (n=824)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.7057 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.2298` → IC=+0.182 (n=171)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2298 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `1.4411` → IC=+0.179 (n=297)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.4411 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `2.1532` → IC=+0.155 (n=404)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.1532 (IC base=+0.155)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.163 (n=961)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.02 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `2762.3879` → IC=+0.186 (n=418)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2762.3879 (IC base=+0.155)

- **PATRÓN** `ibs_20min` < `0.5778` → IC=+0.126 (n=909)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.5778 (IC base=+0.042)

- **PATRÓN** `libro_liquidez` > `2589.9068` → IC=+0.143 (n=469)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 2589.9068 (IC base=+0.042)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0258` → IC=+0.163 (n=244)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0258 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.2705` → IC=+0.179 (n=163)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2705 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.220 (n=116)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.208 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.3149` → IC=+0.175 (n=124)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.3149 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.301` → IC=+0.181 (n=211)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 3.301 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `1.009` → IC=+0.162 (n=214)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.009 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` > `0.6829` → IC=+0.168 (n=218)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 0.6829 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.8264` → IC=+0.194 (n=145)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.8264 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `2.3975` → IC=+0.180 (n=73)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.3975 (IC base=+0.156)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.182 (n=287)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.03 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `2810.6023` → IC=+0.175 (n=81)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2810.6023 (IC base=+0.156)

- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.160 (n=248)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0129 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.159 (n=127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 15.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.3393` → IC=+0.144 (n=186)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.3393 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `1.209` → IC=+0.266 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.209 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.268` → IC=+0.171 (n=74)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 5.268 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `0.891` → IC=+0.149 (n=186)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.891 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.160 (n=51)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.537` → IC=+0.189 (n=88)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.537 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.7855` → IC=+0.144 (n=88)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.7855 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `1906.4868` → IC=+0.125 (n=278)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 1906.4868 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.140 (n=259)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 19.0 (IC base=+0.124)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.228 (n=6445)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=20122)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.4401` → IC=+0.229 (n=19327)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4401 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.8827` → IC=+0.210 (n=2332)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8827 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.14` → IC=+0.254 (n=4718)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.14 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.2184` → IC=+0.164 (n=12988)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2184 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2412` → IC=+0.206 (n=3489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2412 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6168` → IC=+0.193 (n=6280)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6168 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `107.0` → IC=+0.202 (n=17966)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 107.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.196 (n=7809)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0057 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.194 (n=5903)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0119 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.4855` → IC=+0.193 (n=17703)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.4855 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=6587)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` < `0.5902` → IC=+0.242 (n=17703)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5902 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.672` → IC=+0.204 (n=2425)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.672 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.481` → IC=+0.194 (n=17176)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 3.481 (IC base=+0.190)

- **PATRÓN** `volumen_regimen` < `1.0581` → IC=+0.165 (n=10504)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.0581 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.2922` → IC=+0.253 (n=2409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2922 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.6336` → IC=+0.201 (n=5619)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6336 (IC base=+0.190)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.222 (n=11141)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.190)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3586` → IC=+0.231 (n=3125)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3586 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.244 (n=1514)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.231)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.234 (n=2108)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` > `0.9703` → IC=+0.322 (n=1417)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9703 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.165` → IC=+0.347 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.165 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.2327` → IC=+0.290 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2327 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` < `1.4439` → IC=+0.231 (n=1004)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4439 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` > `2.2767` → IC=+0.238 (n=1366)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2767 (IC base=+0.231)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.248 (n=3399)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.231)

- **PATRÓN** `libro_liquidez` > `2042.6` → IC=+0.234 (n=1042)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2042.6 (IC base=+0.231)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.254 (n=1905)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.231)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.269 (n=2721)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.265)

- **PATRÓN** `drift_60min` |x|≤ `0.0871` → IC=+0.296 (n=907)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0871 (IC base=+0.265)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.271 (n=2496)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.265)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.266 (n=2473)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.265)

- **PATRÓN** `ibs_20min` < `0.5301` → IC=+0.287 (n=2721)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5301 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` < `0.0964` → IC=+0.267 (n=2464)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0964 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` > `0.289` → IC=+0.290 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.289 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` < `1.5607` → IC=+0.265 (n=1142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5607 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` > `2.6706` → IC=+0.275 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6706 (IC base=+0.265)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.266 (n=3116)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.265)

- **PATRÓN** `libro_liquidez` > `1751.3303` → IC=+0.271 (n=1814)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1751.3303 (IC base=+0.265)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.272 (n=1165)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.265)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.188 (n=1046)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0029 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.1047` → IC=+0.159 (n=1381)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1047 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.156 (n=3263)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.2254` → IC=+0.197 (n=3137)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.2254 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.3224` → IC=+0.200 (n=1079)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3224 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.765` → IC=+0.157 (n=949)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 6.765 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.176` → IC=+0.146 (n=2752)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 3.176 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.6317` → IC=+0.170 (n=1046)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.6317 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` > `1.0745` → IC=+0.148 (n=1422)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 1.0745 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2735` → IC=+0.186 (n=450)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2735 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.167` → IC=+0.152 (n=2706)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.167 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `1.5264` → IC=+0.150 (n=2748)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.5264 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `231.0` → IC=+0.173 (n=1011)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 231.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.162 (n=2709)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0059 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.0785` → IC=+0.185 (n=903)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.0785 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=994)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.6912` → IC=+0.191 (n=2709)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6912 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.02` → IC=+0.146 (n=445)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 11.02 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.366` → IC=+0.142 (n=2732)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 6.366 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.0502` → IC=+0.154 (n=2384)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.0502 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2183` → IC=+0.196 (n=504)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2183 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.4295` → IC=+0.145 (n=2603)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4295 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.7783` → IC=+0.146 (n=1735)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.7783 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=3515)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `234.0` → IC=+0.159 (n=842)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 234.0 (IC base=+0.140)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.252 (n=1073)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=3365)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=2881)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=1200)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.194` → IC=+0.326 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.194 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` < `0.1312` → IC=+0.227 (n=3027)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1312 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `1.6151` → IC=+0.229 (n=3135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6151 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.231 (n=3845)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `1356.8594` → IC=+0.230 (n=3216)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1356.8594 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.245 (n=2685)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0109 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.1796` → IC=+0.257 (n=1341)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1796 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.265 (n=1153)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.0485` → IC=+0.307 (n=1017)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0485 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.679` → IC=+0.298 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.679 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.3502` → IC=+0.304 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3502 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.154` → IC=+0.252 (n=1945)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.154 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.247 (n=1549)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1908.5984` → IC=+0.252 (n=1382)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1908.5984 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.249 (n=1926)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.241)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.194 (n=1116)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0035 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.1306` → IC=+0.167 (n=1468)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1306 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.154 (n=3459)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` > `0.9064` → IC=+0.275 (n=1112)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9064 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.1421` → IC=+0.167 (n=1723)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1421 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.028` → IC=+0.158 (n=1494)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.028 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `0.8596` → IC=+0.158 (n=2225)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8596 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.2333` → IC=+0.191 (n=590)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2333 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `1.5208` → IC=+0.160 (n=1434)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.5208 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `7345.5998` → IC=+0.237 (n=1112)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7345.5998 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.155 (n=1450)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 70.0 (IC base=+0.142)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.158 (n=2792)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0076 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4423` → IC=+0.145 (n=2789)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.4423 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.160 (n=1019)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.7229` → IC=+0.189 (n=2789)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.7229 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.207` → IC=+0.168 (n=555)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.207 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.157` → IC=+0.136 (n=2429)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 3.157 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6909` → IC=+0.152 (n=1227)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6909 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2956` → IC=+0.226 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2956 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.5381` → IC=+0.145 (n=2404)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.5381 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `6154.2761` → IC=+0.205 (n=930)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6154.2761 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.142 (n=1817)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 96.0 (IC base=+0.136)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.153 (n=1530)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0108 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.151 (n=2372)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.4348` → IC=+0.192 (n=3369)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.4348 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `1.0121` → IC=+0.206 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0121 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.522` → IC=+0.266 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.522 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `0.8789` → IC=+0.135 (n=2247)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8789 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.1636` → IC=+0.121 (n=3521)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1636 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `2.4932` → IC=+0.121 (n=3293)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_spike_ratio` < 2.4932 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.121 (n=3509)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2685.6288` → IC=+0.244 (n=1123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2685.6288 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.155 (n=2821)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0105 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1348` → IC=+0.154 (n=1069)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1348 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.154 (n=1503)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 15.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.210 (n=3224)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6667 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.18` → IC=+0.142 (n=3077)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.18 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.6385` → IC=+0.149 (n=1068)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.6385 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2256` → IC=+0.168 (n=558)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2256 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4386` → IC=+0.150 (n=1007)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4386 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2559.146` → IC=+0.197 (n=1068)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2559.146 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.135 (n=2662)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 44.0 (IC base=+0.120)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0138` → IC=+0.256 (n=2812)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0138 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.237 (n=3281)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.240 (n=2097)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` > `0.6129` → IC=+0.269 (n=2810)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6129 (IC base=+0.233)

- **PATRÓN** `dist_vwap_pct` > `0.1926` → IC=+0.249 (n=1662)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1926 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.319` → IC=+0.281 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.319 (IC base=+0.233)

- **PATRÓN** `volumen_regimen` < `1.2206` → IC=+0.237 (n=3145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2206 (IC base=+0.233)

- **PATRÓN** `volumen_regimen` > `0.6422` → IC=+0.238 (n=3145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6422 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.2361` → IC=+0.253 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2361 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.4826` → IC=+0.250 (n=1023)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4826 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.234 (n=4087)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `2077.2844` → IC=+0.233 (n=3145)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2077.2844 (IC base=+0.233)

- **PATRÓN** `sigma_h` > `0.0257` → IC=+0.260 (n=1080)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0257 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.243 (n=3044)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.52` → IC=+0.270 (n=3248)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.52 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.225` → IC=+0.277 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.225 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` > `1.22` → IC=+0.260 (n=1079)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.22 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2848` → IC=+0.300 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2848 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.8121` → IC=+0.236 (n=2022)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8121 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `1.4288` → IC=+0.239 (n=3033)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4288 (IC base=+0.238)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.235 (n=2955)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.238)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.199 (n=5573)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.246 (n=1920)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.5016` → IC=+0.224 (n=5728)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5016 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.231 (n=2084)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.9346` → IC=+0.255 (n=1911)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9346 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` < `0.4256` → IC=+0.219 (n=4162)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4256 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.873` → IC=+0.223 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.873 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.585` → IC=+0.216 (n=5099)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.585 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` < `0.7054` → IC=+0.227 (n=1862)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7054 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `0.8828` → IC=+0.218 (n=2821)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8828 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.217 (n=5347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.1655` → IC=+0.222 (n=1618)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1655 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `1.4526` → IC=+0.223 (n=1880)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4526 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.223 (n=4483)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `3710.1526` → IC=+0.226 (n=3819)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3710.1526 (IC base=+0.216)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.239 (n=1404)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.4928` → IC=+0.212 (n=4192)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4928 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=1417)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.212 (n=1867)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` < `0.7306` → IC=+0.205 (n=4192)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7306 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` > `0.6542` → IC=+0.210 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6542 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` < `0.238` → IC=+0.194 (n=3875)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.238 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.812` → IC=+0.207 (n=3748)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.812 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `1.0974` → IC=+0.203 (n=3514)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0974 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.199 (n=3856)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.2233` → IC=+0.202 (n=838)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2233 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `1.5371` → IC=+0.202 (n=1818)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5371 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `2.1921` → IC=+0.206 (n=1873)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1921 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.199 (n=5573)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.213 (n=1828)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.197)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.273 (n=792)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.264)

- **PATRÓN** `drift_60min` |x|≤ `0.1129` → IC=+0.289 (n=396)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1129 (IC base=+0.264)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.271 (n=950)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.264)

- **PATRÓN** `ibs_20min` < `0.2427` → IC=+0.286 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2427 (IC base=+0.264)

- **PATRÓN** `dist_vwap_pct` < `0.1966` → IC=+0.278 (n=834)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1966 (IC base=+0.264)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.122` → IC=+0.286 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.122 (IC base=+0.264)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.699` → IC=+0.265 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.699 (IC base=+0.264)

- **PATRÓN** `volumen_regimen` < `1.2212` → IC=+0.267 (n=898)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2212 (IC base=+0.264)

- **PATRÓN** `volumen_regimen` > `0.8676` → IC=+0.282 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8676 (IC base=+0.264)

- **PATRÓN** `volumen_pendiente_norm` > `0.2866` → IC=+0.343 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2866 (IC base=+0.264)

- **PATRÓN** `volumen_spike_ratio` < `2.4928` → IC=+0.269 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4928 (IC base=+0.264)

- **PATRÓN** `volumen_spike_ratio` > `2.1875` → IC=+0.265 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1875 (IC base=+0.264)

- **PATRÓN** `libro_liquidez` > `12817.5218` → IC=+0.274 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12817.5218 (IC base=+0.264)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.261 (n=499)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.3833` → IC=+0.196 (n=1486)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.3833 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.220 (n=544)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.191 (n=552)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 5.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.1373` → IC=+0.201 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1373 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `0.6887` → IC=+0.199 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6887 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.338` → IC=+0.204 (n=1457)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.338 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.642` → IC=+0.209 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.642 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.1518` → IC=+0.200 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1518 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `1.412` → IC=+0.199 (n=493)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.412 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.1667` → IC=+0.186 (n=670)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.1667 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `14600.5038` → IC=+0.188 (n=674)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 14600.5038 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `684.0` → IC=+0.194 (n=1440)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 684.0 (IC base=+0.182)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `drift_60min` |x|≤ `0.5868` → IC=+0.204 (n=855)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5868 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.238 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` < `0.7078` → IC=+0.196 (n=570)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.7078 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.240 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.492` → IC=+0.239 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.492 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.2085` → IC=+0.237 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2085 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `1.8234` → IC=+0.204 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8234 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `2758.665` → IC=+0.221 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2758.665 (IC base=+0.195)

- **PATRÓN** `ballena_activa_n` < `5.0` → IC=+0.197 (n=377)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 5.0 (IC base=+0.195)

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
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.226 (n=290)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.226 (n=589)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.273 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` > `0.7235` → IC=+0.237 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7235 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.252` → IC=+0.219 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.252 (IC base=+0.191)

- **PATRÓN** `volumen_regimen` < `0.6342` → IC=+0.236 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6342 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` < `0.1064` → IC=+0.203 (n=778)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1064 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` < `2.1715` → IC=+0.197 (n=743)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.1715 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `1.478` → IC=+0.197 (n=844)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.478 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.199 (n=1024)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.02 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `4246.9516` → IC=+0.236 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4246.9516 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.0128` → IC=+0.216 (n=638)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0128 (IC base=+0.215)

- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.216 (n=290)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.5998` → IC=+0.236 (n=638)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5998 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.247 (n=448)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.7341` → IC=+0.241 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7341 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `0.5012` → IC=+0.226 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5012 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.917` → IC=+0.218 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.917 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.825` → IC=+0.223 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.825 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` < `1.1185` → IC=+0.214 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1185 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `0.6722` → IC=+0.216 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6722 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` < `0.1067` → IC=+0.229 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1067 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `2.2044` → IC=+0.256 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2044 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `2953.4632` → IC=+0.230 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2953.4632 (IC base=+0.215)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.241 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.215)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.154 (n=645)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0036 (IC base=+0.061)

- **PATRÓN** `ibs_20min` > `0.7601` → IC=+0.198 (n=1228)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.7601 (IC base=+0.061)

- **PATRÓN** `dist_vwap_pct` > `0.1464` → IC=+0.143 (n=942)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.1464 (IC base=+0.061)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.771` → IC=+0.146 (n=405)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 10.771 (IC base=+0.061)

- **PATRÓN** `ibs_20min` < `0.0431` → IC=+0.262 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0431 (IC base=+0.048)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.872` → IC=+0.170 (n=183)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.872 (IC base=+0.048)

- **PATRÓN** `volumen_pendiente_norm` > `0.1457` → IC=+0.147 (n=324)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.1457 (IC base=+0.048)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.3609` → IC=-0.155 (n=198)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3609
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=597)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.129 (n=628)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0057 (IC base=+0.081)

- **PATRÓN** `ibs_20min` > `0.3609` → IC=+0.161 (n=597)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.3609 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.172 (n=297)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.081)

- **PATRÓN** `ibs_20min` < `0.0617` → IC=+0.285 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0617 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` > `0.2162` → IC=+0.180 (n=95)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2162 (IC base=+0.058)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.134 (n=424)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.005 (IC base=+0.082)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.137 (n=309)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 15.0 (IC base=+0.082)

- **PATRÓN** `ibs_20min` > `0.5505` → IC=+0.181 (n=537)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.5505 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` > `0.1265` → IC=+0.185 (n=300)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1265 (IC base=+0.082)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.957` → IC=+0.207 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.957 (IC base=+0.082)

- **PATRÓN** `ibs_20min` < `0.0289` → IC=+0.256 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0289 (IC base=+0.016)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.686` → IC=+0.219 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.686 (IC base=+0.016)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.7273` → IC=+0.142 (n=431)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.7273 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.7051` → IC=+0.136 (n=149)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.7051 (IC base=+0.024)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.903` → IC=+0.138 (n=136)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 8.903 (IC base=+0.024)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.154 (n=287)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0105 (IC base=+0.071)

- **PATRÓN** `ibs_20min` < `0.0882` → IC=+0.255 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0882 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` < `0.1816` → IC=+0.136 (n=281)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1816 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.114` → IC=+0.357 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.114 (IC base=+0.071)

- **PATRÓN** `volumen_regimen` > `1.1045` → IC=+0.183 (n=99)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 1.1045 (IC base=+0.071)

- **PATRÓN** `volumen_pendiente_norm` > `0.152` → IC=+0.185 (n=90)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.152 (IC base=+0.071)

- **PATRÓN** `volumen_spike_ratio` > `1.5314` → IC=+0.147 (n=242)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.5314 (IC base=+0.071)

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

- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.209 (n=201)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.201 (n=229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` > `0.6686` → IC=+0.172 (n=602)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.6686 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` > `0.5397` → IC=+0.254 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5397 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.608` → IC=+0.136 (n=330)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 3.608 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.636` → IC=+0.138 (n=443)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 2.636 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `0.6221` → IC=+0.180 (n=201)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6221 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` < `0.1492` → IC=+0.167 (n=508)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.1492 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `1.3996` → IC=+0.191 (n=166)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.3996 (IC base=+0.132)

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

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.299 (n=157)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.269 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6842 (IC base=+0.233)

- **PATRÓN** `dist_vwap_pct` > `0.6827` → IC=+0.382 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6827 (IC base=+0.233)

- **PATRÓN** `dist_vwap_pct` < `0.2453` → IC=+0.233 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2453 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.006` → IC=+0.341 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.006 (IC base=+0.233)

- **PATRÓN** `volumen_regimen` < `0.7968` → IC=+0.273 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7968 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.0951` → IC=+0.287 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0951 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.4814` → IC=+0.340 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4814 (IC base=+0.233)

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
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=217)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=217)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=493)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=3774)

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
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=1494)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=1448)

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
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=900)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=900)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.132 (n=275)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=705)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1014)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1014)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=237)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=237)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.130 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=181)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.191 (n=53)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=297)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=335)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=278)

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
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=291)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `restante_min` < `10.72` → IC=-0.167 (n=28)

  - _Acción_: SKIP cuando `restante_min` < 10.72
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=58)

- **FILTRO** `lag_apertura_s` > `255.1` → IC=-0.145 (n=29)

  - _Acción_: SKIP cuando `lag_apertura_s` > 255.1
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=57)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.192 (n=63)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=71)

- **FILTRO** `hora_utc` > `14.0` → IC=-0.198 (n=61)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=73)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.250 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=48)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.51` → IC=+0.149 (n=257)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.51 (IC base=+0.001)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` > `0.61` → IC=-0.130 (n=44)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=172)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.150 (n=135)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=284)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.124 (n=139)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=536)

- **FILTRO** `profundidad_ratio` < `43.4` → IC=-0.135 (n=168)

  - _Acción_: SKIP cuando `profundidad_ratio` < 43.4
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=507)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.196 (n=110)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=446)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` > `0.58` → IC=-0.125 (n=262)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=320)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.169 (n=122)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=503)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` > `0.61` → IC=-0.132 (n=93)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=294)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.156 (n=248)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=517)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.174 (n=6737)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=21772)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.177 (n=7126)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=22213)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.190 (n=1280)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=3967)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.176 (n=1216)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=4000)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.140 (n=1377)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 1.0 (IC base=+0.041)

- **PATRÓN** `libro_liquidez` > `1040.2746` → IC=+0.140 (n=2624)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 1040.2746 (IC base=+0.041)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.131 (n=2454)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.5 (IC base=+0.013)

- **PATRÓN** `libro_liquidez` > `1148.885` → IC=+0.150 (n=1775)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1148.885 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.183 (n=1016)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3140)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.205 (n=1275)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=4063)

- **PATRÓN** `ibs_20min` > `0.9645` → IC=+0.129 (n=1785)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` > 0.9645 (IC base=+0.035)

- **PATRÓN** `libro_liquidez` > `1731.3732` → IC=+0.121 (n=1785)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1731.3732 (IC base=+0.035)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.155 (n=1294)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=3953)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2416)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=2340)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.188 (n=922)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=2871)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=3772)

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
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=952)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.196 (n=366)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=715)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.132 (n=19624)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=43628)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.297 (n=14819)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=48433)

- **FILTRO** `ibs_7min` < `0.2264` → IC=-0.231 (n=15813)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2264
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=47439)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.152 (n=21266)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=41986)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.243 (n=19694)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=59821)

- **FILTRO** `ibs_7min` > `0.2827` → IC=-0.181 (n=19878)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2827
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=59637)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.154 (n=2774)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=8395)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.317 (n=2720)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=8449)

- **FILTRO** `ibs_7min` < `0.7113` → IC=-0.249 (n=3685)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7113
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=7484)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.150 (n=2631)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=8538)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.277 (n=3285)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=10441)

- **FILTRO** `ibs_7min` > `0.7722` → IC=-0.215 (n=3429)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7722
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=10297)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.261 (n=2523)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=8072)

- **FILTRO** `ibs_7min` < `0.7175` → IC=-0.203 (n=2648)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7175
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=7947)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.194 (n=2636)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=7959)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.259 (n=2695)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=8136)

- **FILTRO** `ibs_7min` > `0.2646` → IC=-0.191 (n=2707)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2646
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=8124)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.179 (n=2690)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=8141)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.162 (n=2617)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=8023)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.312 (n=2646)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=7994)

- **FILTRO** `ibs_7min` < `0.2886` → IC=-0.247 (n=3511)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2886
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=7129)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.196 (n=2315)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=8325)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.260 (n=3465)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=11107)

- **FILTRO** `ibs_7min` > `0.7298` → IC=-0.181 (n=3642)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7298
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=10930)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=2485)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=7784)

- **FILTRO** `ibs_7min` < `0.72` → IC=-0.194 (n=2566)

  - _Acción_: SKIP cuando `ibs_7min` < 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=7703)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.189 (n=2497)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=7772)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.260 (n=2449)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=8253)

- **FILTRO** `ibs_7min` > `0.2747` → IC=-0.173 (n=2675)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2747
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=8027)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.175 (n=2604)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=8098)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=2545)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=7713)

- **FILTRO** `ibs_7min` < `0.7097` → IC=-0.225 (n=3383)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7097
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=6875)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.221 (n=2410)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=7848)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.194 (n=3626)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=11729)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.299 (n=2561)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=7760)

- **FILTRO** `ibs_7min` < `0.1818` → IC=-0.231 (n=2579)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1818
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=7742)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.203 (n=2435)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=7886)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.225 (n=3558)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=10771)

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
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=869)

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
- **PATRÓN** `delta_ratio` |x|> `0.3983` → IC=+0.136 (n=1315)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.3983 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.128 (n=1203)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 14.0 (IC base=+0.126)

- **PATRÓN** `total_vol_5m` < `4211.332` → IC=+0.143 (n=877)

  - _Acción_: Kelly boost +0.71€ cuando `total_vol_5m` < 4211.332 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `3448.6944` → IC=+0.144 (n=597)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 3448.6944 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.126 (n=452)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 10.0 (IC base=+0.126)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.173 (n=148)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 14.0 (IC base=+0.125)

- **PATRÓN** `total_vol_5m` < `285.121` → IC=+0.147 (n=205)

  - _Acción_: Kelly boost +0.74€ cuando `total_vol_5m` < 285.121 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2520.4138` → IC=+0.214 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2520.4138 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.122 (n=141)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 7.0 (IC base=+0.125)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.4378` → IC=+0.135 (n=94)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.4378 (IC base=+0.111)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.133 (n=246)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 14.0 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2304.5801` → IC=+0.138 (n=183)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2304.5801 (IC base=+0.111)

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
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.177 (n=230)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.196 (n=110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 6.0 (IC base=+0.153)

- **PATRÓN** `total_vol_5m` < `4901.52` → IC=+0.199 (n=154)

  - _Acción_: Kelly boost +0.99€ cuando `total_vol_5m` < 4901.52 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `3106.4902` → IC=+0.178 (n=206)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 3106.4902 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.160 (n=101)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 28.0 (IC base=+0.153)

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

- **FILTRO** `sigma_h` < `0.0087` → IC=-0.291 (n=41)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0087
  - _Potencial_: sin este filtro IC_bueno=-0.216 (n=86)

- **FILTRO** `pct_vs_K` |x|> `3.2571` → IC=-0.432 (n=42)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.2571
  - _Potencial_: sin este filtro IC_bueno=-0.144 (n=85)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=353)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=422)

- **PATRÓN** `streak_estiramiento` < `0.2952` → IC=+0.148 (n=89)

  - _Acción_: Kelly boost +0.74€ cuando `streak_estiramiento` < 0.2952 (IC base=+0.013)

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
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=113)

- **PATRÓN** `streak_estiramiento` < `0.2356` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `streak_estiramiento` < 0.2356 (IC base=+0.013)

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
- **PATRÓN** `volumen_racha` < `17126.646` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_racha` < 17126.646 (IC base=+0.051)

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
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=4374)

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
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=2499)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.189 (n=1800)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0055 (IC base=+0.165)

- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.175 (n=1363)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0125 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.1794` → IC=+0.183 (n=3598)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.1794 (IC base=+0.165)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0986` → IC=+0.175 (n=1249)

  - _Acción_: Kelly boost +0.87€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0986 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.172 (n=3765)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.165)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.167 (n=3785)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 15.0 (IC base=+0.165)

- **PATRÓN** `ibs_15` > `0.5328` → IC=+0.238 (n=4087)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5328 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.1301` → IC=+0.161 (n=1997)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.1301 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` < `0.3187` → IC=+0.151 (n=3311)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.3187 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.103` → IC=+0.263 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.103 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `4551.8044` → IC=+0.182 (n=1363)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 4551.8044 (IC base=+0.165)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1670)

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
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.160 (n=839)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0068 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.1091` → IC=+0.160 (n=560)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1091 (IC base=+0.141)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1412` → IC=+0.149 (n=559)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio_macro` |x|> 0.1412 (IC base=+0.141)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1229` → IC=+0.151 (n=336)

  - _Acción_: Kelly boost +0.75€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1229 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.149 (n=764)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 6.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.146 (n=879)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 17.0 (IC base=+0.141)

- **PATRÓN** `ibs_15` > `0.622` → IC=+0.258 (n=751)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.622 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.1202` → IC=+0.158 (n=516)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1202 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.285` → IC=+0.285 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.285 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `5753.161` → IC=+0.168 (n=381)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 5753.161 (IC base=+0.141)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8788` → IC=+0.234 (n=336)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8788 (IC base=+0.079)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=523)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.079)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0193` → IC=+0.192 (n=602)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0193 (IC base=+0.192)

- **PATRÓN** `sigma_h` > `0.0242` → IC=+0.226 (n=301)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0242 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.0876` → IC=+0.225 (n=398)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0876 (IC base=+0.192)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.093` → IC=+0.248 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.093 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.203 (n=810)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.192)

- **PATRÓN** `ibs_15` > `0.5143` → IC=+0.271 (n=902)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5143 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` > `0.1302` → IC=+0.210 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1302 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.497` → IC=+0.231 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.497 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.196 (n=616)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.02 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `2947.677` → IC=+0.292 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2947.677 (IC base=+0.192)

- **PATRÓN** `ibs_15` < `0.1071` → IC=+0.171 (n=812)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.85€ cuando `ibs_15` < 0.1071 (IC base=+0.070)

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
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.177 (n=2315)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=2317)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.214 (n=1814)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=2818)

- **FILTRO** `libro_liquidez` < `4281.527` → IC=-0.155 (n=3057)

  - _Acción_: SKIP cuando `libro_liquidez` < 4281.527
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=1575)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.138` → IC=+0.219 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.138 (IC base=-0.068)

- **PATRÓN** `ibs_15` > `0.6335` → IC=+0.281 (n=1119)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6335 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1113` → IC=+0.207 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1113 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` < `0.266` → IC=+0.200 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.266 (IC base=-0.068)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2307` → IC=+0.272 (n=1351)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2307 (IC base=-0.010)

- **PATRÓN** `ibs_15` < `0.3703` → IC=+0.282 (n=4054)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3703 (IC base=-0.010)

- **PATRÓN** `dist_vwap_pct` > `0.6596` → IC=+0.272 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6596 (IC base=-0.010)

- **PATRÓN** `dist_vwap_pct` < `0.1669` → IC=+0.246 (n=3047)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1669 (IC base=-0.010)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0335` → IC=-0.224 (n=2192)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0335
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=733)

- **FILTRO** `sigma_h` < `0.0036` → IC=-0.222 (n=731)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0036
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=2194)

- **FILTRO** `sigma_ewma_delta_pct` > `23.14` → IC=-0.267 (n=419)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.14
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=2506)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.153 (n=283)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0029 (IC base=+0.086)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1441` → IC=+0.271 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1441 (IC base=+0.086)

- **PATRÓN** `ibs_15` > `0.7639` → IC=+0.330 (n=381)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7639 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.1051` → IC=+0.283 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1051 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` < `0.3659` → IC=+0.286 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3659 (IC base=+0.086)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.055` → IC=+0.148 (n=248)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 19.055 (IC base=+0.086)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0674` → IC=+0.246 (n=69)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0674 (IC base=-0.191)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1389` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1389 (IC base=-0.191)

- **PATRÓN** `ibs_15` < `0.6221` → IC=+0.317 (n=69)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6221 (IC base=-0.191)

- **PATRÓN** `dist_vwap_pct` < `0.0415` → IC=+0.325 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0415 (IC base=-0.191)

- **PATRÓN** `ballena_activa_n` < `291.0` → IC=+0.378 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 291.0 (IC base=-0.191)

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

- **PATRÓN** `sigma_h` < `0.0079` → IC=+0.251 (n=1564)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0079 (IC base=+0.244)

- **PATRÓN** `drift_15min` |x|≤ `0.774` → IC=+0.256 (n=1377)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.774 (IC base=+0.244)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2143` → IC=+0.272 (n=709)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2143 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=577)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.247 (n=1063)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.244)

- **PATRÓN** `ibs_15` < `0.3774` → IC=+0.275 (n=1565)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3774 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` > `0.6208` → IC=+0.264 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6208 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.399` → IC=+0.252 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.399 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.448` → IC=+0.248 (n=1634)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.448 (IC base=+0.244)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1724` → IC=-0.247 (n=362)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1724
  - _Potencial_: sin este filtro IC_bueno=-0.161 (n=705)

- **FILTRO** `drift_15min` |x|> `0.89` → IC=-0.284 (n=266)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.89
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=801)

- **FILTRO** `sigma_ewma_delta_pct` > `6.65` → IC=-0.208 (n=245)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.65
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=822)

- **FILTRO** `sigma_ewma_delta_pct` > `17.556` → IC=-0.141 (n=564)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.556
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=4526)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.190)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.190)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.190)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=-0.190)

- **PATRÓN** `ibs_15` < `0.4074` → IC=+0.289 (n=700)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.4074 (IC base=-0.035)

- **PATRÓN** `dist_vwap_pct` < `0.4441` → IC=+0.231 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4441 (IC base=-0.035)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0587` → IC=-0.225 (n=947)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0587
  - _Potencial_: sin este filtro IC_bueno=-0.165 (n=317)

- **FILTRO** `drift_60min` |x|> `0.1514` → IC=-0.222 (n=315)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1514
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=949)

- **FILTRO** `drift_15min` |x|> `0.7503` → IC=-0.247 (n=631)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.7503
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=633)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=1245)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.210)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.210)

- **PATRÓN** `delta_ratio_macro` |x|> `0.07` → IC=+0.275 (n=823)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.07 (IC base=-0.024)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1169` → IC=+0.290 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1169 (IC base=-0.024)

- **PATRÓN** `ibs_15` < `0.137` → IC=+0.313 (n=614)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.137 (IC base=-0.024)

- **PATRÓN** `dist_vwap_pct` > `0.7785` → IC=+0.347 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7785 (IC base=-0.024)

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

- **PATRÓN** `dist_vwap_pct` > `0.1533` → IC=+0.130 (n=71)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 0.1533 (IC base=+0.055)

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

- **PATRÓN** `dist_vwap_pct` > `0.1533` → IC=+0.130 (n=71)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 0.1533 (IC base=+0.055)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5328 sube el IC de +0.165 a +0.238 en UPDOWN_GBM#15min (n=4087). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7223 sube el IC de +0.206 a +0.277 en UPDOWN_GBM#BTC#15min (n=696). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.622 sube el IC de +0.141 a +0.258 en UPDOWN_GBM#ETH#15min (n=751). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.8788 sube el IC de +0.079 a +0.234 en UPDOWN_GBM#SOL#15min (n=336). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5143 sube el IC de +0.192 a +0.271 en UPDOWN_GBM#XRP#15min (n=902). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1071 sube el IC de +0.070 a +0.171 en UPDOWN_GBM#XRP#15min (n=812). Ya aplicado como kelly_boost=+0.85€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6335 sube el IC de -0.068 a +0.281 en UPDOWN_GBM_15M_TARDIO (n=1119). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3703 sube el IC de -0.010 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=4054). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7639 sube el IC de +0.086 a +0.330 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=381). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6221 sube el IC de -0.191 a +0.317 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=69). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5874 sube el IC de +0.153 a +0.247 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=556). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3774 sube el IC de +0.244 a +0.275 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1565). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.190 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.4074 sube el IC de -0.035 a +0.289 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=700). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.210 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.137 sube el IC de -0.024 a +0.313 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=614). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.103 a +0.364 en UPDOWN_GBM_ETH_15M_HORA7 (n=20). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.103 a +0.364 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=20). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8393 sube el IC de +0.286 a +0.317 en UPDOWN_GBM_IBS_ALTO (n=1213). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.280 a +0.306 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=647). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8516 sube el IC de +0.293 a +0.324 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=567). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7883 sube el IC de +0.365 a +0.398 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=693). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.9198 sube el IC de +0.361 a +0.406 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=233). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7604 sube el IC de +0.367 a +0.405 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=344). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2069 | +0.087 | +216.65€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2069 | +0.087 | +216.65€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1671 | +0.089 | +182.97€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1671 | +0.089 | +182.97€ | 0 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 284 | +0.070 | +11.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 284 | +0.070 | +11.30€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 83 | +0.123 | +22.71€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 83 | +0.123 | +22.71€ | 1 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 885 | -0.015 | +90.69€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 885 | -0.015 | +90.69€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 683 | -0.039 | +61.68€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 683 | -0.039 | +61.68€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 150 | +0.086 | +25.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 150 | +0.086 | +25.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 46 | +0.000 | +1.55€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 46 | +0.000 | +1.55€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 43604 | -0.083 | -5577.41€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2577 | +0.060 | -285.29€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 41027 | -0.092 | -5292.12€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4611 | -0.117 | -763.35€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4611 | -0.117 | -763.35€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2577 | +0.060 | -285.29€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2577 | +0.060 | -285.29€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4593 | -0.116 | -894.88€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4593 | -0.116 | -894.88€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 11692 | -0.023 | -1151.78€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 11692 | -0.023 | -1151.78€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 11743 | -0.117 | -1096.95€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 11743 | -0.117 | -1096.95€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8388 | -0.126 | -1385.16€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8388 | -0.126 | -1385.16€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 41548 | -0.013 | +3153.80€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 10713 | +0.005 | +1623.79€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 30835 | -0.019 | +1530.01€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 41548 | -0.013 | +3153.80€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 10713 | +0.005 | +1623.79€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 30835 | -0.019 | +1530.01€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 165054 | +0.114 | -6774.83€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 20217 | +0.180 | -688.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 741 | -0.005 | -76.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 134433 | +0.106 | -5673.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 9663 | +0.094 | -335.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 22276 | +0.106 | -1422.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 67 | -0.181 | +5.90€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 22194 | +0.107 | -1416.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 31644 | +0.125 | -539.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5456 | +0.181 | -224.29€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 22266 | +0.120 | -172.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3880 | +0.079 | -120.04€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 22331 | +0.099 | -1584.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 82 | -0.119 | -3.25€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 22234 | +0.100 | -1570.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 35174 | +0.123 | -722.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 8996 | +0.176 | -209.51€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 22597 | +0.106 | -455.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3569 | +0.101 | -48.96€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 31326 | +0.113 | -1498.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5539 | +0.197 | -265.76€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 644 | +0.025 | -22.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 22929 | +0.095 | -1042.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2214 | +0.110 | -166.70€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#XRP | 22303 | +0.106 | -1008.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 77 | -0.108 | +7.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 22213 | +0.107 | -1015.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 26647 | +0.194 | -1733.79€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 26647 | +0.194 | -1733.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 6031 | +0.177 | -540.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 6031 | +0.177 | -540.76€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 3617 | +0.200 | -108.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 3617 | +0.200 | -108.08€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 5963 | +0.176 | -508.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 5963 | +0.176 | -508.95€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5089 | +0.247 | -188.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5089 | +0.247 | -188.36€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 5868 | +0.185 | -401.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 5868 | +0.185 | -401.40€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 93608 | +0.201 | -6762.92€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 93608 | +0.201 | -6762.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 16118 | +0.183 | -1719.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 16118 | +0.183 | -1719.69€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 15093 | +0.225 | -502.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 15093 | +0.225 | -502.52€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 16057 | +0.181 | -1687.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 16057 | +0.181 | -1687.46€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 15224 | +0.218 | -614.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 15224 | +0.218 | -614.44€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 15517 | +0.202 | -1004.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 15517 | +0.202 | -1004.10€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 15599 | +0.197 | -1234.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 15599 | +0.197 | -1234.71€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 35909 | +0.117 | +293.79€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 35909 | +0.117 | +293.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 17862 | +0.118 | +200.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 17862 | +0.118 | +200.05€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 18047 | +0.115 | +93.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 18047 | +0.115 | +93.74€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2300 | +0.294 | +1.63€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2300 | +0.294 | +1.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1055 | +0.281 | -23.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1055 | +0.281 | -23.63€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1117 | +0.301 | +22.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1117 | +0.301 | +22.39€ | 0 | 5 |
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
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1808 | +0.069 | -76.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 713 | +0.045 | -64.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1095 | +0.084 | -11.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1381 | +0.077 | -32.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 286 | +0.049 | -21.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1095 | +0.084 | -11.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 345 | +0.027 | -46.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 345 | +0.027 | -46.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 71947 | +0.101 | -1739.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 5797 | +0.093 | +90.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 66150 | +0.101 | -1830.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 39430 | +0.105 | -406.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 5797 | +0.093 | +90.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 33633 | +0.108 | -497.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 15057 | +0.109 | -77.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 15057 | +0.109 | -77.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 17460 | +0.082 | -1256.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 17460 | +0.082 | -1256.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 904 | +0.189 | -110.96€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 904 | +0.189 | -110.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 904 | +0.189 | -110.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 904 | +0.189 | -110.96€ | 2 | 4 |
| ✅ GBM_LATE_15M | 49100 | +0.097 | +26764.76€ | 0 | 18 |
| ✅ GBM_LATE_15M#15min | 49100 | +0.097 | +26764.76€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 8160 | +0.222 | +6913.05€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 8160 | +0.222 | +6913.05€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 7508 | +0.177 | +5842.98€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 7508 | +0.177 | +5842.98€ | 0 | 22 |
| ✅ GBM_LATE_15M#DOGE | 8796 | +0.205 | +6837.25€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 8796 | +0.205 | +6837.25€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 6720 | +0.050 | +2008.21€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 6720 | +0.050 | +2008.21€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 6859 | -0.032 | +1730.02€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 6859 | -0.032 | +1730.02€ | 4 | 15 |
| ✅ GBM_LATE_15M#XRP | 11057 | -0.027 | +3433.26€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 11057 | -0.027 | +3433.26€ | 4 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 52239 | +0.085 | +29528.70€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 52239 | +0.085 | +29528.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 10104 | +0.001 | +5226.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 10104 | +0.001 | +5226.57€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 11214 | +0.008 | +2867.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 11214 | +0.008 | +2867.38€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 7151 | +0.286 | +7905.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 7151 | +0.286 | +7905.68€ | 0 | 23 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 9705 | +0.014 | +2884.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 9705 | +0.014 | +2884.49€ | 1 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 8156 | +0.041 | +3514.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 8156 | +0.041 | +3514.59€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5909 | +0.311 | +7129.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5909 | +0.311 | +7129.99€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 38915 | +0.180 | +31927.36€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 38915 | +0.180 | +31927.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 5873 | +0.236 | +5382.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 5873 | +0.236 | +5382.23€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 6144 | +0.147 | +4617.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 6144 | +0.147 | +4617.04€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 6245 | +0.223 | +5366.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 6245 | +0.223 | +5366.41€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 6643 | +0.135 | +5178.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 6643 | +0.135 | +5178.58€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 7326 | +0.122 | +5430.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 7326 | +0.122 | +5430.76€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 6684 | +0.230 | +5952.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 6684 | +0.230 | +5952.34€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 10308 | +0.125 | +4995.19€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 10308 | +0.125 | +4995.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 456 | +0.159 | +291.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 456 | +0.159 | +291.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2968 | +0.131 | +1622.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2968 | +0.131 | +1622.08€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 491 | +0.153 | +259.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 491 | +0.153 | +259.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3093 | +0.133 | +1498.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3093 | +0.133 | +1498.76€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2606 | +0.095 | +983.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2606 | +0.095 | +983.98€ | 1 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 694 | +0.139 | +339.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 694 | +0.139 | +339.32€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO | 49372 | +0.186 | +40002.61€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#15min | 49372 | +0.186 | +40002.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 7793 | +0.247 | +7429.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 7793 | +0.247 | +7429.05€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 7793 | +0.143 | +5434.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 7793 | +0.143 | +5434.12€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 8350 | +0.233 | +7452.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 8350 | +0.233 | +7452.72€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 8166 | +0.139 | +5893.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 8166 | +0.139 | +5893.62€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 8761 | +0.119 | +6085.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 8761 | +0.119 | +6085.07€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 8509 | +0.235 | +7708.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 8509 | +0.235 | +7708.04€ | 0 | 21 |
| ✅ GBM_LATE_5M | 13225 | +0.208 | +10622.01€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 13225 | +0.208 | +10622.01€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1039 | +0.245 | +982.84€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1039 | +0.245 | +982.84€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3177 | +0.213 | +2762.03€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3177 | +0.213 | +2762.03€ | 0 | 26 |
| ✅ GBM_LATE_5M#DOGE | 1218 | +0.198 | +909.95€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1218 | +0.198 | +909.95€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 3829 | +0.200 | +2830.96€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3829 | +0.200 | +2830.96€ | 0 | 26 |
| ✅ GBM_LATE_5M#SOL | 2009 | +0.201 | +1606.75€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2009 | +0.201 | +1606.75€ | 0 | 25 |
| ✅ GBM_LATE_5M#XRP | 1953 | +0.209 | +1529.48€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1953 | +0.209 | +1529.48€ | 0 | 0 |
| ✅ GBM_LATE_60M | 4210 | +0.056 | +1213.02€ | 0 | 7 |
| ✅ GBM_LATE_60M#60min | 4210 | +0.056 | +1213.02€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1510 | +0.071 | +495.09€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1510 | +0.071 | +495.09€ | 1 | 5 |
| ✅ GBM_LATE_60M#ETH | 1367 | +0.057 | +424.39€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1367 | +0.057 | +424.39€ | 0 | 7 |
| ✅ GBM_LATE_60M#SOL | 1333 | +0.039 | +293.53€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1333 | +0.039 | +293.53€ | 0 | 10 |
| 🚫 GBM_LATE_60M_FADE | 639 | -0.250 | -31.17€ | 9 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 639 | -0.250 | -31.17€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 239 | -0.247 | -16.76€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 239 | -0.247 | -16.76€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 230 | -0.246 | -6.48€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 230 | -0.246 | -6.48€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 170 | -0.256 | -7.92€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 170 | -0.256 | -7.92€ | 6 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1724 | +0.082 | +422.68€ | 1 | 12 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1724 | +0.082 | +422.68€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 671 | +0.078 | +161.08€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 671 | +0.078 | +161.08€ | 1 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 599 | +0.054 | +92.58€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 599 | +0.054 | +92.58€ | 2 | 13 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 454 | +0.125 | +169.02€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 454 | +0.125 | +169.02€ | 2 | 9 |
| ✅ LATE_WINDOW_5MIN | 192 | +0.278 | +203.97€ | 1 | 13 |
| ✅ LATE_WINDOW_5MIN#5min | 192 | +0.278 | +203.97€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 192 | +0.278 | +203.97€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 192 | +0.278 | +203.97€ | 1 | 13 |
| ✅ LEADLAG_BTC_XRP_15M | 3890 | +0.101 | +929.83€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3890 | +0.101 | +929.83€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3890 | +0.101 | +929.83€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3890 | +0.101 | +929.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 747 | -0.013 | +9.06€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 747 | -0.013 | +9.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 7 | -0.058 | -1.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 7 | -0.058 | -1.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 221 | -0.007 | +5.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 221 | -0.007 | +5.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 27 | -0.155 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 27 | -0.155 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 195 | +0.038 | +17.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 195 | +0.038 | +17.32€ | 2 | 3 |
| ✅ LIQUIDACIONES_15M#SOL | 245 | -0.002 | +2.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 245 | -0.002 | +2.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 3997 | +0.017 | +103.96€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3997 | +0.017 | +103.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 188 | +0.032 | -0.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 188 | +0.032 | -0.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 815 | +0.015 | +40.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 815 | +0.015 | +40.20€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 216 | +0.000 | +1.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 216 | +0.000 | +1.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1546 | +0.022 | +30.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1546 | +0.022 | +30.58€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 762 | +0.012 | +2.17€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 762 | +0.012 | +2.17€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 470 | +0.015 | +29.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 470 | +0.015 | +29.46€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2009 | -0.037 | -25.27€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2009 | -0.037 | -25.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 602 | -0.030 | -12.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 602 | -0.030 | -12.45€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 701 | -0.013 | +9.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 701 | -0.013 | +9.21€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 706 | -0.068 | -22.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 706 | -0.068 | -22.03€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 11791 | -0.033 | -135.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 5634 | -0.037 | -105.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 6157 | -0.029 | -29.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 406 | -0.047 | -20.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 202 | -0.020 | +1.01€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 204 | -0.073 | -21.94€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 3049 | -0.022 | +15.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1446 | -0.022 | +8.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1603 | -0.022 | +7.37€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1227 | -0.026 | +17.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 623 | -0.034 | -2.20€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 604 | -0.017 | +19.60€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 2615 | -0.042 | -83.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1231 | -0.048 | -58.93€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1384 | -0.035 | -24.83€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 2271 | -0.030 | -10.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1094 | -0.036 | -18.58€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1177 | -0.024 | +8.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 2223 | -0.042 | -52.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1038 | -0.048 | -35.05€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1185 | -0.037 | -17.82€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 57848 | -0.000 | +3002.39€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 57848 | -0.000 | +3002.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 10463 | +0.027 | +1367.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 10463 | +0.027 | +1367.92€ | 2 | 4 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 8216 | -0.035 | -114.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 8216 | -0.035 | -114.22€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 10587 | +0.024 | +1103.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 10587 | +0.024 | +1103.88€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 8105 | -0.048 | -155.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 8105 | -0.048 | -155.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 9802 | -0.005 | +262.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 9802 | -0.005 | +262.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 10675 | +0.017 | +538.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 10675 | +0.017 | +538.36€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6906 | -0.056 | -141.24€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6906 | -0.056 | -141.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1237 | -0.002 | -17.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1237 | -0.002 | -17.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1893 | -0.069 | -33.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1893 | -0.069 | -33.26€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 66 | -0.015 | -0.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 66 | -0.015 | -0.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 791 | -0.119 | -33.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 791 | -0.119 | -33.96€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2061 | -0.070 | -30.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2061 | -0.070 | -30.76€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 142767 | -0.077 | +1909.87€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 142767 | -0.077 | +1909.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 24895 | -0.079 | +1334.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 24895 | -0.079 | +1334.74€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 21426 | -0.099 | -1004.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 21426 | -0.099 | -1004.01€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 25212 | -0.069 | +1237.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 25212 | -0.069 | +1237.17€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 20971 | -0.097 | -607.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 20971 | -0.097 | -607.32€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 25613 | -0.057 | +316.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 25613 | -0.057 | +316.10€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 24650 | -0.069 | +633.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 24650 | -0.069 | +633.19€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8930 | -0.035 | -187.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8930 | -0.035 | -187.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1002 | -0.017 | -19.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1002 | -0.017 | -19.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2055 | -0.048 | -30.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2055 | -0.048 | -30.39€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2620 | -0.026 | -40.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2620 | -0.026 | -40.14€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1241 | -0.061 | -33.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1241 | -0.061 | -33.25€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1003 | -0.030 | -32.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1003 | -0.030 | -32.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 1889 | +0.121 | +756.91€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 1753 | +0.126 | +744.32€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 409 | +0.125 | +185.32€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 409 | +0.125 | +185.32€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 366 | +0.111 | +120.14€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 366 | +0.111 | +120.14€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#ETH | 338 | +0.138 | +168.70€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 338 | +0.138 | +168.70€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 306 | +0.153 | +170.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 306 | +0.153 | +170.54€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 334 | +0.101 | +99.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 334 | +0.101 | +99.62€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1765 | -0.016 | -19.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1765 | -0.016 | -19.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 335 | +0.002 | +11.00€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 335 | +0.002 | +11.00€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 321 | -0.036 | -11.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 321 | -0.036 | -11.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 449 | -0.045 | -35.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 449 | -0.045 | -35.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 369 | +0.007 | +6.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 369 | +0.007 | +6.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 291 | +0.002 | +11.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 291 | +0.002 | +11.10€ | 0 | 0 |
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
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 430 | -0.213 | -48.62€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 58 | -0.183 | -0.74€ | 1 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 420 | -0.213 | -37.32€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 371 | -0.224 | -43.82€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 49 | -0.128 | +6.50€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 340 | -0.199 | +4.53€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 317 | -0.196 | +1.81€ | 4 | 0 |
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
| ✅ STREAK_FADE_15M | 813 | +0.037 | +66.79€ | 2 | 4 |
| ✅ STREAK_FADE_15M#15min | 813 | +0.037 | +66.79€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 310 | +0.026 | +5.92€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 310 | +0.026 | +5.92€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 67 | -0.007 | -1.40€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 67 | -0.007 | -1.40€ | 1 | 0 |
| ✅ STREAK_FADE_15M#SOL | 80 | +0.012 | +5.58€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 80 | +0.012 | +5.58€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 356 | +0.061 | +56.69€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 356 | +0.061 | +56.69€ | 1 | 5 |
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
| ✅ STREAK_FADE_60M | 108 | -0.045 | -10.31€ | 2 | 0 |
| ✅ STREAK_FADE_60M#60min | 108 | -0.045 | -10.31€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 43 | -0.100 | -5.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 43 | -0.100 | -5.07€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 65 | -0.007 | -5.24€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 65 | -0.007 | -5.24€ | 0 | 1 |
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
| ✅ STRUCT_NO_15M | 10553 | +0.014 | -46.48€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 10553 | +0.014 | -46.48€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4393 | +0.019 | -2.02€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4393 | +0.019 | -2.02€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3627 | +0.010 | -28.45€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3627 | +0.010 | -28.45€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2533 | +0.009 | -16.01€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2533 | +0.009 | -16.01€ | 1 | 0 |
| ✅ UPDOWN_GBM | 87664 | +0.056 | +7910.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 21144 | +0.083 | +4530.12€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2758 | +0.002 | +31.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 58199 | +0.054 | +3254.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 5248 | +0.004 | +96.18€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 7059 | +0.093 | +1142.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1576 | +0.156 | +698.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5406 | +0.076 | +445.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 20180 | +0.057 | +1752.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2930 | +0.085 | +676.55€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 773 | +0.004 | +13.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 13995 | +0.064 | +989.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2369 | +0.002 | +69.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 113 | -0.074 | +2.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 9259 | +0.072 | +976.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1555 | +0.147 | +610.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 7626 | +0.057 | +367.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 20909 | +0.047 | +1416.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 5208 | +0.072 | +799.37€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 740 | +0.007 | +17.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 12944 | +0.047 | +578.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1911 | +0.006 | +18.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 106 | -0.102 | +2.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 18983 | +0.036 | +1026.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 5433 | +0.037 | +436.68€ | 0 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 702 | -0.010 | +2.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 11786 | +0.043 | +585.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 968 | +0.004 | +7.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 94 | -0.135 | -6.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 11272 | +0.069 | +1597.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4442 | +0.103 | +1308.48€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 6442 | +0.049 | +288.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 313 | -0.103 | -0.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 924 | +0.365 | +336.80€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 924 | +0.365 | +336.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 466 | +0.361 | +160.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 466 | +0.361 | +160.58€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 458 | +0.367 | +176.22€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 458 | +0.367 | +176.22€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 21564 | -0.022 | +5156.79€ | 3 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 21564 | -0.022 | +5156.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 4053 | -0.114 | +180.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 4053 | -0.114 | +180.58€ | 3 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2826 | +0.220 | +1818.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2826 | +0.220 | +1818.56€ | 1 | 20 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 6157 | -0.062 | +825.86€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 6157 | -0.062 | +825.86€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5862 | -0.064 | +1058.52€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5862 | -0.064 | +1058.52€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 263 | +0.066 | +28.30€ | 0 | 8 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 263 | +0.066 | +28.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 263 | +0.066 | +28.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 263 | +0.066 | +28.30€ | 0 | 8 |
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