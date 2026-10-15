# Hipótesis automáticas — 2026-10-15 11:57 UTC
_Generado por shadow_postmortem.py sobre 908482 resoluciones (PNL=+116280.75€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **PATRÓN** `py_entrada` > `0.56` → IC=+0.271 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.56 (IC base=+0.136)

- **PATRÓN** `n_total_lado` > `68.0` → IC=+0.194 (n=256)

  - _Acción_: Kelly boost +0.97€ cuando `n_total_lado` > 68.0 (IC base=+0.136)

- **PATRÓN** `banda_hit_calibrado` > `0.6329` → IC=+0.271 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6329 (IC base=+0.136)

- **PATRÓN** `banda_z` > `9.53` → IC=+0.215 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.53 (IC base=+0.136)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.734` → IC=+0.134 (n=679)

  - _Acción_: Kelly boost +0.67€ cuando `ballenas_wallet_edge_medio` > 0.734 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=263)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.135 (n=519)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 11.0 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=823)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.136)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.545` → IC=+0.279 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.545 (IC base=+0.142)

- **PATRÓN** `n_total_lado` > `72.0` → IC=+0.212 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 72.0 (IC base=+0.142)

- **PATRÓN** `banda_hit_calibrado` > `0.6169` → IC=+0.265 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6169 (IC base=+0.142)

- **PATRÓN** `banda_z` > `9.994` → IC=+0.229 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.994 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.193 (n=213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=725)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.142)

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
- **FILTRO** `restante_s_al_confirmar` < `143.4` → IC=-0.204 (n=9506)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 143.4
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=28520)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `130.45` → IC=-0.265 (n=1108)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.45
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3327)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `122.71` → IC=-0.298 (n=1041)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.71
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=3124)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `167.27` → IC=-0.213 (n=2468)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 167.27
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=7407)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `132.25` → IC=-0.285 (n=1845)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.25
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=5537)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.210 (n=20158)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=4169)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `9308.1489` → IC=+0.178 (n=1870)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 9308.1489 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.132 (n=17055)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=20699)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.226 (n=15763)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=6936)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `7251.7214` → IC=+0.161 (n=2670)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 7251.7214 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=1982)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.196 (n=1941)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 17.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` > `0.775` → IC=+0.364 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.775 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.197 (n=2433)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `16269.5677` → IC=+0.205 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16269.5677 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.195 (n=1743)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 7.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.192 (n=1947)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 17.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.187)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.190 (n=2494)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `16111.0352` → IC=+0.196 (n=643)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 16111.0352 (IC base=+0.187)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.164 (n=448)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` > 0.61 (IC base=+0.084)

- **PATRÓN** `libro_liquidez` > `6891.1913` → IC=+0.172 (n=120)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 6891.1913 (IC base=+0.084)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.137 (n=1056)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.44 (IC base=+0.088)

- **PATRÓN** `libro_liquidez` > `5854.7033` → IC=+0.126 (n=241)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 5854.7033 (IC base=+0.088)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=3925)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.157)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.158 (n=2690)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 12.0 (IC base=+0.157)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.367 (n=1311)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.223 (n=1749)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.214)

- **PATRÓN** `py_entrada` < `0.255` → IC=+0.359 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.255 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.218 (n=2052)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.214)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.141 (n=980)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.144 (n=839)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.137)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.254 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=769)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2166.1457` → IC=+0.144 (n=425)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 2166.1457 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `4449.086` → IC=+0.160 (n=151)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 4449.086 (IC base=+0.074)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=919)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.410 (n=1130)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.150 (n=1272)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.158 (n=670)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 7.0 (IC base=+0.148)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.285 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=842)

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

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.257 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.129)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `11.0` → IC=-0.297 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=147)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=16934)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.201 (n=14436)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.233 (n=7039)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.178 (n=3933)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.177 (n=3729)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 17.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.180 (n=3822)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.73 (IC base=+0.176)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **FILTRO** `libro_liquidez` < `9614.35` → IC=-0.328 (n=56)

  - _Acción_: SKIP cuando `libro_liquidez` < 9614.35
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.232 (n=1268)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.314 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.223)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=3864)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.183 (n=3711)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.188 (n=1445)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.73 (IC base=+0.180)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.255 (n=3361)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.246)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.350 (n=1123)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=3789)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.193 (n=2435)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.194 (n=2796)

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

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.246 (n=22138)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.201)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=10278)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.188 (n=7019)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 12.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.201 (n=9769)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.185)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=4554)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.227 (n=4503)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.284 (n=3208)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.188 (n=3730)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.180 (n=6999)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 12.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.194 (n=9320)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.180)

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

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.276 (n=3133)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.204 (n=8897)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.263 (n=3275)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=3624)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.197 (n=3686)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=3800)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.190 (n=7909)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` < `4.22` → IC=+0.124 (n=7290)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` < 4.22 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.137 (n=7790)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.41` → IC=+0.137 (n=7244)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.41 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=3915)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` < `4.19` → IC=+0.126 (n=3631)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.19 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.141 (n=3938)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.95 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=4786)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `2.81` → IC=+0.144 (n=3597)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 2.81 (IC base=+0.120)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.187 (n=3994)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.132 (n=4257)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.135 (n=3655)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4776` → IC=+0.134 (n=12242)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.4776 (IC base=+0.116)

- **PATRÓN** `ibs_20min` > `0.9828` → IC=+0.246 (n=4081)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9828 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` > `0.7771` → IC=+0.261 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7771 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` < `0.3704` → IC=+0.251 (n=3357)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3704 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.967` → IC=+0.185 (n=4609)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 5.967 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `1.2062` → IC=+0.251 (n=3505)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2062 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` > `0.6206` → IC=+0.256 (n=3505)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6206 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.3025` → IC=+0.231 (n=1233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3025 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` > `2.344` → IC=+0.224 (n=3931)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.344 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.5668` → IC=+0.141 (n=15054)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5668 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.5855` → IC=+0.185 (n=1018)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.5855 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.1525` → IC=+0.185 (n=5381)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.1525 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `1.1873` → IC=+0.181 (n=5767)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 1.1873 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.0502` → IC=+0.183 (n=2616)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.0502 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2948` → IC=+0.230 (n=1441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2948 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.6706` → IC=+0.207 (n=3275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6706 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `110.0` → IC=+0.219 (n=9664)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 110.0 (IC base=+0.074)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.213 (n=901)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.191)

- **PATRÓN** `drift_60min` |x|≤ `0.348` → IC=+0.195 (n=2688)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.348 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.203 (n=1298)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.196 (n=1807)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 11.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `0.9749` → IC=+0.275 (n=1219)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9749 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.088` → IC=+0.279 (n=1164)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.088 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.242 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `2.2844` → IC=+0.207 (n=1158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2844 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.204 (n=2830)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `2091.32` → IC=+0.210 (n=896)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2091.32 (IC base=+0.191)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.203 (n=1593)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.235 (n=2229)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0082 (IC base=+0.233)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.236 (n=1012)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0073 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.0878` → IC=+0.265 (n=743)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0878 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.257 (n=811)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.5113` → IC=+0.255 (n=2228)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5113 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.795` → IC=+0.235 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.795 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` < `0.0939` → IC=+0.236 (n=1978)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0939 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.2849` → IC=+0.241 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2849 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.4419` → IC=+0.231 (n=698)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4419 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.6545` → IC=+0.243 (n=698)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6545 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=2465)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `1564.64` → IC=+0.243 (n=2228)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1564.64 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.232 (n=795)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.233)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.236 (n=962)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.222)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.224 (n=992)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.1063` → IC=+0.257 (n=962)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1063 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=2293)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.222 (n=2233)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.2996` → IC=+0.239 (n=2186)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2996 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.1292` → IC=+0.228 (n=1209)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1292 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.408` → IC=+0.259 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.408 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` < `1.2382` → IC=+0.224 (n=2186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2382 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `0.6213` → IC=+0.227 (n=2188)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6213 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.2757` → IC=+0.246 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2757 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `1.4025` → IC=+0.222 (n=718)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4025 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.4315` → IC=+0.249 (n=718)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4315 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `15942.3752` → IC=+0.222 (n=991)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15942.3752 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.152 (n=2219)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0057 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.0752` → IC=+0.171 (n=739)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.0752 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.162 (n=844)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.7299` → IC=+0.177 (n=2217)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.7299 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.1297` → IC=+0.155 (n=2046)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1297 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.121` → IC=+0.152 (n=360)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 11.121 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.229` → IC=+0.143 (n=2027)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.229 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `1.1861` → IC=+0.143 (n=2217)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1861 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.0948` → IC=+0.165 (n=808)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0948 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.4481` → IC=+0.143 (n=2099)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4481 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.7847` → IC=+0.142 (n=1399)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.7847 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `222.0` → IC=+0.171 (n=895)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 222.0 (IC base=+0.135)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.210 (n=925)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.196 (n=2908)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.194 (n=2489)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.272 (n=1063)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.342` → IC=+0.265 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.342 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.194 (n=2445)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.3519` → IC=+0.210 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3519 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `2.7012` → IC=+0.210 (n=1218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7012 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=3284)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `1993.66` → IC=+0.201 (n=1257)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1993.66 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.0087` → IC=+0.225 (n=1642)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0087 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.1765` → IC=+0.227 (n=1083)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1765 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.250 (n=926)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.0083` → IC=+0.276 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0083 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.528` → IC=+0.261 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.528 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3477` → IC=+0.256 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3477 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `1.7274` → IC=+0.218 (n=1025)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7274 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.7242` → IC=+0.229 (n=1056)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7242 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `2069.52` → IC=+0.234 (n=821)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2069.52 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.220 (n=2014)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.139 (n=142)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=3340)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.159 (n=503)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0036 (IC base=+0.049)

- **PATRÓN** `ibs_20min` > `0.9545` → IC=+0.220 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9545 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `0.1324` → IC=+0.320 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1324 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` < `0.1849` → IC=+0.320 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1849 (IC base=+0.049)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.077` → IC=+0.181 (n=1070)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 5.077 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` < `0.858` → IC=+0.331 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.858 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` > `1.2365` → IC=+0.342 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2365 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` < `0.1741` → IC=+0.320 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1741 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.2986` → IC=+0.335 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2986 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` < `1.4081` → IC=+0.338 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4081 (IC base=+0.049)

- **PATRÓN** `ballena_activa_n` < `149.0` → IC=+0.326 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 149.0 (IC base=+0.049)

- **PATRÓN** `ibs_20min` < `0.0951` → IC=+0.168 (n=871)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.0951 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` > `0.6765` → IC=+0.162 (n=211)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.6765 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` < `0.1293` → IC=+0.136 (n=1368)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1293 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` < `0.8506` → IC=+0.149 (n=1001)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8506 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.2866` → IC=+0.201 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2866 (IC base=+0.034)

- **PATRÓN** `volumen_spike_ratio` > `1.5118` → IC=+0.150 (n=1284)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.5118 (IC base=+0.034)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.174 (n=90)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=508)

- **FILTRO** `ibs_20min` < `0.2821` → IC=-0.195 (n=149)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2821
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=449)

- **FILTRO** `ibs_20min` > `0.2206` → IC=-0.131 (n=3310)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2206
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=1631)

- **FILTRO** `sigma_ewma_delta_pct` > `8.672` → IC=-0.234 (n=509)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.672
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=4432)

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

- **PATRÓN** `ibs_20min` < `0.2206` → IC=+0.150 (n=1631)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.2206 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` > `0.2682` → IC=+0.275 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2682 (IC base=-0.038)

- **PATRÓN** `volumen_regimen` < `0.7071` → IC=+0.288 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7071 (IC base=-0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.0789` → IC=+0.299 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0789 (IC base=-0.038)

- **PATRÓN** `volumen_spike_ratio` < `2.3831` → IC=+0.299 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3831 (IC base=-0.038)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6259` → IC=-0.182 (n=882)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6259
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=2647)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.162 (n=900)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=2629)

- **FILTRO** `ibs_20min` > `0.7576` → IC=-0.204 (n=1290)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7576
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=3889)

- **PATRÓN** `dist_vwap_pct` > `0.7462` → IC=+0.327 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7462 (IC base=-0.071)

- **PATRÓN** `dist_vwap_pct` < `0.2641` → IC=+0.297 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2641 (IC base=-0.071)

- **PATRÓN** `volumen_regimen` < `1.004` → IC=+0.292 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.004 (IC base=-0.071)

- **PATRÓN** `volumen_regimen` > `0.7043` → IC=+0.307 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7043 (IC base=-0.071)

- **PATRÓN** `volumen_pendiente_norm` < `0.1011` → IC=+0.296 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1011 (IC base=-0.071)

- **PATRÓN** `volumen_spike_ratio` < `1.42` → IC=+0.321 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.42 (IC base=-0.071)

- **PATRÓN** `volumen_spike_ratio` > `1.8487` → IC=+0.296 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8487 (IC base=-0.071)

- **PATRÓN** `dist_vwap_pct` > `0.8069` → IC=+0.279 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8069 (IC base=-0.008)

- **PATRÓN** `volumen_regimen` > `1.0722` → IC=+0.281 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0722 (IC base=-0.008)

- **PATRÓN** `volumen_pendiente_norm` > `0.1021` → IC=+0.282 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1021 (IC base=-0.008)

- **PATRÓN** `volumen_spike_ratio` < `2.1643` → IC=+0.261 (n=1112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1643 (IC base=-0.008)

- **PATRÓN** `volumen_spike_ratio` > `1.424` → IC=+0.261 (n=1263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.424 (IC base=-0.008)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.205 (n=5390)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0096 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.4565` → IC=+0.187 (n=14430)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4565 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.6743` → IC=+0.291 (n=1581)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6743 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.637` → IC=+0.157 (n=7231)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.637 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `1.173` → IC=+0.256 (n=5938)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.173 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `0.6892` → IC=+0.261 (n=5305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6892 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.2396` → IC=+0.269 (n=1771)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2396 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `2.6391` → IC=+0.265 (n=3173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6391 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.287 (n=9081)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.096)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.163 (n=5193)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0091 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.5355` → IC=+0.161 (n=13694)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.5355 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.2414` → IC=+0.261 (n=4789)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2414 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.1942` → IC=+0.266 (n=1623)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1942 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.294` → IC=+0.314 (n=1019)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.294 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `1.5781` → IC=+0.286 (n=3039)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5781 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.6195` → IC=+0.279 (n=2303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6195 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.289 (n=6830)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 78.0 (IC base=+0.075)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.3699` → IC=-0.166 (n=1474)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3699
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=2993)

- **FILTRO** `ibs_20min` > `0.7471` → IC=-0.201 (n=928)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7471
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=2786)

- **FILTRO** `sigma_ewma_delta_pct` > `4.525` → IC=-0.195 (n=814)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.525
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=2900)

- **PATRÓN** `ibs_20min` > `0.9114` → IC=+0.296 (n=1117)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9114 (IC base=+0.033)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.09` → IC=+0.211 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.09 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` > `0.2294` → IC=+0.292 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2294 (IC base=+0.033)

- **PATRÓN** `volumen_spike_ratio` < `1.4472` → IC=+0.228 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4472 (IC base=+0.033)

- **PATRÓN** `volumen_spike_ratio` > `2.2443` → IC=+0.262 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2443 (IC base=+0.033)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.263 (n=971)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.033)

- **PATRÓN** `ibs_20min` < `0.1593` → IC=+0.160 (n=929)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1593 (IC base=-0.027)

- **PATRÓN** `volumen_pendiente_norm` < `0.2689` → IC=+0.401 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2689 (IC base=-0.027)

- **PATRÓN** `volumen_spike_ratio` < `2.4877` → IC=+0.403 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4877 (IC base=-0.027)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.401 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=-0.027)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1138` → IC=+0.206 (n=817)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1138 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` < `1.1961` → IC=+0.182 (n=1561)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.1961 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` > `0.6809` → IC=+0.190 (n=1395)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 0.6809 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` < `0.0744` → IC=+0.182 (n=1444)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` < 0.0744 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.2732` → IC=+0.213 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2732 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `1.4225` → IC=+0.209 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4225 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` > `2.4708` → IC=+0.189 (n=513)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.4708 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `220.0` → IC=+0.230 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 220.0 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` < `0.1086` → IC=+0.232 (n=976)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1086 (IC base=+0.002)

- **PATRÓN** `volumen_regimen` > `0.6201` → IC=+0.235 (n=988)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6201 (IC base=+0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2707` → IC=+0.298 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2707 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.5384` → IC=+0.234 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5384 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.1651` → IC=+0.252 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1651 (IC base=+0.002)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.300 (n=797)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.260)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.266 (n=2510)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.260)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.261 (n=2145)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.260)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.306 (n=1244)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.27` → IC=+0.293 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.27 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` < `0.0986` → IC=+0.272 (n=2067)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0986 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` > `1.6122` → IC=+0.266 (n=2300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6122 (IC base=+0.260)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.272 (n=2812)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `1981.341` → IC=+0.282 (n=1083)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1981.341 (IC base=+0.260)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.331 (n=925)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.1808` → IC=+0.306 (n=898)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1808 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.326 (n=786)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.290)

- **PATRÓN** `ibs_20min` < `0.3644` → IC=+0.292 (n=2041)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3644 (IC base=+0.290)

- **PATRÓN** `ibs_20min` > `0.25` → IC=+0.293 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.25 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.67` → IC=+0.311 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.67 (IC base=+0.290)

- **PATRÓN** `volumen_pendiente_norm` < `0.1966` → IC=+0.288 (n=1982)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1966 (IC base=+0.290)

- **PATRÓN** `volumen_pendiente_norm` > `0.3414` → IC=+0.306 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3414 (IC base=+0.290)

- **PATRÓN** `volumen_spike_ratio` < `1.7224` → IC=+0.301 (n=854)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7224 (IC base=+0.290)

- **PATRÓN** `volumen_spike_ratio` > `2.6496` → IC=+0.297 (n=880)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6496 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `2061.827` → IC=+0.315 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2061.827 (IC base=+0.290)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.285 (n=1311)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.290)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7426` → IC=-0.184 (n=962)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7426
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=2887)

- **PATRÓN** `ibs_20min` > `0.8856` → IC=+0.173 (n=902)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.8856 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` < `0.3683` → IC=+0.228 (n=1209)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3683 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` < `1.0144` → IC=+0.239 (n=1095)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0144 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` < `0.1637` → IC=+0.232 (n=1320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1637 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.102` → IC=+0.246 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.102 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` < `1.3934` → IC=+0.250 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3934 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` > `2.1367` → IC=+0.232 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1367 (IC base=+0.028)

- **PATRÓN** `ballena_activa_n` < `108.0` → IC=+0.261 (n=1082)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 108.0 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` < `0.1923` → IC=+0.229 (n=835)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1923 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` < `1.0374` → IC=+0.234 (n=750)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0374 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` < `0.1021` → IC=+0.243 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1021 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2917` → IC=+0.281 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2917 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.7992` → IC=+0.267 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7992 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.4526` → IC=+0.256 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4526 (IC base=-0.001)

- **PATRÓN** `ballena_activa_n` < `127.0` → IC=+0.255 (n=814)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 127.0 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7636` → IC=-0.203 (n=1709)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7636
  - _Potencial_: sin este filtro IC_bueno=+0.298 (n=1709)

- **FILTRO** `ibs_20min` > `0.6538` → IC=-0.235 (n=845)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6538
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=2537)

- **FILTRO** `sigma_ewma_delta_pct` > `8.569` → IC=-0.238 (n=387)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.569
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=2995)

- **PATRÓN** `ibs_20min` > `0.7636` → IC=+0.298 (n=1709)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7636 (IC base=+0.047)

- **PATRÓN** `dist_vwap_pct` > `0.213` → IC=+0.332 (n=770)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.213 (IC base=+0.047)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.607` → IC=+0.169 (n=535)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.607 (IC base=+0.047)

- **PATRÓN** `volumen_regimen` < `0.8471` → IC=+0.328 (n=863)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8471 (IC base=+0.047)

- **PATRÓN** `volumen_regimen` > `0.6292` → IC=+0.316 (n=1294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6292 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` < `0.1583` → IC=+0.315 (n=1340)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1583 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.2751` → IC=+0.352 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2751 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` < `1.443` → IC=+0.336 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.443 (IC base=+0.047)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.331 (n=1252)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 57.0 (IC base=+0.047)

- **PATRÓN** `ibs_20min` < `0.5556` → IC=+0.142 (n=2244)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5556 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.2098` → IC=+0.248 (n=987)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2098 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` < `0.7067` → IC=+0.259 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7067 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` > `1.1832` → IC=+0.241 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1832 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` < `0.0995` → IC=+0.243 (n=1024)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0995 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.0719` → IC=+0.253 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0719 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` < `2.4223` → IC=+0.254 (n=1036)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4223 (IC base=+0.030)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.271 (n=1051)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 53.0 (IC base=+0.030)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.342 (n=1645)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.296)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.311 (n=884)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.296)

- **PATRÓN** `ibs_20min` > `0.6511` → IC=+0.329 (n=1841)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6511 (IC base=+0.296)

- **PATRÓN** `dist_vwap_pct` > `0.2098` → IC=+0.327 (n=1047)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2098 (IC base=+0.296)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.776` → IC=+0.317 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.776 (IC base=+0.296)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.306 (n=1842)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6279 (IC base=+0.296)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.340 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.296)

- **PATRÓN** `volumen_spike_ratio` > `1.4265` → IC=+0.307 (n=1763)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4265 (IC base=+0.296)

- **PATRÓN** `libro_liquidez` > `2474.544` → IC=+0.309 (n=1645)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2474.544 (IC base=+0.296)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.330 (n=1563)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.296)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.331 (n=1298)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.298)

- **PATRÓN** `drift_60min` |x|≤ `0.1888` → IC=+0.302 (n=857)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1888 (IC base=+0.298)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.306 (n=973)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.298)

- **PATRÓN** `ibs_20min` < `0.3679` → IC=+0.324 (n=1947)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3679 (IC base=+0.298)

- **PATRÓN** `dist_vwap_pct` > `0.3128` → IC=+0.298 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3128 (IC base=+0.298)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.522` → IC=+0.308 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.522 (IC base=+0.298)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.013` → IC=+0.299 (n=2319)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.013 (IC base=+0.298)

- **PATRÓN** `volumen_regimen` < `0.7185` → IC=+0.300 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7185 (IC base=+0.298)

- **PATRÓN** `volumen_regimen` > `1.2266` → IC=+0.326 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2266 (IC base=+0.298)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.352 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.298)

- **PATRÓN** `volumen_spike_ratio` < `1.4127` → IC=+0.305 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4127 (IC base=+0.298)

- **PATRÓN** `volumen_spike_ratio` > `2.1329` → IC=+0.299 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1329 (IC base=+0.298)

- **PATRÓN** `libro_liquidez` > `2649.5572` → IC=+0.304 (n=1298)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2649.5572 (IC base=+0.298)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.184 (n=3964)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0048 (IC base=+0.178)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.220 (n=3963)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.3458` → IC=+0.188 (n=10447)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3458 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=12334)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `0.5604` → IC=+0.232 (n=11871)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5604 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `0.1663` → IC=+0.207 (n=4907)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1663 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.355` → IC=+0.255 (n=2342)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.355 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `1.1946` → IC=+0.168 (n=7876)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1946 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` > `0.6273` → IC=+0.163 (n=7878)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6273 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2936` → IC=+0.201 (n=1734)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2936 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `2.5994` → IC=+0.189 (n=3832)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.5994 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `2010.77` → IC=+0.183 (n=10605)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2010.77 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.196 (n=10790)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 98.0 (IC base=+0.178)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.186 (n=7637)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0068 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.0802` → IC=+0.224 (n=3817)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0802 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=4293)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` < `0.4975` → IC=+0.235 (n=11440)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4975 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` < `0.1746` → IC=+0.174 (n=8081)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.1746 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.127` → IC=+0.197 (n=1883)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.127 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.673` → IC=+0.178 (n=10601)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 3.673 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `1.18` → IC=+0.164 (n=8173)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.18 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2918` → IC=+0.228 (n=1680)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2918 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `2.621` → IC=+0.187 (n=3568)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.621 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.190 (n=10403)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 102.0 (IC base=+0.178)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.232 (n=665)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.3319` → IC=+0.226 (n=1990)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3319 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.221 (n=728)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.215 (n=1347)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.9243` → IC=+0.290 (n=1327)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9243 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.141` → IC=+0.330 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.141 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.271 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.2575` → IC=+0.221 (n=851)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2575 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.219 (n=2114)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2092.77` → IC=+0.219 (n=664)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2092.77 (IC base=+0.208)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.246 (n=703)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.0973` → IC=+0.295 (n=681)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0973 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.248 (n=1392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.245 (n=764)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.0092` → IC=+0.298 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0092 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` < `0.1002` → IC=+0.244 (n=1339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1002 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.2954` → IC=+0.278 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2954 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` < `1.4323` → IC=+0.259 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4323 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `2.6765` → IC=+0.248 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6765 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.246 (n=1717)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `1548.958` → IC=+0.254 (n=1548)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1548.958 (IC base=+0.242)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.244 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.242)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.218 (n=597)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.1622` → IC=+0.184 (n=1194)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1622 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.171 (n=1883)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.3518` → IC=+0.223 (n=1789)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3518 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.1371` → IC=+0.214 (n=1104)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1371 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.442` → IC=+0.224 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.442 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `0.6923` → IC=+0.170 (n=788)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.6923 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` > `1.0696` → IC=+0.157 (n=811)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.0696 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.184 (n=283)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `1.5081` → IC=+0.172 (n=770)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5081 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `2.4856` → IC=+0.160 (n=584)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.4856 (IC base=+0.155)

- **PATRÓN** `ballena_activa_n` < `230.0` → IC=+0.171 (n=754)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 230.0 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.168 (n=1882)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0058 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.2991` → IC=+0.165 (n=1882)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.2991 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.190 (n=718)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.6119` → IC=+0.203 (n=1882)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6119 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.602` → IC=+0.204 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.602 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.2014` → IC=+0.161 (n=1882)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2014 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.0931` → IC=+0.144 (n=1584)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` < 0.0931 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.158` → IC=+0.147 (n=576)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.158 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.4911` → IC=+0.150 (n=1763)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4911 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.4235` → IC=+0.146 (n=1763)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4235 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `233.0` → IC=+0.168 (n=747)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 233.0 (IC base=+0.144)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.229 (n=1337)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.3972` → IC=+0.223 (n=1765)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3972 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.216 (n=2080)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=1044)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.525` → IC=+0.293 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.525 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.352` → IC=+0.230 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.352 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.7786` → IC=+0.212 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7786 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.7121` → IC=+0.226 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7121 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.218 (n=2371)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `1983.418` → IC=+0.222 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1983.418 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.245 (n=1514)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0102 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.0954` → IC=+0.271 (n=575)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0954 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.288 (n=573)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.3548` → IC=+0.251 (n=1723)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3548 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.616` → IC=+0.278 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.616 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.3529` → IC=+0.273 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3529 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.7274` → IC=+0.240 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7274 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.7291` → IC=+0.243 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7291 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2066.3805` → IC=+0.251 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2066.3805 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.229 (n=1412)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 28.0 (IC base=+0.234)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.173 (n=1915)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0074 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.4031` → IC=+0.165 (n=1915)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.4031 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=1989)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.3133` → IC=+0.210 (n=1915)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3133 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1398` → IC=+0.196 (n=1191)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1398 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.936` → IC=+0.202 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.936 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.8554` → IC=+0.159 (n=1277)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8554 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1013` → IC=+0.178 (n=793)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1013 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.5324` → IC=+0.153 (n=826)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.5324 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `2.4974` → IC=+0.167 (n=626)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.4974 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `4749.981` → IC=+0.191 (n=1277)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 4749.981 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.158 (n=1854)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 143.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.157 (n=2020)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0071 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.3933` → IC=+0.147 (n=2020)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3933 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.180 (n=763)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.6805` → IC=+0.188 (n=2020)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6805 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.1544` → IC=+0.155 (n=2012)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1544 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.871` → IC=+0.158 (n=711)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 6.871 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.8593` → IC=+0.162 (n=1347)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8593 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2969` → IC=+0.203 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2969 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.8013` → IC=+0.136 (n=1257)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.8013 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `2.5308` → IC=+0.139 (n=629)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.5308 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `4468.9287` → IC=+0.173 (n=1347)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 4468.9287 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `120.0` → IC=+0.133 (n=1620)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 120.0 (IC base=+0.129)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.128 (n=724)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0059 (IC base=+0.128)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.172 (n=982)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0101 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.4413` → IC=+0.128 (n=1906)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.4413 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=2207)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.4889` → IC=+0.215 (n=2166)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4889 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.1959` → IC=+0.191 (n=1278)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1959 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.686` → IC=+0.267 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.686 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `1.1845` → IC=+0.142 (n=2166)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1845 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` < `0.1609` → IC=+0.136 (n=2195)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.1609 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.436` → IC=+0.148 (n=700)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.436 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `2841.8261` → IC=+0.213 (n=982)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2841.8261 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.165 (n=660)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 20.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.137 (n=2218)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0106 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.108` → IC=+0.170 (n=741)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.108 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=2247)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.5909` → IC=+0.220 (n=2219)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5909 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` < `0.2001` → IC=+0.148 (n=2078)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2001 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.49` → IC=+0.125 (n=449)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` > 7.49 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.536` → IC=+0.125 (n=1957)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` < 2.536 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.1753` → IC=+0.128 (n=2218)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.1753 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.2741` → IC=+0.154 (n=290)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.2741 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4523` → IC=+0.129 (n=686)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.4523 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `2.4248` → IC=+0.133 (n=685)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.4248 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2696.1504` → IC=+0.190 (n=1006)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2696.1504 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.126 (n=2016)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 50.0 (IC base=+0.119)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.243 (n=1794)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0128 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.282` → IC=+0.228 (n=1339)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.282 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.221 (n=2083)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.227 (n=1362)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` > `0.6583` → IC=+0.256 (n=2007)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6583 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` > `0.1903` → IC=+0.225 (n=1322)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1903 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` < `0.4888` → IC=+0.220 (n=1778)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4888 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.606` → IC=+0.248 (n=914)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.606 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` < `1.1809` → IC=+0.222 (n=2008)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1809 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` > `0.6223` → IC=+0.226 (n=2008)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6223 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.268 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.283 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` < `2.4642` → IC=+0.227 (n=1954)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4642 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `1.8021` → IC=+0.229 (n=1303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8021 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `2646.4017` → IC=+0.230 (n=1338)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2646.4017 (IC base=+0.219)

- **PATRÓN** `sigma_h` < `0.0124` → IC=+0.236 (n=904)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0124 (IC base=+0.226)

- **PATRÓN** `sigma_h` > `0.0225` → IC=+0.238 (n=933)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0225 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.0896` → IC=+0.260 (n=685)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0896 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.247 (n=1001)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` < `0.425` → IC=+0.255 (n=2055)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.425 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.2956` → IC=+0.234 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2956 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.326` → IC=+0.249 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.326 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.7056` → IC=+0.234 (n=1836)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7056 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2775` → IC=+0.286 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2775 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.4331` → IC=+0.227 (n=1904)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4331 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2404.776` → IC=+0.232 (n=1836)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2404.776 (IC base=+0.226)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.208 (n=1347)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.177)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.182 (n=1021)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0086 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.3361` → IC=+0.188 (n=2689)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3361 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.209 (n=1503)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `0.7284` → IC=+0.229 (n=2037)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7284 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.7813` → IC=+0.193 (n=464)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.7813 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.676` → IC=+0.205 (n=1315)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.676 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `0.8649` → IC=+0.196 (n=1823)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8649 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` > `0.6964` → IC=+0.181 (n=2443)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 0.6964 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.1005` → IC=+0.188 (n=1100)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1005 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` < `1.4324` → IC=+0.194 (n=990)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4324 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `2.1994` → IC=+0.181 (n=1346)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.1994 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.181 (n=3459)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.02 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `2734.4955` → IC=+0.182 (n=2730)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2734.4955 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.190 (n=2833)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 150.0 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.145 (n=1076)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0037 (IC base=+0.097)

- **PATRÓN** `ibs_20min` < `0.3715` → IC=+0.163 (n=2144)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.3715 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.135 (n=1068)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 20.0 (IC base=+0.097)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.213 (n=381)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.0997` → IC=+0.221 (n=381)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0997 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.196 (n=780)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 8.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `0.6494` → IC=+0.227 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6494 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.3033` → IC=+0.186 (n=272)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.3033 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.109` → IC=+0.188 (n=370)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 3.109 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.828` → IC=+0.168 (n=917)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 6.828 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `0.8759` → IC=+0.194 (n=577)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.8759 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.0705` → IC=+0.175 (n=340)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.0705 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `2.2101` → IC=+0.178 (n=746)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.2101 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `1.4133` → IC=+0.169 (n=847)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.4133 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `14780.6856` → IC=+0.179 (n=577)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 14780.6856 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `155.0` → IC=+0.203 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 155.0 (IC base=+0.168)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.192 (n=342)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0028 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.3426` → IC=+0.141 (n=1018)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3426 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.136 (n=910)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 7.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.6327` → IC=+0.169 (n=896)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.6327 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.1864` → IC=+0.145 (n=1034)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1864 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.719` → IC=+0.131 (n=196)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 8.719 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.162` → IC=+0.127 (n=921)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.162 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `1.0613` → IC=+0.151 (n=462)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 1.0613 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.1594` → IC=+0.173 (n=270)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1594 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `2.1137` → IC=+0.138 (n=887)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.1137 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.125 (n=1320)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `305.0` → IC=+0.152 (n=868)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 305.0 (IC base=+0.125)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.248 (n=626)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.2023` → IC=+0.229 (n=625)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2023 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.227 (n=983)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.6798` → IC=+0.272 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6798 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.3558` → IC=+0.221 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3558 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` < `0.2051` → IC=+0.215 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2051 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.93` → IC=+0.233 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.93 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` < `0.8407` → IC=+0.216 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8407 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` > `1.1816` → IC=+0.229 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1816 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.1583` → IC=+0.243 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1583 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.4123` → IC=+0.248 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4123 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.4427` → IC=+0.229 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4427 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.1008` → IC=+0.172 (n=312)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.1008 (IC base=+0.074)

- **PATRÓN** `libro_liquidez` > `7105.0758` → IC=+0.135 (n=623)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 7105.0758 (IC base=+0.074)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.169 (n=336)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0095 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.5405` → IC=+0.157 (n=742)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.5405 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.208 (n=354)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.270 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.97` → IC=+0.233 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.97 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.204` → IC=+0.218 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.204 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `1.0551` → IC=+0.179 (n=653)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 1.0551 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` > `0.7177` → IC=+0.163 (n=662)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.7177 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.2786` → IC=+0.191 (n=108)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2786 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `1.4569` → IC=+0.158 (n=238)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4569 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `2.1881` → IC=+0.172 (n=324)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.1881 (IC base=+0.157)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.160 (n=763)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.02 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `3064.7088` → IC=+0.191 (n=247)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 3064.7088 (IC base=+0.157)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.150 (n=667)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.5 (IC base=+0.066)

- **PATRÓN** `libro_liquidez` > `2782.2891` → IC=+0.166 (n=342)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2782.2891 (IC base=+0.066)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.122 (n=622)

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
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.182 (n=5174)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0047 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.221 (n=5157)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=16121)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.5573` → IC=+0.239 (n=13816)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5573 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.1629` → IC=+0.193 (n=5589)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1629 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.338` → IC=+0.251 (n=3782)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.338 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.2248` → IC=+0.169 (n=10360)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2248 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2907` → IC=+0.203 (n=2052)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2907 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6091` → IC=+0.197 (n=5006)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6091 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `1824.38` → IC=+0.184 (n=15465)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1824.38 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `75.0` → IC=+0.205 (n=12435)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 75.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.195 (n=6181)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0054 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.3808` → IC=+0.190 (n=12349)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.3808 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=5240)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.5785` → IC=+0.242 (n=14033)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5785 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` < `0.176` → IC=+0.171 (n=8491)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.176 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.903` → IC=+0.207 (n=1957)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.903 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.645` → IC=+0.189 (n=13544)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 3.645 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `0.7049` → IC=+0.161 (n=4172)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.7049 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.2891` → IC=+0.252 (n=1890)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2891 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.6102` → IC=+0.198 (n=4409)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.6102 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `1759.007` → IC=+0.187 (n=14032)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 1759.007 (IC base=+0.187)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.214 (n=8634)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.187)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.237 (n=847)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.3497` → IC=+0.220 (n=2537)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3497 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.230 (n=1224)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.222 (n=1713)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.326 (n=976)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.646` → IC=+0.346 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.646 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.2784` → IC=+0.285 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2784 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.2714` → IC=+0.234 (n=1102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2714 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.234 (n=2655)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `2014.3` → IC=+0.231 (n=1150)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2014.3 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.234 (n=1056)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.217)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.263 (n=2154)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0082 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.1214` → IC=+0.274 (n=946)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1214 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.266 (n=1955)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.285 (n=2153)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.386` → IC=+0.264 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.386 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` < `0.0954` → IC=+0.258 (n=1914)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0954 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.2826` → IC=+0.276 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2826 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `2.2727` → IC=+0.267 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2727 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.259 (n=2385)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1563.22` → IC=+0.268 (n=2149)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1563.22 (IC base=+0.258)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.260 (n=716)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.258)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.201 (n=842)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.177` → IC=+0.163 (n=1666)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.177 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=2607)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.2578` → IC=+0.206 (n=2499)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2578 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1243` → IC=+0.194 (n=1336)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1243 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.648` → IC=+0.163 (n=410)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.648 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.169` → IC=+0.155 (n=2291)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.169 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.629` → IC=+0.175 (n=834)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.629 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.071` → IC=+0.153 (n=2232)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.071 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2706` → IC=+0.173 (n=353)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2706 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1727` → IC=+0.158 (n=2146)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1727 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.525` → IC=+0.154 (n=2180)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.525 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `10298.6539` → IC=+0.151 (n=2499)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 10298.6539 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `268.0` → IC=+0.181 (n=1051)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 268.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.165 (n=2091)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.2565` → IC=+0.163 (n=1840)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.2565 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=791)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.7006` → IC=+0.199 (n=2091)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.7006 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.1328` → IC=+0.166 (n=1940)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1328 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.218` → IC=+0.159 (n=464)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 9.218 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.1817` → IC=+0.155 (n=2091)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.1817 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.2169` → IC=+0.198 (n=392)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2169 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.4236` → IC=+0.151 (n=1987)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4236 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.7697` → IC=+0.160 (n=1325)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7697 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `338.0` → IC=+0.146 (n=1265)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 338.0 (IC base=+0.145)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.248 (n=857)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.229 (n=2686)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.227 (n=2308)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=954)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.366` → IC=+0.316 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.366 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` < `0.2094` → IC=+0.224 (n=2616)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2094 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.7011` → IC=+0.238 (n=1129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7011 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.231 (n=3036)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1852.3672` → IC=+0.234 (n=1713)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1852.3672 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.243 (n=2115)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.1805` → IC=+0.254 (n=1057)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1805 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.267 (n=909)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0252` → IC=+0.302 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0252 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.071` → IC=+0.290 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.071 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3446` → IC=+0.296 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3446 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.7283` → IC=+0.236 (n=1002)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7283 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1351` → IC=+0.248 (n=1517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1351 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `2062.62` → IC=+0.266 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2062.62 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.254 (n=1047)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.240)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.202 (n=1166)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.4203` → IC=+0.157 (n=2650)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.4203 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.158 (n=2755)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.253` → IC=+0.193 (n=2650)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.253 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.141` → IC=+0.168 (n=1425)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.141 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.171` → IC=+0.160 (n=1076)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.171 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `0.8719` → IC=+0.163 (n=1768)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8719 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.2831` → IC=+0.183 (n=348)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2831 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.5199` → IC=+0.166 (n=1137)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.5199 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.1716` → IC=+0.158 (n=1172)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.1716 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `6925.4045` → IC=+0.237 (n=1202)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6925.4045 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.171 (n=1127)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 77.0 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.189 (n=732)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0033 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.4396` → IC=+0.140 (n=2196)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4396 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=804)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.7398` → IC=+0.186 (n=2196)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.7398 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.1491` → IC=+0.144 (n=1977)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1491 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.146` → IC=+0.177 (n=335)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 11.146 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.8747` → IC=+0.140 (n=1465)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.8747 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2969` → IC=+0.235 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2969 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `2.2242` → IC=+0.133 (n=1857)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.2242 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.4287` → IC=+0.139 (n=2109)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.4287 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `5240.6227` → IC=+0.204 (n=996)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5240.6227 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `157.0` → IC=+0.130 (n=2117)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 157.0 (IC base=+0.130)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.148 (n=1781)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0083 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=977)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.4474` → IC=+0.199 (n=2668)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.4474 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `1.0588` → IC=+0.206 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0588 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.855` → IC=+0.267 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.855 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `0.8855` → IC=+0.149 (n=1780)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8855 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` < `0.0984` → IC=+0.126 (n=2509)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.0984 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.137 (n=345)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `2.4754` → IC=+0.125 (n=2603)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.4754 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `1.4643` → IC=+0.127 (n=2603)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.4643 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.130 (n=2728)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2875.1364` → IC=+0.252 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2875.1364 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.137 (n=830)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 25.0 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.142 (n=2554)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0111 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1334` → IC=+0.160 (n=850)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1334 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.160 (n=1191)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 15.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.6397` → IC=+0.215 (n=2549)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6397 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.2162` → IC=+0.139 (n=2174)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.2162 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.348` → IC=+0.135 (n=2451)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 3.348 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.6417` → IC=+0.141 (n=850)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.6417 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2234` → IC=+0.172 (n=428)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2234 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4343` → IC=+0.147 (n=792)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4343 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2724.0258` → IC=+0.211 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2724.0258 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.139 (n=2097)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 48.0 (IC base=+0.120)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0136` → IC=+0.244 (n=2273)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0136 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=2654)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.235 (n=1702)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.6074` → IC=+0.270 (n=2273)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6074 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` > `0.1993` → IC=+0.243 (n=1402)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1993 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.737` → IC=+0.270 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.737 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` < `1.2311` → IC=+0.231 (n=2545)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2311 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.6434` → IC=+0.229 (n=2544)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6434 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2358` → IC=+0.248 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2358 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `2.5092` → IC=+0.244 (n=825)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5092 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.227 (n=3299)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `2654.4856` → IC=+0.237 (n=1696)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2654.4856 (IC base=+0.225)

- **PATRÓN** `sigma_h` > `0.0229` → IC=+0.248 (n=1201)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0229 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.235 (n=2486)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` < `0.51` → IC=+0.264 (n=2655)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.51 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.19` → IC=+0.259 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.19 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `1.228` → IC=+0.255 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.228 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2798` → IC=+0.299 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2798 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.4288` → IC=+0.229 (n=2451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4288 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `2418.5428` → IC=+0.230 (n=2366)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2418.5428 (IC base=+0.227)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.221 (n=2409)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.227)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.186 (n=4620)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.239 (n=1559)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.5036` → IC=+0.210 (n=4665)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5036 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=1666)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.9404` → IC=+0.246 (n=1555)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9404 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `0.1722` → IC=+0.205 (n=1781)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1722 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` < `0.4338` → IC=+0.208 (n=3347)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4338 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.78` → IC=+0.210 (n=1521)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.78 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.65` → IC=+0.201 (n=4161)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.65 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `0.7064` → IC=+0.217 (n=1501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7064 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `0.886` → IC=+0.205 (n=2274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.886 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.166` → IC=+0.221 (n=1304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.166 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `1.4535` → IC=+0.207 (n=1532)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4535 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `2.2626` → IC=+0.204 (n=2083)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2626 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=3614)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `2599.0182` → IC=+0.207 (n=4665)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2599.0182 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.230 (n=1159)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.184)

- **PATRÓN** `drift_60min` |x|≤ `0.4908` → IC=+0.200 (n=3477)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4908 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=1170)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.200 (n=1569)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` < `0.728` → IC=+0.190 (n=3477)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.728 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` > `0.6725` → IC=+0.196 (n=600)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.6725 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` < `0.2386` → IC=+0.181 (n=3145)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.2386 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.149` → IC=+0.192 (n=3481)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 6.149 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` < `1.0969` → IC=+0.195 (n=2889)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 1.0969 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` < `0.0972` → IC=+0.189 (n=3179)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.0972 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` < `1.5312` → IC=+0.189 (n=1509)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.5312 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `1.806` → IC=+0.192 (n=2287)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 1.806 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.186 (n=4620)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.184)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.195 (n=2996)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 162.0 (IC base=+0.184)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.252 (n=571)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.0885` → IC=+0.271 (n=216)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0885 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.242 (n=677)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.239 (n=301)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.4994` → IC=+0.262 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4994 (IC base=+0.236)

- **PATRÓN** `dist_vwap_pct` < `0.3306` → IC=+0.249 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3306 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.115` → IC=+0.245 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.115 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.615` → IC=+0.238 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.615 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` < `1.2117` → IC=+0.242 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2117 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` > `0.8594` → IC=+0.251 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8594 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.333 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `1.8328` → IC=+0.246 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8328 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `12382.594` → IC=+0.251 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12382.594 (IC base=+0.236)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.243 (n=527)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.3687` → IC=+0.176 (n=1192)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3687 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=431)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.190 (n=453)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 5.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` < `0.1485` → IC=+0.189 (n=525)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.1485 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.6078` → IC=+0.170 (n=541)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.6078 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.6858` → IC=+0.208 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6858 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` < `0.157` → IC=+0.164 (n=1172)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.157 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.406` → IC=+0.182 (n=1172)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 6.406 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `0.8847` → IC=+0.198 (n=795)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.8847 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.2162` → IC=+0.183 (n=247)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2162 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.409` → IC=+0.173 (n=396)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.409 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `1.8022` → IC=+0.176 (n=791)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.8022 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `11334.4505` → IC=+0.176 (n=1192)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 11334.4505 (IC base=+0.163)

- **PATRÓN** `ballena_activa_n` < `699.0` → IC=+0.175 (n=1147)

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
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0089 (IC base=+0.197)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.203 (n=230)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.6094` → IC=+0.223 (n=507)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6094 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.231 (n=344)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` < `0.7187` → IC=+0.215 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7187 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` > `0.5232` → IC=+0.215 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5232 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` < `0.3106` → IC=+0.202 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3106 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.952` → IC=+0.202 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.952 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.926` → IC=+0.205 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.926 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `0.7555` → IC=+0.207 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7555 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` > `0.9331` → IC=+0.203 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9331 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` < `0.1071` → IC=+0.223 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1071 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `2.1886` → IC=+0.234 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1886 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `2975.5942` → IC=+0.219 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2975.5942 (IC base=+0.197)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.232 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 47.0 (IC base=+0.197)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.160 (n=672)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0039 (IC base=+0.068)

- **PATRÓN** `ibs_20min` > `0.4045` → IC=+0.143 (n=1434)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.4045 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.3558` → IC=+0.152 (n=512)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.3558 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.3` → IC=+0.174 (n=317)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 11.3 (IC base=+0.068)

- **PATRÓN** `ibs_20min` < `0.1757` → IC=+0.271 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1757 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.0969` → IC=+0.147 (n=711)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.0969 (IC base=+0.073)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.617` → IC=+0.175 (n=118)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 10.617 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.1476` → IC=+0.211 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1476 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` < `2.6098` → IC=+0.131 (n=664)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 2.6098 (IC base=+0.073)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.134 (n=514)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0056 (IC base=+0.088)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.146 (n=173)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 18.0 (IC base=+0.088)

- **PATRÓN** `ibs_20min` > `0.537` → IC=+0.191 (n=432)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.537 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.119` → IC=+0.159 (n=253)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.119 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.2737` → IC=+0.243 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2737 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` < `0.2112` → IC=+0.139 (n=364)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.2112 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` < `1.1907` → IC=+0.120 (n=330)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` < 1.1907 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.0693` → IC=+0.179 (n=135)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.0693 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` < `2.5595` → IC=+0.125 (n=307)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.5595 (IC base=+0.086)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.152 (n=334)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0046 (IC base=+0.092)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.124 (n=469)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 7.0 (IC base=+0.092)

- **PATRÓN** `ibs_20min` > `0.6494` → IC=+0.202 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6494 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` > `0.1258` → IC=+0.188 (n=245)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1258 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.328` → IC=+0.250 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.328 (IC base=+0.092)

- **PATRÓN** `volumen_regimen` < `0.8144` → IC=+0.124 (n=312)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 0.8144 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `1633.9423` → IC=+0.132 (n=210)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 1633.9423 (IC base=+0.092)

- **PATRÓN** `ibs_20min` < `0.0123` → IC=+0.333 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0123 (IC base=+0.037)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.103` → IC=+0.237 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.103 (IC base=+0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.1363` → IC=+0.197 (n=64)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1363 (IC base=+0.037)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` > `0.1333` → IC=-0.212 (n=57)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1333
  - _Potencial_: sin este filtro IC_bueno=+0.264 (n=172)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.160 (n=327)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.75 (IC base=+0.025)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.817` → IC=+0.150 (n=135)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 7.817 (IC base=+0.025)

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

- **FILTRO** `sigma_h` > `0.0046` → IC=-0.333 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0046
  - _Potencial_: sin este filtro IC_bueno=-0.261 (n=69)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.375 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.246 (n=69)

- **FILTRO** `dist_vwap_pct` > `0.1206` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1206
  - _Potencial_: sin este filtro IC_bueno=-0.258 (n=64)

- **FILTRO** `libro_liquidez` < `1269.5074` → IC=-0.292 (n=22)

  - _Acción_: SKIP cuando `libro_liquidez` < 1269.5074
  - _Potencial_: sin este filtro IC_bueno=-0.275 (n=69)

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
- **PATRÓN** `libro_liquidez` > `2859.854` → IC=+0.131 (n=540)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2859.854 (IC base=+0.102)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2859.854` → IC=+0.131 (n=540)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2859.854 (IC base=+0.102)

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
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=3304)

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

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.495 (IC base=+0.028)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=1214)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=1168)

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
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=731)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=731)

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
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=195)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=219)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=254)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.121 (n=56)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=198)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=232)

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
- **FILTRO** `py_entrada` < `0.4` → IC=-0.129 (n=1155)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=3005)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `restante_min` < `3.89` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `restante_min` < 3.89
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **FILTRO** `lag_apertura_s` > `66.61` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `lag_apertura_s` > 66.61
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.169 (n=125)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` < 0.46 (IC base=+0.012)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.180 (n=48)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=209)

- **FILTRO** `lag_apertura_s` > `268.36` → IC=-0.129 (n=87)

  - _Acción_: SKIP cuando `lag_apertura_s` > 268.36
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=170)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **PATRÓN** `py_entrada` < `0.57` → IC=+0.148 (n=69)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.57 (IC base=+0.055)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.143 (n=292)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=100)

- **FILTRO** `profundidad_ratio` < `39.0` → IC=-0.190 (n=98)

  - _Acción_: SKIP cuando `profundidad_ratio` < 39.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=294)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.254 (n=63)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=275)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.124 (n=232)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=249)

- **FILTRO** `restante_min` < `3.8` → IC=-0.137 (n=235)

  - _Acción_: SKIP cuando `restante_min` < 3.8
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=246)

- **FILTRO** `lag_apertura_s` > `98.09` → IC=-0.173 (n=163)

  - _Acción_: SKIP cuando `lag_apertura_s` > 98.09
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=318)

- **FILTRO** `profundidad_ratio` < `22.9` → IC=-0.122 (n=117)

  - _Acción_: SKIP cuando `profundidad_ratio` < 22.9
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=240)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.180 (n=73)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=297)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **PATRÓN** `py_entrada` > `0.49` → IC=+0.133 (n=145)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` > 0.49 (IC base=-0.011)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.128 (n=304)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=109)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.179 (n=107)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=400)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.164 (n=5400)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=17086)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.169 (n=5782)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=17452)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.191 (n=994)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=3059)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.165 (n=963)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=3198)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.139 (n=1066)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 1.0 (IC base=+0.038)

- **PATRÓN** `libro_liquidez` > `1416.7` → IC=+0.136 (n=2027)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 1416.7 (IC base=+0.038)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.125 (n=1936)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.5 (IC base=+0.014)

- **PATRÓN** `libro_liquidez` > `1539.8007` → IC=+0.147 (n=1415)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 1539.8007 (IC base=+0.014)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.174 (n=812)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=2506)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.174 (n=1003)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=3093)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.184 (n=1058)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=3178)

- **PATRÓN** `ibs_20min` > `0.9632` → IC=+0.127 (n=1393)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` > 0.9632 (IC base=+0.037)

- **PATRÓN** `libro_liquidez` > `1843.918` → IC=+0.124 (n=1393)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 1843.918 (IC base=+0.037)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=2295)

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
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=423)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.263 (n=137)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=411)

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
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=34705)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=12204)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=38070)

- **FILTRO** `ibs_7min` < `0.2434` → IC=-0.230 (n=12568)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2434
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=37706)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.152 (n=17040)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=33234)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.238 (n=15440)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=48189)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.180 (n=15745)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=47884)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.145 (n=2514)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=6173)

- **FILTRO** `py_entrada` < `0.46` → IC=-0.236 (n=4313)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=4374)

- **FILTRO** `ibs_7min` < `0.7093` → IC=-0.247 (n=2865)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7093
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=5822)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.175 (n=1957)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=6730)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.270 (n=2729)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=8315)

- **FILTRO** `ibs_7min` > `0.775` → IC=-0.211 (n=2757)

  - _Acción_: SKIP cuando `ibs_7min` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=8287)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.263 (n=1946)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=6585)

- **FILTRO** `ibs_7min` < `0.7295` → IC=-0.195 (n=2131)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7295
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=6400)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.190 (n=2132)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6399)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.264 (n=2102)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=6557)

- **FILTRO** `ibs_7min` > `0.2665` → IC=-0.194 (n=2164)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2665
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=6495)

- **FILTRO** `ballena_activa_n` > `149.0` → IC=-0.182 (n=2159)

  - _Acción_: SKIP cuando `ballena_activa_n` > 149.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=6500)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.155 (n=2034)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=6234)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.316 (n=2009)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=6259)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.245 (n=2711)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=5557)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.192 (n=2058)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6210)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.249 (n=2687)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=9056)

- **FILTRO** `ibs_7min` > `0.7333` → IC=-0.175 (n=2934)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7333
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=8809)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.262 (n=1908)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=6306)

- **FILTRO** `ibs_7min` < `0.7326` → IC=-0.187 (n=2053)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7326
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=6161)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.192 (n=2025)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=6189)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.268 (n=1892)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=6622)

- **FILTRO** `ibs_7min` > `0.275` → IC=-0.179 (n=2128)

  - _Acción_: SKIP cuando `ibs_7min` > 0.275
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=6386)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.178 (n=2063)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=6451)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=1944)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=6376)

- **FILTRO** `ibs_7min` < `0.2222` → IC=-0.234 (n=2049)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2222
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=6271)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.184 (n=2876)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=9295)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.281 (n=2044)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=6210)

- **FILTRO** `ibs_7min` < `0.2183` → IC=-0.220 (n=2063)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2183
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=6191)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.199 (n=1888)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=6366)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.210 (n=2785)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=8713)

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
- **PATRÓN** `delta_ratio` |x|> `0.3982` → IC=+0.146 (n=1078)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio` |x|> 0.3982 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.143 (n=499)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 14.0 (IC base=+0.130)

- **PATRÓN** `total_vol_5m` < `443.866` → IC=+0.163 (n=360)

  - _Acción_: Kelly boost +0.81€ cuando `total_vol_5m` < 443.866 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `3685.1446` → IC=+0.138 (n=489)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 3685.1446 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.159 (n=367)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 13.0 (IC base=+0.130)

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
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio` |x|> 0.4156 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.152 (n=225)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 4.0 (IC base=+0.130)

- **PATRÓN** `total_vol_5m` < `392.5834` → IC=+0.214 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 392.5834 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `7950.7251` → IC=+0.133 (n=145)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 7950.7251 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.190 (n=98)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 72.0 (IC base=+0.130)

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
- **PATRÓN** `libro_spread` < `0.01` → IC=+0.180 (n=123)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.091)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.4547` → IC=-0.256 (n=43)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.4547
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=130)

- **FILTRO** `sigma_h` > `0.006` → IC=-0.297 (n=205)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=403)

- **FILTRO** `T_h` > `129.6273` → IC=-0.212 (n=151)

  - _Acción_: SKIP cuando `T_h` > 129.6273
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=457)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.177 (n=153)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0034 (IC base=-0.080)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `88.1766` → IC=-0.287 (n=45)

  - _Acción_: SKIP cuando `T_h` > 88.1766
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=138)

- **FILTRO** `pct_vs_K` |x|> `4.0446` → IC=-0.223 (n=45)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.0446
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=138)

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
- **FILTRO** `sigma_h` < `0.0043` → IC=-0.194 (n=47)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0043
  - _Potencial_: sin este filtro IC_bueno=-0.129 (n=141)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=291)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=366)

- **FILTRO** `streak_estiramiento` > `0.8566` → IC=-0.175 (n=81)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.8566
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=244)

- **PATRÓN** `streak_estiramiento` < `0.5637` → IC=+0.191 (n=163)

  - _Acción_: Kelly boost +0.95€ cuando `streak_estiramiento` < 0.5637 (IC base=+0.040)

- **PATRÓN** `libro_liquidez` > `2526.423` → IC=+0.130 (n=133)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2526.423 (IC base=+0.040)

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

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.142 (n=107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 7.0 (IC base=+0.084)

- **PATRÓN** `streak_estiramiento` < `0.4503` → IC=+0.185 (n=90)

  - _Acción_: Kelly boost +0.92€ cuando `streak_estiramiento` < 0.4503 (IC base=+0.084)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.167 (n=76)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 29.0 (IC base=+0.084)

- **PATRÓN** `libro_liquidez` > `2312.8768` → IC=+0.156 (n=120)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2312.8768 (IC base=+0.084)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=720)

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
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=933)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1327)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1073)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=1089)

### STRUCT_NO_15M
- **FILTRO** `hora_utc` < `19.0` → IC=-0.227 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3792)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `hora_utc` < `19.0` → IC=-0.227 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=2068)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.199 (n=1090)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0045 (IC base=+0.184)

- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.205 (n=1090)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.184)

- **PATRÓN** `drift_60min` |x|≤ `0.1708` → IC=+0.196 (n=2876)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1708 (IC base=+0.184)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3519` → IC=+0.193 (n=2933)

  - _Acción_: Kelly boost +0.97€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3519 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.190 (n=3033)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 6.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.188 (n=3006)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 15.0 (IC base=+0.184)

- **PATRÓN** `ibs_15` > `0.5749` → IC=+0.263 (n=3268)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5749 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` > `0.1236` → IC=+0.180 (n=1544)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.1236 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` < `0.4805` → IC=+0.171 (n=2867)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.4805 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.67` → IC=+0.258 (n=854)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.67 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `5050.3314` → IC=+0.205 (n=1090)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5050.3314 (IC base=+0.184)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=1291)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.232 (n=569)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.0585` → IC=+0.262 (n=191)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0585 (IC base=+0.220)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2509` → IC=+0.249 (n=189)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2509 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.242 (n=532)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.220)

- **PATRÓN** `ibs_15` > `0.7251` → IC=+0.284 (n=567)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7251 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `0.1369` → IC=+0.247 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1369 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.114` → IC=+0.303 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.114 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.222 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `16282.4193` → IC=+0.259 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16282.4193 (IC base=+0.220)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.36` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.36
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=724)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.159 (n=643)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0065 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.0668` → IC=+0.149 (n=283)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.0668 (IC base=+0.144)

- **PATRÓN** `drift_15min` |x|≤ `0.3986` → IC=+0.145 (n=215)

  - _Acción_: Kelly boost +0.73€ cuando `drift_15min` |x|≤ 0.3986 (IC base=+0.144)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1466` → IC=+0.153 (n=428)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio_macro` |x|> 0.1466 (IC base=+0.144)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1312` → IC=+0.156 (n=251)

  - _Acción_: Kelly boost +0.78€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1312 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.149 (n=593)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 6.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.148 (n=672)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 17.0 (IC base=+0.144)

- **PATRÓN** `ibs_15` > `0.5639` → IC=+0.247 (n=642)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5639 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1154` → IC=+0.157 (n=403)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1154 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.6102` → IC=+0.146 (n=730)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.6102 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.028` → IC=+0.289 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.028 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `3555.0527` → IC=+0.153 (n=574)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3555.0527 (IC base=+0.144)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `18.363` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.363
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=282)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.144 (n=223)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0059 (IC base=+0.102)

- **PATRÓN** `drift_60min` |x|≤ `0.1607` → IC=+0.146 (n=445)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1607 (IC base=+0.102)

- **PATRÓN** `ibs_15` > `0.9048` → IC=+0.264 (n=223)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9048 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=370)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.102)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.407` → IC=+0.153 (n=70)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 8.407 (IC base=+0.023)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0236` → IC=+0.261 (n=253)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0236 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.1697` → IC=+0.219 (n=666)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1697 (IC base=+0.209)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3395` → IC=+0.240 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3395 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.224 (n=672)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.209)

- **PATRÓN** `ibs_15` > `0.561` → IC=+0.294 (n=757)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.561 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` > `0.1836` → IC=+0.219 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1836 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.0` → IC=+0.236 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.0 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2985.1852` → IC=+0.296 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2985.1852 (IC base=+0.209)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.164 (n=750)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.82€ cuando `ibs_15` < 0.1111 (IC base=+0.066)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.370 (n=398)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.362)

- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.370 (n=596)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0028 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1506` → IC=+0.382 (n=397)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1506 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2297` → IC=+0.380 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2297 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.375 (n=600)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.398 (n=596)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.4169` → IC=+0.391 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4169 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.772` → IC=+0.384 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.772 (IC base=+0.362)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.367 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `3505.1277` → IC=+0.371 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3505.1277 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.363 (n=276)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.364)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.388 (n=105)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.364)

- **PATRÓN** `drift_15min` |x|≤ `0.5105` → IC=+0.363 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5105 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2136` → IC=+0.389 (n=142)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2136 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1371` → IC=+0.396 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1371 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.383 (n=314)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.8077` → IC=+0.389 (n=314)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8077 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.2458` → IC=+0.394 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2458 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.859` → IC=+0.384 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.859 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `15285.027` → IC=+0.390 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15285.027 (IC base=+0.364)

- **PATRÓN** `ballena_activa_n` < `489.0` → IC=+0.411 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 489.0 (IC base=+0.364)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.358 (n=125)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.357)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.377 (n=128)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.357)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0902` → IC=+0.370 (n=252)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0902 (IC base=+0.357)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2986` → IC=+0.376 (n=224)

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

- **PATRÓN** `dist_vwap_pct` < `0.2918` → IC=+0.359 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2918 (IC base=+0.357)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.352` → IC=+0.385 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.352 (IC base=+0.357)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.361 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.357)

- **PATRÓN** `libro_liquidez` > `3939.9229` → IC=+0.385 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3939.9229 (IC base=+0.357)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0123` → IC=-0.220 (n=1024)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0123
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=3076)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.207 (n=1594)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=2506)

- **FILTRO** `libro_liquidez` < `4162.3546` → IC=-0.150 (n=2706)

  - _Acción_: SKIP cuando `libro_liquidez` < 4162.3546
  - _Potencial_: sin este filtro IC_bueno=+0.099 (n=1394)

- **PATRÓN** `ibs_15` > `0.6349` → IC=+0.284 (n=991)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6349 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` > `0.1102` → IC=+0.210 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1102 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` < `0.424` → IC=+0.203 (n=961)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.424 (IC base=-0.065)

- **PATRÓN** `delta_ratio_macro` |x|> `0.229` → IC=+0.270 (n=1119)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.229 (IC base=-0.012)

- **PATRÓN** `ibs_15` < `0.3535` → IC=+0.282 (n=3355)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3535 (IC base=-0.012)

- **PATRÓN** `dist_vwap_pct` > `0.6556` → IC=+0.279 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6556 (IC base=-0.012)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.210 (n=580)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=1742)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.232 (n=579)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=1743)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.199 (n=1447)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=875)

- **FILTRO** `sigma_ewma_delta_pct` > `23.498` → IC=-0.263 (n=336)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.498
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=1986)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.212 (n=64)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=2258)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.126 (n=701)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0052 (IC base=+0.099)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2047` → IC=+0.299 (n=142)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2047 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.120 (n=704)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 5.0 (IC base=+0.099)

- **PATRÓN** `ibs_15` > `0.7591` → IC=+0.335 (n=313)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7591 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.1047` → IC=+0.304 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1047 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` < `0.3672` → IC=+0.297 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3672 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.471` → IC=+0.146 (n=162)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 24.471 (IC base=+0.099)

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
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=644)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.163 (n=437)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0058 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.161 (n=496)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0034 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.0709` → IC=+0.192 (n=219)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.0709 (IC base=+0.153)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1405` → IC=+0.155 (n=331)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio_macro` |x|> 0.1405 (IC base=+0.153)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.191 (n=377)

  - _Acción_: Kelly boost +0.96€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.176 (n=353)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 11.0 (IC base=+0.153)

- **PATRÓN** `ibs_15` > `0.6258` → IC=+0.259 (n=496)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6258 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.455` → IC=+0.159 (n=133)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.455 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.2726` → IC=+0.155 (n=465)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.2726 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.52` → IC=+0.265 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.52 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=644)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `10452.9608` → IC=+0.167 (n=166)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 10452.9608 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.257 (n=521)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.3569` → IC=+0.243 (n=1039)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3569 (IC base=+0.243)

- **PATRÓN** `drift_15min` |x|≤ `0.7675` → IC=+0.256 (n=1039)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7675 (IC base=+0.243)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1572` → IC=+0.257 (n=787)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1572 (IC base=+0.243)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3304` → IC=+0.244 (n=1142)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3304 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.251 (n=439)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.244 (n=459)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.243)

- **PATRÓN** `ibs_15` < `0.3685` → IC=+0.273 (n=1180)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3685 (IC base=+0.243)

- **PATRÓN** `dist_vwap_pct` > `0.7887` → IC=+0.282 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7887 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.549` → IC=+0.255 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.549 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.569` → IC=+0.246 (n=1235)

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

- **FILTRO** `sigma_ewma_delta_pct` > `18.156` → IC=-0.144 (n=490)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.156
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=3927)

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

- **PATRÓN** `delta_ratio_macro` |x|> `0.0649` → IC=+0.244 (n=529)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0649 (IC base=-0.038)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.288 (n=530)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` < `0.4491` → IC=+0.251 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4491 (IC base=-0.038)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0196` → IC=-0.246 (n=570)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0196
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=571)

- **FILTRO** `drift_15min` |x|> `1.2387` → IC=-0.267 (n=285)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2387
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=856)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=1122)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.203)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.203)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0679` → IC=+0.270 (n=727)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0679 (IC base=-0.025)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1132` → IC=+0.298 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1132 (IC base=-0.025)

- **PATRÓN** `ibs_15` < `0.3297` → IC=+0.295 (n=814)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3297 (IC base=-0.025)

- **PATRÓN** `dist_vwap_pct` > `0.7727` → IC=+0.349 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7727 (IC base=-0.025)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.299 (n=883)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.0533` → IC=+0.319 (n=335)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0533 (IC base=+0.291)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2411` → IC=+0.301 (n=335)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2411 (IC base=+0.291)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2247` → IC=+0.303 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2247 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.306 (n=1053)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8382` → IC=+0.321 (n=1002)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8382 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.1552` → IC=+0.316 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1552 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.754` → IC=+0.372 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.754 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `12684.1483` → IC=+0.314 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12684.1483 (IC base=+0.291)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.310 (n=240)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.0574` → IC=+0.314 (n=181)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0574 (IC base=+0.288)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2571` → IC=+0.309 (n=181)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2571 (IC base=+0.288)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3977` → IC=+0.299 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3977 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.306 (n=545)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.288)

- **PATRÓN** `ibs_15` > `0.827` → IC=+0.313 (n=543)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.827 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` > `0.2546` → IC=+0.324 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2546 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.865` → IC=+0.379 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.865 (IC base=+0.288)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.287 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `16334.7136` → IC=+0.331 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16334.7136 (IC base=+0.288)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5749 sube el IC de +0.184 a +0.263 en UPDOWN_GBM#15min (n=3268). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7251 sube el IC de +0.220 a +0.284 en UPDOWN_GBM#BTC#15min (n=567). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5639 sube el IC de +0.144 a +0.247 en UPDOWN_GBM#ETH#15min (n=642). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.9048 sube el IC de +0.102 a +0.264 en UPDOWN_GBM#SOL#15min (n=223). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.561 sube el IC de +0.209 a +0.294 en UPDOWN_GBM#XRP#15min (n=757). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.066 a +0.164 en UPDOWN_GBM#XRP#15min (n=750). Ya aplicado como kelly_boost=+0.82€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6349 sube el IC de -0.065 a +0.284 en UPDOWN_GBM_15M_TARDIO (n=991). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3535 sube el IC de -0.012 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=3355). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7591 sube el IC de +0.099 a +0.335 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=313). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6128 sube el IC de -0.195 a +0.296 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=52). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6258 sube el IC de +0.153 a +0.259 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=496). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3685 sube el IC de +0.243 a +0.273 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1180). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.185 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.038 a +0.288 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=530). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.203 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3297 sube el IC de -0.025 a +0.295 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=814). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8382 sube el IC de +0.291 a +0.321 en UPDOWN_GBM_IBS_ALTO (n=1002). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.827 sube el IC de +0.288 a +0.313 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=543). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8516 sube el IC de +0.293 a +0.325 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=460). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.362 a +0.398 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=596). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8077 sube el IC de +0.364 a +0.389 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=314). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7479 sube el IC de +0.357 a +0.408 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=282). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1787 | +0.091 | +208.12€ | 0 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1787 | +0.091 | +208.12€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1410 | +0.096 | +181.87€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1410 | +0.096 | +181.87€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 274 | +0.065 | +10.54€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 274 | +0.065 | +10.54€ | 6 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 72 | +0.108 | +16.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 72 | +0.108 | +16.05€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 466 | -0.015 | +54.35€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 466 | -0.015 | +54.35€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 337 | -0.028 | +31.45€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 337 | -0.028 | +31.45€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 103 | +0.033 | +18.31€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 103 | +0.033 | +18.31€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 23 | -0.060 | +1.23€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 23 | -0.060 | +1.23€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 38026 | -0.082 | -4774.59€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2053 | +0.021 | -241.07€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 35973 | -0.088 | -4533.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4435 | -0.116 | -762.62€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4435 | -0.116 | -762.62€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2053 | +0.021 | -241.07€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2053 | +0.021 | -241.07€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4165 | -0.110 | -848.94€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4165 | -0.110 | -848.94€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 10116 | -0.012 | -895.11€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 10116 | -0.012 | -895.11€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 9875 | -0.105 | -751.77€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 9875 | -0.105 | -751.77€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 7382 | -0.138 | -1275.08€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 7382 | -0.138 | -1275.08€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 31838 | -0.017 | +3574.77€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 8241 | +0.004 | +1730.79€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 23597 | -0.024 | +1843.97€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 31838 | -0.017 | +3574.77€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 8241 | +0.004 | +1730.79€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 23597 | -0.024 | +1843.97€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 135094 | +0.114 | -5706.40€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 17831 | +0.182 | -537.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 588 | -0.027 | -67.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 108499 | +0.104 | -4841.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 8176 | +0.103 | -259.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 18002 | +0.107 | -1127.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 59 | -0.156 | +9.83€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 17928 | +0.108 | -1125.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 26351 | +0.128 | -411.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5093 | +0.191 | -155.19€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 17985 | +0.118 | -159.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3231 | +0.086 | -75.00€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 18053 | +0.096 | -1341.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 70 | -0.111 | -5.12€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 17968 | +0.098 | -1325.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 28724 | +0.123 | -550.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 7512 | +0.176 | -136.09€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 18213 | +0.106 | -351.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2987 | +0.101 | -54.65€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 25943 | +0.114 | -1355.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5033 | +0.194 | -256.44€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 491 | +0.007 | -13.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 18461 | +0.093 | -955.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1958 | +0.137 | -129.96€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 18021 | +0.103 | -919.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 64 | -0.076 | +5.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 17944 | +0.104 | -925.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 21695 | +0.195 | -1357.01€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 21695 | +0.195 | -1357.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4968 | +0.176 | -445.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4968 | +0.176 | -445.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 2626 | +0.201 | -60.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 2626 | +0.201 | -60.67€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 4908 | +0.179 | -403.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 4908 | +0.179 | -403.03€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4275 | +0.246 | -141.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4275 | +0.246 | -141.81€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4839 | +0.187 | -319.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4839 | +0.187 | -319.71€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 75604 | +0.201 | -5479.20€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 75604 | +0.201 | -5479.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 12994 | +0.185 | -1342.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 12994 | +0.185 | -1342.45€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 12202 | +0.224 | -426.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 12202 | +0.224 | -426.64€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 12958 | +0.180 | -1390.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 12958 | +0.180 | -1390.73€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 12276 | +0.220 | -471.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 12276 | +0.220 | -471.30€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 12526 | +0.202 | -823.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 12526 | +0.202 | -823.48€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 12648 | +0.196 | -1024.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 12648 | +0.196 | -1024.60€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 28921 | +0.117 | +207.32€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 28921 | +0.117 | +207.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 14377 | +0.120 | +178.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 14377 | +0.120 | +178.29€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 14544 | +0.114 | +29.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 14544 | +0.114 | +29.03€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1523 | +0.069 | -67.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 582 | +0.055 | -45.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 941 | +0.078 | -21.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 72 | +0.108 | +2.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 72 | +0.108 | +2.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1173 | +0.075 | -33.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 232 | +0.064 | -11.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 941 | +0.078 | -21.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 278 | +0.032 | -37.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 278 | +0.032 | -37.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 56596 | +0.100 | -1422.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 4578 | +0.093 | +64.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 52018 | +0.101 | -1486.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 31220 | +0.105 | -339.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 4578 | +0.093 | +64.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 26642 | +0.107 | -404.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 11509 | +0.109 | -39.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 11509 | +0.109 | -39.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 13867 | +0.081 | -1043.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 13867 | +0.081 | -1043.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 892 | +0.192 | -113.16€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 892 | +0.192 | -113.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 892 | +0.192 | -113.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 892 | +0.192 | -113.16€ | 2 | 4 |
| ✅ GBM_LATE_15M | 39130 | +0.092 | +20032.45€ | 0 | 17 |
| ✅ GBM_LATE_15M#15min | 39130 | +0.092 | +20032.45€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 6553 | +0.210 | +5228.76€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 6553 | +0.210 | +5228.76€ | 0 | 24 |
| ✅ GBM_LATE_15M#BTC | 5869 | +0.178 | +4372.56€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 5869 | +0.178 | +4372.56€ | 0 | 26 |
| ✅ GBM_LATE_15M#DOGE | 6977 | +0.203 | +5373.27€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 6977 | +0.203 | +5373.27€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 5484 | +0.040 | +1483.77€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 5484 | +0.040 | +1483.77€ | 1 | 17 |
| ✅ GBM_LATE_15M#SOL | 5539 | -0.031 | +1191.90€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 5539 | -0.031 | +1191.90€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 8708 | -0.033 | +2382.18€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 8708 | -0.033 | +2382.18€ | 3 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 42283 | +0.086 | +22872.83€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 42283 | +0.086 | +22872.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 8181 | +0.005 | +4212.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 8181 | +0.005 | +4212.36€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 8894 | +0.013 | +2041.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 8894 | +0.013 | +2041.33€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 5902 | +0.274 | +6242.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 5902 | +0.274 | +6242.43€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 7457 | +0.013 | +1797.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 7457 | +0.013 | +1797.27€ | 1 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 6800 | +0.039 | +2774.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 6800 | +0.039 | +2774.16€ | 3 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5049 | +0.297 | +5805.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5049 | +0.297 | +5805.28€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 31080 | +0.178 | +24839.96€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 31080 | +0.178 | +24839.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 4716 | +0.223 | +4068.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 4716 | +0.223 | +4068.97€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 4893 | +0.150 | +3592.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 4893 | +0.150 | +3592.04€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 4966 | +0.222 | +4241.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 4966 | +0.222 | +4241.08€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 5246 | +0.139 | +3978.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 5246 | +0.139 | +3978.85€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 5844 | +0.123 | +4282.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 5844 | +0.123 | +4282.12€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 5415 | +0.223 | +4676.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 5415 | +0.223 | +4676.90€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 8360 | +0.136 | +4087.56€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 8360 | +0.136 | +4087.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2510 | +0.144 | +1431.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2510 | +0.144 | +1431.07€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 418 | +0.148 | +207.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 418 | +0.148 | +207.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2494 | +0.143 | +1183.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2494 | +0.143 | +1183.76€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1993 | +0.111 | +774.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1993 | +0.111 | +774.15€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 540 | +0.133 | +238.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 540 | +0.133 | +238.31€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO | 39328 | +0.183 | +31013.29€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#15min | 39328 | +0.183 | +31013.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 6247 | +0.236 | +5679.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 6247 | +0.236 | +5679.85€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 6118 | +0.147 | +4121.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 6118 | +0.147 | +4121.95€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 6627 | +0.231 | +5868.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 6627 | +0.231 | +5868.68€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 6460 | +0.138 | +4581.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 6460 | +0.138 | +4581.29€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 6954 | +0.122 | +4745.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 6954 | +0.122 | +4745.47€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 6922 | +0.226 | +6016.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 6922 | +0.226 | +6016.04€ | 0 | 21 |
| ✅ GBM_LATE_5M | 10854 | +0.194 | +8059.08€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 10854 | +0.194 | +8059.08€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 919 | +0.232 | +813.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 919 | +0.232 | +813.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2450 | +0.189 | +1930.32€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2450 | +0.189 | +1930.32€ | 0 | 28 |
| ✅ GBM_LATE_5M#DOGE | 1011 | +0.177 | +667.91€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1011 | +0.177 | +667.91€ | 0 | 17 |
| ✅ GBM_LATE_5M#ETH | 3221 | +0.191 | +2244.49€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3221 | +0.191 | +2244.49€ | 0 | 25 |
| ✅ GBM_LATE_5M#SOL | 1603 | +0.190 | +1207.30€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1603 | +0.190 | +1207.30€ | 0 | 28 |
| ✅ GBM_LATE_5M#XRP | 1650 | +0.196 | +1195.07€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1650 | +0.196 | +1195.07€ | 0 | 0 |
| ✅ GBM_LATE_60M | 3106 | +0.070 | +1069.47€ | 0 | 9 |
| ✅ GBM_LATE_60M#60min | 3106 | +0.070 | +1069.47€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1156 | +0.087 | +437.16€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1156 | +0.087 | +437.16€ | 0 | 9 |
| ✅ GBM_LATE_60M#ETH | 995 | +0.074 | +386.45€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 995 | +0.074 | +386.45€ | 0 | 10 |
| ✅ GBM_LATE_60M#SOL | 955 | +0.044 | +245.87€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 955 | +0.044 | +245.87€ | 1 | 12 |
| 🚫 GBM_LATE_60M_FADE | 533 | -0.246 | -22.94€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 533 | -0.246 | -22.94€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 201 | -0.239 | -10.94€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 201 | -0.239 | -10.94€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 190 | -0.229 | -4.06€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 190 | -0.229 | -4.06€ | 6 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 142 | -0.271 | -7.94€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 142 | -0.271 | -7.94€ | 4 | 0 |
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
| ✅ LEADLAG_BTC_XRP_15M | 3219 | +0.100 | +796.91€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3219 | +0.100 | +796.91€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3219 | +0.100 | +796.91€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3219 | +0.100 | +796.91€ | 0 | 1 |
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
| ✅ LIQUIDACIONES_5M | 3510 | +0.016 | +78.28€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3510 | +0.016 | +78.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 171 | +0.015 | -3.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 171 | +0.015 | -3.81€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 692 | +0.017 | +36.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 692 | +0.017 | +36.31€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1264 | +0.025 | +29.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1264 | +0.025 | +29.19€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 749 | +0.011 | +1.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 749 | +0.011 | +1.36€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 431 | +0.010 | +20.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 431 | +0.010 | +20.32€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1651 | -0.042 | -29.63€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1651 | -0.042 | -29.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 468 | -0.036 | -13.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 468 | -0.036 | -13.36€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 558 | -0.016 | +5.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 558 | -0.016 | +5.32€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 625 | -0.069 | -21.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 625 | -0.069 | -21.59€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 7354 | -0.026 | +4.29€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 3489 | -0.038 | -97.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 3865 | -0.015 | +101.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 209 | -0.012 | +7.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 105 | +0.014 | +8.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 104 | -0.038 | -1.64€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 1849 | -0.019 | +13.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 880 | -0.025 | -6.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 969 | -0.014 | +20.23€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 806 | -0.020 | +16.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 404 | -0.042 | -10.53€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 402 | +0.003 | +26.54€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 1568 | -0.044 | -67.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 730 | -0.063 | -68.88€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 838 | -0.027 | +1.57€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1439 | -0.017 | +30.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 688 | -0.033 | -7.95€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 751 | -0.002 | +38.83€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1483 | -0.030 | +4.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 682 | -0.040 | -11.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 801 | -0.022 | +15.96€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 45720 | -0.001 | +2287.17€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 45720 | -0.001 | +2287.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 8214 | +0.025 | +1049.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 8214 | +0.025 | +1049.31€ | 2 | 4 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 6656 | -0.034 | -93.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 6656 | -0.034 | -93.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 8332 | +0.023 | +841.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 8332 | +0.023 | +841.63€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 6490 | -0.047 | -135.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 6490 | -0.047 | -135.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 7714 | -0.004 | +237.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 7714 | -0.004 | +237.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 8314 | +0.015 | +387.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 8314 | +0.015 | +387.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6458 | -0.060 | -160.52€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6458 | -0.060 | -160.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1649 | -0.080 | -43.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1649 | -0.080 | -43.08€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 53 | -0.064 | -2.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 53 | -0.064 | -2.93€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 755 | -0.120 | -31.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 755 | -0.120 | -31.95€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1920 | -0.078 | -42.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1920 | -0.078 | -42.26€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 856 | -0.015 | -25.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 856 | -0.015 | -25.00€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3367 | +0.004 | -1.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3367 | +0.004 | -1.04€ | 0 | 0 |
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
| ✅ MOMENTUM_IBS_5M#XRP | 190 | -0.010 | -6.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 190 | -0.010 | -6.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 113903 | -0.075 | +1841.70€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 113903 | -0.075 | +1841.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 19731 | -0.075 | +1052.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 19731 | -0.075 | +1052.61€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 17190 | -0.099 | -945.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 17190 | -0.099 | -945.68€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 20011 | -0.066 | +1152.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 20011 | -0.066 | +1152.07€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 16728 | -0.096 | -522.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 16728 | -0.096 | -522.68€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 20491 | -0.055 | +355.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 20491 | -0.055 | +355.60€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 19752 | -0.065 | +749.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 19752 | -0.065 | +749.77€ | 4 | 0 |
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
| ✅ ORDER_FLOW_5M | 1572 | +0.124 | +644.01€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 1436 | +0.130 | +631.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 335 | +0.150 | +185.05€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 335 | +0.150 | +185.05€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 296 | +0.121 | +105.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 296 | +0.121 | +105.68€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#ETH | 290 | +0.130 | +133.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 290 | +0.130 | +133.02€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 253 | +0.151 | +138.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 253 | +0.151 | +138.41€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 262 | +0.091 | +69.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 262 | +0.091 | +69.26€ | 0 | 1 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1266 | -0.017 | -18.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1266 | -0.017 | -18.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 241 | -0.010 | +3.92€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 241 | -0.010 | +3.92€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 221 | -0.002 | +5.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 221 | -0.002 | +5.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 334 | -0.039 | -21.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 334 | -0.039 | -21.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 265 | -0.002 | -1.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 265 | -0.002 | -1.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 205 | -0.027 | -5.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 205 | -0.027 | -5.17€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 848 | -0.068 | -39.09€ | 3 | 1 |
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
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 361 | -0.211 | -38.46€ | 3 | 0 |
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
| ✅ STREAK_FADE_15M | 695 | +0.029 | +30.87€ | 3 | 2 |
| ✅ STREAK_FADE_15M#15min | 695 | +0.029 | +30.87€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 300 | +0.023 | +3.36€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 300 | +0.023 | +3.36€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 56 | -0.017 | -4.00€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 56 | -0.017 | -4.00€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 71 | -0.007 | -0.09€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 71 | -0.007 | -0.09€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 268 | +0.056 | +31.59€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 268 | +0.056 | +31.59€ | 0 | 6 |
| ✅ STREAK_FADE_5M | 3401 | -0.021 | -132.03€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3401 | -0.021 | -132.03€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1051 | -0.022 | -37.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1051 | -0.022 | -37.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 588 | -0.027 | -26.12€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 588 | -0.027 | -26.12€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 162 | -0.043 | -14.36€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 162 | -0.043 | -14.36€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1600 | -0.016 | -54.04€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1600 | -0.016 | -54.04€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 95 | -0.046 | -8.93€ | 4 | 0 |
| ✅ STREAK_FADE_60M#60min | 95 | -0.046 | -8.93€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 40 | -0.071 | -3.54€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 40 | -0.071 | -3.54€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 55 | -0.026 | -5.39€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 55 | -0.026 | -5.39€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 10428 | +0.017 | +96.63€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 10428 | +0.017 | +96.63€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2669 | +0.019 | +22.63€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2669 | +0.019 | +22.63€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2671 | +0.021 | +40.65€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2671 | +0.021 | +40.65€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2884 | +0.009 | -2.06€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2884 | +0.009 | -2.06€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2204 | +0.022 | +35.40€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2204 | +0.022 | +35.40€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 9519 | +0.013 | -48.55€ | 1 | 0 |
| ✅ STRUCT_NO_15M#15min | 9519 | +0.013 | -48.55€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3811 | +0.017 | -8.79€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3811 | +0.017 | -8.79€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3606 | +0.011 | -28.71€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3606 | +0.011 | -28.71€ | 1 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2102 | +0.010 | -11.05€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2102 | +0.010 | -11.05€ | 1 | 0 |
| ✅ UPDOWN_GBM | 70902 | +0.052 | +6174.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 17771 | +0.084 | +3966.16€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2320 | +0.006 | +21.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 46454 | +0.047 | +2105.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 4115 | +0.009 | +82.32€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6818 | +0.089 | +1072.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1543 | +0.158 | +694.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5198 | +0.070 | +378.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 14624 | +0.054 | +1241.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2241 | +0.091 | +550.82€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 605 | +0.012 | +11.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 9859 | +0.059 | +617.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1831 | +0.006 | +58.07€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 88 | -0.067 | +3.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8107 | +0.066 | +846.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1529 | +0.149 | +607.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6500 | +0.047 | +240.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 15866 | +0.043 | +999.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 4130 | +0.064 | +592.30€ | 0 | 12 |
| ✅ UPDOWN_GBM#ETH#240min | 595 | +0.007 | +12.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 9646 | +0.042 | +378.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1415 | +0.011 | +14.76€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 80 | -0.110 | +1.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 15620 | +0.030 | +692.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 4345 | +0.034 | +355.96€ | 0 | 4 |
| ✅ UPDOWN_GBM#SOL#240min | 577 | -0.004 | +0.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 9757 | +0.033 | +331.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 869 | +0.010 | +9.49€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 72 | -0.135 | -4.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 9865 | +0.061 | +1324.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3983 | +0.102 | +1165.04€ | 0 | 9 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 5494 | +0.035 | +159.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 240 | -0.103 | +0.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 794 | +0.362 | +282.50€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 794 | +0.362 | +282.50€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 418 | +0.364 | +146.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 418 | +0.364 | +146.27€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 376 | +0.357 | +136.23€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 376 | +0.357 | +136.23€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 18806 | -0.024 | +4537.51€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 18806 | -0.024 | +4537.51€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1674 | -0.056 | +500.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1674 | -0.056 | +500.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3256 | -0.111 | +145.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3256 | -0.111 | +145.65€ | 5 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 926 | +0.220 | +767.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 926 | +0.220 | +767.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2234 | +0.216 | +1453.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2234 | +0.216 | +1453.67€ | 1 | 23 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5360 | -0.064 | +698.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5360 | -0.064 | +698.24€ | 5 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5356 | -0.064 | +971.49€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5356 | -0.064 | +971.49€ | 3 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 211 | +0.035 | +5.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 211 | +0.035 | +5.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 211 | +0.035 | +5.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 211 | +0.035 | +5.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1336 | +0.291 | +1127.19€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1336 | +0.291 | +1127.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 723 | +0.288 | +575.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 723 | +0.288 | +575.11€ | 0 | 10 |
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
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.045) — sin ventaja clara. oversold(IBS<0.3): IC=+0.063 n=24731 | neutral: IC=+0.054 n=26098 | overbought(IBS>0.7): IC=+0.099 n=25148
  - _Datos_: n=78972 IC=+0.073 PNL=+11706.14€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 685 celda(s) pasan gate riguroso completo de 2625 evaluadas (n>=40) y 3654 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.034 < 0.08 — monitorear
  - _Datos_: n=4345 IC=+0.034 PNL=+355.96€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1293/15 IC=+0.298 PNL=+580.12€ | BTC: n=1226/15 IC=+0.257 PNL=+166.14€ | SOL: n=849/15 IC=+0.379 PNL=+880.99€

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
  - _Estado_: 70840 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.135 n=744/60 | contraria IC=+0.194 n=770 | gap=-0.059 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=435, boost estimado=+0.013. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 253 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1415/40 IC=+0.011 PNL=+14.76€ | BTC#60min: n=1831/40 IC=+0.006 PNL=+58.07€ | SOL#60min: n=869/40 IC=+0.010 PNL=+9.49€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.048 n=515276 | tras_1loss IC=+0.093 n=392906 | tras_2loss IC=+0.063 n=159686/40 | gap=-0.015 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.034 n=9692 | contrario_BTC IC=+0.051 n=8472/40 | gap=+0.017 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.203 > 0.08 con n=676 PNL=+511.32€
  - _Datos_: n=676 IC=+0.203 PNL=+511.32€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.179 > 0.08 con n=761 PNL=+459.88€
  - _Datos_: n=761 IC=+0.179 PNL=+459.88€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.189 > 0.08 con n=59 PNL=+35.04€
  - _Datos_: n=59 IC=+0.189 PNL=+35.04€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.333 > 0.1 con n=2747 PNL=+1538.36€
  - _Datos_: n=2747 IC=+0.333 PNL=+1538.36€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=603 IC=+0.077 PNL=+70.30€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=603 IC=+0.077 PNL=+70.30€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=77 IC=+0.183 PNL=+51.33€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=77 IC=+0.183 PNL=+51.33€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=66960 IC=+0.051 PNL=+5889.51€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=66960 IC=+0.051 PNL=+5889.51€

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
  - _Estado_: 1/20 ops en el filtro definido (IC actual=+0.008 PNL=+1.96€)
  - _Datos_: n=1 IC=+0.008 PNL=+1.96€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: 07h sigue en ORDER_FLOW_BLACKLIST_HOURS -- mientras siga ahí, nunca genera fila para volver a evaluarse (26-Ago, triage candidatas estancadas)

**〰️ H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: n=2770 IC=+0.006 PNL=-1.18€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2770 IC=+0.006 PNL=-1.18€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1345 IC=+0.015 PNL=+83.50€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1345 IC=+0.015 PNL=+83.50€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=874 IC=+0.013 PNL=+28.47€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=874 IC=+0.013 PNL=+28.47€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.184 > 0.1 con n=4357 PNL=+2830.94€
  - _Datos_: n=4357 IC=+0.184 PNL=+2830.94€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=2888 IC=+0.068 PNL=+215.71€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2888 IC=+0.068 PNL=+215.71€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=2241 IC=+0.091 PNL=+550.82€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=2241 IC=+0.091 PNL=+550.82€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 0/50 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: confirmada 2026-07-01 (IC=-0.037 n=52) e implementada en shadow_predict.py (skip si drift_15min∈[-0.3,0.3)) -- verificado 26-Ago con 2177 filas post-TWAP reales, 0 caen en la zona filtrada. Frozen by design, no falta n

**🟡 H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.100 > 0.08 con n=10168 PNL=+2930.91€
  - _Datos_: n=10168 IC=+0.100 PNL=+2930.91€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=282 IC=-0.225 PNL=+3.45€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=282 IC=-0.225 PNL=+3.45€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=399 IC=-0.019 PNL=-7.91€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=399 IC=-0.019 PNL=-7.91€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=916 IC=+0.037 PNL=+89.25€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=916 IC=+0.037 PNL=+89.25€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=108 IC=+0.027 PNL=+3.08€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=108 IC=+0.027 PNL=+3.08€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=7797 IC=+0.018 PNL=+173.40€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=7797 IC=+0.018 PNL=+173.40€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.115 > 0.08 con n=336 PNL=+72.98€
  - _Datos_: n=336 IC=+0.115 PNL=+72.98€

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.262 n=149) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=149 IC=+0.262 PNL=+134.77€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=11867 IC=+0.051 PNL=+1028.09€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=11867 IC=+0.051 PNL=+1028.09€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=4159 IC=+0.065 PNL=+601.81€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4159 IC=+0.065 PNL=+601.81€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.112 > 0.08 con n=516 PNL=+169.86€
  - _Datos_: n=516 IC=+0.112 PNL=+169.86€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.152 > 0.08 con n=1039 PNL=+291.81€
  - _Datos_: n=1039 IC=+0.152 PNL=+291.81€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.113 > 0.08 con n=807 PNL=+431.75€
  - _Datos_: n=807 IC=+0.113 PNL=+431.75€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=64364 IC=+0.118 PNL=+23936.47€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=64364 IC=+0.118 PNL=+23936.47€

**〰️ H-CUSTOM-MERCURY-RETROGRADO** — Mercurio retrógrado: ¿rendimiento peor durante la ventana?
  - _Hipótesis_: Mismo origen que H-CUSTOM-MOON-LLENA (paper de Fornero, 43 Jornadas SADAF 2023). Qi, Wang & Zhang (2022, 48 mercados, 1973-2019): rendimientos 3.33%/año más bajos durante Mercurio retrógrado. Kou & Ma (2022) en China (99.8% cuentas retail): hasta -31% anualizado. Ambos estudios confirman que el mecanismo es la creencia/superstición de inversores retail (mayor efecto cuanto más retail y más supersticioso el mercado), no un efecto astral literal — Polymarket encaja en ese perfil. Ventanas 2026 (fuente pública, actualizar cada año): 26-feb a 20-mar, 29-jun a 23-jul, 24-oct a 13-nov.
  - _Umbral_: n≥100 PERO ADEMÁS necesita cubrir al menos 2-3 ventanas de retrogradación distintas (no solo la de jun-jul 2026) — esperar mínimo hasta después de la ventana de oct-nov 2026
  - _Acción_: Si IC en mercury_retrogrado=1 < IC en mercury_retrogrado=0 con margen ≥0.05 y ≥2 ventanas distintas cubiertas → considerar boost/filtro. No implementar tras una sola ventana (jun-jul 2026) por more que n sea alto — sería solo un evento, no un patrón.
  - _Estado_: n=1792 IC=+0.109 PNL=+195.82€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=1792 IC=+0.109 PNL=+195.82€

**〰️ H-CUSTOM-SMART-MONEY-CONSENSUS** — Consenso de wallets 'smart money' — ¿confirma nuestra dirección?
  - _Hipótesis_: Javi propuso estudiar bots/wallets que operan bien en nuestros mismos mercados. En vez de creer artículos (ya verificamos 2 veces esta semana que las narrativas no aguantan el cruce con datos reales), smart_money_tracker.py mide el track record REAL de wallets activas en BTC/ETH/SOL/XRP Up-or-Down 5/15/60min vía data-api.polymarket.com/positions, filtrado a posiciones 'Up or Down'. Clasifica como 'smart' las wallets con n>=10 posiciones, win_rate>=0.55 y pnl_total>0. smart_money_consensus es el sesgo direccional reciente (Up-Down)/(Up+Down) de esas wallets 'smart' por activo. Hipótesis: si nuestra decisión (BUY_YES/BUY_NO) coincide con el consenso smart money, mejor IC que cuando diverge. RESET METODOLOGICO 2026-07-02: la clasificacion 'smart' original via /positions estaba INVERTIDA para wallets de alta frecuencia (el endpoint solo retiene el residuo perdedor sin redimir; verificado: 'wowitsamazing' figuraba como -$478k y es +$10k/mes en el leaderboard oficial). Desde 2026-07-02T06:12Z el consenso se construye solo con wallets verificadas en el leaderboard oficial (pnl_mes>=$1000, 24 wallets). Los valores de smart_money_consensus capturados en features ANTES de esa fecha provienen de la clasificacion rota — descontar ese tramo al evaluar.
  - _Umbral_: n≥40 y IC>+0.08 — además necesita que existan wallets 'smart' acumuladas (0 al empezar, se van descubriendo cada ciclo)
  - _Acción_: Si IC en confluencia (decisión coincide con signo de smart_money_consensus) supera en >=0.05 al IC en divergencia, con n≥40 en cada lado → boost ×1.1-1.2 cuando coincide, considerar reducir stake cuando diverge fuerte.
  - _Estado_: n=10666 IC=+0.055 PNL=+1042.43€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=10666 IC=+0.055 PNL=+1042.43€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.129 > 0.02 con n=906 PNL=+391.14€
  - _Datos_: n=906 IC=+0.129 PNL=+391.14€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=202 IC=-0.083 PNL=+23.24€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=202 IC=-0.083 PNL=+23.24€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.448 > 0.1 con n=1545 PNL=+1503.55€
  - _Datos_: n=1545 IC=+0.448 PNL=+1503.55€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=27403 IC=+0.073 PNL=+3987.07€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=27403 IC=+0.073 PNL=+3987.07€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.213 > 0.1 con n=6335 PNL=+3856.84€
  - _Datos_: n=6335 IC=+0.213 PNL=+3856.84€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.135 < -0.1 con n=431 PNL=+55.32€
  - _Datos_: n=431 IC=-0.135 PNL=+55.32€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2974 IC=+0.066 PNL=+367.38€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2974 IC=+0.066 PNL=+367.38€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=128 IC=-0.100 PNL=+4.60€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=128 IC=-0.100 PNL=+4.60€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.116 > 0.1 con n=722 PNL=+196.08€
  - _Datos_: n=722 IC=+0.116 PNL=+196.08€

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
  - _Estado_: n=29248 IC=-0.134 PNL=+2325.39€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=29248 IC=-0.134 PNL=+2325.39€

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
  - _Estado_: n=2955 IC=+0.135 PNL=+1788.01€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2955 IC=+0.135 PNL=+1788.01€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.208 > 0.08 con n=3846 PNL=+2847.62€
  - _Datos_: n=3846 IC=+0.208 PNL=+2847.62€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=7299 IC=+0.048 PNL=+572.34€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=7299 IC=+0.048 PNL=+572.34€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.090 > 0.08 con n=3206 PNL=+1687.68€
  - _Datos_: n=3206 IC=+0.090 PNL=+1687.68€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.220 > 0.08 con n=754 PNL=+444.43€
  - _Datos_: n=754 IC=+0.220 PNL=+444.43€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.224 < -0.1 con n=3002 PNL=-234.80€
  - _Datos_: n=3002 IC=-0.224 PNL=-234.80€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=8054 IC=+0.200 PNL=+6075.68€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=8054 IC=+0.200 PNL=+6075.68€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.121 > 0.08 con n=114 PNL=+50.17€
  - _Datos_: n=114 IC=+0.121 PNL=+50.17€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=2948 IC=+0.079 PNL=+989.30€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2948 IC=+0.079 PNL=+989.30€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.175 > 0.08 con n=2717 PNL=+1979.47€
  - _Datos_: n=2717 IC=+0.175 PNL=+1979.47€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=4565 IC=-0.029 PNL=+1246.74€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4565 IC=-0.029 PNL=+1246.74€

**〰️ H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: n=658 IC=+0.077 PNL=-46.84€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=658 IC=+0.077 PNL=-46.84€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.240 > 0.08 con n=4500 PNL=-377.50€
  - _Datos_: n=4500 IC=+0.240 PNL=-377.50€

**〰️ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: n>=40 y IC>0.08
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: n=63 IC=-0.008 PNL=+4.40€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=63 IC=-0.008 PNL=+4.40€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.099 n=1632) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1632 IC=+0.099 PNL=+351.76€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.321 > 0.08 con n=416 PNL=+127.60€
  - _Datos_: n=416 IC=+0.321 PNL=+127.60€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.414 n=544) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=544 IC=+0.414 PNL=+784.74€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=12994 IC=+0.185 PNL=-1342.45€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=12994 IC=+0.185 PNL=-1342.45€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.212 > 0.1 con n=213 PNL=+134.68€
  - _Datos_: n=213 IC=+0.212 PNL=+134.68€
