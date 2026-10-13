# Hipótesis automáticas — 2026-10-13 21:34 UTC
_Generado por shadow_postmortem.py sobre 885138 resoluciones (PNL=+112943.94€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.236 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.128)

- **PATRÓN** `n_total_lado` > `68.0` → IC=+0.195 (n=254)

  - _Acción_: Kelly boost +0.98€ cuando `n_total_lado` > 68.0 (IC base=+0.128)

- **PATRÓN** `banda_hit_calibrado` > `0.6274` → IC=+0.260 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6274 (IC base=+0.128)

- **PATRÓN** `banda_z` > `9.53` → IC=+0.211 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.53 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.174 (n=253)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=794)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.128)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.233 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.134)

- **PATRÓN** `n_total_lado` > `73.0` → IC=+0.211 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 73.0 (IC base=+0.134)

- **PATRÓN** `banda_hit_calibrado` > `0.6167` → IC=+0.253 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6167 (IC base=+0.134)

- **PATRÓN** `banda_z` > `9.998` → IC=+0.223 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.998 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=639)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=696)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.134)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.355` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `py_entrada` < 0.355
  - _Potencial_: sin este filtro IC_bueno=+0.234 (n=107)

- **FILTRO** `banda_hit_calibrado` < `0.8019` → IC=-0.146 (n=46)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.8019
  - _Potencial_: sin este filtro IC_bueno=+0.255 (n=96)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.184 (n=115)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.353 (n=32)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=98)

- **PATRÓN** `py_entrada` > `0.355` → IC=+0.234 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.355 (IC base=+0.125)

- **PATRÓN** `banda_hit_calibrado` > `0.8019` → IC=+0.255 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8019 (IC base=+0.125)

- **PATRÓN** `banda_z` > `7.17` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `banda_z` > 7.17 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.128 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 4.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.136 (n=97)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 14.0 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.184 (n=115)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `906.0197` → IC=+0.170 (n=107)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 906.0197 (IC base=+0.125)

### BALLENAS_CONFIRMADAS_15M#XRP#15min
- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `n_ballena_banda` > 26.0 (IC base=+0.154)

- **PATRÓN** `n_total_lado` > `38.0` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 38.0 (IC base=+0.154)

- **PATRÓN** `banda_z` > `2.517` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 2.517 (IC base=+0.154)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.705` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `ballenas_wallet_edge_medio` > 0.705 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.224 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `2518.5859` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2518.5859 (IC base=+0.154)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `144.06` → IC=-0.206 (n=9315)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.06
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=27946)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `130.76` → IC=-0.265 (n=1107)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.76
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3322)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `122.47` → IC=-0.300 (n=1030)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.47
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=3092)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `167.13` → IC=-0.219 (n=2423)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 167.13
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=7269)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `132.38` → IC=-0.292 (n=1803)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.38
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=5411)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.209 (n=19721)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=4123)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `9345.8788` → IC=+0.178 (n=1848)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 9345.8788 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.133 (n=16666)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=20031)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 7.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.228 (n=15381)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=6836)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `7308.1777` → IC=+0.159 (n=2631)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 7308.1777 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=1968)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.197 (n=1923)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` > `0.775` → IC=+0.364 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.775 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.197 (n=2414)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `16191.7122` → IC=+0.209 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16191.7122 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.194 (n=1735)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 7.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.193 (n=1937)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 17.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.187)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.189 (n=2480)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `16076.7957` → IC=+0.196 (n=639)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 16076.7957 (IC base=+0.187)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.170 (n=440)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.61 (IC base=+0.086)

- **PATRÓN** `libro_liquidez` > `6900.0098` → IC=+0.169 (n=119)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 6900.0098 (IC base=+0.086)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.135 (n=1039)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.44 (IC base=+0.085)

- **PATRÓN** `libro_liquidez` > `5856.6213` → IC=+0.124 (n=240)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 5856.6213 (IC base=+0.085)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=3849)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.157)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.367 (n=1268)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.224 (n=1718)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.215)

- **PATRÓN** `py_entrada` < `0.25` → IC=+0.362 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.25 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.220 (n=2002)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.215)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=962)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.146 (n=821)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 15.0 (IC base=+0.140)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.261 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=750)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `2154.4479` → IC=+0.149 (n=417)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2154.4479 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.160 (n=151)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.072)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.241 (n=906)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.408 (n=1100)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.150 (n=1266)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=667)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.148)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.285 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=834)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.148)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.175 (n=336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 7.0 (IC base=+0.162)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.350 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.153 (n=194)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.02 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `3371.7925` → IC=+0.146 (n=80)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3371.7925 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.159 (n=409)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.235 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.126)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.795` → IC=-0.329 (n=68)

  - _Acción_: SKIP cuando `py_entrada` > 0.795
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=137)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=16552)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.202 (n=14030)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.231 (n=6898)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.180 (n=3636)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.179 (n=3635)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 17.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.181 (n=3714)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.177)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.229 (n=1805)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.311 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.225)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=3786)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.184 (n=3618)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.188 (n=1425)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.73 (IC base=+0.180)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.255 (n=3297)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.246)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.350 (n=1084)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.78 (IC base=+0.246)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.246)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=3711)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.194 (n=2364)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.194 (n=2728)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.188)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.431 (n=648)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.428)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.428 (n=637)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.428)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.440 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.428)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.430 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.428)

- **PATRÓN** `libro_liquidez` > `4030.0105` → IC=+0.439 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4030.0105 (IC base=+0.428)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.434 (n=285)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.447 (n=188)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.436)

- **PATRÓN** `libro_liquidez` > `18155.0675` → IC=+0.438 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 18155.0675 (IC base=+0.436)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.444 (n=194)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.432)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.432)

- **PATRÓN** `libro_liquidez` > `3468.0377` → IC=+0.446 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3468.0377 (IC base=+0.432)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.404 (n=133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.402)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.403 (n=132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.402)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.412 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.402)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=24)

- **FILTRO** `libro_liquidez` < `6345.2155` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 6345.2155
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=14)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=21330)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.246 (n=21661)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.201)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.192 (n=3175)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 18.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.188 (n=6797)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 12.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.201 (n=9510)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.185)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.226 (n=4461)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.228 (n=4340)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.285 (n=3132)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.188 (n=3650)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.179 (n=6787)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 12.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.194 (n=9075)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=4493)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.223 (n=3394)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.277 (n=3068)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.206 (n=8203)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.203 (n=8115)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.261 (n=3214)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=3544)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.198 (n=3563)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=3722)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=7691)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` < `4.21` → IC=+0.124 (n=7073)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` < 4.21 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=7538)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.125 (n=9323)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.43` → IC=+0.139 (n=7062)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.43 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=3805)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.143 (n=3805)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.95 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.132 (n=4624)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 7.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `2.86` → IC=+0.146 (n=3504)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.86 (IC base=+0.120)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.190 (n=3886)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.134 (n=4124)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.137 (n=3551)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.25 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.300 (n=1529)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.292)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.294 (n=1510)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.380 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `4306.2044` → IC=+0.297 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4306.2044 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.290 (n=690)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.283)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.285 (n=593)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.283)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.355 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `5376.6669` → IC=+0.296 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5376.6669 (IC base=+0.283)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.320 (n=492)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.291)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.296 (n=725)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.291)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.387 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.291)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.291 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `1714.5953` → IC=+0.300 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1714.5953 (IC base=+0.291)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.447 (n=708)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.443)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.442 (n=586)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.443 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.443)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.451 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.443)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.444 (n=796)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.443)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.444 (n=337)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.440)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.442 (n=292)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.440 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.448 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.440)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.465 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.447)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.453 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.447)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.447 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.447)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.448 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.447)

- **PATRÓN** `libro_liquidez` > `2084.3627` → IC=+0.462 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2084.3627 (IC base=+0.447)

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
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=86)

- **FILTRO** `py_entrada` > `0.735` → IC=-0.365 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=72)

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
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=86)

- **FILTRO** `py_entrada` > `0.735` → IC=-0.365 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=72)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4774` → IC=+0.133 (n=11898)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.4774 (IC base=+0.116)

- **PATRÓN** `ibs_20min` > `0.9836` → IC=+0.244 (n=3966)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9836 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` > `0.7769` → IC=+0.261 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7769 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` < `0.3744` → IC=+0.254 (n=3207)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3744 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.971` → IC=+0.185 (n=4488)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 5.971 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `1.2089` → IC=+0.252 (n=3384)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2089 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` > `0.6177` → IC=+0.258 (n=3383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6177 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.3021` → IC=+0.234 (n=1197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3021 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` > `2.3416` → IC=+0.223 (n=3810)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3416 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.5669` → IC=+0.142 (n=14602)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5669 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.5823` → IC=+0.187 (n=1020)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.5823 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.1504` → IC=+0.187 (n=5107)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.1504 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `1.1934` → IC=+0.182 (n=5545)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.1934 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.0529` → IC=+0.182 (n=2514)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.0529 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2953` → IC=+0.231 (n=1390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2953 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.6801` → IC=+0.211 (n=3153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6801 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `111.0` → IC=+0.220 (n=9299)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 111.0 (IC base=+0.074)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.215 (n=879)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.3476` → IC=+0.194 (n=2619)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.3476 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.202 (n=1273)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.193 (n=1748)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `0.9736` → IC=+0.273 (n=1187)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9736 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.088` → IC=+0.276 (n=1129)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.088 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.240 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `2.2724` → IC=+0.204 (n=1128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2724 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.203 (n=2742)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `2097.85` → IC=+0.211 (n=873)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2097.85 (IC base=+0.189)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.203 (n=1521)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.237 (n=1443)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.233)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.240 (n=978)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.0876` → IC=+0.263 (n=720)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0876 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.257 (n=784)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.5085` → IC=+0.255 (n=2157)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5085 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.256` → IC=+0.234 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.256 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` < `0.0942` → IC=+0.237 (n=1912)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0942 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.2867` → IC=+0.252 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2867 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.4408` → IC=+0.231 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4408 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.6484` → IC=+0.250 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6484 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=2377)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `1596.68` → IC=+0.245 (n=2157)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1596.68 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.233 (n=736)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.233)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.234 (n=933)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.223)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.223 (n=961)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.106` → IC=+0.258 (n=934)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.106 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.234 (n=2118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.224 (n=2161)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.9678` → IC=+0.268 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9678 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` > `0.1301` → IC=+0.227 (n=1191)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1301 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.469` → IC=+0.258 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.469 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `1.2468` → IC=+0.225 (n=2118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2468 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `0.6213` → IC=+0.229 (n=2117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6213 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.2765` → IC=+0.248 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2765 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `1.5137` → IC=+0.223 (n=917)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5137 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `2.4379` → IC=+0.250 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4379 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `12045.4998` → IC=+0.223 (n=1891)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12045.4998 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.184 (n=716)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0026 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0741` → IC=+0.175 (n=712)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0741 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=816)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.5867` → IC=+0.184 (n=1877)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.5867 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1289` → IC=+0.158 (n=1943)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1289 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.179` → IC=+0.155 (n=346)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 11.179 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.252` → IC=+0.144 (n=1951)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.252 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.1913` → IC=+0.146 (n=2133)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.1913 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.0964` → IC=+0.165 (n=781)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0964 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.4576` → IC=+0.146 (n=2015)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4576 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.4228` → IC=+0.143 (n=2015)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.4228 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `223.0` → IC=+0.174 (n=855)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 223.0 (IC base=+0.137)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.212 (n=901)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=2838)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.194 (n=2410)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.269 (n=1037)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.343` → IC=+0.261 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.343 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.194 (n=2377)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.35` → IC=+0.212 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.35 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.1521` → IC=+0.203 (n=1737)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1521 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=3182)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `2003.547` → IC=+0.201 (n=1222)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2003.547 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.225 (n=2101)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.1763` → IC=+0.229 (n=1050)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1763 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.250 (n=898)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.218 (n=1098)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.0711` → IC=+0.236 (n=1050)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0711 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.551` → IC=+0.258 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.551 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3459` → IC=+0.254 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3459 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `1.724` → IC=+0.218 (n=991)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.724 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.724` → IC=+0.231 (n=1022)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.724 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `2076.9484` → IC=+0.232 (n=795)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2076.9484 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.220 (n=2191)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.143 (n=138)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=3229)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.158 (n=492)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0035 (IC base=+0.051)

- **PATRÓN** `ibs_20min` > `0.9581` → IC=+0.221 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9581 (IC base=+0.051)

- **PATRÓN** `dist_vwap_pct` < `0.1865` → IC=+0.332 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1865 (IC base=+0.051)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.069` → IC=+0.183 (n=1048)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 5.069 (IC base=+0.051)

- **PATRÓN** `volumen_regimen` < `0.8538` → IC=+0.332 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8538 (IC base=+0.051)

- **PATRÓN** `volumen_regimen` > `1.2365` → IC=+0.349 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2365 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` < `0.1776` → IC=+0.323 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1776 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.2965` → IC=+0.345 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2965 (IC base=+0.051)

- **PATRÓN** `volumen_spike_ratio` < `1.4113` → IC=+0.351 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4113 (IC base=+0.051)

- **PATRÓN** `volumen_spike_ratio` > `2.2172` → IC=+0.326 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2172 (IC base=+0.051)

- **PATRÓN** `ballena_activa_n` < `149.0` → IC=+0.333 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 149.0 (IC base=+0.051)

- **PATRÓN** `ibs_20min` < `0.0956` → IC=+0.168 (n=842)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.0956 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` > `0.6662` → IC=+0.162 (n=214)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.6662 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` < `0.1285` → IC=+0.139 (n=1282)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1285 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` < `0.8497` → IC=+0.146 (n=955)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.8497 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` > `0.2875` → IC=+0.208 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2875 (IC base=+0.033)

- **PATRÓN** `volumen_spike_ratio` > `1.5177` → IC=+0.154 (n=1224)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5177 (IC base=+0.033)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.181 (n=89)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=498)

- **FILTRO** `ibs_20min` < `0.2909` → IC=-0.196 (n=146)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2909
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=441)

- **FILTRO** `ibs_20min` > `0.2222` → IC=-0.131 (n=3218)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2222
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=1606)

- **FILTRO** `sigma_ewma_delta_pct` > `8.658` → IC=-0.228 (n=497)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.658
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=4327)

- **PATRÓN** `ibs_20min` > `0.7913` → IC=+0.183 (n=200)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.7913 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` > `1.012` → IC=+0.283 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.012 (IC base=+0.031)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.257` → IC=+0.167 (n=67)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.257 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` < `0.8709` → IC=+0.256 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8709 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` > `1.0006` → IC=+0.300 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0006 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` < `0.1553` → IC=+0.268 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1553 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` < `2.1915` → IC=+0.283 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1915 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` > `1.5489` → IC=+0.257 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5489 (IC base=+0.031)

- **PATRÓN** `ibs_20min` < `0.2222` → IC=+0.150 (n=1606)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.2222 (IC base=-0.037)

- **PATRÓN** `dist_vwap_pct` > `0.2615` → IC=+0.275 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2615 (IC base=-0.037)

- **PATRÓN** `volumen_regimen` < `0.7096` → IC=+0.286 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7096 (IC base=-0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.0793` → IC=+0.303 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0793 (IC base=-0.037)

- **PATRÓN** `volumen_spike_ratio` < `2.3831` → IC=+0.297 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3831 (IC base=-0.037)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6309` → IC=-0.181 (n=850)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6309
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=2554)

- **FILTRO** `ibs_20min` < `0.725` → IC=-0.153 (n=2246)

  - _Acción_: SKIP cuando `ibs_20min` < 0.725
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=1158)

- **FILTRO** `ibs_20min` > `0.76` → IC=-0.203 (n=1253)

  - _Acción_: SKIP cuando `ibs_20min` > 0.76
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=3781)

- **PATRÓN** `dist_vwap_pct` > `0.4517` → IC=+0.323 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4517 (IC base=-0.073)

- **PATRÓN** `dist_vwap_pct` < `0.2719` → IC=+0.296 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2719 (IC base=-0.073)

- **PATRÓN** `volumen_regimen` > `0.704` → IC=+0.309 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.704 (IC base=-0.073)

- **PATRÓN** `volumen_pendiente_norm` < `0.1043` → IC=+0.298 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1043 (IC base=-0.073)

- **PATRÓN** `volumen_spike_ratio` < `1.5875` → IC=+0.308 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5875 (IC base=-0.073)

- **PATRÓN** `volumen_spike_ratio` > `1.8711` → IC=+0.299 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8711 (IC base=-0.073)

- **PATRÓN** `dist_vwap_pct` > `0.8102` → IC=+0.280 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8102 (IC base=-0.008)

- **PATRÓN** `volumen_regimen` > `1.0811` → IC=+0.283 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0811 (IC base=-0.008)

- **PATRÓN** `volumen_pendiente_norm` > `0.1044` → IC=+0.283 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1044 (IC base=-0.008)

- **PATRÓN** `volumen_spike_ratio` < `2.1851` → IC=+0.260 (n=1065)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1851 (IC base=-0.008)

- **PATRÓN** `volumen_spike_ratio` > `1.4311` → IC=+0.264 (n=1210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4311 (IC base=-0.008)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.204 (n=5237)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.8863` → IC=+0.276 (n=7114)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8863 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.9512` → IC=+0.292 (n=1202)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9512 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.646` → IC=+0.156 (n=7023)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.646 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` < `1.1749` → IC=+0.254 (n=5767)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1749 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` > `0.6888` → IC=+0.261 (n=5151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6888 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.2399` → IC=+0.270 (n=1716)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2399 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` > `2.6391` → IC=+0.265 (n=3082)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6391 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.285 (n=8795)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.097)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.162 (n=5039)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.009 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.5377` → IC=+0.160 (n=13295)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.5377 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.2383` → IC=+0.259 (n=4574)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2383 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.1951` → IC=+0.264 (n=1567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1951 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.313 (n=976)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `1.5849` → IC=+0.284 (n=2921)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5849 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.2745` → IC=+0.279 (n=3009)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2745 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.288 (n=6548)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 78.0 (IC base=+0.075)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.3699` → IC=-0.163 (n=1431)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3699
  - _Potencial_: sin este filtro IC_bueno=+0.132 (n=2906)

- **FILTRO** `ibs_20min` > `0.7516` → IC=-0.197 (n=896)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7516
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=2691)

- **FILTRO** `sigma_ewma_delta_pct` > `4.554` → IC=-0.193 (n=782)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.554
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=2805)

- **PATRÓN** `ibs_20min` > `0.9137` → IC=+0.293 (n=1085)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9137 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.142` → IC=+0.208 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.142 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.2294` → IC=+0.293 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2294 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `1.4484` → IC=+0.224 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4484 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` > `2.2386` → IC=+0.258 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2386 (IC base=+0.035)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.260 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.035)

- **PATRÓN** `ibs_20min` < `0.1593` → IC=+0.156 (n=898)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.1593 (IC base=-0.028)

- **PATRÓN** `volumen_pendiente_norm` < `0.2231` → IC=+0.411 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2231 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` < `2.4877` → IC=+0.409 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4877 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` > `1.5212` → IC=+0.405 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5212 (IC base=-0.028)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.411 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=-0.028)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1138` → IC=+0.203 (n=808)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1138 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `0.6802` → IC=+0.190 (n=1358)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 0.6802 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.2738` → IC=+0.223 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2738 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.4247` → IC=+0.203 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4247 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` > `2.4786` → IC=+0.195 (n=499)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.4786 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `222.0` → IC=+0.228 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 222.0 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.1506` → IC=+0.232 (n=960)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1506 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` > `0.621` → IC=+0.235 (n=945)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.621 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` < `0.0739` → IC=+0.228 (n=818)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0739 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2715` → IC=+0.305 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2715 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.5529` → IC=+0.235 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5529 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1853` → IC=+0.253 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1853 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.291 (n=1551)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0084 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.265 (n=2331)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.259)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.260 (n=2083)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.305 (n=1211)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.692` → IC=+0.288 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.692 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` < `0.1318` → IC=+0.270 (n=2131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1318 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `1.6119` → IC=+0.265 (n=2239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6119 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.271 (n=2732)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1990.0184` → IC=+0.282 (n=1055)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1990.0184 (IC base=+0.259)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.330 (n=899)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.1806` → IC=+0.307 (n=870)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1806 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.327 (n=760)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.291)

- **PATRÓN** `ibs_20min` < `0.3636` → IC=+0.293 (n=1978)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3636 (IC base=+0.291)

- **PATRÓN** `ibs_20min` > `0.1075` → IC=+0.293 (n=1318)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1075 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.722` → IC=+0.306 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.722 (IC base=+0.291)

- **PATRÓN** `volumen_pendiente_norm` < `0.195` → IC=+0.289 (n=1919)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.195 (IC base=+0.291)

- **PATRÓN** `volumen_pendiente_norm` > `0.3387` → IC=+0.306 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3387 (IC base=+0.291)

- **PATRÓN** `volumen_spike_ratio` < `1.7177` → IC=+0.303 (n=827)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7177 (IC base=+0.291)

- **PATRÓN** `volumen_spike_ratio` > `2.6391` → IC=+0.300 (n=852)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6391 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `2071.5956` → IC=+0.314 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2071.5956 (IC base=+0.291)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.292 (n=1627)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 32.0 (IC base=+0.291)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7487` → IC=-0.183 (n=929)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7487
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=2791)

- **PATRÓN** `ibs_20min` > `0.89` → IC=+0.171 (n=872)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.89 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.3683` → IC=+0.227 (n=1143)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3683 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` < `1.0152` → IC=+0.239 (n=1050)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0152 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.1022` → IC=+0.243 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1022 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `1.3995` → IC=+0.253 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3995 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `108.0` → IC=+0.259 (n=1032)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 108.0 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.1886` → IC=+0.223 (n=771)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1886 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` < `1.0374` → IC=+0.233 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0374 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` < `0.1029` → IC=+0.238 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1029 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.287 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.8189` → IC=+0.264 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8189 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.468` → IC=+0.257 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.468 (IC base=-0.001)

- **PATRÓN** `ballena_activa_n` < `129.0` → IC=+0.255 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 129.0 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7636` → IC=-0.199 (n=1660)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7636
  - _Potencial_: sin este filtro IC_bueno=+0.295 (n=1660)

- **FILTRO** `ibs_20min` > `0.6552` → IC=-0.232 (n=825)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6552
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=2479)

- **FILTRO** `sigma_ewma_delta_pct` > `8.58` → IC=-0.231 (n=374)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.58
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=2930)

- **PATRÓN** `ibs_20min` > `0.7636` → IC=+0.295 (n=1660)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7636 (IC base=+0.048)

- **PATRÓN** `dist_vwap_pct` > `0.213` → IC=+0.329 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.213 (IC base=+0.048)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.607` → IC=+0.169 (n=517)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.607 (IC base=+0.048)

- **PATRÓN** `volumen_regimen` < `0.8488` → IC=+0.324 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8488 (IC base=+0.048)

- **PATRÓN** `volumen_regimen` > `0.6318` → IC=+0.314 (n=1258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6318 (IC base=+0.048)

- **PATRÓN** `volumen_pendiente_norm` < `0.0993` → IC=+0.311 (n=1186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0993 (IC base=+0.048)

- **PATRÓN** `volumen_pendiente_norm` > `0.2747` → IC=+0.342 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2747 (IC base=+0.048)

- **PATRÓN** `volumen_spike_ratio` < `1.4432` → IC=+0.334 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4432 (IC base=+0.048)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.338 (n=830)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.048)

- **PATRÓN** `ibs_20min` < `0.5556` → IC=+0.139 (n=2192)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.5556 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.2075` → IC=+0.241 (n=945)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2075 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` < `0.7056` → IC=+0.258 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7056 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` > `1.1866` → IC=+0.232 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1866 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` < `0.2185` → IC=+0.240 (n=1181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2185 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.0737` → IC=+0.244 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0737 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `2.4243` → IC=+0.251 (n=1003)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4243 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.267 (n=1012)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 53.0 (IC base=+0.029)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.340 (n=1606)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.294)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.311 (n=854)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.294)

- **PATRÓN** `ibs_20min` > `0.6511` → IC=+0.326 (n=1797)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6511 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` > `0.2148` → IC=+0.325 (n=1030)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2148 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.776` → IC=+0.316 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.776 (IC base=+0.294)

- **PATRÓN** `volumen_regimen` > `0.6263` → IC=+0.305 (n=1797)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6263 (IC base=+0.294)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.341 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.294)

- **PATRÓN** `volumen_spike_ratio` > `1.4313` → IC=+0.306 (n=1720)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4313 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `2476.5668` → IC=+0.308 (n=1606)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2476.5668 (IC base=+0.294)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.329 (n=1533)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.294)

- **PATRÓN** `sigma_h` > `0.015` → IC=+0.329 (n=1270)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.015 (IC base=+0.296)

- **PATRÓN** `drift_60min` |x|≤ `0.1875` → IC=+0.298 (n=839)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1875 (IC base=+0.296)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.305 (n=955)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.296)

- **PATRÓN** `ibs_20min` < `0.3676` → IC=+0.322 (n=1904)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3676 (IC base=+0.296)

- **PATRÓN** `dist_vwap_pct` > `0.3069` → IC=+0.297 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3069 (IC base=+0.296)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.522` → IC=+0.305 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.522 (IC base=+0.296)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.01` → IC=+0.297 (n=2270)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.01 (IC base=+0.296)

- **PATRÓN** `volumen_regimen` < `0.7189` → IC=+0.297 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7189 (IC base=+0.296)

- **PATRÓN** `volumen_regimen` > `1.2298` → IC=+0.326 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2298 (IC base=+0.296)

- **PATRÓN** `volumen_pendiente_norm` > `0.2334` → IC=+0.348 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2334 (IC base=+0.296)

- **PATRÓN** `volumen_spike_ratio` < `1.4177` → IC=+0.303 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4177 (IC base=+0.296)

- **PATRÓN** `volumen_spike_ratio` > `2.1415` → IC=+0.299 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1415 (IC base=+0.296)

- **PATRÓN** `libro_liquidez` > `2437.8819` → IC=+0.303 (n=1701)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2437.8819 (IC base=+0.296)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.186 (n=3864)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0047 (IC base=+0.178)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.218 (n=3858)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.3471` → IC=+0.187 (n=10180)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3471 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=12051)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `0.5614` → IC=+0.230 (n=11568)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5614 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `0.1674` → IC=+0.206 (n=4846)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1674 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.36` → IC=+0.254 (n=2290)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.36 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `1.1981` → IC=+0.168 (n=7680)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1981 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` > `0.6261` → IC=+0.162 (n=7680)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6261 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2937` → IC=+0.200 (n=1695)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2937 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` < `1.4509` → IC=+0.176 (n=3732)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.4509 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `2.6045` → IC=+0.186 (n=3733)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6045 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `2017.3302` → IC=+0.183 (n=10334)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2017.3302 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.194 (n=10478)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 99.0 (IC base=+0.178)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.188 (n=7398)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0067 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.0799` → IC=+0.226 (n=3698)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0799 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=4170)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` < `0.4951` → IC=+0.236 (n=11088)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4951 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.163` → IC=+0.198 (n=1834)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 10.163 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `1.1817` → IC=+0.166 (n=7924)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1817 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.2919` → IC=+0.227 (n=1629)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2919 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.626` → IC=+0.187 (n=3453)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.626 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `67.0` → IC=+0.196 (n=8845)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 67.0 (IC base=+0.179)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.234 (n=648)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.206)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.235 (n=647)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.334` → IC=+0.224 (n=1940)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.334 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.211 (n=2044)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.212 (n=1301)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `0.9205` → IC=+0.288 (n=1293)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9205 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.153` → IC=+0.329 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.153 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.2806` → IC=+0.265 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2806 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `1.5416` → IC=+0.208 (n=1633)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5416 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.217 (n=2050)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `2099.48` → IC=+0.218 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2099.48 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.243 (n=1000)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.243)

- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.243 (n=500)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0077 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.0691` → IC=+0.300 (n=502)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0691 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.246 (n=1358)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.249 (n=732)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.243)

- **PATRÓN** `ibs_20min` < `0.2692` → IC=+0.266 (n=1320)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2692 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` < `0.1001` → IC=+0.244 (n=1296)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1001 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` > `0.2954` → IC=+0.279 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2954 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` < `1.4284` → IC=+0.260 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4284 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` > `2.6765` → IC=+0.251 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6765 (IC base=+0.243)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.247 (n=1657)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.243)

- **PATRÓN** `libro_liquidez` > `1582.26` → IC=+0.255 (n=1500)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1582.26 (IC base=+0.243)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.249 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.243)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.218 (n=583)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.1622` → IC=+0.184 (n=1163)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1622 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.173 (n=1837)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.3558` → IC=+0.221 (n=1743)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3558 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.1371` → IC=+0.212 (n=1091)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1371 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.482` → IC=+0.225 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.482 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `0.6892` → IC=+0.167 (n=767)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.6892 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` > `1.0731` → IC=+0.157 (n=790)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.0731 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.183 (n=276)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `1.5142` → IC=+0.174 (n=750)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.5142 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `2.4993` → IC=+0.158 (n=568)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.4993 (IC base=+0.155)

- **PATRÓN** `ballena_activa_n` < `424.0` → IC=+0.160 (n=1664)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 424.0 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.168 (n=1823)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0057 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.2319` → IC=+0.178 (n=1602)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2319 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.190 (n=697)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.6054` → IC=+0.206 (n=1820)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6054 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.665` → IC=+0.203 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.665 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.2025` → IC=+0.166 (n=1820)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2025 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` < `0.0712` → IC=+0.148 (n=1453)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.0712 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.153 (n=557)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.4965` → IC=+0.154 (n=1702)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4965 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.7795` → IC=+0.151 (n=1134)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.7795 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `234.0` → IC=+0.174 (n=722)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 234.0 (IC base=+0.148)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.232 (n=885)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0105 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.4018` → IC=+0.222 (n=1716)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4018 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.215 (n=2031)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=1017)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.494` → IC=+0.290 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.494 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3512` → IC=+0.227 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3512 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.7724` → IC=+0.214 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7724 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.6914` → IC=+0.223 (n=854)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6914 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.217 (n=2297)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `1991.8648` → IC=+0.222 (n=884)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1991.8648 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.247 (n=1466)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0101 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.1423` → IC=+0.267 (n=733)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1423 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.284 (n=642)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.3543` → IC=+0.252 (n=1665)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3543 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.643` → IC=+0.273 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.643 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.3508` → IC=+0.275 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3508 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.7209` → IC=+0.244 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7209 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.7264` → IC=+0.244 (n=718)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7264 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2072.7575` → IC=+0.249 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2072.7575 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.229 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.234)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.175 (n=1868)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0073 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.4054` → IC=+0.167 (n=1866)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.4054 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=1942)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.3146` → IC=+0.209 (n=1866)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3146 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.1399` → IC=+0.194 (n=1183)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1399 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.995` → IC=+0.202 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.995 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.8534` → IC=+0.163 (n=1244)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8534 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.1017` → IC=+0.176 (n=770)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1017 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `1.4249` → IC=+0.159 (n=610)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4249 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `2.5068` → IC=+0.168 (n=610)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.5068 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `4763.2061` → IC=+0.196 (n=1244)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 4763.2061 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `144.0` → IC=+0.161 (n=1802)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 144.0 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.158 (n=1960)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.007 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.3873` → IC=+0.148 (n=1959)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3873 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=740)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.6805` → IC=+0.189 (n=1958)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6805 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.152` → IC=+0.158 (n=1931)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.152 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.889` → IC=+0.157 (n=691)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 6.889 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.162 (n=1306)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.856 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2969` → IC=+0.198 (n=296)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2969 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.8063` → IC=+0.134 (n=1217)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.8063 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `1.4194` → IC=+0.133 (n=1825)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.4194 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `4463.5371` → IC=+0.172 (n=1305)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4463.5371 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `60.0` → IC=+0.146 (n=605)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 60.0 (IC base=+0.129)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.128 (n=705)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0059 (IC base=+0.126)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.166 (n=958)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.01 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.5681` → IC=+0.127 (n=2113)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.5681 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.141 (n=2161)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.4915` → IC=+0.214 (n=2113)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4915 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.1958` → IC=+0.190 (n=1262)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1958 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.71` → IC=+0.265 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.71 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `1.1893` → IC=+0.141 (n=2113)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.1893 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` < `0.161` → IC=+0.135 (n=2139)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.161 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.4387` → IC=+0.144 (n=683)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4387 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.126 (n=2194)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `2867.7686` → IC=+0.211 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2867.7686 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.155 (n=676)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 21.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.144 (n=1892)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0092 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1069` → IC=+0.170 (n=717)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1069 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=2181)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.5897` → IC=+0.219 (n=2149)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5897 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.1983` → IC=+0.150 (n=1992)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1983 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.536` → IC=+0.130 (n=436)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 7.536 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.536` → IC=+0.123 (n=1897)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` < 2.536 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.1776` → IC=+0.132 (n=2149)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1776 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1652` → IC=+0.123 (n=2062)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1652 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2744` → IC=+0.152 (n=280)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.2744 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4537` → IC=+0.135 (n=664)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.4537 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `2.4253` → IC=+0.130 (n=663)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.4253 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2719.7776` → IC=+0.191 (n=974)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2719.7776 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.130 (n=1970)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 51.0 (IC base=+0.120)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.240 (n=1751)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0127 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.2828` → IC=+0.225 (n=1307)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2828 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.220 (n=2036)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.221 (n=1766)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.6533` → IC=+0.253 (n=1959)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6533 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `0.193` → IC=+0.223 (n=1300)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.193 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.578` → IC=+0.246 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.578 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` < `1.0253` → IC=+0.218 (n=1724)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0253 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `0.6195` → IC=+0.224 (n=1959)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6195 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.2835` → IC=+0.266 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2835 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `2.4718` → IC=+0.223 (n=1906)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4718 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `1.8101` → IC=+0.229 (n=1271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8101 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `2649.2154` → IC=+0.228 (n=1306)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2649.2154 (IC base=+0.216)

- **PATRÓN** `sigma_h` < `0.0122` → IC=+0.236 (n=880)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0122 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.0224` → IC=+0.233 (n=907)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0224 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.0901` → IC=+0.256 (n=667)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0901 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.246 (n=976)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` < `0.425` → IC=+0.256 (n=2001)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.425 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `1.1573` → IC=+0.236 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1573 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.365` → IC=+0.249 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.365 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `0.6417` → IC=+0.236 (n=1998)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6417 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.285 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.4377` → IC=+0.229 (n=1851)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4377 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `2413.7909` → IC=+0.233 (n=1785)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2413.7909 (IC base=+0.227)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.208 (n=997)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.173)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.176 (n=994)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0085 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.3355` → IC=+0.184 (n=2622)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.3355 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.207 (n=1482)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.4918` → IC=+0.209 (n=2662)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4918 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.783` → IC=+0.193 (n=463)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.783 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.69` → IC=+0.202 (n=1276)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.69 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `0.8641` → IC=+0.192 (n=1776)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.8641 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.6955` → IC=+0.177 (n=2380)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.6955 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.1015` → IC=+0.186 (n=1074)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1015 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `1.4359` → IC=+0.193 (n=966)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4359 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.5192` → IC=+0.177 (n=965)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.5192 (IC base=+0.173)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.177 (n=3387)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.02 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `2760.8656` → IC=+0.179 (n=2662)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2760.8656 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.186 (n=2761)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 152.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.144 (n=1032)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0036 (IC base=+0.101)

- **PATRÓN** `ibs_20min` < `0.3677` → IC=+0.162 (n=2063)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.3677 (IC base=+0.101)

- **PATRÓN** `volumen_spike_ratio` < `1.433` → IC=+0.130 (n=1003)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.433 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `4301.7166` → IC=+0.127 (n=2063)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 4301.7166 (IC base=+0.101)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.134 (n=1298)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 29.0 (IC base=+0.101)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.208 (n=375)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.0998` → IC=+0.216 (n=375)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0998 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.194 (n=776)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 8.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.6473` → IC=+0.219 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6473 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.305` → IC=+0.190 (n=269)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.305 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.146` → IC=+0.190 (n=362)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.146 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.835` → IC=+0.164 (n=903)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 6.835 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `0.8755` → IC=+0.191 (n=568)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.8755 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.0712` → IC=+0.174 (n=335)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.0712 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `2.2167` → IC=+0.173 (n=733)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 2.2167 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `1.4165` → IC=+0.166 (n=833)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.4165 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `14845.767` → IC=+0.177 (n=567)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 14845.767 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `154.0` → IC=+0.198 (n=362)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 154.0 (IC base=+0.164)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.194 (n=334)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0027 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.3402` → IC=+0.144 (n=986)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3402 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.140 (n=888)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 7.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.6292` → IC=+0.171 (n=868)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.6292 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.715` → IC=+0.139 (n=189)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 8.715 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.158` → IC=+0.133 (n=895)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 3.158 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` > `1.0616` → IC=+0.155 (n=447)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.0616 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.1002` → IC=+0.175 (n=343)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1002 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `2.1142` → IC=+0.143 (n=857)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.1142 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=1278)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `300.0` → IC=+0.151 (n=840)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 300.0 (IC base=+0.130)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.245 (n=618)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.2023` → IC=+0.225 (n=616)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2023 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.224 (n=970)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.6782` → IC=+0.267 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6782 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.3577` → IC=+0.221 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3577 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` < `0.207` → IC=+0.212 (n=831)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.207 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.951` → IC=+0.227 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.951 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` < `0.8392` → IC=+0.212 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8392 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `1.182` → IC=+0.226 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.182 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.1596` → IC=+0.240 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1596 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `1.4123` → IC=+0.245 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4123 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.4427` → IC=+0.226 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4427 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.129 (n=402)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0038 (IC base=+0.083)

- **PATRÓN** `ibs_20min` < `0.0976` → IC=+0.171 (n=305)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.0976 (IC base=+0.083)

- **PATRÓN** `libro_liquidez` > `3960.0517` → IC=+0.120 (n=817)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 3960.0517 (IC base=+0.083)

- **PATRÓN** `ballena_activa_n` < `63.0` → IC=+0.121 (n=584)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 63.0 (IC base=+0.083)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.150 (n=700)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0106 (IC base=+0.149)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.152 (n=317)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0093 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.178 (n=628)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 8.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.266 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.97` → IC=+0.233 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.97 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.219` → IC=+0.213 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.219 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `1.0604` → IC=+0.168 (n=616)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.0604 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` > `0.7219` → IC=+0.157 (n=625)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.7219 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.173 (n=102)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `1.4569` → IC=+0.156 (n=225)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.4569 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `2.1893` → IC=+0.159 (n=306)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.1893 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.154 (n=727)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.02 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `3079.1777` → IC=+0.194 (n=233)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 3079.1777 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.148 (n=618)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.5 (IC base=+0.061)

- **PATRÓN** `volumen_spike_ratio` < `1.5674` → IC=+0.120 (n=293)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_spike_ratio` < 1.5674 (IC base=+0.061)

- **PATRÓN** `libro_liquidez` > `2790.5115` → IC=+0.156 (n=315)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2790.5115 (IC base=+0.061)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.140 (n=429)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 22.0 (IC base=+0.061)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0238` → IC=+0.170 (n=192)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0238 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.186 (n=192)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.007 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.3919` → IC=+0.167 (n=169)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3919 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.181 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 16.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.204 (n=86)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.5556` → IC=+0.184 (n=172)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.5556 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.2393` → IC=+0.167 (n=106)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.2393 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `1.115` → IC=+0.162 (n=214)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 1.115 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.385` → IC=+0.181 (n=164)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 3.385 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `0.6182` → IC=+0.175 (n=192)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6182 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` < `0.2537` → IC=+0.184 (n=188)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.2537 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.4483` → IC=+0.241 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4483 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `2.6132` → IC=+0.172 (n=56)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.6132 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.183 (n=197)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `2503.8283` → IC=+0.169 (n=128)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2503.8283 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.158 (n=191)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0117 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.163 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.61` → IC=+0.134 (n=214)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.61 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `1.1597` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1597 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.009` → IC=+0.146 (n=80)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 3.009 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` > `1.2382` → IC=+0.144 (n=71)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.2382 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.174 (n=41)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.115)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.138 (n=172)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 17.0 (IC base=+0.115)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.180 (n=5018)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0046 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.220 (n=5017)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=15736)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.5584` → IC=+0.238 (n=13443)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5584 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.1633` → IC=+0.192 (n=5538)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1633 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.354` → IC=+0.251 (n=3685)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.354 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `1.2261` → IC=+0.168 (n=10079)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2261 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.2909` → IC=+0.203 (n=2003)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2909 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.6094` → IC=+0.196 (n=4869)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6094 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `1832.7008` → IC=+0.185 (n=15048)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 1832.7008 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `118.0` → IC=+0.200 (n=13697)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 118.0 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.194 (n=5982)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0053 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.3801` → IC=+0.192 (n=11961)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.3801 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=5086)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.5765` → IC=+0.243 (n=13593)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5765 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` < `0.1751` → IC=+0.172 (n=8130)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1751 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.935` → IC=+0.210 (n=1902)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.935 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.673` → IC=+0.190 (n=13122)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 3.673 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `1.06` → IC=+0.161 (n=8083)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.06 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.2896` → IC=+0.251 (n=1832)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2896 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.6131` → IC=+0.200 (n=4265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6131 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `1768.765` → IC=+0.188 (n=13592)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 1768.765 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.214 (n=8422)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.188)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.239 (n=828)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.215)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.246 (n=828)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.3486` → IC=+0.219 (n=2472)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3486 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.229 (n=1199)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.219 (n=1657)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `0.9639` → IC=+0.317 (n=1121)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9639 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.684` → IC=+0.349 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.684 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.2778` → IC=+0.278 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2778 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `2.2647` → IC=+0.231 (n=1073)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2647 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.232 (n=2572)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `2018.1736` → IC=+0.232 (n=1121)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2018.1736 (IC base=+0.215)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.232 (n=1424)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.215)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.263 (n=2080)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.2021` → IC=+0.272 (n=1388)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2021 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.266 (n=1899)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.4947` → IC=+0.284 (n=2080)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4947 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.456` → IC=+0.263 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.456 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` < `0.0947` → IC=+0.258 (n=1850)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0947 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.2835` → IC=+0.282 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2835 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `2.2759` → IC=+0.272 (n=890)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2759 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.261 (n=2300)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1595.2` → IC=+0.269 (n=2080)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1595.2 (IC base=+0.259)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.260 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.259)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.200 (n=814)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1762` → IC=+0.163 (n=1616)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1762 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=2540)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.2643` → IC=+0.207 (n=2425)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2643 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1248` → IC=+0.192 (n=1322)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1248 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.703` → IC=+0.165 (n=401)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.703 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.181` → IC=+0.156 (n=2218)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.181 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.6288` → IC=+0.173 (n=809)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6288 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.0712` → IC=+0.154 (n=2163)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0712 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2706` → IC=+0.174 (n=345)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2706 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1761` → IC=+0.160 (n=2081)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1761 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.5289` → IC=+0.154 (n=2113)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5289 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `268.0` → IC=+0.181 (n=1014)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 268.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.196 (n=672)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0026 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0775` → IC=+0.189 (n=673)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0775 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=765)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.3041` → IC=+0.242 (n=1343)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3041 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1328` → IC=+0.170 (n=1847)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1328 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.289` → IC=+0.162 (n=338)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.289 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.1835` → IC=+0.158 (n=2014)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1835 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.154` → IC=+0.196 (n=538)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.154 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.4321` → IC=+0.152 (n=1910)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4321 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.7807` → IC=+0.163 (n=1273)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.7807 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `252.0` → IC=+0.151 (n=612)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 252.0 (IC base=+0.147)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.249 (n=835)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.228 (n=2621)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2234)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=936)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.391` → IC=+0.312 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.391 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.224 (n=2200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.6929` → IC=+0.238 (n=1097)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6929 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.230 (n=2941)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1864.29` → IC=+0.235 (n=1665)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1864.29 (IC base=+0.221)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.247 (n=2051)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.241)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.244 (n=2086)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.1797` → IC=+0.259 (n=1025)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1797 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.268 (n=881)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.0222` → IC=+0.302 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0222 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.074` → IC=+0.290 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.074 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.3428` → IC=+0.294 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3428 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.723` → IC=+0.240 (n=969)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.723 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.13` → IC=+0.248 (n=1468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.13 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `2073.5784` → IC=+0.264 (n=776)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2073.5784 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.262 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.241)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.202 (n=1139)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.4176` → IC=+0.158 (n=2576)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4176 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=2687)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.2572` → IC=+0.193 (n=2576)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.2572 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.5571` → IC=+0.175 (n=672)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.5571 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.181` → IC=+0.163 (n=1043)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 4.181 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.8719` → IC=+0.167 (n=1719)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8719 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2831` → IC=+0.184 (n=340)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2831 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.5221` → IC=+0.172 (n=1106)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5221 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.1748` → IC=+0.159 (n=1139)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.1748 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `7016.877` → IC=+0.238 (n=1168)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7016.877 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.175 (n=1089)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 78.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.190 (n=713)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0032 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.4332` → IC=+0.143 (n=2116)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.4332 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.158 (n=776)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.7398` → IC=+0.188 (n=2116)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.7398 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.1474` → IC=+0.146 (n=1877)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1474 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.273` → IC=+0.172 (n=324)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 11.273 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.8737` → IC=+0.142 (n=1411)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.8737 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.2971` → IC=+0.232 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2971 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `1.4321` → IC=+0.141 (n=2031)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4321 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `5227.3609` → IC=+0.202 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5227.3609 (IC base=+0.131)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.144 (n=1734)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0081 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=953)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.4483` → IC=+0.197 (n=2602)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.4483 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `1.0538` → IC=+0.206 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0538 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.916` → IC=+0.264 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.916 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `0.8869` → IC=+0.148 (n=1734)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8869 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` < `0.0985` → IC=+0.125 (n=2446)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.0985 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2796` → IC=+0.135 (n=338)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.2796 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `2.4762` → IC=+0.123 (n=2537)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.4762 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `1.4643` → IC=+0.126 (n=2537)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.4643 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.128 (n=2656)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2890.5622` → IC=+0.250 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2890.5622 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.135 (n=842)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 26.0 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.143 (n=2478)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0109 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1331` → IC=+0.163 (n=826)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1331 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=2554)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.215 (n=2482)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.2158` → IC=+0.139 (n=2089)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.2158 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.389` → IC=+0.134 (n=2388)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 3.389 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.7128` → IC=+0.142 (n=1090)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.7128 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2236` → IC=+0.169 (n=415)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2236 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4381` → IC=+0.151 (n=769)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4381 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2731.4412` → IC=+0.211 (n=826)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2731.4412 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.140 (n=2016)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 48.0 (IC base=+0.120)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0135` → IC=+0.242 (n=2216)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0135 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.227 (n=2593)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.231 (n=1788)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.6038` → IC=+0.268 (n=2219)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6038 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` > `0.2021` → IC=+0.241 (n=1379)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2021 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.721` → IC=+0.269 (n=836)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.721 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `1.2312` → IC=+0.228 (n=2480)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2312 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `0.6399` → IC=+0.226 (n=2480)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6399 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.2363` → IC=+0.248 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2363 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `2.5155` → IC=+0.249 (n=803)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5155 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.225 (n=3214)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `2659.8294` → IC=+0.236 (n=1653)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2659.8294 (IC base=+0.223)

- **PATRÓN** `sigma_h` > `0.0228` → IC=+0.246 (n=1169)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0228 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.234 (n=2429)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` < `0.51` → IC=+0.264 (n=2586)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.51 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.201` → IC=+0.257 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.201 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `1.232` → IC=+0.255 (n=860)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.232 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2822` → IC=+0.299 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2822 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.4358` → IC=+0.230 (n=2385)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4358 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2424.6542` → IC=+0.228 (n=2304)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2424.6542 (IC base=+0.226)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.220 (n=2328)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.226)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.186 (n=4548)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.239 (n=1533)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.504` → IC=+0.208 (n=4597)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.504 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=1648)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.200 (n=2107)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` > `0.9405` → IC=+0.245 (n=1533)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9405 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.1725` → IC=+0.202 (n=1757)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1725 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.4364` → IC=+0.207 (n=3281)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4364 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.157` → IC=+0.212 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.157 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.654` → IC=+0.200 (n=4105)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.654 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `0.7053` → IC=+0.214 (n=1474)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7053 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` > `0.8872` → IC=+0.204 (n=2233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8872 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.1666` → IC=+0.220 (n=1282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1666 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `1.4551` → IC=+0.207 (n=1510)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4551 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `1.8435` → IC=+0.201 (n=3019)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8435 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=3546)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `2599.0182` → IC=+0.206 (n=4597)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2599.0182 (IC base=+0.199)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.232 (n=1145)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.184)

- **PATRÓN** `drift_60min` |x|≤ `0.4924` → IC=+0.200 (n=3423)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4924 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=1158)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.201 (n=1528)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` < `0.18` → IC=+0.199 (n=1508)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.18 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` > `0.6764` → IC=+0.194 (n=596)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.6764 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` < `0.2396` → IC=+0.181 (n=3082)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.2396 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.129` → IC=+0.191 (n=3433)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 6.129 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` < `1.0988` → IC=+0.194 (n=2842)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 1.0988 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.189 (n=3127)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` < `1.5322` → IC=+0.190 (n=1486)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.5322 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `1.8118` → IC=+0.191 (n=2251)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 1.8118 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.186 (n=4548)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.184)

- **PATRÓN** `ballena_activa_n` < `68.0` → IC=+0.198 (n=2233)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 68.0 (IC base=+0.184)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.259 (n=553)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.0876` → IC=+0.269 (n=210)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0876 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.245 (n=629)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.235 (n=281)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.5007` → IC=+0.258 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5007 (IC base=+0.233)

- **PATRÓN** `dist_vwap_pct` < `0.3521` → IC=+0.247 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3521 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.143` → IC=+0.235 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.143 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.615` → IC=+0.236 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.615 (IC base=+0.233)

- **PATRÓN** `volumen_regimen` < `1.2183` → IC=+0.241 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2183 (IC base=+0.233)

- **PATRÓN** `volumen_regimen` > `0.8658` → IC=+0.251 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8658 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.2943` → IC=+0.338 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2943 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.8412` → IC=+0.243 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8412 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.5651` → IC=+0.235 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5651 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `12403.5268` → IC=+0.253 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12403.5268 (IC base=+0.233)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.243 (n=515)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.3693` → IC=+0.175 (n=1168)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3693 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=430)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.190 (n=434)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 5.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` < `0.1485` → IC=+0.186 (n=514)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.1485 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.6084` → IC=+0.169 (n=530)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.6084 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.6916` → IC=+0.205 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6916 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` < `0.1586` → IC=+0.163 (n=1144)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1586 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.385` → IC=+0.181 (n=1152)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 6.385 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `0.8855` → IC=+0.198 (n=779)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.8855 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.0681` → IC=+0.181 (n=538)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.0681 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.409` → IC=+0.172 (n=388)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.409 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `1.804` → IC=+0.179 (n=776)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.804 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `11371.3164` → IC=+0.175 (n=1168)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 11371.3164 (IC base=+0.163)

- **PATRÓN** `ballena_activa_n` < `701.0` → IC=+0.175 (n=1125)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 701.0 (IC base=+0.163)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.201 (n=232)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.172)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.185 (n=316)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0098 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.5794` → IC=+0.180 (n=696)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.5794 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.235 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.51` → IC=+0.217 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.51 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` < `0.3521` → IC=+0.172 (n=834)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` < 0.3521 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.2084` → IC=+0.226 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2084 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `3.3854` → IC=+0.184 (n=232)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 3.3854 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `2525.266` → IC=+0.217 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2525.266 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.229 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.275 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `2.0` → IC=+0.267 (n=58)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 2.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.2121` → IC=+0.263 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2121 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.442` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.442 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` < `0.2021` → IC=+0.250 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2021 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `2.4518` → IC=+0.250 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4518 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.861` → IC=+0.250 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.861 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `2407.5596` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2407.5596 (IC base=+0.227)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.229 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.227)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0079` → IC=+0.215 (n=1321)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0079 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.4612` → IC=+0.207 (n=1321)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4612 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.219 (n=482)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` < `0.5155` → IC=+0.217 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5155 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `0.8779` → IC=+0.204 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8779 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.178` → IC=+0.208 (n=1192)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.178 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `0.882` → IC=+0.202 (n=881)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.882 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `1.2372` → IC=+0.211 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2372 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.204 (n=1216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.1645` → IC=+0.203 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1645 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `1.4176` → IC=+0.224 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4176 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=1348)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.246 (n=356)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.4905` → IC=+0.205 (n=1066)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4905 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.199 (n=420)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.188 (n=757)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 11.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` < `0.7503` → IC=+0.186 (n=1066)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.7503 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.0847` → IC=+0.183 (n=1066)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.0847 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.6564` → IC=+0.194 (n=191)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.6564 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.355` → IC=+0.187 (n=964)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 4.355 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.2441` → IC=+0.194 (n=1066)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 1.2441 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.0737` → IC=+0.197 (n=450)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.0737 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `2.1797` → IC=+0.192 (n=919)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.1797 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `7173.1135` → IC=+0.194 (n=1066)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 7173.1135 (IC base=+0.180)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.220 (n=452)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0086 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.206 (n=641)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.9259` → IC=+0.248 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9259 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.7483` → IC=+0.241 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7483 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.204` → IC=+0.213 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.204 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `0.6991` → IC=+0.233 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6991 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` < `0.1072` → IC=+0.184 (n=612)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.1072 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.0799` → IC=+0.199 (n=300)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.0799 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `1.5574` → IC=+0.185 (n=290)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.5574 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.4567` → IC=+0.213 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4567 (IC base=+0.179)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.185 (n=785)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `3112.065` → IC=+0.196 (n=604)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 3112.065 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.196 (n=660)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 53.0 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.206 (n=441)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.3655` → IC=+0.240 (n=329)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3655 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.229 (n=334)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` < `0.72` → IC=+0.219 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.72 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.5261` → IC=+0.216 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5261 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` < `0.3111` → IC=+0.208 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3111 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.947` → IC=+0.214 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.947 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.926` → IC=+0.206 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.926 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `0.7544` → IC=+0.212 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7544 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `0.9331` → IC=+0.204 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9331 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` < `0.1072` → IC=+0.232 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1072 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `2.5787` → IC=+0.228 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5787 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `3008.5906` → IC=+0.221 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3008.5906 (IC base=+0.201)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.238 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 47.0 (IC base=+0.201)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.159 (n=655)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0038 (IC base=+0.074)

- **PATRÓN** `ibs_20min` > `0.4079` → IC=+0.149 (n=1393)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.4079 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.3572` → IC=+0.152 (n=504)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.3572 (IC base=+0.074)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.422` → IC=+0.183 (n=307)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 11.422 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.277` → IC=+0.158 (n=188)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.277 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.1837` → IC=+0.264 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1837 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` < `0.0939` → IC=+0.137 (n=661)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.0939 (IC base=+0.065)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.626` → IC=+0.158 (n=112)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 10.626 (IC base=+0.065)

- **PATRÓN** `volumen_pendiente_norm` > `0.147` → IC=+0.209 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.147 (IC base=+0.065)

- **PATRÓN** `volumen_spike_ratio` < `2.5975` → IC=+0.125 (n=624)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.5975 (IC base=+0.065)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.136 (n=504)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0056 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.143 (n=169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 18.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.5412` → IC=+0.198 (n=422)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.5412 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.156 (n=251)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.549` → IC=+0.122 (n=268)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` > 3.549 (IC base=+0.094)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.127 (n=226)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0035 (IC base=+0.080)

- **PATRÓN** `ibs_20min` < `0.5593` → IC=+0.194 (n=276)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.5593 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` < `0.2051` → IC=+0.133 (n=344)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.2051 (IC base=+0.080)

- **PATRÓN** `volumen_regimen` < `1.1836` → IC=+0.120 (n=314)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` < 1.1836 (IC base=+0.080)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.169 (n=128)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.080)

- **PATRÓN** `volumen_spike_ratio` < `2.5247` → IC=+0.125 (n=291)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.5247 (IC base=+0.080)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.153 (n=324)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0046 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.131 (n=456)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 7.0 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.6598` → IC=+0.208 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6598 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.1242` → IC=+0.187 (n=244)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1242 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.499` → IC=+0.255 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.499 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` < `0.8145` → IC=+0.133 (n=303)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.8145 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` < `1.7834` → IC=+0.124 (n=267)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.7834 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `1760.3207` → IC=+0.171 (n=150)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 1760.3207 (IC base=+0.097)

- **PATRÓN** `ibs_20min` < `0.0162` → IC=+0.322 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0162 (IC base=+0.022)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.031` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.031 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.136` → IC=+0.178 (n=57)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.136 (IC base=+0.022)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.160 (n=319)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.75 (IC base=+0.031)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.865` → IC=+0.147 (n=131)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 7.865 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.2406` → IC=+0.159 (n=89)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2406 (IC base=+0.031)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.163 (n=194)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0093 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.1176` → IC=+0.259 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1176 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.2159` → IC=+0.192 (n=37)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.2159 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` < `0.3658` → IC=+0.172 (n=178)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.3658 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.815` → IC=+0.361 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.815 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` > `1.0763` → IC=+0.237 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0763 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.1517` → IC=+0.284 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1517 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` > `2.5298` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5298 (IC base=+0.088)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.212 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.088)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1828` → IC=-0.317 (n=69)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1828
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=211)

- **FILTRO** `dist_vwap_pct` > `0.2348` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2348
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=265)

- **FILTRO** `volumen_regimen` < `0.7615` → IC=-0.333 (n=70)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7615
  - _Potencial_: sin este filtro IC_bueno=-0.164 (n=212)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.369 (n=59)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=178)

- **FILTRO** `drift_60min` |x|> `0.2042` → IC=-0.314 (n=57)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2042
  - _Potencial_: sin este filtro IC_bueno=-0.256 (n=174)

- **FILTRO** `dist_vwap_pct` > `0.4126` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4126
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=215)

- **FILTRO** `volumen_pendiente_norm` > `0.0538` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0538
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=126)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.266 (n=45)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=48)

- **FILTRO** `ibs_20min` < `0.1017` → IC=-0.250 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1017
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=63)

- **FILTRO** `volumen_regimen` < `0.8417` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8417
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=70)

- **FILTRO** `volumen_spike_ratio` > `3.5274` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.5274
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=53)

- **FILTRO** `sigma_h` < `0.002` → IC=-0.315 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.002
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=78)

- **FILTRO** `volumen_regimen` < `0.5486` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.5486
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=78)

- **FILTRO** `volumen_spike_ratio` > `1.5538` → IC=-0.333 (n=34)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.5538
  - _Potencial_: sin este filtro IC_bueno=-0.158 (n=36)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.6398` → IC=-0.439 (n=31)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6398
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=65)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.375 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=67)

- **FILTRO** `dist_vwap_pct` > `0.1189` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1189
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=62)

- **FILTRO** `volumen_spike_ratio` < `1.4507` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4507
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=39)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=59)

- **PATRÓN** `ibs_20min` > `0.9508` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.9508 (IC base=-0.163)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=77)

- **FILTRO** `volumen_spike_ratio` < `1.5847` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.5847
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=51)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=30)

- **FILTRO** `dist_vwap_pct` > `0.2956` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2956
  - _Potencial_: sin este filtro IC_bueno=-0.281 (n=30)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.165 (n=213)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0058 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.148 (n=177)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.6786` → IC=+0.146 (n=470)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.6786 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.5113` → IC=+0.189 (n=104)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.5113 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` < `0.8634` → IC=+0.133 (n=314)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.8634 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` < `0.2335` → IC=+0.133 (n=407)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.2335 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` < `2.5471` → IC=+0.135 (n=368)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.5471 (IC base=+0.105)

- **PATRÓN** `ibs_20min` < `0.156` → IC=+0.165 (n=482)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.156 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.104` → IC=+0.182 (n=168)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 9.104 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` > `0.2774` → IC=+0.135 (n=83)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.2774 (IC base=+0.070)

- **PATRÓN** `libro_liquidez` > `3150.9935` → IC=+0.148 (n=365)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3150.9935 (IC base=+0.070)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6592` → IC=-0.240 (n=48)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6592
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=144)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.218 (n=83)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.172 (n=169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 12.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.163 (n=93)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 6.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.1361` → IC=+0.198 (n=250)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.1361 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1185` → IC=+0.160 (n=266)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1185 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.253` → IC=+0.163 (n=78)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 10.253 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.678` → IC=+0.165 (n=198)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 4.678 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `0.6197` → IC=+0.157 (n=249)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.6197 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.0757` → IC=+0.170 (n=192)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.0757 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.191 (n=40)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.5308` → IC=+0.177 (n=218)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.5308 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.4429` → IC=+0.164 (n=218)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.4429 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `5212.6338` → IC=+0.155 (n=166)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 5212.6338 (IC base=+0.147)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1363` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1363
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=156)

- **FILTRO** `ibs_20min` > `0.208` → IC=-0.142 (n=93)

  - _Acción_: SKIP cuando `ibs_20min` > 0.208
  - _Potencial_: sin este filtro IC_bueno=+0.138 (n=183)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.122 (n=149)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0047 (IC base=+0.082)

- **PATRÓN** `ibs_20min` > `0.8022` → IC=+0.121 (n=151)

  - _Acción_: Kelly boost +0.60€ cuando `ibs_20min` > 0.8022 (IC base=+0.082)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.023` → IC=+0.124 (n=131)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` < 4.023 (IC base=+0.082)

- **PATRÓN** `volumen_pendiente_norm` < `0.1363` → IC=+0.120 (n=156)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_pendiente_norm` < 0.1363 (IC base=+0.082)

- **PATRÓN** `volumen_spike_ratio` < `1.7943` → IC=+0.160 (n=95)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.7943 (IC base=+0.082)

- **PATRÓN** `ibs_20min` < `0.208` → IC=+0.138 (n=183)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.208 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.059` → IC=+0.245 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.059 (IC base=+0.043)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.4444` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4444
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=92)

- **FILTRO** `dist_vwap_pct` > `0.2725` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2725
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=98)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.304 (n=105)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.273 (n=148)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.242 (n=157)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.7358` → IC=+0.246 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7358 (IC base=+0.244)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.256 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` > `0.6436` → IC=+0.381 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6436 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` < `0.2189` → IC=+0.242 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2189 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.333` → IC=+0.297 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.333 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` < `1.0021` → IC=+0.279 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0021 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` < `0.2516` → IC=+0.300 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2516 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.325 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` < `1.4907` → IC=+0.375 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4907 (IC base=+0.244)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.250 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `665.8128` → IC=+0.248 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 665.8128 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.321` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.321 (IC base=-0.081)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.314 (n=57)

- **PATRÓN** `drift_ventana_pct` |x|> `0.332` → IC=+0.300 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.332 (IC base=+0.292)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.373 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.292)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.9778` → IC=+0.354 (n=53)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9778 (IC base=+0.292)

- **PATRÓN** `ballena_activa_n` < `1127.0` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1127.0 (IC base=+0.292)

- **PATRÓN** `drift_ventana_pct` |x|> `0.356` → IC=+0.231 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.356 (IC base=+0.210)

- **PATRÓN** `elapsed_s` > `185.1` → IC=+0.211 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 185.1 (IC base=+0.210)

- **PATRÓN** `elapsed_s` < `214.9` → IC=+0.245 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 214.9 (IC base=+0.210)

- **PATRÓN** `drift_15min` |x|≤ `1.2534` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.2534 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.275 (n=38)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.210)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.314 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.259 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.210)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.314 (n=57)

- **PATRÓN** `drift_ventana_pct` |x|> `0.332` → IC=+0.300 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.332 (IC base=+0.292)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.373 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.292)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.9778` → IC=+0.354 (n=53)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9778 (IC base=+0.292)

- **PATRÓN** `ballena_activa_n` < `1127.0` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1127.0 (IC base=+0.292)

- **PATRÓN** `drift_ventana_pct` |x|> `0.356` → IC=+0.231 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.356 (IC base=+0.210)

- **PATRÓN** `elapsed_s` > `185.1` → IC=+0.211 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 185.1 (IC base=+0.210)

- **PATRÓN** `elapsed_s` < `214.9` → IC=+0.245 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 214.9 (IC base=+0.210)

- **PATRÓN** `drift_15min` |x|≤ `1.2534` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.2534 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.275 (n=38)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.210)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.314 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.259 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.210)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `libro_liquidez` > `2868.8566` → IC=+0.132 (n=530)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2868.8566 (IC base=+0.102)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2868.8566` → IC=+0.132 (n=530)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2868.8566 (IC base=+0.102)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=170)

- **FILTRO** `libro_liquidez` < `2696.1504` → IC=-0.229 (n=46)

  - _Acción_: SKIP cuando `libro_liquidez` < 2696.1504
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=140)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=246)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=232)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=62)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.149 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.188 (n=14)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=25)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.143 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` > `4.0` → IC=-0.167 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.136 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=107)

### LIQUIDACIONES_15M#XRP#15min
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
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=3185)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=100)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=57)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=89)

- **FILTRO** `ballena_activa_n` > `118.0` → IC=-0.217 (n=58)

  - _Acción_: SKIP cuando `ballena_activa_n` > 118.0
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=29)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.188 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=130)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.139 (n=217)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.495 (IC base=+0.034)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=1167)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=1121)

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
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=705)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=395)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=376)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.141 (n=154)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.495 (IC base=+0.016)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=804)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=804)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.132 (n=248)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=636)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=699)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=699)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=218)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=218)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.136 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=180)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.122 (n=88)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=145)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=179)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=203)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=247)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.121 (n=56)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=187)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=221)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=324)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=324)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=238)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.141 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=177)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.136 (n=1041)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=2665)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **PATRÓN** `py_entrada` > `0.55` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.55 (IC base=+0.071)

- **PATRÓN** `restante_min` > `9.94` → IC=+0.125 (n=46)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` > 9.94 (IC base=+0.071)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.071)

- **PATRÓN** `lag_apertura_s` < `303.82` → IC=+0.125 (n=46)

  - _Acción_: Kelly boost +0.62€ cuando `lag_apertura_s` < 303.82 (IC base=+0.071)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `restante_min` < `3.89` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `restante_min` < 3.89
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **FILTRO** `lag_apertura_s` > `66.61` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `lag_apertura_s` > 66.61
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.129 (n=243)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=130)

- **FILTRO** `profundidad_ratio` < `258.3` → IC=-0.124 (n=123)

  - _Acción_: SKIP cuando `profundidad_ratio` < 258.3
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=250)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.186 (n=116)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` < 0.46 (IC base=+0.028)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.198 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=193)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **PATRÓN** `py_entrada` < `0.5` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` < 0.5 (IC base=+0.038)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.218 (n=76)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=262)

- **FILTRO** `profundidad_ratio` < `37.0` → IC=-0.174 (n=84)

  - _Acción_: SKIP cuando `profundidad_ratio` < 37.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=254)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.263 (n=57)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=256)

- **PATRÓN** `py_entrada` < `0.46` → IC=+0.159 (n=80)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` < 0.46 (IC base=-0.030)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.123 (n=263)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=154)

- **FILTRO** `restante_min` < `3.8` → IC=-0.139 (n=206)

  - _Acción_: SKIP cuando `restante_min` < 3.8
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=211)

- **FILTRO** `lag_apertura_s` > `98.75` → IC=-0.178 (n=141)

  - _Acción_: SKIP cuando `lag_apertura_s` > 98.75
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=276)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.176 (n=69)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=262)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **PATRÓN** `py_entrada` > `0.48` → IC=+0.130 (n=133)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` > 0.48 (IC base=-0.016)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.120 (n=277)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=99)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.186 (n=100)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=364)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.166 (n=5207)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=16652)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.168 (n=5587)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=16954)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.189 (n=954)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=2972)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.163 (n=932)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=3104)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.120 (n=2441)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.5 (IC base=+0.038)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.137 (n=1036)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 1.0 (IC base=+0.038)

- **PATRÓN** `libro_liquidez` > `1420.26` → IC=+0.133 (n=1963)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 1420.26 (IC base=+0.038)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.123 (n=1869)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.5 (IC base=+0.013)

- **PATRÓN** `libro_liquidez` > `1558.4` → IC=+0.146 (n=1373)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1558.4 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.176 (n=784)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=2445)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.177 (n=966)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=3006)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.185 (n=1017)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=3090)

- **PATRÓN** `ibs_20min` > `0.9635` → IC=+0.124 (n=1352)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` > 0.9635 (IC base=+0.036)

- **PATRÓN** `libro_liquidez` > `1859.5984` → IC=+0.130 (n=1351)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 1859.5984 (IC base=+0.036)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2269)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2682)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=3422)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.172 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=416)

- **FILTRO** `ibs_20min` > `0.1742` → IC=-0.144 (n=133)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1742
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=406)

### MOMENTUM_IBS_15M_FADE#DOGE#15min
- **FILTRO** `libro_liquidez` < `2574.706` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 2574.706
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `ibs_20min` < `0.1975` → IC=-0.223 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1975
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=224)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.191 (n=121)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=293)

- **FILTRO** `drift_20min_pct` |x|> `0.1544` → IC=-0.155 (n=140)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1544
  - _Potencial_: sin este filtro IC_bueno=-0.116 (n=274)

- **FILTRO** `libro_liquidez` < `2908.728` → IC=-0.186 (n=103)

  - _Acción_: SKIP cuando `libro_liquidez` < 2908.728
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=311)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=838)

- **FILTRO** `libro_liquidez` < `2053.5963` → IC=-0.164 (n=343)

  - _Acción_: SKIP cuando `libro_liquidez` < 2053.5963
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=698)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=232)

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

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.152 (n=44)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.037)

### MOMENTUM_IBS_5M#DOGE#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=39)

### MOMENTUM_IBS_5M#ETH#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=414)

### MOMENTUM_IBS_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=631)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `8.0` → IC=-0.130 (n=15030)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=33843)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.286 (n=11826)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=37047)

- **FILTRO** `ibs_7min` < `0.2471` → IC=-0.231 (n=12218)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2471
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=36655)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.155 (n=16074)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=32799)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.237 (n=14993)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=46883)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.179 (n=15345)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=46531)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.144 (n=2423)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=6002)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.309 (n=2027)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=6398)

- **FILTRO** `ibs_7min` < `0.7097` → IC=-0.246 (n=2780)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7097
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=5645)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.173 (n=1940)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=6485)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.270 (n=2641)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=8102)

- **FILTRO** `ibs_7min` > `0.7742` → IC=-0.209 (n=2684)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7742
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=8059)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.126 (n=1983)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=6313)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.265 (n=1898)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=6398)

- **FILTRO** `ibs_7min` < `0.7323` → IC=-0.195 (n=2074)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7323
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=6222)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.189 (n=2065)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6231)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.263 (n=2041)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=6393)

- **FILTRO** `ibs_7min` > `0.2665` → IC=-0.194 (n=2107)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2665
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=6327)

- **FILTRO** `ballena_activa_n` > `148.0` → IC=-0.184 (n=2097)

  - _Acción_: SKIP cuando `ballena_activa_n` > 148.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=6337)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.159 (n=1961)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=6060)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.317 (n=1931)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=6090)

- **FILTRO** `ibs_7min` < `0.703` → IC=-0.245 (n=2645)

  - _Acción_: SKIP cuando `ibs_7min` < 0.703
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=5376)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.224 (n=1677)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=6344)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.247 (n=2600)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=8824)

- **FILTRO** `ibs_7min` > `0.7333` → IC=-0.174 (n=2854)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7333
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=8570)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.265 (n=1849)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=6151)

- **FILTRO** `ibs_7min` < `0.7339` → IC=-0.187 (n=2000)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7339
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=6000)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.192 (n=1986)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=6014)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.264 (n=2062)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=6207)

- **FILTRO** `ibs_7min` > `0.2748` → IC=-0.179 (n=2067)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2748
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=6202)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.178 (n=2022)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=6247)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.274 (n=2018)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=6107)

- **FILTRO** `ibs_7min` < `0.2308` → IC=-0.235 (n=2026)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2308
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=6099)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.186 (n=2791)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=9027)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=1985)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=6021)

- **FILTRO** `ibs_7min` < `0.2187` → IC=-0.220 (n=2001)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2187
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=6005)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.200 (n=1859)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=6147)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.209 (n=2721)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=8467)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.158 (n=299)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=980)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=1264)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.160 (n=51)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=633)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=818)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=372)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.138 (n=158)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=316)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.226 (n=49)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=426)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.129 (n=68)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=609)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=376)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.144 (n=1043)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.141 (n=486)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 14.0 (IC base=+0.129)

- **PATRÓN** `total_vol_5m` < `442.4725` → IC=+0.160 (n=348)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 442.4725 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `3698.2852` → IC=+0.133 (n=472)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 3698.2852 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.160 (n=336)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 13.0 (IC base=+0.129)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4372` → IC=+0.163 (n=81)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio` |x|> 0.4372 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.223 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `2614.7862` → IC=+0.235 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2614.7862 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.182 (n=105)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 9.0 (IC base=+0.147)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.4389` → IC=+0.139 (n=70)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio` |x|> 0.4389 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.137 (n=89)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 4.0 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.129 (n=246)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.04 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2022.4544` → IC=+0.130 (n=209)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2022.4544 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.151 (n=81)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 8.0 (IC base=+0.118)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4161` → IC=+0.176 (n=140)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio` |x|> 0.4161 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.153 (n=217)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 4.0 (IC base=+0.128)

- **PATRÓN** `total_vol_5m` < `390.3055` → IC=+0.226 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 390.3055 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `8021.3213` → IC=+0.134 (n=140)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 8021.3213 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.184 (n=93)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 72.0 (IC base=+0.128)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4332` → IC=+0.244 (n=84)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4332 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.172 (n=135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 12.0 (IC base=+0.149)

- **PATRÓN** `total_vol_5m` < `4970.298` → IC=+0.191 (n=124)

  - _Acción_: Kelly boost +0.95€ cuando `total_vol_5m` < 4970.298 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `3077.3625` → IC=+0.158 (n=185)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3077.3625 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.182 (n=61)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 28.0 (IC base=+0.149)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.401` → IC=+0.135 (n=176)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.401 (IC base=+0.095)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.121 (n=172)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` < 13.0 (IC base=+0.095)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.185 (n=122)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `3635.4092` → IC=+0.170 (n=89)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 3635.4092 (IC base=+0.095)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.4547` → IC=-0.256 (n=43)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.4547
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=130)

- **FILTRO** `sigma_h` > `0.0051` → IC=-0.265 (n=300)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0051
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=302)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.167 (n=151)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0034 (IC base=-0.084)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0054` → IC=-0.272 (n=90)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0054
  - _Potencial_: sin este filtro IC_bueno=+0.177 (n=91)

- **FILTRO** `T_h` > `87.9981` → IC=-0.287 (n=45)

  - _Acción_: SKIP cuando `T_h` > 87.9981
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=136)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.292 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=-0.046)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0055` → IC=-0.152 (n=44)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0055
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=16)

- **FILTRO** `pct_vs_K` |x|> `7.7861` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.7861
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=40)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0097` → IC=-0.167 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=70)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.224 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=-0.066)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.224 (n=418)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=140)

- **FILTRO** `pct_vs_K` |x|> `2.2191` → IC=-0.386 (n=234)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.2191
  - _Potencial_: sin este filtro IC_bueno=-0.116 (n=235)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0042` → IC=-0.202 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0042
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=142)

- **FILTRO** `T_h` > `79.3043` → IC=-0.185 (n=125)

  - _Acción_: SKIP cuando `T_h` > 79.3043
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=62)

- **FILTRO** `pct_vs_K` |x|> `3.0008` → IC=-0.432 (n=42)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.0008
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=129)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `T_h` < `139.5329` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `T_h` < 139.5329
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `sigma_h` < `0.0085` → IC=-0.239 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

- **FILTRO** `T_h` > `144.5457` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` > 144.5457
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.005` → IC=-0.278 (n=52)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=106)

- **FILTRO** `T_h` < `87.9918` → IC=-0.278 (n=52)

  - _Acción_: SKIP cuando `T_h` < 87.9918
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=106)

- **FILTRO** `sigma_h` > `0.0088` → IC=-0.365 (n=35)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0088
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=109)

- **FILTRO** `sigma_h` < `0.005` → IC=-0.263 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=108)

- **FILTRO** `T_h` > `57.1769` → IC=-0.306 (n=96)

  - _Acción_: SKIP cuando `T_h` > 57.1769
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=48)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `T_h` < `145.7969` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` < 145.7969
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0082` → IC=-0.300 (n=48)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0082
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=100)

- **FILTRO** `T_h` > `113.7599` → IC=-0.220 (n=73)

  - _Acción_: SKIP cuando `T_h` > 113.7599
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=75)

- **FILTRO** `sigma_h` > `0.015` → IC=-0.346 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.015
  - _Potencial_: sin este filtro IC_bueno=-0.263 (n=74)

- **FILTRO** `pct_vs_K` |x|> `3.8261` → IC=-0.414 (n=33)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.8261
  - _Potencial_: sin este filtro IC_bueno=-0.216 (n=65)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1224` → IC=+0.475 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1224 (IC base=+0.337)

- **PATRÓN** `sigma_h` < `0.0135` → IC=+0.357 (n=89)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0135 (IC base=+0.337)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.378 (n=88)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.337)

- **PATRÓN** `T_h` > `0.7758` → IC=+0.385 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7758 (IC base=+0.337)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.477 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.337)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.354 (n=80)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.337)

- **PATRÓN** `edge` > `0.096` → IC=+0.446 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.096 (IC base=+0.419)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.429 (n=68)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.419)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.442 (n=135)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.419)

- **PATRÓN** `T_h` < `0.9836` → IC=+0.427 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9836 (IC base=+0.419)

- **PATRÓN** `T_h` > `1.4813` → IC=+0.444 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4813 (IC base=+0.419)

- **PATRÓN** `dist_50` > `0.3811` → IC=+0.466 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3811 (IC base=+0.419)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.478 (n=133)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.419)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1026` → IC=+0.457 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1026 (IC base=+0.430)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.417 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.430)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.460 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.430)

- **PATRÓN** `T_h` < `0.9672` → IC=+0.456 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9672 (IC base=+0.430)

- **PATRÓN** `T_h` > `0.4508` → IC=+0.423 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4508 (IC base=+0.430)

- **PATRÓN** `dist_50` > `0.4084` → IC=+0.478 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4084 (IC base=+0.430)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.423 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.430)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.430)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.1975` → IC=+0.482 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1975 (IC base=+0.434)

- **PATRÓN** `sigma_h` < `0.016` → IC=+0.465 (n=55)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.016 (IC base=+0.434)

- **PATRÓN** `T_h` > `0.4742` → IC=+0.446 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4742 (IC base=+0.434)

- **PATRÓN** `dist_50` > `0.354` → IC=+0.464 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.354 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.435 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.434)

- **PATRÓN** `edge` > `0.1961` → IC=+0.478 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1961 (IC base=+0.463)

- **PATRÓN** `sigma_h` < `0.0156` → IC=+0.478 (n=132)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0156 (IC base=+0.463)

- **PATRÓN** `T_h` > `1.1834` → IC=+0.478 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.1834 (IC base=+0.463)

- **PATRÓN** `dist_50` > `0.4421` → IC=+0.485 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4421 (IC base=+0.463)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.472 (n=139)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.463)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=281)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=363)

- **FILTRO** `streak_estiramiento` > `0.8581` → IC=-0.171 (n=80)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.8581
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=242)

- **PATRÓN** `streak_estiramiento` < `0.4095` → IC=+0.225 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.4095 (IC base=+0.036)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=27)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=14)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=27)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.000)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `streak_estiramiento` < `0.293` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `streak_estiramiento` < 0.293 (IC base=+0.005)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.155 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 10.0 (IC base=+0.079)

- **PATRÓN** `streak_estiramiento` < `0.3243` → IC=+0.181 (n=67)

  - _Acción_: Kelly boost +0.91€ cuando `streak_estiramiento` < 0.3243 (IC base=+0.079)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.126 (n=113)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 44.0 (IC base=+0.079)

- **PATRÓN** `libro_liquidez` > `2312.8768` → IC=+0.150 (n=118)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2312.8768 (IC base=+0.079)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=94)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=100)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.190 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=31)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=43)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=820)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=697)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` < `11.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `libro_liquidez` < `3338.6704` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_liquidez` < 3338.6704
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### STREAK_FADE_60M#ETH#60min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

### STREAK_FADE_60M#SOL#60min
- **PATRÓN** `regimen_ma_toques` > `4.0` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.050)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=916)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1327)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1046)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=1064)

### STRUCT_NO_15M
- **FILTRO** `libro_liquidez` < `7203.0371` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 7203.0371
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3747)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `libro_liquidez` < `7203.0371` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 7203.0371
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=2019)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.203 (n=1040)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.226 (n=1040)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.1668` → IC=+0.198 (n=2745)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.1668 (IC base=+0.190)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3513` → IC=+0.201 (n=2783)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3513 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=3127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.196 (n=2847)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `ibs_15` > `0.5833` → IC=+0.269 (n=3122)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5833 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` > `0.1229` → IC=+0.186 (n=1501)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1229 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` < `0.3094` → IC=+0.177 (n=2352)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.3094 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.684` → IC=+0.267 (n=813)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.684 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `5316.1531` → IC=+0.203 (n=1040)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5316.1531 (IC base=+0.190)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=1231)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.240 (n=367)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.0591` → IC=+0.263 (n=184)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0591 (IC base=+0.217)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2526` → IC=+0.251 (n=183)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2526 (IC base=+0.217)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2321` → IC=+0.229 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2321 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=556)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.217)

- **PATRÓN** `ibs_15` > `0.7223` → IC=+0.277 (n=550)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7223 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` > `0.1371` → IC=+0.242 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1371 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.202` → IC=+0.298 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.202 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.218 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `16220.2116` → IC=+0.253 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16220.2116 (IC base=+0.217)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.513` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.513
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=698)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.186 (n=208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0033 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.0669` → IC=+0.152 (n=274)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.0669 (IC base=+0.146)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1464` → IC=+0.159 (n=414)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio_macro` |x|> 0.1464 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1304` → IC=+0.163 (n=241)

  - _Acción_: Kelly boost +0.81€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1304 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.148 (n=575)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 6.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.152 (n=650)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.5725` → IC=+0.245 (n=621)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5725 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1186` → IC=+0.157 (n=397)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1186 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.2815` → IC=+0.148 (n=574)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2815 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.049` → IC=+0.290 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.049 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `3552.1099` → IC=+0.153 (n=555)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3552.1099 (IC base=+0.146)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `18.995` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.995
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=259)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.170 (n=201)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0101 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1493` → IC=+0.154 (n=403)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1493 (IC base=+0.118)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0641` → IC=+0.125 (n=603)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.62€ cuando `delta_ratio_macro` |x|> 0.0641 (IC base=+0.118)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3335` → IC=+0.135 (n=554)

  - _Acción_: Kelly boost +0.67€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3335 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.131 (n=277)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 6.0 (IC base=+0.118)

- **PATRÓN** `ibs_15` > `0.9091` → IC=+0.295 (n=203)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9091 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.3733` → IC=+0.125 (n=609)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` < 0.3733 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.786` → IC=+0.152 (n=116)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 17.786 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=337)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.118)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0232` → IC=+0.281 (n=236)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0232 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.1654` → IC=+0.224 (n=624)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1654 (IC base=+0.218)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.33` → IC=+0.245 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.33 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.236 (n=647)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.218)

- **PATRÓN** `ibs_15` > `0.5714` → IC=+0.301 (n=710)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5714 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` > `0.1903` → IC=+0.225 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1903 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.758` → IC=+0.267 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.758 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `2995.8059` → IC=+0.286 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2995.8059 (IC base=+0.218)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.163 (n=725)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.81€ cuando `ibs_15` < 0.1111 (IC base=+0.065)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.367 (n=389)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.361)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.368 (n=583)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0027 (IC base=+0.361)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1511` → IC=+0.385 (n=388)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1511 (IC base=+0.361)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2309` → IC=+0.383 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2309 (IC base=+0.361)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.375 (n=589)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.361)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.396 (n=585)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.361)

- **PATRÓN** `dist_vwap_pct` > `0.4165` → IC=+0.390 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4165 (IC base=+0.361)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.722` → IC=+0.387 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.722 (IC base=+0.361)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.366 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.361)

- **PATRÓN** `libro_liquidez` > `3505.1277` → IC=+0.370 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3505.1277 (IC base=+0.361)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.361 (n=272)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.362)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.376 (n=103)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.362)

- **PATRÓN** `drift_15min` |x|≤ `0.5078` → IC=+0.361 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5078 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2147` → IC=+0.394 (n=140)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2147 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1371` → IC=+0.394 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1371 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.381 (n=310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.8077` → IC=+0.388 (n=309)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8077 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.2504` → IC=+0.394 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2504 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.997` → IC=+0.382 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.997 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.822` → IC=+0.361 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.822 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `15285.027` → IC=+0.387 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15285.027 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `487.0` → IC=+0.409 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 487.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.362 (n=121)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.359)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.366 (n=275)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.359)

- **PATRÓN** `drift_60min` |x|≤ `0.1075` → IC=+0.360 (n=184)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1075 (IC base=+0.359)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0901` → IC=+0.375 (n=246)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0901 (IC base=+0.359)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2995` → IC=+0.381 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2995 (IC base=+0.359)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.389 (n=133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.359)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.365 (n=124)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.359)

- **PATRÓN** `ibs_15` > `0.7504` → IC=+0.406 (n=275)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7504 (IC base=+0.359)

- **PATRÓN** `dist_vwap_pct` > `0.4453` → IC=+0.366 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4453 (IC base=+0.359)

- **PATRÓN** `dist_vwap_pct` < `0.2918` → IC=+0.362 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2918 (IC base=+0.359)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.293` → IC=+0.393 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.293 (IC base=+0.359)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.363 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.359)

- **PATRÓN** `libro_liquidez` > `3893.6222` → IC=+0.390 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3893.6222 (IC base=+0.359)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.361 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 139.0 (IC base=+0.359)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0121` → IC=-0.222 (n=998)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0121
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=2997)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.207 (n=1545)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=2450)

- **FILTRO** `libro_liquidez` < `4148.2911` → IC=-0.147 (n=2636)

  - _Acción_: SKIP cuando `libro_liquidez` < 4148.2911
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=1359)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1416` → IC=+0.188 (n=645)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1416 (IC base=-0.065)

- **PATRÓN** `ibs_15` > `0.6347` → IC=+0.283 (n=966)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6347 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` > `0.1109` → IC=+0.207 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1109 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` < `0.4229` → IC=+0.202 (n=926)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4229 (IC base=-0.065)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1326` → IC=+0.261 (n=2173)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1326 (IC base=-0.013)

- **PATRÓN** `ibs_15` < `0.3521` → IC=+0.281 (n=3255)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3521 (IC base=-0.013)

- **PATRÓN** `dist_vwap_pct` > `0.6528` → IC=+0.278 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6528 (IC base=-0.013)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.206 (n=563)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=1692)

- **FILTRO** `sigma_h` < `0.0038` → IC=-0.223 (n=744)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0038
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=1511)

- **FILTRO** `sigma_ewma_delta_pct` > `23.641` → IC=-0.262 (n=325)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.641
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=1930)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.212 (n=64)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=2191)

- **FILTRO** `libro_liquidez` < `16240.1959` → IC=-0.204 (n=1488)

  - _Acción_: SKIP cuando `libro_liquidez` < 16240.1959
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=767)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.172 (n=227)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0026 (IC base=+0.094)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2139` → IC=+0.290 (n=136)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2139 (IC base=+0.094)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1064` → IC=+0.280 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1064 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.134 (n=334)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 15.0 (IC base=+0.094)

- **PATRÓN** `ibs_15` > `0.7566` → IC=+0.331 (n=299)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7566 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.1047` → IC=+0.299 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1047 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` < `0.3651` → IC=+0.294 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3651 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.1` → IC=+0.142 (n=199)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 20.1 (IC base=+0.094)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0674` → IC=+0.217 (n=51)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0674 (IC base=-0.195)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1779` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1779 (IC base=-0.195)

- **PATRÓN** `ibs_15` < `0.618` → IC=+0.296 (n=52)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.618 (IC base=-0.195)

- **PATRÓN** `dist_vwap_pct` < `0.0474` → IC=+0.287 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0474 (IC base=-0.195)

- **PATRÓN** `ballena_activa_n` < `291.0` → IC=+0.389 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 291.0 (IC base=-0.195)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.162 (n=629)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.164 (n=427)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.163 (n=485)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0033 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.1112` → IC=+0.181 (n=324)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.1112 (IC base=+0.154)

- **PATRÓN** `drift_15min` |x|≤ `0.4034` → IC=+0.159 (n=162)

  - _Acción_: Kelly boost +0.79€ cuando `drift_15min` |x|≤ 0.4034 (IC base=+0.154)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1408` → IC=+0.162 (n=323)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio_macro` |x|> 0.1408 (IC base=+0.154)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2962` → IC=+0.197 (n=367)

  - _Acción_: Kelly boost +0.98€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2962 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.176 (n=347)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 11.0 (IC base=+0.154)

- **PATRÓN** `ibs_15` > `0.6288` → IC=+0.258 (n=485)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6288 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.455` → IC=+0.159 (n=133)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.455 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `0.1594` → IC=+0.159 (n=373)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1594 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.52` → IC=+0.263 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.52 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.162 (n=629)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `10575.7678` → IC=+0.171 (n=162)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 10575.7678 (IC base=+0.154)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.253 (n=499)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.3518` → IC=+0.243 (n=999)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3518 (IC base=+0.242)

- **PATRÓN** `drift_15min` |x|≤ `0.7599` → IC=+0.253 (n=998)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7599 (IC base=+0.242)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1543` → IC=+0.256 (n=756)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1543 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.243 (n=1006)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.242)

- **PATRÓN** `ibs_15` < `0.3682` → IC=+0.273 (n=1134)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3682 (IC base=+0.242)

- **PATRÓN** `dist_vwap_pct` > `0.7785` → IC=+0.290 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7785 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.581` → IC=+0.252 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.581 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.698` → IC=+0.247 (n=1182)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.698 (IC base=+0.242)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1044` → IC=-0.204 (n=458)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1044
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=459)

- **FILTRO** `drift_60min` |x|> `0.1724` → IC=-0.254 (n=311)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1724
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=606)

- **FILTRO** `drift_15min` |x|> `0.8765` → IC=-0.271 (n=229)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8765
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=688)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.182)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.182)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.182)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.182)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0819` → IC=+0.240 (n=456)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0819 (IC base=-0.038)

- **PATRÓN** `ibs_15` < `0.3462` → IC=+0.282 (n=511)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3462 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` < `0.1802` → IC=+0.247 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1802 (IC base=-0.038)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0195` → IC=-0.249 (n=552)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0195
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=553)

- **FILTRO** `drift_15min` |x|> `1.2333` → IC=-0.263 (n=276)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2333
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=829)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=1086)

- **FILTRO** `libro_liquidez` < `2981.8454` → IC=-0.213 (n=828)

  - _Acción_: SKIP cuando `libro_liquidez` < 2981.8454
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=277)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.203)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.203)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1531` → IC=+0.278 (n=354)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1531 (IC base=-0.026)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1115` → IC=+0.304 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1115 (IC base=-0.026)

- **PATRÓN** `ibs_15` < `0.3297` → IC=+0.294 (n=780)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3297 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` > `0.7812` → IC=+0.348 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7812 (IC base=-0.026)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.295 (n=977)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.0533` → IC=+0.320 (n=326)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0533 (IC base=+0.290)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2454` → IC=+0.296 (n=326)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2454 (IC base=+0.290)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2247` → IC=+0.306 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2247 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.305 (n=1026)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.290)

- **PATRÓN** `ibs_15` > `0.8379` → IC=+0.321 (n=977)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8379 (IC base=+0.290)

- **PATRÓN** `dist_vwap_pct` > `0.4335` → IC=+0.323 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4335 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.865` → IC=+0.369 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.865 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `12706.4331` → IC=+0.311 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12706.4331 (IC base=+0.290)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.308 (n=232)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.0584` → IC=+0.309 (n=176)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0584 (IC base=+0.284)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2603` → IC=+0.309 (n=176)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2603 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.304 (n=529)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.284)

- **PATRÓN** `ibs_15` > `0.8267` → IC=+0.309 (n=527)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8267 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.2546` → IC=+0.321 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2546 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.276` → IC=+0.376 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 24.276 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.283 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `16334.7136` → IC=+0.326 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16334.7136 (IC base=+0.284)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.309 (n=301)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.296)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.296 (n=450)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.296)

- **PATRÓN** `drift_60min` |x|≤ `0.0515` → IC=+0.324 (n=151)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0515 (IC base=+0.296)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1516` → IC=+0.305 (n=300)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1516 (IC base=+0.296)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3023` → IC=+0.314 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3023 (IC base=+0.296)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.314 (n=406)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.296)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.297 (n=407)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.296)

- **PATRÓN** `ibs_15` > `0.8745` → IC=+0.340 (n=403)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8745 (IC base=+0.296)

- **PATRÓN** `dist_vwap_pct` > `0.6362` → IC=+0.327 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6362 (IC base=+0.296)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.66` → IC=+0.353 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.66 (IC base=+0.296)

### UPDOWN_OU_5M
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1212` → IC=-0.151 (n=81)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1212
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=243)

- **FILTRO** `ballena_activa_n` > `47.0` → IC=-0.136 (n=218)

  - _Acción_: SKIP cuando `ballena_activa_n` > 47.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=74)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.172 (n=117)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=354)

- **FILTRO** `ballena_activa_n` > `50.0` → IC=-0.204 (n=52)

  - _Acción_: SKIP cuando `ballena_activa_n` > 50.0
  - _Potencial_: sin este filtro IC_bueno=-0.131 (n=158)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1319` → IC=-0.173 (n=47)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1319
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=143)

- **FILTRO** `drift_60min` |x|> `0.2244` → IC=-0.222 (n=16)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2244
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=33)

- **FILTRO** `drift_15min` |x|> `0.3481` → IC=-0.278 (n=16)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3481
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=33)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1941` → IC=-0.231 (n=24)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1941
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=25)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.3151` → IC=-0.158 (n=36)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.3151
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=19)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.296` → IC=-0.370 (n=21)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.296
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0775` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0775
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `sigma_h` < `0.0063` → IC=-0.243 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=18)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0905` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0905
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `83.3501` → IC=+0.201 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.194)

- **PATRÓN** `ratio` < `0.973` → IC=+0.419 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.194)

- **PATRÓN** `T_h` > `111.996` → IC=+0.351 (n=2003)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.996 (IC base=+0.336)

- **PATRÓN** `ratio` > `1.0235` → IC=+0.369 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0235 (IC base=+0.336)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `103.3918` → IC=+0.181 (n=183)

  - _Acción_: Kelly boost +0.91€ cuando `T_h` > 103.3918 (IC base=+0.168)

- **PATRÓN** `ratio` < `0.9839` → IC=+0.333 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9839 (IC base=+0.168)

- **PATRÓN** `T_h` > `109.696` → IC=+0.303 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 109.696 (IC base=+0.291)

- **PATRÓN** `ratio` > `1.0466` → IC=+0.393 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0466 (IC base=+0.291)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `83.3501` → IC=+0.241 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.232)

- **PATRÓN** `ratio` < `0.9849` → IC=+0.429 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9849 (IC base=+0.232)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.350 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.324)

- **PATRÓN** `ratio` > `1.0093` → IC=+0.343 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0093 (IC base=+0.324)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1038` → IC=+0.448 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1038 (IC base=+0.400)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5833 sube el IC de +0.190 a +0.269 en UPDOWN_GBM#15min (n=3122). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7223 sube el IC de +0.217 a +0.277 en UPDOWN_GBM#BTC#15min (n=550). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5725 sube el IC de +0.146 a +0.245 en UPDOWN_GBM#ETH#15min (n=621). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.9091 sube el IC de +0.118 a +0.295 en UPDOWN_GBM#SOL#15min (n=203). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5714 sube el IC de +0.218 a +0.301 en UPDOWN_GBM#XRP#15min (n=710). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.065 a +0.163 en UPDOWN_GBM#XRP#15min (n=725). Ya aplicado como kelly_boost=+0.81€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6347 sube el IC de -0.065 a +0.283 en UPDOWN_GBM_15M_TARDIO (n=966). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3521 sube el IC de -0.013 a +0.281 en UPDOWN_GBM_15M_TARDIO (n=3255). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7566 sube el IC de +0.094 a +0.331 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=299). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.618 sube el IC de -0.195 a +0.296 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=52). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6288 sube el IC de +0.154 a +0.258 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=485). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3682 sube el IC de +0.242 a +0.273 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1134). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.182 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3462 sube el IC de -0.038 a +0.282 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=511). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.203 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3297 sube el IC de -0.026 a +0.294 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=780). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8379 sube el IC de +0.290 a +0.321 en UPDOWN_GBM_IBS_ALTO (n=977). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8267 sube el IC de +0.284 a +0.309 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=527). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8745 sube el IC de +0.296 a +0.340 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=403). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.361 a +0.396 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=585). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8077 sube el IC de +0.362 a +0.388 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=309). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7504 sube el IC de +0.359 a +0.406 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=275). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1749 | +0.087 | +189.79€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1749 | +0.087 | +189.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1374 | +0.091 | +163.46€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1374 | +0.091 | +163.46€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 272 | +0.066 | +10.61€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 272 | +0.066 | +10.61€ | 4 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 72 | +0.108 | +16.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 72 | +0.108 | +16.05€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 420 | +0.002 | +68.78€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 420 | +0.002 | +68.78€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 301 | +0.002 | +46.93€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 301 | +0.002 | +46.93€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 93 | +0.016 | +17.27€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 93 | +0.016 | +17.27€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 23 | -0.060 | +1.23€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 23 | -0.060 | +1.23€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 37261 | -0.083 | -4642.38€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1992 | +0.014 | -239.72€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 35269 | -0.089 | -4402.66€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4429 | -0.116 | -761.79€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4429 | -0.116 | -761.79€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1992 | +0.014 | -239.72€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1992 | +0.014 | -239.72€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4122 | -0.113 | -843.39€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4122 | -0.113 | -843.39€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 9812 | -0.006 | -826.74€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 9812 | -0.006 | -826.74€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 9692 | -0.108 | -711.46€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 9692 | -0.108 | -711.46€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 7214 | -0.144 | -1259.29€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 7214 | -0.144 | -1259.29€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 30817 | -0.018 | +3543.15€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 7971 | +0.004 | +1742.37€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 22846 | -0.025 | +1800.78€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 30817 | -0.018 | +3543.15€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 7971 | +0.004 | +1742.37€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 22846 | -0.025 | +1800.78€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 131858 | +0.114 | -5521.17€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 17568 | +0.182 | -538.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 573 | -0.030 | -65.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 105698 | +0.105 | -4643.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 8019 | +0.103 | -273.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 17541 | +0.106 | -1116.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 58 | -0.150 | +11.01€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 17468 | +0.107 | -1115.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 25789 | +0.128 | -417.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5058 | +0.191 | -162.13€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 17523 | +0.118 | -146.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3166 | +0.086 | -86.68€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 17591 | +0.097 | -1291.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 69 | -0.106 | -3.93€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 17507 | +0.098 | -1275.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 28030 | +0.124 | -494.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 7353 | +0.176 | -128.66€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 17740 | +0.106 | -304.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2925 | +0.100 | -52.10€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 25349 | +0.114 | -1322.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4968 | +0.192 | -262.68€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 476 | +0.004 | -11.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 17977 | +0.093 | -913.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1928 | +0.135 | -134.75€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 17558 | +0.104 | -878.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 62 | -0.062 | +8.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 17483 | +0.105 | -886.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 21145 | +0.195 | -1314.29€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 21145 | +0.195 | -1314.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4849 | +0.177 | -431.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4849 | +0.177 | -431.76€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 2512 | +0.202 | -51.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 2512 | +0.202 | -51.48€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 4793 | +0.179 | -394.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 4793 | +0.179 | -394.66€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4184 | +0.246 | -136.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4184 | +0.246 | -136.80€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4728 | +0.187 | -313.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4728 | +0.187 | -313.34€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 942 | +0.428 | -30.30€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 942 | +0.428 | -30.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 373 | +0.436 | -5.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 373 | +0.436 | -5.44€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 365 | +0.432 | -7.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 365 | +0.432 | -7.94€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 192 | +0.402 | -14.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 192 | +0.402 | -14.47€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 73645 | +0.201 | -5332.36€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 73645 | +0.201 | -5332.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 12659 | +0.185 | -1303.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 12659 | +0.185 | -1303.50€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 11873 | +0.225 | -406.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 11873 | +0.225 | -406.03€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 12631 | +0.179 | -1363.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 12631 | +0.179 | -1363.67€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 11954 | +0.220 | -451.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 11954 | +0.220 | -451.90€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 12205 | +0.202 | -803.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 12205 | +0.202 | -803.01€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 12323 | +0.196 | -1004.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 12323 | +0.196 | -1004.24€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 28168 | +0.117 | +202.81€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 28168 | +0.117 | +202.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 14000 | +0.120 | +176.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 14000 | +0.120 | +176.83€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 14168 | +0.114 | +25.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 14168 | +0.114 | +25.98€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1920 | +0.292 | -6.59€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1920 | +0.292 | -6.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 874 | +0.283 | -12.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 874 | +0.283 | -12.20€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 927 | +0.291 | +0.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 927 | +0.291 | +0.30€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 119 | +0.351 | +5.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 119 | +0.351 | +5.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 885 | +0.443 | +6.43€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 885 | +0.443 | +6.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 429 | +0.440 | -0.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 429 | +0.440 | -0.12€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 410 | +0.447 | +6.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 410 | +0.447 | +6.00€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1487 | +0.071 | -59.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 562 | +0.062 | -37.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 925 | +0.077 | -21.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 70 | +0.111 | +3.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 70 | +0.111 | +3.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1148 | +0.077 | -27.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 223 | +0.078 | -5.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 925 | +0.077 | -21.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 269 | +0.035 | -35.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 269 | +0.035 | -35.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 54916 | +0.100 | -1369.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 4446 | +0.093 | +64.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 50470 | +0.101 | -1434.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 30314 | +0.105 | -320.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 4446 | +0.093 | +64.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 25868 | +0.107 | -385.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 11135 | +0.109 | -45.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 11135 | +0.109 | -45.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 13467 | +0.082 | -1003.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 13467 | +0.082 | -1003.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 888 | +0.194 | -112.61€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 888 | +0.194 | -112.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 888 | +0.194 | -112.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 888 | +0.194 | -112.61€ | 2 | 4 |
| ✅ GBM_LATE_15M | 37986 | +0.092 | +19427.33€ | 0 | 17 |
| ✅ GBM_LATE_15M#15min | 37986 | +0.092 | +19427.33€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 6366 | +0.209 | +5065.99€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 6366 | +0.209 | +5065.99€ | 0 | 24 |
| ✅ GBM_LATE_15M#BTC | 5665 | +0.180 | +4234.56€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 5665 | +0.180 | +4234.56€ | 0 | 26 |
| ✅ GBM_LATE_15M#DOGE | 6773 | +0.203 | +5209.30€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 6773 | +0.203 | +5209.30€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 5333 | +0.040 | +1443.23€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 5333 | +0.040 | +1443.23€ | 1 | 17 |
| ✅ GBM_LATE_15M#SOL | 5411 | -0.030 | +1187.70€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 5411 | -0.030 | +1187.70€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 8438 | -0.034 | +2286.54€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 8438 | -0.034 | +2286.54€ | 3 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 41063 | +0.086 | +22151.06€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 41063 | +0.086 | +22151.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 7924 | +0.006 | +4086.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 7924 | +0.006 | +4086.35€ | 3 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 8638 | +0.013 | +1942.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 8638 | +0.013 | +1942.99€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 5737 | +0.274 | +6058.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 5737 | +0.274 | +6058.94€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 7206 | +0.013 | +1710.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 7206 | +0.013 | +1710.10€ | 1 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 6624 | +0.039 | +2712.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 6624 | +0.039 | +2712.13€ | 3 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4934 | +0.295 | +5640.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4934 | +0.295 | +5640.54€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 30205 | +0.178 | +24141.46€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 30205 | +0.178 | +24141.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 4584 | +0.222 | +3937.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 4584 | +0.222 | +3937.08€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 4749 | +0.151 | +3509.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 4749 | +0.151 | +3509.91€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 4818 | +0.221 | +4097.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 4818 | +0.221 | +4097.82€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 5097 | +0.140 | +3894.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 5097 | +0.140 | +3894.56€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 5681 | +0.123 | +4157.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 5681 | +0.123 | +4157.98€ | 0 | 27 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 5276 | +0.222 | +4544.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 5276 | +0.222 | +4544.11€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 8097 | +0.136 | +3913.59€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 8097 | +0.136 | +3913.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 389 | +0.152 | +241.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 389 | +0.152 | +241.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2448 | +0.146 | +1366.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2448 | +0.146 | +1366.66€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 416 | +0.148 | +207.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 416 | +0.148 | +207.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2448 | +0.146 | +1183.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2448 | +0.146 | +1183.75€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1857 | +0.105 | +674.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1857 | +0.105 | +674.27€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 539 | +0.134 | +240.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 539 | +0.134 | +240.28€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO | 38185 | +0.183 | +30092.51€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#15min | 38185 | +0.183 | +30092.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 6068 | +0.235 | +5508.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 6068 | +0.235 | +5508.57€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 5915 | +0.149 | +3967.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 5915 | +0.149 | +3967.69€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 6434 | +0.231 | +5694.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 6434 | +0.231 | +5694.23€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 6254 | +0.139 | +4470.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 6254 | +0.139 | +4470.65€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 6770 | +0.122 | +4627.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 6770 | +0.122 | +4627.56€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 6744 | +0.225 | +5823.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 6744 | +0.225 | +5823.81€ | 0 | 21 |
| ✅ GBM_LATE_5M | 10692 | +0.193 | +7926.85€ | 1 | 30 |
| ✅ GBM_LATE_5M#5min | 10692 | +0.193 | +7926.85€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 919 | +0.232 | +813.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 919 | +0.232 | +813.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2394 | +0.187 | +1876.77€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2394 | +0.187 | +1876.77€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 1002 | +0.176 | +657.98€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1002 | +0.176 | +657.98€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 3182 | +0.192 | +2230.67€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3182 | +0.192 | +2230.67€ | 0 | 24 |
| ✅ GBM_LATE_5M#SOL | 1558 | +0.189 | +1169.50€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1558 | +0.189 | +1169.50€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1637 | +0.194 | +1177.94€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1637 | +0.194 | +1177.94€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2997 | +0.071 | +1031.84€ | 0 | 10 |
| ✅ GBM_LATE_60M#60min | 2997 | +0.071 | +1031.84€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1120 | +0.088 | +409.26€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1120 | +0.088 | +409.26€ | 0 | 11 |
| ✅ GBM_LATE_60M#ETH | 956 | +0.073 | +375.99€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 956 | +0.073 | +375.99€ | 0 | 11 |
| ✅ GBM_LATE_60M#SOL | 921 | +0.047 | +246.59€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 921 | +0.047 | +246.59€ | 0 | 12 |
| 🚫 GBM_LATE_60M_FADE | 519 | -0.241 | -16.86€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 519 | -0.241 | -16.86€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 196 | -0.232 | -8.39€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 196 | -0.232 | -8.39€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 185 | -0.222 | -1.51€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 185 | -0.222 | -1.51€ | 5 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 138 | -0.271 | -6.96€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 138 | -0.271 | -6.96€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1356 | +0.086 | +345.11€ | 0 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1356 | +0.086 | +345.11€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 524 | +0.086 | +111.59€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 524 | +0.086 | +111.59€ | 1 | 13 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 501 | +0.061 | +81.87€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 501 | +0.061 | +81.87€ | 2 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 331 | +0.125 | +151.65€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 331 | +0.125 | +151.65€ | 2 | 15 |
| ✅ LATE_WINDOW_5MIN | 144 | +0.253 | +124.85€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 144 | +0.253 | +124.85€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 144 | +0.253 | +124.85€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 144 | +0.253 | +124.85€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3168 | +0.101 | +793.20€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3168 | +0.101 | +793.20€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3168 | +0.101 | +793.20€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3168 | +0.101 | +793.20€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 453 | -0.065 | -30.08€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 453 | -0.065 | -30.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 131 | -0.019 | +0.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 131 | -0.019 | +0.81€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 73 | -0.087 | -8.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 73 | -0.087 | -8.28€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 168 | -0.029 | -5.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 168 | -0.029 | -5.75€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M | 3391 | +0.018 | +82.45€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3391 | +0.018 | +82.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 166 | +0.018 | -3.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 166 | +0.018 | -3.24€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 634 | +0.022 | +39.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 634 | +0.022 | +39.10€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1217 | +0.029 | +33.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1217 | +0.029 | +33.12€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 746 | +0.011 | +0.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 746 | +0.011 | +0.72€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 425 | +0.008 | +17.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 425 | +0.008 | +17.83€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1598 | -0.041 | -27.13€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1598 | -0.041 | -27.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 451 | -0.034 | -11.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 451 | -0.034 | -11.82€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 540 | -0.018 | +3.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 540 | -0.018 | +3.82€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 607 | -0.067 | -19.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 607 | -0.067 | -19.13€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 6721 | -0.023 | +53.21€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 3197 | -0.031 | -33.48€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 3524 | -0.015 | +86.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 193 | +0.003 | +13.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 95 | +0.046 | +15.12€ | 0 | 4 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 98 | -0.040 | -1.54€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 1684 | -0.011 | +41.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 805 | -0.017 | +6.31€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 879 | -0.005 | +35.11€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 737 | -0.025 | +6.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 374 | -0.043 | -9.57€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 363 | -0.007 | +15.89€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 1400 | -0.037 | -38.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 651 | -0.050 | -38.62€ | 3 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 749 | -0.026 | +0.10€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1327 | -0.021 | +16.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 635 | -0.032 | -3.02€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 692 | -0.011 | +19.85€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1380 | -0.027 | +13.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 637 | -0.035 | -3.70€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 743 | -0.019 | +17.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 14662 | -0.012 | -218.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14662 | -0.012 | -218.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 44400 | -0.001 | +2136.21€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 44400 | -0.001 | +2136.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 7962 | +0.025 | +1010.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 7962 | +0.025 | +1010.12€ | 2 | 5 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 6494 | -0.035 | -118.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 6494 | -0.035 | -118.58€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 8079 | +0.023 | +790.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 8079 | +0.023 | +790.85€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 6326 | -0.047 | -146.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 6326 | -0.047 | -146.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 7481 | -0.004 | +244.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 7481 | -0.004 | +244.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 8058 | +0.015 | +355.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 8058 | +0.015 | +355.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6409 | -0.060 | -157.57€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6409 | -0.060 | -157.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1224 | +0.000 | -14.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1224 | +0.000 | -14.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1630 | -0.079 | -41.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1630 | -0.079 | -41.06€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 53 | -0.064 | -2.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 53 | -0.064 | -2.93€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 748 | -0.121 | -33.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 748 | -0.121 | -33.08€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1898 | -0.078 | -40.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1898 | -0.078 | -40.70€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 856 | -0.015 | -25.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 856 | -0.015 | -25.00€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3365 | +0.005 | -0.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3365 | +0.005 | -0.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 131 | -0.034 | -0.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 131 | -0.034 | -0.72€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 192 | +0.015 | +1.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 192 | +0.015 | +1.02€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 138 | +0.000 | -1.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 138 | +0.000 | -1.83€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1325 | +0.006 | +6.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1325 | +0.006 | +6.88€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1390 | +0.007 | +0.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1390 | +0.007 | +0.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 189 | -0.008 | -5.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 189 | -0.008 | -5.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 110749 | -0.074 | +1753.86€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 110749 | -0.074 | +1753.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 19168 | -0.075 | +1015.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 19168 | -0.075 | +1015.91€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 16730 | -0.099 | -915.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 16730 | -0.099 | -915.23€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 19445 | -0.066 | +1123.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 19445 | -0.066 | +1123.28€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 16269 | -0.095 | -484.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 16269 | -0.095 | -484.62€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 19943 | -0.054 | +346.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 19943 | -0.054 | +346.50€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 19194 | -0.065 | +668.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 19194 | -0.065 | +668.01€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8627 | -0.033 | -174.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8627 | -0.033 | -174.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 997 | -0.017 | -19.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 997 | -0.017 | -19.30€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1963 | -0.045 | -22.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1963 | -0.045 | -22.09€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2569 | -0.026 | -42.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2569 | -0.026 | -42.09€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1152 | -0.051 | -25.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1152 | -0.051 | -25.16€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 938 | -0.029 | -32.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 938 | -0.029 | -32.79€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1524 | +0.122 | +613.88€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 1388 | +0.129 | +601.29€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 324 | +0.147 | +175.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 324 | +0.147 | +175.72€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 278 | +0.118 | +94.64€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 278 | +0.118 | +94.64€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#ETH | 280 | +0.128 | +125.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 280 | +0.128 | +125.53€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 246 | +0.149 | +132.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 246 | +0.149 | +132.53€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 260 | +0.095 | +72.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 260 | +0.095 | +72.87€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1217 | -0.019 | -26.37€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1217 | -0.019 | -26.37€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 231 | -0.011 | +3.11€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 231 | -0.011 | +3.11€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 211 | -0.012 | +0.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 211 | -0.012 | +0.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 314 | -0.041 | -24.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 314 | -0.041 | -24.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 257 | -0.002 | -1.51€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 257 | -0.002 | -1.51€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 204 | -0.024 | -4.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 204 | -0.024 | -4.10€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 842 | -0.071 | -42.25€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 389 | -0.119 | -77.77€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 300 | -0.152 | -67.97€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 89 | -0.005 | -9.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 301 | -0.035 | +22.38€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 215 | -0.030 | +22.89€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 86 | -0.045 | -0.50€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 152 | -0.019 | +13.13€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 122 | -0.024 | +8.23€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 30 | +0.000 | +4.90€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 637 | -0.087 | -36.85€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 205 | -0.022 | -5.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1027 | -0.207 | -57.18€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 414 | -0.207 | -37.94€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 358 | -0.211 | -38.22€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 56 | -0.172 | +0.28€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 348 | -0.217 | -30.63€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 302 | -0.227 | -36.32€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 46 | -0.146 | +5.69€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 265 | -0.193 | +11.38€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 246 | -0.190 | +8.24€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 19 | -0.204 | +3.14€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 906 | -0.211 | -66.30€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 121 | -0.175 | +9.11€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 420 | +0.396 | +400.99€ | 0 | 13 |
| ✅ RESOLUTION_SNIPER#BTC | 53 | +0.118 | +46.13€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 53 | +0.118 | +46.13€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 105 | +0.369 | +91.40€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 105 | +0.369 | +91.40€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 262 | +0.458 | +263.46€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 262 | +0.458 | +263.46€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 420 | +0.396 | +400.99€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 682 | +0.026 | +24.65€ | 3 | 1 |
| ✅ STREAK_FADE_15M#15min | 682 | +0.026 | +24.65€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 296 | +0.024 | +3.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 296 | +0.024 | +3.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 55 | -0.026 | -5.35€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 55 | -0.026 | -5.35€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 71 | -0.007 | -0.09€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 71 | -0.007 | -0.09€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 260 | +0.050 | +26.65€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 260 | +0.050 | +26.65€ | 0 | 5 |
| ✅ STREAK_FADE_5M | 3376 | -0.021 | -130.18€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3376 | -0.021 | -130.18€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1051 | -0.022 | -37.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1051 | -0.022 | -37.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 586 | -0.025 | -25.10€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 586 | -0.025 | -25.10€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 162 | -0.043 | -14.36€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 162 | -0.043 | -14.36€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1577 | -0.016 | -53.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1577 | -0.016 | -53.20€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 95 | -0.046 | -8.93€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 95 | -0.046 | -8.93€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 40 | -0.071 | -3.54€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 40 | -0.071 | -3.54€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 55 | -0.026 | -5.39€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 55 | -0.026 | -5.39€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 10323 | +0.018 | +100.05€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 10323 | +0.018 | +100.05€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2650 | +0.021 | +27.26€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2650 | +0.021 | +27.26€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2637 | +0.021 | +40.82€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2637 | +0.021 | +40.82€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2884 | +0.009 | -2.06€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2884 | +0.009 | -2.06€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2152 | +0.022 | +34.03€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2152 | +0.022 | +34.03€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 9422 | +0.013 | -52.44€ | 1 | 0 |
| ✅ STRUCT_NO_15M#15min | 9422 | +0.013 | -52.44€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3766 | +0.017 | -8.42€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3766 | +0.017 | -8.42€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3603 | +0.011 | -28.25€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3603 | +0.011 | -28.25€ | 1 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2053 | +0.007 | -15.76€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2053 | +0.007 | -15.76€ | 1 | 0 |
| ✅ UPDOWN_GBM | 69047 | +0.052 | +6036.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 17196 | +0.085 | +3896.17€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2275 | +0.007 | +16.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 45370 | +0.047 | +2047.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 3969 | +0.009 | +76.42€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6818 | +0.089 | +1072.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1543 | +0.158 | +694.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5198 | +0.070 | +378.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 14051 | +0.054 | +1184.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2155 | +0.091 | +525.09€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 587 | +0.013 | +9.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 9455 | +0.058 | +591.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1768 | +0.007 | +54.46€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 86 | -0.068 | +4.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8047 | +0.066 | +843.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1529 | +0.149 | +607.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6440 | +0.047 | +237.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 15346 | +0.043 | +960.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3992 | +0.062 | +569.21€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 580 | +0.009 | +10.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 9337 | +0.042 | +364.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1358 | +0.013 | +14.67€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 79 | -0.105 | +2.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 15183 | +0.030 | +688.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 4156 | +0.037 | +369.86€ | 0 | 9 |
| ✅ UPDOWN_GBM#SOL#240min | 565 | -0.003 | -0.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 9549 | +0.032 | +316.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 843 | +0.009 | +7.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 70 | -0.139 | -4.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 9600 | +0.062 | +1289.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3821 | +0.103 | +1129.96€ | 0 | 9 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 5391 | +0.036 | +159.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 235 | -0.103 | +1.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 777 | +0.361 | +275.86€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 777 | +0.361 | +275.86€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 411 | +0.362 | +140.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 411 | +0.362 | +140.98€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 366 | +0.359 | +134.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 366 | +0.359 | +134.88€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 18352 | -0.024 | +4418.59€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 18352 | -0.024 | +4418.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1674 | -0.056 | +500.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1674 | -0.056 | +500.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3161 | -0.112 | +127.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3161 | -0.112 | +127.04€ | 5 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 926 | +0.220 | +767.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 926 | +0.220 | +767.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2157 | +0.216 | +1393.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2157 | +0.216 | +1393.30€ | 1 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5225 | -0.064 | +694.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5225 | -0.064 | +694.75€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5209 | -0.064 | +935.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5209 | -0.064 | +935.04€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 206 | +0.034 | +5.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 206 | +0.034 | +5.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 206 | +0.034 | +5.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 206 | +0.034 | +5.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1302 | +0.290 | +1093.73€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1302 | +0.290 | +1093.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 702 | +0.284 | +546.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 702 | +0.284 | +546.85€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 600 | +0.296 | +546.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 600 | +0.296 | +546.88€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 795 | -0.111 | -81.71€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 795 | -0.111 | -81.71€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 239 | -0.085 | -18.46€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 239 | -0.085 | -18.46€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 84 | -0.151 | -7.62€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 84 | -0.151 | -7.62€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 89 | -0.181 | -6.27€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 89 | -0.181 | -6.27€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 3328 | +0.304 | +1606.07€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1210 | +0.257 | +164.75€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1278 | +0.298 | +569.42€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 840 | +0.379 | +871.90€ | 0 | 1 |