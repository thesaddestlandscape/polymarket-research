# Hipótesis automáticas — 2026-10-06 03:03 UTC
_Generado por shadow_postmortem.py sobre 769314 resoluciones (PNL=+93789.29€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=575)

- **PATRÓN** `py_entrada` > `0.51` → IC=+0.239 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.51 (IC base=+0.130)

- **PATRÓN** `n_total_lado` > `70.0` → IC=+0.209 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 70.0 (IC base=+0.130)

- **PATRÓN** `banda_hit_calibrado` > `0.7972` → IC=+0.262 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7972 (IC base=+0.130)

- **PATRÓN** `banda_z` > `9.249` → IC=+0.184 (n=213)

  - _Acción_: Kelly boost +0.92€ cuando `banda_z` > 9.249 (IC base=+0.130)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.71` → IC=+0.130 (n=568)

  - _Acción_: Kelly boost +0.65€ cuando `ballenas_wallet_edge_medio` > 0.71 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.158 (n=220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=675)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `3090.2364` → IC=+0.133 (n=426)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 3090.2364 (IC base=+0.130)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=438)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.220 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.136)

- **PATRÓN** `n_total_lado` > `66.0` → IC=+0.194 (n=233)

  - _Acción_: Kelly boost +0.97€ cuando `n_total_lado` > 66.0 (IC base=+0.136)

- **PATRÓN** `banda_hit_calibrado` > `0.6176` → IC=+0.252 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6176 (IC base=+0.136)

- **PATRÓN** `banda_z` > `9.958` → IC=+0.198 (n=170)

  - _Acción_: Kelly boost +0.99€ cuando `banda_z` > 9.958 (IC base=+0.136)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.903` → IC=+0.138 (n=415)

  - _Acción_: Kelly boost +0.69€ cuando `ballenas_wallet_edge_medio` > 0.903 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.174 (n=170)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=577)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.136)

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

- **FILTRO** `py_entrada` > `0.5` → IC=-0.371 (n=29)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=94)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.177 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=94)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=107)

- **PATRÓN** `py_entrada` > `0.705` → IC=+0.255 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.705 (IC base=+0.125)

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

- **PATRÓN** `libro_liquidez` > `1207.4096` → IC=+0.185 (n=71)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1207.4096 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.125 (n=94)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.5 (IC base=+0.004)

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
- **FILTRO** `restante_s_al_confirmar` < `143.77` → IC=-0.215 (n=8476)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 143.77
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=25430)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `130.91` → IC=-0.270 (n=1087)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.91
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=3261)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `124.35` → IC=-0.304 (n=990)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 124.35
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=2972)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `165.07` → IC=-0.222 (n=2129)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 165.07
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=6387)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `128.65` → IC=-0.310 (n=1643)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.65
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=4931)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.213 (n=16302)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.104)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=3898)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `5357.1858` → IC=+0.170 (n=2536)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 5357.1858 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.136 (n=14510)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.134 (n=17611)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.229 (n=13481)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.164 (n=6403)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7626.6933` → IC=+0.167 (n=2454)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 7626.6933 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.206 (n=1899)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.200 (n=1852)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.348 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=2331)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `16056.3738` → IC=+0.212 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16056.3738 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.199 (n=1677)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=1858)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.196 (n=2386)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `16023.7287` → IC=+0.210 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16023.7287 (IC base=+0.194)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.555` → IC=+0.124 (n=1041)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.555 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `4587.7919` → IC=+0.123 (n=250)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 4587.7919 (IC base=+0.093)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=437)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.088)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.133 (n=948)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.44 (IC base=+0.088)

- **PATRÓN** `libro_liquidez` > `5754.4405` → IC=+0.144 (n=234)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 5754.4405 (IC base=+0.088)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=3430)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.355 (n=1138)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.233 (n=1537)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` < `0.235` → IC=+0.363 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.235 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.228 (n=1780)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.223)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=852)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.144 (n=731)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.137)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.254 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=664)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2151.7929` → IC=+0.153 (n=370)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2151.7929 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.074)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.238 (n=825)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.215)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.408 (n=992)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.156 (n=59)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.151 (n=1229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.155 (n=654)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.148)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.291 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=810)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.148)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.182 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 7.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.372 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.156 (n=193)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.149 (n=368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.117)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.220 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.117)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.284 (n=132)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=68)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=14488)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.200 (n=13797)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.229 (n=6174)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.178 (n=3223)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 6.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.177 (n=3224)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.179 (n=3279)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.73 (IC base=+0.174)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **FILTRO** `py_entrada` < `0.775` → IC=-0.284 (n=49)

  - _Acción_: SKIP cuando `py_entrada` < 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=63)

- **FILTRO** `libro_liquidez` < `9614.35` → IC=-0.328 (n=56)

  - _Acción_: SKIP cuando `libro_liquidez` < 9614.35
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.238 (n=1424)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.233 (n=1411)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.232)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.335 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.232)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.189 (n=3180)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 6.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.186 (n=3199)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.188 (n=2675)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.253 (n=2944)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.242)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.332 (n=1018)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.242)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=3278)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=2804)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.191 (n=2477)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.71 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.198 (n=1183)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.73 (IC base=+0.189)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.433 (n=597)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.428)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.427 (n=685)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.428)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=686)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.428)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.428)

- **PATRÓN** `libro_liquidez` > `2748.7904` → IC=+0.435 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2748.7904 (IC base=+0.428)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.432 (n=262)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.433)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.443 (n=174)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.433)

- **PATRÓN** `libro_liquidez` > `19769.7921` → IC=+0.443 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 19769.7921 (IC base=+0.433)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.444 (n=246)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.433)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.433)

- **PATRÓN** `libro_liquidez` > `3371.5411` → IC=+0.446 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3371.5411 (IC base=+0.433)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.408 (n=128)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.404)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.406 (n=126)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.404)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.408 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.404)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.419 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.404)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=24)

- **FILTRO** `libro_liquidez` < `7880.4556` → IC=-0.344 (n=30)

  - _Acción_: SKIP cuando `libro_liquidez` < 7880.4556
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.203 (n=43235)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.243 (n=18982)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.185 (n=7447)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.185 (n=5948)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.198 (n=8196)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.71 (IC base=+0.183)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=3889)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.269 (n=4409)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.180 (n=7859)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 7.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.192 (n=7858)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.235 (n=3913)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.274 (n=2662)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.207 (n=7169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.204 (n=5713)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.261 (n=2837)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.201 (n=3104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.244 (n=3292)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.194)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=6633)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` < `4.19` → IC=+0.125 (n=6143)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.19 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=6425)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.46` → IC=+0.137 (n=6122)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.46 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=3315)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` < `4.16` → IC=+0.128 (n=3044)

  - _Acción_: Kelly boost +0.64€ cuando `restante_min` < 4.16 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.142 (n=3212)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.135 (n=4025)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `3.14` → IC=+0.146 (n=3041)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 3.14 (IC base=+0.120)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.188 (n=3318)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.113)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.130 (n=3518)

  - _Acción_: Kelly boost +0.65€ cuando `restante_min` > 4.96 (IC base=+0.113)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.134 (n=3103)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 2.25 (IC base=+0.113)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.314 (n=938)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.292 (n=1375)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.289)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.379 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `4193.5606` → IC=+0.302 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4193.5606 (IC base=+0.289)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.292 (n=622)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.336 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `3797.228` → IC=+0.289 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3797.228 (IC base=+0.279)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.320 (n=448)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.296 (n=659)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.289)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.388 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `1436.9616` → IC=+0.306 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1436.9616 (IC base=+0.289)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.355 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.349)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.367 (n=81)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.349)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.390 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.349)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.353 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.349)

- **PATRÓN** `libro_liquidez` > `761.0655` → IC=+0.377 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 761.0655 (IC base=+0.349)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.443 (n=589)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.440 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.440 (n=698)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.439)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.441 (n=254)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.438 (n=287)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.438 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.445 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.436)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.459 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.442)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.442 (n=101)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.451 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.443 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.444 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.442)

- **PATRÓN** `libro_liquidez` > `2138.537` → IC=+0.457 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2138.537 (IC base=+0.442)

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
- **FILTRO** `hora_utc` < `5.0` → IC=-0.273 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=74)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=74)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.237 (n=55)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=39)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.308 (n=222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.297 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.276 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `983.8593` → IC=+0.277 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 983.8593 (IC base=+0.259)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **FILTRO** `hora_utc` < `5.0` → IC=-0.273 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=74)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=74)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.237 (n=55)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=39)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.308 (n=222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.297 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.276 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `983.8593` → IC=+0.277 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 983.8593 (IC base=+0.259)

### GBM_LATE_15M
- **PATRÓN** `drift_60min` |x|≤ `0.4845` → IC=+0.130 (n=10349)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.4845 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.9838` → IC=+0.243 (n=3450)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9838 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.3754` → IC=+0.253 (n=2698)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3754 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.034` → IC=+0.183 (n=3921)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 6.034 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.2099` → IC=+0.250 (n=2893)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2099 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` > `0.616` → IC=+0.255 (n=2893)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.616 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.3031` → IC=+0.225 (n=1050)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3031 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `2.332` → IC=+0.218 (n=3283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.332 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.5652` → IC=+0.140 (n=12582)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.5652 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` > `0.5754` → IC=+0.202 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5754 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` < `0.1467` → IC=+0.181 (n=4221)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.1467 (IC base=+0.071)

- **PATRÓN** `volumen_regimen` < `1.1976` → IC=+0.180 (n=4620)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 1.1976 (IC base=+0.071)

- **PATRÓN** `volumen_regimen` > `0.6249` → IC=+0.179 (n=4621)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 0.6249 (IC base=+0.071)

- **PATRÓN** `volumen_pendiente_norm` > `0.2954` → IC=+0.227 (n=1156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2954 (IC base=+0.071)

- **PATRÓN** `volumen_spike_ratio` > `1.5684` → IC=+0.201 (n=7065)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5684 (IC base=+0.071)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.216 (n=7713)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.071)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.220 (n=773)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.178)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.185 (n=770)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.008 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.3502` → IC=+0.185 (n=2304)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.3502 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.193 (n=1125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 15.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.276 (n=932)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.766` → IC=+0.295 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.766 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.230 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `1.4349` → IC=+0.180 (n=2178)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4349 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.194 (n=2371)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.04 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `2052.3` → IC=+0.184 (n=768)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2052.3 (IC base=+0.178)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.243 (n=1649)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.0888` → IC=+0.267 (n=615)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0888 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.258 (n=681)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0595` → IC=+0.285 (n=811)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0595 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.523` → IC=+0.251 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.523 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.415` → IC=+0.237 (n=1927)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.415 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` < `0.0939` → IC=+0.234 (n=1624)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0939 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.265 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.612` → IC=+0.253 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.612 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=2021)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1980.5457` → IC=+0.234 (n=836)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1980.5457 (IC base=+0.234)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.243 (n=806)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.351` → IC=+0.231 (n=1822)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.351 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.235 (n=1828)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `0.9785` → IC=+0.261 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9785 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `0.1891` → IC=+0.222 (n=961)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1891 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` < `0.5446` → IC=+0.225 (n=1919)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5446 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.772` → IC=+0.258 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.772 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` < `1.2487` → IC=+0.223 (n=1822)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2487 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `0.6166` → IC=+0.224 (n=1822)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6166 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` < `0.1611` → IC=+0.219 (n=1878)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1611 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.236 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.4169` → IC=+0.243 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4169 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.180 (n=610)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0026 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.162 (n=611)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.158 (n=702)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.141 (n=830)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 7.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.7224` → IC=+0.178 (n=1828)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.7224 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1275` → IC=+0.155 (n=1650)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1275 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.361` → IC=+0.145 (n=291)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 11.361 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.302` → IC=+0.143 (n=1677)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.302 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.2035` → IC=+0.147 (n=1828)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.2035 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `0.6207` → IC=+0.137 (n=1829)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6207 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.0974` → IC=+0.170 (n=665)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.0974 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4573` → IC=+0.149 (n=1716)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4573 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.7857` → IC=+0.144 (n=1144)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.7857 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `230.0` → IC=+0.170 (n=720)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 230.0 (IC base=+0.136)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.201 (n=2332)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.196 (n=2328)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 6.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=2084)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.264 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.356` → IC=+0.258 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.356 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.196 (n=2036)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.3499` → IC=+0.192 (n=310)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.3499 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `1.7667` → IC=+0.198 (n=1999)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.7667 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.197 (n=2782)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `2032.445` → IC=+0.202 (n=776)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2032.445 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.221 (n=1807)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.1771` → IC=+0.223 (n=904)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1771 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=782)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.215 (n=959)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.0645` → IC=+0.233 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0645 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.697` → IC=+0.248 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.697 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.3471` → IC=+0.256 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3471 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.7289` → IC=+0.217 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7289 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.7373` → IC=+0.227 (n=871)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7373 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.212 (n=1185)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `1955.48` → IC=+0.215 (n=930)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1955.48 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.215 (n=1856)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.212)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.164 (n=126)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=2774)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.153 (n=442)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0036 (IC base=+0.042)

- **PATRÓN** `ibs_20min` > `0.9588` → IC=+0.222 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9588 (IC base=+0.042)

- **PATRÓN** `dist_vwap_pct` < `0.1865` → IC=+0.325 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1865 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.971` → IC=+0.175 (n=920)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 4.971 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` < `0.8546` → IC=+0.332 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8546 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` > `1.2208` → IC=+0.330 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2208 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` < `0.1819` → IC=+0.317 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1819 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.3037` → IC=+0.337 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3037 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` < `1.4291` → IC=+0.359 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4291 (IC base=+0.042)

- **PATRÓN** `ballena_activa_n` < `154.0` → IC=+0.324 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 154.0 (IC base=+0.042)

- **PATRÓN** `ibs_20min` < `0.0999` → IC=+0.162 (n=726)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.0999 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` > `0.4612` → IC=+0.198 (n=240)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.4612 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` < `0.8504` → IC=+0.155 (n=770)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8504 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.2877` → IC=+0.210 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2877 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` > `1.5315` → IC=+0.166 (n=983)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.5315 (IC base=+0.028)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.175 (n=75)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=427)

- **FILTRO** `ibs_20min` < `0.3103` → IC=-0.182 (n=124)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3103
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=378)

- **FILTRO** `ibs_20min` > `0.2308` → IC=-0.126 (n=2793)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2308
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=1389)

- **FILTRO** `sigma_ewma_delta_pct` > `8.784` → IC=-0.218 (n=438)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.784
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=3744)

- **PATRÓN** `ibs_20min` > `0.8` → IC=+0.194 (n=171)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.8 (IC base=+0.040)

- **PATRÓN** `dist_vwap_pct` > `0.9797` → IC=+0.285 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9797 (IC base=+0.040)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.351` → IC=+0.138 (n=175)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 2.351 (IC base=+0.040)

- **PATRÓN** `volumen_regimen` > `1.0782` → IC=+0.300 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0782 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` < `0.1509` → IC=+0.283 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1509 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` < `2.1712` → IC=+0.293 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1712 (IC base=+0.040)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.280 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.040)

- **PATRÓN** `ibs_20min` < `0.2308` → IC=+0.136 (n=1389)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.2308 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.1816` → IC=+0.270 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1816 (IC base=-0.039)

- **PATRÓN** `volumen_regimen` < `0.6948` → IC=+0.272 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6948 (IC base=-0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.1613` → IC=+0.321 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1613 (IC base=-0.039)

- **PATRÓN** `volumen_spike_ratio` < `2.4196` → IC=+0.293 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4196 (IC base=-0.039)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.638` → IC=-0.176 (n=733)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.638
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=2201)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.207 (n=745)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2189)

- **FILTRO** `ibs_20min` > `0.7658` → IC=-0.206 (n=1087)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7658
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=3263)

- **PATRÓN** `dist_vwap_pct` > `0.7626` → IC=+0.316 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7626 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` < `0.2747` → IC=+0.310 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2747 (IC base=-0.070)

- **PATRÓN** `volumen_regimen` < `0.988` → IC=+0.295 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.988 (IC base=-0.070)

- **PATRÓN** `volumen_regimen` > `0.6476` → IC=+0.310 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6476 (IC base=-0.070)

- **PATRÓN** `volumen_pendiente_norm` < `0.1025` → IC=+0.301 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1025 (IC base=-0.070)

- **PATRÓN** `volumen_spike_ratio` < `2.4802` → IC=+0.298 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4802 (IC base=-0.070)

- **PATRÓN** `volumen_spike_ratio` > `1.8609` → IC=+0.298 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8609 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` > `0.8408` → IC=+0.287 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8408 (IC base=-0.013)

- **PATRÓN** `volumen_regimen` < `0.7232` → IC=+0.248 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7232 (IC base=-0.013)

- **PATRÓN** `volumen_regimen` > `1.0722` → IC=+0.279 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0722 (IC base=-0.013)

- **PATRÓN** `volumen_pendiente_norm` > `0.0997` → IC=+0.268 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0997 (IC base=-0.013)

- **PATRÓN** `volumen_spike_ratio` < `2.1538` → IC=+0.256 (n=871)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1538 (IC base=-0.013)

- **PATRÓN** `volumen_spike_ratio` > `1.4219` → IC=+0.256 (n=990)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4219 (IC base=-0.013)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.198 (n=4518)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0094 (IC base=+0.099)

- **PATRÓN** `ibs_20min` > `0.4693` → IC=+0.187 (n=12094)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4693 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.6822` → IC=+0.284 (n=1408)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6822 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.69` → IC=+0.154 (n=6139)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 3.69 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` < `1.1749` → IC=+0.247 (n=4946)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1749 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` > `0.692` → IC=+0.255 (n=4418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.692 (IC base=+0.099)

- **PATRÓN** `volumen_pendiente_norm` < `0.1099` → IC=+0.242 (n=7685)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1099 (IC base=+0.099)

- **PATRÓN** `volumen_pendiente_norm` > `0.2954` → IC=+0.255 (n=1140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2954 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` < `1.4695` → IC=+0.241 (n=2660)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4695 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` > `2.6475` → IC=+0.255 (n=2659)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6475 (IC base=+0.099)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.275 (n=7534)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.099)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.165 (n=4366)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0089 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.5455` → IC=+0.158 (n=11516)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.5455 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.6833` → IC=+0.251 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6833 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.2359` → IC=+0.251 (n=3783)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2359 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.7077` → IC=+0.249 (n=1741)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7077 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.1973` → IC=+0.262 (n=1319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1973 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2957` → IC=+0.307 (n=776)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2957 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.5933` → IC=+0.280 (n=2416)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5933 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.2867` → IC=+0.269 (n=2489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2867 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.282 (n=5389)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 78.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2584` → IC=-0.162 (n=940)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2584
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=2825)

- **FILTRO** `ibs_20min` > `0.7573` → IC=-0.173 (n=774)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7573
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=2323)

- **FILTRO** `sigma_ewma_delta_pct` > `4.594` → IC=-0.174 (n=691)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.594
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=2406)

- **PATRÓN** `ibs_20min` > `0.9077` → IC=+0.275 (n=942)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9077 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.261` → IC=+0.200 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.261 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.2277` → IC=+0.272 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2277 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` < `1.4426` → IC=+0.213 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4426 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` > `2.2004` → IC=+0.230 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2004 (IC base=+0.041)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.225 (n=832)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.2231` → IC=+0.435 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2231 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` < `2.6396` → IC=+0.427 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6396 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` > `1.5328` → IC=+0.423 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5328 (IC base=-0.023)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.418 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=-0.023)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8651` → IC=+0.160 (n=907)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.8651 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` > `0.1138` → IC=+0.194 (n=695)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1138 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` > `0.6779` → IC=+0.183 (n=1142)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.6779 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` < `0.0758` → IC=+0.172 (n=1180)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` < 0.0758 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.212 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` < `1.4288` → IC=+0.194 (n=419)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4288 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` > `2.4379` → IC=+0.186 (n=419)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.4379 (IC base=+0.028)

- **PATRÓN** `ballena_activa_n` < `229.0` → IC=+0.230 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 229.0 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` < `0.1504` → IC=+0.226 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1504 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` > `0.613` → IC=+0.228 (n=756)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.613 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2706` → IC=+0.302 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2706 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.4386` → IC=+0.232 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4386 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1719` → IC=+0.238 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1719 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.272 (n=2055)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.251)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.256 (n=2067)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.252 (n=2065)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.251)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=1069)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.251)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.786` → IC=+0.282 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.786 (IC base=+0.251)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.267 (n=1754)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.251)

- **PATRÓN** `volumen_spike_ratio` > `2.1777` → IC=+0.264 (n=1310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1777 (IC base=+0.251)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.261 (n=2432)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.251)

- **PATRÓN** `libro_liquidez` > `2024.646` → IC=+0.273 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2024.646 (IC base=+0.251)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.301 (n=1709)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.1799` → IC=+0.301 (n=752)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1799 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.320 (n=577)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.287)

- **PATRÓN** `ibs_20min` < `0.36` → IC=+0.292 (n=1708)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.36 (IC base=+0.287)

- **PATRÓN** `ibs_20min` > `0.1` → IC=+0.287 (n=1141)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.7` → IC=+0.297 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.7 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` < `0.1951` → IC=+0.282 (n=1660)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1951 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` > `0.1208` → IC=+0.291 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1208 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` < `1.7249` → IC=+0.300 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7249 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` > `2.6449` → IC=+0.292 (n=730)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6449 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1947.66` → IC=+0.298 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1947.66 (IC base=+0.287)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.288 (n=1398)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.287)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7682` → IC=-0.183 (n=784)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7682
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=2356)

- **PATRÓN** `ibs_20min` > `0.9028` → IC=+0.169 (n=714)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.9028 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.2109` → IC=+0.220 (n=754)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2109 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `1.009` → IC=+0.244 (n=821)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.009 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.1715` → IC=+0.231 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1715 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.0824` → IC=+0.227 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0824 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.4183` → IC=+0.261 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4183 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.291 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.1217` → IC=+0.236 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1217 (IC base=-0.003)

- **PATRÓN** `volumen_regimen` < `1.0403` → IC=+0.226 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0403 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2957` → IC=+0.282 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2957 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.8558` → IC=+0.266 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8558 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.5231` → IC=+0.238 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5231 (IC base=-0.003)

- **PATRÓN** `ballena_activa_n` < `132.0` → IC=+0.259 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 132.0 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7632` → IC=-0.186 (n=1440)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7632
  - _Potencial_: sin este filtro IC_bueno=+0.284 (n=1442)

- **FILTRO** `ibs_20min` > `0.6696` → IC=-0.244 (n=724)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6696
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=2174)

- **FILTRO** `sigma_ewma_delta_pct` > `4.814` → IC=-0.203 (n=614)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.814
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=2284)

- **PATRÓN** `ibs_20min` > `0.7632` → IC=+0.284 (n=1442)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7632 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `1.0273` → IC=+0.333 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0273 (IC base=+0.049)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.668` → IC=+0.164 (n=453)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 9.668 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` < `0.8605` → IC=+0.311 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8605 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` > `0.639` → IC=+0.304 (n=1098)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.639 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.301 (n=1036)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.2757` → IC=+0.324 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2757 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` < `1.7979` → IC=+0.315 (n=710)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7979 (IC base=+0.049)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.324 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.049)

- **PATRÓN** `ibs_20min` < `0.5714` → IC=+0.133 (n=1921)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5714 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` < `0.2679` → IC=+0.242 (n=780)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2679 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `0.7052` → IC=+0.269 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7052 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `1.1883` → IC=+0.231 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1883 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.0703` → IC=+0.265 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0703 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `2.4456` → IC=+0.250 (n=799)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4456 (IC base=+0.022)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.263 (n=808)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.022)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.008` → IC=+0.326 (n=1638)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.008 (IC base=+0.286)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.305 (n=771)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.286)

- **PATRÓN** `ibs_20min` > `0.6494` → IC=+0.320 (n=1638)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6494 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.2129` → IC=+0.319 (n=954)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2129 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.776` → IC=+0.309 (n=815)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.776 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.947` → IC=+0.286 (n=1848)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.947 (IC base=+0.286)

- **PATRÓN** `volumen_regimen` > `0.8596` → IC=+0.312 (n=1092)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8596 (IC base=+0.286)

- **PATRÓN** `volumen_pendiente_norm` > `0.2809` → IC=+0.336 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2809 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` > `1.4334` → IC=+0.299 (n=1563)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4334 (IC base=+0.286)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.289 (n=1594)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `2644.5329` → IC=+0.299 (n=1092)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2644.5329 (IC base=+0.286)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.322 (n=1360)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.286)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.317 (n=1158)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.1875` → IC=+0.287 (n=764)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1875 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.291 (n=1650)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.286)

- **PATRÓN** `ibs_20min` < `0.37` → IC=+0.311 (n=1736)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.37 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.3052` → IC=+0.294 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3052 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` < `0.2248` → IC=+0.286 (n=1598)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2248 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.512` → IC=+0.298 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.512 (IC base=+0.286)

- **PATRÓN** `volumen_regimen` > `1.2298` → IC=+0.318 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2298 (IC base=+0.286)

- **PATRÓN** `volumen_pendiente_norm` > `0.2334` → IC=+0.333 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2334 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` < `1.4227` → IC=+0.296 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4227 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` > `2.1367` → IC=+0.285 (n=710)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1367 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `2638.1798` → IC=+0.289 (n=1157)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2638.1798 (IC base=+0.286)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.187 (n=3371)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0047 (IC base=+0.174)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.208 (n=3367)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.3541` → IC=+0.185 (n=8888)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.3541 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=10552)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.569` → IC=+0.227 (n=10100)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.569 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.17` → IC=+0.200 (n=4357)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.17 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.456` → IC=+0.251 (n=2031)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.456 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `1.2068` → IC=+0.167 (n=6720)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2068 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` > `0.63` → IC=+0.162 (n=6719)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.63 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.2957` → IC=+0.198 (n=1501)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2957 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `1.566` → IC=+0.174 (n=4286)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.566 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `2.613` → IC=+0.182 (n=3248)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.613 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `1992.2048` → IC=+0.178 (n=9023)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 1992.2048 (IC base=+0.174)

- **PATRÓN** `ballena_activa_n` < `104.0` → IC=+0.189 (n=9010)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 104.0 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.188 (n=6429)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0066 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.0801` → IC=+0.223 (n=3212)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0801 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=3668)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` < `0.4861` → IC=+0.231 (n=9632)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4861 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` < `0.1678` → IC=+0.170 (n=6703)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1678 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.32` → IC=+0.196 (n=1613)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.32 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` < `1.1779` → IC=+0.163 (n=6906)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1779 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` > `0.2923` → IC=+0.215 (n=1397)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2923 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` < `1.5615` → IC=+0.173 (n=3929)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.5615 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `2.6147` → IC=+0.177 (n=2976)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.6147 (IC base=+0.175)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.184 (n=8592)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 106.0 (IC base=+0.175)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.239 (n=565)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.199)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.205 (n=567)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.3411` → IC=+0.220 (n=1692)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3411 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.203 (n=1693)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.201 (n=1230)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` > `0.9158` → IC=+0.286 (n=1128)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9158 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.283` → IC=+0.332 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.283 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.250 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `1.825` → IC=+0.191 (n=1057)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.825 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `1.4361` → IC=+0.197 (n=1584)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4361 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.212 (n=1751)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.199)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.248 (n=1133)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.242)

- **PATRÓN** `sigma_h` > `0.0042` → IC=+0.249 (n=1287)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0042 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.1015` → IC=+0.296 (n=566)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1015 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.251 (n=1235)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.1026` → IC=+0.278 (n=858)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1026 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.392` → IC=+0.245 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.392 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.242` → IC=+0.248 (n=1393)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.242 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` < `0.1623` → IC=+0.240 (n=1241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1623 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.2925` → IC=+0.271 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2925 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` < `1.4211` → IC=+0.260 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4211 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `2.621` → IC=+0.242 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.621 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.243 (n=1419)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `1971.7086` → IC=+0.256 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1971.7086 (IC base=+0.242)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.219 (n=670)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.1657` → IC=+0.185 (n=1013)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1657 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.181 (n=1524)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `0.3916` → IC=+0.224 (n=1518)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3916 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.1985` → IC=+0.213 (n=891)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1985 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.528` → IC=+0.232 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.528 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `0.6895` → IC=+0.170 (n=668)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.6895 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.193 (n=239)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `1.4168` → IC=+0.185 (n=494)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.4168 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `2.4856` → IC=+0.157 (n=494)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.4856 (IC base=+0.159)

- **PATRÓN** `ballena_activa_n` < `236.0` → IC=+0.172 (n=635)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 236.0 (IC base=+0.159)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.162 (n=1592)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0057 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.2985` → IC=+0.166 (n=1589)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.2985 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.182 (n=612)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.5923` → IC=+0.199 (n=1590)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.5923 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.1339` → IC=+0.171 (n=1575)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1339 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.912` → IC=+0.201 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.912 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.2096` → IC=+0.162 (n=1589)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2096 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` < `0.2292` → IC=+0.145 (n=1637)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` < 0.2292 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.1598` → IC=+0.148 (n=487)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.1598 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `2.485` → IC=+0.153 (n=1477)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.485 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.7706` → IC=+0.144 (n=984)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.7706 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `208.0` → IC=+0.175 (n=469)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 208.0 (IC base=+0.142)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.227 (n=565)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.2476` → IC=+0.221 (n=1127)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2476 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.224 (n=600)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.293 (n=881)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.539` → IC=+0.277 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.539 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.205 (n=1423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.1282` → IC=+0.207 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1282 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `1.7745` → IC=+0.205 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7745 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `2.7293` → IC=+0.213 (n=736)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7293 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=2010)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `1955.4972` → IC=+0.226 (n=767)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1955.4972 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.243 (n=1269)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0102 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.143` → IC=+0.261 (n=634)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.143 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.278 (n=497)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` < `0.3506` → IC=+0.249 (n=1441)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3506 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.677` → IC=+0.259 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.677 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.3507` → IC=+0.261 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3507 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `1.7408` → IC=+0.240 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7408 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `2.7291` → IC=+0.235 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7291 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `1946.335` → IC=+0.231 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1946.335 (IC base=+0.226)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.220 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.226)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.207 (n=715)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.0786` → IC=+0.202 (n=542)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0786 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=1692)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.3344` → IC=+0.208 (n=1623)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3344 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.1385` → IC=+0.189 (n=1061)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1385 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.995` → IC=+0.209 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.995 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.8563` → IC=+0.163 (n=1083)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8563 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1017` → IC=+0.170 (n=680)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1017 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `1.437` → IC=+0.166 (n=531)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.437 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `2.5308` → IC=+0.162 (n=531)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.5308 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `5095.3746` → IC=+0.197 (n=1082)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 5095.3746 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.154 (n=1560)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 151.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.162 (n=1491)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0061 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.3828` → IC=+0.149 (n=1693)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3828 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=648)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.6697` → IC=+0.184 (n=1693)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6697 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.904` → IC=+0.160 (n=586)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 6.904 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.8556` → IC=+0.160 (n=1129)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8556 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2969` → IC=+0.184 (n=254)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2969 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.8212` → IC=+0.140 (n=1044)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.8212 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `1.5265` → IC=+0.129 (n=1399)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.5265 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `4360.2899` → IC=+0.166 (n=1128)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 4360.2899 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `149.0` → IC=+0.128 (n=1505)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 149.0 (IC base=+0.128)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.161 (n=838)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0099 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.4445` → IC=+0.128 (n=1626)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.4445 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=1892)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.212 (n=1861)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `1.0351` → IC=+0.215 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0351 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.874` → IC=+0.259 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.874 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `1.2036` → IC=+0.137 (n=1848)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.2036 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` > `0.6463` → IC=+0.130 (n=1848)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 0.6463 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` < `0.1642` → IC=+0.134 (n=1865)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.1642 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.5459` → IC=+0.143 (n=786)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.5459 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.4852` → IC=+0.129 (n=596)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 2.4852 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.129 (n=1937)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `2388.0002` → IC=+0.186 (n=1232)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2388.0002 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.148 (n=1460)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 46.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.155 (n=819)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0061 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1034` → IC=+0.179 (n=618)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.1034 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=1868)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.5778` → IC=+0.217 (n=1852)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5778 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `0.7489` → IC=+0.123 (n=335)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.7489 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.197` → IC=+0.148 (n=1700)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.197 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.441` → IC=+0.124 (n=757)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 3.441 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.1756` → IC=+0.131 (n=1852)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1756 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2289` → IC=+0.155 (n=326)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.2289 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4534` → IC=+0.138 (n=567)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.4534 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `1.8188` → IC=+0.125 (n=1132)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.8188 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2749.8` → IC=+0.184 (n=840)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2749.8 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.128 (n=1658)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 52.0 (IC base=+0.120)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.232 (n=1731)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.2868` → IC=+0.214 (n=1154)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2868 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=1803)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.212 (n=784)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.246 (n=1732)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.1979` → IC=+0.214 (n=1177)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1979 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.594` → IC=+0.245 (n=797)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.594 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` < `1.1935` → IC=+0.211 (n=1731)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1935 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `0.6237` → IC=+0.217 (n=1732)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6237 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.273 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.283 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `2.4718` → IC=+0.211 (n=1678)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4718 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.8108` → IC=+0.221 (n=1119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8108 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.211 (n=1653)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `2635.1118` → IC=+0.211 (n=1154)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2635.1118 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.0117` → IC=+0.228 (n=781)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0117 (IC base=+0.216)

- **PATRÓN** `sigma_h` > `0.0223` → IC=+0.222 (n=805)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0223 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.0901` → IC=+0.241 (n=592)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0901 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.237 (n=872)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` < `0.0196` → IC=+0.287 (n=781)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0196 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `1.1567` → IC=+0.235 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1567 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.365` → IC=+0.253 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.365 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `0.6367` → IC=+0.228 (n=1774)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6367 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.2821` → IC=+0.274 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2821 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `2.1991` → IC=+0.208 (n=1431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1991 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `1.4386` → IC=+0.216 (n=1626)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4386 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `2610.8726` → IC=+0.223 (n=1183)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2610.8726 (IC base=+0.216)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.196 (n=1166)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0041 (IC base=+0.169)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.172 (n=886)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0084 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.3375` → IC=+0.180 (n=2332)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.3375 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.189 (n=2413)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 8.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.3404` → IC=+0.197 (n=2650)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.3404 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.7873` → IC=+0.184 (n=422)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.7873 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.756` → IC=+0.195 (n=1154)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 3.756 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `0.869` → IC=+0.190 (n=1581)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.869 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `1.2057` → IC=+0.178 (n=790)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 1.2057 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.1639` → IC=+0.174 (n=703)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1639 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.4437` → IC=+0.183 (n=858)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.4437 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.5338` → IC=+0.174 (n=858)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.5338 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.172 (n=3025)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `2741.5709` → IC=+0.171 (n=2368)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2741.5709 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `146.0` → IC=+0.186 (n=2432)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 146.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.154 (n=909)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0036 (IC base=+0.111)

- **PATRÓN** `drift_60min` |x|≤ `0.3369` → IC=+0.122 (n=2396)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.61€ cuando `drift_60min` |x|≤ 0.3369 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.123 (n=2558)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` < `0.0721` → IC=+0.197 (n=909)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.0721 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `0.6986` → IC=+0.125 (n=1085)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 0.6986 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.0753` → IC=+0.127 (n=1037)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` > 0.0753 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `1.4406` → IC=+0.149 (n=881)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4406 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2793.9248` → IC=+0.130 (n=2432)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2793.9248 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.130 (n=1148)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 29.0 (IC base=+0.111)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.210 (n=322)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.3296` → IC=+0.174 (n=729)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.3296 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.191 (n=674)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 8.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.6381` → IC=+0.207 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6381 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.291` → IC=+0.172 (n=245)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.291 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.146` → IC=+0.175 (n=315)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.146 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.8788` → IC=+0.180 (n=486)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.8788 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` < `0.157` → IC=+0.156 (n=765)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.157 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.2468` → IC=+0.158 (n=626)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.2468 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.5264` → IC=+0.155 (n=636)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.5264 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `14621.9043` → IC=+0.166 (n=486)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 14621.9043 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.205 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 150.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.203 (n=291)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.3454` → IC=+0.159 (n=862)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.3454 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.150 (n=826)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 6.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.147 (n=874)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 17.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.611` → IC=+0.184 (n=758)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.611 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.1812` → IC=+0.159 (n=856)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1812 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.162` → IC=+0.148 (n=788)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 3.162 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.2142` → IC=+0.146 (n=862)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.2142 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` > `1.063` → IC=+0.169 (n=391)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.063 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.1608` → IC=+0.198 (n=233)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1608 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `2.121` → IC=+0.161 (n=750)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.121 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=1114)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `12062.2629` → IC=+0.144 (n=770)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 12062.2629 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `354.0` → IC=+0.155 (n=829)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 354.0 (IC base=+0.143)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.242 (n=563)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.2048` → IC=+0.219 (n=560)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2048 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.219 (n=881)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `0.6705` → IC=+0.253 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6705 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.3577` → IC=+0.212 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3577 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` < `0.2037` → IC=+0.205 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2037 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.09` → IC=+0.221 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.09 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` < `0.8419` → IC=+0.210 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8419 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` > `1.1822` → IC=+0.220 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1822 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.1608` → IC=+0.231 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1608 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `1.4324` → IC=+0.224 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4324 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `2.4672` → IC=+0.234 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4672 (IC base=+0.202)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.136 (n=707)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0061 (IC base=+0.108)

- **PATRÓN** `drift_60min` |x|≤ `0.0974` → IC=+0.139 (n=267)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.0974 (IC base=+0.108)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.125 (n=721)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 7.0 (IC base=+0.108)

- **PATRÓN** `ibs_20min` < `0.0868` → IC=+0.165 (n=267)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.0868 (IC base=+0.108)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.472` → IC=+0.154 (n=209)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 6.472 (IC base=+0.108)

- **PATRÓN** `volumen_regimen` < `0.6885` → IC=+0.153 (n=353)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6885 (IC base=+0.108)

- **PATRÓN** `volumen_pendiente_norm` > `0.2234` → IC=+0.143 (n=127)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.2234 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `4005.7464` → IC=+0.133 (n=715)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 4005.7464 (IC base=+0.108)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.130 (n=344)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 42.0 (IC base=+0.108)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.475` → IC=-0.126 (n=268)

  - _Acción_: SKIP cuando `ibs_20min` > 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=522)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.172 (n=613)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0051 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.5405` → IC=+0.161 (n=612)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.5405 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.191 (n=558)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 8.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.277 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.947` → IC=+0.233 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.947 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.329` → IC=+0.218 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.329 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `1.0674` → IC=+0.176 (n=538)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.0674 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` > `0.6528` → IC=+0.166 (n=612)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6528 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.2813` → IC=+0.174 (n=90)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2813 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `2.4855` → IC=+0.159 (n=590)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.4855 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `2.1991` → IC=+0.174 (n=268)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.1991 (IC base=+0.159)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.163 (n=648)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.02 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `3078.7088` → IC=+0.194 (n=204)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 3078.7088 (IC base=+0.159)

- **PATRÓN** `ibs_20min` < `0.475` → IC=+0.147 (n=522)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.475 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` < `1.569` → IC=+0.124 (n=248)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.569 (IC base=+0.054)

- **PATRÓN** `libro_liquidez` > `2864.9802` → IC=+0.153 (n=269)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2864.9802 (IC base=+0.054)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.143 (n=242)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 15.0 (IC base=+0.054)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0238` → IC=+0.170 (n=192)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0238 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.0144` → IC=+0.200 (n=128)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0144 (IC base=+0.154)

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

- **PATRÓN** `volumen_regimen` > `0.6949` → IC=+0.176 (n=171)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6949 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` < `0.1233` → IC=+0.175 (n=155)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.1233 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.4483` → IC=+0.241 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4483 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `2.6132` → IC=+0.172 (n=56)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.6132 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.183 (n=197)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `2503.8283` → IC=+0.169 (n=128)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2503.8283 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.160 (n=189)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0119 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.158 (n=77)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.131 (n=212)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.6 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` > `1.1597` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1597 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.025` → IC=+0.146 (n=80)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 3.025 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` > `0.6515` → IC=+0.126 (n=212)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.6515 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.2293` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2293 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` > `2.8124` → IC=+0.132 (n=66)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.8124 (IC base=+0.116)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.138 (n=172)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 17.0 (IC base=+0.116)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.178 (n=4375)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0046 (IC base=+0.176)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.212 (n=4354)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=13668)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `0.9914` → IC=+0.309 (n=4352)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9914 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.1638` → IC=+0.186 (n=4948)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1638 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.392` → IC=+0.246 (n=3208)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.392 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `1.2317` → IC=+0.165 (n=8746)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2317 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.2905` → IC=+0.197 (n=1774)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2905 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `2.602` → IC=+0.195 (n=4210)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.602 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `1977.5784` → IC=+0.180 (n=11664)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 1977.5784 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.202 (n=10294)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 79.0 (IC base=+0.176)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.196 (n=5189)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0053 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.1468` → IC=+0.195 (n=5175)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1468 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=4446)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` < `0.4516` → IC=+0.248 (n=10351)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4516 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` < `0.173` → IC=+0.166 (n=6947)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.173 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.097` → IC=+0.204 (n=1659)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.097 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.749` → IC=+0.185 (n=11329)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 3.749 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `0.7054` → IC=+0.163 (n=3509)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.7054 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.2897` → IC=+0.249 (n=1566)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2897 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `1.8643` → IC=+0.192 (n=7323)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 1.8643 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.207 (n=7090)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.185)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.250 (n=723)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.207)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.224 (n=723)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.3542` → IC=+0.209 (n=2169)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3542 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.225 (n=1057)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.210 (n=1451)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.328 (n=806)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.744` → IC=+0.354 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.744 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.2292` → IC=+0.262 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2292 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `2.5801` → IC=+0.216 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5801 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.227 (n=2217)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `2052.8` → IC=+0.212 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2052.8 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.265 (n=1187)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.259)

- **PATRÓN** `sigma_h` > `0.0043` → IC=+0.264 (n=1783)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0043 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.1247` → IC=+0.281 (n=784)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1247 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.270 (n=1608)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.3587` → IC=+0.283 (n=1567)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3587 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.509` → IC=+0.265 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.509 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.2832` → IC=+0.289 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2832 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `2.6244` → IC=+0.279 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6244 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.260 (n=1953)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1977.88` → IC=+0.270 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1977.88 (IC base=+0.259)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.211 (n=698)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.1797` → IC=+0.164 (n=1395)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1797 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=2193)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.2855` → IC=+0.206 (n=2090)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2855 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.126` → IC=+0.190 (n=1182)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.126 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.75` → IC=+0.179 (n=350)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 11.75 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.233` → IC=+0.153 (n=1911)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.233 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.703` → IC=+0.170 (n=920)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.703 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.0734` → IC=+0.153 (n=1851)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0734 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2717` → IC=+0.188 (n=299)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2717 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.1442` → IC=+0.161 (n=1788)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1442 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.5212` → IC=+0.155 (n=1816)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.5212 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `277.0` → IC=+0.183 (n=870)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 277.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.161 (n=1744)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0057 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.3305` → IC=+0.158 (n=1744)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.3305 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=668)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.148 (n=793)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 7.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.6837` → IC=+0.196 (n=1744)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.6837 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.1318` → IC=+0.166 (n=1592)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1318 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.563` → IC=+0.159 (n=294)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 11.563 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.341` → IC=+0.146 (n=1577)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 4.341 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.1913` → IC=+0.159 (n=1744)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1913 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1548` → IC=+0.199 (n=466)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1548 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.4364` → IC=+0.154 (n=1643)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4364 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.7778` → IC=+0.159 (n=1095)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7778 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `258.0` → IC=+0.145 (n=519)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 258.0 (IC base=+0.145)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.232 (n=2143)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.228 (n=2143)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.226 (n=2162)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=810)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.864` → IC=+0.294 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.864 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` < `0.2056` → IC=+0.226 (n=2157)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2056 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `1.7675` → IC=+0.232 (n=1843)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7675 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=2557)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `2032.0592` → IC=+0.242 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2032.0592 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.243 (n=1768)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.1801` → IC=+0.249 (n=885)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1801 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.258 (n=770)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.236 (n=943)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0146` → IC=+0.301 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0146 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.949` → IC=+0.286 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.949 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.3417` → IC=+0.296 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3417 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.735` → IC=+0.236 (n=829)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.735 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.1488` → IC=+0.241 (n=1255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1488 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.237 (n=1165)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1947.66` → IC=+0.246 (n=911)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1947.66 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.253 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.234)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.198 (n=986)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0038 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.3343` → IC=+0.153 (n=1968)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.3343 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.155 (n=2333)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.2701` → IC=+0.189 (n=2236)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.2701 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.5422` → IC=+0.163 (n=610)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.5422 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.174` → IC=+0.151 (n=915)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 4.174 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8733` → IC=+0.160 (n=1490)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8733 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.1662` → IC=+0.173 (n=595)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1662 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.5279` → IC=+0.159 (n=957)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.5279 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.186` → IC=+0.150 (n=986)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.186 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `7316.3109` → IC=+0.235 (n=1013)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7316.3109 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.181 (n=704)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 70.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.188 (n=604)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0033 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.3486` → IC=+0.144 (n=1586)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3486 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.160 (n=666)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.134 (n=629)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 5.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.7338` → IC=+0.183 (n=1801)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.7338 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.36` → IC=+0.170 (n=274)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 11.36 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `0.8747` → IC=+0.143 (n=1201)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.8747 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.2975` → IC=+0.229 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2975 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `2.2519` → IC=+0.136 (n=1519)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.2519 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `1.4482` → IC=+0.142 (n=1726)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4482 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `8699.5677` → IC=+0.205 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8699.5677 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.135 (n=1723)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 166.0 (IC base=+0.132)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.135 (n=2243)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0056 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=827)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.4565` → IC=+0.200 (n=2243)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4565 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `1.024` → IC=+0.210 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.024 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.525` → IC=+0.243 (n=827)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.525 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.2309` → IC=+0.137 (n=2243)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.2309 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1623` → IC=+0.128 (n=2311)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1623 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.1941` → IC=+0.136 (n=990)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.1941 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.131 (n=2292)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2553.7156` → IC=+0.236 (n=1017)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2553.7156 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.146 (n=676)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 27.0 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.173 (n=720)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0056 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.1302` → IC=+0.165 (n=714)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1302 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.160 (n=794)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.5049` → IC=+0.234 (n=1883)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5049 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` < `0.2163` → IC=+0.140 (n=1771)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.2163 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.49` → IC=+0.133 (n=2062)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 3.49 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.7143` → IC=+0.160 (n=943)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.7143 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2238` → IC=+0.184 (n=349)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2238 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `2.1656` → IC=+0.137 (n=1736)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.1656 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2799.1755` → IC=+0.198 (n=713)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2799.1755 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.139 (n=1730)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 50.0 (IC base=+0.122)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.233 (n=2180)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.220 (n=2283)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.219 (n=1569)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.263 (n=1950)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `0.2081` → IC=+0.233 (n=1247)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2081 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.748` → IC=+0.262 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.748 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` < `1.2391` → IC=+0.219 (n=2180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2391 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `0.6411` → IC=+0.222 (n=2180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6411 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.2365` → IC=+0.241 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2365 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `2.5125` → IC=+0.249 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5125 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=2061)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `2636.2554` → IC=+0.224 (n=1453)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2636.2554 (IC base=+0.216)

- **PATRÓN** `sigma_h` < `0.0095` → IC=+0.217 (n=766)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0095 (IC base=+0.215)

- **PATRÓN** `sigma_h` > `0.0226` → IC=+0.230 (n=1040)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0226 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.231 (n=1623)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.4167` → IC=+0.264 (n=2015)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4167 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `1.1797` → IC=+0.215 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1797 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` < `0.2936` → IC=+0.218 (n=2141)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2936 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.876` → IC=+0.255 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.876 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `1.2292` → IC=+0.244 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2292 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.2821` → IC=+0.284 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2821 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.215 (n=2098)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=+0.215)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.206 (n=2018)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.215)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.166 (n=3815)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.229 (n=1303)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.3911` → IC=+0.196 (n=3421)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.3911 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.201 (n=1455)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.188 (n=1762)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 6.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` > `0.9411` → IC=+0.242 (n=1296)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9411 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` > `0.1681` → IC=+0.195 (n=1441)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1681 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.195` → IC=+0.210 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.195 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` < `0.7115` → IC=+0.191 (n=1180)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.7115 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` > `0.8924` → IC=+0.190 (n=1788)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 0.8924 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.1702` → IC=+0.215 (n=1094)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1702 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` < `1.4601` → IC=+0.192 (n=1278)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.4601 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `2.6347` → IC=+0.192 (n=1278)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6347 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.193 (n=2875)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.186)

- **PATRÓN** `libro_liquidez` > `3788.4039` → IC=+0.195 (n=2591)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 3788.4039 (IC base=+0.186)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.222 (n=962)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.4845` → IC=+0.181 (n=2873)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.4845 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.199 (n=1017)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.181 (n=1298)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 6.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` < `0.18` → IC=+0.188 (n=1265)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.18 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.6448` → IC=+0.179 (n=530)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.6448 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` < `0.2352` → IC=+0.158 (n=2562)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.2352 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.184` → IC=+0.172 (n=2864)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` < 6.184 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `1.2562` → IC=+0.168 (n=2709)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2562 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` < `0.0969` → IC=+0.169 (n=2617)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.0969 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.2228` → IC=+0.167 (n=598)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2228 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `1.5394` → IC=+0.169 (n=1247)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.5394 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `1.8277` → IC=+0.174 (n=1889)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.8277 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.166 (n=3815)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `12310.7311` → IC=+0.166 (n=958)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 12310.7311 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `198.0` → IC=+0.174 (n=2468)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 198.0 (IC base=+0.164)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.239 (n=351)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.0834` → IC=+0.263 (n=175)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0834 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.223 (n=525)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.214 (n=232)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.51` → IC=+0.233 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.51 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.7622` → IC=+0.217 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7622 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` < `0.3165` → IC=+0.221 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3165 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.039` → IC=+0.231 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.039 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.526` → IC=+0.213 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.526 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` < `1.2246` → IC=+0.221 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2246 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` > `0.5931` → IC=+0.221 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5931 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2975` → IC=+0.306 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2975 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `2.2945` → IC=+0.220 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2945 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `12467.3842` → IC=+0.235 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12467.3842 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.229 (n=467)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.3657` → IC=+0.162 (n=1060)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.3657 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.194 (n=396)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.197 (n=354)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 4.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.1485` → IC=+0.179 (n=466)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.1485 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.6071` → IC=+0.154 (n=481)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.6071 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.6653` → IC=+0.180 (n=101)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.6653 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.211` → IC=+0.150 (n=1074)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.211 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.385` → IC=+0.166 (n=1043)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 6.385 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.8817` → IC=+0.187 (n=707)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.8817 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.2216` → IC=+0.180 (n=220)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2216 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.5397` → IC=+0.154 (n=1056)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.5397 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.8221` → IC=+0.169 (n=704)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.8221 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `11518.9437` → IC=+0.161 (n=1059)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 11518.9437 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `700.0` → IC=+0.160 (n=1014)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 700.0 (IC base=+0.148)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.200 (n=231)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.171)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.186 (n=313)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0098 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.581` → IC=+0.179 (n=689)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.581 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` > `0.994` → IC=+0.233 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.994 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.494` → IC=+0.222 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.494 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.2079` → IC=+0.222 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2079 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `1.6744` → IC=+0.172 (n=230)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.6744 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `3.3613` → IC=+0.184 (n=229)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 3.3613 (IC base=+0.171)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.241 (n=56)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.295 (n=37)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.288 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `0.2121` → IC=+0.276 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2121 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.442` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.442 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.1988` → IC=+0.259 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1988 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `2.3165` → IC=+0.244 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3165 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `1.861` → IC=+0.265 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.861 (IC base=+0.237)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.219 (n=396)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.1504` → IC=+0.216 (n=522)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1504 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=434)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.195 (n=543)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 6.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.5225` → IC=+0.205 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5225 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `0.8847` → IC=+0.199 (n=396)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.8847 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` < `0.2031` → IC=+0.203 (n=993)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2031 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.174` → IC=+0.200 (n=1066)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.174 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `1.0845` → IC=+0.198 (n=1045)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 1.0845 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` > `1.2448` → IC=+0.196 (n=396)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` > 1.2448 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.1659` → IC=+0.206 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1659 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `2.4779` → IC=+0.200 (n=1163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4779 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.197 (n=1189)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.226 (n=315)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.3841` → IC=+0.196 (n=831)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.3841 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.186 (n=323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.165)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.174 (n=634)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 10.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` < `0.7559` → IC=+0.170 (n=945)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.7559 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.0897` → IC=+0.171 (n=945)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.0897 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.6046` → IC=+0.186 (n=205)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.6046 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` < `0.2152` → IC=+0.166 (n=874)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.2152 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.153` → IC=+0.168 (n=1052)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 9.153 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `0.6432` → IC=+0.203 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6432 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` > `0.7259` → IC=+0.166 (n=844)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.7259 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.0728` → IC=+0.183 (n=399)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.0728 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `2.1949` → IC=+0.180 (n=815)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.1949 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `1.7864` → IC=+0.167 (n=617)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.7864 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `7437.397` → IC=+0.179 (n=945)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 7437.397 (IC base=+0.165)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.008` → IC=+0.214 (n=320)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.197 (n=437)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 4.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.260 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.1976` → IC=+0.207 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1976 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.541` → IC=+0.218 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.541 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `0.7091` → IC=+0.195 (n=211)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.7091 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `1.2699` → IC=+0.179 (n=160)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 1.2699 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.1631` → IC=+0.222 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1631 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `2.5383` → IC=+0.220 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5383 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.175 (n=580)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.02 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `3350.8386` → IC=+0.209 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3350.8386 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.191 (n=412)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 49.0 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.232 (n=121)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.3766` → IC=+0.227 (n=243)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3766 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.180 (n=126)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 16.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.207 (n=257)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` < `0.0952` → IC=+0.240 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0952 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.8547` → IC=+0.217 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8547 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.114` → IC=+0.187 (n=65)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 9.114 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.1` → IC=+0.183 (n=351)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 5.1 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `0.7878` → IC=+0.185 (n=160)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.7878 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` < `0.105` → IC=+0.224 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.105 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `1.8988` → IC=+0.192 (n=235)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.8988 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.2063` → IC=+0.191 (n=160)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.2063 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `3502.7972` → IC=+0.197 (n=325)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 3502.7972 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.216 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.179)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.157 (n=557)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0038 (IC base=+0.083)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.126 (n=583)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 16.0 (IC base=+0.083)

- **PATRÓN** `ibs_20min` > `0.4422` → IC=+0.157 (n=1171)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.4422 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` > `0.3509` → IC=+0.153 (n=439)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.3509 (IC base=+0.083)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.472` → IC=+0.184 (n=270)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 11.472 (IC base=+0.083)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.175 (n=161)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.083)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.245 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2 (IC base=+0.047)

- **PATRÓN** `dist_vwap_pct` < `0.1111` → IC=+0.124 (n=490)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.1111 (IC base=+0.047)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.09` → IC=+0.127 (n=414)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 4.09 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.1432` → IC=+0.178 (n=116)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1432 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` < `2.5975` → IC=+0.134 (n=424)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.5975 (IC base=+0.047)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.144 (n=431)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0058 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.124 (n=437)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.099)

- **PATRÓN** `ibs_20min` > `0.4165` → IC=+0.176 (n=399)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.4165 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.1239` → IC=+0.162 (n=214)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.1239 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.581` → IC=+0.123 (n=237)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 3.581 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` < `2.5009` → IC=+0.128 (n=358)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 2.5009 (IC base=+0.099)

- **PATRÓN** `ibs_20min` < `0.0493` → IC=+0.281 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0493 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.1876` → IC=+0.123 (n=258)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.1876 (IC base=+0.073)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.155` → IC=+0.143 (n=225)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 7.155 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.1547` → IC=+0.138 (n=56)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.1547 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` < `2.5091` → IC=+0.129 (n=211)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 2.5091 (IC base=+0.073)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.154 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=156)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.150 (n=278)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0046 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.127 (n=392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 7.0 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.6875` → IC=+0.212 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6875 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.173 (n=215)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.674` → IC=+0.280 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.674 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.2829` → IC=+0.185 (n=52)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2829 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `1.7889` → IC=+0.134 (n=222)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.7889 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `1151.5637` → IC=+0.150 (n=341)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1151.5637 (IC base=+0.096)

- **PATRÓN** `ibs_20min` < `0.7041` → IC=+0.152 (n=133)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.7041 (IC base=+0.005)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0103` → IC=-0.245 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0103
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=150)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.242 (n=122)

- **PATRÓN** `ibs_20min` > `0.7647` → IC=+0.178 (n=259)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.7647 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` > `0.7192` → IC=+0.132 (n=104)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` > 0.7192 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` > `0.2443` → IC=+0.183 (n=77)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2443 (IC base=+0.054)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.157 (n=132)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0084 (IC base=+0.047)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.242 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2 (IC base=+0.047)

- **PATRÓN** `dist_vwap_pct` > `0.1153` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1153 (IC base=+0.047)

- **PATRÓN** `dist_vwap_pct` < `0.1816` → IC=+0.145 (n=119)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1816 (IC base=+0.047)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.04` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.04 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.0754` → IC=+0.300 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0754 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` < `2.1886` → IC=+0.174 (n=87)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 2.1886 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` > `1.4788` → IC=+0.189 (n=88)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.4788 (IC base=+0.047)

### GBM_LATE_60M_FADE
- **FILTRO** `dist_vwap_pct` > `0.2352` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2352
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=234)

- **FILTRO** `volumen_regimen` < `0.7425` → IC=-0.359 (n=62)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7425
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=188)

- **FILTRO** `volumen_spike_ratio` > `2.9817` → IC=-0.189 (n=43)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.9817
  - _Potencial_: sin este filtro IC_bueno=-0.137 (n=133)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.206 (n=49)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=201)

- **FILTRO** `sigma_h` > `0.0054` → IC=-0.377 (n=55)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0054
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=166)

- **FILTRO** `dist_vwap_pct` > `0.3156` → IC=-0.392 (n=35)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3156
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=186)

- **FILTRO** `sigma_ewma_delta_pct` > `10.676` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 10.676
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=197)

- **FILTRO** `volumen_pendiente_norm` > `0.0538` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0538
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=110)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` < `0.0034` → IC=-0.238 (n=40)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=41)

- **FILTRO** `hora_utc` < `5.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=46)

- **FILTRO** `ibs_20min` < `0.0864` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0864
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=55)

- **FILTRO** `volumen_regimen` < `0.8402` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8402
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=61)

- **FILTRO** `volumen_regimen` > `0.8359` → IC=-0.340 (n=23)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8359
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=71)

- **FILTRO** `volumen_spike_ratio` > `1.5538` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.5538
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=31)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.5872` → IC=-0.466 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5872
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=55)

- **FILTRO** `hora_utc` < `5.0` → IC=-0.350 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.258 (n=64)

- **FILTRO** `ibs_20min` > `0.791` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` > 0.791
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=55)

- **FILTRO** `volumen_spike_ratio` > `2.0968` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.0968
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=34)

- **PATRÓN** `ibs_20min` > `0.9583` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9583 (IC base=-0.167)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=71)

- **FILTRO** `volumen_spike_ratio` < `1.5474` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.5474
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=47)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=61)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=30)

- **FILTRO** `dist_vwap_pct` < `0.219` → IC=-0.346 (n=24)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.219
  - _Potencial_: sin este filtro IC_bueno=-0.283 (n=21)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=23)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.172 (n=178)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0057 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.137 (n=188)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 15.0 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.6592` → IC=+0.144 (n=389)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.6592 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.4722` → IC=+0.196 (n=90)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.4722 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `0.657` → IC=+0.144 (n=130)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.657 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` < `0.1711` → IC=+0.121 (n=286)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1711 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `2.5286` → IC=+0.128 (n=288)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 2.5286 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.131 (n=139)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 17.0 (IC base=+0.077)

- **PATRÓN** `ibs_20min` < `0.1558` → IC=+0.166 (n=348)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.1558 (IC base=+0.077)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.636` → IC=+0.196 (n=90)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.636 (IC base=+0.077)

- **PATRÓN** `libro_liquidez` > `2756.8049` → IC=+0.139 (n=264)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2756.8049 (IC base=+0.077)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6472` → IC=-0.256 (n=39)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6472
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=117)

- **PATRÓN** `sigma_h` > `0.0024` → IC=+0.177 (n=159)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0024 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.194 (n=60)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.141 (n=62)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.1524` → IC=+0.189 (n=178)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.1524 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.0856` → IC=+0.145 (n=184)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.0856 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.645` → IC=+0.180 (n=145)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 4.645 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `0.6861` → IC=+0.158 (n=159)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.6861 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` < `0.1846` → IC=+0.182 (n=146)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` < 0.1846 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.6699` → IC=+0.185 (n=147)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 2.6699 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.4468` → IC=+0.164 (n=147)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.4468 (IC base=+0.140)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1654` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1654
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=104)

- **FILTRO** `libro_liquidez` < `1526.5273` → IC=-0.174 (n=41)

  - _Acción_: SKIP cuando `libro_liquidez` < 1526.5273
  - _Potencial_: sin este filtro IC_bueno=+0.127 (n=124)

- **FILTRO** `ibs_20min` > `0.3236` → IC=-0.167 (n=46)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3236
  - _Potencial_: sin este filtro IC_bueno=+0.138 (n=139)

- **PATRÓN** `volumen_spike_ratio` < `1.8285` → IC=+0.127 (n=65)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.8285 (IC base=+0.051)

- **PATRÓN** `libro_liquidez` > `1526.5273` → IC=+0.127 (n=124)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 1526.5273 (IC base=+0.051)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.122 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 8.0 (IC base=+0.061)

- **PATRÓN** `ibs_20min` < `0.3236` → IC=+0.138 (n=139)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.3236 (IC base=+0.061)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.429` → IC=+0.306 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.429 (IC base=+0.061)

- **PATRÓN** `volumen_regimen` < `0.6541` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6541 (IC base=+0.061)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `volumen_pendiente_norm` < `0.0968` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0968
  - _Potencial_: sin este filtro IC_bueno=+0.194 (n=34)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.275 (n=100)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.254 (n=136)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.229)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.230 (n=150)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` > `0.9298` → IC=+0.243 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9298 (IC base=+0.229)

- **PATRÓN** `dist_vwap_pct` > `0.6339` → IC=+0.342 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6339 (IC base=+0.229)

- **PATRÓN** `dist_vwap_pct` < `0.1348` → IC=+0.234 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1348 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.349` → IC=+0.283 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.349 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` < `1.0151` → IC=+0.267 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0151 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.311 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` < `1.4907` → IC=+0.364 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4907 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `2.1536` → IC=+0.278 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1536 (IC base=+0.229)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.232 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.0968` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0968 (IC base=-0.042)

### LATE_WINDOW_5MIN
- **PATRÓN** `drift_ventana_pct` |x|> `0.4522` → IC=+0.333 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4522 (IC base=+0.288)

- **PATRÓN** `elapsed_s` > `189.2` → IC=+0.360 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 189.2 (IC base=+0.288)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.447 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.8028` → IC=+0.367 (n=43)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8028 (IC base=+0.288)

- **PATRÓN** `ballena_activa_n` < `1158.0` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1158.0 (IC base=+0.288)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3418` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3418 (IC base=+0.192)

- **PATRÓN** `elapsed_s` > `182.9` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `elapsed_s` > 182.9 (IC base=+0.192)

- **PATRÓN** `elapsed_s` < `209.7` → IC=+0.227 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 209.7 (IC base=+0.192)

- **PATRÓN** `drift_15min` |x|≤ `1.3142` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.3142 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.6424` → IC=+0.265 (n=32)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6424 (IC base=+0.192)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.280 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.192)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.260 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.192)

### LATE_WINDOW_5MIN#BTC#5min
- **PATRÓN** `drift_ventana_pct` |x|> `0.4522` → IC=+0.333 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4522 (IC base=+0.288)

- **PATRÓN** `elapsed_s` > `189.2` → IC=+0.360 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 189.2 (IC base=+0.288)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.447 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.8028` → IC=+0.367 (n=43)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8028 (IC base=+0.288)

- **PATRÓN** `ballena_activa_n` < `1158.0` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1158.0 (IC base=+0.288)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3418` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3418 (IC base=+0.192)

- **PATRÓN** `elapsed_s` > `182.9` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `elapsed_s` > 182.9 (IC base=+0.192)

- **PATRÓN** `elapsed_s` < `209.7` → IC=+0.227 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 209.7 (IC base=+0.192)

- **PATRÓN** `drift_15min` |x|≤ `1.3142` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.3142 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.6424` → IC=+0.265 (n=32)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6424 (IC base=+0.192)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.280 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.192)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.260 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.192)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.125 (n=992)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `2947.9372` → IC=+0.153 (n=341)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2947.9372 (IC base=+0.105)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.125 (n=992)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `2947.9372` → IC=+0.153 (n=341)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2947.9372 (IC base=+0.105)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=150)

- **FILTRO** `libro_liquidez` < `10077.5355` → IC=-0.185 (n=109)

  - _Acción_: SKIP cuando `libro_liquidez` < 10077.5355
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=57)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=235)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=221)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=49)

- **FILTRO** `hora_utc` < `3.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=53)

- **FILTRO** `libro_liquidez` < `10893.2451` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 10893.2451
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=52)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.188 (n=14)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=25)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=2625)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=95)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=95)

- **FILTRO** `ballena_activa_n` > `555.0` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `ballena_activa_n` > 555.0
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=62)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.188 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.132 (n=104)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.132 (n=104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 15.0 (IC base=+0.059)

- **PATRÓN** `libro_liquidez` > `2582.0434` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2582.0434 (IC base=+0.059)

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

- **PATRÓN** `liq_usd_total` > `68754.71` → IC=+0.147 (n=134)

  - _Acción_: Kelly boost +0.74€ cuando `liq_usd_total` > 68754.71 (IC base=+0.047)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.145 (n=170)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.495 (IC base=+0.047)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=1013)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=967)

- **FILTRO** `liq_usd_total` < `9664.41` → IC=-0.231 (n=24)

  - _Acción_: SKIP cuando `liq_usd_total` < 9664.41
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9855` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9855
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=17)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.292 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `ballena_activa_n` > `142.0` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 142.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=604)

- **FILTRO** `liq_n` < `8.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `liq_n` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **FILTRO** `liq_usd_total` < `24810.11` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `liq_usd_total` < 24810.11
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

### LIQUIDACIONES_5M#XRP#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=322)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.152 (n=116)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.495 (IC base=+0.029)

- **PATRÓN** `libro_liquidez` > `3976.0824` → IC=+0.141 (n=115)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 3976.0824 (IC base=+0.029)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=763)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=763)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=525)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=525)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=210)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=210)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.136 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=172)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.122 (n=88)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=137)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=132)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=156)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=242)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=127)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=140)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=296)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=296)

- **FILTRO** `libro_liquidez` < `480.724` → IC=-0.139 (n=81)

  - _Acción_: SKIP cuando `libro_liquidez` < 480.724
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=245)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=192)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.141 (n=678)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=1667)

- **PATRÓN** `py_entrada` < `0.47` → IC=+0.147 (n=564)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.47 (IC base=+0.019)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.52` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `py_entrada` < 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=10)

- **FILTRO** `py_entrada` > `0.45` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

- **FILTRO** `restante_min` < `3.89` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `restante_min` < 3.89
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

- **FILTRO** `lag_apertura_s` > `66.61` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `lag_apertura_s` > 66.61
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.52` → IC=-0.128 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.151 (n=61)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.224 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.46 (IC base=+0.044)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.173 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=103)

- **FILTRO** `restante_min` < `8.28` → IC=-0.150 (n=38)

  - _Acción_: SKIP cuando `restante_min` < 8.28
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=115)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.160 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=105)

- **FILTRO** `lag_apertura_s` > `402.96` → IC=-0.150 (n=38)

  - _Acción_: SKIP cuando `lag_apertura_s` > 402.96
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=115)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `lag_apertura_s` > `60.75` → IC=-0.122 (n=117)

  - _Acción_: SKIP cuando `lag_apertura_s` > 60.75
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=40)

- **PATRÓN** `py_entrada` < `0.54` → IC=+0.141 (n=37)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.54 (IC base=+0.071)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `lag_apertura_s` > `133.19` → IC=-0.141 (n=104)

  - _Acción_: SKIP cuando `lag_apertura_s` > 133.19
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=105)

- **FILTRO** `profundidad_ratio` < `53.7` → IC=-0.200 (n=68)

  - _Acción_: SKIP cuando `profundidad_ratio` < 53.7
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=141)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.250 (n=42)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=176)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.134 (n=170)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=97)

- **FILTRO** `restante_min` < `3.4` → IC=-0.219 (n=87)

  - _Acción_: SKIP cuando `restante_min` < 3.4
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=180)

- **FILTRO** `lag_apertura_s` > `94.28` → IC=-0.217 (n=90)

  - _Acción_: SKIP cuando `lag_apertura_s` > 94.28
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=177)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **PATRÓN** `lag_apertura_s` < `95.05` → IC=+0.141 (n=76)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 95.05 (IC base=+0.000)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **PATRÓN** `py_entrada` < `0.49` → IC=+0.125 (n=78)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.49 (IC base=+0.004)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.139 (n=167)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.156 (n=91)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.156 (n=91)

  - _Acción_: Kelly boost +0.78€ cuando `py_entrada` > 0.5 (IC base=-0.035)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.194 (n=83)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=234)

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

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1413)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.475` → IC=-0.163 (n=4647)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=14039)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.165 (n=4812)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=14507)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.193 (n=821)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=2490)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.149 (n=804)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=2653)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.173 (n=837)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=2526)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.180 (n=876)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=2629)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.164 (n=793)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=2519)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2225)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2485)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=3225)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.172 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=412)

- **FILTRO** `libro_liquidez` < `16920.0467` → IC=-0.163 (n=176)

  - _Acción_: SKIP cuando `libro_liquidez` < 16920.0467
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=359)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `libro_liquidez` < `3613.7014` → IC=-0.152 (n=110)

  - _Acción_: SKIP cuando `libro_liquidez` < 3613.7014
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=224)

- **FILTRO** `py_entrada` > `0.615` → IC=-0.216 (n=86)

  - _Acción_: SKIP cuando `py_entrada` > 0.615
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=289)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=798)

- **FILTRO** `libro_liquidez` < `1967.9764` → IC=-0.169 (n=330)

  - _Acción_: SKIP cuando `libro_liquidez` < 1967.9764
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=671)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=232)

### MOMENTUM_IBS_5M#BNB#5min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=40)

- **FILTRO** `drift_7min_pct` |x|> `0.0331` → IC=-0.158 (n=36)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0331
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=19)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0331` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_7min_pct` |x|≤ 0.0331 (IC base=-0.026)

### MOMENTUM_IBS_5M#BTC#5min
- **FILTRO** `hora_utc` > `18.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=90)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.200 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.043)

### MOMENTUM_IBS_5M#DOGE#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=38)

### MOMENTUM_IBS_5M#ETH#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=414)

### MOMENTUM_IBS_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=631)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `8.0` → IC=-0.131 (n=13003)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=29044)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=9867)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=32180)

- **FILTRO** `ibs_7min` < `0.2617` → IC=-0.235 (n=10511)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2617
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=31536)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.154 (n=14166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=27881)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.236 (n=12921)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=40476)

- **FILTRO** `ibs_7min` > `0.2889` → IC=-0.179 (n=13338)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2889
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=40059)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.142 (n=2111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=5039)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.309 (n=1704)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=5446)

- **FILTRO** `ibs_7min` < `0.7097` → IC=-0.253 (n=2359)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7097
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=4791)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.186 (n=1561)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=5589)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.267 (n=2251)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=7001)

- **FILTRO** `ibs_7min` > `0.7821` → IC=-0.210 (n=2312)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7821
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=6940)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.132 (n=1709)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=5483)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.249 (n=1765)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=5427)

- **FILTRO** `ibs_7min` < `0.7415` → IC=-0.197 (n=1797)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7415
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=5395)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.179 (n=1797)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=5395)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.265 (n=1733)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=5576)

- **FILTRO** `ibs_7min` > `0.2655` → IC=-0.193 (n=1827)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2655
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=5482)

- **FILTRO** `ballena_activa_n` > `150.0` → IC=-0.191 (n=1820)

  - _Acción_: SKIP cuando `ballena_activa_n` > 150.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=5489)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.165 (n=1682)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=5113)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.317 (n=1612)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=5183)

- **FILTRO** `ibs_7min` < `0.7042` → IC=-0.247 (n=2242)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7042
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=4553)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.218 (n=1544)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5251)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.243 (n=2243)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=7616)

- **FILTRO** `ibs_7min` > `0.7391` → IC=-0.172 (n=2463)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7391
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=7396)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=2233)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=4679)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.238 (n=2051)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=4861)

- **FILTRO** `ibs_7min` < `0.7407` → IC=-0.185 (n=1728)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7407
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5184)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.183 (n=1718)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=5194)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.268 (n=1759)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=5362)

- **FILTRO** `ibs_7min` > `0.2755` → IC=-0.183 (n=1780)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2755
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=5341)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.183 (n=1739)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=5382)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.272 (n=1649)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=5465)

- **FILTRO** `ibs_7min` < `0.25` → IC=-0.233 (n=1749)

  - _Acción_: SKIP cuando `ibs_7min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=5365)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.183 (n=2408)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=7779)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.276 (n=1635)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=5249)

- **FILTRO** `ibs_7min` < `0.2511` → IC=-0.224 (n=1721)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2511
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=5163)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.199 (n=1694)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=5190)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.206 (n=2384)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=7285)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.153 (n=295)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=962)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=1242)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.139 (n=164)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=499)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1156)

- **FILTRO** `libro_liquidez` < `7936.4939` → IC=-0.130 (n=347)

  - _Acción_: SKIP cuando `libro_liquidez` < 7936.4939
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=706)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=355)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.226 (n=49)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=409)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.129 (n=68)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=589)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=251)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.134 (n=925)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.135 (n=423)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 14.0 (IC base=+0.121)

- **PATRÓN** `total_vol_5m` < `442.4725` → IC=+0.149 (n=309)

  - _Acción_: Kelly boost +0.75€ cuando `total_vol_5m` < 442.4725 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.128 (n=783)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 52.0 (IC base=+0.121)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.438` → IC=+0.162 (n=72)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio` |x|> 0.438 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.226 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `2614.7862` → IC=+0.216 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2614.7862 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.184 (n=93)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 11.0 (IC base=+0.141)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.156 (n=59)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 8.0 (IC base=+0.104)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4139` → IC=+0.172 (n=126)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.86€ cuando `delta_ratio` |x|> 0.4139 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.208 (n=63)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.111)

- **PATRÓN** `total_vol_5m` < `385.7846` → IC=+0.206 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 385.7846 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.182 (n=83)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 73.0 (IC base=+0.111)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3985` → IC=+0.179 (n=166)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.89€ cuando `delta_ratio` |x|> 0.3985 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.192 (n=76)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 6.0 (IC base=+0.146)

- **PATRÓN** `total_vol_5m` < `7882.091` → IC=+0.167 (n=166)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 7882.091 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.173 (n=53)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 28.0 (IC base=+0.146)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `libro_spread` < `0.01` → IC=+0.190 (n=111)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `3599.4239` → IC=+0.167 (n=82)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3599.4239 (IC base=+0.095)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.6961` → IC=-0.238 (n=40)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.6961
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=122)

- **FILTRO** `sigma_h` > `0.0044` → IC=-0.232 (n=345)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0044
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=179)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.005` → IC=-0.243 (n=103)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.005
  - _Potencial_: sin este filtro IC_bueno=+0.255 (n=51)

- **FILTRO** `T_h` > `88.6528` → IC=-0.400 (n=38)

  - _Acción_: SKIP cuando `T_h` > 88.6528
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=116)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.255 (n=51)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=-0.077)

- **PATRÓN** `pct_vs_K` |x|≤ `1.7678` → IC=+0.148 (n=52)

  - _Acción_: Kelly boost +0.74€ cuando `pct_vs_K` |x|≤ 1.7678 (IC base=-0.077)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0056` → IC=-0.128 (n=41)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0056
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=15)

- **FILTRO** `pct_vs_K` |x|> `8.3214` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.3214
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=37)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0061` → IC=-0.185 (n=71)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0061
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=24)

- **FILTRO** `T_h` < `39.9942` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `T_h` < 39.9942
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=72)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0048` → IC=-0.178 (n=119)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=360)

- **FILTRO** `T_h` > `71.8388` → IC=-0.157 (n=359)

  - _Acción_: SKIP cuando `T_h` > 71.8388
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=120)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.309 (n=103)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.252 (n=313)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.321 (n=104)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.248 (n=312)

- **FILTRO** `T_h` > `57.7851` → IC=-0.311 (n=311)

  - _Acción_: SKIP cuando `T_h` > 57.7851
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=105)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `87.6255` → IC=-0.143 (n=110)

  - _Acción_: SKIP cuando `T_h` > 87.6255
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=55)

- **FILTRO** `pct_vs_K` |x|> `2.7902` → IC=-0.384 (n=41)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7902
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=124)

- **FILTRO** `sigma_h` > `0.0057` → IC=-0.318 (n=75)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0057
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=77)

- **FILTRO** `T_h` > `143.1632` → IC=-0.311 (n=51)

  - _Acción_: SKIP cuando `T_h` > 143.1632
  - _Potencial_: sin este filtro IC_bueno=-0.277 (n=101)

- **FILTRO** `T_h` < `95.9199` → IC=-0.327 (n=50)

  - _Acción_: SKIP cuando `T_h` < 95.9199
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=102)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `T_h` < `139.5329` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `T_h` < 139.5329
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

- **FILTRO** `sigma_h` < `0.0085` → IC=-0.239 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

- **FILTRO** `T_h` > `144.5457` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` > 144.5457
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` > `135.986` → IC=-0.288 (n=31)

  - _Acción_: SKIP cuando `T_h` > 135.986
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=101)

- **FILTRO** `T_h` < `87.9918` → IC=-0.278 (n=43)

  - _Acción_: SKIP cuando `T_h` < 87.9918
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=89)

- **FILTRO** `sigma_h` > `0.0088` → IC=-0.348 (n=31)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0088
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=95)

- **FILTRO** `sigma_h` < `0.0049` → IC=-0.318 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0049
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=95)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` > `0.006` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `T_h` < `145.7969` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` < 145.7969
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0078` → IC=-0.177 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0078
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=89)

- **FILTRO** `T_h` > `113.0501` → IC=-0.150 (n=58)

  - _Acción_: SKIP cuando `T_h` > 113.0501
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=60)

- **FILTRO** `sigma_h` > `0.0077` → IC=-0.345 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0077
  - _Potencial_: sin este filtro IC_bueno=-0.267 (n=28)

- **FILTRO** `T_h` > `41.2311` → IC=-0.375 (n=62)

  - _Acción_: SKIP cuando `T_h` > 41.2311
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=22)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1246` → IC=+0.470 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1246 (IC base=+0.353)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.380 (n=73)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0073 (IC base=+0.353)

- **PATRÓN** `T_h` < `0.5477` → IC=+0.386 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.5477 (IC base=+0.353)

- **PATRÓN** `T_h` > `1.202` → IC=+0.426 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.202 (IC base=+0.353)

- **PATRÓN** `dist_50` > `0.3302` → IC=+0.440 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3302 (IC base=+0.353)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.375 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.353)

- **PATRÓN** `edge` > `0.095` → IC=+0.455 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.095 (IC base=+0.423)

- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.434 (n=59)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0074 (IC base=+0.423)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.450 (n=119)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.423)

- **PATRÓN** `T_h` < `0.5967` → IC=+0.435 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.5967 (IC base=+0.423)

- **PATRÓN** `T_h` > `1.4774` → IC=+0.452 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4774 (IC base=+0.423)

- **PATRÓN** `dist_50` > `0.3811` → IC=+0.483 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3811 (IC base=+0.423)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.476 (n=121)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.423)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1026` → IC=+0.454 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1026 (IC base=+0.425)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.413 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.425)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.457 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.425)

- **PATRÓN** `T_h` < `1.0313` → IC=+0.454 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.0313 (IC base=+0.425)

- **PATRÓN** `T_h` > `0.4508` → IC=+0.417 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4508 (IC base=+0.425)

- **PATRÓN** `dist_50` > `0.4122` → IC=+0.477 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4122 (IC base=+0.425)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.417 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.438 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.425)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.1975` → IC=+0.479 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1975 (IC base=+0.439)

- **PATRÓN** `sigma_h` < `0.0161` → IC=+0.458 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0161 (IC base=+0.439)

- **PATRÓN** `T_h` > `0.7758` → IC=+0.454 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7758 (IC base=+0.439)

- **PATRÓN** `dist_50` > `0.354` → IC=+0.458 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.354 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.433 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.439)

- **PATRÓN** `edge` > `0.1155` → IC=+0.472 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1155 (IC base=+0.465)

- **PATRÓN** `sigma_h` < `0.0149` → IC=+0.483 (n=118)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0149 (IC base=+0.465)

- **PATRÓN** `T_h` > `0.77` → IC=+0.467 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.77 (IC base=+0.465)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.491 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.465)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.469 (n=128)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.465)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=246)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=334)

- **FILTRO** `streak_estiramiento` > `0.7643` → IC=-0.124 (n=99)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.7643
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=194)

- **PATRÓN** `streak_estiramiento` < `0.5782` → IC=+0.151 (n=147)

  - _Acción_: Kelly boost +0.76€ cuando `streak_estiramiento` < 0.5782 (IC base=+0.035)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=25)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=55)

- **FILTRO** `volumen_racha` > `935008.9` → IC=-0.141 (n=37)

  - _Acción_: SKIP cuando `volumen_racha` > 935008.9
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=38)

- **FILTRO** `streak_estiramiento` > `0.4881` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4881
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=52)

- **PATRÓN** `volumen_racha` < `935008.9` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_racha` < 935008.9 (IC base=+0.006)

- **PATRÓN** `streak_estiramiento` < `0.4177` → IC=+0.133 (n=47)

  - _Acción_: Kelly boost +0.66€ cuando `streak_estiramiento` < 0.4177 (IC base=+0.006)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.130 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 10.0 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.130 (n=98)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 48.0 (IC base=+0.068)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=88)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=94)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=37)

- **FILTRO** `streak_estiramiento` > `1.1202` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_estiramiento` > 1.1202
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=32)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=25)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=820)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=562)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` > `3.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=14)

- **FILTRO** `libro_liquidez` < `2775.6672` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_liquidez` < 2775.6672
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### STREAK_FADE_60M#ETH#60min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=784)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1319)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=936)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=931)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3434)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1793)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.204 (n=782)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.198)

- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.236 (n=782)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.1587` → IC=+0.204 (n=2064)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1587 (IC base=+0.198)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2215` → IC=+0.208 (n=782)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2215 (IC base=+0.198)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1293` → IC=+0.226 (n=887)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1293 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.204 (n=2185)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.199 (n=2414)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.198)

- **PATRÓN** `ibs_15` > `0.6129` → IC=+0.276 (n=2347)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6129 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.1189` → IC=+0.200 (n=1173)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1189 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.921` → IC=+0.277 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.921 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `7342.6348` → IC=+0.207 (n=782)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7342.6348 (IC base=+0.198)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=1004)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.229 (n=418)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.0582` → IC=+0.270 (n=159)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0582 (IC base=+0.213)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1464` → IC=+0.236 (n=316)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1464 (IC base=+0.213)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1443` → IC=+0.257 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1443 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.240 (n=444)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.213)

- **PATRÓN** `ibs_15` > `0.7141` → IC=+0.276 (n=475)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7141 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `0.3824` → IC=+0.263 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3824 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.367` → IC=+0.271 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.367 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `16196.8854` → IC=+0.245 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16196.8854 (IC base=+0.213)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.513` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.513
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=594)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.186 (n=173)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0034 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.0673` → IC=+0.158 (n=229)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.0673 (IC base=+0.145)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2347` → IC=+0.174 (n=173)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio_macro` |x|> 0.2347 (IC base=+0.145)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1251` → IC=+0.168 (n=197)

  - _Acción_: Kelly boost +0.84€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1251 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.160 (n=374)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 11.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.148 (n=543)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 17.0 (IC base=+0.145)

- **PATRÓN** `ibs_15` > `0.5778` → IC=+0.243 (n=519)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5778 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.153` → IC=+0.147 (n=290)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.153 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.2646` → IC=+0.151 (n=480)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.2646 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.546` → IC=+0.229 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.546 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `3469.9204` → IC=+0.158 (n=463)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3469.9204 (IC base=+0.145)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `20.909` → IC=-0.133 (n=28)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 20.909
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=190)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.262 (n=107)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0085 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.189` → IC=+0.201 (n=322)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.189 (IC base=+0.167)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0757` → IC=+0.171 (n=287)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.86€ cuando `delta_ratio_macro` |x|> 0.0757 (IC base=+0.167)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3457` → IC=+0.214 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3457 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.181 (n=214)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 12.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.170 (n=331)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 17.0 (IC base=+0.167)

- **PATRÓN** `ibs_15` > `0.5455` → IC=+0.256 (n=322)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5455 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.1299` → IC=+0.178 (n=181)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1299 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` < `0.33` → IC=+0.174 (n=317)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.33 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.263` → IC=+0.308 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.263 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.186 (n=205)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `2478.4536` → IC=+0.184 (n=321)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2478.4536 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.188 (n=248)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 36.0 (IC base=+0.167)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.256` → IC=+0.154 (n=53)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 8.256 (IC base=+0.003)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.251 (n=521)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.0798` → IC=+0.215 (n=258)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0798 (IC base=+0.210)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0439` → IC=+0.214 (n=583)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0439 (IC base=+0.210)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0888` → IC=+0.264 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0888 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.239 (n=289)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.210)

- **PATRÓN** `ibs_15` > `0.5854` → IC=+0.290 (n=583)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5854 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` > `0.3547` → IC=+0.217 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3547 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.493` → IC=+0.240 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.493 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.374` → IC=+0.213 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.374 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2945.7354` → IC=+0.292 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2945.7354 (IC base=+0.210)

- **PATRÓN** `ibs_15` < `0.1136` → IC=+0.154 (n=631)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.77€ cuando `ibs_15` < 0.1136 (IC base=+0.066)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.364 (n=351)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.357)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.363 (n=525)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0027 (IC base=+0.357)

- **PATRÓN** `drift_60min` |x|≤ `0.1109` → IC=+0.358 (n=351)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1109 (IC base=+0.357)

- **PATRÓN** `drift_15min` |x|≤ `0.4034` → IC=+0.360 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4034 (IC base=+0.357)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1493` → IC=+0.381 (n=350)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1493 (IC base=+0.357)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1344` → IC=+0.393 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1344 (IC base=+0.357)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.374 (n=530)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.357)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.394 (n=525)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.357)

- **PATRÓN** `dist_vwap_pct` > `0.4172` → IC=+0.387 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4172 (IC base=+0.357)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.252` → IC=+0.371 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.252 (IC base=+0.357)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.364 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.357)

- **PATRÓN** `libro_liquidez` > `3823.0046` → IC=+0.370 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3823.0046 (IC base=+0.357)

- **PATRÓN** `ballena_activa_n` < `443.0` → IC=+0.377 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 443.0 (IC base=+0.357)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.362 (n=252)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.359)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.367 (n=96)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.359)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.367 (n=96)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.359)

- **PATRÓN** `drift_15min` |x|≤ `0.5086` → IC=+0.360 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5086 (IC base=+0.359)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1529` → IC=+0.380 (n=190)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1529 (IC base=+0.359)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1332` → IC=+0.393 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1332 (IC base=+0.359)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.379 (n=288)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.359)

- **PATRÓN** `ibs_15` > `0.8057` → IC=+0.389 (n=286)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8057 (IC base=+0.359)

- **PATRÓN** `dist_vwap_pct` > `0.3926` → IC=+0.397 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3926 (IC base=+0.359)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.575` → IC=+0.367 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.575 (IC base=+0.359)

- **PATRÓN** `libro_liquidez` > `16049.8465` → IC=+0.388 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16049.8465 (IC base=+0.359)

- **PATRÓN** `ballena_activa_n` < `500.0` → IC=+0.410 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 500.0 (IC base=+0.359)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.352 (n=106)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.354)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.374 (n=109)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.354)

- **PATRÓN** `drift_60min` |x|≤ `0.1062` → IC=+0.364 (n=160)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1062 (IC base=+0.354)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.370 (n=214)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.354)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.378 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.354)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.414 (n=115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.354)

- **PATRÓN** `ibs_15` > `0.7574` → IC=+0.401 (n=240)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7574 (IC base=+0.354)

- **PATRÓN** `dist_vwap_pct` > `0.4449` → IC=+0.365 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4449 (IC base=+0.354)

- **PATRÓN** `dist_vwap_pct` < `0.2797` → IC=+0.355 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2797 (IC base=+0.354)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.939` → IC=+0.372 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.939 (IC base=+0.354)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.587` → IC=+0.353 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.587 (IC base=+0.354)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.360 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.354)

- **PATRÓN** `libro_liquidez` > `4204.0039` → IC=+0.378 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4204.0039 (IC base=+0.354)

- **PATRÓN** `ballena_activa_n` < `147.0` → IC=+0.359 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 147.0 (IC base=+0.354)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0121` → IC=-0.225 (n=862)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0121
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=2587)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.204 (n=1267)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=2182)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1405` → IC=+0.183 (n=553)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.91€ cuando `delta_ratio_macro` |x|> 0.1405 (IC base=-0.065)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1366` → IC=+0.241 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1366 (IC base=-0.065)

- **PATRÓN** `ibs_15` > `0.6364` → IC=+0.279 (n=830)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6364 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` > `0.1051` → IC=+0.199 (n=479)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1051 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` < `0.4113` → IC=+0.199 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4113 (IC base=-0.065)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1271` → IC=+0.256 (n=1769)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1271 (IC base=-0.018)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3195` → IC=+0.249 (n=2593)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3195 (IC base=-0.018)

- **PATRÓN** `ibs_15` < `0.3499` → IC=+0.277 (n=2654)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3499 (IC base=-0.018)

- **PATRÓN** `dist_vwap_pct` > `0.857` → IC=+0.296 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.857 (IC base=-0.018)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.215 (n=496)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=1490)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.229 (n=496)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=1490)

- **FILTRO** `sigma_ewma_delta_pct` > `23.724` → IC=-0.266 (n=284)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.724
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=1702)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.183 (n=197)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0027 (IC base=+0.086)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1979` → IC=+0.289 (n=112)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1979 (IC base=+0.086)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1373` → IC=+0.302 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1373 (IC base=+0.086)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.121 (n=404)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 12.0 (IC base=+0.086)

- **PATRÓN** `ibs_15` > `0.7533` → IC=+0.327 (n=246)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7533 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.1012` → IC=+0.294 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1012 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` < `0.4975` → IC=+0.290 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4975 (IC base=+0.086)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.533` → IC=+0.126 (n=287)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` > 8.533 (IC base=+0.086)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0613` → IC=+0.223 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0613 (IC base=-0.192)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1779` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1779 (IC base=-0.192)

- **PATRÓN** `ibs_15` < `0.5625` → IC=+0.333 (n=40)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.5625 (IC base=-0.192)

- **PATRÓN** `dist_vwap_pct` < `0.0474` → IC=+0.305 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0474 (IC base=-0.192)

- **PATRÓN** `ballena_activa_n` < `291.0` → IC=+0.438 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 291.0 (IC base=-0.192)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.165 (n=527)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.160 (n=360)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0058 (IC base=+0.156)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.163 (n=408)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0034 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.0735` → IC=+0.209 (n=180)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0735 (IC base=+0.156)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1408` → IC=+0.157 (n=272)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.78€ cuando `delta_ratio_macro` |x|> 0.1408 (IC base=+0.156)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2902` → IC=+0.213 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2902 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.179 (n=291)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 11.0 (IC base=+0.156)

- **PATRÓN** `ibs_15` > `0.6489` → IC=+0.261 (n=408)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6489 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` < `0.2628` → IC=+0.168 (n=380)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.2628 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.12` → IC=+0.214 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.12 (IC base=+0.156)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.165 (n=527)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `11295.4184` → IC=+0.174 (n=136)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 11295.4184 (IC base=+0.156)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.249 (n=424)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.3509` → IC=+0.241 (n=847)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3509 (IC base=+0.238)

- **PATRÓN** `drift_15min` |x|≤ `0.7642` → IC=+0.248 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7642 (IC base=+0.238)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2096` → IC=+0.265 (n=437)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2096 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.242 (n=851)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.238)

- **PATRÓN** `ibs_15` < `0.3605` → IC=+0.270 (n=963)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3605 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `0.7312` → IC=+0.295 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7312 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.315` → IC=+0.255 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.315 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.498` → IC=+0.242 (n=1011)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.498 (IC base=+0.238)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1702` → IC=-0.238 (n=273)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1702
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=535)

- **FILTRO** `drift_15min` |x|> `0.8825` → IC=-0.269 (n=201)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8825
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=607)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.214 (n=341)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.144 (n=467)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1455` → IC=+0.174 (n=44)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio_macro` |x|> 0.1455 (IC base=-0.174)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.226 (n=60)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.174)

- **PATRÓN** `dist_vwap_pct` > `0.2752` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.2752 (IC base=-0.174)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1292 (IC base=-0.174)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.221 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.174)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0787` → IC=+0.237 (n=382)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0787 (IC base=-0.039)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1879` → IC=+0.232 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1879 (IC base=-0.039)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.274 (n=428)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.6467` → IC=+0.239 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6467 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` < `0.172` → IC=+0.237 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.172 (IC base=-0.039)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0193` → IC=-0.257 (n=484)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0193
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=485)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.252 (n=313)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=656)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.201)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.201)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1479` → IC=+0.280 (n=302)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1479 (IC base=-0.029)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1101` → IC=+0.314 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1101 (IC base=-0.029)

- **PATRÓN** `ibs_15` < `0.3256` → IC=+0.293 (n=665)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3256 (IC base=-0.029)

- **PATRÓN** `dist_vwap_pct` > `0.8075` → IC=+0.350 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8075 (IC base=-0.029)

### UPDOWN_GBM_ETH_15M_HORA7
- **FILTRO** `ibs_15` < `0.8434` → IC=-0.167 (n=19)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8434
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=11)

- **PATRÓN** `dist_vwap_pct` > `0.1511` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1511 (IC base=+0.034)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **FILTRO** `ibs_15` < `0.8434` → IC=-0.167 (n=19)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8434
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=11)

- **PATRÓN** `dist_vwap_pct` > `0.1511` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1511 (IC base=+0.034)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.297 (n=566)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.292)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.292 (n=759)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.0529` → IC=+0.325 (n=283)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0529 (IC base=+0.292)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2389` → IC=+0.300 (n=283)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2389 (IC base=+0.292)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2214` → IC=+0.315 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2214 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.313 (n=884)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.292)

- **PATRÓN** `ibs_15` > `0.8393` → IC=+0.326 (n=848)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8393 (IC base=+0.292)

- **PATRÓN** `dist_vwap_pct` > `0.4275` → IC=+0.332 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4275 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.63` → IC=+0.349 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.63 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `12836.5354` → IC=+0.309 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12836.5354 (IC base=+0.292)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.300 (n=203)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.327 (n=154)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.286)

- **PATRÓN** `drift_15min` |x|≤ `0.4172` → IC=+0.285 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4172 (IC base=+0.286)

- **PATRÓN** `delta_ratio_macro` |x|> `0.252` → IC=+0.314 (n=154)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.252 (IC base=+0.286)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1428` → IC=+0.305 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1428 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.307 (n=486)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.286)

- **PATRÓN** `ibs_15` > `0.83` → IC=+0.314 (n=461)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.83 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.2573` → IC=+0.338 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2573 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.469` → IC=+0.362 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.469 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `16220.2116` → IC=+0.333 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16220.2116 (IC base=+0.286)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.305 (n=259)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.299)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.305 (n=387)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.299)

- **PATRÓN** `drift_60min` |x|≤ `0.1077` → IC=+0.312 (n=259)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1077 (IC base=+0.299)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2883` → IC=+0.320 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2883 (IC base=+0.299)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.327 (n=374)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.299)

- **PATRÓN** `ibs_15` > `0.8527` → IC=+0.338 (n=387)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8527 (IC base=+0.299)

- **PATRÓN** `dist_vwap_pct` > `0.2764` → IC=+0.311 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2764 (IC base=+0.299)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.266` → IC=+0.330 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.266 (IC base=+0.299)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0876` → IC=-0.253 (n=75)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0876
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=226)

- **FILTRO** `sigma_h` > `0.0043` → IC=-0.260 (n=102)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0043
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=199)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.187 (n=113)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=345)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0682` → IC=-0.145 (n=60)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0682
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=117)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.126` → IC=-0.174 (n=44)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.126
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=133)

- **FILTRO** `drift_15min` |x|> `0.3691` → IC=-0.265 (n=15)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3691
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=32)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1819` → IC=-0.260 (n=23)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1819
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=24)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2665` → IC=-0.156 (n=30)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2665
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=16)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2122` → IC=-0.395 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2122
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0775` → IC=-0.292 (n=22)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0775
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `sigma_h` > `0.0046` → IC=-0.222 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0046
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=12)

### UPDOWN_OU_5M#XRP#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1195` → IC=-0.206 (n=15)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1195
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `sigma_h` > `0.006` → IC=-0.265 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

- **FILTRO** `drift_15min` |x|> `0.3593` → IC=-0.206 (n=15)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3593
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.3119` → IC=-0.184 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.3119
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `81.6124` → IC=+0.233 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 81.6124 (IC base=+0.218)

- **PATRÓN** `ratio` < `0.9766` → IC=+0.473 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9766 (IC base=+0.218)

- **PATRÓN** `T_h` > `145.7419` → IC=+0.388 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7419 (IC base=+0.335)

- **PATRÓN** `ratio` > `1.0104` → IC=+0.318 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0104 (IC base=+0.335)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `126.1277` → IC=+0.252 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 126.1277 (IC base=+0.201)

- **PATRÓN** `ratio` < `0.973` → IC=+0.458 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.201)

- **PATRÓN** `T_h` > `104.0063` → IC=+0.293 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 104.0063 (IC base=+0.287)

- **PATRÓN** `ratio` > `1.0479` → IC=+0.400 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0479 (IC base=+0.287)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `83.3501` → IC=+0.268 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.249)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.433 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.249)

- **PATRÓN** `T_h` > `111.9558` → IC=+0.345 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9558 (IC base=+0.321)

- **PATRÓN** `ratio` > `1.0131` → IC=+0.357 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0131 (IC base=+0.321)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1131` → IC=+0.457 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1131 (IC base=+0.401)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6129 sube el IC de +0.198 a +0.276 en UPDOWN_GBM#15min (n=2347). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7141 sube el IC de +0.213 a +0.276 en UPDOWN_GBM#BTC#15min (n=475). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5778 sube el IC de +0.145 a +0.243 en UPDOWN_GBM#ETH#15min (n=519). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.5455 sube el IC de +0.167 a +0.256 en UPDOWN_GBM#SOL#15min (n=322). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5854 sube el IC de +0.210 a +0.290 en UPDOWN_GBM#XRP#15min (n=583). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1136 sube el IC de +0.066 a +0.154 en UPDOWN_GBM#XRP#15min (n=631). Ya aplicado como kelly_boost=+0.77€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6364 sube el IC de -0.065 a +0.279 en UPDOWN_GBM_15M_TARDIO (n=830). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3499 sube el IC de -0.018 a +0.277 en UPDOWN_GBM_15M_TARDIO (n=2654). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7533 sube el IC de +0.086 a +0.327 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=246). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.5625 sube el IC de -0.192 a +0.333 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=40). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6489 sube el IC de +0.156 a +0.261 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=408). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3605 sube el IC de +0.238 a +0.270 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=963). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.174 a +0.226 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=60). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.039 a +0.274 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=428). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.201 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3256 sube el IC de -0.029 a +0.293 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=665). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8393 sube el IC de +0.292 a +0.326 en UPDOWN_GBM_IBS_ALTO (n=848). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.83 sube el IC de +0.286 a +0.314 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=461). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8527 sube el IC de +0.299 a +0.338 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=387). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.357 a +0.394 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=525). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8057 sube el IC de +0.359 a +0.389 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=286). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7574 sube el IC de +0.354 a +0.401 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=240). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1538 | +0.097 | +193.06€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1538 | +0.097 | +193.06€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1170 | +0.103 | +164.64€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1170 | +0.103 | +164.64€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 265 | +0.069 | +12.71€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 265 | +0.069 | +12.71€ | 6 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 72 | +0.108 | +16.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 72 | +0.108 | +16.05€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 182 | +0.033 | +41.15€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 182 | +0.033 | +41.15€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 149 | +0.030 | +37.36€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 149 | +0.030 | +37.36€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 11 | +0.106 | +1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 11 | +0.106 | +1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 22 | -0.042 | +2.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 22 | -0.042 | +2.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 33906 | -0.086 | -4543.37€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1718 | -0.016 | -220.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 32188 | -0.089 | -4322.84€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4348 | -0.121 | -761.00€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4348 | -0.121 | -761.00€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1718 | -0.016 | -220.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1718 | -0.016 | -220.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3962 | -0.114 | -903.36€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3962 | -0.114 | -903.36€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 8788 | -0.000 | -839.28€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 8788 | -0.000 | -839.28€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 8516 | -0.104 | -595.00€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 8516 | -0.104 | -595.00€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 6574 | -0.153 | -1224.20€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 6574 | -0.153 | -1224.20€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 25773 | -0.020 | +3766.35€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 6670 | +0.002 | +1767.44€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 19103 | -0.028 | +1998.91€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 25773 | -0.020 | +3766.35€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 6670 | +0.002 | +1767.44€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 19103 | -0.028 | +1998.91€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 116077 | +0.114 | -5159.42€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 16265 | +0.183 | -488.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 492 | -0.049 | -60.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 92112 | +0.103 | -4336.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 7208 | +0.104 | -273.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 15297 | +0.103 | -1077.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 54 | -0.143 | +10.84€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 15228 | +0.104 | -1076.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 23014 | +0.130 | -376.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4872 | +0.197 | -135.96€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 15276 | +0.116 | -147.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2824 | +0.091 | -71.37€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 15343 | +0.094 | -1230.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 61 | -0.119 | -6.11€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 15267 | +0.095 | -1213.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 24654 | +0.125 | -411.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 6579 | +0.176 | -98.20€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 15445 | +0.107 | -252.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2618 | +0.100 | -52.25€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 22454 | +0.114 | -1228.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4643 | +0.189 | -270.01€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 395 | -0.011 | -7.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 15650 | +0.094 | -801.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1766 | +0.130 | -149.69€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#XRP | 15315 | +0.102 | -834.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 56 | -0.035 | +10.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 15246 | +0.102 | -845.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 18521 | +0.194 | -1157.05€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 18521 | +0.194 | -1157.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4300 | +0.174 | -401.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4300 | +0.174 | -401.72€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1992 | +0.203 | -28.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1992 | +0.203 | -28.45€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 4241 | +0.182 | -342.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 4241 | +0.182 | -342.71€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3729 | +0.242 | -129.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3729 | +0.242 | -129.03€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4180 | +0.189 | -268.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4180 | +0.189 | -268.90€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 868 | +0.428 | -28.73€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 868 | +0.428 | -28.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 343 | +0.433 | -6.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 343 | +0.433 | -6.97€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 327 | +0.433 | -6.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 327 | +0.433 | -6.27€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 186 | +0.404 | -13.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 186 | +0.404 | -13.04€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 64321 | +0.200 | -4778.31€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 64321 | +0.200 | -4778.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 11064 | +0.183 | -1179.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 11064 | +0.183 | -1179.13€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 10347 | +0.224 | -354.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 10347 | +0.224 | -354.42€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 11064 | +0.176 | -1242.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 11064 | +0.176 | -1242.26€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 10405 | +0.221 | -383.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 10405 | +0.221 | -383.14€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 10655 | +0.203 | -702.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 10655 | +0.203 | -702.96€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 10786 | +0.194 | -916.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 10786 | +0.194 | -916.40€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 24480 | +0.117 | +167.71€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 24480 | +0.117 | +167.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 12156 | +0.120 | +151.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 12156 | +0.120 | +151.39€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 12324 | +0.113 | +16.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 12324 | +0.113 | +16.32€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1747 | +0.289 | -21.11€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1747 | +0.289 | -21.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 789 | +0.279 | -18.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 789 | +0.279 | -18.88€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 841 | +0.289 | -6.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 841 | +0.289 | -6.45€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 117 | +0.349 | +4.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 117 | +0.349 | +4.22€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 783 | +0.439 | -0.05€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 783 | +0.439 | -0.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 376 | +0.436 | -2.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 376 | +0.436 | -2.61€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 361 | +0.442 | +2.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 361 | +0.442 | +2.01€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1343 | +0.072 | -57.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 486 | +0.059 | -37.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 857 | +0.079 | -19.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1052 | +0.078 | -26.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 195 | +0.074 | -7.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 857 | +0.079 | -19.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 225 | +0.033 | -32.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 225 | +0.033 | -32.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 46921 | +0.100 | -1216.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3810 | +0.092 | +47.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 43111 | +0.100 | -1264.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 26031 | +0.104 | -296.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3810 | +0.092 | +47.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 22221 | +0.106 | -344.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 9277 | +0.110 | -17.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 9277 | +0.110 | -17.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 11613 | +0.081 | -903.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 11613 | +0.081 | -903.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 867 | +0.205 | -102.15€ | 3 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 867 | +0.205 | -102.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 867 | +0.205 | -102.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 867 | +0.205 | -102.15€ | 3 | 4 |
| ✅ GBM_LATE_15M | 32856 | +0.089 | +16328.60€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 32856 | +0.089 | +16328.60€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 5526 | +0.203 | +4265.30€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 5526 | +0.203 | +4265.30€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 4866 | +0.178 | +3495.08€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 4866 | +0.178 | +3495.08€ | 0 | 26 |
| ✅ GBM_LATE_15M#DOGE | 5835 | +0.201 | +4414.67€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 5835 | +0.201 | +4414.67€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 4661 | +0.033 | +1175.27€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4661 | +0.033 | +1175.27€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 4684 | -0.030 | +1028.19€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 4684 | -0.030 | +1028.19€ | 4 | 12 |
| ✅ GBM_LATE_15M#XRP | 7284 | -0.036 | +1950.10€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 7284 | -0.036 | +1950.10€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 35495 | +0.087 | +18861.44€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 35495 | +0.087 | +18861.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 6862 | +0.012 | +3542.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 6862 | +0.012 | +3542.29€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 7350 | +0.013 | +1566.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 7350 | +0.013 | +1566.79€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 5012 | +0.268 | +5151.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 5012 | +0.268 | +5151.52€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 5994 | +0.011 | +1319.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 5994 | +0.011 | +1319.33€ | 1 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 5780 | +0.035 | +2306.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 5780 | +0.035 | +2306.89€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4497 | +0.286 | +4974.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4497 | +0.286 | +4974.61€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 26308 | +0.175 | +20450.59€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 26308 | +0.175 | +20450.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3970 | +0.217 | +3337.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3970 | +0.217 | +3337.69€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 4142 | +0.150 | +3010.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 4142 | +0.150 | +3010.93€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 4173 | +0.215 | +3441.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 4173 | +0.215 | +3441.13€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 4420 | +0.139 | +3256.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 4420 | +0.139 | +3256.25€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 4931 | +0.123 | +3569.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 4931 | +0.123 | +3569.10€ | 0 | 27 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4672 | +0.212 | +3835.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4672 | +0.212 | +3835.50€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 7162 | +0.139 | +3433.73€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 7162 | +0.139 | +3433.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 340 | +0.140 | +187.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 340 | +0.140 | +187.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2119 | +0.146 | +1163.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2119 | +0.146 | +1163.22€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 375 | +0.142 | +175.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 375 | +0.142 | +175.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2186 | +0.156 | +1092.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2186 | +0.156 | +1092.99€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1605 | +0.107 | +574.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1605 | +0.107 | +574.20€ | 1 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 537 | +0.135 | +240.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 537 | +0.135 | +240.44€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 33088 | +0.180 | +25499.53€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 33088 | +0.180 | +25499.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 5264 | +0.231 | +4675.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 5264 | +0.231 | +4675.03€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 5110 | +0.148 | +3340.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 5110 | +0.148 | +3340.80€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 5533 | +0.228 | +4821.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 5533 | +0.228 | +4821.24€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 5380 | +0.136 | +3722.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 5380 | +0.136 | +3722.91€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 5842 | +0.123 | +4015.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 5842 | +0.123 | +4015.65€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 5959 | +0.215 | +4923.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 5959 | +0.215 | +4923.89€ | 0 | 23 |
| ✅ GBM_LATE_5M | 9012 | +0.177 | +6099.41€ | 1 | 30 |
| ✅ GBM_LATE_5M#5min | 9012 | +0.177 | +6099.41€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 835 | +0.229 | +729.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 835 | +0.229 | +729.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2111 | +0.169 | +1523.16€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2111 | +0.169 | +1523.16€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 992 | +0.176 | +650.38€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 992 | +0.176 | +650.38€ | 0 | 17 |
| ✅ GBM_LATE_5M#ETH | 2840 | +0.180 | +1869.25€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2840 | +0.180 | +1869.25€ | 0 | 28 |
| ✅ GBM_LATE_5M#SOL | 1122 | +0.173 | +744.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1122 | +0.173 | +744.62€ | 0 | 26 |
| ✅ GBM_LATE_5M#XRP | 1112 | +0.148 | +582.60€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1112 | +0.148 | +582.60€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2430 | +0.072 | +891.23€ | 0 | 11 |
| ✅ GBM_LATE_60M#60min | 2430 | +0.072 | +891.23€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 914 | +0.089 | +338.88€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 914 | +0.089 | +338.88€ | 0 | 11 |
| ✅ GBM_LATE_60M#ETH | 761 | +0.071 | +340.55€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 761 | +0.071 | +340.55€ | 1 | 9 |
| ✅ GBM_LATE_60M#SOL | 755 | +0.052 | +211.80€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 755 | +0.052 | +211.80€ | 2 | 11 |
| 🚫 GBM_LATE_60M_FADE | 471 | -0.238 | -12.07€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 471 | -0.238 | -12.07€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 175 | -0.217 | -6.54€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 175 | -0.217 | -6.54€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 164 | -0.229 | -0.38€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 164 | -0.229 | -0.38€ | 4 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 132 | -0.269 | -5.15€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 132 | -0.269 | -5.15€ | 6 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1045 | +0.086 | +262.11€ | 0 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1045 | +0.086 | +262.11€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 393 | +0.075 | +78.43€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 393 | +0.075 | +78.43€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 350 | +0.057 | +45.38€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 350 | +0.057 | +45.38€ | 3 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 302 | +0.135 | +138.31€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 302 | +0.135 | +138.31€ | 1 | 13 |
| ✅ LATE_WINDOW_5MIN | 127 | +0.244 | +103.44€ | 0 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 127 | +0.244 | +103.44€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 127 | +0.244 | +103.44€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 127 | +0.244 | +103.44€ | 0 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 2777 | +0.103 | +733.78€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2777 | +0.103 | +733.78€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2777 | +0.103 | +733.78€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2777 | +0.103 | +733.78€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 422 | -0.071 | -32.34€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 422 | -0.071 | -32.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 116 | -0.034 | -1.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 116 | -0.034 | -1.97€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 68 | -0.086 | -7.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 68 | -0.086 | -7.96€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 157 | -0.028 | -5.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 157 | -0.028 | -5.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 2826 | +0.024 | +81.40€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2826 | +0.024 | +81.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 140 | +0.042 | +2.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 140 | +0.042 | +2.02€ | 1 | 2 |
| ✅ LIQUIDACIONES_5M#BTC | 428 | +0.028 | +32.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 428 | +0.028 | +32.88€ | 4 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 201 | -0.022 | -6.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 201 | -0.022 | -6.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1062 | +0.031 | +30.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1062 | +0.031 | +30.97€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 644 | +0.020 | +5.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 644 | +0.020 | +5.71€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 351 | +0.021 | +15.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 351 | +0.021 | +15.93€ | 1 | 2 |
| ✅ LIQUIDACIONES_60M | 1383 | -0.045 | -30.11€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1383 | -0.045 | -30.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 396 | -0.043 | -14.17€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 396 | -0.043 | -14.17€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 454 | -0.024 | +0.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 454 | -0.024 | +0.33€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 533 | -0.065 | -16.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 533 | -0.065 | -16.27€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 4538 | -0.013 | +143.76€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 2155 | -0.017 | +45.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 2383 | -0.009 | +98.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 127 | -0.004 | +4.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 64 | +0.045 | +10.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 63 | -0.054 | -5.84€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 1117 | -0.004 | +40.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 531 | -0.012 | +8.17€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 586 | +0.003 | +32.29€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 515 | -0.015 | +20.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 255 | -0.025 | +3.27€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 260 | -0.004 | +17.01€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 928 | -0.034 | -20.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 427 | -0.050 | -27.32€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 501 | -0.021 | +6.88€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 888 | -0.011 | +39.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 434 | -0.009 | +25.21€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 454 | -0.013 | +14.36€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 963 | -0.006 | +59.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 444 | -0.004 | +26.10€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 519 | -0.007 | +33.44€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 14662 | -0.012 | -218.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14662 | -0.012 | -218.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 0 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 38005 | -0.004 | +1783.26€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 38005 | -0.004 | +1783.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 6768 | +0.024 | +903.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 6768 | +0.024 | +903.53€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 5677 | -0.033 | -97.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 5677 | -0.033 | -97.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 6868 | +0.019 | +683.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 6868 | +0.019 | +683.68€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 5474 | -0.052 | -165.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 5474 | -0.052 | -165.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 6408 | -0.009 | +191.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 6408 | -0.009 | +191.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 6810 | +0.012 | +267.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 6810 | +0.012 | +267.63€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6168 | -0.059 | -144.88€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6168 | -0.059 | -144.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1218 | +0.001 | -13.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1218 | +0.001 | -13.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1522 | -0.077 | -32.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1522 | -0.077 | -32.57€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 709 | -0.126 | -34.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 709 | -0.126 | -34.50€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1818 | -0.077 | -33.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1818 | -0.077 | -33.66€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 856 | -0.015 | -25.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 856 | -0.015 | -25.00€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3351 | +0.004 | -2.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3351 | +0.004 | -2.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 191 | +0.018 | +1.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 191 | +0.018 | +1.53€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 137 | -0.004 | -2.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 137 | -0.004 | -2.36€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1319 | +0.006 | +5.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1319 | +0.006 | +5.66€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1388 | +0.007 | +0.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1388 | +0.007 | +0.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 95444 | -0.073 | +1641.57€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 95444 | -0.073 | +1641.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 16402 | -0.074 | +897.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 16402 | -0.074 | +897.14€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 14501 | -0.098 | -778.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 14501 | -0.098 | -778.65€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 16654 | -0.066 | +913.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 16654 | -0.066 | +913.94€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 14033 | -0.095 | -412.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 14033 | -0.095 | -412.76€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 17301 | -0.052 | +328.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 17301 | -0.052 | +328.98€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 16553 | -0.064 | +692.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 16553 | -0.064 | +692.91€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8061 | -0.031 | -149.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8061 | -0.031 | -149.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1920 | -0.043 | -18.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1920 | -0.043 | -18.51€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2242 | -0.025 | -30.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2242 | -0.025 | -30.43€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1115 | -0.049 | -23.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1115 | -0.049 | -23.18€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 780 | -0.022 | -24.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 780 | -0.022 | -24.72€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1368 | +0.115 | +500.40€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1232 | +0.121 | +487.80€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 288 | +0.141 | +148.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 288 | +0.141 | +148.99€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 233 | +0.104 | +62.96€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 233 | +0.104 | +62.96€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 250 | +0.111 | +95.03€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 250 | +0.111 | +95.03€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 221 | +0.146 | +115.32€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 221 | +0.146 | +115.32€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 240 | +0.095 | +65.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 240 | +0.095 | +65.50€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 913 | -0.017 | -23.00€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 913 | -0.017 | -23.00€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 181 | +0.008 | +9.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 181 | +0.008 | +9.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 131 | -0.011 | -1.89€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 131 | -0.011 | -1.89€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 243 | -0.043 | -20.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 243 | -0.043 | -20.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 200 | +0.010 | +2.06€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 200 | +0.010 | +2.06€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 158 | -0.044 | -11.35€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 158 | -0.044 | -11.35€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 753 | -0.092 | -72.24€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 344 | -0.144 | -82.11€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 264 | -0.188 | -74.97€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 80 | +0.000 | -7.14€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 267 | -0.050 | -2.77€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 188 | -0.053 | -3.54€ | 2 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 79 | -0.043 | +0.77€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 142 | -0.042 | +12.63€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 113 | -0.057 | +7.23€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 29 | +0.016 | +5.41€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 565 | -0.117 | -71.28€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 188 | -0.016 | -0.96€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 895 | -0.202 | -53.85€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 372 | -0.195 | -33.02€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 317 | -0.199 | -33.81€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 55 | -0.167 | +0.79€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 302 | -0.217 | -32.10€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 258 | -0.227 | -37.67€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 44 | -0.152 | +5.58€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 221 | -0.191 | +11.27€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 202 | -0.186 | +8.13€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 19 | -0.204 | +3.14€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 777 | -0.206 | -63.36€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 118 | -0.175 | +9.51€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 366 | +0.405 | +299.63€ | 0 | 13 |
| ✅ RESOLUTION_SNIPER#BTC | 40 | +0.119 | -1.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 40 | +0.119 | -1.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 95 | +0.376 | +78.12€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 95 | +0.376 | +78.12€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 231 | +0.461 | +222.74€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 231 | +0.461 | +222.74€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 366 | +0.405 | +299.63€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 618 | +0.029 | +19.55€ | 3 | 1 |
| ✅ STREAK_FADE_15M#15min | 618 | +0.029 | +19.55€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 295 | +0.022 | +2.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 295 | +0.022 | +2.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 46 | +0.042 | -0.04€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 46 | +0.042 | -0.04€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 65 | -0.007 | -1.72€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 65 | -0.007 | -1.72€ | 2 | 0 |
| ✅ STREAK_FADE_15M#XRP | 212 | +0.047 | +19.00€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 212 | +0.047 | +19.00€ | 3 | 4 |
| ✅ STREAK_FADE_5M | 3084 | -0.021 | -121.90€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3084 | -0.021 | -121.90€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 907 | -0.020 | -31.15€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 907 | -0.020 | -31.15€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 579 | -0.027 | -25.73€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 579 | -0.027 | -25.73€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1442 | -0.017 | -50.61€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1442 | -0.017 | -50.61€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 88 | -0.056 | -9.21€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 88 | -0.056 | -9.21€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 50 | -0.019 | -4.76€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 50 | -0.019 | -4.76€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 9692 | +0.019 | +107.23€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 9692 | +0.019 | +107.23€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2629 | +0.021 | +27.79€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2629 | +0.021 | +27.79€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2293 | +0.028 | +51.26€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2293 | +0.028 | +51.26€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2861 | +0.010 | -0.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2861 | +0.010 | -0.81€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1909 | +0.021 | +28.99€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1909 | +0.021 | +28.99€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 8734 | +0.013 | -44.71€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 8734 | +0.013 | -44.71€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3453 | +0.017 | -9.06€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3453 | +0.017 | -9.06€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3454 | +0.012 | -22.27€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3454 | +0.012 | -22.27€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1827 | +0.008 | -13.38€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1827 | +0.008 | -13.38€ | 1 | 0 |
| ✅ UPDOWN_GBM | 56866 | +0.045 | +4357.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 14169 | +0.080 | +2999.71€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 1875 | +0.005 | +8.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 37348 | +0.038 | +1301.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 3275 | +0.006 | +48.06€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 5841 | +0.081 | +794.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1154 | +0.156 | +503.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 41 | -0.035 | -1.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 4646 | +0.064 | +293.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 10975 | +0.050 | +876.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1815 | +0.089 | +411.38€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 498 | +0.012 | +5.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 7103 | +0.053 | +414.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1485 | +0.006 | +41.70€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 74 | -0.079 | +2.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 6794 | +0.055 | +571.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1129 | +0.142 | +419.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 38 | +0.000 | -1.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 5627 | +0.038 | +153.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 12442 | +0.035 | +684.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3425 | +0.057 | +461.87€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 491 | +0.007 | +8.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 7349 | +0.033 | +210.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1112 | +0.004 | -1.09€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 65 | -0.112 | +3.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 12636 | +0.023 | +458.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 3350 | +0.033 | +287.59€ | 0 | 13 |
| ✅ UPDOWN_GBM#SOL#240min | 481 | -0.001 | -0.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 8069 | +0.023 | +169.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 678 | +0.010 | +7.45€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 58 | -0.150 | -5.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 8176 | +0.052 | +974.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3296 | +0.100 | +915.39€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 326 | +0.006 | -1.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 4554 | +0.021 | +60.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 197 | -0.113 | +1.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 700 | +0.357 | +239.04€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 700 | +0.357 | +239.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 381 | +0.359 | +125.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 381 | +0.359 | +125.94€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 319 | +0.354 | +113.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 319 | +0.354 | +113.10€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 15770 | -0.028 | +3676.22€ | 2 | 9 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 15770 | -0.028 | +3676.22€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1257 | -0.054 | +422.49€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1257 | -0.054 | +422.49€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2770 | -0.113 | +117.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2770 | -0.113 | +117.58€ | 3 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 698 | +0.207 | +543.51€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 698 | +0.207 | +543.51€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1827 | +0.213 | +1158.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1827 | +0.213 | +1158.13€ | 1 | 20 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 4599 | -0.063 | +615.31€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 4599 | -0.063 | +615.31€ | 3 | 10 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 4619 | -0.066 | +819.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 4619 | -0.066 | +819.20€ | 2 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 176 | +0.028 | +6.95€ | 1 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 176 | +0.028 | +6.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 176 | +0.028 | +6.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 176 | +0.028 | +6.95€ | 1 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1130 | +0.292 | +931.54€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1130 | +0.292 | +931.54€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 614 | +0.286 | +467.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 614 | +0.286 | +467.96€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 516 | +0.299 | +463.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 516 | +0.299 | +463.59€ | 0 | 8 |
| ✅ UPDOWN_OU_5M | 759 | -0.115 | -86.15€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#5min | 759 | -0.115 | -86.15€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 224 | -0.088 | -18.30€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 224 | -0.088 | -18.30€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 73 | -0.167 | -9.78€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 73 | -0.167 | -9.78€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 83 | -0.194 | -8.02€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 83 | -0.194 | -8.02€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 34 | -0.194 | -7.31€ | 4 | 0 |
| ✅ WEEKLY_PRICE | 2929 | +0.306 | +1438.10€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1040 | +0.260 | +155.34€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1121 | +0.299 | +491.94€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 768 | +0.378 | +790.81€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.023 n=704 — no justifica filtro, seguir monitorizando
  - _Datos_: n=704 IC=+0.023 PNL=+34.66€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 614 celda(s) pasan gate riguroso completo de 2454 evaluadas (n>=40) y 3430 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.032 < 0.08 — monitorear
  - _Datos_: n=3346 IC=+0.032 PNL=+285.14€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1121/15 IC=+0.299 PNL=+491.94€ | BTC: n=1040/15 IC=+0.260 PNL=+155.34€ | SOL: n=768/15 IC=+0.378 PNL=+790.81€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 30 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
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
  - _Estado_: alineada_con_outcome_prev IC=+0.129 n=545/60 | contraria IC=+0.192 n=554 | gap=-0.064 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=377, boost estimado=+0.007. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1112/40 IC=+0.004 PNL=-1.09€ | BTC#60min: n=1485/40 IC=+0.006 PNL=+41.70€ | SOL#60min: n=678/40 IC=+0.010 PNL=+7.45€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.049 n=434814 | tras_1loss IC=+0.088 n=333653 | tras_2loss IC=+0.057 n=137245/40 | gap=-0.009 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.210 > 0.08 con n=463 PNL=+362.92€
  - _Datos_: n=463 IC=+0.210 PNL=+362.92€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.209 > 0.08 con n=548 PNL=+401.56€
  - _Datos_: n=548 IC=+0.209 PNL=+401.56€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.198 > 0.08 con n=51 PNL=+31.30€
  - _Datos_: n=51 IC=+0.198 PNL=+31.30€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.331 > 0.1 con n=2390 PNL=+1299.17€
  - _Datos_: n=2390 IC=+0.331 PNL=+1299.17€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=459 IC=+0.073 PNL=+52.02€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=459 IC=+0.073 PNL=+52.02€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=66 IC=+0.176 PNL=+41.61€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=66 IC=+0.176 PNL=+41.61€

**⏳ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: 30
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 4/15 ops en el filtro definido (IC actual=+0.067 PNL=+7.14€)
  - _Datos_: n=4 IC=+0.067 PNL=+7.14€

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
  - _Estado_: n=2217 IC=+0.011 PNL=+12.22€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2217 IC=+0.011 PNL=+12.22€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1058 IC=-0.005 PNL=+35.84€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1058 IC=-0.005 PNL=+35.84€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=704 IC=+0.023 PNL=+34.66€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=704 IC=+0.023 PNL=+34.66€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.198 > 0.1 con n=3126 PNL=+2168.02€
  - _Datos_: n=3126 IC=+0.198 PNL=+2168.02€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1814 IC=+0.089 PNL=+410.88€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1814 IC=+0.089 PNL=+410.88€

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
  - _Estado_: n=732 IC=+0.025 PNL=+58.96€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=732 IC=+0.025 PNL=+58.96€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=77 IC=+0.057 PNL=+4.75€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=77 IC=+0.057 PNL=+4.75€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.244 n=127) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=127 IC=+0.244 PNL=+103.44€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.120 > 0.02 con n=785 PNL=+304.78€
  - _Datos_: n=785 IC=+0.120 PNL=+304.78€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=191 IC=-0.070 PNL=+27.59€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=191 IC=-0.070 PNL=+27.59€

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
  - _Estado_: n=21214 IC=+0.069 PNL=+2936.63€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=21214 IC=+0.069 PNL=+2936.63€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.144 < -0.1 con n=338 PNL=+34.89€
  - _Datos_: n=338 IC=-0.144 PNL=+34.89€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2516 IC=+0.066 PNL=+300.00€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2516 IC=+0.066 PNL=+300.00€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=107 IC=-0.115 PNL=+4.82€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=107 IC=-0.115 PNL=+4.82€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.116 > 0.1 con n=607 PNL=+155.48€
  - _Datos_: n=607 IC=+0.116 PNL=+155.48€

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
  - _Estado_: n=23803 IC=-0.136 PNL=+1721.92€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=23803 IC=-0.136 PNL=+1721.92€

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
  - _Estado_: n=2436 IC=+0.136 PNL=+1399.85€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2436 IC=+0.136 PNL=+1399.85€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=5797 IC=+0.038 PNL=+345.74€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=5797 IC=+0.038 PNL=+345.74€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.089 > 0.08 con n=2670 PNL=+1419.94€
  - _Datos_: n=2670 IC=+0.089 PNL=+1419.94€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.227 < -0.1 con n=2419 PNL=-198.46€
  - _Datos_: n=2419 IC=-0.227 PNL=-198.46€

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
  - _Estado_: n=50 IC=+0.000 PNL=+5.79€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=50 IC=+0.000 PNL=+5.79€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.101 n=1413) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1413 IC=+0.101 PNL=+319.35€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.409 n=495) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=495 IC=+0.409 PNL=+699.65€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=11057 IC=+0.183 PNL=-1177.59€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=11057 IC=+0.183 PNL=-1177.59€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.208 > 0.1 con n=176 PNL=+108.01€
  - _Datos_: n=176 IC=+0.208 PNL=+108.01€
