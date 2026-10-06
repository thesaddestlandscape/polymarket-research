# Hipótesis automáticas — 2026-10-06 08:28 UTC
_Generado por shadow_postmortem.py sobre 772887 resoluciones (PNL=+94288.01€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=575)

- **PATRÓN** `py_entrada` > `0.51` → IC=+0.236 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.51 (IC base=+0.128)

- **PATRÓN** `n_total_lado` > `70.0` → IC=+0.209 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 70.0 (IC base=+0.128)

- **PATRÓN** `banda_hit_calibrado` > `0.6284` → IC=+0.259 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6284 (IC base=+0.128)

- **PATRÓN** `banda_z` > `9.204` → IC=+0.183 (n=216)

  - _Acción_: Kelly boost +0.92€ cuando `banda_z` > 9.204 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.158 (n=220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=680)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `3098.2903` → IC=+0.131 (n=429)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 3098.2903 (IC base=+0.128)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=438)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.244 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.134)

- **PATRÓN** `n_total_lado` > `42.0` → IC=+0.164 (n=477)

  - _Acción_: Kelly boost +0.82€ cuando `n_total_lado` > 42.0 (IC base=+0.134)

- **PATRÓN** `banda_hit_calibrado` > `0.6168` → IC=+0.251 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6168 (IC base=+0.134)

- **PATRÓN** `banda_z` > `9.932` → IC=+0.201 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.932 (IC base=+0.134)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.903` → IC=+0.134 (n=419)

  - _Acción_: Kelly boost +0.67€ cuando `ballenas_wallet_edge_medio` > 0.903 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=535)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=582)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.134)

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
- **FILTRO** `restante_s_al_confirmar` < `143.77` → IC=-0.214 (n=8507)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 143.77
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=25529)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `130.69` → IC=-0.271 (n=1088)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.69
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=3264)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `124.32` → IC=-0.304 (n=994)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 124.32
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=2985)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `165.02` → IC=-0.224 (n=2139)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 165.02
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=6420)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `128.75` → IC=-0.309 (n=1651)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.75
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=4954)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.213 (n=16361)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.104)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=3901)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `5341.9699` → IC=+0.169 (n=2540)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 5341.9699 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.136 (n=14510)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.134 (n=17811)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.229 (n=13522)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.164 (n=6407)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7601.2069` → IC=+0.168 (n=2457)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 7601.2069 (IC base=+0.126)

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
- **PATRÓN** `py_entrada` > `0.555` → IC=+0.124 (n=1043)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.555 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `4587.7919` → IC=+0.121 (n=251)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 4587.7919 (IC base=+0.092)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.137 (n=441)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.089)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.134 (n=951)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.44 (IC base=+0.089)

- **PATRÓN** `libro_liquidez` > `5754.4405` → IC=+0.144 (n=234)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 5754.4405 (IC base=+0.089)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=3441)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.354 (n=1146)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.233 (n=1538)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` < `0.24` → IC=+0.362 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.24 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.228 (n=1784)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.223)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=854)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.143 (n=735)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.136)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.248 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=666)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `2151.7929` → IC=+0.154 (n=371)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2151.7929 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.075)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.238 (n=825)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.215)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.409 (n=997)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.156 (n=59)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.151 (n=1230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=655)
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

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.222 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.117)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.284 (n=132)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=68)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=14535)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.200 (n=13875)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.228 (n=6198)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.176 (n=3424)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.176 (n=3241)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.173)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.178 (n=3292)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.173)

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

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.239 (n=1351)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.233 (n=1426)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.232)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.321 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.232)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=3366)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.187 (n=3214)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.188 (n=2686)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.253 (n=2954)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.242)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.331 (n=1023)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=3287)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=2819)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.191 (n=2486)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.71 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.198 (n=1188)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.73 (IC base=+0.190)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.433 (n=597)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.428)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.427 (n=688)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.428)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.428)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.428)

- **PATRÓN** `libro_liquidez` > `2168.6864` → IC=+0.436 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2168.6864 (IC base=+0.428)

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
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.443 (n=227)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.433)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.433)

- **PATRÓN** `libro_liquidez` > `3371.5411` → IC=+0.446 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3371.5411 (IC base=+0.433)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.408 (n=128)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.405)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.407 (n=127)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.405)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.408 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.405)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.420 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.405)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=24)

- **FILTRO** `libro_liquidez` < `7880.4556` → IC=-0.344 (n=30)

  - _Acción_: SKIP cuando `libro_liquidez` < 7880.4556
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.203 (n=43255)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.243 (n=19069)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.185 (n=7451)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.185 (n=5995)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.198 (n=8239)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.71 (IC base=+0.183)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=3889)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.269 (n=4431)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.180 (n=7871)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 7.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.193 (n=7891)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.235 (n=3913)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.274 (n=2678)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.207 (n=7172)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.203 (n=5755)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.260 (n=2847)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.201 (n=3104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.244 (n=3303)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=6659)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` < `4.19` → IC=+0.125 (n=6163)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` < 4.19 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=6451)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=8235)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.47` → IC=+0.137 (n=6160)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.47 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=3327)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` < `4.16` → IC=+0.127 (n=3058)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.16 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.141 (n=3229)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.135 (n=4075)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `3.14` → IC=+0.146 (n=3054)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 3.14 (IC base=+0.120)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.188 (n=3332)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.113)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.130 (n=3532)

  - _Acción_: Kelly boost +0.65€ cuando `restante_min` > 4.96 (IC base=+0.113)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.135 (n=3112)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 2.25 (IC base=+0.113)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.301 (n=1397)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.380 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `4195.4603` → IC=+0.300 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4195.4603 (IC base=+0.288)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.291 (n=624)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.278)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.350 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `3803.5445` → IC=+0.288 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3803.5445 (IC base=+0.278)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.320 (n=448)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.288)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.295 (n=661)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.388 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `1438.1591` → IC=+0.304 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1438.1591 (IC base=+0.288)

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
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.443 (n=590)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.441 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.445 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.439)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.440 (n=701)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.439)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.443 (n=298)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.437)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.438 (n=289)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.438 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.446 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.437)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.459 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.442)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.442 (n=102)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.451 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.443 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.444 (n=318)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4836` → IC=+0.130 (n=10394)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.4836 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.9841` → IC=+0.243 (n=3465)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9841 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.374` → IC=+0.254 (n=2716)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.374 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.034` → IC=+0.183 (n=3935)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 6.034 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.2107` → IC=+0.250 (n=2908)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2107 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` > `0.6912` → IC=+0.258 (n=2599)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6912 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.3033` → IC=+0.227 (n=1056)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3033 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `2.3318` → IC=+0.219 (n=3299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3318 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.5652` → IC=+0.140 (n=12639)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.5652 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` > `0.7547` → IC=+0.204 (n=691)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7547 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` < `0.1474` → IC=+0.181 (n=4258)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.1474 (IC base=+0.071)

- **PATRÓN** `volumen_regimen` < `1.1974` → IC=+0.180 (n=4648)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 1.1974 (IC base=+0.071)

- **PATRÓN** `volumen_regimen` > `0.6254` → IC=+0.179 (n=4647)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 0.6254 (IC base=+0.071)

- **PATRÓN** `volumen_pendiente_norm` > `0.2953` → IC=+0.228 (n=1164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2953 (IC base=+0.071)

- **PATRÓN** `volumen_spike_ratio` > `1.5682` → IC=+0.202 (n=7103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5682 (IC base=+0.071)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.216 (n=7757)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.071)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.218 (n=781)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.178)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.185 (n=773)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.008 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.3497` → IC=+0.184 (n=2314)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.3497 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.193 (n=1125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 15.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.182 (n=1547)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 11.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.275 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.773` → IC=+0.293 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.773 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.230 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `1.4349` → IC=+0.180 (n=2187)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4349 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.193 (n=2385)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.04 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `2057.32` → IC=+0.183 (n=771)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2057.32 (IC base=+0.178)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.243 (n=1653)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.0883` → IC=+0.267 (n=617)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0883 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.258 (n=681)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.0583` → IC=+0.285 (n=814)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0583 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.523` → IC=+0.252 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.523 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.408` → IC=+0.238 (n=1935)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.408 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` < `0.0941` → IC=+0.234 (n=1628)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0941 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2841` → IC=+0.262 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2841 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.6178` → IC=+0.255 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6178 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=2030)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `1982.2745` → IC=+0.235 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1982.2745 (IC base=+0.235)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.241 (n=808)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.3507` → IC=+0.232 (n=1832)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3507 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.236 (n=1835)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `0.9785` → IC=+0.262 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9785 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `0.1891` → IC=+0.222 (n=961)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1891 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` < `0.3423` → IC=+0.224 (n=1710)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3423 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.769` → IC=+0.259 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.769 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` < `1.2495` → IC=+0.223 (n=1832)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2495 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `0.6169` → IC=+0.225 (n=1832)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6169 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.239 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.4178` → IC=+0.246 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4178 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.176 (n=615)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0026 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.161 (n=614)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.158 (n=702)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.139 (n=842)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.7237` → IC=+0.177 (n=1837)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.7237 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.1279` → IC=+0.154 (n=1663)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1279 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.348` → IC=+0.143 (n=292)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 11.348 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.3` → IC=+0.143 (n=1685)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.3 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `1.2035` → IC=+0.146 (n=1837)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.2035 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` > `0.6207` → IC=+0.136 (n=1838)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6207 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.0979` → IC=+0.166 (n=666)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0979 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.4573` → IC=+0.148 (n=1724)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4573 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.7857` → IC=+0.144 (n=1150)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.7857 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `230.0` → IC=+0.170 (n=725)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 230.0 (IC base=+0.135)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.201 (n=2338)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.196 (n=2462)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=2099)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.264 (n=902)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.356` → IC=+0.259 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.356 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.195 (n=2046)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.3499` → IC=+0.194 (n=312)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.3499 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `1.7667` → IC=+0.199 (n=2008)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.7667 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.197 (n=2795)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `2034.4` → IC=+0.200 (n=779)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2034.4 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.223 (n=1812)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.1771` → IC=+0.224 (n=907)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1771 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=782)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.217 (n=968)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` < `0.0645` → IC=+0.234 (n=908)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0645 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.697` → IC=+0.249 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.697 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.3473` → IC=+0.257 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3473 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.7283` → IC=+0.219 (n=848)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7283 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.7396` → IC=+0.228 (n=874)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7396 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `1956.6784` → IC=+0.215 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1956.6784 (IC base=+0.213)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.216 (n=1865)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.213)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.164 (n=126)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=2790)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.152 (n=443)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0036 (IC base=+0.042)

- **PATRÓN** `ibs_20min` > `0.9588` → IC=+0.223 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9588 (IC base=+0.042)

- **PATRÓN** `dist_vwap_pct` < `0.1865` → IC=+0.323 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1865 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.971` → IC=+0.175 (n=924)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 4.971 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` < `0.8553` → IC=+0.330 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8553 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` > `1.2251` → IC=+0.338 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2251 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.3037` → IC=+0.339 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3037 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` < `1.4291` → IC=+0.360 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4291 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` > `2.2171` → IC=+0.317 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2171 (IC base=+0.042)

- **PATRÓN** `ballena_activa_n` < `153.0` → IC=+0.323 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 153.0 (IC base=+0.042)

- **PATRÓN** `ibs_20min` < `0.0987` → IC=+0.161 (n=730)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.0987 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` > `0.4593` → IC=+0.201 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4593 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` < `0.8509` → IC=+0.156 (n=774)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8509 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.2877` → IC=+0.210 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2877 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` > `1.5312` → IC=+0.168 (n=989)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.5312 (IC base=+0.028)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.175 (n=75)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=427)

- **FILTRO** `ibs_20min` < `0.3103` → IC=-0.182 (n=124)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3103
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=378)

- **FILTRO** `ibs_20min` > `0.2308` → IC=-0.127 (n=2806)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2308
  - _Potencial_: sin este filtro IC_bueno=+0.137 (n=1397)

- **FILTRO** `sigma_ewma_delta_pct` > `8.773` → IC=-0.218 (n=438)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.773
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=3765)

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

- **PATRÓN** `ibs_20min` < `0.2308` → IC=+0.137 (n=1397)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.2308 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.1825` → IC=+0.270 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1825 (IC base=-0.039)

- **PATRÓN** `volumen_regimen` < `0.7017` → IC=+0.274 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7017 (IC base=-0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.161` → IC=+0.325 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.161 (IC base=-0.039)

- **PATRÓN** `volumen_spike_ratio` < `2.4034` → IC=+0.293 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4034 (IC base=-0.039)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6378` → IC=-0.176 (n=736)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6378
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=2211)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.210 (n=754)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2193)

- **FILTRO** `ibs_20min` > `0.7658` → IC=-0.207 (n=1092)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7658
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=3280)

- **PATRÓN** `dist_vwap_pct` > `0.4566` → IC=+0.310 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4566 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` < `0.2747` → IC=+0.312 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2747 (IC base=-0.070)

- **PATRÓN** `volumen_regimen` < `0.988` → IC=+0.296 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.988 (IC base=-0.070)

- **PATRÓN** `volumen_regimen` > `0.6476` → IC=+0.312 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6476 (IC base=-0.070)

- **PATRÓN** `volumen_pendiente_norm` < `0.1025` → IC=+0.302 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1025 (IC base=-0.070)

- **PATRÓN** `volumen_spike_ratio` < `2.4802` → IC=+0.299 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4802 (IC base=-0.070)

- **PATRÓN** `volumen_spike_ratio` > `1.8609` → IC=+0.299 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8609 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` > `0.8345` → IC=+0.285 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8345 (IC base=-0.013)

- **PATRÓN** `volumen_regimen` < `0.7241` → IC=+0.250 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7241 (IC base=-0.013)

- **PATRÓN** `volumen_regimen` > `1.0722` → IC=+0.279 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0722 (IC base=-0.013)

- **PATRÓN** `volumen_pendiente_norm` > `0.0991` → IC=+0.269 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0991 (IC base=-0.013)

- **PATRÓN** `volumen_spike_ratio` < `2.1607` → IC=+0.258 (n=878)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1607 (IC base=-0.013)

- **PATRÓN** `volumen_spike_ratio` > `1.4218` → IC=+0.257 (n=997)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4218 (IC base=-0.013)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.197 (n=4541)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0094 (IC base=+0.099)

- **PATRÓN** `ibs_20min` > `0.4693` → IC=+0.187 (n=12159)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4693 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.6799` → IC=+0.285 (n=1418)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6799 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.69` → IC=+0.154 (n=6158)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 3.69 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` < `1.1783` → IC=+0.247 (n=4977)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1783 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` > `0.6924` → IC=+0.256 (n=4445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6924 (IC base=+0.099)

- **PATRÓN** `volumen_pendiente_norm` < `0.081` → IC=+0.243 (n=7358)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.081 (IC base=+0.099)

- **PATRÓN** `volumen_pendiente_norm` > `0.2423` → IC=+0.255 (n=1514)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2423 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` < `1.4689` → IC=+0.242 (n=2676)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4689 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` > `2.6446` → IC=+0.256 (n=2676)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6446 (IC base=+0.099)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.275 (n=7582)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.099)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.165 (n=4389)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0089 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.5455` → IC=+0.158 (n=11574)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.5455 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.6796` → IC=+0.252 (n=776)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6796 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.1702` → IC=+0.251 (n=3635)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1702 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.7084` → IC=+0.250 (n=1751)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7084 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.1971` → IC=+0.260 (n=1325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1971 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2954` → IC=+0.308 (n=781)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2954 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.5928` → IC=+0.280 (n=2429)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5928 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.2862` → IC=+0.270 (n=2503)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2862 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.283 (n=5421)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 78.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2584` → IC=-0.165 (n=946)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2584
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=2840)

- **FILTRO** `ibs_20min` > `0.7572` → IC=-0.172 (n=778)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7572
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=2338)

- **FILTRO** `sigma_ewma_delta_pct` > `4.599` → IC=-0.172 (n=694)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.599
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=2422)

- **PATRÓN** `ibs_20min` > `0.9069` → IC=+0.273 (n=947)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9069 (IC base=+0.040)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.272` → IC=+0.200 (n=671)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.272 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.2273` → IC=+0.270 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2273 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` < `1.4426` → IC=+0.210 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4426 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` > `2.1959` → IC=+0.232 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1959 (IC base=+0.040)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.224 (n=841)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.2231` → IC=+0.438 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2231 (IC base=-0.022)

- **PATRÓN** `volumen_spike_ratio` < `2.6397` → IC=+0.428 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6397 (IC base=-0.022)

- **PATRÓN** `volumen_spike_ratio` > `1.5288` → IC=+0.424 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5288 (IC base=-0.022)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.436 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=-0.022)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8645` → IC=+0.160 (n=913)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.8645 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.1138` → IC=+0.194 (n=695)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1138 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` > `0.6783` → IC=+0.184 (n=1151)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 0.6783 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.2765` → IC=+0.219 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2765 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `1.4286` → IC=+0.196 (n=422)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4286 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` > `2.4426` → IC=+0.189 (n=422)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.4426 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `229.0` → IC=+0.231 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 229.0 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.1506` → IC=+0.227 (n=773)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1506 (IC base=-0.002)

- **PATRÓN** `volumen_regimen` > `0.613` → IC=+0.228 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.613 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` < `0.0738` → IC=+0.221 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0738 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2707` → IC=+0.304 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2707 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.4389` → IC=+0.233 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4389 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.1737` → IC=+0.236 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1737 (IC base=-0.002)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.006` → IC=+0.272 (n=2064)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.252)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.257 (n=2073)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.252)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.252 (n=2078)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.252)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=1072)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.252)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.781` → IC=+0.281 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.781 (IC base=+0.252)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.267 (n=1764)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.252)

- **PATRÓN** `volumen_spike_ratio` > `1.6253` → IC=+0.258 (n=1974)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6253 (IC base=+0.252)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.261 (n=2443)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.252)

- **PATRÓN** `libro_liquidez` > `2027.2693` → IC=+0.275 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2027.2693 (IC base=+0.252)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.325 (n=777)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.1799` → IC=+0.302 (n=755)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1799 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.320 (n=577)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.287)

- **PATRÓN** `ibs_20min` < `0.36` → IC=+0.292 (n=1714)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.36 (IC base=+0.287)

- **PATRÓN** `ibs_20min` > `0.1` → IC=+0.288 (n=1145)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.693` → IC=+0.298 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.693 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` < `0.1951` → IC=+0.283 (n=1666)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1951 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` > `0.1208` → IC=+0.293 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1208 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` < `1.7245` → IC=+0.301 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7245 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` > `2.6496` → IC=+0.293 (n=733)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6496 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1950.2584` → IC=+0.300 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1950.2584 (IC base=+0.287)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.289 (n=1407)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.287)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7664` → IC=-0.182 (n=788)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7664
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=2366)

- **PATRÓN** `ibs_20min` > `0.9013` → IC=+0.169 (n=719)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.9013 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.2109` → IC=+0.219 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2109 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `1.0122` → IC=+0.241 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0122 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.1712` → IC=+0.232 (n=990)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1712 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.4183` → IC=+0.263 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4183 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.287 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.1219` → IC=+0.236 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1219 (IC base=-0.003)

- **PATRÓN** `volumen_regimen` < `1.1974` → IC=+0.222 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1974 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2957` → IC=+0.282 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2957 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.845` → IC=+0.264 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.845 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.5184` → IC=+0.240 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5184 (IC base=-0.003)

- **PATRÓN** `ballena_activa_n` < `133.0` → IC=+0.257 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 133.0 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7632` → IC=-0.187 (n=1448)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7632
  - _Potencial_: sin este filtro IC_bueno=+0.285 (n=1452)

- **FILTRO** `ibs_20min` > `0.6696` → IC=-0.244 (n=728)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6696
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=2185)

- **FILTRO** `sigma_ewma_delta_pct` > `8.654` → IC=-0.229 (n=341)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.654
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=2572)

- **PATRÓN** `ibs_20min` > `0.7632` → IC=+0.285 (n=1452)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7632 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `1.0215` → IC=+0.335 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0215 (IC base=+0.049)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.668` → IC=+0.163 (n=455)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 9.668 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` < `0.8605` → IC=+0.311 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8605 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` > `0.6395` → IC=+0.305 (n=1105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6395 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.302 (n=1044)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.2757` → IC=+0.325 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2757 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` < `1.7975` → IC=+0.316 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7975 (IC base=+0.049)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.325 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.049)

- **PATRÓN** `ibs_20min` < `0.5692` → IC=+0.132 (n=1923)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5692 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` < `0.2686` → IC=+0.243 (n=788)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2686 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `0.7092` → IC=+0.268 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7092 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `1.1879` → IC=+0.232 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1879 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.0701` → IC=+0.267 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0701 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `2.4411` → IC=+0.251 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4411 (IC base=+0.022)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.264 (n=815)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.022)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.008` → IC=+0.326 (n=1644)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.008 (IC base=+0.286)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.306 (n=778)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.286)

- **PATRÓN** `ibs_20min` > `0.6494` → IC=+0.320 (n=1643)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6494 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.2118` → IC=+0.319 (n=955)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2118 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.77` → IC=+0.309 (n=817)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.77 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.947` → IC=+0.287 (n=1855)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.947 (IC base=+0.286)

- **PATRÓN** `volumen_regimen` > `0.6275` → IC=+0.299 (n=1643)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6275 (IC base=+0.286)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.336 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` > `1.4333` → IC=+0.299 (n=1569)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4333 (IC base=+0.286)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.289 (n=1595)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `2646.5003` → IC=+0.300 (n=1095)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2646.5003 (IC base=+0.286)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.322 (n=1365)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.286)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.318 (n=1163)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.1875` → IC=+0.288 (n=767)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1875 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.291 (n=1651)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.287)

- **PATRÓN** `ibs_20min` < `0.37` → IC=+0.311 (n=1743)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.37 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.3051` → IC=+0.294 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3051 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.512` → IC=+0.299 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.512 (IC base=+0.287)

- **PATRÓN** `volumen_regimen` > `1.2276` → IC=+0.318 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2276 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` > `0.2331` → IC=+0.334 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2331 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` < `1.4234` → IC=+0.295 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4234 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` > `2.1367` → IC=+0.286 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1367 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `2640.6397` → IC=+0.289 (n=1161)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2640.6397 (IC base=+0.287)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.187 (n=3392)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0047 (IC base=+0.174)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.208 (n=3383)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.3536` → IC=+0.185 (n=8926)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.3536 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=10582)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.5682` → IC=+0.227 (n=10142)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5682 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.1699` → IC=+0.200 (n=4360)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1699 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.465` → IC=+0.250 (n=2036)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.465 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `1.2063` → IC=+0.167 (n=6745)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2063 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` > `0.6307` → IC=+0.163 (n=6746)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6307 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.2957` → IC=+0.198 (n=1508)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2957 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `1.4521` → IC=+0.174 (n=3262)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.4521 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `2.6119` → IC=+0.182 (n=3261)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.6119 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `1993.8402` → IC=+0.178 (n=9060)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 1993.8402 (IC base=+0.174)

- **PATRÓN** `ballena_activa_n` < `104.0` → IC=+0.189 (n=9054)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 104.0 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.189 (n=6446)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0066 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.0801` → IC=+0.223 (n=3222)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0801 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=3668)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` < `0.4857` → IC=+0.232 (n=9663)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4857 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` < `0.1681` → IC=+0.170 (n=6731)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1681 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.32` → IC=+0.197 (n=1620)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 10.32 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` < `1.1783` → IC=+0.164 (n=6927)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1783 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` > `0.2924` → IC=+0.217 (n=1407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2924 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `2.6155` → IC=+0.178 (n=2987)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.6155 (IC base=+0.175)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.185 (n=8621)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 106.0 (IC base=+0.175)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.234 (n=569)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.198)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.205 (n=567)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.3396` → IC=+0.218 (n=1699)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3396 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=1798)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.203 (n=1133)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` > `0.9158` → IC=+0.286 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9158 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.288` → IC=+0.331 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.288 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.250 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `1.4352` → IC=+0.196 (n=1592)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4352 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.211 (n=1761)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `2054.47` → IC=+0.198 (n=567)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2054.47 (IC base=+0.198)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.251 (n=1137)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.243)

- **PATRÓN** `sigma_h` > `0.0042` → IC=+0.249 (n=1294)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0042 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.1013` → IC=+0.297 (n=569)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1013 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.251 (n=1237)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.243)

- **PATRÓN** `ibs_20min` < `0.1034` → IC=+0.279 (n=862)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1034 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.394` → IC=+0.245 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.394 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.252` → IC=+0.249 (n=1399)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.252 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` < `0.1626` → IC=+0.241 (n=1245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1626 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` > `0.2925` → IC=+0.274 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2925 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` < `1.4211` → IC=+0.261 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4211 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` > `2.6242` → IC=+0.243 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6242 (IC base=+0.243)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.244 (n=1425)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.243)

- **PATRÓN** `libro_liquidez` > `1973.02` → IC=+0.259 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1973.02 (IC base=+0.243)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.220 (n=672)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.160)

- **PATRÓN** `drift_60min` |x|≤ `0.1656` → IC=+0.185 (n=1017)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1656 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.181 (n=1527)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 6.0 (IC base=+0.160)

- **PATRÓN** `ibs_20min` > `0.3884` → IC=+0.225 (n=1525)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3884 (IC base=+0.160)

- **PATRÓN** `dist_vwap_pct` > `0.1978` → IC=+0.213 (n=893)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1978 (IC base=+0.160)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.506` → IC=+0.232 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.506 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` < `0.6924` → IC=+0.170 (n=671)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.6924 (IC base=+0.160)

- **PATRÓN** `volumen_pendiente_norm` > `0.2838` → IC=+0.193 (n=242)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2838 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` < `1.4161` → IC=+0.185 (n=496)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.4161 (IC base=+0.160)

- **PATRÓN** `ballena_activa_n` < `235.0` → IC=+0.173 (n=637)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 235.0 (IC base=+0.160)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.161 (n=1595)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0057 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.2319` → IC=+0.175 (n=1403)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2319 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.182 (n=612)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.5918` → IC=+0.198 (n=1594)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.5918 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.1345` → IC=+0.171 (n=1583)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1345 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.901` → IC=+0.201 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.901 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.2077` → IC=+0.162 (n=1594)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2077 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` < `0.2292` → IC=+0.145 (n=1641)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` < 0.2292 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.1603` → IC=+0.146 (n=490)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.1603 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `2.4908` → IC=+0.153 (n=1481)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4908 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.7719` → IC=+0.144 (n=987)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.7719 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `208.0` → IC=+0.176 (n=471)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 208.0 (IC base=+0.142)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0116` → IC=+0.228 (n=568)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0116 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.2466` → IC=+0.223 (n=1133)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2466 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.212 (n=1771)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.293 (n=885)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.543` → IC=+0.276 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.543 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.205 (n=1430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.1281` → IC=+0.208 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1281 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `1.7786` → IC=+0.206 (n=718)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7786 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `2.7283` → IC=+0.213 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7283 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=2020)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `1957.2184` → IC=+0.227 (n=770)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1957.2184 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.244 (n=1272)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0102 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.143` → IC=+0.262 (n=636)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.143 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.278 (n=497)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` < `0.35` → IC=+0.250 (n=1445)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.35 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.677` → IC=+0.260 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.677 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.3507` → IC=+0.263 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3507 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.7408` → IC=+0.241 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7408 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `2.7347` → IC=+0.235 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7347 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `1947.66` → IC=+0.234 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1947.66 (IC base=+0.227)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.221 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.227)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.206 (n=718)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.0779` → IC=+0.200 (n=544)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0779 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=1698)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.3333` → IC=+0.208 (n=1630)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3333 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.1379` → IC=+0.189 (n=1063)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1379 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.995` → IC=+0.207 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.995 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.8567` → IC=+0.161 (n=1087)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8567 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1017` → IC=+0.171 (n=682)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1017 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `1.437` → IC=+0.167 (n=533)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.437 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `2.5308` → IC=+0.160 (n=533)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.5308 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `5056.175` → IC=+0.198 (n=1087)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 5056.175 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `128.0` → IC=+0.157 (n=1382)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 128.0 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.162 (n=1496)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0061 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.3824` → IC=+0.150 (n=1696)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.3824 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=648)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.669` → IC=+0.185 (n=1696)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.669 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.904` → IC=+0.160 (n=589)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 6.904 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.160 (n=1131)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.856 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2971` → IC=+0.186 (n=256)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2971 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.8227` → IC=+0.138 (n=1047)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.8227 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `1.5277` → IC=+0.130 (n=1402)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.5277 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `4347.5908` → IC=+0.166 (n=1131)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 4347.5908 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.128 (n=1511)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 150.0 (IC base=+0.129)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.161 (n=842)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0099 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.444` → IC=+0.128 (n=1631)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.444 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=1896)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.212 (n=1866)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.1998` → IC=+0.182 (n=1136)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1998 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.874` → IC=+0.260 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.874 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `1.2007` → IC=+0.139 (n=1854)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.2007 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `0.6466` → IC=+0.130 (n=1854)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 0.6466 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` < `0.1642` → IC=+0.135 (n=1870)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.1642 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.5459` → IC=+0.145 (n=789)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.5459 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.4852` → IC=+0.128 (n=597)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 2.4852 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.130 (n=1944)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `2892.276` → IC=+0.205 (n=841)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2892.276 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.148 (n=1468)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 46.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.155 (n=821)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0061 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1033` → IC=+0.177 (n=620)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.1033 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=1875)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.5778` → IC=+0.217 (n=1860)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5778 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `0.7475` → IC=+0.123 (n=335)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.7475 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.197` → IC=+0.148 (n=1711)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.197 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.366` → IC=+0.128 (n=568)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 5.366 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.1756` → IC=+0.131 (n=1860)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1756 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2274` → IC=+0.158 (n=328)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.2274 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4527` → IC=+0.134 (n=569)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.4527 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `1.8145` → IC=+0.125 (n=1138)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.8145 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2750.8782` → IC=+0.185 (n=843)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2750.8782 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.128 (n=1665)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 52.0 (IC base=+0.120)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.232 (n=1737)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.2846` → IC=+0.216 (n=1159)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2846 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.211 (n=1807)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.214 (n=792)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.247 (n=1738)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.1969` → IC=+0.214 (n=1178)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1969 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` < `0.2855` → IC=+0.207 (n=1246)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2855 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.6` → IC=+0.245 (n=797)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.6 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` < `1.1907` → IC=+0.212 (n=1738)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1907 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `0.6251` → IC=+0.218 (n=1737)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6251 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.273 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.283 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `2.4718` → IC=+0.212 (n=1685)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4718 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.8108` → IC=+0.222 (n=1123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8108 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.211 (n=1654)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `2636.4702` → IC=+0.213 (n=1158)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2636.4702 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.0117` → IC=+0.229 (n=783)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0117 (IC base=+0.217)

- **PATRÓN** `sigma_h` > `0.0223` → IC=+0.223 (n=806)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0223 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.0897` → IC=+0.243 (n=593)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0897 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.237 (n=872)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.0196` → IC=+0.288 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0196 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` > `1.1561` → IC=+0.235 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1561 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.386` → IC=+0.254 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.386 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` > `0.6385` → IC=+0.228 (n=1778)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6385 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.2819` → IC=+0.275 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2819 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `2.2006` → IC=+0.209 (n=1435)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2006 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `1.4384` → IC=+0.216 (n=1630)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4384 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `2611.5123` → IC=+0.225 (n=1185)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2611.5123 (IC base=+0.217)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.201 (n=887)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.169)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.172 (n=889)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0083 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.3367` → IC=+0.180 (n=2342)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.3367 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.189 (n=2414)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 8.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.3396` → IC=+0.197 (n=2661)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.3396 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.3645` → IC=+0.182 (n=807)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.3645 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.759` → IC=+0.194 (n=1153)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 3.759 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `0.8703` → IC=+0.189 (n=1588)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8703 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `1.2058` → IC=+0.180 (n=794)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 1.2058 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.1641` → IC=+0.176 (n=707)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1641 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.4431` → IC=+0.182 (n=861)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.4431 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.539` → IC=+0.176 (n=861)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.539 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.173 (n=3039)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `2751.7394` → IC=+0.171 (n=2377)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2751.7394 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `146.0` → IC=+0.187 (n=2442)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 146.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.154 (n=916)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0036 (IC base=+0.111)

- **PATRÓN** `drift_60min` |x|≤ `0.3366` → IC=+0.122 (n=2404)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.61€ cuando `drift_60min` |x|≤ 0.3366 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.123 (n=2562)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` < `0.0721` → IC=+0.197 (n=912)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.0721 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `0.6986` → IC=+0.125 (n=1089)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 0.6986 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.0754` → IC=+0.126 (n=1042)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` > 0.0754 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `1.4409` → IC=+0.149 (n=885)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4409 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2799.497` → IC=+0.131 (n=2439)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2799.497 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.130 (n=1149)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 29.0 (IC base=+0.111)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.206 (n=325)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.3292` → IC=+0.176 (n=738)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3292 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.191 (n=674)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 8.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.6376` → IC=+0.208 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6376 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.2886` → IC=+0.173 (n=246)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.2886 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.181` → IC=+0.176 (n=316)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.181 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.8817` → IC=+0.178 (n=492)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.8817 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` < `0.157` → IC=+0.157 (n=773)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.157 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.2468` → IC=+0.159 (n=634)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.2468 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.5264` → IC=+0.158 (n=644)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.5264 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `14592.7283` → IC=+0.164 (n=492)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 14592.7283 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `148.0` → IC=+0.202 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 148.0 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.198 (n=289)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0027 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.3447` → IC=+0.159 (n=867)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3447 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.150 (n=829)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 6.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.148 (n=881)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 17.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.6112` → IC=+0.185 (n=763)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6112 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.1813` → IC=+0.159 (n=864)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1813 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.567` → IC=+0.150 (n=918)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 6.567 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.2138` → IC=+0.146 (n=867)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.2138 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` > `1.0712` → IC=+0.168 (n=393)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 1.0712 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.1612` → IC=+0.198 (n=236)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1612 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `2.1216` → IC=+0.163 (n=754)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.1216 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.412` → IC=+0.148 (n=857)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.412 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=1121)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `12062.2629` → IC=+0.144 (n=774)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 12062.2629 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `353.0` → IC=+0.155 (n=835)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 353.0 (IC base=+0.143)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.241 (n=561)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.2048` → IC=+0.218 (n=561)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2048 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.220 (n=882)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `0.6714` → IC=+0.251 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6714 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.3573` → IC=+0.213 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3573 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` < `0.2032` → IC=+0.204 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2032 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.089` → IC=+0.221 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.089 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` < `0.8419` → IC=+0.209 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8419 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` > `1.1822` → IC=+0.221 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1822 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.268` → IC=+0.233 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.268 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `1.4275` → IC=+0.228 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4275 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `2.4672` → IC=+0.231 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4672 (IC base=+0.202)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.135 (n=707)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0061 (IC base=+0.109)

- **PATRÓN** `drift_60min` |x|≤ `0.0962` → IC=+0.141 (n=268)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.0962 (IC base=+0.109)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.134 (n=552)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 11.0 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.0868` → IC=+0.163 (n=268)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.0868 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.459` → IC=+0.151 (n=210)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 6.459 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` < `0.6877` → IC=+0.152 (n=354)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6877 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` > `0.2234` → IC=+0.146 (n=128)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.2234 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `4032.9691` → IC=+0.133 (n=718)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 4032.9691 (IC base=+0.109)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.129 (n=346)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 42.0 (IC base=+0.109)

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
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.178 (n=4378)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0046 (IC base=+0.176)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.212 (n=4373)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=13719)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `0.9914` → IC=+0.310 (n=4373)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9914 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.1633` → IC=+0.186 (n=4956)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1633 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.389` → IC=+0.245 (n=3219)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.389 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `1.2331` → IC=+0.165 (n=8787)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2331 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.2903` → IC=+0.197 (n=1785)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2903 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `2.6011` → IC=+0.195 (n=4230)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6011 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `1979.1984` → IC=+0.180 (n=11719)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 1979.1984 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.202 (n=10356)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 79.0 (IC base=+0.176)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.197 (n=5208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0053 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.1466` → IC=+0.195 (n=5197)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1466 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=4446)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` < `0.4516` → IC=+0.249 (n=10393)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4516 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` < `0.1733` → IC=+0.167 (n=6992)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1733 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.107` → IC=+0.206 (n=1669)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.107 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.747` → IC=+0.186 (n=11369)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 3.747 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `1.207` → IC=+0.159 (n=8006)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.207 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.2897` → IC=+0.251 (n=1577)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2897 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `1.8631` → IC=+0.192 (n=7354)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 1.8631 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.208 (n=7126)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.185)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.249 (n=728)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.206)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.224 (n=727)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.3519` → IC=+0.208 (n=2179)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3519 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.225 (n=1057)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.208 (n=1465)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.329 (n=809)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.744` → IC=+0.351 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.744 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.265 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `2.5787` → IC=+0.218 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5787 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.226 (n=2231)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `2058.72` → IC=+0.209 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2058.72 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.266 (n=1195)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.260)

- **PATRÓN** `sigma_h` > `0.0043` → IC=+0.264 (n=1788)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0043 (IC base=+0.260)

- **PATRÓN** `drift_60min` |x|≤ `0.1241` → IC=+0.282 (n=787)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1241 (IC base=+0.260)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.270 (n=1609)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.260)

- **PATRÓN** `ibs_20min` < `0.3579` → IC=+0.284 (n=1573)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3579 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.508` → IC=+0.266 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.508 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` > `0.2835` → IC=+0.288 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2835 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` > `2.6325` → IC=+0.280 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6325 (IC base=+0.260)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.260 (n=1962)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `1979.29` → IC=+0.271 (n=811)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1979.29 (IC base=+0.260)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.212 (n=703)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.1797` → IC=+0.165 (n=1401)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1797 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=2201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.2855` → IC=+0.207 (n=2100)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2855 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.126` → IC=+0.190 (n=1182)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.126 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.721` → IC=+0.179 (n=350)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 11.721 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.221` → IC=+0.155 (n=1921)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.221 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.7033` → IC=+0.171 (n=924)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.7033 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` < `0.0733` → IC=+0.154 (n=1859)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0733 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.2723` → IC=+0.188 (n=302)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2723 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.1485` → IC=+0.160 (n=1797)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1485 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.5228` → IC=+0.156 (n=1824)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.5228 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `276.0` → IC=+0.183 (n=869)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 276.0 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.161 (n=1753)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0057 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.33` → IC=+0.157 (n=1751)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.33 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=668)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.147 (n=803)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 7.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.684` → IC=+0.195 (n=1751)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.684 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.132` → IC=+0.165 (n=1602)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.132 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.56` → IC=+0.161 (n=296)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.56 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.333` → IC=+0.146 (n=1583)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 4.333 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.1895` → IC=+0.159 (n=1751)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1895 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1548` → IC=+0.198 (n=468)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1548 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.4384` → IC=+0.154 (n=1650)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4384 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.7762` → IC=+0.160 (n=1100)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7762 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `258.0` → IC=+0.146 (n=523)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 258.0 (IC base=+0.145)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.232 (n=2156)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=2262)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.226 (n=2177)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=815)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.417` → IC=+0.300 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.417 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` < `0.2056` → IC=+0.226 (n=2169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2056 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `1.6215` → IC=+0.229 (n=2075)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6215 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=2570)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `2034.0327` → IC=+0.237 (n=718)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2034.0327 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.245 (n=1773)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.1798` → IC=+0.250 (n=887)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1798 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.258 (n=770)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.239 (n=952)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.0148` → IC=+0.301 (n=673)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0148 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.96` → IC=+0.286 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.96 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.3417` → IC=+0.297 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3417 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` < `1.7339` → IC=+0.239 (n=832)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7339 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.1472` → IC=+0.242 (n=1260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1472 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.237 (n=1165)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `1950.2584` → IC=+0.248 (n=914)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1950.2584 (IC base=+0.235)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.255 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.235)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.197 (n=989)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0038 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.3335` → IC=+0.152 (n=1976)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.3335 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.155 (n=2343)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.2704` → IC=+0.189 (n=2245)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2704 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.5409` → IC=+0.163 (n=613)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.5409 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.171` → IC=+0.151 (n=918)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 4.171 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8744` → IC=+0.160 (n=1497)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8744 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.1662` → IC=+0.174 (n=597)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1662 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.5297` → IC=+0.158 (n=963)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.5297 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.1865` → IC=+0.149 (n=991)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.1865 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `7315.5234` → IC=+0.236 (n=1018)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7315.5234 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.180 (n=710)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 70.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.186 (n=607)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0033 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.3481` → IC=+0.144 (n=1592)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3481 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.160 (n=666)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.137 (n=635)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 5.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.7338` → IC=+0.184 (n=1810)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.7338 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.357` → IC=+0.170 (n=371)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.357 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `0.876` → IC=+0.143 (n=1207)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.876 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.2976` → IC=+0.232 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2976 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `1.4473` → IC=+0.143 (n=1734)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.4473 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `8648.0766` → IC=+0.206 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8648.0766 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.135 (n=1731)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 166.0 (IC base=+0.132)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.136 (n=2254)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0055 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=827)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.4565` → IC=+0.201 (n=2254)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4565 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `1.0213` → IC=+0.209 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0213 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.525` → IC=+0.242 (n=831)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.525 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `0.8916` → IC=+0.147 (n=1503)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8916 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1623` → IC=+0.128 (n=2322)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1623 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.1924` → IC=+0.136 (n=995)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.1924 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.131 (n=2305)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2555.8611` → IC=+0.236 (n=1022)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2555.8611 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.147 (n=684)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 27.0 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.176 (n=718)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0056 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.1302` → IC=+0.165 (n=717)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1302 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.160 (n=794)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.5065` → IC=+0.234 (n=1891)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5065 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` < `0.2166` → IC=+0.141 (n=1784)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.2166 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.49` → IC=+0.133 (n=2069)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 3.49 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.7144` → IC=+0.160 (n=948)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.7144 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.223` → IC=+0.185 (n=350)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.223 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `2.1597` → IC=+0.138 (n=1745)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.1597 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2797.1957` → IC=+0.197 (n=717)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2797.1957 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.140 (n=1738)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 50.0 (IC base=+0.122)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.234 (n=2189)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.220 (n=2290)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.221 (n=1581)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.264 (n=1958)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `0.2063` → IC=+0.234 (n=1251)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2063 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.744` → IC=+0.261 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.744 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` < `1.2371` → IC=+0.219 (n=2189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2371 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `0.6415` → IC=+0.223 (n=2189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6415 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.2366` → IC=+0.245 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2366 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `2.5113` → IC=+0.247 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5113 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.225 (n=2064)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `2638.7996` → IC=+0.226 (n=1459)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2638.7996 (IC base=+0.216)

- **PATRÓN** `sigma_h` < `0.0095` → IC=+0.218 (n=768)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0095 (IC base=+0.215)

- **PATRÓN** `sigma_h` > `0.0226` → IC=+0.230 (n=1043)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0226 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.231 (n=1623)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.4167` → IC=+0.264 (n=2023)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4167 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `1.1776` → IC=+0.216 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1776 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` < `0.2921` → IC=+0.218 (n=2151)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2921 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.883` → IC=+0.256 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.883 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `1.2299` → IC=+0.243 (n=766)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2299 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.282` → IC=+0.283 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.282 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `1.4305` → IC=+0.216 (n=2106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4305 (IC base=+0.215)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.207 (n=2027)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.215)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=3834)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.230 (n=1308)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.3909` → IC=+0.197 (n=3434)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.3909 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.201 (n=1455)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.190 (n=1780)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 6.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` > `0.9408` → IC=+0.240 (n=1303)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9408 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` > `0.1682` → IC=+0.195 (n=1441)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1682 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.195` → IC=+0.210 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.195 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `0.7119` → IC=+0.192 (n=1186)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.7119 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` > `0.8938` → IC=+0.190 (n=1797)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 0.8938 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.1701` → IC=+0.215 (n=1099)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1701 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` < `1.4601` → IC=+0.193 (n=1283)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4601 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.6348` → IC=+0.193 (n=1283)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6348 (IC base=+0.187)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.193 (n=2888)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `3788.4039` → IC=+0.195 (n=2601)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 3788.4039 (IC base=+0.187)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.222 (n=963)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.4838` → IC=+0.183 (n=2887)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.4838 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.199 (n=1017)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.165)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.184 (n=1313)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 6.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` < `0.18` → IC=+0.188 (n=1272)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.18 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.6425` → IC=+0.178 (n=533)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.6425 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` < `0.2349` → IC=+0.159 (n=2581)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.2349 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.184` → IC=+0.173 (n=2879)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` < 6.184 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `1.255` → IC=+0.170 (n=2723)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.255 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` < `0.097` → IC=+0.169 (n=2629)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.097 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.2226` → IC=+0.168 (n=601)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2226 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `1.5395` → IC=+0.170 (n=1254)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5395 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `1.8271` → IC=+0.174 (n=1899)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.8271 (IC base=+0.165)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=3834)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `12289.2679` → IC=+0.167 (n=963)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 12289.2679 (IC base=+0.165)

- **PATRÓN** `ballena_activa_n` < `195.0` → IC=+0.175 (n=2480)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 195.0 (IC base=+0.165)

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

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.281 (n=39)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.237)

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
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.219 (n=397)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.1507` → IC=+0.214 (n=523)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1507 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=434)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.195 (n=543)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 6.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.5225` → IC=+0.205 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5225 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `0.8854` → IC=+0.199 (n=396)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.8854 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` < `0.14` → IC=+0.205 (n=924)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.14 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.178` → IC=+0.201 (n=1067)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.178 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `1.0845` → IC=+0.198 (n=1045)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 1.0845 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` > `1.2448` → IC=+0.197 (n=397)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` > 1.2448 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.1071` → IC=+0.194 (n=1091)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.1071 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.1659` → IC=+0.207 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1659 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `2.4777` → IC=+0.199 (n=1162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4777 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.197 (n=1190)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.222 (n=318)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.3841` → IC=+0.195 (n=832)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.3841 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.186 (n=323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.173 (n=635)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 10.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` < `0.7588` → IC=+0.170 (n=946)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.7588 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.0908` → IC=+0.170 (n=945)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.0908 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.6046` → IC=+0.186 (n=205)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.6046 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` < `0.2152` → IC=+0.165 (n=875)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.2152 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.153` → IC=+0.167 (n=1053)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 9.153 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `0.6434` → IC=+0.204 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6434 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` > `0.7259` → IC=+0.165 (n=845)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.7259 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.0726` → IC=+0.183 (n=399)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.0726 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `2.1956` → IC=+0.181 (n=816)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.1956 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `1.7864` → IC=+0.166 (n=618)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.7864 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `7437.397` → IC=+0.179 (n=945)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 7437.397 (IC base=+0.164)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.008` → IC=+0.218 (n=324)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.3182` → IC=+0.171 (n=323)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.3182 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.200 (n=441)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.261 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.1981` → IC=+0.207 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1981 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.485` → IC=+0.220 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.485 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `0.6477` → IC=+0.201 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6477 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `1.2699` → IC=+0.177 (n=162)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.2699 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.1631` → IC=+0.217 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1631 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.5383` → IC=+0.217 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5383 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.177 (n=586)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.02 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `3351.4953` → IC=+0.213 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3351.4953 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.193 (n=418)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 49.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.198 (n=329)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0069 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.3766` → IC=+0.229 (n=245)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3766 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.180 (n=126)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 16.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.202 (n=246)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` < `0.0922` → IC=+0.244 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0922 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.8305` → IC=+0.219 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8305 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.061` → IC=+0.196 (n=67)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 9.061 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.1` → IC=+0.183 (n=355)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 5.1 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.9767` → IC=+0.188 (n=245)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.9767 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` < `0.1057` → IC=+0.224 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1057 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `1.8976` → IC=+0.195 (n=237)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.8976 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.2075` → IC=+0.187 (n=161)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.2075 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `3511.2758` → IC=+0.200 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3511.2758 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.215 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 53.0 (IC base=+0.180)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.155 (n=563)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0038 (IC base=+0.081)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.126 (n=583)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 16.0 (IC base=+0.081)

- **PATRÓN** `ibs_20min` > `0.4422` → IC=+0.155 (n=1181)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.4422 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.1402` → IC=+0.140 (n=646)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.1402 (IC base=+0.081)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.45` → IC=+0.186 (n=272)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 11.45 (IC base=+0.081)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.177 (n=165)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.081)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.246 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2 (IC base=+0.050)

- **PATRÓN** `dist_vwap_pct` < `0.1125` → IC=+0.127 (n=499)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` < 0.1125 (IC base=+0.050)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.169` → IC=+0.132 (n=419)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 4.169 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.1454` → IC=+0.183 (n=118)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1454 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` < `2.5975` → IC=+0.137 (n=431)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.5975 (IC base=+0.050)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.141 (n=433)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0057 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.125 (n=438)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.099)

- **PATRÓN** `ibs_20min` > `0.4165` → IC=+0.176 (n=402)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.4165 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.164 (n=215)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` < `2.5107` → IC=+0.127 (n=360)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 2.5107 (IC base=+0.099)

- **PATRÓN** `ibs_20min` < `0.0493` → IC=+0.283 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0493 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` < `0.1876` → IC=+0.126 (n=263)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` < 0.1876 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.157` → IC=+0.145 (n=229)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 7.157 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` > `0.8156` → IC=+0.131 (n=158)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 0.8156 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.0743` → IC=+0.139 (n=95)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.0743 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` < `2.5091` → IC=+0.134 (n=214)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.5091 (IC base=+0.076)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.154 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=158)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.149 (n=280)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0046 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.128 (n=393)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 7.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.6875` → IC=+0.209 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6875 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.173 (n=215)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.674` → IC=+0.273 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.674 (IC base=+0.094)

- **PATRÓN** `volumen_pendiente_norm` > `0.2829` → IC=+0.191 (n=53)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2829 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` < `1.7889` → IC=+0.128 (n=224)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.7889 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `1151.5637` → IC=+0.144 (n=344)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 1151.5637 (IC base=+0.094)

- **PATRÓN** `ibs_20min` < `0.7041` → IC=+0.150 (n=135)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.7041 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2423` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2423 (IC base=+0.005)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0103` → IC=-0.250 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0103
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=151)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.246 (n=124)

- **PATRÓN** `ibs_20min` > `0.7647` → IC=+0.177 (n=261)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.7647 (IC base=+0.051)

- **PATRÓN** `dist_vwap_pct` > `0.7176` → IC=+0.130 (n=106)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 0.7176 (IC base=+0.051)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.144` → IC=+0.123 (n=112)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` > 8.144 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.2436` → IC=+0.183 (n=77)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2436 (IC base=+0.051)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.167 (n=133)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0084 (IC base=+0.052)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.246 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` > `0.1153` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1153 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` < `0.1829` → IC=+0.150 (n=121)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1829 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.968` → IC=+0.333 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.968 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` > `0.0794` → IC=+0.304 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0794 (IC base=+0.052)

- **PATRÓN** `volumen_spike_ratio` > `1.8705` → IC=+0.196 (n=67)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.8705 (IC base=+0.052)

### GBM_LATE_60M_FADE
- **FILTRO** `dist_vwap_pct` > `0.2352` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2352
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=237)

- **FILTRO** `volumen_regimen` < `0.7431` → IC=-0.361 (n=63)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7431
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=190)

- **FILTRO** `volumen_spike_ratio` > `2.98` → IC=-0.196 (n=44)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.98
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=135)

- **FILTRO** `volumen_spike_ratio` < `1.6212` → IC=-0.172 (n=59)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.6212
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=120)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.206 (n=49)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=204)

- **FILTRO** `sigma_h` > `0.0054` → IC=-0.377 (n=55)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0054
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=166)

- **FILTRO** `dist_vwap_pct` > `0.3156` → IC=-0.392 (n=35)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3156
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=186)

- **FILTRO** `volumen_pendiente_norm` > `0.0538` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0538
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=110)

- **FILTRO** `volumen_spike_ratio` > `2.2319` → IC=-0.329 (n=33)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.2319
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=102)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` < `5.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.153 (n=47)

- **FILTRO** `ibs_20min` < `0.1017` → IC=-0.224 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1017
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=55)

- **FILTRO** `volumen_regimen` < `0.8402` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8402
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=62)

- **FILTRO** `volumen_spike_ratio` > `3.1256` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.1256
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=39)

- **FILTRO** `volumen_regimen` > `0.8359` → IC=-0.340 (n=23)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8359
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=71)

- **FILTRO** `volumen_spike_ratio` > `1.5538` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.5538
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=31)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` < `0.0025` → IC=-0.364 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0025
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=63)

- **FILTRO** `ibs_20min` < `0.5872` → IC=-0.466 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5872
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=56)

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

- **PATRÓN** `ibs_20min` > `0.9583` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9583 (IC base=-0.171)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=72)

- **FILTRO** `volumen_spike_ratio` < `1.5474` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.5474
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=48)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=62)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=30)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=23)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.172 (n=178)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0057 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.137 (n=188)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 15.0 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.6592` → IC=+0.145 (n=390)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.6592 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.4722` → IC=+0.196 (n=90)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.4722 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` < `0.657` → IC=+0.144 (n=130)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.657 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` < `2.5313` → IC=+0.129 (n=289)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 2.5313 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.131 (n=139)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 17.0 (IC base=+0.079)

- **PATRÓN** `ibs_20min` < `0.156` → IC=+0.169 (n=354)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.156 (IC base=+0.079)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.664` → IC=+0.202 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.664 (IC base=+0.079)

- **PATRÓN** `libro_liquidez` > `1542.2638` → IC=+0.120 (n=359)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 1542.2638 (IC base=+0.079)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6472` → IC=-0.256 (n=39)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6472
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=117)

- **PATRÓN** `sigma_h` > `0.0024` → IC=+0.187 (n=161)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0024 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.194 (n=60)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.151 (n=64)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 5.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.1524` → IC=+0.194 (n=181)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.1524 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.2068` → IC=+0.145 (n=29)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.2068 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.0881` → IC=+0.151 (n=187)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.0881 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.678` → IC=+0.182 (n=146)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 4.678 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `0.6182` → IC=+0.159 (n=180)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6182 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` < `0.1846` → IC=+0.187 (n=148)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.1846 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.6699` → IC=+0.189 (n=149)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.6699 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.4429` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.4429 (IC base=+0.145)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1654` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1654
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=105)

- **FILTRO** `libro_liquidez` < `1526.5273` → IC=-0.174 (n=41)

  - _Acción_: SKIP cuando `libro_liquidez` < 1526.5273
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=125)

- **PATRÓN** `volumen_spike_ratio` < `1.8731` → IC=+0.132 (n=66)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.8731 (IC base=+0.054)

- **PATRÓN** `libro_liquidez` > `1526.5273` → IC=+0.130 (n=125)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 1526.5273 (IC base=+0.054)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.144 (n=99)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 12.0 (IC base=+0.065)

- **PATRÓN** `ibs_20min` < `0.3236` → IC=+0.139 (n=142)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.3236 (IC base=+0.065)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.429` → IC=+0.311 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.429 (IC base=+0.065)

- **PATRÓN** `volumen_regimen` < `0.8448` → IC=+0.129 (n=95)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.8448 (IC base=+0.065)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `volumen_pendiente_norm` < `0.0968` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0968
  - _Potencial_: sin este filtro IC_bueno=+0.176 (n=35)

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

- **PATRÓN** `volumen_pendiente_norm` > `0.0968` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.0968 (IC base=-0.046)

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
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.124 (n=994)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `2856.5544` → IC=+0.144 (n=465)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 2856.5544 (IC base=+0.104)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.124 (n=994)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `2856.5544` → IC=+0.144 (n=465)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 2856.5544 (IC base=+0.104)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=150)

- **FILTRO** `libro_liquidez` < `10077.5355` → IC=-0.185 (n=109)

  - _Acción_: SKIP cuando `libro_liquidez` < 10077.5355
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=57)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=237)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=223)

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

- **FILTRO** `hora_utc` > `6.0` → IC=-0.133 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

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
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=2646)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=96)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=53)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=96)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.188 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.126 (n=105)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.126 (n=105)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 15.0 (IC base=+0.055)

- **PATRÓN** `libro_liquidez` > `2582.9138` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2582.9138 (IC base=+0.055)

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

- **PATRÓN** `liq_usd_total` > `62122.28` → IC=+0.145 (n=136)

  - _Acción_: Kelly boost +0.72€ cuando `liq_usd_total` > 62122.28 (IC base=+0.045)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.140 (n=173)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.495 (IC base=+0.045)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=1017)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=971)

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
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=608)

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
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=327)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.155 (n=117)

  - _Acción_: Kelly boost +0.78€ cuando `py_entrada` < 0.495 (IC base=+0.028)

- **PATRÓN** `libro_liquidez` > `3976.0824` → IC=+0.139 (n=117)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 3976.0824 (IC base=+0.028)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=766)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=766)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.133 (n=246)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=600)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=531)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=531)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=211)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=211)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.136 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=173)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.122 (n=88)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=138)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=133)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=157)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=242)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=129)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=142)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=298)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=298)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=195)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.142 (n=686)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=1691)

- **PATRÓN** `py_entrada` < `0.47` → IC=+0.146 (n=566)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.47 (IC base=+0.020)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=14)

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
- **FILTRO** `py_entrada` < `0.52` → IC=-0.124 (n=163)

  - _Acción_: SKIP cuando `py_entrada` < 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=63)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.216 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.46 (IC base=+0.042)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.147 (n=49)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=105)

- **FILTRO** `lag_apertura_s` > `402.96` → IC=-0.150 (n=38)

  - _Acción_: SKIP cuando `lag_apertura_s` > 402.96
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=116)

- **FILTRO** `profundidad_ratio` < `30.9` → IC=-0.131 (n=101)

  - _Acción_: SKIP cuando `profundidad_ratio` < 30.9
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=53)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **PATRÓN** `py_entrada` < `0.54` → IC=+0.141 (n=37)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.54 (IC base=+0.071)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `restante_min` < `13.49` → IC=-0.121 (n=151)

  - _Acción_: SKIP cuando `restante_min` < 13.49
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=60)

- **FILTRO** `lag_apertura_s` > `133.19` → IC=-0.145 (n=105)

  - _Acción_: SKIP cuando `lag_apertura_s` > 133.19
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=106)

- **FILTRO** `profundidad_ratio` < `54.8` → IC=-0.204 (n=69)

  - _Acción_: SKIP cuando `profundidad_ratio` < 54.8
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=142)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.250 (n=42)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=178)

- **PATRÓN** `py_entrada` < `0.48` → IC=+0.141 (n=62)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.48 (IC base=-0.018)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.140 (n=173)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=100)

- **FILTRO** `restante_min` < `3.43` → IC=-0.228 (n=90)

  - _Acción_: SKIP cuando `restante_min` < 3.43
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=183)

- **FILTRO** `lag_apertura_s` > `93.56` → IC=-0.213 (n=92)

  - _Acción_: SKIP cuando `lag_apertura_s` > 93.56
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=181)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.128 (n=49)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=156)

- **PATRÓN** `lag_apertura_s` < `98.43` → IC=+0.133 (n=77)

  - _Acción_: Kelly boost +0.66€ cuando `lag_apertura_s` < 98.43 (IC base=+0.002)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **PATRÓN** `py_entrada` < `0.49` → IC=+0.125 (n=78)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.49 (IC base=+0.004)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.137 (n=169)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.156 (n=91)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.156 (n=91)

  - _Acción_: Kelly boost +0.78€ cuando `py_entrada` > 0.5 (IC base=-0.034)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.198 (n=84)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=238)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.163 (n=4674)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=14107)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.166 (n=4844)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=14578)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.195 (n=827)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=2503)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.149 (n=809)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=2667)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.121 (n=1606)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` < 0.5 (IC base=+0.015)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.175 (n=840)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=2542)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.196 (n=818)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=2705)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.165 (n=797)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=2535)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2225)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=2491)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=3231)

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

- **FILTRO** `ibs_20min` < `0.1975` → IC=-0.223 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1975
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=224)

- **FILTRO** `py_entrada` > `0.615` → IC=-0.216 (n=86)

  - _Acción_: SKIP cuando `py_entrada` > 0.615
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=291)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=798)

- **FILTRO** `libro_liquidez` < `1968.1644` → IC=-0.170 (n=331)

  - _Acción_: SKIP cuando `libro_liquidez` < 1968.1644
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=673)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.132 (n=13165)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=29056)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=9910)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=32311)

- **FILTRO** `ibs_7min` < `0.2617` → IC=-0.235 (n=10555)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2617
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=31666)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.154 (n=14231)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=27990)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.236 (n=12977)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=40674)

- **FILTRO** `ibs_7min` > `0.2885` → IC=-0.180 (n=13407)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2885
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=40244)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.144 (n=2139)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=5041)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.309 (n=1712)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=5468)

- **FILTRO** `ibs_7min` < `0.7091` → IC=-0.253 (n=2367)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7091
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=4813)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.186 (n=1564)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=5616)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.267 (n=2265)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=7032)

- **FILTRO** `ibs_7min` > `0.7815` → IC=-0.211 (n=2324)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7815
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=6973)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.132 (n=1727)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=5498)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.249 (n=1773)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=5452)

- **FILTRO** `ibs_7min` < `0.7423` → IC=-0.198 (n=1806)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7423
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=5419)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.180 (n=1804)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=5421)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.265 (n=1745)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=5596)

- **FILTRO** `ibs_7min` > `0.2659` → IC=-0.194 (n=1835)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2659
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=5506)

- **FILTRO** `ballena_activa_n` > `149.0` → IC=-0.190 (n=1834)

  - _Acción_: SKIP cuando `ballena_activa_n` > 149.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=5507)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.162 (n=1952)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=4872)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.316 (n=1620)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=5204)

- **FILTRO** `ibs_7min` < `0.7037` → IC=-0.247 (n=2251)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7037
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=4573)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.217 (n=1549)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5275)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.243 (n=2247)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=7657)

- **FILTRO** `ibs_7min` > `0.7383` → IC=-0.172 (n=2475)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7383
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=7429)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=2260)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=4681)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.239 (n=2056)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=4885)

- **FILTRO** `ibs_7min` < `0.7409` → IC=-0.186 (n=1735)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7409
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5206)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.183 (n=1726)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=5215)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.269 (n=1768)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=5389)

- **FILTRO** `ibs_7min` > `0.2753` → IC=-0.184 (n=1789)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2753
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=5368)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.184 (n=1745)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=5412)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.273 (n=1656)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=5484)

- **FILTRO** `ibs_7min` < `0.25` → IC=-0.233 (n=1755)

  - _Acción_: SKIP cuando `ibs_7min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=5385)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.184 (n=2421)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=7813)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.277 (n=1642)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=5269)

- **FILTRO** `ibs_7min` < `0.25` → IC=-0.225 (n=1715)

  - _Acción_: SKIP cuando `ibs_7min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=5196)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.200 (n=1700)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=5211)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.206 (n=2390)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=7328)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.153 (n=295)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=963)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=1243)

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
- **PATRÓN** `delta_ratio` |x|> `0.398` → IC=+0.134 (n=928)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.398 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.135 (n=423)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 14.0 (IC base=+0.122)

- **PATRÓN** `total_vol_5m` < `442.2457` → IC=+0.149 (n=309)

  - _Acción_: Kelly boost +0.75€ cuando `total_vol_5m` < 442.2457 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.129 (n=785)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 52.0 (IC base=+0.122)

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
  - _Acción_: Kelly boost +0.86€ cuando `delta_ratio` |x|> 0.4139 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.208 (n=63)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.114)

- **PATRÓN** `total_vol_5m` < `384.339` → IC=+0.209 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 384.339 (IC base=+0.114)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.186 (n=84)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 73.0 (IC base=+0.114)

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
- **PATRÓN** `libro_spread` < `0.01` → IC=+0.193 (n=112)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `3599.4239` → IC=+0.167 (n=82)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3599.4239 (IC base=+0.097)

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
- **FILTRO** `T_h` > `71.8388` → IC=-0.157 (n=359)

  - _Acción_: SKIP cuando `T_h` > 71.8388
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=120)

- **FILTRO** `pct_vs_K` |x|> `3.7615` → IC=-0.260 (n=119)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.7615
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=360)

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

- **FILTRO** `T_h` > `143.1632` → IC=-0.311 (n=51)

  - _Acción_: SKIP cuando `T_h` > 143.1632
  - _Potencial_: sin este filtro IC_bueno=-0.277 (n=101)

- **FILTRO** `pct_vs_K` |x|> `2.7927` → IC=-0.424 (n=51)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7927
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=101)

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

- **FILTRO** `pct_vs_K` |x|> `3.4756` → IC=-0.406 (n=30)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4756
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=102)

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
- **FILTRO** `T_h` > `113.0501` → IC=-0.150 (n=58)

  - _Acción_: SKIP cuando `T_h` > 113.0501
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=60)

- **FILTRO** `pct_vs_K` |x|> `3.656` → IC=-0.238 (n=40)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.656
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=78)

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

- **PATRÓN** `T_h` < `0.9836` → IC=+0.433 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9836 (IC base=+0.423)

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
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=89)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=95)

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
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=566)

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
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=787)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1319)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=938)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=935)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3439)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=1798)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.201 (n=794)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.197)

- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.236 (n=794)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.1588` → IC=+0.203 (n=2096)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1588 (IC base=+0.197)

- **PATRÓN** `delta_ratio_macro` |x|> `0.222` → IC=+0.203 (n=794)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.222 (IC base=+0.197)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1301` → IC=+0.221 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1301 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.205 (n=2202)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.198 (n=2462)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.197)

- **PATRÓN** `ibs_15` > `0.6128` → IC=+0.276 (n=2382)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6128 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` > `0.1187` → IC=+0.200 (n=1175)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1187 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.983` → IC=+0.276 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.983 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `7277.3676` → IC=+0.207 (n=794)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7277.3676 (IC base=+0.197)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1018)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.238 (n=319)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.0582` → IC=+0.272 (n=160)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0582 (IC base=+0.215)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2012` → IC=+0.249 (n=217)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2012 (IC base=+0.215)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1075` → IC=+0.257 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1075 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=480)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.215)

- **PATRÓN** `ibs_15` > `0.7176` → IC=+0.277 (n=478)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7176 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `0.1371` → IC=+0.250 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1371 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.367` → IC=+0.272 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.367 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.214 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `16193.642` → IC=+0.247 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16193.642 (IC base=+0.215)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.513` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.513
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=600)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.184 (n=175)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0034 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.0673` → IC=+0.152 (n=231)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.0673 (IC base=+0.141)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2347` → IC=+0.167 (n=175)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio_macro` |x|> 0.2347 (IC base=+0.141)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1251` → IC=+0.162 (n=199)

  - _Acción_: Kelly boost +0.81€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1251 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.160 (n=374)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 11.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.142 (n=549)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 17.0 (IC base=+0.141)

- **PATRÓN** `ibs_15` > `0.5749` → IC=+0.241 (n=523)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5749 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.153` → IC=+0.147 (n=290)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.153 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.2614` → IC=+0.145 (n=485)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.2614 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.56` → IC=+0.223 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.56 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `3469.9204` → IC=+0.152 (n=467)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3469.9204 (IC base=+0.141)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `20.909` → IC=-0.133 (n=28)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 20.909
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=194)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.252 (n=111)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0085 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.1915` → IC=+0.201 (n=332)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1915 (IC base=+0.164)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0623` → IC=+0.171 (n=332)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.85€ cuando `delta_ratio_macro` |x|> 0.0623 (IC base=+0.164)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3453` → IC=+0.203 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3453 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.178 (n=231)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 11.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.172 (n=114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 4.0 (IC base=+0.164)

- **PATRÓN** `ibs_15` > `0.5357` → IC=+0.255 (n=332)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5357 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.1304` → IC=+0.178 (n=181)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1304 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` < `0.1732` → IC=+0.167 (n=283)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1732 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.265` → IC=+0.300 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.265 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.181 (n=214)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `2945.673` → IC=+0.191 (n=221)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2945.673 (IC base=+0.164)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `15.788` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 15.788 (IC base=+0.002)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.252 (n=527)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.0797` → IC=+0.214 (n=260)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0797 (IC base=+0.212)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0439` → IC=+0.216 (n=590)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0439 (IC base=+0.212)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0888` → IC=+0.261 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0888 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.241 (n=295)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.212)

- **PATRÓN** `ibs_15` > `0.5854` → IC=+0.292 (n=590)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5854 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.1342` → IC=+0.217 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1342 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.493` → IC=+0.244 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.493 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.39` → IC=+0.214 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.39 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `2949.5574` → IC=+0.294 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2949.5574 (IC base=+0.212)

- **PATRÓN** `ibs_15` < `0.1136` → IC=+0.155 (n=635)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.77€ cuando `ibs_15` < 0.1136 (IC base=+0.067)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.364 (n=351)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.358)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.364 (n=526)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0027 (IC base=+0.358)

- **PATRÓN** `drift_60min` |x|≤ `0.1109` → IC=+0.358 (n=351)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1109 (IC base=+0.358)

- **PATRÓN** `drift_15min` |x|≤ `0.4034` → IC=+0.360 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4034 (IC base=+0.358)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1497` → IC=+0.381 (n=350)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1497 (IC base=+0.358)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1344` → IC=+0.393 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1344 (IC base=+0.358)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.374 (n=531)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.358)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.394 (n=526)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.358)

- **PATRÓN** `dist_vwap_pct` > `0.4169` → IC=+0.388 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4169 (IC base=+0.358)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.247` → IC=+0.371 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.247 (IC base=+0.358)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.364 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.358)

- **PATRÓN** `libro_liquidez` > `3820.3005` → IC=+0.371 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3820.3005 (IC base=+0.358)

- **PATRÓN** `ballena_activa_n` < `443.0` → IC=+0.377 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 443.0 (IC base=+0.358)

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
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.353 (n=107)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.354)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.374 (n=109)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.354)

- **PATRÓN** `drift_60min` |x|≤ `0.1074` → IC=+0.365 (n=161)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1074 (IC base=+0.354)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.371 (n=215)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.354)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.298` → IC=+0.378 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.298 (IC base=+0.354)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.414 (n=115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.354)

- **PATRÓN** `ibs_15` > `0.7601` → IC=+0.401 (n=240)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7601 (IC base=+0.354)

- **PATRÓN** `dist_vwap_pct` > `0.4449` → IC=+0.365 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4449 (IC base=+0.354)

- **PATRÓN** `dist_vwap_pct` < `0.2797` → IC=+0.356 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2797 (IC base=+0.354)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.937` → IC=+0.372 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.937 (IC base=+0.354)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.587` → IC=+0.354 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.587 (IC base=+0.354)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.361 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.354)

- **PATRÓN** `libro_liquidez` > `4204.0039` → IC=+0.378 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4204.0039 (IC base=+0.354)

- **PATRÓN** `ballena_activa_n` < `147.0` → IC=+0.360 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 147.0 (IC base=+0.354)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0121` → IC=-0.227 (n=869)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0121
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=2610)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=1282)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=2197)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1406` → IC=+0.180 (n=558)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1406 (IC base=-0.066)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1371` → IC=+0.236 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1371 (IC base=-0.066)

- **PATRÓN** `ibs_15` > `0.6347` → IC=+0.278 (n=837)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6347 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` > `0.1051` → IC=+0.199 (n=479)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1051 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` < `0.2555` → IC=+0.198 (n=689)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.2555 (IC base=-0.066)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1277` → IC=+0.259 (n=1784)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1277 (IC base=-0.017)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1868` → IC=+0.251 (n=1744)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1868 (IC base=-0.017)

- **PATRÓN** `ibs_15` < `0.3499` → IC=+0.279 (n=2677)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3499 (IC base=-0.017)

- **PATRÓN** `dist_vwap_pct` > `0.8516` → IC=+0.296 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8516 (IC base=-0.017)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.214 (n=498)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=1496)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.230 (n=498)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=1496)

- **FILTRO** `sigma_ewma_delta_pct` > `23.695` → IC=-0.266 (n=284)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.695
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=1710)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.185 (n=198)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0027 (IC base=+0.087)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2011` → IC=+0.300 (n=113)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2011 (IC base=+0.087)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1378` → IC=+0.304 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1378 (IC base=+0.087)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.121 (n=404)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 12.0 (IC base=+0.087)

- **PATRÓN** `ibs_15` > `0.7572` → IC=+0.328 (n=248)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7572 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.1012` → IC=+0.294 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1012 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.3535` → IC=+0.284 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3535 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.533` → IC=+0.127 (n=290)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` > 8.533 (IC base=+0.087)

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
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=533)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.153 (n=364)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0058 (IC base=+0.150)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.163 (n=369)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0038 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1119` → IC=+0.187 (n=276)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.1119 (IC base=+0.150)

- **PATRÓN** `drift_15min` |x|≤ `0.4046` → IC=+0.150 (n=138)

  - _Acción_: Kelly boost +0.75€ cuando `drift_15min` |x|≤ 0.4046 (IC base=+0.150)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1408` → IC=+0.153 (n=275)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio_macro` |x|> 0.1408 (IC base=+0.150)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1366` → IC=+0.210 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1366 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.179 (n=291)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 11.0 (IC base=+0.150)

- **PATRÓN** `ibs_15` > `0.6448` → IC=+0.257 (n=413)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6448 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.5705` → IC=+0.155 (n=82)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.5705 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.2602` → IC=+0.158 (n=384)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.2602 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.1` → IC=+0.214 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.1 (IC base=+0.150)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.160 (n=533)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `11221.3084` → IC=+0.171 (n=138)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 11221.3084 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.248 (n=426)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.35` → IC=+0.242 (n=852)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.35 (IC base=+0.238)

- **PATRÓN** `drift_15min` |x|≤ `0.7631` → IC=+0.249 (n=852)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7631 (IC base=+0.238)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2098` → IC=+0.267 (n=440)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2098 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.243 (n=858)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.238)

- **PATRÓN** `ibs_15` < `0.3605` → IC=+0.271 (n=968)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3605 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `0.729` → IC=+0.297 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.729 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.337` → IC=+0.257 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.337 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.53` → IC=+0.243 (n=1017)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.53 (IC base=+0.238)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1702` → IC=-0.241 (n=276)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1702
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=537)

- **FILTRO** `drift_15min` |x|> `0.8825` → IC=-0.271 (n=203)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8825
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=610)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.243 (n=72)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.168 (n=741)

- **FILTRO** `sigma_ewma_delta_pct` > `18.28` → IC=-0.143 (n=421)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.28
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3391)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1455` → IC=+0.174 (n=44)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio_macro` |x|> 0.1455 (IC base=-0.175)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.226 (n=60)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.175)

- **PATRÓN** `dist_vwap_pct` > `0.2752` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.2752 (IC base=-0.175)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1292 (IC base=-0.175)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.221 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.175)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0787` → IC=+0.236 (n=385)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0787 (IC base=-0.039)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1879` → IC=+0.234 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1879 (IC base=-0.039)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.274 (n=432)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.6425` → IC=+0.230 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6425 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` < `0.172` → IC=+0.237 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.172 (IC base=-0.039)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1279` → IC=-0.222 (n=487)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1279
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=489)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.258 (n=320)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=656)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.203)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.203)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1479` → IC=+0.282 (n=305)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1479 (IC base=-0.029)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1101` → IC=+0.313 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1101 (IC base=-0.029)

- **PATRÓN** `ibs_15` < `0.3273` → IC=+0.295 (n=672)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3273 (IC base=-0.029)

- **PATRÓN** `dist_vwap_pct` > `0.7986` → IC=+0.353 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7986 (IC base=-0.029)

### UPDOWN_GBM_ETH_15M_HORA7
- **FILTRO** `ibs_15` < `0.8489` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8489
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=11)

- **PATRÓN** `dist_vwap_pct` > `0.1511` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1511 (IC base=+0.030)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **FILTRO** `ibs_15` < `0.8489` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8489
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=11)

- **PATRÓN** `dist_vwap_pct` > `0.1511` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1511 (IC base=+0.030)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.297 (n=569)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.053` → IC=+0.326 (n=286)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.053 (IC base=+0.293)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2394` → IC=+0.304 (n=284)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2394 (IC base=+0.293)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2224` → IC=+0.314 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2224 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.313 (n=890)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.293)

- **PATRÓN** `ibs_15` > `0.8393` → IC=+0.327 (n=852)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8393 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.4264` → IC=+0.332 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4264 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.63` → IC=+0.350 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.63 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `12836.5354` → IC=+0.310 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12836.5354 (IC base=+0.293)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.301 (n=204)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.328 (n=155)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.287)

- **PATRÓN** `drift_15min` |x|≤ `0.4172` → IC=+0.287 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4172 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2522` → IC=+0.315 (n=155)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2522 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1107` → IC=+0.304 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1107 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.309 (n=490)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.8303` → IC=+0.318 (n=464)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8303 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.4105` → IC=+0.350 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4105 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.469` → IC=+0.364 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.469 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `16217.9862` → IC=+0.334 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16217.9862 (IC base=+0.287)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.305 (n=260)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.298)

- **PATRÓN** `sigma_h` > `0.0039` → IC=+0.303 (n=348)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0039 (IC base=+0.298)

- **PATRÓN** `drift_60min` |x|≤ `0.0515` → IC=+0.318 (n=130)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0515 (IC base=+0.298)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2902` → IC=+0.318 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2902 (IC base=+0.298)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.328 (n=375)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.298)

- **PATRÓN** `ibs_15` > `0.8516` → IC=+0.339 (n=389)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8516 (IC base=+0.298)

- **PATRÓN** `dist_vwap_pct` > `0.437` → IC=+0.315 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.437 (IC base=+0.298)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.221` → IC=+0.330 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.221 (IC base=+0.298)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0876` → IC=-0.253 (n=75)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0876
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=227)

- **FILTRO** `sigma_h` > `0.0043` → IC=-0.260 (n=102)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0043
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=200)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1727` → IC=-0.180 (n=23)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1727
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=24)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2122` → IC=-0.395 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2122
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6128 sube el IC de +0.197 a +0.276 en UPDOWN_GBM#15min (n=2382). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7176 sube el IC de +0.215 a +0.277 en UPDOWN_GBM#BTC#15min (n=478). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5749 sube el IC de +0.141 a +0.241 en UPDOWN_GBM#ETH#15min (n=523). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.5357 sube el IC de +0.164 a +0.255 en UPDOWN_GBM#SOL#15min (n=332). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5854 sube el IC de +0.212 a +0.292 en UPDOWN_GBM#XRP#15min (n=590). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1136 sube el IC de +0.067 a +0.155 en UPDOWN_GBM#XRP#15min (n=635). Ya aplicado como kelly_boost=+0.77€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6347 sube el IC de -0.066 a +0.278 en UPDOWN_GBM_15M_TARDIO (n=837). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3499 sube el IC de -0.017 a +0.279 en UPDOWN_GBM_15M_TARDIO (n=2677). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7572 sube el IC de +0.087 a +0.328 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=248). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.5625 sube el IC de -0.192 a +0.333 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=40). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6448 sube el IC de +0.150 a +0.257 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=413). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3605 sube el IC de +0.238 a +0.271 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=968). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.175 a +0.226 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=60). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.039 a +0.274 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=432). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.203 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3273 sube el IC de -0.029 a +0.295 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=672). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8393 sube el IC de +0.293 a +0.327 en UPDOWN_GBM_IBS_ALTO (n=852). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8303 sube el IC de +0.287 a +0.318 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=464). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8516 sube el IC de +0.298 a +0.339 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=389). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.358 a +0.394 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=526). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8057 sube el IC de +0.359 a +0.389 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=286). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7601 sube el IC de +0.354 a +0.401 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=240). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1544 | +0.096 | +188.30€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1544 | +0.096 | +188.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1176 | +0.102 | +159.88€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1176 | +0.102 | +159.88€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 265 | +0.069 | +12.71€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 265 | +0.069 | +12.71€ | 6 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 72 | +0.108 | +16.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 72 | +0.108 | +16.05€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 194 | +0.031 | +45.85€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 194 | +0.031 | +45.85€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 160 | +0.025 | +41.22€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 160 | +0.025 | +41.22€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 12 | +0.129 | +2.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 12 | +0.129 | +2.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 22 | -0.042 | +2.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 22 | -0.042 | +2.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 34036 | -0.085 | -4560.75€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1724 | -0.015 | -218.54€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 32312 | -0.089 | -4342.21€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4352 | -0.121 | -765.28€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4352 | -0.121 | -765.28€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1724 | -0.015 | -218.54€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1724 | -0.015 | -218.54€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3979 | -0.114 | -899.31€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3979 | -0.114 | -899.31€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 8817 | +0.001 | -839.34€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 8817 | +0.001 | -839.34€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 8559 | -0.105 | -609.74€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 8559 | -0.105 | -609.74€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 6605 | -0.152 | -1228.54€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 6605 | -0.152 | -1228.54€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 25932 | -0.020 | +3764.07€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 6709 | +0.002 | +1764.61€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 19223 | -0.027 | +1999.46€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 25932 | -0.020 | +3764.07€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 6709 | +0.002 | +1764.61€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 19223 | -0.027 | +1999.46€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 116523 | +0.114 | -5165.61€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 16295 | +0.183 | -488.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 496 | -0.048 | -61.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 92501 | +0.103 | -4345.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 7231 | +0.104 | -269.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 15363 | +0.103 | -1082.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 54 | -0.143 | +10.84€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 15294 | +0.104 | -1081.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 23088 | +0.130 | -376.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4872 | +0.197 | -135.96€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 15341 | +0.116 | -147.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2833 | +0.091 | -71.03€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 15408 | +0.094 | -1230.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 61 | -0.119 | -6.11€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 15332 | +0.095 | -1213.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 24749 | +0.124 | -420.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 6601 | +0.176 | -99.80€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 15509 | +0.107 | -260.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2627 | +0.101 | -51.58€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 22535 | +0.115 | -1226.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4651 | +0.189 | -268.71€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 399 | -0.011 | -7.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 15714 | +0.094 | -803.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1771 | +0.130 | -147.20€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#XRP | 15380 | +0.102 | -829.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 56 | -0.035 | +10.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 15311 | +0.103 | -839.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 18599 | +0.194 | -1162.47€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 18599 | +0.194 | -1162.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4317 | +0.173 | -408.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4317 | +0.173 | -408.15€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 2007 | +0.203 | -27.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 2007 | +0.203 | -27.12€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 4256 | +0.182 | -342.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 4256 | +0.182 | -342.64€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3745 | +0.242 | -130.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3745 | +0.242 | -130.97€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4195 | +0.190 | -267.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4195 | +0.190 | -267.35€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 871 | +0.428 | -28.43€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 871 | +0.428 | -28.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 343 | +0.433 | -6.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 343 | +0.433 | -6.97€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 329 | +0.433 | -6.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 329 | +0.433 | -6.07€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 187 | +0.405 | -12.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 187 | +0.405 | -12.95€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 64583 | +0.200 | -4800.62€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 64583 | +0.200 | -4800.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 11111 | +0.183 | -1185.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 11111 | +0.183 | -1185.30€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 10393 | +0.224 | -359.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 10393 | +0.224 | -359.53€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 11104 | +0.177 | -1240.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 11104 | +0.177 | -1240.02€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 10448 | +0.221 | -384.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 10448 | +0.221 | -384.82€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 10697 | +0.202 | -707.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 10697 | +0.202 | -707.67€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 10830 | +0.193 | -923.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 10830 | +0.193 | -923.28€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 24584 | +0.117 | +180.48€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 24584 | +0.117 | +180.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 12210 | +0.120 | +152.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 12210 | +0.120 | +152.80€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 12374 | +0.113 | +27.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 12374 | +0.113 | +27.68€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1752 | +0.288 | -23.81€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1752 | +0.288 | -23.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 792 | +0.278 | -20.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 792 | +0.278 | -20.08€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 843 | +0.288 | -7.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 843 | +0.288 | -7.95€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 117 | +0.349 | +4.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 117 | +0.349 | +4.22€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 786 | +0.439 | +0.33€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 786 | +0.439 | +0.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 378 | +0.437 | -2.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 378 | +0.437 | -2.36€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 362 | +0.442 | +2.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 362 | +0.442 | +2.14€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1348 | +0.072 | -57.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 489 | +0.060 | -37.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 859 | +0.078 | -19.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1055 | +0.078 | -26.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 196 | +0.076 | -6.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 859 | +0.078 | -19.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 227 | +0.033 | -32.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 227 | +0.033 | -32.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 47150 | +0.100 | -1226.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3826 | +0.092 | +48.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 43324 | +0.100 | -1275.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 26155 | +0.104 | -301.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3826 | +0.092 | +48.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 22329 | +0.106 | -349.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 9333 | +0.110 | -19.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 9333 | +0.110 | -19.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 11662 | +0.081 | -906.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 11662 | +0.081 | -906.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 867 | +0.205 | -102.15€ | 3 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 867 | +0.205 | -102.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 867 | +0.205 | -102.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 867 | +0.205 | -102.15€ | 3 | 4 |
| ✅ GBM_LATE_15M | 33007 | +0.088 | +16395.19€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 33007 | +0.088 | +16395.19€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 5550 | +0.203 | +4284.47€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 5550 | +0.203 | +4284.47€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 4891 | +0.178 | +3516.00€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 4891 | +0.178 | +3516.00€ | 0 | 25 |
| ✅ GBM_LATE_15M#DOGE | 5859 | +0.201 | +4445.40€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 5859 | +0.201 | +4445.40€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 4683 | +0.033 | +1167.45€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4683 | +0.033 | +1167.45€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 4705 | -0.031 | +1028.80€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 4705 | -0.031 | +1028.80€ | 4 | 12 |
| ✅ GBM_LATE_15M#XRP | 7319 | -0.036 | +1953.06€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 7319 | -0.036 | +1953.06€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 35678 | +0.087 | +18970.27€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 35678 | +0.087 | +18970.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 6902 | +0.012 | +3559.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 6902 | +0.012 | +3559.86€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 7390 | +0.013 | +1578.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 7390 | +0.013 | +1578.45€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 5034 | +0.268 | +5186.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 5034 | +0.268 | +5186.33€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 6027 | +0.011 | +1324.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 6027 | +0.011 | +1324.58€ | 1 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 5813 | +0.035 | +2317.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 5813 | +0.035 | +2317.11€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4512 | +0.287 | +5003.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4512 | +0.287 | +5003.94€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 26404 | +0.175 | +20532.13€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 26404 | +0.175 | +20532.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3987 | +0.217 | +3351.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3987 | +0.217 | +3351.38€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 4158 | +0.150 | +3019.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 4158 | +0.150 | +3019.34€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 4189 | +0.216 | +3460.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 4189 | +0.216 | +3460.41€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 4434 | +0.138 | +3260.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 4434 | +0.138 | +3260.66€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 4950 | +0.123 | +3581.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 4950 | +0.123 | +3581.32€ | 0 | 27 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4686 | +0.212 | +3859.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4686 | +0.212 | +3859.02€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 7187 | +0.140 | +3460.13€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 7187 | +0.140 | +3460.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 340 | +0.140 | +187.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 340 | +0.140 | +187.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2138 | +0.147 | +1186.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2138 | +0.147 | +1186.34€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 375 | +0.142 | +175.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 375 | +0.142 | +175.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2192 | +0.156 | +1096.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2192 | +0.156 | +1096.26€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1605 | +0.107 | +574.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1605 | +0.107 | +574.20€ | 1 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 537 | +0.135 | +240.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 537 | +0.135 | +240.44€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 33234 | +0.181 | +25635.12€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 33234 | +0.181 | +25635.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 5288 | +0.230 | +4694.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 5288 | +0.230 | +4694.21€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 5133 | +0.149 | +3364.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 5133 | +0.149 | +3364.60€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 5557 | +0.228 | +4851.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 5557 | +0.228 | +4851.98€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 5405 | +0.136 | +3727.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 5405 | +0.136 | +3727.76€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 5870 | +0.124 | +4037.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 5870 | +0.124 | +4037.76€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 5981 | +0.216 | +4958.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 5981 | +0.216 | +4958.81€ | 0 | 23 |
| ✅ GBM_LATE_5M | 9051 | +0.178 | +6150.18€ | 1 | 30 |
| ✅ GBM_LATE_5M#5min | 9051 | +0.178 | +6150.18€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 835 | +0.229 | +729.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 835 | +0.229 | +729.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2111 | +0.169 | +1523.16€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2111 | +0.169 | +1523.16€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 992 | +0.176 | +650.38€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 992 | +0.176 | +650.38€ | 0 | 17 |
| ✅ GBM_LATE_5M#ETH | 2842 | +0.180 | +1867.48€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2842 | +0.180 | +1867.48€ | 0 | 29 |
| ✅ GBM_LATE_5M#SOL | 1134 | +0.174 | +760.14€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1134 | +0.174 | +760.14€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1137 | +0.153 | +619.61€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1137 | +0.153 | +619.61€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2452 | +0.072 | +888.50€ | 0 | 11 |
| ✅ GBM_LATE_60M#60min | 2452 | +0.072 | +888.50€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 923 | +0.090 | +342.45€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 923 | +0.090 | +342.45€ | 0 | 11 |
| ✅ GBM_LATE_60M#ETH | 767 | +0.070 | +334.93€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 767 | +0.070 | +334.93€ | 1 | 10 |
| ✅ GBM_LATE_60M#SOL | 762 | +0.051 | +211.12€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 762 | +0.051 | +211.12€ | 2 | 11 |
| 🚫 GBM_LATE_60M_FADE | 474 | -0.239 | -14.62€ | 9 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 474 | -0.239 | -14.62€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 176 | -0.219 | -7.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 176 | -0.219 | -7.05€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 165 | -0.231 | -1.91€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 165 | -0.231 | -1.91€ | 5 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 133 | -0.270 | -5.66€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 133 | -0.270 | -5.66€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1054 | +0.088 | +269.95€ | 0 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1054 | +0.088 | +269.95€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 396 | +0.078 | +82.55€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 396 | +0.078 | +82.55€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 355 | +0.060 | +50.59€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 355 | +0.060 | +50.59€ | 2 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 303 | +0.133 | +136.81€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 303 | +0.133 | +136.81€ | 1 | 13 |
| ✅ LATE_WINDOW_5MIN | 127 | +0.244 | +103.44€ | 0 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 127 | +0.244 | +103.44€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 127 | +0.244 | +103.44€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 127 | +0.244 | +103.44€ | 0 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 2782 | +0.103 | +733.72€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2782 | +0.103 | +733.72€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2782 | +0.103 | +733.72€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2782 | +0.103 | +733.72€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 424 | -0.068 | -31.31€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 424 | -0.068 | -31.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 116 | -0.034 | -1.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 116 | -0.034 | -1.97€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 68 | -0.086 | -7.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 68 | -0.086 | -7.96€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 159 | -0.022 | -4.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 159 | -0.022 | -4.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 2848 | +0.023 | +78.34€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2848 | +0.023 | +78.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 141 | +0.038 | +0.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 141 | +0.038 | +0.40€ | 1 | 2 |
| ✅ LIQUIDACIONES_5M#BTC | 435 | +0.026 | +32.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 435 | +0.026 | +32.30€ | 4 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 202 | -0.020 | -5.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 202 | -0.020 | -5.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1066 | +0.032 | +32.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1066 | +0.032 | +32.08€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 648 | +0.017 | +3.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 648 | +0.017 | +3.67€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 356 | +0.020 | +15.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 356 | +0.020 | +15.50€ | 1 | 2 |
| ✅ LIQUIDACIONES_60M | 1392 | -0.044 | -29.12€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1392 | -0.044 | -29.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 398 | -0.043 | -14.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 398 | -0.043 | -14.11€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 456 | -0.022 | +1.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 456 | -0.022 | +1.42€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 538 | -0.065 | -16.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 538 | -0.065 | -16.43€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 4578 | -0.013 | +141.14€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 2167 | -0.017 | +47.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 2411 | -0.010 | +93.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 128 | +0.000 | +5.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 64 | +0.045 | +10.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 64 | -0.045 | -4.73€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 1127 | -0.005 | +39.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 534 | -0.011 | +8.96€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 593 | +0.001 | +30.12€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 519 | -0.013 | +22.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 256 | -0.023 | +4.00€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 263 | -0.002 | +18.18€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 940 | -0.035 | -23.17€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 431 | -0.050 | -27.21€ | 4 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 509 | -0.022 | +4.04€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 894 | -0.012 | +37.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 436 | -0.009 | +24.79€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 458 | -0.015 | +12.70€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 970 | -0.005 | +60.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 446 | -0.004 | +26.65€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 524 | -0.006 | +33.44€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 38203 | -0.004 | +1788.74€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 38203 | -0.004 | +1788.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 6806 | +0.024 | +906.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 6806 | +0.024 | +906.03€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 5700 | -0.032 | -95.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 5700 | -0.032 | -95.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 6905 | +0.019 | +681.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 6905 | +0.019 | +681.42€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 5499 | -0.051 | -161.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 5499 | -0.051 | -161.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 6443 | -0.009 | +190.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 6443 | -0.009 | +190.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 6850 | +0.012 | +266.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 6850 | +0.012 | +266.95€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6174 | -0.059 | -143.44€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6174 | -0.059 | -143.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1219 | +0.001 | -13.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1219 | +0.001 | -13.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1522 | -0.077 | -32.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1522 | -0.077 | -32.57€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 711 | -0.124 | -33.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 711 | -0.124 | -33.17€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1821 | -0.077 | -34.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1821 | -0.077 | -34.09€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 95872 | -0.073 | +1597.62€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 95872 | -0.073 | +1597.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 16477 | -0.074 | +876.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 16477 | -0.074 | +876.97€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 14566 | -0.098 | -775.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 14566 | -0.098 | -775.41€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 16728 | -0.066 | +912.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 16728 | -0.066 | +912.78€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 14098 | -0.095 | -416.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 14098 | -0.095 | -416.81€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 17374 | -0.052 | +315.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 17374 | -0.052 | +315.80€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 16629 | -0.064 | +684.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 16629 | -0.064 | +684.28€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8063 | -0.031 | -149.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8063 | -0.031 | -149.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1921 | -0.042 | -17.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1921 | -0.042 | -17.94€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2242 | -0.025 | -30.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2242 | -0.025 | -30.43€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1115 | -0.049 | -23.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1115 | -0.049 | -23.18€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 781 | -0.022 | -25.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 781 | -0.022 | -25.23€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1371 | +0.115 | +505.86€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1235 | +0.122 | +493.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 288 | +0.141 | +148.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 288 | +0.141 | +148.99€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 233 | +0.104 | +62.96€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 233 | +0.104 | +62.96€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 252 | +0.114 | +98.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 252 | +0.114 | +98.87€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 221 | +0.146 | +115.32€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 221 | +0.146 | +115.32€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 241 | +0.097 | +67.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 241 | +0.097 | +67.12€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 919 | -0.017 | -21.90€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 919 | -0.017 | -21.90€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 181 | +0.008 | +9.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 181 | +0.008 | +9.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 133 | -0.018 | -4.03€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 133 | -0.018 | -4.03€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 246 | -0.040 | -19.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 246 | -0.040 | -19.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 201 | +0.012 | +3.82€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 201 | +0.012 | +3.82€ | 0 | 0 |
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
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 317 | -0.199 | -33.81€ | 4 | 0 |
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
| ✅ STREAK_FADE_5M | 3091 | -0.021 | -120.43€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3091 | -0.021 | -120.43€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 909 | -0.020 | -31.15€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 909 | -0.020 | -31.15€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 580 | -0.026 | -25.19€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 580 | -0.026 | -25.19€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1446 | -0.017 | -49.68€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1446 | -0.017 | -49.68€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 88 | -0.056 | -9.21€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 88 | -0.056 | -9.21€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 50 | -0.019 | -4.76€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 50 | -0.019 | -4.76€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 9709 | +0.019 | +108.60€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 9709 | +0.019 | +108.60€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2632 | +0.021 | +28.30€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2632 | +0.021 | +28.30€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2301 | +0.028 | +51.18€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2301 | +0.028 | +51.18€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2861 | +0.010 | -0.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2861 | +0.010 | -0.81€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1915 | +0.021 | +29.94€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1915 | +0.021 | +29.94€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 8745 | +0.013 | -44.38€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 8745 | +0.013 | -44.38€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3458 | +0.017 | -8.64€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3458 | +0.017 | -8.64€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3455 | +0.012 | -22.78€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3455 | +0.012 | -22.78€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1832 | +0.008 | -12.96€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1832 | +0.008 | -12.96€ | 1 | 0 |
| ✅ UPDOWN_GBM | 57446 | +0.045 | +4443.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 14289 | +0.081 | +3034.27€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 1895 | +0.004 | +6.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 37762 | +0.039 | +1355.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 3301 | +0.006 | +47.28€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 5896 | +0.081 | +803.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1176 | +0.155 | +508.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 43 | -0.033 | -1.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 4677 | +0.064 | +296.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 11089 | +0.050 | +894.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1825 | +0.090 | +420.54€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 502 | +0.012 | +5.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 7191 | +0.054 | +424.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1497 | +0.006 | +41.65€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 74 | -0.079 | +2.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 6880 | +0.056 | +590.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1148 | +0.143 | +430.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 41 | -0.012 | -2.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 5691 | +0.039 | +162.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 12563 | +0.035 | +689.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3445 | +0.056 | +454.39€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 495 | +0.007 | +8.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 7437 | +0.034 | +223.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1121 | +0.004 | -0.59€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 65 | -0.112 | +3.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 12763 | +0.024 | +469.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 3377 | +0.033 | +287.33€ | 0 | 12 |
| ✅ UPDOWN_GBM#SOL#240min | 485 | -0.001 | -0.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 8160 | +0.024 | +181.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 683 | +0.009 | +6.22€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 58 | -0.150 | -5.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 8253 | +0.053 | +998.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3318 | +0.101 | +932.57€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 329 | +0.004 | -1.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 4606 | +0.023 | +67.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 197 | -0.113 | +1.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 701 | +0.358 | +239.80€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 701 | +0.358 | +239.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 381 | +0.359 | +125.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 381 | +0.359 | +125.94€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 320 | +0.354 | +113.86€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 320 | +0.354 | +113.86€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 15881 | -0.028 | +3694.19€ | 2 | 9 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 15881 | -0.028 | +3694.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1279 | -0.053 | +432.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1279 | -0.053 | +432.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2784 | -0.113 | +119.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2784 | -0.113 | +119.06€ | 3 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 705 | +0.210 | +557.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 705 | +0.210 | +557.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1840 | +0.212 | +1157.09€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1840 | +0.212 | +1157.09€ | 1 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 4625 | -0.063 | +613.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 4625 | -0.063 | +613.35€ | 4 | 10 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 4648 | -0.066 | +815.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 4648 | -0.066 | +815.07€ | 2 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 178 | +0.028 | +6.60€ | 1 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 178 | +0.028 | +6.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 178 | +0.028 | +6.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 178 | +0.028 | +6.60€ | 1 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1136 | +0.293 | +937.87€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1136 | +0.293 | +937.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 618 | +0.287 | +475.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 618 | +0.287 | +475.56€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 518 | +0.298 | +462.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 518 | +0.298 | +462.30€ | 0 | 8 |
| ✅ UPDOWN_OU_5M | 760 | -0.116 | -86.66€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#5min | 760 | -0.116 | -86.66€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 224 | -0.088 | -18.30€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 224 | -0.088 | -18.30€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 74 | -0.171 | -10.29€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 74 | -0.171 | -10.29€ | 2 | 0 |
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
  - _Estado_: 617 celda(s) pasan gate riguroso completo de 2456 evaluadas (n>=40) y 3434 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.033 < 0.08 — monitorear
  - _Datos_: n=3375 IC=+0.033 PNL=+283.40€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.130 n=552/60 | contraria IC=+0.190 n=560 | gap=-0.060 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=379, boost estimado=+0.008. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1119/40 IC=+0.004 PNL=-0.56€ | BTC#60min: n=1495/40 IC=+0.006 PNL=+41.70€ | SOL#60min: n=682/40 IC=+0.010 PNL=+6.73€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.048 n=436841 | tras_1loss IC=+0.089 n=335125 | tras_2loss IC=+0.058 n=137800/40 | gap=-0.009 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.202 > 0.08 con n=478 PNL=+357.44€
  - _Datos_: n=478 IC=+0.202 PNL=+357.44€

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
  - _Estado_: n=2227 IC=+0.010 PNL=+9.10€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2227 IC=+0.010 PNL=+9.10€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1069 IC=-0.001 PNL=+38.77€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1069 IC=-0.001 PNL=+38.77€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.197 > 0.1 con n=3161 PNL=+2168.42€
  - _Datos_: n=3161 IC=+0.197 PNL=+2168.42€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1822 IC=+0.089 PNL=+415.70€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1822 IC=+0.089 PNL=+415.70€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.121 > 0.02 con n=786 PNL=+306.40€
  - _Datos_: n=786 IC=+0.121 PNL=+306.40€

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
  - _Estado_: n=21439 IC=+0.069 PNL=+2949.06€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=21439 IC=+0.069 PNL=+2949.06€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.145 < -0.1 con n=339 PNL=+34.38€
  - _Datos_: n=339 IC=-0.145 PNL=+34.38€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2531 IC=+0.067 PNL=+303.40€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2531 IC=+0.067 PNL=+303.40€

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
  - _Estado_: n=23907 IC=-0.136 PNL=+1712.73€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=23907 IC=-0.136 PNL=+1712.73€

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
  - _Estado_: n=2448 IC=+0.135 PNL=+1401.56€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2448 IC=+0.135 PNL=+1401.56€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=6026 IC=+0.042 PNL=+385.51€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6026 IC=+0.042 PNL=+385.51€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.088 > 0.08 con n=2723 PNL=+1438.09€
  - _Datos_: n=2723 IC=+0.088 PNL=+1438.09€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.228 < -0.1 con n=2433 PNL=-205.48€
  - _Datos_: n=2433 IC=-0.228 PNL=-205.48€

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.102 n=1417) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1417 IC=+0.102 PNL=+323.36€

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
  - _Estado_: n=11102 IC=+0.183 PNL=-1185.13€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=11102 IC=+0.183 PNL=-1185.13€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.208 > 0.1 con n=176 PNL=+108.01€
  - _Datos_: n=176 IC=+0.208 PNL=+108.01€
