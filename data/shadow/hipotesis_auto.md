# Hipótesis automáticas — 2026-10-15 09:39 UTC
_Generado por shadow_postmortem.py sobre 907175 resoluciones (PNL=+115970.57€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **PATRÓN** `py_entrada` > `0.56` → IC=+0.270 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.56 (IC base=+0.135)

- **PATRÓN** `n_total_lado` > `68.0` → IC=+0.194 (n=256)

  - _Acción_: Kelly boost +0.97€ cuando `n_total_lado` > 68.0 (IC base=+0.135)

- **PATRÓN** `banda_hit_calibrado` > `0.6329` → IC=+0.270 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6329 (IC base=+0.135)

- **PATRÓN** `banda_z` > `9.53` → IC=+0.215 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.53 (IC base=+0.135)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.734` → IC=+0.134 (n=678)

  - _Acción_: Kelly boost +0.67€ cuando `ballenas_wallet_edge_medio` > 0.734 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=263)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=821)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.135)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.545` → IC=+0.278 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.545 (IC base=+0.141)

- **PATRÓN** `n_total_lado` > `72.0` → IC=+0.212 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 72.0 (IC base=+0.141)

- **PATRÓN** `banda_hit_calibrado` > `0.6169` → IC=+0.264 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6169 (IC base=+0.141)

- **PATRÓN** `banda_z` > `9.994` → IC=+0.229 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.994 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.193 (n=213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.150 (n=723)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.141)

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
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=100)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=99)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=115)

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
- **FILTRO** `restante_s_al_confirmar` < `143.54` → IC=-0.204 (n=9491)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 143.54
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=28486)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `130.45` → IC=-0.265 (n=1108)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.45
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3327)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `122.77` → IC=-0.298 (n=1040)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.77
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=3121)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `167.3` → IC=-0.214 (n=2465)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 167.3
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=7398)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `132.3` → IC=-0.285 (n=1842)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.3
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=5528)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.210 (n=20138)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=4167)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `9308.1489` → IC=+0.179 (n=1869)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 9308.1489 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.132 (n=17055)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=20699)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.226 (n=15721)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=6931)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `7255.7854` → IC=+0.161 (n=2668)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 7255.7854 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=1981)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.196 (n=1940)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 17.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` > `0.775` → IC=+0.364 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.775 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.197 (n=2432)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `16256.7192` → IC=+0.206 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16256.7192 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.194 (n=1742)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 7.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.192 (n=1946)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 17.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.187)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.189 (n=2493)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `16111.0352` → IC=+0.196 (n=643)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 16111.0352 (IC base=+0.187)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.164 (n=448)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` > 0.61 (IC base=+0.084)

- **PATRÓN** `libro_liquidez` > `6891.1913` → IC=+0.172 (n=120)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 6891.1913 (IC base=+0.084)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.137 (n=1055)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.44 (IC base=+0.088)

- **PATRÓN** `libro_liquidez` > `5854.7033` → IC=+0.126 (n=241)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 5854.7033 (IC base=+0.088)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=3919)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.157)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.157 (n=2684)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 12.0 (IC base=+0.157)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.367 (n=1307)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.223 (n=1747)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.214)

- **PATRÓN** `py_entrada` < `0.255` → IC=+0.359 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.255 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.218 (n=2050)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.214)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.141 (n=979)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.144 (n=838)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.137)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.254 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=768)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2164.5524` → IC=+0.142 (n=425)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2164.5524 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `4449.086` → IC=+0.160 (n=151)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 4449.086 (IC base=+0.074)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=919)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.411 (n=1129)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.150 (n=1271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.158 (n=670)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 7.0 (IC base=+0.148)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.285 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=841)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.163 (n=419)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.256 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.129)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `11.0` → IC=-0.297 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=147)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=16897)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.201 (n=14399)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.233 (n=7025)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.178 (n=3925)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.177 (n=3721)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 17.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.180 (n=3815)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.73 (IC base=+0.176)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **FILTRO** `libro_liquidez` < `9614.35` → IC=-0.328 (n=56)

  - _Acción_: SKIP cuando `libro_liquidez` < 9614.35
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.223 (n=1884)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.234 (n=1261)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.314 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.223)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=3856)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.183 (n=3703)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.188 (n=1442)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.73 (IC base=+0.180)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.255 (n=3355)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.246)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.349 (n=1119)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=3781)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.194 (n=2427)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.194 (n=2790)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.188)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.431 (n=735)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.427)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.427 (n=653)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.427)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.441 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.427)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.430 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.427)

- **PATRÓN** `libro_liquidez` > `7257.3682` → IC=+0.442 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7257.3682 (IC base=+0.427)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `10.0` → IC=+0.449 (n=192)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.450 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

- **PATRÓN** `libro_liquidez` > `18173.9066` → IC=+0.439 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 18173.9066 (IC base=+0.437)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.445 (n=199)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.429)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.440 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.429)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.429)

- **PATRÓN** `libro_liquidez` > `4371.3371` → IC=+0.438 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4371.3371 (IC base=+0.429)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.405 (n=135)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.403)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.403 (n=132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.403)

- **PATRÓN** `py_entrada` > `0.91` → IC=+0.409 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.91 (IC base=+0.403)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.775` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=18)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=25)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=21801)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.246 (n=22109)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.201)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.192 (n=3246)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 18.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.187 (n=7000)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 12.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.201 (n=9755)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.185)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=4554)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.227 (n=4503)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.284 (n=3202)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.188 (n=3730)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.180 (n=6978)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 12.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.194 (n=9306)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=4587)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.221 (n=3516)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.277 (n=3128)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.204 (n=8877)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.263 (n=3273)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=3624)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.197 (n=3686)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.248 (n=3795)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.190 (n=7891)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` < `4.21` → IC=+0.124 (n=7223)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` < 4.21 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.137 (n=7772)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.41` → IC=+0.137 (n=7229)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.41 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=3906)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` < `4.19` → IC=+0.126 (n=3628)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.19 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.141 (n=3926)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=4786)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `2.82` → IC=+0.144 (n=3592)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 2.82 (IC base=+0.120)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.187 (n=3985)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.132 (n=4249)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.135 (n=3650)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.25 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.297 (n=1549)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.289 (n=1312)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.289)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.372 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `4309.8353` → IC=+0.290 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4309.8353 (IC base=+0.289)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.286 (n=700)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.279)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.281 (n=605)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.343 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `5377.6935` → IC=+0.291 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5377.6935 (IC base=+0.279)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.317 (n=496)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.293 (n=739)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.289)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.382 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `1723.4194` → IC=+0.297 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1723.4194 (IC base=+0.289)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.444 (n=717)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.440)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.440 (n=596)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.440 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.440)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.441 (n=809)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.440)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.439 (n=342)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.440 (n=297)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.435 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.436)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.450 (n=335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.445)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.451 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.445)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.447 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.445)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.446 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.445)

- **PATRÓN** `libro_liquidez` > `2127.0131` → IC=+0.453 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2127.0131 (IC base=+0.445)

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
  - _Potencial_: sin este filtro IC_bueno=-0.228 (n=90)

- **FILTRO** `py_entrada` > `0.735` → IC=-0.365 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=76)

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
  - _Potencial_: sin este filtro IC_bueno=-0.228 (n=90)

- **FILTRO** `py_entrada` > `0.735` → IC=-0.365 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=76)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4777` → IC=+0.134 (n=12220)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.4777 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.983` → IC=+0.246 (n=4073)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.983 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.7795` → IC=+0.261 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7795 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` < `0.3719` → IC=+0.253 (n=3348)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3719 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.971` → IC=+0.185 (n=4606)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 5.971 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `1.2074` → IC=+0.252 (n=3498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2074 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` > `0.6202` → IC=+0.257 (n=3498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6202 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.3025` → IC=+0.232 (n=1231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3025 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` > `2.343` → IC=+0.224 (n=3923)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.343 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.5667` → IC=+0.141 (n=15030)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5667 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.587` → IC=+0.186 (n=1015)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.587 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.1525` → IC=+0.185 (n=5370)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.1525 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `1.1879` → IC=+0.181 (n=5757)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 1.1879 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.0511` → IC=+0.182 (n=2610)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.0511 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2949` → IC=+0.231 (n=1440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2949 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.6723` → IC=+0.208 (n=3268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6723 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `110.0` → IC=+0.219 (n=9646)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 110.0 (IC base=+0.074)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.213 (n=901)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.191)

- **PATRÓN** `drift_60min` |x|≤ `0.3482` → IC=+0.195 (n=2683)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.3482 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.203 (n=1298)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.196 (n=1800)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 11.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `0.9754` → IC=+0.276 (n=1216)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9754 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.105` → IC=+0.278 (n=1162)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.105 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.244 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `2.2809` → IC=+0.208 (n=1156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2809 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.204 (n=2823)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `2092.1` → IC=+0.210 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2092.1 (IC base=+0.191)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.204 (n=1588)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.235 (n=2229)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0082 (IC base=+0.233)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.234 (n=1011)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0073 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.0878` → IC=+0.265 (n=742)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0878 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.257 (n=811)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.5113` → IC=+0.255 (n=2224)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5113 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.795` → IC=+0.234 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.795 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` < `0.0939` → IC=+0.236 (n=1973)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0939 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.2861` → IC=+0.243 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2861 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.4422` → IC=+0.231 (n=697)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4422 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.6562` → IC=+0.242 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6562 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=2459)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `1567.2992` → IC=+0.243 (n=2223)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1567.2992 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.231 (n=791)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.233)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.236 (n=962)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.223)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.225 (n=989)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.1063` → IC=+0.258 (n=960)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1063 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=2287)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.223 (n=2227)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.9624` → IC=+0.272 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9624 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` > `0.1296` → IC=+0.229 (n=1207)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1296 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.434` → IC=+0.259 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.434 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `1.2394` → IC=+0.225 (n=2182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2394 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `0.6219` → IC=+0.227 (n=2181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6219 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.276` → IC=+0.246 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.276 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `2.4328` → IC=+0.248 (n=716)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4328 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.151 (n=2214)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0057 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.0752` → IC=+0.170 (n=738)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.0752 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.162 (n=844)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.7296` → IC=+0.177 (n=2212)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.7296 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.1305` → IC=+0.154 (n=2041)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1305 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.129` → IC=+0.150 (n=358)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 11.129 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.236` → IC=+0.142 (n=2023)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.236 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `1.1913` → IC=+0.142 (n=2212)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1913 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.0952` → IC=+0.164 (n=804)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.0952 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.449` → IC=+0.143 (n=2094)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.449 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.7847` → IC=+0.142 (n=1396)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.7847 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `222.0` → IC=+0.171 (n=892)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 222.0 (IC base=+0.134)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.209 (n=923)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.196 (n=2901)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.194 (n=2482)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.272 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.333` → IC=+0.264 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.333 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.195 (n=2440)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.352` → IC=+0.209 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.352 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `2.7012` → IC=+0.210 (n=1215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7012 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=3277)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `1993.7784` → IC=+0.201 (n=1255)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1993.7784 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.0087` → IC=+0.224 (n=1641)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0087 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.1771` → IC=+0.225 (n=1083)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1771 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.250 (n=926)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.0082` → IC=+0.275 (n=820)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0082 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.533` → IC=+0.260 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.533 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3479` → IC=+0.255 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3479 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `1.7274` → IC=+0.218 (n=1023)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7274 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.7264` → IC=+0.229 (n=1054)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7264 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `2070.398` → IC=+0.234 (n=819)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2070.398 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.220 (n=2009)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.139 (n=142)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=3337)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.159 (n=503)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0036 (IC base=+0.049)

- **PATRÓN** `ibs_20min` > `0.9545` → IC=+0.220 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9545 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `0.1324` → IC=+0.320 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1324 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` < `0.1849` → IC=+0.320 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1849 (IC base=+0.049)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.077` → IC=+0.181 (n=1069)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 5.077 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` < `0.858` → IC=+0.331 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.858 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` > `1.2365` → IC=+0.342 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2365 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` < `0.1741` → IC=+0.320 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1741 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.2985` → IC=+0.335 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2985 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` < `1.4081` → IC=+0.338 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4081 (IC base=+0.049)

- **PATRÓN** `ballena_activa_n` < `149.0` → IC=+0.326 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 149.0 (IC base=+0.049)

- **PATRÓN** `ibs_20min` < `0.0951` → IC=+0.168 (n=871)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.0951 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` > `0.6765` → IC=+0.162 (n=211)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.6765 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.136 (n=1365)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1292 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` < `0.8509` → IC=+0.149 (n=1000)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8509 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.2866` → IC=+0.201 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2866 (IC base=+0.034)

- **PATRÓN** `volumen_spike_ratio` > `1.5114` → IC=+0.150 (n=1282)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.5114 (IC base=+0.034)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.174 (n=90)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=508)

- **FILTRO** `ibs_20min` < `0.2821` → IC=-0.195 (n=149)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2821
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=449)

- **FILTRO** `ibs_20min` > `0.2209` → IC=-0.131 (n=3305)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2209
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=1629)

- **FILTRO** `sigma_ewma_delta_pct` > `8.666` → IC=-0.235 (n=507)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.666
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=4427)

- **PATRÓN** `ibs_20min` > `0.7857` → IC=+0.180 (n=204)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.7857 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` > `1.012` → IC=+0.283 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.012 (IC base=+0.030)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.37` → IC=+0.130 (n=209)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 2.37 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` < `0.57` → IC=+0.258 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.57 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` > `0.992` → IC=+0.288 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.992 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` < `0.0844` → IC=+0.270 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0844 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` < `2.1931` → IC=+0.281 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1931 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` > `1.5504` → IC=+0.254 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5504 (IC base=+0.030)

- **PATRÓN** `ibs_20min` < `0.2209` → IC=+0.150 (n=1629)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.2209 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` > `0.2682` → IC=+0.275 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2682 (IC base=-0.038)

- **PATRÓN** `volumen_regimen` < `0.7071` → IC=+0.288 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7071 (IC base=-0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.0789` → IC=+0.299 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0789 (IC base=-0.038)

- **PATRÓN** `volumen_spike_ratio` < `2.3831` → IC=+0.299 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3831 (IC base=-0.038)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6268` → IC=-0.183 (n=879)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6268
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=2641)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.162 (n=899)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=2621)

- **FILTRO** `ibs_20min` > `0.7576` → IC=-0.204 (n=1289)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7576
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=3882)

- **PATRÓN** `dist_vwap_pct` > `0.7472` → IC=+0.326 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7472 (IC base=-0.071)

- **PATRÓN** `dist_vwap_pct` < `0.2654` → IC=+0.299 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2654 (IC base=-0.071)

- **PATRÓN** `volumen_regimen` < `1.1386` → IC=+0.294 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1386 (IC base=-0.071)

- **PATRÓN** `volumen_regimen` > `0.7043` → IC=+0.310 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7043 (IC base=-0.071)

- **PATRÓN** `volumen_pendiente_norm` < `0.1011` → IC=+0.299 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1011 (IC base=-0.071)

- **PATRÓN** `volumen_pendiente_norm` > `0.0729` → IC=+0.295 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0729 (IC base=-0.071)

- **PATRÓN** `volumen_spike_ratio` < `1.4208` → IC=+0.325 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4208 (IC base=-0.071)

- **PATRÓN** `volumen_spike_ratio` > `1.8519` → IC=+0.297 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8519 (IC base=-0.071)

- **PATRÓN** `dist_vwap_pct` > `0.8089` → IC=+0.282 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8089 (IC base=-0.008)

- **PATRÓN** `volumen_regimen` > `1.0723` → IC=+0.280 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0723 (IC base=-0.008)

- **PATRÓN** `volumen_pendiente_norm` > `0.1026` → IC=+0.281 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1026 (IC base=-0.008)

- **PATRÓN** `volumen_spike_ratio` < `2.1643` → IC=+0.262 (n=1109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1643 (IC base=-0.008)

- **PATRÓN** `volumen_spike_ratio` > `1.424` → IC=+0.262 (n=1260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.424 (IC base=-0.008)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.204 (n=5380)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0096 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.4565` → IC=+0.187 (n=14401)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4565 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.6755` → IC=+0.291 (n=1577)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6755 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.639` → IC=+0.156 (n=7215)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.639 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `1.1742` → IC=+0.256 (n=5923)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1742 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `0.6894` → IC=+0.262 (n=5291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6894 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.2396` → IC=+0.270 (n=1768)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2396 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `2.6394` → IC=+0.265 (n=3165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6394 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.287 (n=9057)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.096)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.163 (n=5186)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0091 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.5355` → IC=+0.161 (n=13667)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.5355 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.2414` → IC=+0.261 (n=4779)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2414 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.1947` → IC=+0.266 (n=1620)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1947 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2941` → IC=+0.314 (n=1017)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2941 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `1.5783` → IC=+0.285 (n=3033)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5783 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.2682` → IC=+0.279 (n=3125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2682 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.289 (n=6815)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 78.0 (IC base=+0.075)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.3697` → IC=-0.166 (n=1469)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3697
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=2988)

- **FILTRO** `ibs_20min` > `0.7476` → IC=-0.202 (n=926)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7476
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=2780)

- **FILTRO** `sigma_ewma_delta_pct` > `4.528` → IC=-0.195 (n=811)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.528
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=2895)

- **PATRÓN** `ibs_20min` > `0.9114` → IC=+0.296 (n=1115)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9114 (IC base=+0.033)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.098` → IC=+0.212 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.098 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` > `0.2294` → IC=+0.298 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2294 (IC base=+0.033)

- **PATRÓN** `volumen_spike_ratio` < `1.4472` → IC=+0.227 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4472 (IC base=+0.033)

- **PATRÓN** `volumen_spike_ratio` > `2.2427` → IC=+0.264 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2427 (IC base=+0.033)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.263 (n=967)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.033)

- **PATRÓN** `ibs_20min` < `0.1593` → IC=+0.160 (n=927)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1593 (IC base=-0.027)

- **PATRÓN** `volumen_pendiente_norm` < `0.0734` → IC=+0.414 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0734 (IC base=-0.027)

- **PATRÓN** `volumen_spike_ratio` < `2.4828` → IC=+0.402 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4828 (IC base=-0.027)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.401 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=-0.027)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1138` → IC=+0.206 (n=817)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1138 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `1.197` → IC=+0.182 (n=1557)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.197 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `0.6813` → IC=+0.191 (n=1391)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 0.6813 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` < `0.0744` → IC=+0.182 (n=1440)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` < 0.0744 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.2738` → IC=+0.211 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2738 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.4225` → IC=+0.208 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4225 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` > `2.4786` → IC=+0.188 (n=511)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.4786 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `220.0` → IC=+0.233 (n=671)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 220.0 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.1086` → IC=+0.232 (n=972)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1086 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` > `0.6206` → IC=+0.235 (n=984)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6206 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2713` → IC=+0.297 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2713 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.5384` → IC=+0.234 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5384 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1658` → IC=+0.251 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1658 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.299 (n=795)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.260)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.266 (n=2505)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.260)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.261 (n=2140)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.260)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.306 (n=1243)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.27` → IC=+0.293 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.27 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` < `0.1325` → IC=+0.271 (n=2181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1325 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` > `1.6126` → IC=+0.266 (n=2296)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6126 (IC base=+0.260)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.271 (n=2807)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `1981.7532` → IC=+0.282 (n=1081)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1981.7532 (IC base=+0.260)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.331 (n=924)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.1809` → IC=+0.306 (n=896)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1809 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.326 (n=786)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.290)

- **PATRÓN** `ibs_20min` < `0.3636` → IC=+0.292 (n=2036)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3636 (IC base=+0.290)

- **PATRÓN** `ibs_20min` > `0.25` → IC=+0.293 (n=926)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.25 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.68` → IC=+0.311 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.68 (IC base=+0.290)

- **PATRÓN** `volumen_pendiente_norm` < `0.1968` → IC=+0.288 (n=1979)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1968 (IC base=+0.290)

- **PATRÓN** `volumen_pendiente_norm` > `0.3414` → IC=+0.306 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3414 (IC base=+0.290)

- **PATRÓN** `volumen_spike_ratio` < `1.7226` → IC=+0.302 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7226 (IC base=+0.290)

- **PATRÓN** `volumen_spike_ratio` > `2.6513` → IC=+0.298 (n=878)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6513 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `2062.62` → IC=+0.315 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2062.62 (IC base=+0.290)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.286 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.290)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7452` → IC=-0.184 (n=959)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7452
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=2881)

- **PATRÓN** `ibs_20min` > `0.8859` → IC=+0.173 (n=900)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.8859 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` > `0.1528` → IC=+0.223 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1528 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` < `0.3691` → IC=+0.227 (n=1206)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3691 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` < `1.0157` → IC=+0.239 (n=1091)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0157 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.1014` → IC=+0.244 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1014 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` < `1.3919` → IC=+0.249 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3919 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` > `2.1373` → IC=+0.231 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1373 (IC base=+0.028)

- **PATRÓN** `ballena_activa_n` < `108.0` → IC=+0.261 (n=1076)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 108.0 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` < `0.1923` → IC=+0.228 (n=833)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1923 (IC base=-0.000)

- **PATRÓN** `volumen_regimen` < `1.0374` → IC=+0.233 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0374 (IC base=-0.000)

- **PATRÓN** `volumen_pendiente_norm` < `0.1021` → IC=+0.243 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1021 (IC base=-0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.288 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=-0.000)

- **PATRÓN** `volumen_spike_ratio` < `1.8013` → IC=+0.267 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8013 (IC base=-0.000)

- **PATRÓN** `volumen_spike_ratio` > `2.4561` → IC=+0.258 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4561 (IC base=-0.000)

- **PATRÓN** `ballena_activa_n` < `127.0` → IC=+0.254 (n=812)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 127.0 (IC base=-0.000)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7632` → IC=-0.204 (n=1704)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7632
  - _Potencial_: sin este filtro IC_bueno=+0.298 (n=1708)

- **FILTRO** `ibs_20min` > `0.6538` → IC=-0.235 (n=844)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6538
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=2535)

- **FILTRO** `sigma_ewma_delta_pct` > `8.569` → IC=-0.237 (n=386)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.569
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=2993)

- **PATRÓN** `ibs_20min` > `0.7632` → IC=+0.298 (n=1708)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7632 (IC base=+0.048)

- **PATRÓN** `dist_vwap_pct` > `0.213` → IC=+0.331 (n=769)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.213 (IC base=+0.048)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.606` → IC=+0.168 (n=534)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.606 (IC base=+0.048)

- **PATRÓN** `volumen_regimen` < `0.8456` → IC=+0.328 (n=860)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8456 (IC base=+0.048)

- **PATRÓN** `volumen_regimen` > `0.6292` → IC=+0.316 (n=1290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6292 (IC base=+0.048)

- **PATRÓN** `volumen_pendiente_norm` < `0.1585` → IC=+0.315 (n=1337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1585 (IC base=+0.048)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.351 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.048)

- **PATRÓN** `volumen_spike_ratio` < `1.4432` → IC=+0.336 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4432 (IC base=+0.048)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.341 (n=858)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.048)

- **PATRÓN** `ibs_20min` < `0.5556` → IC=+0.141 (n=2242)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5556 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.2098` → IC=+0.248 (n=986)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2098 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` < `0.7067` → IC=+0.259 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7067 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` > `1.1839` → IC=+0.240 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1839 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` < `0.0996` → IC=+0.243 (n=1024)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0996 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.0733` → IC=+0.253 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0733 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` < `2.4232` → IC=+0.254 (n=1036)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4232 (IC base=+0.030)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.271 (n=1050)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 53.0 (IC base=+0.030)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.341 (n=1642)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.296)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.311 (n=884)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.296)

- **PATRÓN** `ibs_20min` > `0.6511` → IC=+0.329 (n=1838)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6511 (IC base=+0.296)

- **PATRÓN** `dist_vwap_pct` > `0.2113` → IC=+0.326 (n=1045)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2113 (IC base=+0.296)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.778` → IC=+0.317 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.778 (IC base=+0.296)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.306 (n=1838)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6279 (IC base=+0.296)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.340 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.296)

- **PATRÓN** `volumen_spike_ratio` > `1.4265` → IC=+0.308 (n=1760)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4265 (IC base=+0.296)

- **PATRÓN** `libro_liquidez` > `2474.544` → IC=+0.309 (n=1642)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2474.544 (IC base=+0.296)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.330 (n=1559)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.296)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.331 (n=1298)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.298)

- **PATRÓN** `drift_60min` |x|≤ `0.1879` → IC=+0.302 (n=855)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1879 (IC base=+0.298)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.306 (n=973)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.298)

- **PATRÓN** `ibs_20min` < `0.3676` → IC=+0.323 (n=1943)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3676 (IC base=+0.298)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.518` → IC=+0.308 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.518 (IC base=+0.298)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.013` → IC=+0.299 (n=2314)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.013 (IC base=+0.298)

- **PATRÓN** `volumen_regimen` < `0.7185` → IC=+0.300 (n=855)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7185 (IC base=+0.298)

- **PATRÓN** `volumen_regimen` > `1.2272` → IC=+0.326 (n=648)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2272 (IC base=+0.298)

- **PATRÓN** `volumen_pendiente_norm` > `0.2824` → IC=+0.351 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2824 (IC base=+0.298)

- **PATRÓN** `volumen_spike_ratio` < `1.4133` → IC=+0.305 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4133 (IC base=+0.298)

- **PATRÓN** `volumen_spike_ratio` > `2.1331` → IC=+0.300 (n=803)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1331 (IC base=+0.298)

- **PATRÓN** `libro_liquidez` > `2649.5572` → IC=+0.303 (n=1295)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2649.5572 (IC base=+0.298)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.184 (n=3962)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0048 (IC base=+0.178)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.220 (n=3954)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.3461` → IC=+0.188 (n=10434)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3461 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=12314)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `0.5603` → IC=+0.232 (n=11856)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5603 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `0.1663` → IC=+0.208 (n=4903)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1663 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.355` → IC=+0.255 (n=2339)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.355 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `1.1952` → IC=+0.168 (n=7869)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1952 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` > `0.6271` → IC=+0.163 (n=7869)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6271 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2937` → IC=+0.201 (n=1733)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2937 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `2.5994` → IC=+0.188 (n=3827)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.5994 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `2011.3648` → IC=+0.183 (n=10592)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2011.3648 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.196 (n=10772)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 98.0 (IC base=+0.178)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.186 (n=7630)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0068 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.0801` → IC=+0.224 (n=3807)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0801 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=4293)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` < `0.4968` → IC=+0.235 (n=11421)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4968 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` < `0.1746` → IC=+0.174 (n=8064)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.1746 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.126` → IC=+0.196 (n=1882)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.126 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.673` → IC=+0.178 (n=10578)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 3.673 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `1.1804` → IC=+0.163 (n=8159)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1804 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2921` → IC=+0.228 (n=1676)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2921 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `2.6228` → IC=+0.187 (n=3561)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6228 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.190 (n=10379)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 102.0 (IC base=+0.178)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.232 (n=665)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.3321` → IC=+0.226 (n=1987)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3321 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.221 (n=728)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.215 (n=1343)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.9243` → IC=+0.290 (n=1325)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9243 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.142` → IC=+0.330 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.142 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.271 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.2555` → IC=+0.222 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2555 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.219 (n=2110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2092.8686` → IC=+0.219 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2092.8686 (IC base=+0.208)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.245 (n=701)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.0973` → IC=+0.295 (n=680)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0973 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.248 (n=1388)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.245 (n=764)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.0092` → IC=+0.298 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0092 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` < `0.1002` → IC=+0.244 (n=1336)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1002 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.2955` → IC=+0.277 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2955 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` < `1.4323` → IC=+0.260 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4323 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `2.6765` → IC=+0.248 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6765 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.246 (n=1713)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `1548.958` → IC=+0.254 (n=1545)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1548.958 (IC base=+0.242)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.243 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.242)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.218 (n=597)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.1622` → IC=+0.184 (n=1192)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1622 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.171 (n=1881)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.3506` → IC=+0.223 (n=1788)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3506 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.1371` → IC=+0.214 (n=1104)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1371 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.468` → IC=+0.224 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.468 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `0.6921` → IC=+0.171 (n=787)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.6921 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` > `1.0696` → IC=+0.157 (n=811)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.0696 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.184 (n=283)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `1.5085` → IC=+0.171 (n=771)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5085 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `2.4896` → IC=+0.160 (n=583)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.4896 (IC base=+0.155)

- **PATRÓN** `ballena_activa_n` < `230.0` → IC=+0.171 (n=754)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 230.0 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.168 (n=1879)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0058 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.234` → IC=+0.171 (n=1653)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.234 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.190 (n=718)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.6117` → IC=+0.203 (n=1879)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6117 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.645` → IC=+0.204 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.645 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.2024` → IC=+0.161 (n=1879)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2024 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.0933` → IC=+0.144 (n=1582)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` < 0.0933 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.2735` → IC=+0.147 (n=293)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2735 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.4914` → IC=+0.150 (n=1760)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4914 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.4236` → IC=+0.146 (n=1760)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4236 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `233.0` → IC=+0.168 (n=744)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 233.0 (IC base=+0.144)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.229 (n=1336)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.3992` → IC=+0.223 (n=1761)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3992 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.216 (n=2074)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=1042)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.514` → IC=+0.293 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.514 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.3522` → IC=+0.230 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3522 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.7745` → IC=+0.212 (n=851)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7745 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.7121` → IC=+0.226 (n=877)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7121 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.218 (n=2365)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `1983.579` → IC=+0.221 (n=908)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1983.579 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.245 (n=1513)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0102 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.0954` → IC=+0.270 (n=573)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0954 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.288 (n=573)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.3548` → IC=+0.252 (n=1720)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3548 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.616` → IC=+0.277 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.616 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.3534` → IC=+0.273 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3534 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.7279` → IC=+0.241 (n=719)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7279 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.7325` → IC=+0.243 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7325 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2067.0984` → IC=+0.253 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2067.0984 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.231 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.234)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.173 (n=1914)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0074 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.4031` → IC=+0.165 (n=1914)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.4031 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=1987)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.3133` → IC=+0.210 (n=1914)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3133 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.1398` → IC=+0.196 (n=1191)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1398 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.936` → IC=+0.201 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.936 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `1.0351` → IC=+0.155 (n=1684)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0351 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1013` → IC=+0.178 (n=792)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1013 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `1.533` → IC=+0.152 (n=826)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.533 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `2.4972` → IC=+0.166 (n=626)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.4972 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `4749.981` → IC=+0.191 (n=1276)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 4749.981 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.158 (n=1852)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 143.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.157 (n=2019)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0071 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.3937` → IC=+0.147 (n=2017)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3937 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.180 (n=763)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.6801` → IC=+0.189 (n=2017)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6801 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.1544` → IC=+0.155 (n=2008)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1544 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.869` → IC=+0.157 (n=710)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 6.869 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.8593` → IC=+0.162 (n=1345)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8593 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2971` → IC=+0.202 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2971 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.8007` → IC=+0.136 (n=1255)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.8007 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `2.5324` → IC=+0.138 (n=628)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.5324 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `4455.908` → IC=+0.173 (n=1345)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4455.908 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `120.0` → IC=+0.132 (n=1616)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 120.0 (IC base=+0.129)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.128 (n=724)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0059 (IC base=+0.128)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.171 (n=982)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0101 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.4413` → IC=+0.129 (n=1904)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.4413 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=2204)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.4909` → IC=+0.215 (n=2163)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4909 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.1961` → IC=+0.191 (n=1277)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1961 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.679` → IC=+0.269 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.679 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `1.1851` → IC=+0.142 (n=2164)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1851 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` < `0.161` → IC=+0.136 (n=2195)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.161 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.4374` → IC=+0.147 (n=700)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4374 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `2845.8235` → IC=+0.213 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2845.8235 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.164 (n=659)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 20.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.137 (n=2214)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0106 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.1079` → IC=+0.170 (n=738)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1079 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=2241)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.5909` → IC=+0.220 (n=2216)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5909 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` < `0.2001` → IC=+0.147 (n=2072)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2001 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.49` → IC=+0.127 (n=448)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` > 7.49 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.533` → IC=+0.125 (n=1952)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` < 2.533 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.1756` → IC=+0.129 (n=2214)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.1756 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.2743` → IC=+0.154 (n=290)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.2743 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4517` → IC=+0.130 (n=684)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.4517 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `2.4249` → IC=+0.134 (n=684)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.4249 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2693.9146` → IC=+0.190 (n=1004)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2693.9146 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.126 (n=2010)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 50.0 (IC base=+0.119)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.243 (n=1791)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0128 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.2828` → IC=+0.228 (n=1337)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2828 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.221 (n=2080)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.227 (n=1359)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` > `0.6571` → IC=+0.256 (n=2005)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6571 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` > `0.1903` → IC=+0.225 (n=1320)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1903 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` < `0.4885` → IC=+0.221 (n=1776)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4885 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.61` → IC=+0.249 (n=913)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.61 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` < `1.1809` → IC=+0.222 (n=2005)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1809 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` > `0.6223` → IC=+0.226 (n=2005)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6223 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.268 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.283 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` < `2.15` → IC=+0.222 (n=1719)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.15 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `1.8029` → IC=+0.228 (n=1301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8029 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `2645.421` → IC=+0.230 (n=1337)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2645.421 (IC base=+0.219)

- **PATRÓN** `sigma_h` < `0.0098` → IC=+0.239 (n=684)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0098 (IC base=+0.226)

- **PATRÓN** `sigma_h` > `0.0225` → IC=+0.238 (n=930)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0225 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.0896` → IC=+0.260 (n=684)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0896 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.247 (n=1001)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` < `0.425` → IC=+0.255 (n=2053)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.425 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.2961` → IC=+0.234 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2961 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.326` → IC=+0.249 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.326 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.706` → IC=+0.234 (n=1832)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.706 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2775` → IC=+0.286 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2775 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.4331` → IC=+0.228 (n=1901)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4331 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2404.776` → IC=+0.232 (n=1832)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2404.776 (IC base=+0.226)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.208 (n=1346)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.177)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.182 (n=1019)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0086 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.3361` → IC=+0.188 (n=2684)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3361 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.209 (n=1503)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `0.729` → IC=+0.228 (n=2033)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.729 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.783` → IC=+0.193 (n=463)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.783 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.673` → IC=+0.205 (n=1309)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.673 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `0.8646` → IC=+0.196 (n=1819)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8646 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` > `0.6955` → IC=+0.181 (n=2437)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.6955 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.1008` → IC=+0.190 (n=1097)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.1008 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` < `1.4335` → IC=+0.194 (n=989)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4335 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `2.2004` → IC=+0.180 (n=1343)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.2004 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.181 (n=3453)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.02 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `2734.4955` → IC=+0.182 (n=2725)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2734.4955 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.190 (n=2832)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 151.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` < `0.3715` → IC=+0.163 (n=2139)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.3715 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.135 (n=1063)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 20.0 (IC base=+0.097)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.213 (n=381)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.0998` → IC=+0.221 (n=381)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0998 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.195 (n=779)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 8.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.6494` → IC=+0.227 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6494 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.3035` → IC=+0.189 (n=271)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.3035 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.109` → IC=+0.187 (n=369)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 3.109 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.828` → IC=+0.168 (n=917)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 6.828 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `0.8772` → IC=+0.194 (n=577)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.8772 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.0705` → IC=+0.175 (n=340)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.0705 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `2.2101` → IC=+0.177 (n=745)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.2101 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `1.414` → IC=+0.169 (n=846)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.414 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `14780.6856` → IC=+0.178 (n=576)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 14780.6856 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `155.0` → IC=+0.203 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 155.0 (IC base=+0.167)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.192 (n=339)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0028 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.3447` → IC=+0.140 (n=1015)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.3447 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.133 (n=971)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.6342` → IC=+0.168 (n=893)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.6342 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` < `0.1877` → IC=+0.143 (n=1030)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1877 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.715` → IC=+0.129 (n=195)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 8.715 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.16` → IC=+0.126 (n=917)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 3.16 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `1.0617` → IC=+0.151 (n=460)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.0617 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.172 (n=269)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `2.1137` → IC=+0.136 (n=883)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.1137 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `1.4037` → IC=+0.127 (n=1002)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.4037 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.123 (n=1315)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `306.0` → IC=+0.149 (n=866)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 306.0 (IC base=+0.123)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.248 (n=626)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.2023` → IC=+0.228 (n=624)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2023 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.227 (n=982)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.6792` → IC=+0.270 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6792 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.3558` → IC=+0.221 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3558 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` < `0.2052` → IC=+0.215 (n=844)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2052 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.948` → IC=+0.232 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.948 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` < `0.8407` → IC=+0.216 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8407 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` > `1.1816` → IC=+0.229 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1816 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.1588` → IC=+0.243 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1588 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.4127` → IC=+0.248 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4127 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.4427` → IC=+0.229 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4427 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.1008` → IC=+0.172 (n=312)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.1008 (IC base=+0.074)

- **PATRÓN** `libro_liquidez` > `7105.0758` → IC=+0.135 (n=623)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 7105.0758 (IC base=+0.074)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.167 (n=334)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0095 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.5372` → IC=+0.158 (n=737)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.5372 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.208 (n=354)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.270 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.9739` → IC=+0.231 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9739 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.134` → IC=+0.219 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.134 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `1.0549` → IC=+0.182 (n=649)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.0549 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` > `0.7162` → IC=+0.165 (n=658)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.7162 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.1652` → IC=+0.186 (n=205)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1652 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `2.4588` → IC=+0.158 (n=709)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.4588 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `2.1893` → IC=+0.173 (n=322)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.1893 (IC base=+0.158)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.161 (n=759)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.02 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `3065.6596` → IC=+0.194 (n=246)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 3065.6596 (IC base=+0.158)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.150 (n=664)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.5 (IC base=+0.066)

- **PATRÓN** `volumen_spike_ratio` < `1.5613` → IC=+0.127 (n=317)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.5613 (IC base=+0.066)

- **PATRÓN** `libro_liquidez` > `2782.2891` → IC=+0.164 (n=340)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2782.2891 (IC base=+0.066)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.122 (n=617)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 31.0 (IC base=+0.066)

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

- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.158 (n=191)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0119 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.163 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.61` → IC=+0.134 (n=214)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.61 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `1.1471` → IC=+0.296 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1471 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.969` → IC=+0.155 (n=56)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 4.969 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` > `0.6529` → IC=+0.120 (n=214)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` > 0.6529 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.174 (n=41)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.134 (n=173)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 17.0 (IC base=+0.113)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.182 (n=5147)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0047 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.221 (n=5147)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=16088)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.5574` → IC=+0.240 (n=13794)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5574 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.1631` → IC=+0.193 (n=5585)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1631 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.334` → IC=+0.252 (n=3778)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.334 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.2251` → IC=+0.169 (n=10347)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2251 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2909` → IC=+0.203 (n=2050)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2909 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6091` → IC=+0.196 (n=4998)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6091 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `1824.7572` → IC=+0.184 (n=15440)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1824.7572 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `75.0` → IC=+0.205 (n=12408)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 75.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.194 (n=6165)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0054 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.3809` → IC=+0.190 (n=12328)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.3809 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=5240)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.578` → IC=+0.242 (n=14009)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.578 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` < `0.176` → IC=+0.170 (n=8474)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.176 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.902` → IC=+0.207 (n=1954)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.902 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.646` → IC=+0.189 (n=13522)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 3.646 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `0.705` → IC=+0.160 (n=4166)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.705 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.2893` → IC=+0.252 (n=1887)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2893 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.611` → IC=+0.198 (n=4402)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.611 (IC base=+0.187)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.214 (n=8613)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.187)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.237 (n=847)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.3498` → IC=+0.220 (n=2532)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3498 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.230 (n=1224)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.222 (n=1706)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.326 (n=976)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.662` → IC=+0.348 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.662 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.2784` → IC=+0.285 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2784 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.2691` → IC=+0.234 (n=1100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2691 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.234 (n=2648)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `2014.8787` → IC=+0.230 (n=1148)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2014.8787 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.234 (n=1054)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.217)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.262 (n=2148)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.1217` → IC=+0.274 (n=945)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1217 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.266 (n=1949)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` < `0.4991` → IC=+0.285 (n=2145)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4991 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.385` → IC=+0.264 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.385 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` < `0.0955` → IC=+0.258 (n=1910)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0955 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.2829` → IC=+0.276 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2829 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `2.2756` → IC=+0.267 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2756 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.259 (n=2379)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1563.22` → IC=+0.268 (n=2145)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1563.22 (IC base=+0.258)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.261 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.258)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.201 (n=842)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1771` → IC=+0.163 (n=1663)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1771 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=2601)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.2597` → IC=+0.207 (n=2494)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2597 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1246` → IC=+0.193 (n=1335)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1246 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.648` → IC=+0.163 (n=410)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.648 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.174` → IC=+0.155 (n=2286)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.174 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.629` → IC=+0.175 (n=833)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.629 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.071` → IC=+0.153 (n=2228)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.071 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2706` → IC=+0.173 (n=353)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2706 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.173` → IC=+0.159 (n=2143)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.173 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.525` → IC=+0.155 (n=2176)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.525 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `10297.6968` → IC=+0.151 (n=2494)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 10297.6968 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `268.0` → IC=+0.182 (n=1048)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 268.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.164 (n=2087)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.2565` → IC=+0.163 (n=1836)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.2565 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=791)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.6986` → IC=+0.198 (n=2086)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.6986 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.1329` → IC=+0.165 (n=1934)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1329 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.218` → IC=+0.158 (n=463)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 9.218 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.473` → IC=+0.145 (n=2103)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 6.473 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.1835` → IC=+0.154 (n=2086)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.1835 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.217` → IC=+0.197 (n=391)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.217 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.4292` → IC=+0.150 (n=1983)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4292 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.7706` → IC=+0.161 (n=1322)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7706 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `338.0` → IC=+0.146 (n=1261)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 338.0 (IC base=+0.145)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.248 (n=855)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.229 (n=2679)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.227 (n=2301)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=952)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.36` → IC=+0.318 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.36 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` < `0.2095` → IC=+0.224 (n=2610)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2095 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.698` → IC=+0.239 (n=1127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.698 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.231 (n=3029)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1853.9484` → IC=+0.235 (n=1709)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1853.9484 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.243 (n=2113)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.1806` → IC=+0.254 (n=1056)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1806 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.267 (n=909)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.025` → IC=+0.302 (n=800)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.025 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.071` → IC=+0.290 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.071 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3447` → IC=+0.295 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3447 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.7283` → IC=+0.236 (n=1000)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7283 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1354` → IC=+0.248 (n=1515)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1354 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `2063.0384` → IC=+0.266 (n=800)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2063.0384 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.254 (n=1042)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.240)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.202 (n=1166)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.4204` → IC=+0.157 (n=2647)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.4204 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.158 (n=2750)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.2536` → IC=+0.193 (n=2646)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.2536 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.141` → IC=+0.168 (n=1425)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.141 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.174` → IC=+0.159 (n=1074)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 4.174 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.8725` → IC=+0.162 (n=1766)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8725 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.183 (n=348)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.283 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.52` → IC=+0.166 (n=1136)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.52 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `2.1716` → IC=+0.159 (n=1170)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.1716 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `6925.4045` → IC=+0.238 (n=1200)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6925.4045 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.171 (n=1122)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 77.0 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.189 (n=731)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0033 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.4396` → IC=+0.140 (n=2193)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4396 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=804)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.7398` → IC=+0.186 (n=2193)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.7398 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.1491` → IC=+0.144 (n=1973)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1491 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.146` → IC=+0.176 (n=334)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 11.146 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.8747` → IC=+0.140 (n=1463)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.8747 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2971` → IC=+0.235 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2971 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `2.2246` → IC=+0.133 (n=1854)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.2246 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `1.4284` → IC=+0.138 (n=2106)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.4284 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `5235.3611` → IC=+0.203 (n=994)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5235.3611 (IC base=+0.129)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.147 (n=1779)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0083 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=977)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.4481` → IC=+0.199 (n=2665)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.4481 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `1.0588` → IC=+0.206 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0588 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.855` → IC=+0.267 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.855 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `0.8849` → IC=+0.149 (n=1777)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8849 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` < `0.0984` → IC=+0.126 (n=2507)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.0984 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.136 (n=344)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `2.4762` → IC=+0.125 (n=2601)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.4762 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `1.4651` → IC=+0.127 (n=2601)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.4651 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.130 (n=2727)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2873.0862` → IC=+0.253 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2873.0862 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.137 (n=827)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 25.0 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.142 (n=2552)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0111 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1341` → IC=+0.159 (n=851)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1341 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.160 (n=1191)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 15.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.6397` → IC=+0.215 (n=2546)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6397 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.2162` → IC=+0.139 (n=2170)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.2162 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.348` → IC=+0.135 (n=2450)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 3.348 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.6416` → IC=+0.140 (n=849)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.6416 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2236` → IC=+0.172 (n=428)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2236 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4357` → IC=+0.148 (n=791)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4357 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2724.0258` → IC=+0.211 (n=849)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2724.0258 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.139 (n=2093)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 48.0 (IC base=+0.120)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0136` → IC=+0.244 (n=2271)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0136 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=2649)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.235 (n=1697)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.607` → IC=+0.270 (n=2270)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.607 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.1993` → IC=+0.243 (n=1400)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1993 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.737` → IC=+0.269 (n=852)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.737 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` < `1.2312` → IC=+0.231 (n=2541)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2312 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.6424` → IC=+0.229 (n=2541)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6424 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2358` → IC=+0.248 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2358 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `2.5103` → IC=+0.244 (n=823)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5103 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.227 (n=3294)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2652.5528` → IC=+0.238 (n=1694)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2652.5528 (IC base=+0.226)

- **PATRÓN** `sigma_h` > `0.0229` → IC=+0.248 (n=1199)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0229 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.234 (n=2480)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` < `0.5098` → IC=+0.265 (n=2644)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5098 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.188` → IC=+0.259 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.188 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `1.2292` → IC=+0.255 (n=881)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2292 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.299 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.4297` → IC=+0.229 (n=2448)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4297 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `2418.0544` → IC=+0.230 (n=2362)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2418.0544 (IC base=+0.227)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.221 (n=2403)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.227)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.186 (n=4618)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.239 (n=1559)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.5036` → IC=+0.210 (n=4664)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5036 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=1666)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.9404` → IC=+0.246 (n=1555)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9404 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `0.1722` → IC=+0.205 (n=1781)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1722 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` < `0.4337` → IC=+0.208 (n=3346)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4337 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.152` → IC=+0.211 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.152 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.648` → IC=+0.201 (n=4161)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.648 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `0.7064` → IC=+0.217 (n=1500)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7064 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `0.886` → IC=+0.205 (n=2274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.886 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.166` → IC=+0.221 (n=1304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.166 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `1.4536` → IC=+0.206 (n=1532)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4536 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `2.2626` → IC=+0.204 (n=2083)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2626 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=3613)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `2599.0182` → IC=+0.207 (n=4664)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2599.0182 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.232 (n=1164)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.184)

- **PATRÓN** `drift_60min` |x|≤ `0.4905` → IC=+0.200 (n=3475)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4905 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=1170)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.200 (n=1569)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` < `0.18` → IC=+0.200 (n=1530)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.18 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` > `0.6733` → IC=+0.196 (n=599)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.6733 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` < `0.2386` → IC=+0.181 (n=3143)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.2386 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.149` → IC=+0.192 (n=3480)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 6.149 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` < `1.0969` → IC=+0.195 (n=2888)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 1.0969 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` < `0.0972` → IC=+0.189 (n=3177)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.0972 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` < `1.5312` → IC=+0.189 (n=1509)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.5312 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `1.806` → IC=+0.191 (n=2286)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 1.806 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.186 (n=4618)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.184)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.195 (n=2995)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 162.0 (IC base=+0.184)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.254 (n=568)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.0885` → IC=+0.271 (n=216)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0885 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.242 (n=676)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.239 (n=301)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.5007` → IC=+0.262 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5007 (IC base=+0.235)

- **PATRÓN** `dist_vwap_pct` < `0.3306` → IC=+0.249 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3306 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.115` → IC=+0.243 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.115 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.615` → IC=+0.238 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.615 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` < `1.2148` → IC=+0.242 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2148 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` > `0.8602` → IC=+0.252 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8602 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.333 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` < `1.8328` → IC=+0.245 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8328 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `12380.2329` → IC=+0.251 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12380.2329 (IC base=+0.235)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.242 (n=526)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.369` → IC=+0.175 (n=1192)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.369 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=431)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.190 (n=453)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 5.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` < `0.1485` → IC=+0.189 (n=525)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.1485 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.6081` → IC=+0.170 (n=540)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.6081 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.6887` → IC=+0.205 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6887 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` < `0.1571` → IC=+0.163 (n=1171)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1571 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.407` → IC=+0.182 (n=1172)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 6.407 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `0.8855` → IC=+0.198 (n=795)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.8855 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.216` → IC=+0.184 (n=248)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.216 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.409` → IC=+0.173 (n=396)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.409 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `1.8008` → IC=+0.176 (n=791)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.8008 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `11334.4505` → IC=+0.176 (n=1191)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 11334.4505 (IC base=+0.163)

- **PATRÓN** `ballena_activa_n` < `699.0` → IC=+0.175 (n=1146)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 699.0 (IC base=+0.163)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.200 (n=235)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.173)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.189 (n=319)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0099 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.4317` → IC=+0.179 (n=618)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.4317 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.229 (n=253)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.994` → IC=+0.233 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.994 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.507` → IC=+0.218 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.507 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2086` → IC=+0.228 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2086 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.2548` → IC=+0.182 (n=467)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.2548 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `2541.2134` → IC=+0.216 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2541.2134 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.229 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.250 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.281 (n=39)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.2121` → IC=+0.263 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2121 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.442` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.442 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `2.4518` → IC=+0.250 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4518 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.861` → IC=+0.250 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.861 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `2407.5596` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2407.5596 (IC base=+0.227)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.008` → IC=+0.213 (n=1338)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.462` → IC=+0.207 (n=1338)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.462 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=483)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.5141` → IC=+0.211 (n=892)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5141 (IC base=+0.199)

- **PATRÓN** `ibs_20min` > `0.8789` → IC=+0.205 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8789 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.152` → IC=+0.206 (n=1203)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.152 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `0.881` → IC=+0.200 (n=892)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.881 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` > `1.2372` → IC=+0.210 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2372 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` < `0.1051` → IC=+0.201 (n=1231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1051 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.1639` → IC=+0.203 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1639 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `1.412` → IC=+0.217 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.412 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.201 (n=1367)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.247 (n=361)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.4952` → IC=+0.206 (n=1079)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4952 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.201 (n=422)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.189 (n=770)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 11.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.75` → IC=+0.188 (n=1079)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.75 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `0.0817` → IC=+0.185 (n=1079)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.0817 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `0.6705` → IC=+0.191 (n=189)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.6705 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.719` → IC=+0.187 (n=1100)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 6.719 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.6373` → IC=+0.224 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6373 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.0737` → IC=+0.197 (n=454)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.0737 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `1.4127` → IC=+0.206 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4127 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `1.7767` → IC=+0.184 (n=704)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.7767 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `7108.3687` → IC=+0.193 (n=1079)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 7108.3687 (IC base=+0.182)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.211 (n=613)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.213 (n=659)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.260 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` > `0.7405` → IC=+0.239 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7405 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.252` → IC=+0.220 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.252 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `0.7001` → IC=+0.238 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7001 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` < `0.1071` → IC=+0.191 (n=629)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.1071 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.0795` → IC=+0.205 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0795 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `1.5672` → IC=+0.191 (n=299)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.5672 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `2.4766` → IC=+0.219 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4766 (IC base=+0.185)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.191 (n=809)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `3527.135` → IC=+0.210 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3527.135 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.204 (n=683)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 53.0 (IC base=+0.185)

- **PATRÓN** `sigma_h` < `0.0089` → IC=+0.203 (n=338)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0089 (IC base=+0.198)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.208 (n=231)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.6094` → IC=+0.224 (n=506)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6094 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.231 (n=344)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` < `0.7181` → IC=+0.216 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7181 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.5232` → IC=+0.215 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5232 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` < `0.3106` → IC=+0.203 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3106 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.952` → IC=+0.202 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.952 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.926` → IC=+0.205 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.926 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` < `0.7555` → IC=+0.207 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7555 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` > `0.9331` → IC=+0.205 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9331 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` < `0.1071` → IC=+0.225 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1071 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `2.1886` → IC=+0.234 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1886 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `2975.6047` → IC=+0.218 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2975.6047 (IC base=+0.198)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.232 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 47.0 (IC base=+0.198)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.161 (n=671)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0038 (IC base=+0.069)

- **PATRÓN** `ibs_20min` > `0.4045` → IC=+0.144 (n=1431)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.4045 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.1425` → IC=+0.137 (n=759)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.1425 (IC base=+0.069)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.319` → IC=+0.176 (n=316)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 11.319 (IC base=+0.069)

- **PATRÓN** `ibs_20min` < `0.1786` → IC=+0.268 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1786 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` < `0.0969` → IC=+0.146 (n=707)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.0969 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.626` → IC=+0.175 (n=118)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 10.626 (IC base=+0.072)

- **PATRÓN** `volumen_pendiente_norm` > `0.147` → IC=+0.209 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.147 (IC base=+0.072)

- **PATRÓN** `volumen_spike_ratio` < `2.6098` → IC=+0.131 (n=661)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 2.6098 (IC base=+0.072)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.135 (n=513)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0056 (IC base=+0.090)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.146 (n=173)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 18.0 (IC base=+0.090)

- **PATRÓN** `ibs_20min` > `0.537` → IC=+0.193 (n=431)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.537 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` > `0.119` → IC=+0.159 (n=253)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.119 (IC base=+0.090)

- **PATRÓN** `ibs_20min` < `0.0263` → IC=+0.282 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0263 (IC base=+0.084)

- **PATRÓN** `dist_vwap_pct` < `0.2112` → IC=+0.137 (n=362)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.2112 (IC base=+0.084)

- **PATRÓN** `volumen_pendiente_norm` > `0.0692` → IC=+0.172 (n=135)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.0692 (IC base=+0.084)

- **PATRÓN** `volumen_spike_ratio` < `2.5091` → IC=+0.125 (n=305)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 2.5091 (IC base=+0.084)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.153 (n=332)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0046 (IC base=+0.092)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.125 (n=467)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 7.0 (IC base=+0.092)

- **PATRÓN** `ibs_20min` > `0.6494` → IC=+0.204 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6494 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` > `0.1258` → IC=+0.188 (n=245)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1258 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.364` → IC=+0.250 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.364 (IC base=+0.092)

- **PATRÓN** `volumen_regimen` < `0.8145` → IC=+0.126 (n=311)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 0.8145 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `1632.0481` → IC=+0.132 (n=210)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 1632.0481 (IC base=+0.092)

- **PATRÓN** `ibs_20min` < `0.0123` → IC=+0.333 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0123 (IC base=+0.038)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.103` → IC=+0.237 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.103 (IC base=+0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.136` → IC=+0.197 (n=64)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.136 (IC base=+0.038)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` > `0.1333` → IC=-0.212 (n=57)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1333
  - _Potencial_: sin este filtro IC_bueno=+0.264 (n=172)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.162 (n=326)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.75 (IC base=+0.026)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.817` → IC=+0.150 (n=135)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 7.817 (IC base=+0.026)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.163 (n=203)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.01 (IC base=+0.092)

- **PATRÓN** `ibs_20min` < `0.1333` → IC=+0.264 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1333 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` > `0.2139` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.2139 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` < `0.3758` → IC=+0.175 (n=189)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.3758 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.807` → IC=+0.325 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.807 (IC base=+0.092)

- **PATRÓN** `volumen_regimen` > `1.0763` → IC=+0.250 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0763 (IC base=+0.092)

- **PATRÓN** `volumen_pendiente_norm` > `0.084` → IC=+0.260 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.084 (IC base=+0.092)

- **PATRÓN** `volumen_spike_ratio` < `2.193` → IC=+0.187 (n=132)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 2.193 (IC base=+0.092)

- **PATRÓN** `volumen_spike_ratio` > `2.5569` → IC=+0.211 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5569 (IC base=+0.092)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.210 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.092)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `8.0` → IC=-0.333 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=227)

- **FILTRO** `dist_vwap_pct` > `0.2348` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2348
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=274)

- **FILTRO** `volumen_spike_ratio` < `1.533` → IC=-0.196 (n=54)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.533
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=163)

- **FILTRO** `sigma_h` > `0.0052` → IC=-0.355 (n=60)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0052
  - _Potencial_: sin este filtro IC_bueno=-0.255 (n=182)

- **FILTRO** `dist_vwap_pct` > `0.4185` → IC=-0.413 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4185
  - _Potencial_: sin este filtro IC_bueno=-0.267 (n=221)

- **FILTRO** `sigma_ewma_delta_pct` > `10.676` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 10.676
  - _Potencial_: sin este filtro IC_bueno=-0.277 (n=218)

- **FILTRO** `volumen_pendiente_norm` > `0.0538` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0538
  - _Potencial_: sin este filtro IC_bueno=-0.259 (n=131)

- **FILTRO** `libro_liquidez` < `1287.125` → IC=-0.306 (n=60)

  - _Acción_: SKIP cuando `libro_liquidez` < 1287.125
  - _Potencial_: sin este filtro IC_bueno=-0.272 (n=182)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.273 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=75)

- **FILTRO** `volumen_spike_ratio` > `3.5274` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.5274
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=55)

- **FILTRO** `hora_utc` < `13.0` → IC=-0.300 (n=53)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=53)

- **FILTRO** `volumen_regimen` > `0.8213` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8213
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=80)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `hora_utc` < `5.0` → IC=-0.173 (n=47)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=52)

- **FILTRO** `ibs_20min` < `0.6568` → IC=-0.441 (n=32)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6568
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=67)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.375 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.246 (n=69)

- **FILTRO** `ibs_20min` > `0.538` → IC=-0.372 (n=45)

  - _Acción_: SKIP cuando `ibs_20min` > 0.538
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=46)

- **FILTRO** `dist_vwap_pct` > `0.1206` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1206
  - _Potencial_: sin este filtro IC_bueno=-0.258 (n=64)

- **PATRÓN** `ibs_20min` > `0.9464` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.9464 (IC base=-0.173)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_h` < `0.0063` → IC=-0.324 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=65)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=81)

- **FILTRO** `volumen_spike_ratio` < `1.6197` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.6197
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=54)

- **FILTRO** `dist_vwap_pct` < `0.219` → IC=-0.346 (n=24)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.219
  - _Potencial_: sin este filtro IC_bueno=-0.283 (n=21)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=23)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.165 (n=219)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0059 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.144 (n=178)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 17.0 (IC base=+0.103)

- **PATRÓN** `ibs_20min` > `0.68` → IC=+0.141 (n=483)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.68 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` > `0.5113` → IC=+0.189 (n=104)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.5113 (IC base=+0.103)

- **PATRÓN** `volumen_regimen` < `0.8548` → IC=+0.136 (n=322)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8548 (IC base=+0.103)

- **PATRÓN** `volumen_pendiente_norm` < `0.2851` → IC=+0.128 (n=442)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.2851 (IC base=+0.103)

- **PATRÓN** `volumen_spike_ratio` < `2.5067` → IC=+0.135 (n=381)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.5067 (IC base=+0.103)

- **PATRÓN** `ibs_20min` < `0.1613` → IC=+0.172 (n=501)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.1613 (IC base=+0.075)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.19` → IC=+0.188 (n=136)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 11.19 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2767` → IC=+0.136 (n=86)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.2767 (IC base=+0.075)

- **PATRÓN** `libro_liquidez` > `3239.2397` → IC=+0.153 (n=379)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3239.2397 (IC base=+0.075)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6599` → IC=-0.226 (n=49)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6599
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=150)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.244 (n=88)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.172 (n=178)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 12.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.183 (n=99)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 6.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.1524` → IC=+0.206 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1524 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.0938` → IC=+0.169 (n=267)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.0938 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.265` → IC=+0.163 (n=84)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 10.265 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.257` → IC=+0.165 (n=192)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 3.257 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `0.6211` → IC=+0.168 (n=263)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 0.6211 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.0706` → IC=+0.172 (n=202)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` < 0.0706 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2786` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2786 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.5202` → IC=+0.188 (n=232)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.5202 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.4427` → IC=+0.165 (n=231)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.4427 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `5251.0438` → IC=+0.161 (n=175)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 5251.0438 (IC base=+0.153)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1302` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1302
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=160)

- **FILTRO** `ibs_20min` > `0.2053` → IC=-0.133 (n=96)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2053
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=187)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.122 (n=154)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.005 (IC base=+0.081)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.161 (n=60)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 18.0 (IC base=+0.081)

- **PATRÓN** `ibs_20min` > `0.798` → IC=+0.120 (n=156)

  - _Acción_: Kelly boost +0.60€ cuando `ibs_20min` > 0.798 (IC base=+0.081)

- **PATRÓN** `volumen_pendiente_norm` < `0.1302` → IC=+0.123 (n=160)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1302 (IC base=+0.081)

- **PATRÓN** `volumen_spike_ratio` < `1.441` → IC=+0.187 (n=65)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.441 (IC base=+0.081)

- **PATRÓN** `ibs_20min` < `0.2053` → IC=+0.140 (n=187)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.2053 (IC base=+0.047)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.059` → IC=+0.245 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.059 (IC base=+0.047)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.4444` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4444
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=95)

- **FILTRO** `dist_vwap_pct` > `0.2724` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2724
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=101)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.309 (n=108)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.248)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.275 (n=149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.248)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.247 (n=160)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.248)

- **PATRÓN** `ibs_20min` > `0.6757` → IC=+0.264 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6757 (IC base=+0.248)

- **PATRÓN** `dist_vwap_pct` > `0.6436` → IC=+0.381 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6436 (IC base=+0.248)

- **PATRÓN** `dist_vwap_pct` < `0.2189` → IC=+0.246 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2189 (IC base=+0.248)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.333` → IC=+0.300 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.333 (IC base=+0.248)

- **PATRÓN** `volumen_regimen` < `0.7871` → IC=+0.298 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7871 (IC base=+0.248)

- **PATRÓN** `volumen_pendiente_norm` < `0.3005` → IC=+0.306 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.3005 (IC base=+0.248)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.328 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.248)

- **PATRÓN** `volumen_spike_ratio` < `1.4854` → IC=+0.378 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4854 (IC base=+0.248)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.253 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.248)

- **PATRÓN** `libro_liquidez` > `572.1322` → IC=+0.252 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 572.1322 (IC base=+0.248)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.321` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.321 (IC base=-0.083)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.323 (n=60)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3349` → IC=+0.304 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3349 (IC base=+0.297)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.377 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.297)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.452 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.297)

- **PATRÓN** `drift_60min` |x|≤ `0.9778` → IC=+0.360 (n=55)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9778 (IC base=+0.297)

- **PATRÓN** `ballena_activa_n` < `1115.0` → IC=+0.357 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1115.0 (IC base=+0.297)

- **PATRÓN** `drift_ventana_pct` |x|> `0.356` → IC=+0.241 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.356 (IC base=+0.222)

- **PATRÓN** `elapsed_s` > `185.1` → IC=+0.222 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 185.1 (IC base=+0.222)

- **PATRÓN** `elapsed_s` < `214.9` → IC=+0.255 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 214.9 (IC base=+0.222)

- **PATRÓN** `drift_15min` |x|≤ `2.0223` → IC=+0.256 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.0223 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `1.0086` → IC=+0.250 (n=58)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 1.0086 (IC base=+0.222)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.323 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.267 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.222)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.323 (n=60)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3349` → IC=+0.304 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3349 (IC base=+0.297)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.377 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.297)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.452 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.297)

- **PATRÓN** `drift_60min` |x|≤ `0.9778` → IC=+0.360 (n=55)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9778 (IC base=+0.297)

- **PATRÓN** `ballena_activa_n` < `1115.0` → IC=+0.357 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1115.0 (IC base=+0.297)

- **PATRÓN** `drift_ventana_pct` |x|> `0.356` → IC=+0.241 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.356 (IC base=+0.222)

- **PATRÓN** `elapsed_s` > `185.1` → IC=+0.222 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 185.1 (IC base=+0.222)

- **PATRÓN** `elapsed_s` < `214.9` → IC=+0.255 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 214.9 (IC base=+0.222)

- **PATRÓN** `drift_15min` |x|≤ `2.0223` → IC=+0.256 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.0223 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `1.0086` → IC=+0.250 (n=58)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 1.0086 (IC base=+0.222)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.323 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.267 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.222)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `libro_liquidez` > `2859.8474` → IC=+0.133 (n=540)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2859.8474 (IC base=+0.102)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2859.8474` → IC=+0.133 (n=540)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2859.8474 (IC base=+0.102)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=180)

- **FILTRO** `libro_liquidez` < `2761.3271` → IC=-0.186 (n=49)

  - _Acción_: SKIP cuando `libro_liquidez` < 2761.3271
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=147)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=249)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=66)

- **FILTRO** `ballena_activa_n` > `367.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `ballena_activa_n` > 367.0
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=41)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.149 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.188 (n=14)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=25)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=22)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` > `4.0` → IC=-0.167 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.136 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=108)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=3299)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=100)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=100)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.167 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=125)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.129 (n=227)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.495 (IC base=+0.027)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=1212)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=1166)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=708)

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
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=401)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=382)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.142 (n=160)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.495 (IC base=+0.018)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=825)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=825)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=729)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=729)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=219)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=219)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.132 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=168)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.126 (n=89)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=145)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=194)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=218)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=254)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.121 (n=56)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=197)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=231)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=337)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=337)

- **FILTRO** `libro_liquidez` < `598.969` → IC=-0.126 (n=121)

  - _Acción_: SKIP cuando `libro_liquidez` < 598.969
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=246)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=243)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.129 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=171)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.132 (n=1150)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=2990)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `restante_min` < `3.89` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `restante_min` < 3.89
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **FILTRO** `lag_apertura_s` > `66.61` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `lag_apertura_s` > 66.61
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.122 (n=202)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=213)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.169 (n=125)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` < 0.46 (IC base=+0.012)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.180 (n=48)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=208)

- **FILTRO** `lag_apertura_s` > `360.87` → IC=-0.146 (n=63)

  - _Acción_: SKIP cuando `lag_apertura_s` > 360.87
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=193)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **PATRÓN** `py_entrada` < `0.57` → IC=+0.148 (n=69)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.57 (IC base=+0.055)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.147 (n=290)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=99)

- **FILTRO** `lag_apertura_s` > `274.73` → IC=-0.142 (n=132)

  - _Acción_: SKIP cuando `lag_apertura_s` > 274.73
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=257)

- **FILTRO** `profundidad_ratio` < `37.6` → IC=-0.197 (n=97)

  - _Acción_: SKIP cuando `profundidad_ratio` < 37.6
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=292)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.254 (n=63)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=273)

- **PATRÓN** `py_entrada` < `0.46` → IC=+0.167 (n=88)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.46 (IC base=-0.035)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.125 (n=230)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=247)

- **FILTRO** `restante_min` < `3.8` → IC=-0.136 (n=234)

  - _Acción_: SKIP cuando `restante_min` < 3.8
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=243)

- **FILTRO** `lag_apertura_s` > `98.09` → IC=-0.171 (n=162)

  - _Acción_: SKIP cuando `lag_apertura_s` > 98.09
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=315)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.180 (n=73)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=297)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **PATRÓN** `py_entrada` > `0.49` → IC=+0.133 (n=145)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` > 0.49 (IC base=-0.011)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.147 (n=270)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=141)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.179 (n=107)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=397)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.165 (n=5373)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=17071)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.168 (n=5777)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=17417)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.192 (n=987)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=3056)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.165 (n=962)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=3192)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.139 (n=1066)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 1.0 (IC base=+0.038)

- **PATRÓN** `libro_liquidez` > `1417.8434` → IC=+0.135 (n=2022)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 1417.8434 (IC base=+0.038)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.126 (n=1932)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.5 (IC base=+0.014)

- **PATRÓN** `libro_liquidez` > `1536.66` → IC=+0.148 (n=1413)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 1536.66 (IC base=+0.014)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.175 (n=811)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=2502)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.173 (n=999)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=3088)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.184 (n=1057)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=3172)

- **PATRÓN** `ibs_20min` > `0.9632` → IC=+0.127 (n=1391)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` > 0.9632 (IC base=+0.036)

- **PATRÓN** `libro_liquidez` > `1844.2084` → IC=+0.125 (n=1390)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 1844.2084 (IC base=+0.036)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=2294)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2705)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=3445)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=422)

- **FILTRO** `py_entrada` < `0.435` → IC=-0.254 (n=132)

  - _Acción_: SKIP cuando `py_entrada` < 0.435
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=415)

### MOMENTUM_IBS_15M_FADE#DOGE#15min
- **FILTRO** `libro_liquidez` < `2574.706` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 2574.706
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `libro_liquidez` < `3613.7014` → IC=-0.152 (n=110)

  - _Acción_: SKIP cuando `libro_liquidez` < 3613.7014
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=224)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.193 (n=138)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=283)

- **FILTRO** `libro_liquidez` < `3730.8295` → IC=-0.170 (n=210)

  - _Acción_: SKIP cuando `libro_liquidez` < 3730.8295
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=211)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=855)

- **FILTRO** `libro_liquidez` < `2079.4719` → IC=-0.166 (n=345)

  - _Acción_: SKIP cuando `libro_liquidez` < 2079.4719
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=701)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=15569)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=34596)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=12172)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=37993)

- **FILTRO** `ibs_7min` < `0.2438` → IC=-0.230 (n=12541)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2438
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=37624)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.152 (n=17017)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=33148)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.238 (n=15423)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=48111)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.180 (n=15729)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=47805)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.145 (n=2514)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=6149)

- **FILTRO** `py_entrada` < `0.46` → IC=-0.235 (n=4305)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=4358)

- **FILTRO** `ibs_7min` < `0.7091` → IC=-0.248 (n=2856)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7091
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=5807)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.175 (n=1957)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=6706)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.270 (n=2729)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=8298)

- **FILTRO** `ibs_7min` > `0.775` → IC=-0.211 (n=2754)

  - _Acción_: SKIP cuando `ibs_7min` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=8273)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.263 (n=1940)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=6576)

- **FILTRO** `ibs_7min` < `0.7296` → IC=-0.195 (n=2128)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7296
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=6388)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.190 (n=2126)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6390)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.263 (n=2099)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=6548)

- **FILTRO** `ibs_7min` > `0.2665` → IC=-0.194 (n=2161)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2665
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=6486)

- **FILTRO** `ballena_activa_n` > `149.0` → IC=-0.182 (n=2158)

  - _Acción_: SKIP cuando `ballena_activa_n` > 149.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=6489)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.155 (n=2034)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=6213)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.316 (n=2008)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=6239)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.246 (n=2706)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=5541)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.192 (n=2057)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6190)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.249 (n=2683)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=9043)

- **FILTRO** `ibs_7min` > `0.7333` → IC=-0.175 (n=2931)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7333
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=8795)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.262 (n=1901)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=6298)

- **FILTRO** `ibs_7min` < `0.7327` → IC=-0.188 (n=2049)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7327
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=6150)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.192 (n=2024)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=6175)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.267 (n=1890)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=6611)

- **FILTRO** `ibs_7min` > `0.275` → IC=-0.179 (n=2125)

  - _Acción_: SKIP cuando `ibs_7min` > 0.275
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=6376)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.178 (n=2062)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=6439)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.283 (n=1937)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=6368)

- **FILTRO** `ibs_7min` < `0.2245` → IC=-0.234 (n=2076)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2245
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=6229)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.185 (n=2871)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=9280)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.280 (n=2038)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=6197)

- **FILTRO** `ibs_7min` < `0.2179` → IC=-0.220 (n=2058)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2179
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=6177)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.199 (n=1886)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=6349)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.210 (n=2783)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=8699)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=119)

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
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=821)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.128 (n=151)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=334)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.142 (n=163)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=321)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=435)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.129 (n=68)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=619)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=387)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3982` → IC=+0.148 (n=1075)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio` |x|> 0.3982 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.143 (n=499)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 14.0 (IC base=+0.131)

- **PATRÓN** `total_vol_5m` < `443.866` → IC=+0.165 (n=359)

  - _Acción_: Kelly boost +0.82€ cuando `total_vol_5m` < 443.866 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `3682.1352` → IC=+0.141 (n=488)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3682.1352 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.162 (n=365)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 13.0 (IC base=+0.131)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4367` → IC=+0.163 (n=84)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio` |x|> 0.4367 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.230 (n=120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `2596.4012` → IC=+0.233 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2596.4012 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.184 (n=115)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 9.0 (IC base=+0.150)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3994` → IC=+0.138 (n=222)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio` |x|> 0.3994 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.150 (n=78)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 3.0 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.132 (n=264)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.04 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2365.7446` → IC=+0.133 (n=148)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2365.7446 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.146 (n=145)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 13.0 (IC base=+0.121)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4156` → IC=+0.180 (n=145)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio` |x|> 0.4156 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.155 (n=224)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 4.0 (IC base=+0.132)

- **PATRÓN** `total_vol_5m` < `394.3776` → IC=+0.225 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 394.3776 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `7950.7251` → IC=+0.133 (n=145)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 7950.7251 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.201 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.132)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4332` → IC=+0.253 (n=87)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4332 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.169 (n=173)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 15.0 (IC base=+0.151)

- **PATRÓN** `total_vol_5m` < `8050.476` → IC=+0.172 (n=190)

  - _Acción_: Kelly boost +0.86€ cuando `total_vol_5m` < 8050.476 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `3074.545` → IC=+0.162 (n=190)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 3074.545 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.167 (n=61)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 27.0 (IC base=+0.151)

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

- **FILTRO** `sigma_h` > `0.006` → IC=-0.297 (n=205)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=403)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.177 (n=153)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0034 (IC base=-0.080)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0071` → IC=-0.351 (n=45)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0071
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=138)

- **FILTRO** `T_h` > `88.1766` → IC=-0.287 (n=45)

  - _Acción_: SKIP cuando `T_h` > 88.1766
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=138)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.312 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=-0.041)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `pct_vs_K` |x|> `7.7861` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.7861
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=40)

### PRICE_TARGET_GBM#SOL#atexpiry
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.224 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=-0.066)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.220 (n=423)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=141)

- **FILTRO** `T_h` > `71.5573` → IC=-0.186 (n=422)

  - _Acción_: SKIP cuando `T_h` > 71.5573
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=142)

- **FILTRO** `sigma_h` < `0.0049` → IC=-0.293 (n=119)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0049
  - _Potencial_: sin este filtro IC_bueno=-0.230 (n=357)

- **FILTRO** `pct_vs_K` |x|> `3.3883` → IC=-0.442 (n=118)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.3883
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=358)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `79.3043` → IC=-0.185 (n=125)

  - _Acción_: SKIP cuando `T_h` > 79.3043
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=63)

- **FILTRO** `pct_vs_K` |x|> `1.9536` → IC=-0.398 (n=86)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 1.9536
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=87)

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
- **FILTRO** `sigma_h` < `0.0096` → IC=-0.320 (n=120)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0096
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=40)

- **FILTRO** `T_h` > `135.9851` → IC=-0.281 (n=39)

  - _Acción_: SKIP cuando `T_h` > 135.9851
  - _Potencial_: sin este filtro IC_bueno=-0.240 (n=121)

- **FILTRO** `sigma_h` < `0.0055` → IC=-0.260 (n=48)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0055
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=98)

- **FILTRO** `pct_vs_K` |x|> `3.2846` → IC=-0.439 (n=47)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.2846
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=99)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `T_h` < `145.7969` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` < 145.7969
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0083` → IC=-0.284 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=102)

- **FILTRO** `T_h` > `113.7599` → IC=-0.227 (n=75)

  - _Acción_: SKIP cuando `T_h` > 113.7599
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=76)

- **FILTRO** `sigma_h` < `0.0105` → IC=-0.304 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=52)

- **FILTRO** `pct_vs_K` |x|> `3.7217` → IC=-0.417 (n=34)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.7217
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=67)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1224` → IC=+0.476 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1224 (IC base=+0.339)

- **PATRÓN** `sigma_h` < `0.0135` → IC=+0.359 (n=90)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0135 (IC base=+0.339)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.379 (n=89)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.339)

- **PATRÓN** `T_h` > `0.7758` → IC=+0.385 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7758 (IC base=+0.339)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.477 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.339)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.355 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.339)

- **PATRÓN** `edge` > `0.096` → IC=+0.448 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.096 (IC base=+0.417)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.430 (n=69)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.417)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.436 (n=138)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.417)

- **PATRÓN** `T_h` > `1.4813` → IC=+0.444 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4813 (IC base=+0.417)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.482 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.417)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.478 (n=135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.417)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1023` → IC=+0.457 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.417)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.419 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.417)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.420 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.417)

- **PATRÓN** `T_h` < `1.0313` → IC=+0.457 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.0313 (IC base=+0.417)

- **PATRÓN** `T_h` > `0.4508` → IC=+0.406 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4508 (IC base=+0.417)

- **PATRÓN** `dist_50` > `0.4077` → IC=+0.479 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4077 (IC base=+0.417)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.423 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.417)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.417)

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

- **PATRÓN** `edge` > `0.1961` → IC=+0.478 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1961 (IC base=+0.464)

- **PATRÓN** `sigma_h` < `0.0156` → IC=+0.478 (n=134)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0156 (IC base=+0.464)

- **PATRÓN** `T_h` > `1.1968` → IC=+0.478 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.1968 (IC base=+0.464)

- **PATRÓN** `dist_50` > `0.4373` → IC=+0.485 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4373 (IC base=+0.464)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.472 (n=141)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.464)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=290)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=365)

- **FILTRO** `streak_estiramiento` > `0.8581` → IC=-0.171 (n=80)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.8581
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=244)

- **PATRÓN** `streak_estiramiento` < `0.5654` → IC=+0.185 (n=163)

  - _Acción_: Kelly boost +0.92€ cuando `streak_estiramiento` < 0.5654 (IC base=+0.038)

- **PATRÓN** `libro_liquidez` > `2526.423` → IC=+0.127 (n=132)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 2526.423 (IC base=+0.038)

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
- **PATRÓN** `volumen_racha` < `945898.4` → IC=+0.132 (n=55)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_racha` < 945898.4 (IC base=+0.013)

- **PATRÓN** `streak_estiramiento` < `0.2711` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `streak_estiramiento` < 0.2711 (IC base=+0.013)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.139 (n=106)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 7.0 (IC base=+0.081)

- **PATRÓN** `streak_estiramiento` < `0.4503` → IC=+0.181 (n=89)

  - _Acción_: Kelly boost +0.91€ cuando `streak_estiramiento` < 0.4503 (IC base=+0.081)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.163 (n=78)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 30.0 (IC base=+0.081)

- **PATRÓN** `libro_liquidez` > `2312.8768` → IC=+0.153 (n=119)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2312.8768 (IC base=+0.081)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=92)

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
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=719)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` < `11.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `volumen_racha` > `3677.1957` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `volumen_racha` > 3677.1957
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

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
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=932)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1327)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1072)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=1088)

### STRUCT_NO_15M
- **FILTRO** `hora_utc` < `19.0` → IC=-0.227 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3790)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `hora_utc` < `19.0` → IC=-0.227 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=2065)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.198 (n=1088)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0045 (IC base=+0.184)

- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.206 (n=1088)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.184)

- **PATRÓN** `drift_60min` |x|≤ `0.1707` → IC=+0.196 (n=2872)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1707 (IC base=+0.184)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.352` → IC=+0.194 (n=2928)

  - _Acción_: Kelly boost +0.97€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.352 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.190 (n=3026)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 6.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.188 (n=2999)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 15.0 (IC base=+0.184)

- **PATRÓN** `ibs_15` > `0.5745` → IC=+0.264 (n=3263)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5745 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` > `0.1236` → IC=+0.180 (n=1544)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.1236 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` < `0.4812` → IC=+0.171 (n=2862)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.4812 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.684` → IC=+0.260 (n=852)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.684 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `5050.3314` → IC=+0.205 (n=1088)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5050.3314 (IC base=+0.184)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=1291)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.231 (n=566)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.0585` → IC=+0.259 (n=189)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0585 (IC base=+0.220)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2509` → IC=+0.249 (n=189)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2509 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.241 (n=530)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.220)

- **PATRÓN** `ibs_15` > `0.7243` → IC=+0.282 (n=566)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7243 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `0.1369` → IC=+0.247 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1369 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.126` → IC=+0.303 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.126 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.221 (n=733)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `16220.2116` → IC=+0.249 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16220.2116 (IC base=+0.220)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.36` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.36
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=724)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.190 (n=214)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0034 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.0668` → IC=+0.149 (n=283)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.0668 (IC base=+0.144)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1466` → IC=+0.153 (n=428)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio_macro` |x|> 0.1466 (IC base=+0.144)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1304` → IC=+0.159 (n=250)

  - _Acción_: Kelly boost +0.79€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1304 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.148 (n=592)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 6.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.148 (n=671)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 17.0 (IC base=+0.144)

- **PATRÓN** `ibs_15` > `0.563` → IC=+0.245 (n=642)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.563 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1149` → IC=+0.158 (n=404)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1149 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.6102` → IC=+0.146 (n=729)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.6102 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.028` → IC=+0.289 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.028 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `3555.0527` → IC=+0.152 (n=573)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3555.0527 (IC base=+0.144)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `18.363` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.363
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=282)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.143 (n=222)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0059 (IC base=+0.102)

- **PATRÓN** `drift_60min` |x|≤ `0.1607` → IC=+0.148 (n=444)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.1607 (IC base=+0.102)

- **PATRÓN** `ibs_15` > `0.9048` → IC=+0.268 (n=222)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9048 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=368)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.102)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.407` → IC=+0.153 (n=70)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 8.407 (IC base=+0.023)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0236` → IC=+0.260 (n=252)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0236 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.1697` → IC=+0.219 (n=666)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1697 (IC base=+0.210)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3395` → IC=+0.241 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3395 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.225 (n=670)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.210)

- **PATRÓN** `ibs_15` > `0.561` → IC=+0.295 (n=756)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.561 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` > `0.1857` → IC=+0.219 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1857 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.0` → IC=+0.241 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.0 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2986.0344` → IC=+0.295 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2986.0344 (IC base=+0.210)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.164 (n=750)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.82€ cuando `ibs_15` < 0.1111 (IC base=+0.066)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.370 (n=397)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.361)

- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.369 (n=594)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0028 (IC base=+0.361)

- **PATRÓN** `drift_15min` |x|≤ `0.4024` → IC=+0.361 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4024 (IC base=+0.361)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1511` → IC=+0.382 (n=396)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1511 (IC base=+0.361)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2297` → IC=+0.380 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2297 (IC base=+0.361)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.375 (n=598)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.361)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.398 (n=595)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.361)

- **PATRÓN** `dist_vwap_pct` > `0.4169` → IC=+0.391 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4169 (IC base=+0.361)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.772` → IC=+0.384 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.772 (IC base=+0.361)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.366 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.361)

- **PATRÓN** `libro_liquidez` > `3505.1277` → IC=+0.371 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3505.1277 (IC base=+0.361)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.363 (n=276)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.364)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.388 (n=105)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.364)

- **PATRÓN** `drift_15min` |x|≤ `0.5096` → IC=+0.363 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5096 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2136` → IC=+0.389 (n=142)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2136 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1413` → IC=+0.396 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1413 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.383 (n=313)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.8077` → IC=+0.389 (n=313)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8077 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.2458` → IC=+0.394 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2458 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.997` → IC=+0.384 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.997 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `15285.027` → IC=+0.389 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15285.027 (IC base=+0.364)

- **PATRÓN** `ballena_activa_n` < `489.0` → IC=+0.411 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 489.0 (IC base=+0.364)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.358 (n=188)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.357)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.377 (n=128)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0057 (IC base=+0.357)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0902` → IC=+0.370 (n=252)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0902 (IC base=+0.357)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2986` → IC=+0.376 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2986 (IC base=+0.357)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.386 (n=138)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.357)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.360 (n=127)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.357)

- **PATRÓN** `ibs_15` > `0.7479` → IC=+0.408 (n=282)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7479 (IC base=+0.357)

- **PATRÓN** `dist_vwap_pct` > `0.4536` → IC=+0.377 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4536 (IC base=+0.357)

- **PATRÓN** `dist_vwap_pct` < `0.2918` → IC=+0.358 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2918 (IC base=+0.357)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.352` → IC=+0.385 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.352 (IC base=+0.357)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.361 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.357)

- **PATRÓN** `libro_liquidez` > `3911.5181` → IC=+0.385 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3911.5181 (IC base=+0.357)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0123` → IC=-0.221 (n=1023)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0123
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=3073)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.208 (n=1593)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=2503)

- **FILTRO** `libro_liquidez` < `4158.6606` → IC=-0.149 (n=2703)

  - _Acción_: SKIP cuando `libro_liquidez` < 4158.6606
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=1393)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1408` → IC=+0.187 (n=659)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.93€ cuando `delta_ratio_macro` |x|> 0.1408 (IC base=-0.066)

- **PATRÓN** `ibs_15` > `0.6347` → IC=+0.284 (n=989)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6347 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` > `0.1102` → IC=+0.210 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1102 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` < `0.4242` → IC=+0.202 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4242 (IC base=-0.066)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2291` → IC=+0.270 (n=1118)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2291 (IC base=-0.012)

- **PATRÓN** `ibs_15` < `0.3535` → IC=+0.282 (n=3352)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3535 (IC base=-0.012)

- **PATRÓN** `dist_vwap_pct` > `0.6573` → IC=+0.279 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6573 (IC base=-0.012)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.211 (n=579)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=1741)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.232 (n=579)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=1741)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.199 (n=1445)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=875)

- **FILTRO** `sigma_ewma_delta_pct` > `23.552` → IC=-0.263 (n=336)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.552
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=1984)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.212 (n=64)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=2256)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.125 (n=700)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0052 (IC base=+0.099)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2047` → IC=+0.299 (n=142)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2047 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.138 (n=343)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 15.0 (IC base=+0.099)

- **PATRÓN** `ibs_15` > `0.7572` → IC=+0.334 (n=312)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7572 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.1047` → IC=+0.304 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1047 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` < `0.3672` → IC=+0.296 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3672 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.517` → IC=+0.144 (n=161)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 24.517 (IC base=+0.099)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0659` → IC=+0.222 (n=52)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0659 (IC base=-0.195)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1833` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1833 (IC base=-0.195)

- **PATRÓN** `ibs_15` < `0.6128` → IC=+0.296 (n=52)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6128 (IC base=-0.195)

- **PATRÓN** `dist_vwap_pct` < `0.0474` → IC=+0.287 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0474 (IC base=-0.195)

- **PATRÓN** `ballena_activa_n` < `295.0` → IC=+0.392 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 295.0 (IC base=-0.195)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=643)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.164 (n=436)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.163 (n=443)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0038 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.0704` → IC=+0.196 (n=218)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.0704 (IC base=+0.153)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1408` → IC=+0.154 (n=330)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio_macro` |x|> 0.1408 (IC base=+0.153)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.191 (n=376)

  - _Acción_: Kelly boost +0.95€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.175 (n=352)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 11.0 (IC base=+0.153)

- **PATRÓN** `ibs_15` > `0.6258` → IC=+0.259 (n=495)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6258 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.455` → IC=+0.159 (n=133)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.455 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.1583` → IC=+0.154 (n=385)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1583 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.63` → IC=+0.263 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.63 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=643)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `10510.4052` → IC=+0.171 (n=165)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 10510.4052 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.258 (n=519)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.3569` → IC=+0.244 (n=1037)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3569 (IC base=+0.243)

- **PATRÓN** `drift_15min` |x|≤ `0.7654` → IC=+0.256 (n=1037)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7654 (IC base=+0.243)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1573` → IC=+0.256 (n=786)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1573 (IC base=+0.243)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3306` → IC=+0.244 (n=1141)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3306 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.251 (n=439)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.244 (n=459)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.243)

- **PATRÓN** `ibs_15` < `0.3685` → IC=+0.273 (n=1179)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3685 (IC base=+0.243)

- **PATRÓN** `dist_vwap_pct` > `0.7901` → IC=+0.282 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7901 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.34` → IC=+0.261 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.34 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.569` → IC=+0.247 (n=1233)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.569 (IC base=+0.243)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0102` → IC=-0.243 (n=235)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0102
  - _Potencial_: sin este filtro IC_bueno=-0.165 (n=708)

- **FILTRO** `drift_60min` |x|> `0.1724` → IC=-0.252 (n=320)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1724
  - _Potencial_: sin este filtro IC_bueno=-0.150 (n=623)

- **FILTRO** `drift_15min` |x|> `0.8849` → IC=-0.276 (n=235)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8849
  - _Potencial_: sin este filtro IC_bueno=-0.153 (n=708)

- **FILTRO** `sigma_ewma_delta_pct` > `6.57` → IC=-0.198 (n=223)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.57
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=720)

- **FILTRO** `sigma_ewma_delta_pct` > `18.158` → IC=-0.145 (n=488)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.158
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=3926)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.185)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.185)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.185)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.185)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0649` → IC=+0.243 (n=528)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0649 (IC base=-0.038)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.287 (n=529)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` < `0.4491` → IC=+0.251 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4491 (IC base=-0.038)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0196` → IC=-0.248 (n=569)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0196
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=571)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=1121)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.204)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.204)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1598` → IC=+0.271 (n=369)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1598 (IC base=-0.025)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1132` → IC=+0.300 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1132 (IC base=-0.025)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.298 (n=818)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.025)

- **PATRÓN** `dist_vwap_pct` > `0.7727` → IC=+0.349 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7727 (IC base=-0.025)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.298 (n=881)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.0534` → IC=+0.319 (n=334)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0534 (IC base=+0.290)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2411` → IC=+0.301 (n=335)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2411 (IC base=+0.290)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2247` → IC=+0.303 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2247 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.305 (n=1051)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.290)

- **PATRÓN** `ibs_15` > `0.838` → IC=+0.321 (n=1002)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.838 (IC base=+0.290)

- **PATRÓN** `dist_vwap_pct` > `0.1554` → IC=+0.315 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1554 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.754` → IC=+0.372 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.754 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `12681.8839` → IC=+0.314 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12681.8839 (IC base=+0.290)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.308 (n=238)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.0582` → IC=+0.309 (n=181)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0582 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2575` → IC=+0.308 (n=180)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2575 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.305 (n=543)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.827` → IC=+0.312 (n=541)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.827 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.2546` → IC=+0.324 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2546 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.865` → IC=+0.379 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.865 (IC base=+0.287)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.286 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `16294.6642` → IC=+0.331 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16294.6642 (IC base=+0.287)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.307 (n=460)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.293)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.294 (n=460)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.0523` → IC=+0.321 (n=154)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0523 (IC base=+0.293)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1515` → IC=+0.303 (n=307)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1515 (IC base=+0.293)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1029` → IC=+0.330 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1029 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.311 (n=415)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.296 (n=415)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.293)

- **PATRÓN** `ibs_15` > `0.8516` → IC=+0.325 (n=460)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8516 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.2815` → IC=+0.320 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2815 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.656` → IC=+0.357 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.656 (IC base=+0.293)

### UPDOWN_OU_5M
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1078` → IC=-0.145 (n=212)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1078
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=72)

- **FILTRO** `ballena_activa_n` > `23.0` → IC=-0.201 (n=105)

  - _Acción_: SKIP cuando `ballena_activa_n` > 23.0
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=108)

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
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=144)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1254` → IC=-0.200 (n=18)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1254
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=37)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.306` → IC=-0.380 (n=23)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.306
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0775` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0775
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `sigma_h` < `0.0063` → IC=-0.222 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.150 (n=18)

- **FILTRO** `ballena_activa_n` > `18.0` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `ballena_activa_n` > 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `83.3501` → IC=+0.201 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.193)

- **PATRÓN** `ratio` < `0.973` → IC=+0.420 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.193)

- **PATRÓN** `T_h` > `111.9965` → IC=+0.352 (n=2030)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9965 (IC base=+0.337)

- **PATRÓN** `ratio` > `1.0236` → IC=+0.370 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0236 (IC base=+0.337)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `103.5964` → IC=+0.186 (n=183)

  - _Acción_: Kelly boost +0.93€ cuando `T_h` > 103.5964 (IC base=+0.166)

- **PATRÓN** `ratio` < `0.9943` → IC=+0.287 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9943 (IC base=+0.166)

- **PATRÓN** `T_h` > `110.3225` → IC=+0.304 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 110.3225 (IC base=+0.293)

- **PATRÓN** `ratio` > `1.0466` → IC=+0.394 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0466 (IC base=+0.293)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `83.3501` → IC=+0.240 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.231)

- **PATRÓN** `ratio` < `0.9849` → IC=+0.430 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9849 (IC base=+0.231)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.351 (n=736)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.325)

- **PATRÓN** `ratio` > `1.0093` → IC=+0.345 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0093 (IC base=+0.325)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1038` → IC=+0.448 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1038 (IC base=+0.400)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5745 sube el IC de +0.184 a +0.264 en UPDOWN_GBM#15min (n=3263). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7243 sube el IC de +0.220 a +0.282 en UPDOWN_GBM#BTC#15min (n=566). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.563 sube el IC de +0.144 a +0.245 en UPDOWN_GBM#ETH#15min (n=642). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.9048 sube el IC de +0.102 a +0.268 en UPDOWN_GBM#SOL#15min (n=222). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.561 sube el IC de +0.210 a +0.295 en UPDOWN_GBM#XRP#15min (n=756). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.066 a +0.164 en UPDOWN_GBM#XRP#15min (n=750). Ya aplicado como kelly_boost=+0.82€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6347 sube el IC de -0.066 a +0.284 en UPDOWN_GBM_15M_TARDIO (n=989). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3535 sube el IC de -0.012 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=3352). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7572 sube el IC de +0.099 a +0.334 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=312). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6128 sube el IC de -0.195 a +0.296 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=52). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6258 sube el IC de +0.153 a +0.259 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=495). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3685 sube el IC de +0.243 a +0.273 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1179). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.185 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.038 a +0.287 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=529). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.204 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.025 a +0.298 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=818). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.838 sube el IC de +0.290 a +0.321 en UPDOWN_GBM_IBS_ALTO (n=1002). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.827 sube el IC de +0.287 a +0.312 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=541). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8516 sube el IC de +0.293 a +0.325 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=460). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.361 a +0.398 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=595). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8077 sube el IC de +0.364 a +0.389 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=313). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7479 sube el IC de +0.357 a +0.408 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=282). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1785 | +0.090 | +205.63€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1785 | +0.090 | +205.63€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1408 | +0.095 | +179.37€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1408 | +0.095 | +179.37€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 274 | +0.065 | +10.54€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 274 | +0.065 | +10.54€ | 6 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 72 | +0.108 | +16.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 72 | +0.108 | +16.05€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 464 | -0.015 | +54.68€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 464 | -0.015 | +54.68€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 336 | -0.027 | +32.52€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 336 | -0.027 | +32.52€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 102 | +0.029 | +17.57€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 102 | +0.029 | +17.57€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 23 | -0.060 | +1.23€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 23 | -0.060 | +1.23€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 37977 | -0.082 | -4758.07€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2049 | +0.021 | -239.72€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 35928 | -0.088 | -4518.35€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4435 | -0.116 | -762.62€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4435 | -0.116 | -762.62€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2049 | +0.021 | -239.72€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2049 | +0.021 | -239.72€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4161 | -0.111 | -849.70€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4161 | -0.111 | -849.70€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 10099 | -0.011 | -883.08€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 10099 | -0.011 | -883.08€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 9863 | -0.105 | -749.03€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 9863 | -0.105 | -749.03€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 7370 | -0.139 | -1273.91€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 7370 | -0.139 | -1273.91€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 31776 | -0.017 | +3578.11€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 8223 | +0.004 | +1732.37€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 23553 | -0.025 | +1845.74€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 31776 | -0.017 | +3578.11€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 8223 | +0.004 | +1732.37€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 23553 | -0.025 | +1845.74€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 134906 | +0.114 | -5714.11€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 17818 | +0.182 | -536.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 588 | -0.027 | -67.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 108332 | +0.104 | -4847.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 8168 | +0.103 | -262.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 17974 | +0.106 | -1128.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 59 | -0.156 | +9.83€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 17900 | +0.108 | -1126.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 26318 | +0.128 | -413.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5091 | +0.191 | -154.53€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 17957 | +0.118 | -160.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3228 | +0.086 | -75.51€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 18025 | +0.096 | -1340.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 70 | -0.111 | -5.12€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 17940 | +0.098 | -1323.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 28685 | +0.123 | -552.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 7504 | +0.176 | -136.96€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 18185 | +0.106 | -350.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2984 | +0.101 | -55.98€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 25910 | +0.114 | -1357.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5030 | +0.194 | -255.86€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 491 | +0.007 | -13.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 18433 | +0.093 | -956.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1956 | +0.136 | -131.13€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 17994 | +0.103 | -922.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 64 | -0.076 | +5.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 17917 | +0.104 | -927.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 21658 | +0.195 | -1350.87€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 21658 | +0.195 | -1350.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4960 | +0.176 | -444.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4960 | +0.176 | -444.32€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 2619 | +0.202 | -57.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 2619 | +0.202 | -57.59€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 4900 | +0.179 | -402.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 4900 | +0.179 | -402.90€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4269 | +0.246 | -142.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4269 | +0.246 | -142.99€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4831 | +0.188 | -316.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4831 | +0.188 | -316.83€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 963 | +0.427 | -32.00€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 963 | +0.427 | -32.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 378 | +0.437 | -4.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 378 | +0.437 | -4.78€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 378 | +0.429 | -10.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 378 | +0.429 | -10.68€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 194 | +0.403 | -14.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 194 | +0.403 | -14.22€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 75486 | +0.201 | -5475.41€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 75486 | +0.201 | -5475.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 12975 | +0.185 | -1345.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 12975 | +0.185 | -1345.21€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 12180 | +0.224 | -422.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 12180 | +0.224 | -422.88€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 12937 | +0.179 | -1392.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 12937 | +0.179 | -1392.59€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 12256 | +0.220 | -470.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 12256 | +0.220 | -470.14€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 12506 | +0.202 | -821.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 12506 | +0.202 | -821.27€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 12632 | +0.196 | -1023.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 12632 | +0.196 | -1023.32€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 28876 | +0.117 | +210.12€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 28876 | +0.117 | +210.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 14354 | +0.120 | +184.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 14354 | +0.120 | +184.48€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 14522 | +0.114 | +25.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 14522 | +0.114 | +25.64€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1951 | +0.289 | -21.62€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1951 | +0.289 | -21.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 890 | +0.279 | -21.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 890 | +0.279 | -21.90€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 942 | +0.289 | -5.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 942 | +0.289 | -5.03€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 119 | +0.351 | +5.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 119 | +0.351 | +5.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 898 | +0.440 | +1.59€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 898 | +0.440 | +1.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 436 | +0.436 | -3.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 436 | +0.436 | -3.60€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 416 | +0.445 | +4.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 416 | +0.445 | +4.63€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1522 | +0.069 | -68.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 582 | +0.055 | -45.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 940 | +0.077 | -22.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 72 | +0.108 | +2.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 72 | +0.108 | +2.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1172 | +0.075 | -34.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 232 | +0.064 | -11.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 940 | +0.077 | -22.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 278 | +0.032 | -37.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 278 | +0.032 | -37.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 56494 | +0.100 | -1419.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 4568 | +0.092 | +62.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 51926 | +0.101 | -1482.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 31164 | +0.105 | -340.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 4568 | +0.092 | +62.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 26596 | +0.107 | -403.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 11486 | +0.109 | -37.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 11486 | +0.109 | -37.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 13844 | +0.081 | -1041.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 13844 | +0.081 | -1041.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 892 | +0.192 | -113.16€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 892 | +0.192 | -113.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 892 | +0.192 | -113.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 892 | +0.192 | -113.16€ | 2 | 4 |
| ✅ GBM_LATE_15M | 39064 | +0.092 | +19951.25€ | 0 | 17 |
| ✅ GBM_LATE_15M#15min | 39064 | +0.092 | +19951.25€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 6540 | +0.210 | +5219.07€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 6540 | +0.210 | +5219.07€ | 0 | 24 |
| ✅ GBM_LATE_15M#BTC | 5856 | +0.178 | +4351.99€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 5856 | +0.178 | +4351.99€ | 0 | 24 |
| ✅ GBM_LATE_15M#DOGE | 6965 | +0.203 | +5361.63€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 6965 | +0.203 | +5361.63€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 5480 | +0.040 | +1482.17€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 5480 | +0.040 | +1482.17€ | 1 | 17 |
| ✅ GBM_LATE_15M#SOL | 5532 | -0.031 | +1186.94€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 5532 | -0.031 | +1186.94€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 8691 | -0.034 | +2349.44€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 8691 | -0.034 | +2349.44€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 42200 | +0.086 | +22794.97€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 42200 | +0.086 | +22794.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 8163 | +0.005 | +4190.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 8163 | +0.005 | +4190.59€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 8874 | +0.013 | +2021.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 8874 | +0.013 | +2021.03€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 5892 | +0.274 | +6230.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 5892 | +0.274 | +6230.79€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 7440 | +0.013 | +1790.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 7440 | +0.013 | +1790.57€ | 1 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 6791 | +0.039 | +2766.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 6791 | +0.039 | +2766.47€ | 3 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5040 | +0.297 | +5795.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5040 | +0.297 | +5795.52€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 31032 | +0.178 | +24790.73€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 31032 | +0.178 | +24790.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 4708 | +0.223 | +4061.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 4708 | +0.223 | +4061.08€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 4887 | +0.150 | +3589.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 4887 | +0.150 | +3589.32€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 4955 | +0.222 | +4227.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 4955 | +0.222 | +4227.39€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 5240 | +0.139 | +3967.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 5240 | +0.139 | +3967.56€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 5835 | +0.123 | +4272.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 5835 | +0.123 | +4272.31€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 5407 | +0.223 | +4673.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 5407 | +0.223 | +4673.06€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 8342 | +0.136 | +4060.08€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 8342 | +0.136 | +4060.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2504 | +0.144 | +1405.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2504 | +0.144 | +1405.28€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 418 | +0.148 | +207.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 418 | +0.148 | +207.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2493 | +0.142 | +1183.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2493 | +0.142 | +1183.18€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1982 | +0.111 | +773.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1982 | +0.111 | +773.05€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 540 | +0.133 | +238.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 540 | +0.133 | +238.31€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO | 39264 | +0.183 | +30938.56€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 39264 | +0.183 | +30938.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 6234 | +0.236 | +5670.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 6234 | +0.236 | +5670.16€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 6106 | +0.148 | +4101.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 6106 | +0.148 | +4101.47€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 6615 | +0.231 | +5857.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 6615 | +0.231 | +5857.04€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 6451 | +0.138 | +4568.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 6451 | +0.138 | +4568.48€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 6947 | +0.122 | +4735.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 6947 | +0.122 | +4735.02€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 6911 | +0.226 | +6006.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 6911 | +0.226 | +6006.40€ | 0 | 21 |
| ✅ GBM_LATE_5M | 10851 | +0.194 | +8057.35€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 10851 | +0.194 | +8057.35€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 919 | +0.232 | +813.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 919 | +0.232 | +813.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2448 | +0.189 | +1926.55€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2448 | +0.189 | +1926.55€ | 0 | 28 |
| ✅ GBM_LATE_5M#DOGE | 1011 | +0.177 | +667.91€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1011 | +0.177 | +667.91€ | 0 | 17 |
| ✅ GBM_LATE_5M#ETH | 3221 | +0.191 | +2244.49€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3221 | +0.191 | +2244.49€ | 0 | 25 |
| ✅ GBM_LATE_5M#SOL | 1602 | +0.191 | +1209.34€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1602 | +0.191 | +1209.34€ | 0 | 28 |
| ✅ GBM_LATE_5M#XRP | 1650 | +0.196 | +1195.07€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1650 | +0.196 | +1195.07€ | 0 | 0 |
| ✅ GBM_LATE_60M | 3097 | +0.070 | +1071.06€ | 0 | 9 |
| ✅ GBM_LATE_60M#60min | 3097 | +0.070 | +1071.06€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1152 | +0.087 | +439.13€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1152 | +0.087 | +439.13€ | 0 | 8 |
| ✅ GBM_LATE_60M#ETH | 991 | +0.074 | +384.72€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 991 | +0.074 | +384.72€ | 0 | 10 |
| ✅ GBM_LATE_60M#SOL | 954 | +0.045 | +247.21€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 954 | +0.045 | +247.21€ | 1 | 12 |
| 🚫 GBM_LATE_60M_FADE | 533 | -0.246 | -22.94€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 533 | -0.246 | -22.94€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 201 | -0.239 | -10.94€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 201 | -0.239 | -10.94€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 190 | -0.229 | -4.06€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 190 | -0.229 | -4.06€ | 5 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 142 | -0.271 | -7.94€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 142 | -0.271 | -7.94€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1401 | +0.088 | +388.84€ | 0 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1401 | +0.088 | +388.84€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 549 | +0.088 | +146.01€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 549 | +0.088 | +146.01€ | 1 | 13 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 515 | +0.063 | +88.49€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 515 | +0.063 | +88.49€ | 2 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 337 | +0.125 | +154.35€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 337 | +0.125 | +154.35€ | 2 | 14 |
| ✅ LATE_WINDOW_5MIN | 149 | +0.262 | +134.77€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 149 | +0.262 | +134.77€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 149 | +0.262 | +134.77€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 149 | +0.262 | +134.77€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3217 | +0.101 | +799.63€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3217 | +0.101 | +799.63€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3217 | +0.101 | +799.63€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3217 | +0.101 | +799.63€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 466 | -0.062 | -28.70€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 466 | -0.062 | -28.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 135 | -0.018 | +0.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 135 | -0.018 | +0.92€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 81 | -0.078 | -7.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 81 | -0.078 | -7.55€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 169 | -0.026 | -5.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 169 | -0.026 | -5.21€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 3505 | +0.016 | +77.86€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3505 | +0.016 | +77.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 171 | +0.015 | -3.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 171 | +0.015 | -3.81€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 689 | +0.017 | +35.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 689 | +0.017 | +35.86€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1262 | +0.025 | +29.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1262 | +0.025 | +29.22€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 749 | +0.011 | +1.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 749 | +0.011 | +1.36€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 431 | +0.010 | +20.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 431 | +0.010 | +20.32€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1649 | -0.043 | -30.61€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1649 | -0.043 | -30.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 467 | -0.037 | -13.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 467 | -0.037 | -13.86€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 557 | -0.017 | +4.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 557 | -0.017 | +4.84€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 625 | -0.069 | -21.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 625 | -0.069 | -21.59€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 7328 | -0.026 | +5.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 3478 | -0.038 | -96.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 3850 | -0.015 | +102.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 209 | -0.012 | +7.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 105 | +0.014 | +8.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 104 | -0.038 | -1.64€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 1843 | -0.019 | +13.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 878 | -0.025 | -7.34€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 965 | -0.014 | +20.93€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 802 | -0.019 | +18.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 402 | -0.040 | -8.39€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 400 | +0.003 | +26.44€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 1557 | -0.044 | -67.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 725 | -0.063 | -68.98€ | 4 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 832 | -0.028 | +1.08€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1439 | -0.017 | +30.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 688 | -0.033 | -7.95€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 751 | -0.002 | +38.83€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1478 | -0.030 | +4.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 680 | -0.040 | -12.54€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 798 | -0.021 | +16.61€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 45638 | -0.001 | +2272.61€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 45638 | -0.001 | +2272.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 8197 | +0.026 | +1043.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 8197 | +0.026 | +1043.10€ | 2 | 4 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 6645 | -0.034 | -98.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 6645 | -0.034 | -98.77€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 8316 | +0.023 | +842.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 8316 | +0.023 | +842.31€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 6481 | -0.047 | -133.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 6481 | -0.047 | -133.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 7700 | -0.004 | +238.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 7700 | -0.004 | +238.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 8299 | +0.015 | +380.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 8299 | +0.015 | +380.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6457 | -0.060 | -161.04€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6457 | -0.060 | -161.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1648 | -0.080 | -43.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1648 | -0.080 | -43.60€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 53 | -0.064 | -2.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 53 | -0.064 | -2.93€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 755 | -0.120 | -31.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 755 | -0.120 | -31.95€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1920 | -0.078 | -42.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1920 | -0.078 | -42.26€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 856 | -0.015 | -25.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 856 | -0.015 | -25.00€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3366 | +0.004 | -0.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3366 | +0.004 | -0.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 131 | -0.034 | -0.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 131 | -0.034 | -0.72€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 192 | +0.015 | +1.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 192 | +0.015 | +1.02€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1325 | +0.006 | +6.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1325 | +0.006 | +6.88€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1390 | +0.007 | +0.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1390 | +0.007 | +0.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 189 | -0.008 | -5.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 189 | -0.008 | -5.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 113699 | -0.075 | +1842.56€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 113699 | -0.075 | +1842.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 19690 | -0.075 | +1052.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 19690 | -0.075 | +1052.85€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 17163 | -0.099 | -930.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 17163 | -0.099 | -930.90€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 19973 | -0.066 | +1135.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 19973 | -0.066 | +1135.72€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 16700 | -0.095 | -513.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 16700 | -0.095 | -513.37€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 20456 | -0.055 | +346.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 20456 | -0.055 | +346.22€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 19717 | -0.065 | +752.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 19717 | -0.065 | +752.04€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8672 | -0.033 | -175.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8672 | -0.033 | -175.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1000 | -0.017 | -19.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1000 | -0.017 | -19.75€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1963 | -0.045 | -22.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1963 | -0.045 | -22.09€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2572 | -0.026 | -41.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2572 | -0.026 | -41.37€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1172 | -0.052 | -24.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1172 | -0.052 | -24.34€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 957 | -0.031 | -35.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 957 | -0.031 | -35.13€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1569 | +0.125 | +649.66€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 1433 | +0.131 | +637.07€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 335 | +0.150 | +185.05€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 335 | +0.150 | +185.05€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 296 | +0.121 | +105.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 296 | +0.121 | +105.68€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#ETH | 289 | +0.132 | +135.06€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 289 | +0.132 | +135.06€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 253 | +0.151 | +138.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 253 | +0.151 | +138.41€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 260 | +0.095 | +72.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 260 | +0.095 | +72.87€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1261 | -0.017 | -16.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1261 | -0.017 | -16.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 241 | -0.010 | +3.92€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 241 | -0.010 | +3.92€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 219 | -0.002 | +5.89€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 219 | -0.002 | +5.89€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 333 | -0.037 | -20.35€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 333 | -0.037 | -20.35€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 264 | -0.004 | -2.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 264 | -0.004 | -2.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 204 | -0.024 | -4.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 204 | -0.024 | -4.10€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 848 | -0.068 | -39.09€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 393 | -0.115 | -76.62€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 304 | -0.147 | -66.83€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 89 | -0.005 | -9.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 303 | -0.031 | +24.40€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 217 | -0.025 | +24.90€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 86 | -0.045 | -0.50€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 152 | -0.019 | +13.13€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 122 | -0.024 | +8.23€ | 0 | 1 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 30 | +0.000 | +4.90€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 643 | -0.083 | -33.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 205 | -0.022 | -5.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1040 | -0.207 | -58.02€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 417 | -0.206 | -38.18€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 361 | -0.211 | -38.46€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 56 | -0.172 | +0.28€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 352 | -0.217 | -31.41€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 306 | -0.227 | -37.10€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 46 | -0.146 | +5.69€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 271 | -0.192 | +11.57€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 252 | -0.189 | +8.43€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 19 | -0.204 | +3.14€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 919 | -0.211 | -67.13€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 121 | -0.175 | +9.11€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 427 | +0.395 | +403.64€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#BTC | 56 | +0.138 | +48.27€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 56 | +0.138 | +48.27€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 106 | +0.361 | +89.36€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 106 | +0.361 | +89.36€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 265 | +0.459 | +266.01€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 265 | +0.459 | +266.01€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 427 | +0.395 | +403.64€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 693 | +0.028 | +28.72€ | 3 | 2 |
| ✅ STREAK_FADE_15M#15min | 693 | +0.028 | +28.72€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 299 | +0.022 | +2.86€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 299 | +0.022 | +2.86€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 56 | -0.017 | -4.00€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 56 | -0.017 | -4.00€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 71 | -0.007 | -0.09€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 71 | -0.007 | -0.09€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 267 | +0.054 | +29.94€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 267 | +0.054 | +29.94€ | 0 | 6 |
| ✅ STREAK_FADE_5M | 3400 | -0.021 | -132.51€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3400 | -0.021 | -132.51€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1051 | -0.022 | -37.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1051 | -0.022 | -37.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 588 | -0.027 | -26.12€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 588 | -0.027 | -26.12€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 162 | -0.043 | -14.36€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 162 | -0.043 | -14.36€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1599 | -0.017 | -54.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1599 | -0.017 | -54.52€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 95 | -0.046 | -8.93€ | 4 | 0 |
| ✅ STREAK_FADE_60M#60min | 95 | -0.046 | -8.93€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 40 | -0.071 | -3.54€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 40 | -0.071 | -3.54€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 55 | -0.026 | -5.39€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 55 | -0.026 | -5.39€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 10422 | +0.018 | +98.68€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 10422 | +0.018 | +98.68€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2666 | +0.019 | +24.16€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2666 | +0.019 | +24.16€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2670 | +0.021 | +40.15€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2670 | +0.021 | +40.15€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2884 | +0.009 | -2.06€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2884 | +0.009 | -2.06€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2202 | +0.023 | +36.42€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2202 | +0.023 | +36.42€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 9514 | +0.013 | -48.97€ | 1 | 0 |
| ✅ STRUCT_NO_15M#15min | 9514 | +0.013 | -48.97€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3809 | +0.017 | -8.76€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3809 | +0.017 | -8.76€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3606 | +0.011 | -28.71€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3606 | +0.011 | -28.71€ | 1 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2099 | +0.010 | -11.50€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2099 | +0.010 | -11.50€ | 1 | 0 |
| ✅ UPDOWN_GBM | 70855 | +0.052 | +6166.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 17754 | +0.084 | +3965.04€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2320 | +0.006 | +21.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 46427 | +0.047 | +2098.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 4112 | +0.009 | +82.77€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6818 | +0.089 | +1072.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1543 | +0.158 | +694.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5198 | +0.070 | +378.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 14609 | +0.054 | +1236.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2236 | +0.091 | +548.62€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 605 | +0.012 | +11.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 9850 | +0.058 | +614.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1830 | +0.007 | +58.58€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 88 | -0.067 | +3.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8104 | +0.066 | +845.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1529 | +0.149 | +607.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6497 | +0.047 | +239.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 15853 | +0.043 | +997.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 4126 | +0.064 | +592.25€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 595 | +0.007 | +12.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 9638 | +0.042 | +376.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1414 | +0.011 | +14.20€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 80 | -0.110 | +1.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 15611 | +0.030 | +693.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 4341 | +0.034 | +357.01€ | 0 | 4 |
| ✅ UPDOWN_GBM#SOL#240min | 577 | -0.004 | +0.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 9753 | +0.033 | +330.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 868 | +0.010 | +10.00€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 72 | -0.135 | -4.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 9858 | +0.061 | +1323.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3979 | +0.102 | +1165.11€ | 0 | 9 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 5491 | +0.035 | +158.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 240 | -0.103 | +0.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 792 | +0.361 | +281.13€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 792 | +0.361 | +281.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 417 | +0.364 | +145.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 417 | +0.364 | +145.47€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 375 | +0.357 | +135.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 375 | +0.357 | +135.66€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 18792 | -0.024 | +4530.42€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 18792 | -0.024 | +4530.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1674 | -0.056 | +500.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1674 | -0.056 | +500.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3252 | -0.111 | +145.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3252 | -0.111 | +145.08€ | 5 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 926 | +0.220 | +767.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 926 | +0.220 | +767.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2231 | +0.216 | +1452.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2231 | +0.216 | +1452.87€ | 1 | 23 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5357 | -0.064 | +696.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5357 | -0.064 | +696.18€ | 5 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5352 | -0.064 | +967.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5352 | -0.064 | +967.82€ | 2 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 211 | +0.035 | +5.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 211 | +0.035 | +5.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 211 | +0.035 | +5.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 211 | +0.035 | +5.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1334 | +0.290 | +1124.48€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1334 | +0.290 | +1124.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 721 | +0.287 | +572.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 721 | +0.287 | +572.40€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 613 | +0.293 | +552.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 613 | +0.293 | +552.08€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 799 | -0.112 | -82.76€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#5min | 799 | -0.112 | -82.76€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 240 | -0.083 | -17.98€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 240 | -0.083 | -17.98€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 86 | -0.159 | -8.64€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 86 | -0.159 | -8.64€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 90 | -0.185 | -6.78€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 90 | -0.185 | -6.78€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 3368 | +0.304 | +1627.25€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1226 | +0.257 | +166.14€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1293 | +0.298 | +580.12€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 849 | +0.379 | +880.99€ | 0 | 1 |