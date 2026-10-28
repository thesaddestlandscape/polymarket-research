# Hipótesis automáticas — 2026-10-28 22:11 UTC
_Generado por shadow_postmortem.py sobre 1096810 resoluciones (PNL=+145265.67€)_

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

- **PATRÓN** `libro_liquidez` > `9217.9234` → IC=+0.129 (n=211)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 9217.9234 (IC base=+0.012)

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
- **FILTRO** `restante_s_al_confirmar` < `138.24` → IC=-0.209 (n=10787)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 138.24
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=32365)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `127.47` → IC=-0.261 (n=1152)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.47
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=3458)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `118.95` → IC=-0.296 (n=1143)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 118.95
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3431)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `160.64` → IC=-0.241 (n=2891)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 160.64
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=8673)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.214 (n=23919)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.106)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.124 (n=4622)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `8754.682` → IC=+0.166 (n=2125)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 8754.682 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.127 (n=20596)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.130 (n=36903)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 11.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.226 (n=19066)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=7646)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `6798.202` → IC=+0.154 (n=2959)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 6798.202 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=2113)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.364 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.187 (n=2587)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `16445.5093` → IC=+0.185 (n=672)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 16445.5093 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.186 (n=1851)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.185 (n=2069)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` < `0.295` → IC=+0.312 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.295 (IC base=+0.181)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=2653)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `16197.5868` → IC=+0.187 (n=684)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 16197.5868 (IC base=+0.181)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.170 (n=519)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.61 (IC base=+0.078)

- **PATRÓN** `libro_liquidez` > `7474.4764` → IC=+0.163 (n=99)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 7474.4764 (IC base=+0.078)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.139 (n=1221)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.44 (IC base=+0.082)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=4639)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.165 (n=3923)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 15.0 (IC base=+0.162)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.374 (n=1504)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.216 (n=2080)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.207)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.351 (n=770)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.211 (n=2414)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.207)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=1173)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.149 (n=997)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 15.0 (IC base=+0.144)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.261 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.145 (n=1286)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `2225.8776` → IC=+0.157 (n=508)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2225.8776 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.162 (n=152)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.069)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.253 (n=887)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.226)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1242)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.226)

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

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=20500)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.201 (n=17348)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.232 (n=8452)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.182 (n=2228)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.179 (n=4676)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 18.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.182 (n=4542)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.178 (n=3882)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.221 (n=2570)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.223 (n=1711)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.298 (n=858)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.219)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=4615)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.181 (n=3918)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.188 (n=3596)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.255 (n=3959)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.247)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.248 (n=3354)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.247)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.358 (n=1326)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=4529)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.190 (n=3858)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.192 (n=3358)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.187)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.428 (n=862)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.424)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.426 (n=868)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.424)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.424)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=909)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.424)

- **PATRÓN** `libro_liquidez` > `4341.1458` → IC=+0.441 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4341.1458 (IC base=+0.424)

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
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.430 (n=314)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.424)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.430 (n=340)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.424)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.436 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.424)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.424)

- **PATRÓN** `libro_liquidez` > `4630.3169` → IC=+0.439 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4630.3169 (IC base=+0.424)

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
- **FILTRO** `py_entrada` > `0.765` → IC=-0.294 (n=32)

  - _Acción_: SKIP cuando `py_entrada` > 0.765
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=29)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=26716)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=26891)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.201)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.195 (n=3960)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.185 (n=8508)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 12.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.198 (n=12051)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.71 (IC base=+0.184)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=11201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.225 (n=5449)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.286 (n=3854)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.188 (n=4587)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.201 (n=9392)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.232 (n=3734)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.274 (n=3784)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.212 (n=3805)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.262 (n=3945)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.207 (n=4442)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=4430)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.248 (n=4648)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=9593)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=9718)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.64` → IC=+0.136 (n=11649)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.64 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=4720)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.144 (n=4420)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.128 (n=5822)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `2.66` → IC=+0.145 (n=4387)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.66 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.191 (n=4873)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.115)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=5298)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.115)

- **PATRÓN** `lag_apertura_s` < `3.26` → IC=+0.137 (n=5854)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.26 (IC base=+0.115)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.302 (n=1810)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.388 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `3842.7655` → IC=+0.295 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3842.7655 (IC base=+0.293)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.289 (n=822)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.280)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.363 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `5110.149` → IC=+0.298 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5110.149 (IC base=+0.280)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.324 (n=590)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.299)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.302 (n=857)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.299)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.397 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.299)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.299 (n=975)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4713` → IC=+0.140 (n=14981)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4713 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.126 (n=15156)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=10427)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.9808` → IC=+0.248 (n=4994)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9808 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.7752` → IC=+0.276 (n=833)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7752 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.626` → IC=+0.182 (n=7465)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 3.626 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6213` → IC=+0.266 (n=4395)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6213 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.3043` → IC=+0.246 (n=1547)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3043 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.3564` → IC=+0.232 (n=4855)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3564 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=7679)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `4454.0021` → IC=+0.151 (n=4994)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4454.0021 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.5672` → IC=+0.142 (n=18576)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5672 (IC base=+0.078)

- **PATRÓN** `dist_vwap_pct` > `0.6033` → IC=+0.188 (n=1222)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.6033 (IC base=+0.078)

- **PATRÓN** `volumen_regimen` < `0.6976` → IC=+0.190 (n=3267)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.6976 (IC base=+0.078)

- **PATRÓN** `volumen_pendiente_norm` > `0.2976` → IC=+0.229 (n=1829)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2976 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` > `2.6905` → IC=+0.208 (n=4195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6905 (IC base=+0.078)

- **PATRÓN** `ballena_activa_n` < `105.0` → IC=+0.223 (n=12462)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 105.0 (IC base=+0.078)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.208 (n=1079)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.3557` → IC=+0.209 (n=3237)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3557 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.217 (n=1577)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.212 (n=2166)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `0.9849` → IC=+0.279 (n=1467)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9849 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.693` → IC=+0.282 (n=1434)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.693 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.2838` → IC=+0.259 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2838 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `1.5518` → IC=+0.209 (n=2764)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5518 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=3523)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `2046.307` → IC=+0.208 (n=1079)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2046.307 (IC base=+0.206)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.226 (n=2017)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.243 (n=2761)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0093 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.0873` → IC=+0.277 (n=921)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0873 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.253 (n=1016)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.5484` → IC=+0.259 (n=2758)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5484 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` < `0.0961` → IC=+0.244 (n=2485)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0961 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.2932` → IC=+0.260 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2932 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.447` → IC=+0.243 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.447 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `1.8749` → IC=+0.244 (n=1743)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8749 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.243 (n=3143)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1771.0608` → IC=+0.243 (n=1838)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1771.0608 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.239 (n=1182)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.241)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.237 (n=896)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.228)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.232 (n=1214)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.228)

- **PATRÓN** `drift_60min` |x|≤ `0.106` → IC=+0.257 (n=1180)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.106 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.240 (n=2804)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `0.9314` → IC=+0.272 (n=893)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9314 (IC base=+0.228)

- **PATRÓN** `dist_vwap_pct` > `0.1871` → IC=+0.236 (n=1270)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1871 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.216` → IC=+0.259 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.216 (IC base=+0.228)

- **PATRÓN** `volumen_regimen` < `1.2306` → IC=+0.230 (n=2678)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2306 (IC base=+0.228)

- **PATRÓN** `volumen_regimen` > `0.6235` → IC=+0.232 (n=2678)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6235 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.276 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` < `1.5138` → IC=+0.229 (n=1162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5138 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `2.4384` → IC=+0.259 (n=880)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4384 (IC base=+0.228)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.151 (n=2827)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0059 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.0762` → IC=+0.165 (n=943)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.0762 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.153 (n=1059)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.7205` → IC=+0.170 (n=2825)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.7205 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.906` → IC=+0.141 (n=460)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 10.906 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.076` → IC=+0.136 (n=2578)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 4.076 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `1.2044` → IC=+0.139 (n=2825)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.2044 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.0964` → IC=+0.153 (n=1024)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.0964 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `2.4535` → IC=+0.139 (n=2702)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.4535 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `208.0` → IC=+0.172 (n=1166)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 208.0 (IC base=+0.130)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.215 (n=1130)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=3564)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.265 (n=1311)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.155` → IC=+0.280 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.155 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.198 (n=3015)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.3526` → IC=+0.220 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3526 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.7105` → IC=+0.211 (n=1496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7105 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.199 (n=4056)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `2029.6962` → IC=+0.203 (n=1130)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2029.6962 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.222 (n=2708)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0109 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.452` → IC=+0.224 (n=2707)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.452 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=1159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.0323` → IC=+0.267 (n=1027)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0323 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.158` → IC=+0.256 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.158 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3488` → IC=+0.261 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3488 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.7601` → IC=+0.226 (n=1332)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7601 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.222 (n=1546)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `1916.01` → IC=+0.218 (n=1395)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1916.01 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.217 (n=2561)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.141 (n=165)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=4098)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.146 (n=772)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0043 (IC base=+0.059)

- **PATRÓN** `ibs_20min` > `0.9545` → IC=+0.234 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9545 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.137` → IC=+0.334 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.137 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` < `0.1947` → IC=+0.329 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1947 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.218` → IC=+0.198 (n=1269)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 5.218 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` > `0.693` → IC=+0.341 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.693 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.3054` → IC=+0.340 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3054 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` < `1.4207` → IC=+0.348 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4207 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` > `2.2782` → IC=+0.335 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2782 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `144.0` → IC=+0.334 (n=673)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 144.0 (IC base=+0.059)

- **PATRÓN** `ibs_20min` < `0.0921` → IC=+0.182 (n=1067)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.0921 (IC base=+0.042)

- **PATRÓN** `dist_vwap_pct` > `0.7306` → IC=+0.160 (n=245)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.7306 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` < `0.839` → IC=+0.154 (n=1308)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.839 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.2866` → IC=+0.210 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2866 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` < `1.7858` → IC=+0.143 (n=1258)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.7858 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` > `2.1669` → IC=+0.162 (n=855)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.1669 (IC base=+0.042)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.169 (n=119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=634)

- **FILTRO** `ibs_20min` > `0.2105` → IC=-0.134 (n=4001)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2105
  - _Potencial_: sin este filtro IC_bueno=+0.149 (n=1976)

- **FILTRO** `sigma_ewma_delta_pct` > `8.558` → IC=-0.230 (n=639)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.558
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=5338)

- **PATRÓN** `ibs_20min` > `0.8889` → IC=+0.198 (n=190)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.8889 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.9803` → IC=+0.295 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9803 (IC base=+0.029)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.1` → IC=+0.140 (n=234)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 3.1 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` < `0.871` → IC=+0.272 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.871 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` > `1.0359` → IC=+0.300 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0359 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` < `0.1597` → IC=+0.288 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1597 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `2.4948` → IC=+0.298 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4948 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` > `1.5527` → IC=+0.269 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5527 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.280 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.029)

- **PATRÓN** `ibs_20min` < `0.2105` → IC=+0.149 (n=1976)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.2105 (IC base=-0.040)

- **PATRÓN** `volumen_regimen` < `0.6932` → IC=+0.306 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6932 (IC base=-0.040)

- **PATRÓN** `volumen_pendiente_norm` < `0.1046` → IC=+0.289 (n=691)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1046 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` < `2.4345` → IC=+0.304 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4345 (IC base=-0.040)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.5952` → IC=-0.178 (n=1119)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.5952
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3359)

- **FILTRO** `ibs_20min` < `0.7647` → IC=-0.153 (n=2955)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7647
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=1523)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.166 (n=1049)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=3429)

- **FILTRO** `ibs_20min` > `0.749` → IC=-0.200 (n=1590)

  - _Acción_: SKIP cuando `ibs_20min` > 0.749
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=4772)

- **PATRÓN** `dist_vwap_pct` > `0.7208` → IC=+0.343 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7208 (IC base=-0.064)

- **PATRÓN** `dist_vwap_pct` < `0.2444` → IC=+0.307 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2444 (IC base=-0.064)

- **PATRÓN** `volumen_regimen` > `0.7043` → IC=+0.320 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7043 (IC base=-0.064)

- **PATRÓN** `volumen_pendiente_norm` < `0.1023` → IC=+0.304 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1023 (IC base=-0.064)

- **PATRÓN** `volumen_pendiente_norm` > `0.0744` → IC=+0.301 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0744 (IC base=-0.064)

- **PATRÓN** `volumen_spike_ratio` < `1.4239` → IC=+0.318 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4239 (IC base=-0.064)

- **PATRÓN** `volumen_spike_ratio` > `1.8591` → IC=+0.311 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8591 (IC base=-0.064)

- **PATRÓN** `dist_vwap_pct` > `0.8069` → IC=+0.284 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8069 (IC base=-0.002)

- **PATRÓN** `volumen_regimen` < `0.7243` → IC=+0.265 (n=791)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7243 (IC base=-0.002)

- **PATRÓN** `volumen_regimen` > `1.0669` → IC=+0.284 (n=814)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0669 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.1687` → IC=+0.287 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1687 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` < `2.1753` → IC=+0.264 (n=1471)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1753 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.263 (n=1671)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=-0.002)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.208 (n=6528)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.093)

- **PATRÓN** `ibs_20min` > `0.3103` → IC=+0.167 (n=19567)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.3103 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.9311` → IC=+0.300 (n=1405)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9311 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.571` → IC=+0.165 (n=8754)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 3.571 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` < `1.1733` → IC=+0.267 (n=7207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1733 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` > `0.6911` → IC=+0.274 (n=6440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6911 (IC base=+0.093)

- **PATRÓN** `volumen_pendiente_norm` > `0.2404` → IC=+0.285 (n=2168)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2404 (IC base=+0.093)

- **PATRÓN** `volumen_spike_ratio` > `2.2803` → IC=+0.277 (n=5193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2803 (IC base=+0.093)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.302 (n=11045)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 91.0 (IC base=+0.093)

- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.156 (n=6309)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0096 (IC base=+0.076)

- **PATRÓN** `ibs_20min` < `0.65` → IC=+0.146 (n=18879)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.65 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` < `0.7044` → IC=+0.268 (n=2677)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7044 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` > `1.1952` → IC=+0.267 (n=2027)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1952 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.295` → IC=+0.319 (n=1316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.295 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` < `1.5813` → IC=+0.295 (n=3879)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5813 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` > `2.283` → IC=+0.288 (n=3997)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.283 (IC base=+0.076)

- **PATRÓN** `ballena_activa_n` < `75.0` → IC=+0.299 (n=8748)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 75.0 (IC base=+0.076)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.5801` → IC=-0.152 (n=2654)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5801
  - _Potencial_: sin este filtro IC_bueno=+0.203 (n=2656)

- **FILTRO** `ibs_20min` > `0.729` → IC=-0.222 (n=1145)

  - _Acción_: SKIP cuando `ibs_20min` > 0.729
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=3438)

- **FILTRO** `sigma_ewma_delta_pct` > `4.296` → IC=-0.221 (n=995)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.296
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=3588)

- **PATRÓN** `ibs_20min` > `0.9286` → IC=+0.330 (n=1328)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9286 (IC base=+0.026)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.112` → IC=+0.184 (n=1779)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 3.112 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.316 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.4491` → IC=+0.263 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4491 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` > `2.2621` → IC=+0.291 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2621 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.306 (n=1165)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.026)

- **PATRÓN** `ibs_20min` < `0.1699` → IC=+0.162 (n=1146)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.1699 (IC base=-0.029)

- **PATRÓN** `volumen_pendiente_norm` < `0.0738` → IC=+0.416 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0738 (IC base=-0.029)

- **PATRÓN** `volumen_spike_ratio` < `2.6875` → IC=+0.410 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6875 (IC base=-0.029)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.404 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=-0.029)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.2959` → IC=+0.221 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2959 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` < `1.1954` → IC=+0.204 (n=1925)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1954 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` > `0.6925` → IC=+0.208 (n=1720)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6925 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.2788` → IC=+0.252 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2788 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` < `1.4254` → IC=+0.229 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4254 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` > `2.4638` → IC=+0.207 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4638 (IC base=+0.020)

- **PATRÓN** `ballena_activa_n` < `268.0` → IC=+0.238 (n=1271)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 268.0 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` < `1.1685` → IC=+0.235 (n=1295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1685 (IC base=-0.004)

- **PATRÓN** `volumen_regimen` > `0.6209` → IC=+0.239 (n=1295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6209 (IC base=-0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2716` → IC=+0.299 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2716 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.5381` → IC=+0.249 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5381 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.1598` → IC=+0.251 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1598 (IC base=-0.004)

- **PATRÓN** `ballena_activa_n` < `194.0` → IC=+0.244 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 194.0 (IC base=-0.004)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.316 (n=1272)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.275)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.283 (n=2810)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.275)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.316 (n=1513)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.275)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.678` → IC=+0.305 (n=922)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.678 (IC base=+0.275)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.287 (n=2451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.275)

- **PATRÓN** `volumen_spike_ratio` > `1.6099` → IC=+0.280 (n=2718)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6099 (IC base=+0.275)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.284 (n=3333)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.275)

- **PATRÓN** `libro_liquidez` > `2028.2784` → IC=+0.290 (n=935)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2028.2784 (IC base=+0.275)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.294 (n=1721)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.275)

- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.324 (n=1647)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0087 (IC base=+0.296)

- **PATRÓN** `drift_60min` |x|≤ `0.1781` → IC=+0.315 (n=1087)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1781 (IC base=+0.296)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.322 (n=940)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.296)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.299 (n=854)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.296)

- **PATRÓN** `ibs_20min` < `0.376` → IC=+0.297 (n=2470)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.376 (IC base=+0.296)

- **PATRÓN** `ibs_20min` > `0.1304` → IC=+0.303 (n=1651)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1304 (IC base=+0.296)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.377` → IC=+0.306 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.377 (IC base=+0.296)

- **PATRÓN** `volumen_pendiente_norm` < `0.1975` → IC=+0.295 (n=2427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1975 (IC base=+0.296)

- **PATRÓN** `volumen_pendiente_norm` > `0.3431` → IC=+0.312 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3431 (IC base=+0.296)

- **PATRÓN** `volumen_spike_ratio` < `1.7344` → IC=+0.301 (n=1043)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7344 (IC base=+0.296)

- **PATRÓN** `volumen_spike_ratio` > `2.7019` → IC=+0.309 (n=1075)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7019 (IC base=+0.296)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.298 (n=1248)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.296)

- **PATRÓN** `libro_liquidez` > `1918.06` → IC=+0.303 (n=1120)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1918.06 (IC base=+0.296)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.305 (n=1103)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.296)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7352` → IC=-0.183 (n=1204)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7352
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=3622)

- **PATRÓN** `ibs_20min` > `0.8669` → IC=+0.165 (n=1169)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.8669 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.1489` → IC=+0.231 (n=870)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1489 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.2131` → IC=+0.233 (n=1437)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2131 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `1.0079` → IC=+0.237 (n=1461)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0079 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` > `0.6673` → IC=+0.233 (n=1483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6673 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.1021` → IC=+0.243 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1021 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.4657` → IC=+0.237 (n=1607)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4657 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `119.0` → IC=+0.253 (n=1639)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 119.0 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `1.0212` → IC=+0.243 (n=1020)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0212 (IC base=+0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2825` → IC=+0.300 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2825 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.794` → IC=+0.274 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.794 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.4415` → IC=+0.260 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4415 (IC base=+0.002)

- **PATRÓN** `ballena_activa_n` < `121.0` → IC=+0.263 (n=1125)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 121.0 (IC base=+0.002)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.75` → IC=-0.232 (n=2020)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.310 (n=2051)

- **FILTRO** `ibs_20min` > `0.6364` → IC=-0.234 (n=986)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6364
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=2963)

- **FILTRO** `sigma_ewma_delta_pct` > `8.409` → IC=-0.251 (n=455)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.409
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=3494)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.310 (n=2051)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.75 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` > `0.2143` → IC=+0.343 (n=881)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2143 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.357` → IC=+0.191 (n=635)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.357 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` < `0.8488` → IC=+0.339 (n=1005)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8488 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` > `0.6998` → IC=+0.334 (n=1346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6998 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` < `0.1597` → IC=+0.332 (n=1559)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1597 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.2751` → IC=+0.351 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2751 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.354 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.041)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.350 (n=1296)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 47.0 (IC base=+0.041)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.129 (n=2963)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.6364 (IC base=+0.038)

- **PATRÓN** `volumen_regimen` < `0.6965` → IC=+0.273 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6965 (IC base=+0.038)

- **PATRÓN** `volumen_pendiente_norm` < `0.1591` → IC=+0.243 (n=1436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1591 (IC base=+0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.259 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` < `2.4547` → IC=+0.254 (n=1333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4547 (IC base=+0.038)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.268 (n=1366)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=+0.038)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.353 (n=1891)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.309)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.313 (n=825)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.309)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.316 (n=1005)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.309)

- **PATRÓN** `ibs_20min` > `0.7632` → IC=+0.345 (n=1892)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7632 (IC base=+0.309)

- **PATRÓN** `dist_vwap_pct` > `0.2027` → IC=+0.333 (n=1180)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2027 (IC base=+0.309)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.856` → IC=+0.326 (n=1025)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.856 (IC base=+0.309)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.14` → IC=+0.310 (n=2410)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.14 (IC base=+0.309)

- **PATRÓN** `volumen_regimen` > `0.8673` → IC=+0.329 (n=1411)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8673 (IC base=+0.309)

- **PATRÓN** `volumen_pendiente_norm` > `0.2809` → IC=+0.348 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2809 (IC base=+0.309)

- **PATRÓN** `volumen_spike_ratio` > `1.4319` → IC=+0.322 (n=2033)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4319 (IC base=+0.309)

- **PATRÓN** `libro_liquidez` > `2580.7422` → IC=+0.310 (n=1411)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2580.7422 (IC base=+0.309)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.342 (n=1653)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.309)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.341 (n=1498)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.310)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.318 (n=1127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.310)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.311 (n=1100)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.310)

- **PATRÓN** `ibs_20min` < `0.3778` → IC=+0.332 (n=2245)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3778 (IC base=+0.310)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.619` → IC=+0.325 (n=834)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.619 (IC base=+0.310)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.099` → IC=+0.311 (n=2671)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.099 (IC base=+0.310)

- **PATRÓN** `volumen_regimen` < `0.7226` → IC=+0.315 (n=988)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7226 (IC base=+0.310)

- **PATRÓN** `volumen_regimen` > `1.2164` → IC=+0.340 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2164 (IC base=+0.310)

- **PATRÓN** `volumen_pendiente_norm` > `0.2851` → IC=+0.363 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2851 (IC base=+0.310)

- **PATRÓN** `volumen_spike_ratio` < `1.4152` → IC=+0.324 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4152 (IC base=+0.310)

- **PATRÓN** `volumen_spike_ratio` > `2.1375` → IC=+0.311 (n=938)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1375 (IC base=+0.310)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.227 (n=4854)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.1213` → IC=+0.196 (n=6401)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1213 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=15107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `0.5517` → IC=+0.233 (n=14550)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5517 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `0.1628` → IC=+0.206 (n=5756)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1628 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.241` → IC=+0.254 (n=3791)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.241 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `1.1869` → IC=+0.162 (n=9659)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1869 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` > `0.6242` → IC=+0.160 (n=9660)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6242 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2946` → IC=+0.206 (n=2117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2946 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `2.6126` → IC=+0.191 (n=4712)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.6126 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.196 (n=13466)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 90.0 (IC base=+0.178)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.189 (n=6185)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0055 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.0794` → IC=+0.226 (n=4683)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0794 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.209 (n=6655)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.5146` → IC=+0.238 (n=14040)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5146 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.856` → IC=+0.196 (n=2271)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 9.856 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.521` → IC=+0.185 (n=13111)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 3.521 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `1.1825` → IC=+0.165 (n=10017)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1825 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.223 (n=2089)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6493` → IC=+0.188 (n=4421)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6493 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.194 (n=13003)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 96.0 (IC base=+0.182)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.224 (n=810)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.3411` → IC=+0.235 (n=2425)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3411 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.234 (n=903)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.229 (n=1640)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.9352` → IC=+0.296 (n=1618)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9352 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.755` → IC=+0.330 (n=769)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.755 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.2818` → IC=+0.283 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2818 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `1.8413` → IC=+0.220 (n=1536)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8413 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `1.4401` → IC=+0.223 (n=2304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4401 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=2663)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.223)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.233 (n=1438)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.0927` → IC=+0.305 (n=834)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0927 (IC base=+0.254)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.260 (n=1959)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.254)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.255 (n=1744)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.254)

- **PATRÓN** `ibs_20min` < `0.4167` → IC=+0.272 (n=1895)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4167 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` < `0.1008` → IC=+0.261 (n=1662)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1008 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` > `0.3012` → IC=+0.280 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3012 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` < `1.4441` → IC=+0.276 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4441 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` > `2.7271` → IC=+0.256 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7271 (IC base=+0.254)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.258 (n=2163)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.254)

- **PATRÓN** `libro_liquidez` > `1526.1448` → IC=+0.258 (n=1693)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1526.1448 (IC base=+0.254)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.260 (n=840)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.254)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.208 (n=731)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.064` → IC=+0.192 (n=732)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.064 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=2303)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.314` → IC=+0.216 (n=2193)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.314 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.1861` → IC=+0.218 (n=1160)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1861 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.109` → IC=+0.215 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.109 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.6938` → IC=+0.159 (n=966)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.6938 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` > `1.0626` → IC=+0.151 (n=994)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 1.0626 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.2835` → IC=+0.189 (n=342)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2835 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `1.413` → IC=+0.170 (n=719)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.413 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `2.4812` → IC=+0.163 (n=718)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.4812 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `412.0` → IC=+0.152 (n=2114)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 412.0 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.174 (n=2307)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0059 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.2346` → IC=+0.175 (n=2028)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2346 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.183 (n=1103)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.6182` → IC=+0.208 (n=2305)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6182 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.302` → IC=+0.187 (n=436)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 11.302 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.171` → IC=+0.150 (n=2003)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.171 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.204` → IC=+0.162 (n=2306)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.204 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` < `0.0938` → IC=+0.152 (n=1983)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.0938 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.4914` → IC=+0.153 (n=2182)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4914 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `221.0` → IC=+0.181 (n=940)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 221.0 (IC base=+0.148)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.238 (n=1118)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.3992` → IC=+0.225 (n=2169)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3992 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.234 (n=909)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=1294)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.293` → IC=+0.306 (n=575)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.293 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.212 (n=2132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.3532` → IC=+0.233 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3532 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.7659` → IC=+0.211 (n=1055)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7659 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.7137` → IC=+0.225 (n=1087)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7137 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.217 (n=2945)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `1919.67` → IC=+0.223 (n=1118)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1919.67 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.241 (n=1874)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.4186` → IC=+0.256 (n=1874)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4186 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.278 (n=801)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0243` → IC=+0.290 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0243 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.274` → IC=+0.277 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.274 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.3585` → IC=+0.287 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3585 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.7612` → IC=+0.235 (n=899)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7612 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.1714` → IC=+0.239 (n=1363)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1714 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.234 (n=1092)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1911.8798` → IC=+0.243 (n=965)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1911.8798 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.239 (n=1393)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.234)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.200 (n=1052)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.0784` → IC=+0.198 (n=790)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.0784 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=2458)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.4386` → IC=+0.222 (n=2117)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4386 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.1422` → IC=+0.191 (n=1407)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1422 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.649` → IC=+0.194 (n=540)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 9.649 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.022` → IC=+0.147 (n=2085)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.022 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.1028` → IC=+0.172 (n=965)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1028 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.8297` → IC=+0.143 (n=1549)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.8297 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `2.5287` → IC=+0.162 (n=775)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.5287 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `7034.7561` → IC=+0.197 (n=1075)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 7034.7561 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `133.0` → IC=+0.147 (n=2306)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 133.0 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.156 (n=2508)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0073 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.3911` → IC=+0.146 (n=2505)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3911 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=1193)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.6749` → IC=+0.186 (n=2505)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6749 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.53` → IC=+0.153 (n=607)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 9.53 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.8548` → IC=+0.158 (n=1670)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8548 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.3001` → IC=+0.194 (n=380)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.3001 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.8129` → IC=+0.138 (n=1574)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.8129 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `2.5558` → IC=+0.135 (n=787)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.5558 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `6419.3306` → IC=+0.186 (n=1136)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 6419.3306 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `111.0` → IC=+0.136 (n=2041)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 111.0 (IC base=+0.130)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.173 (n=1206)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0107 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.161 (n=1279)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 15.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.4815` → IC=+0.213 (n=2657)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4815 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.1938` → IC=+0.189 (n=1501)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1938 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.305` → IC=+0.286 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.305 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `1.1761` → IC=+0.135 (n=2655)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.1761 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.7061` → IC=+0.124 (n=2372)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.7061 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` < `0.1639` → IC=+0.131 (n=2711)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.1639 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.5502` → IC=+0.139 (n=1135)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.5502 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.126 (n=2765)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2655.2052` → IC=+0.202 (n=1204)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2655.2052 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.141 (n=1135)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 22.0 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0113` → IC=+0.143 (n=2732)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0113 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.1087` → IC=+0.169 (n=911)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1087 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=2789)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.625` → IC=+0.218 (n=2735)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.625 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.411` → IC=+0.137 (n=2406)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 2.411 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.1845` → IC=+0.128 (n=2731)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.1845 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.1651` → IC=+0.123 (n=2660)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1651 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.278` → IC=+0.135 (n=376)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.278 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.442` → IC=+0.127 (n=854)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.442 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `2.4632` → IC=+0.126 (n=853)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.4632 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2530.1372` → IC=+0.185 (n=1238)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2530.1372 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.124 (n=2525)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 47.0 (IC base=+0.119)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.247 (n=2183)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.1686` → IC=+0.235 (n=1075)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1686 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.226 (n=2536)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=2187)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.6604` → IC=+0.255 (n=2445)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6604 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.1805` → IC=+0.230 (n=1548)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1805 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.643` → IC=+0.255 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.643 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` < `1.1704` → IC=+0.223 (n=2444)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1704 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `0.6229` → IC=+0.230 (n=2443)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6229 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.2322` → IC=+0.266 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2322 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `2.4689` → IC=+0.225 (n=2381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4689 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `1.8103` → IC=+0.233 (n=1587)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8103 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.224 (n=3183)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `2103.5594` → IC=+0.225 (n=2443)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2103.5594 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.237 (n=1091)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.234)

- **PATRÓN** `sigma_h` > `0.0226` → IC=+0.243 (n=1126)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0226 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.0881` → IC=+0.260 (n=827)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0881 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.252 (n=1206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.237 (n=1109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.431` → IC=+0.261 (n=2479)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.431 (IC base=+0.234)

- **PATRÓN** `dist_vwap_pct` > `0.3025` → IC=+0.246 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3025 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.319` → IC=+0.270 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.319 (IC base=+0.234)

- **PATRÓN** `volumen_regimen` < `0.869` → IC=+0.237 (n=1653)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.869 (IC base=+0.234)

- **PATRÓN** `volumen_regimen` > `0.6418` → IC=+0.238 (n=2479)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6418 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2794` → IC=+0.291 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2794 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `2.5151` → IC=+0.231 (n=2320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5151 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `1.4363` → IC=+0.236 (n=2319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4363 (IC base=+0.234)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.206 (n=1596)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.1302` → IC=+0.204 (n=1593)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1302 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.194 (n=3631)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 6.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.3439` → IC=+0.212 (n=3619)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3439 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.7847` → IC=+0.204 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7847 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.597` → IC=+0.211 (n=1565)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.597 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.8638` → IC=+0.202 (n=2170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8638 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` > `1.1944` → IC=+0.183 (n=1085)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 1.1944 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.0739` → IC=+0.188 (n=1462)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.0739 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `1.4307` → IC=+0.194 (n=1175)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4307 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.187 (n=4081)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `2625.0768` → IC=+0.187 (n=3233)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2625.0768 (IC base=+0.180)

- **PATRÓN** `ibs_20min` < `0.395` → IC=+0.150 (n=2648)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.395 (IC base=+0.077)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.200 (n=869)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.3257` → IC=+0.212 (n=984)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3257 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.220 (n=901)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` > `0.6412` → IC=+0.249 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6412 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` > `0.3064` → IC=+0.211 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3064 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.049` → IC=+0.209 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.049 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.274` → IC=+0.192 (n=1126)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 9.274 (IC base=+0.192)

- **PATRÓN** `volumen_regimen` < `0.8772` → IC=+0.214 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8772 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` < `0.1528` → IC=+0.195 (n=1032)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.1528 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` > `0.0706` → IC=+0.194 (n=396)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0706 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` < `2.1894` → IC=+0.205 (n=848)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1894 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `10481.565` → IC=+0.193 (n=984)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 10481.565 (IC base=+0.192)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.204 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 162.0 (IC base=+0.192)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.168 (n=404)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0029 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.6431` → IC=+0.138 (n=1064)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.6431 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.169 (n=520)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 164.0 (IC base=+0.085)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.234 (n=765)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.1262` → IC=+0.219 (n=504)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1262 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.214 (n=1194)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `0.3648` → IC=+0.238 (n=1023)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3648 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` > `0.7873` → IC=+0.206 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7873 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.884` → IC=+0.237 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.884 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `1.0194` → IC=+0.207 (n=1008)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0194 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.159` → IC=+0.224 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.159 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `1.4274` → IC=+0.207 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4274 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `1.7865` → IC=+0.207 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7865 (IC base=+0.197)

- **PATRÓN** `ibs_20min` < `0.1094` → IC=+0.166 (n=381)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.1094 (IC base=+0.070)

- **PATRÓN** `libro_liquidez` > `8288.2304` → IC=+0.142 (n=518)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 8288.2304 (IC base=+0.070)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.7041` → IC=-0.163 (n=339)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7041
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=1020)

- **PATRÓN** `sigma_h` > `0.011` → IC=+0.189 (n=300)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.011 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.191 (n=811)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 8.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.9804` → IC=+0.281 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9804 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.947` → IC=+0.236 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.947 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.072` → IC=+0.246 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.072 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `0.8887` → IC=+0.183 (n=600)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.8887 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` > `0.714` → IC=+0.172 (n=803)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 0.714 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.2307` → IC=+0.188 (n=168)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2307 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `1.4411` → IC=+0.192 (n=290)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.4411 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `2.1481` → IC=+0.167 (n=394)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.1481 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.174 (n=933)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.02 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `2769.6166` → IC=+0.190 (n=408)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2769.6166 (IC base=+0.164)

- **PATRÓN** `ibs_20min` < `0.2222` → IC=+0.187 (n=452)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.2222 (IC base=+0.036)

- **PATRÓN** `libro_liquidez` > `2590.1864` → IC=+0.141 (n=463)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2590.1864 (IC base=+0.036)

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
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.231 (n=6328)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=19778)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.4426` → IC=+0.230 (n=18958)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4426 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.8748` → IC=+0.208 (n=2287)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8748 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.146` → IC=+0.253 (n=4625)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.146 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `1.2201` → IC=+0.166 (n=12733)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2201 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2417` → IC=+0.206 (n=3437)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2417 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.6207` → IC=+0.195 (n=6159)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6207 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `108.0` → IC=+0.202 (n=17612)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 108.0 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.196 (n=7623)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0057 (IC base=+0.189)

- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.191 (n=5776)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0118 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.3724` → IC=+0.194 (n=15246)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.3724 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=6446)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` < `0.5902` → IC=+0.241 (n=17323)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5902 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.691` → IC=+0.203 (n=2381)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.691 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.49` → IC=+0.193 (n=16814)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 3.49 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` < `1.0582` → IC=+0.163 (n=10283)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.0582 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.2921` → IC=+0.252 (n=2348)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2921 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `2.6337` → IC=+0.200 (n=5493)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6337 (IC base=+0.189)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.237 (n=5628)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.189)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3541` → IC=+0.231 (n=3071)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3541 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.244 (n=1493)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.231)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.235 (n=2065)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` > `0.8591` → IC=+0.299 (n=2048)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8591 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.18` → IC=+0.346 (n=721)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.18 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.2333` → IC=+0.287 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2333 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` < `1.4481` → IC=+0.232 (n=987)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4481 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` > `2.2917` → IC=+0.241 (n=1341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2917 (IC base=+0.231)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.248 (n=3329)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.231)

- **PATRÓN** `libro_liquidez` > `2045.6055` → IC=+0.233 (n=1024)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2045.6055 (IC base=+0.231)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.256 (n=1857)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.231)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.269 (n=2657)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0092 (IC base=+0.266)

- **PATRÓN** `drift_60min` |x|≤ `0.0863` → IC=+0.295 (n=886)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0863 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.271 (n=2445)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.266)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.266 (n=2414)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` < `0.5289` → IC=+0.288 (n=2655)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5289 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` < `0.097` → IC=+0.268 (n=2400)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.097 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` > `0.2895` → IC=+0.289 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2895 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` < `1.5681` → IC=+0.268 (n=1113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5681 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` > `2.6826` → IC=+0.278 (n=843)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6826 (IC base=+0.266)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.266 (n=3032)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.266)

- **PATRÓN** `libro_liquidez` > `1769.2468` → IC=+0.271 (n=1770)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1769.2468 (IC base=+0.266)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.273 (n=1109)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.266)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.189 (n=1025)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0029 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.104` → IC=+0.160 (n=1352)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.104 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=3202)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.2315` → IC=+0.202 (n=3072)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2315 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.3206` → IC=+0.201 (n=1064)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3206 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.551` → IC=+0.157 (n=648)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 9.551 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.181` → IC=+0.150 (n=2842)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.181 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.6321` → IC=+0.172 (n=1025)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.6321 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` > `1.0762` → IC=+0.151 (n=1393)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 1.0762 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.2732` → IC=+0.191 (n=444)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2732 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.1714` → IC=+0.154 (n=2649)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.1714 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.5326` → IC=+0.153 (n=2689)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.5326 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `232.0` → IC=+0.178 (n=995)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 232.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.162 (n=2638)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0059 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.0778` → IC=+0.184 (n=880)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.0778 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=976)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.6912` → IC=+0.190 (n=2638)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6912 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.045` → IC=+0.154 (n=435)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 11.045 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.0505` → IC=+0.156 (n=2322)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0505 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2185` → IC=+0.194 (n=492)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2185 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.4315` → IC=+0.146 (n=2533)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4315 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.7783` → IC=+0.146 (n=1688)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.7783 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=3424)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `236.0` → IC=+0.154 (n=819)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 236.0 (IC base=+0.140)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.251 (n=1053)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0127 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=3308)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=2820)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=1183)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.195` → IC=+0.324 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.195 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` < `0.1312` → IC=+0.227 (n=2968)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1312 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `1.6197` → IC=+0.230 (n=3075)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6197 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.232 (n=3767)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `2028.2784` → IC=+0.240 (n=1052)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2028.2784 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.245 (n=2629)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0109 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.1789` → IC=+0.258 (n=1313)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1789 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.262 (n=1127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0476` → IC=+0.304 (n=996)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0476 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.727` → IC=+0.294 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.727 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3488` → IC=+0.307 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3488 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1492` → IC=+0.251 (n=1903)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1492 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.246 (n=1515)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1912.48` → IC=+0.250 (n=1353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1912.48 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.249 (n=1910)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.240)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.197 (n=1091)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0035 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.4269` → IC=+0.153 (n=3269)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4269 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.155 (n=3395)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.8114` → IC=+0.261 (n=1483)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8114 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.142` → IC=+0.167 (n=1689)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.142 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.058` → IC=+0.157 (n=1464)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.058 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.0538` → IC=+0.153 (n=2877)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.0538 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2344` → IC=+0.192 (n=579)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2344 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `1.5231` → IC=+0.160 (n=1406)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.5231 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `2.186` → IC=+0.149 (n=1448)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 2.186 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `5394.3009` → IC=+0.232 (n=1482)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5394.3009 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.155 (n=1406)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 70.0 (IC base=+0.143)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.156 (n=2732)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0076 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.4355` → IC=+0.143 (n=2728)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.4355 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.158 (n=997)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.5885` → IC=+0.204 (n=2401)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5885 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.214` → IC=+0.167 (n=544)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.214 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.143` → IC=+0.133 (n=2382)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 3.143 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.6926` → IC=+0.149 (n=1201)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6926 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2959` → IC=+0.223 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2959 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.5372` → IC=+0.143 (n=2351)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.5372 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `6331.5198` → IC=+0.207 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6331.5198 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `97.0` → IC=+0.139 (n=1795)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 97.0 (IC base=+0.133)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.155 (n=1497)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0107 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.153 (n=2336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 11.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `0.4364` → IC=+0.194 (n=3301)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.4364 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `1.0085` → IC=+0.204 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0085 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.521` → IC=+0.265 (n=836)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.521 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.8801` → IC=+0.138 (n=2202)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.8801 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1636` → IC=+0.122 (n=3442)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1636 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.8305` → IC=+0.126 (n=2151)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.8305 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.123 (n=3439)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2704.1228` → IC=+0.245 (n=1101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2704.1228 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.128 (n=1082)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 22.0 (IC base=+0.120)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.152 (n=2767)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0104 (IC base=+0.116)

- **PATRÓN** `drift_60min` |x|≤ `0.1346` → IC=+0.152 (n=1049)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1346 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.128 (n=3249)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.207 (n=3159)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6667 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.18` → IC=+0.140 (n=3016)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 3.18 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `0.6401` → IC=+0.145 (n=1049)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.6401 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.2255` → IC=+0.161 (n=543)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2255 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `1.4384` → IC=+0.148 (n=988)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4384 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `2572.0411` → IC=+0.197 (n=1048)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2572.0411 (IC base=+0.116)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.130 (n=2636)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 45.0 (IC base=+0.116)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0138` → IC=+0.257 (n=2760)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0138 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.238 (n=3230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.237 (n=2764)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` > `0.6127` → IC=+0.270 (n=2760)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6127 (IC base=+0.234)

- **PATRÓN** `dist_vwap_pct` > `0.1899` → IC=+0.248 (n=1647)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1899 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.305` → IC=+0.280 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.305 (IC base=+0.234)

- **PATRÓN** `volumen_regimen` < `1.2203` → IC=+0.238 (n=3090)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2203 (IC base=+0.234)

- **PATRÓN** `volumen_regimen` > `0.6419` → IC=+0.238 (n=3090)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6419 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2365` → IC=+0.253 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2365 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.4852` → IC=+0.251 (n=1005)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4852 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=4014)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2104.4014` → IC=+0.234 (n=3090)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2104.4014 (IC base=+0.234)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.259 (n=1061)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.242 (n=2995)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.5188` → IC=+0.268 (n=3176)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5188 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.252` → IC=+0.277 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.252 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` > `1.2206` → IC=+0.260 (n=1059)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2206 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2835` → IC=+0.299 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2835 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `1.813` → IC=+0.233 (n=1982)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.813 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `1.4305` → IC=+0.237 (n=2972)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4305 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.234 (n=2891)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.236)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.199 (n=5409)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.247 (n=1875)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.3937` → IC=+0.223 (n=4940)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3937 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=2057)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.9369` → IC=+0.253 (n=1872)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9369 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `0.1711` → IC=+0.217 (n=2118)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1711 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` < `0.4272` → IC=+0.219 (n=4047)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4272 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.624` → IC=+0.222 (n=1837)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.624 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.592` → IC=+0.216 (n=4995)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.592 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` < `0.7054` → IC=+0.228 (n=1814)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7054 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` < `0.1063` → IC=+0.217 (n=5245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1063 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.1657` → IC=+0.222 (n=1585)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1657 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `1.454` → IC=+0.223 (n=1843)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.454 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.222 (n=4353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `3701.6132` → IC=+0.224 (n=3742)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3701.6132 (IC base=+0.216)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.237 (n=1362)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.4873` → IC=+0.213 (n=4070)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4873 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=1377)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.215 (n=1800)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` < `0.7333` → IC=+0.204 (n=4070)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7333 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` > `0.6561` → IC=+0.208 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6561 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` < `0.238` → IC=+0.194 (n=3738)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.238 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.806` → IC=+0.207 (n=3649)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.806 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `1.0952` → IC=+0.204 (n=3407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0952 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` < `0.0983` → IC=+0.200 (n=3742)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0983 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.0741` → IC=+0.200 (n=1815)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0741 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `1.5361` → IC=+0.202 (n=1764)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5361 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `2.1944` → IC=+0.204 (n=1818)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1944 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.199 (n=5409)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.215 (n=1780)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.197)

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

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.228)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.008` → IC=+0.219 (n=1534)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.1458` → IC=+0.220 (n=674)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1458 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.227 (n=554)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` < `0.5044` → IC=+0.219 (n=1022)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5044 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.865` → IC=+0.208 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.865 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.4035` → IC=+0.216 (n=1536)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4035 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.104` → IC=+0.214 (n=1391)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.104 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `1.0529` → IC=+0.208 (n=1348)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0529 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` < `0.105` → IC=+0.208 (n=1414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.105 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `2.4588` → IC=+0.212 (n=1501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4588 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=1586)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.008` → IC=+0.208 (n=1249)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.3829` → IC=+0.219 (n=1098)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3829 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.204 (n=482)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.205 (n=836)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.3985` → IC=+0.201 (n=832)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3985 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `0.0884` → IC=+0.197 (n=1248)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.0884 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.6371` → IC=+0.208 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6371 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` < `0.2254` → IC=+0.194 (n=1214)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.2254 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.229` → IC=+0.196 (n=586)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 3.229 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.748` → IC=+0.195 (n=1276)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 6.748 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `0.6375` → IC=+0.232 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6375 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.0756` → IC=+0.224 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0756 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `2.2019` → IC=+0.197 (n=1076)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.2019 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.5263` → IC=+0.198 (n=409)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.5263 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `4977.4624` → IC=+0.198 (n=1248)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 4977.4624 (IC base=+0.193)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.215 (n=566)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.217 (n=824)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.269 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` > `0.7235` → IC=+0.236 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7235 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.242` → IC=+0.220 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.242 (IC base=+0.190)

- **PATRÓN** `volumen_regimen` < `0.6337` → IC=+0.240 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6337 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` < `0.1066` → IC=+0.200 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1066 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.0795` → IC=+0.198 (n=379)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.0795 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` < `1.5721` → IC=+0.199 (n=363)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.5721 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.4925` → IC=+0.204 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4925 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.197 (n=1000)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.02 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `4265.5976` → IC=+0.233 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4265.5976 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.229 (n=282)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.3458` → IC=+0.250 (n=414)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3458 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.255 (n=434)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` < `0.7308` → IC=+0.243 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7308 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `0.4962` → IC=+0.224 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4962 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` < `0.3026` → IC=+0.217 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3026 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.823` → IC=+0.225 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.823 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` < `0.7541` → IC=+0.225 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7541 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `0.9292` → IC=+0.216 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9292 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` < `0.1072` → IC=+0.233 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1072 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `2.2063` → IC=+0.254 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2063 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `2968.4304` → IC=+0.235 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2968.4304 (IC base=+0.216)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.256 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.216)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.146 (n=842)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0042 (IC base=+0.064)

- **PATRÓN** `ibs_20min` > `0.7647` → IC=+0.198 (n=1208)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.7647 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` > `0.1457` → IC=+0.144 (n=928)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.1457 (IC base=+0.064)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.807` → IC=+0.149 (n=397)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 10.807 (IC base=+0.064)

- **PATRÓN** `ibs_20min` < `0.0455` → IC=+0.263 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0455 (IC base=+0.047)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.917` → IC=+0.167 (n=178)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.917 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.1468` → IC=+0.154 (n=313)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.1468 (IC base=+0.047)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.3596` → IC=-0.150 (n=195)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3596
  - _Potencial_: sin este filtro IC_bueno=+0.166 (n=587)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.129 (n=618)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0057 (IC base=+0.086)

- **PATRÓN** `ibs_20min` > `0.3596` → IC=+0.166 (n=587)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.3596 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.119` → IC=+0.176 (n=294)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.119 (IC base=+0.086)

- **PATRÓN** `ibs_20min` < `0.0674` → IC=+0.289 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0674 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.2135` → IC=+0.184 (n=93)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2135 (IC base=+0.056)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.139 (n=419)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.005 (IC base=+0.084)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.138 (n=307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 15.0 (IC base=+0.084)

- **PATRÓN** `ibs_20min` > `0.5536` → IC=+0.184 (n=529)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.5536 (IC base=+0.084)

- **PATRÓN** `dist_vwap_pct` > `0.1265` → IC=+0.186 (n=297)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1265 (IC base=+0.084)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.029` → IC=+0.210 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.029 (IC base=+0.084)

- **PATRÓN** `ibs_20min` < `0.0314` → IC=+0.248 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0314 (IC base=+0.016)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.617` → IC=+0.210 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.617 (IC base=+0.016)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.196 (n=218)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 1.0 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.7076` → IC=+0.133 (n=148)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.7076 (IC base=+0.024)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.982` → IC=+0.142 (n=135)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 8.982 (IC base=+0.024)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.155 (n=276)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0105 (IC base=+0.071)

- **PATRÓN** `ibs_20min` < `0.0714` → IC=+0.254 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0714 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` < `0.1754` → IC=+0.136 (n=270)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1754 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.114` → IC=+0.348 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.114 (IC base=+0.071)

- **PATRÓN** `volumen_regimen` > `1.1045` → IC=+0.191 (n=95)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 1.1045 (IC base=+0.071)

- **PATRÓN** `volumen_pendiente_norm` > `0.1522` → IC=+0.190 (n=85)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.1522 (IC base=+0.071)

- **PATRÓN** `volumen_spike_ratio` > `1.8481` → IC=+0.151 (n=173)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.8481 (IC base=+0.071)

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

- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.204 (n=201)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0077 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.201 (n=229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` > `0.6686` → IC=+0.170 (n=598)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.6686 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.5388` → IC=+0.240 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5388 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.614` → IC=+0.134 (n=329)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 3.614 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.697` → IC=+0.136 (n=440)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 2.697 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.6195` → IC=+0.178 (n=200)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.6195 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` < `0.069` → IC=+0.171 (n=426)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.069 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.396` → IC=+0.189 (n=165)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.396 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.1414` → IC=+0.126 (n=603)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.1414 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.023` → IC=+0.162 (n=199)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 9.023 (IC base=+0.042)

- **PATRÓN** `libro_liquidez` > `4894.8429` → IC=+0.123 (n=311)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 4894.8429 (IC base=+0.042)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.75` → IC=-0.154 (n=79)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
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
  - _Potencial_: sin este filtro IC_bueno=+0.172 (n=193)

- **FILTRO** `ibs_20min` > `0.1628` → IC=-0.137 (n=111)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1628
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=218)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.144 (n=133)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.004 (IC base=+0.122)

- **PATRÓN** `sigma_h` > `0.003` → IC=+0.133 (n=178)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.003 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.1024` → IC=+0.133 (n=88)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.1024 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.200 (n=68)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.8015` → IC=+0.161 (n=178)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.8015 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` < `0.0953` → IC=+0.147 (n=165)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.0953 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.169` → IC=+0.157 (n=208)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 9.169 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.6229` → IC=+0.196 (n=67)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.6229 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1263` → IC=+0.172 (n=193)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` < 0.1263 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `2.1537` → IC=+0.167 (n=151)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.1537 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=168)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `1623.6709` → IC=+0.182 (n=199)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 1623.6709 (IC base=+0.122)

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
  - _Potencial_: sin este filtro IC_bueno=+0.319 (n=81)

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

- **PATRÓN** `drift_ventana_pct` |x|> `0.3474` → IC=+0.265 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3474 (IC base=+0.240)

- **PATRÓN** `elapsed_s` > `187.9` → IC=+0.265 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 187.9 (IC base=+0.240)

- **PATRÓN** `elapsed_s` < `216.8` → IC=+0.246 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 216.8 (IC base=+0.240)

- **PATRÓN** `drift_15min` |x|≤ `2.3607` → IC=+0.306 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3607 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.6424` → IC=+0.308 (n=50)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6424 (IC base=+0.240)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.319 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `1814.0` → IC=+0.289 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1814.0 (IC base=+0.240)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.319 (n=81)

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

- **PATRÓN** `drift_ventana_pct` |x|> `0.3474` → IC=+0.265 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3474 (IC base=+0.240)

- **PATRÓN** `elapsed_s` > `187.9` → IC=+0.265 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 187.9 (IC base=+0.240)

- **PATRÓN** `elapsed_s` < `216.8` → IC=+0.246 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 216.8 (IC base=+0.240)

- **PATRÓN** `drift_15min` |x|≤ `2.3607` → IC=+0.306 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3607 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.6424` → IC=+0.308 (n=50)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6424 (IC base=+0.240)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.319 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `1814.0` → IC=+0.289 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1814.0 (IC base=+0.240)

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
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=463)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=3738)

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
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=1462)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=1416)

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
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=982)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=982)

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
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=78)

- **FILTRO** `lag_apertura_s` > `319.98` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `lag_apertura_s` > 319.98
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=78)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.153 (n=70)

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
- **PATRÓN** `py_entrada` < `0.51` → IC=+0.159 (n=247)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` < 0.51 (IC base=+0.007)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` > `0.61` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=167)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.129 (n=130)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=506)

- **FILTRO** `profundidad_ratio` < `43.4` → IC=-0.146 (n=159)

  - _Acción_: SKIP cuando `profundidad_ratio` < 43.4
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=477)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.129 (n=251)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=277)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.125 (n=190)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=401)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` > `0.61` → IC=-0.124 (n=91)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=281)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.164 (n=6971)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=21010)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.177 (n=7017)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=21765)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.191 (n=1247)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=3896)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.179 (n=1197)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=3918)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.140 (n=1346)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 1.0 (IC base=+0.042)

- **PATRÓN** `libro_liquidez` > `1064.929` → IC=+0.138 (n=2572)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 1064.929 (IC base=+0.042)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.131 (n=2400)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.5 (IC base=+0.011)

- **PATRÓN** `libro_liquidez` > `1200.6624` → IC=+0.151 (n=1740)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1200.6624 (IC base=+0.011)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.184 (n=995)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=3083)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.204 (n=1253)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=3987)

- **PATRÓN** `ibs_20min` > `0.9655` → IC=+0.129 (n=1749)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` > 0.9655 (IC base=+0.035)

- **PATRÓN** `libro_liquidez` > `1363.3324` → IC=+0.120 (n=2572)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 1363.3324 (IC base=+0.035)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.152 (n=1267)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=3883)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2411)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=2335)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.189 (n=911)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=2842)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=3732)

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
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=947)

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
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=43019)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.296 (n=14497)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=47632)

- **FILTRO** `ibs_7min` < `0.2294` → IC=-0.231 (n=15531)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2294
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=46598)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.152 (n=20961)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=41168)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.243 (n=19312)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=58703)

- **FILTRO** `ibs_7min` > `0.2838` → IC=-0.181 (n=19498)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2838
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=58517)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.154 (n=2695)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=8268)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.316 (n=2665)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=8298)

- **FILTRO** `ibs_7min` < `0.7115` → IC=-0.249 (n=3614)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7115
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=7349)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.149 (n=2615)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=8348)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.278 (n=3214)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=10257)

- **FILTRO** `ibs_7min` > `0.7727` → IC=-0.213 (n=3366)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7727
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=10105)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.127 (n=2481)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=7933)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.261 (n=2468)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=7946)

- **FILTRO** `ibs_7min` < `0.7178` → IC=-0.204 (n=2603)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7178
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=7811)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.193 (n=2586)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=7828)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.258 (n=2642)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=7982)

- **FILTRO** `ibs_7min` > `0.2661` → IC=-0.192 (n=2655)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2661
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=7969)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.179 (n=2635)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=7989)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.162 (n=2547)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=7900)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.312 (n=2589)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=7858)

- **FILTRO** `ibs_7min` < `0.2903` → IC=-0.247 (n=3447)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2903
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=7000)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.196 (n=2298)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=8149)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.260 (n=3387)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=10920)

- **FILTRO** `ibs_7min` > `0.7333` → IC=-0.179 (n=3572)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7333
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=10735)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.123 (n=3283)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=6802)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=2434)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=7651)

- **FILTRO** `ibs_7min` < `0.7216` → IC=-0.194 (n=2521)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7216
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=7564)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.188 (n=2464)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=7621)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.262 (n=2396)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=8102)

- **FILTRO** `ibs_7min` > `0.2748` → IC=-0.173 (n=2624)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2748
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=7874)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.175 (n=2564)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=7934)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=2493)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=7592)

- **FILTRO** `ibs_7min` < `0.7111` → IC=-0.224 (n=3325)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7111
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=6760)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.221 (n=2384)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=7701)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.194 (n=3571)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=11478)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.297 (n=2488)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=7647)

- **FILTRO** `ibs_7min` < `0.1875` → IC=-0.229 (n=2532)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1875
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=7603)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.202 (n=2407)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=7728)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.224 (n=3493)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=10573)

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
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=529)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.156 (n=158)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=586)

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

- **FILTRO** `libro_liquidez` < `3272.2118` → IC=-0.156 (n=184)

  - _Acción_: SKIP cuando `libro_liquidez` < 3272.2118
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=552)

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
- **FILTRO** `sigma_h` > `0.0105` → IC=-0.180 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=47)

- **FILTRO** `pct_vs_K` |x|> `9.1619` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 9.1619
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=53)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.013` → IC=-0.243 (n=33)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.013
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=103)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.238 (n=440)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=227)

- **FILTRO** `T_h` > `79.6334` → IC=-0.214 (n=446)

  - _Acción_: SKIP cuando `T_h` > 79.6334
  - _Potencial_: sin este filtro IC_bueno=-0.155 (n=221)

- **FILTRO** `sigma_h` < `0.005` → IC=-0.238 (n=143)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=429)

- **FILTRO** `pct_vs_K` |x|> `3.2571` → IC=-0.431 (n=142)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.2571
  - _Potencial_: sin este filtro IC_bueno=-0.153 (n=430)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0072` → IC=-0.190 (n=143)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0072
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=77)

- **FILTRO** `T_h` > `69.0845` → IC=-0.205 (n=147)

  - _Acción_: SKIP cuando `T_h` > 69.0845
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=73)

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

- **FILTRO** `pct_vs_K` |x|> `3.066` → IC=-0.435 (n=60)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.066
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=118)

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
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=50)

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
- **PATRÓN** `regimen_ma_toques` > `4.0` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.053)

- **PATRÓN** `volumen_racha` < `24607.606` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_racha` < 24607.606 (IC base=+0.053)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=1046)

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
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=4327)

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
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=2456)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.189 (n=1773)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0055 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.177 (n=1343)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0124 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.1786` → IC=+0.183 (n=3549)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1786 (IC base=+0.166)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0992` → IC=+0.175 (n=1229)

  - _Acción_: Kelly boost +0.88€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0992 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.174 (n=3724)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 6.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.168 (n=3722)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 15.0 (IC base=+0.166)

- **PATRÓN** `ibs_15` > `0.5333` → IC=+0.239 (n=4033)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5333 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.1296` → IC=+0.163 (n=1960)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1296 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` < `0.3156` → IC=+0.151 (n=3254)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.3156 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.108` → IC=+0.263 (n=782)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.108 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `4570.1073` → IC=+0.182 (n=1343)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 4570.1073 (IC base=+0.166)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1626)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.223 (n=687)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.0769` → IC=+0.253 (n=302)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0769 (IC base=+0.207)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2639` → IC=+0.227 (n=229)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2639 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.227 (n=719)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.207)

- **PATRÓN** `ibs_15` > `0.7223` → IC=+0.274 (n=687)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7223 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.2377` → IC=+0.223 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2377 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.503` → IC=+0.304 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.503 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `8065.6565` → IC=+0.217 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8065.6565 (IC base=+0.207)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.160 (n=824)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0067 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.1091` → IC=+0.158 (n=550)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1091 (IC base=+0.142)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1416` → IC=+0.151 (n=549)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio_macro` |x|> 0.1416 (IC base=+0.142)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.125` → IC=+0.154 (n=330)

  - _Acción_: Kelly boost +0.77€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.125 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.151 (n=752)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 6.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.146 (n=860)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 17.0 (IC base=+0.142)

- **PATRÓN** `ibs_15` > `0.5173` → IC=+0.230 (n=825)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5173 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.1187` → IC=+0.161 (n=506)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.1187 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.208` → IC=+0.274 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.208 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `5808.0125` → IC=+0.168 (n=374)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 5808.0125 (IC base=+0.142)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `ibs_15` > `0.2239` → IC=-0.120 (n=156)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2239
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=304)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.878` → IC=+0.236 (n=327)
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
- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.385 (n=311)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1501` → IC=+0.376 (n=458)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1501 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1371` → IC=+0.384 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1371 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.375 (n=687)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.396 (n=688)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.1523` → IC=+0.383 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1523 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.219` → IC=+0.394 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.219 (IC base=+0.363)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.368 (n=832)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `3840.073` → IC=+0.373 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3840.073 (IC base=+0.363)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.363 (n=305)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.360)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.407 (n=116)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.360)

- **PATRÓN** `drift_60min` |x|≤ `0.0547` → IC=+0.364 (n=116)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0547 (IC base=+0.360)

- **PATRÓN** `drift_15min` |x|≤ `0.5204` → IC=+0.359 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5204 (IC base=+0.360)

- **PATRÓN** `delta_ratio_macro` |x|> `0.156` → IC=+0.367 (n=231)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.156 (IC base=+0.360)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1436` → IC=+0.392 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1436 (IC base=+0.360)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.378 (n=325)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.360)

- **PATRÓN** `ibs_15` > `0.8541` → IC=+0.388 (n=310)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8541 (IC base=+0.360)

- **PATRÓN** `dist_vwap_pct` > `0.3751` → IC=+0.385 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3751 (IC base=+0.360)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.244` → IC=+0.385 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.244 (IC base=+0.360)

- **PATRÓN** `libro_liquidez` > `8065.6565` → IC=+0.383 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8065.6565 (IC base=+0.360)

- **PATRÓN** `ballena_activa_n` < `499.0` → IC=+0.399 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 499.0 (IC base=+0.360)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.368 (n=340)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.366)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.377 (n=226)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.366)

- **PATRÓN** `drift_60min` |x|≤ `0.1066` → IC=+0.365 (n=227)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1066 (IC base=+0.366)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0833` → IC=+0.379 (n=303)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0833 (IC base=+0.366)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.380 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.366)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.383 (n=160)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.366)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.374 (n=157)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.366)

- **PATRÓN** `ibs_15` > `0.7604` → IC=+0.403 (n=339)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7604 (IC base=+0.366)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.372 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.366)

- **PATRÓN** `dist_vwap_pct` < `0.2918` → IC=+0.370 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2918 (IC base=+0.366)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.356` → IC=+0.403 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.356 (IC base=+0.366)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.372 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.366)

- **PATRÓN** `libro_liquidez` > `4039.5603` → IC=+0.397 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4039.5603 (IC base=+0.366)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.176 (n=2305)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=2306)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.213 (n=1809)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=2802)

- **FILTRO** `libro_liquidez` < `4254.5118` → IC=-0.154 (n=3043)

  - _Acción_: SKIP cuando `libro_liquidez` < 4254.5118
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

- **PATRÓN** `delta_ratio_macro` |x|> `0.2301` → IC=+0.271 (n=1330)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2301 (IC base=-0.011)

- **PATRÓN** `ibs_15` < `0.3679` → IC=+0.282 (n=3986)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3679 (IC base=-0.011)

- **PATRÓN** `dist_vwap_pct` > `0.8792` → IC=+0.275 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8792 (IC base=-0.011)

- **PATRÓN** `dist_vwap_pct` < `0.1655` → IC=+0.246 (n=2991)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1655 (IC base=-0.011)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0334` → IC=-0.223 (n=2151)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0334
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=719)

- **FILTRO** `sigma_h` > `0.0067` → IC=-0.211 (n=717)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=2153)

- **FILTRO** `sigma_h` < `0.0035` → IC=-0.226 (n=717)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=2153)

- **FILTRO** `sigma_ewma_delta_pct` > `23.084` → IC=-0.265 (n=411)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.084
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=2459)

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

- **PATRÓN** `sigma_ewma_delta_pct` > `19.254` → IC=+0.148 (n=245)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 19.254 (IC base=+0.086)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1053` → IC=+0.246 (n=61)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1053 (IC base=-0.191)

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

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.262 (n=507)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.244)

- **PATRÓN** `drift_60min` |x|≤ `0.3539` → IC=+0.245 (n=1338)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3539 (IC base=+0.244)

- **PATRÓN** `drift_15min` |x|≤ `0.7694` → IC=+0.256 (n=1337)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7694 (IC base=+0.244)

- **PATRÓN** `delta_ratio_macro` |x|> `0.214` → IC=+0.271 (n=689)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.214 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=561)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.247 (n=1347)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.244)

- **PATRÓN** `ibs_15` < `0.3764` → IC=+0.276 (n=1519)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3764 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` > `0.1544` → IC=+0.263 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1544 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.392` → IC=+0.252 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.392 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.457` → IC=+0.250 (n=1588)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.457 (IC base=+0.244)

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

- **FILTRO** `sigma_ewma_delta_pct` > `17.595` → IC=-0.144 (n=560)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.595
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=4466)

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

- **PATRÓN** `ibs_15` < `0.3913` → IC=+0.290 (n=678)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3913 (IC base=-0.036)

- **PATRÓN** `dist_vwap_pct` < `0.2615` → IC=+0.234 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2615 (IC base=-0.036)

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
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.290 (n=1200)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.0538` → IC=+0.318 (n=400)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0538 (IC base=+0.284)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1505` → IC=+0.285 (n=800)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1505 (IC base=+0.284)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2236` → IC=+0.297 (n=722)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2236 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.300 (n=1245)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.284)

- **PATRÓN** `ibs_15` > `0.8389` → IC=+0.315 (n=1200)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8389 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.266` → IC=+0.314 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.266 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.379` → IC=+0.384 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.379 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `11994.6281` → IC=+0.304 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11994.6281 (IC base=+0.284)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.303 (n=282)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.278)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.288 (n=291)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.278)

- **PATRÓN** `drift_60min` |x|≤ `0.0587` → IC=+0.315 (n=214)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0587 (IC base=+0.278)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2673` → IC=+0.281 (n=213)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2673 (IC base=+0.278)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3917` → IC=+0.284 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3917 (IC base=+0.278)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.298 (n=672)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.278)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.304 (n=640)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.829 (IC base=+0.278)

- **PATRÓN** `dist_vwap_pct` > `0.2516` → IC=+0.314 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2516 (IC base=+0.278)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.55` → IC=+0.378 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.55 (IC base=+0.278)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.278 (n=827)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `12681.8839` → IC=+0.304 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12681.8839 (IC base=+0.278)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.306 (n=560)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.1077` → IC=+0.314 (n=374)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1077 (IC base=+0.291)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1451` → IC=+0.295 (n=373)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1451 (IC base=+0.291)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1019` → IC=+0.340 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1019 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.307 (n=538)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.291)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.296 (n=509)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8516` → IC=+0.322 (n=560)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8516 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.2815` → IC=+0.314 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2815 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.387` → IC=+0.380 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.387 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `3469.9204` → IC=+0.291 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3469.9204 (IC base=+0.291)

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

- **FILTRO** `drift_15min` |x|> `0.3419` → IC=-0.250 (n=18)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3419
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=37)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2065` → IC=-0.259 (n=27)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2065
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=28)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5333 sube el IC de +0.166 a +0.239 en UPDOWN_GBM#15min (n=4033). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7223 sube el IC de +0.207 a +0.274 en UPDOWN_GBM#BTC#15min (n=687). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5173 sube el IC de +0.142 a +0.230 en UPDOWN_GBM#ETH#15min (n=825). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.878 sube el IC de +0.080 a +0.236 en UPDOWN_GBM#SOL#15min (n=327). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5156 sube el IC de +0.194 a +0.273 en UPDOWN_GBM#XRP#15min (n=897). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1071 sube el IC de +0.070 a +0.169 en UPDOWN_GBM#XRP#15min (n=808). Ya aplicado como kelly_boost=+0.85€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6335 sube el IC de -0.068 a +0.280 en UPDOWN_GBM_15M_TARDIO (n=1113). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3679 sube el IC de -0.011 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=3986). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7639 sube el IC de +0.086 a +0.328 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=375). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6221 sube el IC de -0.191 a +0.317 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=69). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5874 sube el IC de +0.153 a +0.247 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=556). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3764 sube el IC de +0.244 a +0.276 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1519). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.189 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3913 sube el IC de -0.036 a +0.290 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=678). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.210 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.1368 sube el IC de -0.024 a +0.312 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=611). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.103 a +0.364 en UPDOWN_GBM_ETH_15M_HORA7 (n=20). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.103 a +0.364 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=20). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8389 sube el IC de +0.284 a +0.315 en UPDOWN_GBM_IBS_ALTO (n=1200). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.278 a +0.304 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=640). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8516 sube el IC de +0.291 a +0.322 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=560). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.363 a +0.396 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=688). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8541 sube el IC de +0.360 a +0.388 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=310). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7604 sube el IC de +0.366 a +0.403 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=339). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2038 | +0.089 | +220.58€ | 0 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2038 | +0.089 | +220.58€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1646 | +0.092 | +191.85€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1646 | +0.092 | +191.85€ | 0 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 284 | +0.070 | +11.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 284 | +0.070 | +11.30€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 77 | +0.108 | +17.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 77 | +0.108 | +17.77€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 846 | -0.014 | +85.40€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 846 | -0.014 | +85.40€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 652 | -0.040 | +53.18€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 652 | -0.040 | +53.18€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 150 | +0.086 | +25.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 150 | +0.086 | +25.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 38 | +0.025 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 38 | +0.025 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 43152 | -0.083 | -5581.63€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2534 | +0.059 | -276.19€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 40618 | -0.092 | -5305.43€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4610 | -0.117 | -762.28€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4610 | -0.117 | -762.28€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2534 | +0.059 | -276.19€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2534 | +0.059 | -276.19€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4574 | -0.114 | -875.95€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4574 | -0.114 | -875.95€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 11563 | -0.023 | -1187.61€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 11563 | -0.023 | -1187.61€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 11564 | -0.118 | -1116.13€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 11564 | -0.118 | -1116.13€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8307 | -0.124 | -1363.46€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8307 | -0.124 | -1363.46€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 40634 | -0.013 | +3161.58€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 10478 | +0.004 | +1612.80€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 30156 | -0.019 | +1548.78€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 40634 | -0.013 | +3161.58€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 10478 | +0.004 | +1612.80€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 30156 | -0.019 | +1548.78€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 162248 | +0.115 | -6457.17€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 19991 | +0.181 | -660.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 728 | -0.007 | -75.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 131997 | +0.107 | -5401.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 9532 | +0.095 | -319.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 21875 | +0.107 | -1362.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 66 | -0.176 | +7.07€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 21794 | +0.108 | -1357.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 31149 | +0.126 | -487.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5421 | +0.182 | -216.63€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 21865 | +0.121 | -138.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3821 | +0.080 | -110.71€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 21929 | +0.100 | -1522.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 80 | -0.122 | -5.27€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 21834 | +0.101 | -1506.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 34563 | +0.124 | -670.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 8851 | +0.177 | -188.23€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 22183 | +0.106 | -424.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3517 | +0.101 | -49.13€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 30831 | +0.114 | -1449.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5498 | +0.198 | -263.72€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 631 | +0.023 | -21.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 22508 | +0.096 | -1003.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2194 | +0.114 | -160.13€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#XRP | 21901 | +0.107 | -963.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 75 | -0.110 | +6.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 21813 | +0.108 | -970.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 26189 | +0.195 | -1660.99€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 26189 | +0.195 | -1660.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 5934 | +0.177 | -526.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 5934 | +0.177 | -526.44€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 3526 | +0.203 | -91.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 3526 | +0.203 | -91.14€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 5859 | +0.178 | -486.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 5859 | +0.178 | -486.83€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5017 | +0.247 | -184.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5017 | +0.247 | -184.72€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 5774 | +0.186 | -385.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 5774 | +0.186 | -385.62€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1116 | +0.424 | -44.78€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1116 | +0.424 | -44.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 448 | +0.438 | -5.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 448 | +0.438 | -5.17€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 446 | +0.424 | -16.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 446 | +0.424 | -16.70€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 208 | +0.395 | -19.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 208 | +0.395 | -19.04€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 91903 | +0.201 | -6564.18€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 91903 | +0.201 | -6564.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 15812 | +0.184 | -1652.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 15812 | +0.184 | -1652.59€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 14826 | +0.225 | -490.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 14826 | +0.225 | -490.49€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 15762 | +0.181 | -1651.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 15762 | +0.181 | -1651.53€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 14944 | +0.218 | -592.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 14944 | +0.218 | -592.67€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 15238 | +0.203 | -978.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 15238 | +0.203 | -978.65€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 15321 | +0.198 | -1198.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 15321 | +0.198 | -1198.25€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 35246 | +0.117 | +282.14€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 35246 | +0.117 | +282.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 17528 | +0.119 | +205.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 17528 | +0.119 | +205.98€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 17718 | +0.115 | +76.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 17718 | +0.115 | +76.16€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2270 | +0.293 | -8.32€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2270 | +0.293 | -8.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1041 | +0.280 | -27.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1041 | +0.280 | -27.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1102 | +0.299 | +16.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1102 | +0.299 | +16.83€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 127 | +0.337 | +2.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 127 | +0.337 | +2.24€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1038 | +0.444 | +10.16€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1038 | +0.444 | +10.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 504 | +0.437 | -3.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 504 | +0.437 | -3.99€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 486 | +0.453 | +13.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 486 | +0.453 | +13.28€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 48 | +0.400 | +0.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 48 | +0.400 | +0.86€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1785 | +0.070 | -73.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 705 | +0.049 | -59.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1080 | +0.083 | -14.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1363 | +0.077 | -34.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 283 | +0.051 | -19.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1080 | +0.083 | -14.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 340 | +0.032 | -43.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 340 | +0.032 | -43.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 70483 | +0.101 | -1683.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 5684 | +0.092 | +72.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 64799 | +0.102 | -1755.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 38648 | +0.106 | -398.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 5684 | +0.092 | +72.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 32964 | +0.108 | -471.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 14718 | +0.110 | -63.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 14718 | +0.110 | -63.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 17117 | +0.083 | -1221.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 17117 | +0.083 | -1221.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 902 | +0.190 | -109.94€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 902 | +0.190 | -109.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 902 | +0.190 | -109.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 902 | +0.190 | -109.94€ | 2 | 4 |
| ✅ GBM_LATE_15M | 48118 | +0.097 | +25757.61€ | 0 | 17 |
| ✅ GBM_LATE_15M#15min | 48118 | +0.097 | +25757.61€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 7990 | +0.222 | +6780.24€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 7990 | +0.222 | +6780.24€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 7336 | +0.178 | +5715.73€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 7336 | +0.178 | +5715.73€ | 0 | 22 |
| ✅ GBM_LATE_15M#DOGE | 8620 | +0.205 | +6700.46€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 8620 | +0.205 | +6700.46€ | 0 | 19 |
| ✅ GBM_LATE_15M#ETH | 6602 | +0.048 | +1955.17€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 6602 | +0.048 | +1955.17€ | 1 | 16 |
| ✅ GBM_LATE_15M#SOL | 6730 | -0.032 | +1481.26€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 6730 | -0.032 | +1481.26€ | 3 | 13 |
| ✅ GBM_LATE_15M#XRP | 10840 | -0.028 | +3124.76€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 10840 | -0.028 | +3124.76€ | 4 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 51248 | +0.085 | +28360.86€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 51248 | +0.085 | +28360.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 9893 | +0.001 | +5014.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 9893 | +0.001 | +5014.72€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 10990 | +0.008 | +2773.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 10990 | +0.008 | +2773.03€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 7033 | +0.285 | +7734.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 7033 | +0.285 | +7734.42€ | 0 | 23 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 9497 | +0.014 | +2500.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 9497 | +0.014 | +2500.35€ | 1 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 8020 | +0.040 | +3355.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 8020 | +0.040 | +3355.83€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5815 | +0.310 | +6982.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5815 | +0.310 | +6982.50€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 38115 | +0.180 | +31191.11€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 38115 | +0.180 | +31191.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 5758 | +0.237 | +5279.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 5758 | +0.237 | +5279.89€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 5995 | +0.148 | +4518.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 5995 | +0.148 | +4518.87€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 6124 | +0.222 | +5233.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 6124 | +0.222 | +5233.18€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 6498 | +0.136 | +5051.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 6498 | +0.136 | +5051.86€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 7178 | +0.121 | +5296.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 7178 | +0.121 | +5296.94€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 6562 | +0.228 | +5810.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 6562 | +0.228 | +5810.36€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 10119 | +0.126 | +4880.12€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 10119 | +0.126 | +4880.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 455 | +0.161 | +292.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 455 | +0.161 | +292.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2923 | +0.133 | +1605.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2923 | +0.133 | +1605.68€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 481 | +0.152 | +249.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 481 | +0.152 | +249.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3048 | +0.134 | +1461.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3048 | +0.134 | +1461.06€ | 0 | 12 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2557 | +0.096 | +967.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2557 | +0.096 | +967.87€ | 1 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 655 | +0.133 | +302.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 655 | +0.133 | +302.80€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO | 48372 | +0.186 | +39162.51€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#15min | 48372 | +0.186 | +39162.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 7633 | +0.247 | +7280.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 7633 | +0.247 | +7280.59€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 7613 | +0.145 | +5342.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 7613 | +0.145 | +5342.23€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 8185 | +0.232 | +7297.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 8185 | +0.232 | +7297.45€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 7995 | +0.139 | +5736.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 7995 | +0.139 | +5736.41€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 8593 | +0.118 | +5961.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 8593 | +0.118 | +5961.40€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 8353 | +0.235 | +7544.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 8353 | +0.235 | +7544.42€ | 0 | 21 |
| ✅ GBM_LATE_5M | 12908 | +0.208 | +10349.15€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 12908 | +0.208 | +10349.15€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1038 | +0.245 | +980.84€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1038 | +0.245 | +980.84€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3038 | +0.212 | +2644.53€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3038 | +0.212 | +2644.53€ | 0 | 24 |
| ✅ GBM_LATE_5M#DOGE | 1216 | +0.197 | +905.95€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1216 | +0.197 | +905.95€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 3705 | +0.200 | +2714.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3705 | +0.200 | +2714.73€ | 0 | 26 |
| ✅ GBM_LATE_5M#SOL | 1958 | +0.202 | +1573.61€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1958 | +0.202 | +1573.61€ | 0 | 25 |
| ✅ GBM_LATE_5M#XRP | 1953 | +0.209 | +1529.48€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1953 | +0.209 | +1529.48€ | 0 | 0 |
| ✅ GBM_LATE_60M | 4123 | +0.057 | +1215.46€ | 0 | 7 |
| ✅ GBM_LATE_60M#60min | 4123 | +0.057 | +1215.46€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1481 | +0.072 | +500.12€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1481 | +0.072 | +500.12€ | 1 | 5 |
| ✅ GBM_LATE_60M#ETH | 1340 | +0.058 | +420.99€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1340 | +0.058 | +420.99€ | 0 | 7 |
| ✅ GBM_LATE_60M#SOL | 1302 | +0.039 | +294.35€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1302 | +0.039 | +294.35€ | 0 | 10 |
| 🚫 GBM_LATE_60M_FADE | 634 | -0.250 | -30.50€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 634 | -0.250 | -30.50€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 236 | -0.248 | -17.12€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 236 | -0.248 | -17.12€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 228 | -0.243 | -5.46€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 228 | -0.243 | -5.46€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 170 | -0.256 | -7.92€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 170 | -0.256 | -7.92€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1710 | +0.083 | +417.24€ | 1 | 12 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1710 | +0.083 | +417.24€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 666 | +0.078 | +156.30€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 666 | +0.078 | +156.30€ | 1 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 594 | +0.055 | +93.01€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 594 | +0.055 | +93.01€ | 2 | 13 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 450 | +0.126 | +167.92€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 450 | +0.126 | +167.92€ | 2 | 11 |
| ✅ LATE_WINDOW_5MIN | 183 | +0.273 | +178.44€ | 1 | 13 |
| ✅ LATE_WINDOW_5MIN#5min | 183 | +0.273 | +178.44€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 183 | +0.273 | +178.44€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 183 | +0.273 | +178.44€ | 1 | 13 |
| ✅ LEADLAG_BTC_XRP_15M | 3831 | +0.099 | +905.62€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3831 | +0.099 | +905.62€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3831 | +0.099 | +905.62€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3831 | +0.099 | +905.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 714 | -0.018 | -4.04€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 714 | -0.018 | -4.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 6 | -0.037 | -1.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 6 | -0.037 | -1.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 216 | -0.009 | +4.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 216 | -0.009 | +4.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 27 | -0.155 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 27 | -0.155 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 177 | +0.025 | +6.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 177 | +0.025 | +6.00€ | 2 | 1 |
| ✅ LIQUIDACIONES_15M#SOL | 236 | -0.004 | +1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 236 | -0.004 | +1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 3957 | +0.017 | +99.40€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3957 | +0.017 | +99.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 185 | +0.029 | -0.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 185 | +0.029 | -0.77€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 814 | +0.015 | +39.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 814 | +0.015 | +39.58€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 214 | -0.005 | -1.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 214 | -0.005 | -1.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1513 | +0.023 | +31.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1513 | +0.023 | +31.06€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 761 | +0.011 | +1.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 761 | +0.011 | +1.65€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 470 | +0.015 | +29.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 470 | +0.015 | +29.46€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1973 | -0.038 | -26.70€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1973 | -0.038 | -26.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 589 | -0.030 | -12.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 589 | -0.030 | -12.21€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 684 | -0.016 | +6.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 684 | -0.016 | +6.61€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 700 | -0.067 | -21.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 700 | -0.067 | -21.10€ | 6 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 11138 | -0.029 | -32.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 5334 | -0.034 | -59.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 5804 | -0.025 | +27.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 344 | -0.038 | -8.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 176 | -0.011 | +5.79€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 168 | -0.065 | -14.09€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 2877 | -0.019 | +36.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1367 | -0.020 | +13.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1510 | -0.017 | +22.21€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1169 | -0.024 | +19.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 596 | -0.032 | +1.19€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 573 | -0.017 | +18.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 2472 | -0.039 | -68.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1164 | -0.047 | -53.50€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1308 | -0.032 | -15.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 2151 | -0.024 | +22.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1037 | -0.029 | -0.51€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1114 | -0.018 | +23.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 2125 | -0.039 | -33.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 994 | -0.045 | -26.54€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 56763 | -0.000 | +2913.99€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 56763 | -0.000 | +2913.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 10258 | +0.027 | +1326.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 10258 | +0.027 | +1326.43€ | 2 | 4 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 8072 | -0.035 | -125.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 8072 | -0.035 | -125.30€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 10384 | +0.024 | +1067.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 10384 | +0.024 | +1067.62€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 7960 | -0.047 | -139.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 7960 | -0.047 | -139.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 9620 | -0.005 | +257.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 9620 | -0.005 | +257.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 10469 | +0.017 | +527.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 10469 | +0.017 | +527.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6861 | -0.057 | -149.72€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6861 | -0.057 | -149.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1235 | -0.002 | -17.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1235 | -0.002 | -17.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1875 | -0.071 | -37.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1875 | -0.071 | -37.10€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 63 | -0.038 | -1.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 63 | -0.038 | -1.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 789 | -0.119 | -34.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 789 | -0.119 | -34.09€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2041 | -0.070 | -33.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2041 | -0.070 | -33.60€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 140144 | -0.077 | +1808.18€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 140144 | -0.077 | +1808.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 24434 | -0.079 | +1292.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 24434 | -0.079 | +1292.76€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 21038 | -0.100 | -1009.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 21038 | -0.100 | -1009.61€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 24754 | -0.069 | +1214.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 24754 | -0.069 | +1214.60€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 20583 | -0.097 | -644.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 20583 | -0.097 | -644.99€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 25134 | -0.057 | +305.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 25134 | -0.057 | +305.21€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 24201 | -0.069 | +650.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 24201 | -0.069 | +650.21€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8906 | -0.035 | -182.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8906 | -0.035 | -182.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1002 | -0.017 | -19.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1002 | -0.017 | -19.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2050 | -0.047 | -28.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2050 | -0.047 | -28.91€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2614 | -0.026 | -40.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2614 | -0.026 | -40.42€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1235 | -0.059 | -30.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1235 | -0.059 | -30.19€ | 4 | 0 |
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
| ✅ ORDER_FLOW_5M_REACTIVO | 1731 | -0.017 | -23.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1731 | -0.017 | -23.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 330 | -0.003 | +6.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 330 | -0.003 | +6.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 312 | -0.032 | -8.58€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 312 | -0.032 | -8.58€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 437 | -0.047 | -34.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 437 | -0.047 | -34.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 363 | +0.007 | +5.16€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 363 | +0.007 | +5.16€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 289 | -0.002 | +8.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 289 | -0.002 | +8.87€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 999 | -0.074 | -48.57€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 463 | -0.109 | -79.28€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 361 | -0.134 | -65.20€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 102 | -0.019 | -14.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 350 | -0.034 | +23.81€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 252 | -0.024 | +27.39€ | 2 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 98 | -0.060 | -3.59€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 186 | -0.064 | +6.91€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 154 | -0.070 | +3.03€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 32 | -0.029 | +3.88€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 767 | -0.085 | -34.78€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 232 | -0.038 | -13.79€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1239 | -0.208 | -79.67€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 484 | -0.210 | -48.32€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 426 | -0.213 | -47.58€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 58 | -0.183 | -0.74€ | 1 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 418 | -0.212 | -36.30€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 369 | -0.222 | -42.80€ | 3 | 1 |
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
| ✅ STREAK_FADE_60M | 105 | -0.051 | -9.57€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 105 | -0.051 | -9.57€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 43 | -0.100 | -5.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 43 | -0.100 | -5.07€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 62 | -0.016 | -4.50€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 62 | -0.016 | -4.50€ | 0 | 2 |
| ✅ STREAK_MOM_5M | 11335 | +0.015 | +74.14€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11335 | +0.015 | +74.14€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2908 | +0.018 | +24.16€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2908 | +0.018 | +24.16€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2942 | +0.018 | +35.73€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2942 | +0.018 | +35.73€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2907 | +0.008 | -3.40€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2907 | +0.008 | -3.40€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2578 | +0.014 | +17.65€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2578 | +0.014 | +17.65€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 10460 | +0.013 | -49.45€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 10460 | +0.013 | -49.45€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4346 | +0.019 | -3.48€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4346 | +0.019 | -3.48€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3624 | +0.010 | -29.12€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3624 | +0.010 | -29.12€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2490 | +0.008 | -16.85€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2490 | +0.008 | -16.85€ | 1 | 0 |
| ✅ UPDOWN_GBM | 86044 | +0.056 | +7758.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 20843 | +0.083 | +4492.44€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2721 | +0.003 | +32.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 57032 | +0.054 | +3142.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 5139 | +0.004 | +96.46€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 7023 | +0.093 | +1137.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1576 | +0.156 | +698.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5370 | +0.076 | +440.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 19666 | +0.057 | +1705.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2857 | +0.085 | +664.82€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 758 | +0.005 | +14.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 13625 | +0.064 | +955.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2315 | +0.002 | +68.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 111 | -0.075 | +1.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 9094 | +0.071 | +952.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1555 | +0.147 | +610.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 7461 | +0.055 | +343.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 20430 | +0.047 | +1378.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 5095 | +0.072 | +786.36€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 729 | +0.007 | +18.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 12642 | +0.046 | +553.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1860 | +0.006 | +18.62€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 104 | -0.104 | +1.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 18674 | +0.036 | +1001.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 5337 | +0.035 | +424.83€ | 0 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 691 | -0.009 | +2.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 11590 | +0.042 | +572.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 964 | +0.005 | +9.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 92 | -0.138 | -7.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 11155 | +0.069 | +1585.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4423 | +0.104 | +1307.40€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 6344 | +0.048 | +277.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 307 | -0.105 | -3.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 914 | +0.363 | +327.50€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 914 | +0.363 | +327.50€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 462 | +0.360 | +155.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 462 | +0.360 | +155.87€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 452 | +0.366 | +171.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 452 | +0.366 | +171.63€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 21350 | -0.023 | +5065.67€ | 3 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 21350 | -0.023 | +5065.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3983 | -0.114 | +151.90€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3983 | -0.114 | +151.90€ | 4 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2766 | +0.220 | +1784.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2766 | +0.220 | +1784.08€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 6088 | -0.063 | +801.91€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 6088 | -0.063 | +801.91€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5847 | -0.064 | +1054.51€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5847 | -0.064 | +1054.51€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 260 | +0.065 | +27.24€ | 0 | 8 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 260 | +0.065 | +27.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 260 | +0.065 | +27.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 260 | +0.065 | +27.24€ | 0 | 8 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1599 | +0.284 | +1325.78€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1599 | +0.284 | +1325.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 853 | +0.278 | +661.51€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 853 | +0.278 | +661.51€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 746 | +0.291 | +664.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 746 | +0.291 | +664.27€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 842 | -0.114 | -84.99€ | 4 | 0 |
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
  - _Estado_: 753 celda(s) pasan gate riguroso completo de 2778 evaluadas (n>=40) y 3852 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.036 < 0.08 — monitorear
  - _Datos_: n=5336 IC=+0.036 PNL=+425.34€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.140 n=884/60 | contraria IC=+0.187 n=913 | gap=-0.047 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

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
  - _Estado_: ETH#60min: n=1858/40 IC=+0.006 PNL=+18.66€ | BTC#60min: n=2313/40 IC=+0.002 PNL=+68.85€ | SOL#60min: n=964/40 IC=+0.005 PNL=+9.03€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.047 n=623085 | tras_1loss IC=+0.097 n=472867 | tras_2loss IC=+0.067 n=190492/40 | gap=-0.020 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.159 > 0.08 con n=965 PNL=+525.02€
  - _Datos_: n=965 IC=+0.159 PNL=+525.02€

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
  - _Estado_: n=3457 IC=+0.006 PNL=+4.79€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3457 IC=+0.006 PNL=+4.79€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1678 IC=+0.000 PNL=+91.74€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1678 IC=+0.000 PNL=+91.74€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.166 > 0.1 con n=5369 PNL=+3153.25€
  - _Datos_: n=5369 IC=+0.166 PNL=+3153.25€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=2853 IC=+0.085 PNL=+664.27€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=2853 IC=+0.085 PNL=+664.27€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.273 n=183) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=183 IC=+0.273 PNL=+178.44€

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
  - _Estado_: n=34398 IC=+0.073 PNL=+4851.81€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=34398 IC=+0.073 PNL=+4851.81€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.135 < -0.1 con n=604 PNL=+86.01€
  - _Datos_: n=604 IC=-0.135 PNL=+86.01€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.109 > 0.1 con n=922 PNL=+251.33€
  - _Datos_: n=922 IC=+0.109 PNL=+251.33€

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
  - _Estado_: n=36660 IC=-0.135 PNL=+2663.37€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=36660 IC=-0.135 PNL=+2663.37€

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
  - _Estado_: n=3763 IC=+0.130 PNL=+2408.60€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=3763 IC=+0.130 PNL=+2408.60€

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
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.220 < -0.1 con n=3876 PNL=-313.40€
  - _Datos_: n=3876 IC=-0.220 PNL=-313.40€

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.099 n=1939) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1939 IC=+0.099 PNL=+408.24€

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
  - _Estado_: n=15804 IC=+0.184 PNL=-1653.94€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=15804 IC=+0.184 PNL=-1653.94€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.232 > 0.1 con n=252 PNL=+176.71€
  - _Datos_: n=252 IC=+0.232 PNL=+176.71€
