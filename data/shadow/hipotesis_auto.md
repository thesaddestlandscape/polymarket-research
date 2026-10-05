# Hipótesis automáticas — 2026-10-05 17:25 UTC
_Generado por shadow_postmortem.py sobre 763016 resoluciones (PNL=+93072.52€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=575)

- **PATRÓN** `py_entrada` > `0.51` → IC=+0.239 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.51 (IC base=+0.129)

- **PATRÓN** `n_total_lado` > `71.0` → IC=+0.215 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 71.0 (IC base=+0.129)

- **PATRÓN** `banda_hit_calibrado` > `0.7988` → IC=+0.263 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7988 (IC base=+0.129)

- **PATRÓN** `banda_z` > `9.307` → IC=+0.182 (n=212)

  - _Acción_: Kelly boost +0.91€ cuando `banda_z` > 9.307 (IC base=+0.129)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.702` → IC=+0.129 (n=567)

  - _Acción_: Kelly boost +0.65€ cuando `ballenas_wallet_edge_medio` > 0.702 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.156 (n=219)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=672)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `3077.5494` → IC=+0.132 (n=424)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 3077.5494 (IC base=+0.129)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=438)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.219 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.136)

- **PATRÓN** `n_total_lado` > `42.0` → IC=+0.164 (n=471)

  - _Acción_: Kelly boost +0.82€ cuando `n_total_lado` > 42.0 (IC base=+0.136)

- **PATRÓN** `banda_hit_calibrado` > `0.6177` → IC=+0.253 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6177 (IC base=+0.136)

- **PATRÓN** `banda_z` > `9.958` → IC=+0.198 (n=170)

  - _Acción_: Kelly boost +0.99€ cuando `banda_z` > 9.958 (IC base=+0.136)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.888` → IC=+0.139 (n=413)

  - _Acción_: Kelly boost +0.69€ cuando `ballenas_wallet_edge_medio` > 0.888 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=574)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.136)

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

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.297 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.125)

- **PATRÓN** `banda_hit_calibrado` > `0.8094` → IC=+0.257 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8094 (IC base=+0.125)

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
- **FILTRO** `restante_s_al_confirmar` < `143.98` → IC=-0.214 (n=8410)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 143.98
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=25233)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `131.91` → IC=-0.269 (n=1076)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.91
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=3229)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `124.67` → IC=-0.302 (n=980)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 124.67
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=2943)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `164.85` → IC=-0.221 (n=2113)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 164.85
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=6339)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `128.58` → IC=-0.314 (n=1631)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.58
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=4893)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.214 (n=16225)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.104)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=3886)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `5380.041` → IC=+0.170 (n=2525)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 5380.041 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.136 (n=14285)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.134 (n=17480)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.229 (n=13394)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.164 (n=6380)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7609.4381` → IC=+0.168 (n=2446)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 7609.4381 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.206 (n=1896)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.200 (n=1849)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.348 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=2328)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `16054.6223` → IC=+0.214 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16054.6223 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.201 (n=1671)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=1855)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.197 (n=2378)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `16003.8489` → IC=+0.212 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16003.8489 (IC base=+0.195)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.555` → IC=+0.124 (n=1035)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.555 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `4587.7919` → IC=+0.123 (n=250)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 4587.7919 (IC base=+0.092)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.134 (n=435)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.090)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.135 (n=943)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.44 (IC base=+0.090)

- **PATRÓN** `libro_liquidez` > `5754.4405` → IC=+0.144 (n=234)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 5754.4405 (IC base=+0.090)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=3409)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.356 (n=1125)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.232 (n=1528)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` < `0.235` → IC=+0.363 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.235 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.227 (n=1770)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.222)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=846)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.144 (n=729)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.137)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.254 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=657)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2154.4479` → IC=+0.156 (n=367)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2154.4479 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.074)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.237 (n=809)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.214)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.407 (n=982)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.214)

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
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.181 (n=321)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 7.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.372 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.156 (n=193)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.155 (n=363)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.220 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.118)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.284 (n=132)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=68)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=14394)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.201 (n=12233)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.228 (n=6129)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.178 (n=3204)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 6.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.177 (n=3215)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 17.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.180 (n=3258)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.73 (IC base=+0.175)

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

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.238 (n=1243)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.231)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.233 (n=1401)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.231)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.334 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.231)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.188 (n=3161)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 6.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.187 (n=3188)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.188 (n=2658)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.252 (n=2927)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.242)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.332 (n=1007)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.193 (n=3259)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=2795)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.191 (n=2461)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.71 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.196 (n=1176)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.73 (IC base=+0.189)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.436 (n=594)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.441 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.431)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.431)

- **PATRÓN** `libro_liquidez` > `3933.4924` → IC=+0.442 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3933.4924 (IC base=+0.431)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.435 (n=261)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.443 (n=173)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.451 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.436)

- **PATRÓN** `libro_liquidez` > `14878.5401` → IC=+0.442 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14878.5401 (IC base=+0.436)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.447 (n=244)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.466 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.436)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.434 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.436)

- **PATRÓN** `libro_liquidez` > `3371.5411` → IC=+0.452 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3371.5411 (IC base=+0.436)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.408 (n=128)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.409)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.413 (n=124)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.409)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.420 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.409)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.419 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.409)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=24)

- **FILTRO** `libro_liquidez` < `7880.4556` → IC=-0.344 (n=30)

  - _Acción_: SKIP cuando `libro_liquidez` < 7880.4556
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.203 (n=42896)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.242 (n=18859)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.186 (n=7389)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.185 (n=5924)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.198 (n=8129)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.71 (IC base=+0.183)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=3830)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.268 (n=4368)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.180 (n=7801)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 7.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.192 (n=7800)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.235 (n=3860)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.273 (n=2644)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.206 (n=7114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.204 (n=5689)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.260 (n=2819)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.200 (n=3048)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.243 (n=3274)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=6581)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` < `4.19` → IC=+0.125 (n=6103)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.19 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=6365)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.47` → IC=+0.137 (n=6080)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.47 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=3292)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` < `4.16` → IC=+0.127 (n=3023)

  - _Acción_: Kelly boost +0.64€ cuando `restante_min` < 4.16 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.141 (n=3181)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.95 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.135 (n=3995)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `3.15` → IC=+0.145 (n=3020)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 3.15 (IC base=+0.120)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.188 (n=3289)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.113)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.131 (n=3487)

  - _Acción_: Kelly boost +0.65€ cuando `restante_min` > 4.96 (IC base=+0.113)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.135 (n=3072)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.25 (IC base=+0.113)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.313 (n=930)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.289 (n=1306)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.289)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.379 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `4186.9259` → IC=+0.305 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4186.9259 (IC base=+0.289)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.292 (n=618)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.280)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.334 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `3795.9101` → IC=+0.289 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3795.9101 (IC base=+0.280)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.318 (n=444)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.288)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.295 (n=656)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.388 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `1430.8899` → IC=+0.303 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1430.8899 (IC base=+0.288)

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
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.442 (n=585)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.440 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.440 (n=694)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.439)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.441 (n=252)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.438 (n=287)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.437 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.445 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.436)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.459 (n=95)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.442)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.442 (n=101)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.451 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.443 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.443 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.442)

- **PATRÓN** `libro_liquidez` > `2139.052` → IC=+0.457 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2139.052 (IC base=+0.442)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4859` → IC=+0.130 (n=10272)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.4859 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.9841` → IC=+0.243 (n=3423)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9841 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.2166` → IC=+0.255 (n=2287)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2166 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.031` → IC=+0.183 (n=3894)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 6.031 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.211` → IC=+0.251 (n=2869)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.211 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` > `0.6161` → IC=+0.255 (n=2869)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6161 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.3035` → IC=+0.225 (n=1041)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3035 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `1.4666` → IC=+0.211 (n=7185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4666 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.5655` → IC=+0.139 (n=12482)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.5655 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.5793` → IC=+0.203 (n=892)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5793 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` < `0.1474` → IC=+0.180 (n=4169)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.1474 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` < `0.6966` → IC=+0.182 (n=2015)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6966 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` > `1.0532` → IC=+0.179 (n=2074)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 1.0532 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` > `0.2953` → IC=+0.226 (n=1145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2953 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` > `1.5683` → IC=+0.201 (n=7001)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5683 (IC base=+0.070)

- **PATRÓN** `ballena_activa_n` < `116.0` → IC=+0.215 (n=7646)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 116.0 (IC base=+0.070)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.223 (n=764)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.185 (n=764)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.008 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.3505` → IC=+0.185 (n=2287)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.3505 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.192 (n=1110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 15.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.184 (n=1527)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 11.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.277 (n=924)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.766` → IC=+0.296 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.766 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.228 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `1.4339` → IC=+0.180 (n=2164)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4339 (IC base=+0.179)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.195 (n=2351)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.04 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `2047.9302` → IC=+0.186 (n=763)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2047.9302 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.243 (n=1635)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.0888` → IC=+0.265 (n=610)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0888 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.257 (n=669)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.0613` → IC=+0.284 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0613 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.514` → IC=+0.247 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.514 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.408` → IC=+0.237 (n=1914)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.408 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` < `0.0939` → IC=+0.233 (n=1614)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0939 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.2821` → IC=+0.265 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2821 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.6087` → IC=+0.250 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6087 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.234 (n=2003)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.233)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.241 (n=798)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.3531` → IC=+0.231 (n=1807)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3531 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.235 (n=1813)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` > `0.9785` → IC=+0.264 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9785 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` > `0.1889` → IC=+0.222 (n=961)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1889 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` < `0.5455` → IC=+0.224 (n=1902)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5455 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.792` → IC=+0.259 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.792 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` < `1.2499` → IC=+0.223 (n=1807)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2499 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` > `0.6169` → IC=+0.224 (n=1807)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6169 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.2805` → IC=+0.234 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2805 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.4155` → IC=+0.242 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4155 (IC base=+0.219)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.183 (n=606)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0026 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.162 (n=605)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=691)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.141 (n=822)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 7.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.7204` → IC=+0.177 (n=1814)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.7204 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1278` → IC=+0.156 (n=1633)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1278 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.356` → IC=+0.146 (n=289)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 11.356 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.3` → IC=+0.142 (n=1665)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.3 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.204` → IC=+0.148 (n=1814)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.204 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `0.6207` → IC=+0.138 (n=1816)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.6207 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.0974` → IC=+0.172 (n=657)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.0974 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.4565` → IC=+0.150 (n=1702)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4565 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.7854` → IC=+0.146 (n=1135)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.7854 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `14181.4555` → IC=+0.141 (n=1209)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 14181.4555 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `230.0` → IC=+0.170 (n=714)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 230.0 (IC base=+0.137)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.201 (n=2310)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.195 (n=2313)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 6.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.194 (n=2077)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.263 (n=892)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.376` → IC=+0.258 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.376 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.196 (n=2025)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.35` → IC=+0.195 (n=306)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.35 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `1.768` → IC=+0.198 (n=1984)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.768 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.197 (n=2763)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `2029.6962` → IC=+0.203 (n=770)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2029.6962 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.221 (n=1794)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.1765` → IC=+0.224 (n=896)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1765 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=769)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.212 (n=951)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.0652` → IC=+0.232 (n=896)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0652 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.687` → IC=+0.247 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.687 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.3473` → IC=+0.254 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3473 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.7283` → IC=+0.215 (n=838)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7283 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.7404` → IC=+0.226 (n=863)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7404 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.212 (n=1183)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `1826.26` → IC=+0.213 (n=1357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1826.26 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.214 (n=1837)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.211)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=124)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=2753)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.154 (n=437)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0036 (IC base=+0.041)

- **PATRÓN** `ibs_20min` > `0.9598` → IC=+0.222 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9598 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` < `0.5163` → IC=+0.322 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5163 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.913` → IC=+0.173 (n=910)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 4.913 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` < `0.8553` → IC=+0.333 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8553 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` > `1.2207` → IC=+0.328 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2207 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.1112` → IC=+0.331 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1112 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` < `1.427` → IC=+0.356 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.427 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` > `1.8501` → IC=+0.321 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8501 (IC base=+0.041)

- **PATRÓN** `ballena_activa_n` < `153.0` → IC=+0.326 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 153.0 (IC base=+0.041)

- **PATRÓN** `ibs_20min` < `0.0987` → IC=+0.162 (n=720)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.0987 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` > `0.2992` → IC=+0.194 (n=335)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.2992 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` < `0.8504` → IC=+0.156 (n=762)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8504 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.2877` → IC=+0.208 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2877 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` > `1.5315` → IC=+0.165 (n=973)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.5315 (IC base=+0.028)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.175 (n=75)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=420)

- **FILTRO** `ibs_20min` < `0.3111` → IC=-0.180 (n=123)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3111
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=372)

- **FILTRO** `ibs_20min` > `0.2308` → IC=-0.126 (n=2777)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2308
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=1374)

- **FILTRO** `sigma_ewma_delta_pct` > `8.795` → IC=-0.218 (n=435)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.795
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=3716)

- **PATRÓN** `ibs_20min` > `0.7913` → IC=+0.202 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7913 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` > `0.9803` → IC=+0.297 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9803 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.351` → IC=+0.134 (n=173)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 2.351 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` < `0.8994` → IC=+0.270 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8994 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` > `1.0815` → IC=+0.296 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0815 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` < `0.1509` → IC=+0.286 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1509 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` < `2.1695` → IC=+0.290 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1695 (IC base=+0.041)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.284 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.041)

- **PATRÓN** `ibs_20min` < `0.2308` → IC=+0.136 (n=1374)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.2308 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.1758` → IC=+0.270 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1758 (IC base=-0.039)

- **PATRÓN** `volumen_regimen` < `0.7007` → IC=+0.274 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7007 (IC base=-0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.1612` → IC=+0.321 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1612 (IC base=-0.039)

- **PATRÓN** `volumen_spike_ratio` < `2.4232` → IC=+0.290 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4232 (IC base=-0.039)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.641` → IC=-0.177 (n=728)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.641
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=2186)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.206 (n=729)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2185)

- **FILTRO** `ibs_20min` > `0.7664` → IC=-0.206 (n=1078)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7664
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=3237)

- **PATRÓN** `dist_vwap_pct` > `0.7626` → IC=+0.316 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7626 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` < `0.2747` → IC=+0.312 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2747 (IC base=-0.069)

- **PATRÓN** `volumen_regimen` < `0.988` → IC=+0.297 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.988 (IC base=-0.069)

- **PATRÓN** `volumen_regimen` > `0.6476` → IC=+0.310 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6476 (IC base=-0.069)

- **PATRÓN** `volumen_pendiente_norm` < `0.1025` → IC=+0.303 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1025 (IC base=-0.069)

- **PATRÓN** `volumen_spike_ratio` < `2.4802` → IC=+0.299 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4802 (IC base=-0.069)

- **PATRÓN** `volumen_spike_ratio` > `1.8591` → IC=+0.301 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8591 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` > `0.851` → IC=+0.286 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.851 (IC base=-0.013)

- **PATRÓN** `volumen_regimen` < `0.722` → IC=+0.249 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.722 (IC base=-0.013)

- **PATRÓN** `volumen_regimen` > `1.0723` → IC=+0.277 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0723 (IC base=-0.013)

- **PATRÓN** `volumen_pendiente_norm` > `0.099` → IC=+0.265 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.099 (IC base=-0.013)

- **PATRÓN** `volumen_spike_ratio` < `2.1485` → IC=+0.256 (n=860)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1485 (IC base=-0.013)

- **PATRÓN** `volumen_spike_ratio` > `1.4219` → IC=+0.255 (n=978)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4219 (IC base=-0.013)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.198 (n=4477)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0095 (IC base=+0.099)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.187 (n=11990)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4706 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.9754` → IC=+0.286 (n=1073)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9754 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.691` → IC=+0.155 (n=6096)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 3.691 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` < `1.1766` → IC=+0.247 (n=4896)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1766 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` > `0.6921` → IC=+0.255 (n=4373)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6921 (IC base=+0.099)

- **PATRÓN** `volumen_pendiente_norm` < `0.1098` → IC=+0.243 (n=7611)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1098 (IC base=+0.099)

- **PATRÓN** `volumen_pendiente_norm` > `0.2954` → IC=+0.255 (n=1127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2954 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` < `1.4683` → IC=+0.242 (n=2636)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4683 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` > `2.6488` → IC=+0.255 (n=2634)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6488 (IC base=+0.099)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.276 (n=7459)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.099)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.166 (n=4325)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.009 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.5455` → IC=+0.157 (n=11419)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.5455 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.6844` → IC=+0.251 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6844 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.236` → IC=+0.250 (n=3747)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.236 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.7077` → IC=+0.251 (n=1728)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7077 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.1975` → IC=+0.262 (n=1309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1975 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2964` → IC=+0.306 (n=770)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2964 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.5921` → IC=+0.279 (n=2393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5921 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.281 (n=5327)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 78.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2587` → IC=-0.162 (n=932)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2587
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=2797)

- **FILTRO** `ibs_20min` > `0.7588` → IC=-0.174 (n=766)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7588
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=2300)

- **FILTRO** `sigma_ewma_delta_pct` > `4.599` → IC=-0.175 (n=687)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.599
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=2379)

- **PATRÓN** `ibs_20min` > `0.9091` → IC=+0.276 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9091 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.259` → IC=+0.204 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.259 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2277` → IC=+0.269 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2277 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.4416` → IC=+0.215 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4416 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` > `2.2012` → IC=+0.228 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2012 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.228 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2231` → IC=+0.430 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2231 (IC base=-0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.5483` → IC=+0.428 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5483 (IC base=-0.025)

- **PATRÓN** `volumen_spike_ratio` > `1.5249` → IC=+0.425 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5249 (IC base=-0.025)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.432 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=-0.025)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8651` → IC=+0.162 (n=899)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.8651 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` > `0.1138` → IC=+0.194 (n=694)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1138 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` < `1.2024` → IC=+0.169 (n=1264)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.2024 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` > `0.6774` → IC=+0.181 (n=1130)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.6774 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` < `0.0754` → IC=+0.171 (n=1164)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.0754 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.2741` → IC=+0.216 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2741 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` < `1.4274` → IC=+0.195 (n=414)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4274 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` > `2.4308` → IC=+0.185 (n=414)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.4308 (IC base=+0.028)

- **PATRÓN** `ballena_activa_n` < `230.0` → IC=+0.230 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 230.0 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` < `0.1497` → IC=+0.228 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1497 (IC base=+0.000)

- **PATRÓN** `volumen_regimen` > `0.6146` → IC=+0.229 (n=752)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6146 (IC base=+0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.2713` → IC=+0.300 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2713 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` < `1.4389` → IC=+0.235 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4389 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` > `2.1744` → IC=+0.236 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1744 (IC base=+0.000)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.273 (n=2037)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.252)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.256 (n=2052)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.252)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.252 (n=2058)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.252)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=1064)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.252)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.805` → IC=+0.283 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.805 (IC base=+0.252)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.267 (n=1742)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.252)

- **PATRÓN** `volumen_spike_ratio` > `2.182` → IC=+0.263 (n=1299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.182 (IC base=+0.252)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.261 (n=2415)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.252)

- **PATRÓN** `libro_liquidez` > `1949.2551` → IC=+0.270 (n=924)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1949.2551 (IC base=+0.252)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.301 (n=1694)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.179` → IC=+0.300 (n=745)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.179 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.319 (n=568)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.286)

- **PATRÓN** `ibs_20min` < `0.359` → IC=+0.292 (n=1693)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.359 (IC base=+0.286)

- **PATRÓN** `ibs_20min` > `0.1` → IC=+0.287 (n=1132)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.693` → IC=+0.297 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.693 (IC base=+0.286)

- **PATRÓN** `volumen_pendiente_norm` > `0.1211` → IC=+0.291 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1211 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` < `1.7245` → IC=+0.298 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7245 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` > `2.6496` → IC=+0.292 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6496 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `1942.2984` → IC=+0.299 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1942.2984 (IC base=+0.286)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.287 (n=1381)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.286)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7682` → IC=-0.182 (n=777)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7682
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=2332)

- **PATRÓN** `ibs_20min` > `0.9028` → IC=+0.170 (n=706)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.9028 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.3692` → IC=+0.222 (n=860)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3692 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `1.0078` → IC=+0.243 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0078 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` < `0.1712` → IC=+0.232 (n=965)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1712 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.0824` → IC=+0.230 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0824 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.4175` → IC=+0.257 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4175 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `138.0` → IC=+0.253 (n=892)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 138.0 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.122` → IC=+0.238 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.122 (IC base=-0.003)

- **PATRÓN** `volumen_regimen` < `1.0403` → IC=+0.224 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0403 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2957` → IC=+0.279 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2957 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.8479` → IC=+0.268 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8479 (IC base=-0.003)

- **PATRÓN** `ballena_activa_n` < `132.0` → IC=+0.257 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 132.0 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7619` → IC=-0.186 (n=1428)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7619
  - _Potencial_: sin este filtro IC_bueno=+0.285 (n=1428)

- **FILTRO** `ibs_20min` > `0.6694` → IC=-0.244 (n=717)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6694
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=2154)

- **FILTRO** `sigma_ewma_delta_pct` > `4.818` → IC=-0.203 (n=608)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.818
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=2263)

- **PATRÓN** `ibs_20min` > `0.7619` → IC=+0.285 (n=1428)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7619 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `0.2143` → IC=+0.319 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2143 (IC base=+0.049)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.69` → IC=+0.164 (n=448)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 9.69 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.311 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8616 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` > `0.6395` → IC=+0.306 (n=1086)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6395 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` < `0.0993` → IC=+0.302 (n=1021)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0993 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.2759` → IC=+0.324 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2759 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` < `1.4408` → IC=+0.322 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4408 (IC base=+0.049)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.325 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.049)

- **PATRÓN** `ibs_20min` < `0.5692` → IC=+0.133 (n=1895)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.5692 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` < `0.2683` → IC=+0.241 (n=770)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2683 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `0.7056` → IC=+0.270 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7056 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `1.1889` → IC=+0.232 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1889 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.0703` → IC=+0.263 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0703 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `2.4411` → IC=+0.249 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4411 (IC base=+0.022)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.262 (n=799)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.022)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.331 (n=1456)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0105 (IC base=+0.286)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.305 (n=767)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.286)

- **PATRÓN** `ibs_20min` > `0.7461` → IC=+0.328 (n=1456)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7461 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.2148` → IC=+0.319 (n=952)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2148 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.765` → IC=+0.309 (n=814)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.765 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.926` → IC=+0.286 (n=1836)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.926 (IC base=+0.286)

- **PATRÓN** `volumen_regimen` > `0.8619` → IC=+0.312 (n=1086)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8619 (IC base=+0.286)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.334 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` > `1.4339` → IC=+0.298 (n=1556)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4339 (IC base=+0.286)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.289 (n=1592)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `2642.1577` → IC=+0.299 (n=1086)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2642.1577 (IC base=+0.286)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.322 (n=1351)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.286)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.317 (n=1152)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.1888` → IC=+0.289 (n=760)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1888 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.290 (n=1543)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.286)

- **PATRÓN** `ibs_20min` < `0.3726` → IC=+0.311 (n=1727)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3726 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.3061` → IC=+0.296 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3061 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.516` → IC=+0.299 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.516 (IC base=+0.286)

- **PATRÓN** `volumen_regimen` < `0.7176` → IC=+0.286 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7176 (IC base=+0.286)

- **PATRÓN** `volumen_regimen` > `1.2304` → IC=+0.317 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2304 (IC base=+0.286)

- **PATRÓN** `volumen_pendiente_norm` > `0.2331` → IC=+0.333 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2331 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` < `1.4216` → IC=+0.295 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4216 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` > `2.1363` → IC=+0.284 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1363 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `2636.5754` → IC=+0.287 (n=1151)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2636.5754 (IC base=+0.286)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.187 (n=3344)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0047 (IC base=+0.174)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.206 (n=3343)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.3555` → IC=+0.185 (n=8825)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.3555 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=10476)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.5685` → IC=+0.227 (n=10028)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5685 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.1716` → IC=+0.199 (n=4341)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1716 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.468` → IC=+0.251 (n=2020)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.468 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `1.2089` → IC=+0.167 (n=6666)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2089 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` > `0.6308` → IC=+0.162 (n=6666)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6308 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.2956` → IC=+0.196 (n=1493)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2956 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `1.452` → IC=+0.174 (n=3224)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.452 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `2.613` → IC=+0.182 (n=3225)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.613 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `1989.5584` → IC=+0.177 (n=8958)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 1989.5584 (IC base=+0.174)

- **PATRÓN** `ballena_activa_n` < `104.0` → IC=+0.189 (n=8938)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 104.0 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.189 (n=6389)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0066 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.0801` → IC=+0.222 (n=3190)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0801 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=3626)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` < `0.4872` → IC=+0.230 (n=9570)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4872 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` < `0.1689` → IC=+0.170 (n=6650)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1689 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.32` → IC=+0.197 (n=1604)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.32 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` < `1.1783` → IC=+0.164 (n=6865)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1783 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` > `0.2922` → IC=+0.216 (n=1387)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2922 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` < `1.5615` → IC=+0.173 (n=3902)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5615 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `2.6147` → IC=+0.176 (n=2956)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.6147 (IC base=+0.175)

- **PATRÓN** `ballena_activa_n` < `107.0` → IC=+0.183 (n=8542)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 107.0 (IC base=+0.175)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.240 (n=564)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.199)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.203 (n=561)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.3418` → IC=+0.220 (n=1684)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3418 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.203 (n=1683)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.202 (n=1228)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` > `0.9155` → IC=+0.286 (n=1122)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9155 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.283` → IC=+0.333 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.283 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.249 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `1.4343` → IC=+0.198 (n=1575)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4343 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=1739)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `2048.64` → IC=+0.200 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2048.64 (IC base=+0.199)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.248 (n=1123)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.241)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.250 (n=1140)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.1013` → IC=+0.294 (n=562)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1013 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.249 (n=1141)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.242 (n=642)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.1048` → IC=+0.277 (n=851)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1048 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.39` → IC=+0.242 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.39 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.234` → IC=+0.248 (n=1383)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.234 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` < `0.1621` → IC=+0.239 (n=1231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1621 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.2909` → IC=+0.268 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2909 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.4205` → IC=+0.260 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4205 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.6138` → IC=+0.240 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6138 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.243 (n=1405)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1837.5848` → IC=+0.252 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1837.5848 (IC base=+0.241)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.229 (n=503)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.1659` → IC=+0.184 (n=1003)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1659 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.180 (n=1508)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `0.3884` → IC=+0.224 (n=1504)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3884 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.1985` → IC=+0.213 (n=890)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1985 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.537` → IC=+0.233 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.537 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `0.6926` → IC=+0.172 (n=662)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.6926 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` > `1.0768` → IC=+0.159 (n=682)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 1.0768 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.2823` → IC=+0.193 (n=236)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2823 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `1.4146` → IC=+0.182 (n=489)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.4146 (IC base=+0.158)

- **PATRÓN** `ballena_activa_n` < `434.0` → IC=+0.161 (n=1428)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 434.0 (IC base=+0.158)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.163 (n=1580)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0057 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.2988` → IC=+0.167 (n=1578)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.2988 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=605)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.5918` → IC=+0.198 (n=1578)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.5918 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.1344` → IC=+0.171 (n=1562)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1344 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.924` → IC=+0.201 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.924 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.2116` → IC=+0.161 (n=1578)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2116 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` < `0.2291` → IC=+0.145 (n=1625)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.2291 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.0702` → IC=+0.147 (n=703)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.0702 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `2.485` → IC=+0.153 (n=1465)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.485 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.7689` → IC=+0.144 (n=977)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.7689 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `208.0` → IC=+0.173 (n=466)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 208.0 (IC base=+0.142)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.215 (n=1505)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.2471` → IC=+0.220 (n=1121)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2471 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=1755)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.292 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.543` → IC=+0.276 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.543 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.205 (n=1417)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.128` → IC=+0.205 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.128 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `1.7786` → IC=+0.205 (n=710)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7786 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `2.7283` → IC=+0.211 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7283 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.212 (n=1999)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `1952.9484` → IC=+0.221 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1952.9484 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.242 (n=1260)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.1429` → IC=+0.261 (n=629)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1429 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.277 (n=491)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` < `0.3506` → IC=+0.248 (n=1430)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3506 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.676` → IC=+0.257 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.676 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.3512` → IC=+0.260 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3512 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` < `1.7484` → IC=+0.237 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7484 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.7347` → IC=+0.233 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7347 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `1941.7448` → IC=+0.227 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1941.7448 (IC base=+0.224)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.218 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.224)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.182 (n=1418)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0064 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.079` → IC=+0.204 (n=538)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.079 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=1680)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.3344` → IC=+0.207 (n=1611)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3344 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.139` → IC=+0.188 (n=1053)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.139 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.995` → IC=+0.208 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.995 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.8567` → IC=+0.160 (n=1075)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8567 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1022` → IC=+0.170 (n=677)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1022 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `1.4363` → IC=+0.165 (n=527)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.4363 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `2.5292` → IC=+0.162 (n=527)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.5292 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `5109.0415` → IC=+0.196 (n=1074)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 5109.0415 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.154 (n=1552)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 152.0 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.160 (n=1683)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0071 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.3828` → IC=+0.148 (n=1683)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3828 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=642)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.6697` → IC=+0.183 (n=1683)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6697 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.91` → IC=+0.163 (n=583)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 6.91 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.8541` → IC=+0.160 (n=1122)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8541 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2969` → IC=+0.186 (n=253)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2969 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.8212` → IC=+0.140 (n=1038)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.8212 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.5391` → IC=+0.130 (n=519)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.5391 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `4343.582` → IC=+0.165 (n=1122)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 4343.582 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.127 (n=1497)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 150.0 (IC base=+0.128)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.160 (n=832)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0099 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.4465` → IC=+0.128 (n=1612)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.4465 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=1876)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.212 (n=1844)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `1.0411` → IC=+0.214 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0411 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.874` → IC=+0.261 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.874 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `1.2085` → IC=+0.137 (n=1832)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.2085 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` > `0.6466` → IC=+0.131 (n=1833)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 0.6466 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` < `0.1642` → IC=+0.135 (n=1847)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.1642 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.5464` → IC=+0.142 (n=780)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.5464 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.4838` → IC=+0.129 (n=591)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.4838 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.130 (n=1919)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `2388.5554` → IC=+0.184 (n=1221)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2388.5554 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.149 (n=1442)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 46.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.158 (n=811)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0061 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1033` → IC=+0.179 (n=614)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.1033 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=1860)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.5778` → IC=+0.217 (n=1842)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5778 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.1985` → IC=+0.149 (n=1687)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1985 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.362` → IC=+0.129 (n=562)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 5.362 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.1765` → IC=+0.132 (n=1841)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1765 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2289` → IC=+0.160 (n=324)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2289 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4534` → IC=+0.139 (n=563)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.4534 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `1.8188` → IC=+0.126 (n=1126)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.8188 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2744.6466` → IC=+0.185 (n=835)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2744.6466 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.129 (n=1644)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 52.0 (IC base=+0.120)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.230 (n=1719)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.1776` → IC=+0.218 (n=757)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1776 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.209 (n=1792)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.213 (n=779)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.245 (n=1723)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.1986` → IC=+0.214 (n=1174)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1986 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.6` → IC=+0.243 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.6 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `1.1949` → IC=+0.211 (n=1719)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1949 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `0.6251` → IC=+0.216 (n=1719)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6251 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.271 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.283 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `2.4727` → IC=+0.211 (n=1667)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4727 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `1.8125` → IC=+0.220 (n=1111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8125 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.211 (n=1651)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `2852.897` → IC=+0.211 (n=779)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2852.897 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.228 (n=777)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0118 (IC base=+0.215)

- **PATRÓN** `sigma_h` > `0.0223` → IC=+0.221 (n=802)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0223 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.0902` → IC=+0.241 (n=589)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0902 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.237 (n=865)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.0205` → IC=+0.287 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0205 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `1.1598` → IC=+0.234 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1598 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.386` → IC=+0.252 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.386 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `0.6385` → IC=+0.226 (n=1764)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6385 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.2819` → IC=+0.273 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2819 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `2.2062` → IC=+0.208 (n=1423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2062 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `1.4384` → IC=+0.215 (n=1617)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4384 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `2607.8903` → IC=+0.223 (n=1176)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2607.8903 (IC base=+0.215)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.195 (n=1160)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0042 (IC base=+0.169)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.172 (n=879)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0084 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.3396` → IC=+0.180 (n=2312)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.3396 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.188 (n=2391)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 8.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.3407` → IC=+0.197 (n=2628)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.3407 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.7903` → IC=+0.185 (n=420)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.7903 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.758` → IC=+0.194 (n=1143)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 3.758 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `0.8708` → IC=+0.190 (n=1567)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.8708 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `1.2084` → IC=+0.178 (n=784)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 1.2084 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.1639` → IC=+0.173 (n=699)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1639 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.4427` → IC=+0.181 (n=850)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.4427 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.5338` → IC=+0.174 (n=851)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.5338 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.172 (n=2995)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `2727.3504` → IC=+0.171 (n=2348)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2727.3504 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `145.0` → IC=+0.186 (n=2405)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 145.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.156 (n=901)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0036 (IC base=+0.109)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.123 (n=2540)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.0714` → IC=+0.196 (n=902)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.0714 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` < `0.6987` → IC=+0.123 (n=1076)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 0.6987 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` > `0.0756` → IC=+0.125 (n=1028)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` > 0.0756 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` < `1.4408` → IC=+0.147 (n=874)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4408 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `2783.1673` → IC=+0.128 (n=2412)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 2783.1673 (IC base=+0.109)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.129 (n=1145)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 29.0 (IC base=+0.109)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.208 (n=317)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.3322` → IC=+0.175 (n=715)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3322 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.189 (n=661)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 8.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.6364` → IC=+0.209 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6364 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.2887` → IC=+0.173 (n=246)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.2887 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.222` → IC=+0.175 (n=306)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.222 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.8832` → IC=+0.178 (n=477)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.8832 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` < `0.157` → IC=+0.155 (n=747)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.157 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.2382` → IC=+0.161 (n=614)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.2382 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.5216` → IC=+0.158 (n=623)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.5216 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `10661.4307` → IC=+0.156 (n=714)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 10661.4307 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.205 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 151.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.208 (n=286)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.3463` → IC=+0.159 (n=852)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3463 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.150 (n=819)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 6.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.146 (n=866)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 17.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.6098` → IC=+0.183 (n=750)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6098 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.1827` → IC=+0.158 (n=844)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1827 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.14` → IC=+0.146 (n=777)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 3.14 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.2142` → IC=+0.145 (n=852)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.2142 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `0.8668` → IC=+0.160 (n=568)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.8668 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.1609` → IC=+0.195 (n=231)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1609 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `2.121` → IC=+0.162 (n=741)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.121 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.4081` → IC=+0.148 (n=842)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.4081 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=1102)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `12062.2629` → IC=+0.145 (n=761)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 12062.2629 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `355.0` → IC=+0.153 (n=820)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 355.0 (IC base=+0.142)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.241 (n=555)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.2048` → IC=+0.218 (n=555)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2048 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=872)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `0.6705` → IC=+0.252 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6705 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.3604` → IC=+0.211 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3604 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` < `0.2068` → IC=+0.206 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2068 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.089` → IC=+0.221 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.089 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` < `0.8422` → IC=+0.211 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8422 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` > `1.1824` → IC=+0.221 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1824 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.1598` → IC=+0.234 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1598 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `1.4274` → IC=+0.225 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4274 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `2.4553` → IC=+0.232 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4553 (IC base=+0.202)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.131 (n=695)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0061 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.122 (n=710)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 7.0 (IC base=+0.104)

- **PATRÓN** `ibs_20min` < `0.0866` → IC=+0.169 (n=264)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.0866 (IC base=+0.104)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.459` → IC=+0.151 (n=207)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 6.459 (IC base=+0.104)

- **PATRÓN** `volumen_regimen` < `0.6887` → IC=+0.149 (n=348)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.6887 (IC base=+0.104)

- **PATRÓN** `volumen_pendiente_norm` > `0.2234` → IC=+0.146 (n=125)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.2234 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `7746.672` → IC=+0.142 (n=526)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 7746.672 (IC base=+0.104)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.126 (n=335)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 42.0 (IC base=+0.104)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.475` → IC=-0.126 (n=268)

  - _Acción_: SKIP cuando `ibs_20min` > 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=521)

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

- **PATRÓN** `ibs_20min` < `0.475` → IC=+0.146 (n=521)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.475 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` < `1.569` → IC=+0.124 (n=248)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.569 (IC base=+0.054)

- **PATRÓN** `libro_liquidez` > `2864.9802` → IC=+0.153 (n=269)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2864.9802 (IC base=+0.054)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.124 (n=360)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 23.0 (IC base=+0.054)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0238` → IC=+0.168 (n=191)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0238 (IC base=+0.152)

- **PATRÓN** `sigma_h` > `0.0144` → IC=+0.198 (n=127)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0144 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.3919` → IC=+0.165 (n=168)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.3919 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.181 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 16.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.201 (n=85)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.5556` → IC=+0.184 (n=172)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.5556 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.24` → IC=+0.173 (n=105)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.24 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` < `1.115` → IC=+0.161 (n=213)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 1.115 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.317` → IC=+0.181 (n=164)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 3.317 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` > `0.6843` → IC=+0.176 (n=171)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6843 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` < `0.2526` → IC=+0.181 (n=186)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.2526 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `1.4483` → IC=+0.241 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4483 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `2.6132` → IC=+0.172 (n=56)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.6132 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.182 (n=196)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.02 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `2503.9142` → IC=+0.174 (n=127)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2503.9142 (IC base=+0.152)

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
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.179 (n=4341)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0046 (IC base=+0.176)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.211 (n=4327)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=13579)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `0.9919` → IC=+0.309 (n=4323)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9919 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.1642` → IC=+0.186 (n=4936)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1642 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.406` → IC=+0.247 (n=3189)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.406 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `0.8802` → IC=+0.171 (n=5792)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.8802 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.2905` → IC=+0.195 (n=1760)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2905 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `2.602` → IC=+0.195 (n=4180)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.602 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `1974.8681` → IC=+0.180 (n=11583)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 1974.8681 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.202 (n=10210)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 79.0 (IC base=+0.176)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.195 (n=5149)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0053 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.1471` → IC=+0.194 (n=5139)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1471 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=4370)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` < `0.4523` → IC=+0.248 (n=10273)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4523 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` < `0.1737` → IC=+0.166 (n=6884)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1737 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.094` → IC=+0.204 (n=1643)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.094 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.747` → IC=+0.185 (n=11255)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 3.747 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `0.7056` → IC=+0.164 (n=3484)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.7056 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.2897` → IC=+0.250 (n=1552)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2897 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `1.8641` → IC=+0.191 (n=7267)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 1.8641 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.207 (n=7129)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.185)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.251 (n=718)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.207)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.224 (n=720)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.356` → IC=+0.210 (n=2154)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.356 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.225 (n=1042)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.211 (n=1446)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.328 (n=800)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.74` → IC=+0.358 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.74 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.265 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `2.5787` → IC=+0.217 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5787 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.227 (n=2198)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `2048.4076` → IC=+0.214 (n=718)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2048.4076 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.262 (n=1180)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.259)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.262 (n=1766)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.1253` → IC=+0.281 (n=777)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1253 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.270 (n=1596)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.3587` → IC=+0.283 (n=1554)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3587 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.508` → IC=+0.263 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.508 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.2826` → IC=+0.290 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2826 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `2.6242` → IC=+0.277 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6242 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.259 (n=1935)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1973.02` → IC=+0.267 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1973.02 (IC base=+0.259)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.213 (n=699)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1809` → IC=+0.164 (n=1384)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1809 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=2177)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.2855` → IC=+0.206 (n=2077)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2855 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1256` → IC=+0.190 (n=1182)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1256 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.762` → IC=+0.182 (n=347)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 11.762 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.232` → IC=+0.153 (n=1898)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.232 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.7032` → IC=+0.170 (n=915)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.7032 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.0731` → IC=+0.154 (n=1840)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0731 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2719` → IC=+0.189 (n=297)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2719 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1442` → IC=+0.161 (n=1776)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1442 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.5203` → IC=+0.156 (n=1803)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.5203 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `277.0` → IC=+0.182 (n=862)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 277.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.162 (n=1732)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0057 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.263` → IC=+0.162 (n=1523)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.263 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=659)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.148 (n=785)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 7.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.6821` → IC=+0.195 (n=1731)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.6821 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1318` → IC=+0.167 (n=1576)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1318 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.553` → IC=+0.160 (n=292)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 11.553 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.1913` → IC=+0.160 (n=1731)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1913 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1548` → IC=+0.201 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1548 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.4384` → IC=+0.155 (n=1631)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4384 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `1.7778` → IC=+0.161 (n=1087)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.7778 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `348.0` → IC=+0.145 (n=1024)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 348.0 (IC base=+0.146)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0064` → IC=+0.232 (n=2127)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0064 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.228 (n=2128)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.226 (n=2156)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.436` → IC=+0.300 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.436 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` < `0.2056` → IC=+0.226 (n=2144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2056 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `1.7691` → IC=+0.232 (n=1830)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7691 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=2541)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `2028.6484` → IC=+0.241 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2028.6484 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.242 (n=1755)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.1798` → IC=+0.247 (n=877)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1798 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.259 (n=757)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.234 (n=935)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0171` → IC=+0.301 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0171 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.987` → IC=+0.283 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.987 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.3417` → IC=+0.294 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3417 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.7408` → IC=+0.233 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7408 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.1493` → IC=+0.241 (n=1245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1493 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.237 (n=1163)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1943.0952` → IC=+0.244 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1943.0952 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.252 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.234)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.194 (n=979)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0038 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.4253` → IC=+0.152 (n=2220)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.4253 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.154 (n=2319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.2702` → IC=+0.188 (n=2220)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2702 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.5489` → IC=+0.163 (n=609)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.5489 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.174` → IC=+0.151 (n=911)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 4.174 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8735` → IC=+0.160 (n=1480)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8735 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.1662` → IC=+0.173 (n=591)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1662 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.5263` → IC=+0.158 (n=951)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.5263 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.1819` → IC=+0.150 (n=979)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.1819 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `7330.4887` → IC=+0.233 (n=1007)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7330.4887 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.181 (n=700)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 70.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.168 (n=1195)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0051 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.4405` → IC=+0.144 (n=1790)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.4405 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.159 (n=655)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.133 (n=624)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 5.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.7338` → IC=+0.182 (n=1789)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.7338 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.1453` → IC=+0.139 (n=1568)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1453 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.332` → IC=+0.169 (n=364)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.332 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.8747` → IC=+0.142 (n=1193)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.8747 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.2975` → IC=+0.230 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2975 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `2.2545` → IC=+0.135 (n=1509)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.2545 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `1.4488` → IC=+0.142 (n=1714)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4488 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `5639.5091` → IC=+0.195 (n=811)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 5639.5091 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `167.0` → IC=+0.134 (n=1713)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 167.0 (IC base=+0.131)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.135 (n=2228)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.0056 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=811)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.4565` → IC=+0.201 (n=2226)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4565 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `1.0324` → IC=+0.208 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0324 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.54` → IC=+0.245 (n=821)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.54 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.2339` → IC=+0.136 (n=2226)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.2339 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1626` → IC=+0.128 (n=2291)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1626 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2825` → IC=+0.124 (n=296)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.2825 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.1932` → IC=+0.136 (n=982)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.1932 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=1484)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2555.8611` → IC=+0.234 (n=1009)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2555.8611 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.143 (n=1342)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 41.0 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.177 (n=708)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0056 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.1303` → IC=+0.166 (n=708)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1303 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=2192)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.5049` → IC=+0.234 (n=1868)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5049 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` < `0.217` → IC=+0.141 (n=1752)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.217 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.491` → IC=+0.132 (n=2047)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 3.491 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.7144` → IC=+0.161 (n=936)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.7144 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2237` → IC=+0.189 (n=345)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2237 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `2.1606` → IC=+0.136 (n=1721)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.1606 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2799.6738` → IC=+0.199 (n=708)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2799.6738 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.139 (n=1713)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 50.0 (IC base=+0.122)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.232 (n=2166)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=2270)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.218 (n=1942)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.263 (n=1940)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `0.2086` → IC=+0.233 (n=1246)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2086 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.299` → IC=+0.271 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.299 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` < `1.2397` → IC=+0.217 (n=2166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2397 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `0.6419` → IC=+0.221 (n=2166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6419 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.2367` → IC=+0.243 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2367 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `2.5136` → IC=+0.249 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5136 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=2058)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `2633.3465` → IC=+0.222 (n=1444)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2633.3465 (IC base=+0.215)

- **PATRÓN** `sigma_h` < `0.0095` → IC=+0.219 (n=759)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0095 (IC base=+0.214)

- **PATRÓN** `sigma_h` > `0.0226` → IC=+0.231 (n=1032)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0226 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.231 (n=1609)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` < `0.4186` → IC=+0.263 (n=2002)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4186 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `1.1882` → IC=+0.215 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1882 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` < `0.2936` → IC=+0.217 (n=2121)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2936 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.876` → IC=+0.257 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.876 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` > `1.2292` → IC=+0.242 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2292 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.282` → IC=+0.282 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.282 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.215 (n=2083)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=+0.214)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.165 (n=3796)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.226 (n=1284)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.5004` → IC=+0.195 (n=3851)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.5004 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.198 (n=1421)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.187 (n=1748)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 6.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` > `0.9408` → IC=+0.239 (n=1286)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9408 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` > `0.1685` → IC=+0.193 (n=1430)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1685 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.212` → IC=+0.211 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.212 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `0.7119` → IC=+0.191 (n=1166)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.7119 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` > `0.8944` → IC=+0.188 (n=1767)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 0.8944 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.1701` → IC=+0.214 (n=1081)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1701 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `1.459` → IC=+0.191 (n=1268)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.459 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `2.6347` → IC=+0.191 (n=1266)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.6347 (IC base=+0.185)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.191 (n=2848)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `3771.3096` → IC=+0.193 (n=2567)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 3771.3096 (IC base=+0.185)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.222 (n=954)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.4861` → IC=+0.180 (n=2859)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.4861 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.198 (n=1007)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.181 (n=1289)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 6.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` < `0.1802` → IC=+0.189 (n=1258)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.1802 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.6484` → IC=+0.180 (n=529)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.6484 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` < `0.2354` → IC=+0.157 (n=2545)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.2354 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.208` → IC=+0.172 (n=2851)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` < 6.208 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `1.2587` → IC=+0.168 (n=2695)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2587 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` < `0.0969` → IC=+0.168 (n=2604)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.0969 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.2228` → IC=+0.167 (n=596)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2228 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `1.5394` → IC=+0.168 (n=1242)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.5394 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `1.8288` → IC=+0.174 (n=1881)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.8288 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.165 (n=3796)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `12323.4873` → IC=+0.166 (n=953)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 12323.4873 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `199.0` → IC=+0.174 (n=2452)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 199.0 (IC base=+0.164)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.239 (n=350)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.0834` → IC=+0.263 (n=175)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0834 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.222 (n=524)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.214 (n=232)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.515` → IC=+0.233 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.515 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.7622` → IC=+0.217 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7622 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` < `0.3165` → IC=+0.221 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3165 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.039` → IC=+0.228 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.039 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.526` → IC=+0.213 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.526 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` < `1.2246` → IC=+0.221 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2246 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` > `0.5931` → IC=+0.221 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5931 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2975` → IC=+0.306 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2975 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.8529` → IC=+0.224 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8529 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `12467.3842` → IC=+0.234 (n=468)

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
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.186 (n=301)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0067 (IC base=+0.169)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.186 (n=310)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0099 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.5868` → IC=+0.176 (n=683)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.5868 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.227 (n=240)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` < `0.3929` → IC=+0.171 (n=229)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.3929 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.994` → IC=+0.230 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.994 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.51` → IC=+0.221 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.51 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.2076` → IC=+0.218 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2076 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `3.3613` → IC=+0.181 (n=227)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 3.3613 (IC base=+0.169)

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
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.220 (n=395)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.1508` → IC=+0.213 (n=521)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1508 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.203 (n=433)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.196 (n=541)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 6.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.5256` → IC=+0.206 (n=790)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5256 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `0.8854` → IC=+0.198 (n=395)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.8854 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` < `0.2036` → IC=+0.204 (n=991)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2036 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.178` → IC=+0.201 (n=1065)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.178 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `1.0845` → IC=+0.198 (n=1043)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 1.0845 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` > `1.2448` → IC=+0.196 (n=396)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` > 1.2448 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.1071` → IC=+0.194 (n=1089)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.1071 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.1659` → IC=+0.206 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1659 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `2.4777` → IC=+0.199 (n=1160)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.4777 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.196 (n=1187)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.226 (n=315)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.4905` → IC=+0.190 (n=945)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.4905 (IC base=+0.165)

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
- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.203 (n=398)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.3291` → IC=+0.159 (n=303)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3291 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.185 (n=455)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 3.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.262 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.2073` → IC=+0.204 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2073 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.464` → IC=+0.205 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.464 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `0.7121` → IC=+0.197 (n=199)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.7121 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` > `1.2801` → IC=+0.167 (n=151)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.2801 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.1626` → IC=+0.221 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1626 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `2.5405` → IC=+0.209 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5405 (IC base=+0.159)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.167 (n=545)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.02 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `3317.1433` → IC=+0.200 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3317.1433 (IC base=+0.159)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.181 (n=384)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 49.0 (IC base=+0.159)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.221 (n=159)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.3887` → IC=+0.219 (n=233)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3887 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.204 (n=248)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` < `0.0952` → IC=+0.244 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0952 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.5377` → IC=+0.215 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5377 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.4` → IC=+0.178 (n=181)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 2.4 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.208` → IC=+0.175 (n=337)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` < 5.208 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `0.7986` → IC=+0.186 (n=154)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.7986 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` > `1.1868` → IC=+0.177 (n=159)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 1.1868 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` < `0.105` → IC=+0.218 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.105 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `1.6214` → IC=+0.189 (n=149)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.6214 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `2.2105` → IC=+0.186 (n=154)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.2105 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `3219.8531` → IC=+0.201 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3219.8531 (IC base=+0.174)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.215 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.174)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.156 (n=550)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0038 (IC base=+0.082)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.122 (n=569)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 16.0 (IC base=+0.082)

- **PATRÓN** `ibs_20min` > `0.4562` → IC=+0.155 (n=1159)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.4562 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` > `0.1412` → IC=+0.142 (n=643)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1412 (IC base=+0.082)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.472` → IC=+0.185 (n=268)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 11.472 (IC base=+0.082)

- **PATRÓN** `volumen_pendiente_norm` > `0.2792` → IC=+0.171 (n=159)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2792 (IC base=+0.082)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.122 (n=368)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0045 (IC base=+0.052)

- **PATRÓN** `ibs_20min` < `0.2105` → IC=+0.256 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2105 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` < `0.1111` → IC=+0.133 (n=478)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1111 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.09` → IC=+0.136 (n=404)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 4.09 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` > `0.1414` → IC=+0.184 (n=115)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1414 (IC base=+0.052)

- **PATRÓN** `volumen_spike_ratio` < `2.5975` → IC=+0.143 (n=415)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.5975 (IC base=+0.052)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.142 (n=426)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0058 (IC base=+0.098)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.122 (n=432)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.4181` → IC=+0.172 (n=395)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.4181 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.164 (n=215)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `2.5088` → IC=+0.124 (n=354)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.5088 (IC base=+0.098)

- **PATRÓN** `ibs_20min` < `0.0556` → IC=+0.296 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0556 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` < `0.1876` → IC=+0.130 (n=252)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.1876 (IC base=+0.077)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.141` → IC=+0.146 (n=221)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 7.141 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` < `1.1644` → IC=+0.123 (n=229)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 1.1644 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` > `0.8132` → IC=+0.136 (n=152)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.8132 (IC base=+0.077)

- **PATRÓN** `volumen_pendiente_norm` > `0.0743` → IC=+0.149 (n=92)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.0743 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` < `2.5035` → IC=+0.139 (n=206)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.5035 (IC base=+0.077)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.154 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=155)

- **FILTRO** `ibs_20min` > `0.7058` → IC=-0.211 (n=43)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7058
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=133)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.152 (n=277)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0047 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.127 (n=387)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 7.0 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.6963` → IC=+0.211 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6963 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.178 (n=212)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.674` → IC=+0.280 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.674 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.2835` → IC=+0.198 (n=51)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2835 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` < `1.7915` → IC=+0.142 (n=219)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.7915 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `1146.9989` → IC=+0.152 (n=337)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1146.9989 (IC base=+0.097)

- **PATRÓN** `ibs_20min` < `0.7058` → IC=+0.152 (n=133)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.7058 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` < `1.7085` → IC=+0.133 (n=77)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.7085 (IC base=+0.007)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0105` → IC=-0.240 (n=48)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=146)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.265 (n=117)

- **PATRÓN** `ibs_20min` > `0.7647` → IC=+0.174 (n=256)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.7647 (IC base=+0.051)

- **PATRÓN** `dist_vwap_pct` > `0.73` → IC=+0.138 (n=103)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.73 (IC base=+0.051)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.668` → IC=+0.127 (n=81)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` > 9.668 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.2443` → IC=+0.183 (n=77)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2443 (IC base=+0.051)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.220 (n=98)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.056)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.265 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` > `0.1231` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1231 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` < `0.1816` → IC=+0.164 (n=114)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1816 (IC base=+0.056)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.158` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.158 (IC base=+0.056)

- **PATRÓN** `volumen_regimen` < `0.8193` → IC=+0.146 (n=77)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.8193 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.0749` → IC=+0.300 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0749 (IC base=+0.056)

- **PATRÓN** `volumen_spike_ratio` > `1.8571` → IC=+0.223 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8571 (IC base=+0.056)

### GBM_LATE_60M_FADE
- **FILTRO** `dist_vwap_pct` > `0.2352` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2352
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=233)

- **FILTRO** `volumen_regimen` < `0.7425` → IC=-0.359 (n=62)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7425
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=187)

- **FILTRO** `volumen_spike_ratio` > `2.9817` → IC=-0.189 (n=43)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.9817
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=132)

- **FILTRO** `volumen_spike_ratio` < `1.6074` → IC=-0.195 (n=57)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.6074
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=118)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.206 (n=49)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=200)

- **FILTRO** `sigma_h` > `0.0056` → IC=-0.373 (n=53)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0056
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=162)

- **FILTRO** `dist_vwap_pct` > `0.3146` → IC=-0.395 (n=36)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3146
  - _Potencial_: sin este filtro IC_bueno=-0.246 (n=179)

- **FILTRO** `sigma_ewma_delta_pct` > `8.423` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.423
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=185)

- **FILTRO** `volumen_pendiente_norm` > `0.0538` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0538
  - _Potencial_: sin este filtro IC_bueno=-0.236 (n=104)

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

- **FILTRO** `volumen_regimen` > `0.8408` → IC=-0.375 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8408
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=68)

- **FILTRO** `volumen_spike_ratio` > `1.5874` → IC=-0.300 (n=28)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.5874
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=29)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` < `0.0026` → IC=-0.364 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0026
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=62)

- **FILTRO** `ibs_20min` < `0.5872` → IC=-0.466 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5872
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=55)

- **FILTRO** `sigma_h` > `0.0048` → IC=-0.357 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.246 (n=61)

- **FILTRO** `ibs_20min` > `0.538` → IC=-0.354 (n=39)

  - _Acción_: SKIP cuando `ibs_20min` > 0.538
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=41)

- **FILTRO** `volumen_spike_ratio` < `1.4324` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4324
  - _Potencial_: sin este filtro IC_bueno=-0.243 (n=33)

- **PATRÓN** `ibs_20min` > `0.9583` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9583 (IC base=-0.167)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=70)

- **FILTRO** `volumen_spike_ratio` < `1.5474` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.5474
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=46)

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
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.171 (n=174)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0058 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.132 (n=180)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 15.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.6585` → IC=+0.142 (n=383)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.6585 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.4724` → IC=+0.192 (n=89)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.4724 (IC base=+0.094)

- **PATRÓN** `volumen_regimen` < `0.6589` → IC=+0.139 (n=128)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.6589 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` < `2.5028` → IC=+0.123 (n=282)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.5028 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.082)

- **PATRÓN** `ibs_20min` < `0.156` → IC=+0.176 (n=344)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.156 (IC base=+0.082)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.863` → IC=+0.196 (n=113)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 8.863 (IC base=+0.082)

- **PATRÓN** `volumen_spike_ratio` < `2.6699` → IC=+0.128 (n=315)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 2.6699 (IC base=+0.082)

- **PATRÓN** `libro_liquidez` > `2745.0936` → IC=+0.153 (n=260)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2745.0936 (IC base=+0.082)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6466` → IC=-0.250 (n=38)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6466
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=115)

- **PATRÓN** `sigma_h` > `0.0024` → IC=+0.190 (n=156)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0024 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.206 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` < `0.1524` → IC=+0.201 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1524 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.0856` → IC=+0.158 (n=179)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.0856 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.332` → IC=+0.181 (n=142)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 4.332 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.1443` → IC=+0.150 (n=175)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.1443 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` > `0.6754` → IC=+0.171 (n=156)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 0.6754 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.1891` → IC=+0.199 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1891 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.6869` → IC=+0.197 (n=143)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.6869 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.4468` → IC=+0.176 (n=143)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.4468 (IC base=+0.150)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1654` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1654
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=101)

- **FILTRO** `libro_liquidez` < `1506.2493` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `libro_liquidez` < 1506.2493
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=122)

- **FILTRO** `ibs_20min` > `0.327` → IC=-0.160 (n=45)

  - _Acción_: SKIP cuando `ibs_20min` > 0.327
  - _Potencial_: sin este filtro IC_bueno=+0.138 (n=139)

- **PATRÓN** `volumen_spike_ratio` < `1.8267` → IC=+0.136 (n=64)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.8267 (IC base=+0.049)

- **PATRÓN** `libro_liquidez` > `1506.2493` → IC=+0.129 (n=122)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 1506.2493 (IC base=+0.049)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.122 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 8.0 (IC base=+0.065)

- **PATRÓN** `ibs_20min` < `0.327` → IC=+0.138 (n=139)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.327 (IC base=+0.065)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.489` → IC=+0.306 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.489 (IC base=+0.065)

- **PATRÓN** `volumen_regimen` < `0.6541` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6541 (IC base=+0.065)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.4194` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4194
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=79)

- **FILTRO** `dist_vwap_pct` > `0.2724` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2724
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=85)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.270 (n=98)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.250 (n=134)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.229 (n=149)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` < `0.7358` → IC=+0.231 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7358 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.92` → IC=+0.240 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.92 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.6339` → IC=+0.342 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6339 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` < `0.1348` → IC=+0.230 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1348 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.365` → IC=+0.283 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.365 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` < `1.0151` → IC=+0.263 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0151 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.308 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `1.4854` → IC=+0.360 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4854 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `2.1062` → IC=+0.278 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1062 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.229 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.0968` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0968 (IC base=-0.038)

### LATE_WINDOW_5MIN
- **PATRÓN** `drift_ventana_pct` |x|> `0.332` → IC=+0.300 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.332 (IC base=+0.285)

- **PATRÓN** `elapsed_s` > `193.1` → IC=+0.367 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 193.1 (IC base=+0.285)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.8028` → IC=+0.364 (n=42)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8028 (IC base=+0.285)

- **PATRÓN** `ballena_activa_n` < `1158.0` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1158.0 (IC base=+0.285)

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
- **PATRÓN** `drift_ventana_pct` |x|> `0.332` → IC=+0.300 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.332 (IC base=+0.285)

- **PATRÓN** `elapsed_s` > `193.1` → IC=+0.367 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 193.1 (IC base=+0.285)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.8028` → IC=+0.364 (n=42)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8028 (IC base=+0.285)

- **PATRÓN** `ballena_activa_n` < `1158.0` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1158.0 (IC base=+0.285)

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
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.126 (n=978)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` > 0.5 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `2847.4573` → IC=+0.148 (n=458)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 2847.4573 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.125 (n=973)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.101)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.126 (n=978)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` > 0.5 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `2847.4573` → IC=+0.148 (n=458)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 2847.4573 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.125 (n=973)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.101)

### LIQUIDACIONES_15M
- **FILTRO** `py_entrada` < `0.445` → IC=-0.133 (n=47)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=117)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=148)

- **FILTRO** `libro_liquidez` < `9884.3291` → IC=-0.182 (n=108)

  - _Acción_: SKIP cuando `libro_liquidez` < 9884.3291
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=56)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=235)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=221)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=47)

- **FILTRO** `libro_liquidez` < `10724.0239` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 10724.0239
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=51)

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
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=2596)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=95)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.130 (n=52)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=95)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.188 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=103)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.129 (n=103)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 15.0 (IC base=+0.056)

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

- **PATRÓN** `liq_usd_total` > `115065.16` → IC=+0.153 (n=96)

  - _Acción_: Kelly boost +0.77€ cuando `liq_usd_total` > 115065.16 (IC base=+0.047)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.141 (n=168)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.495 (IC base=+0.047)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=1007)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=961)

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
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=599)

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
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=316)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.152 (n=113)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.495 (IC base=+0.027)

- **PATRÓN** `libro_liquidez` > `3962.9688` → IC=+0.135 (n=113)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 3962.9688 (IC base=+0.027)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=759)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=759)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.131 (n=242)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=597)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=513)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=513)

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
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=128)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=152)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=242)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=125)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=138)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=292)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=292)

- **FILTRO** `libro_liquidez` < `564.286` → IC=-0.130 (n=106)

  - _Acción_: SKIP cuando `libro_liquidez` < 564.286
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=216)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=186)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.141 (n=670)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=1645)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.52` → IC=-0.145 (n=29)

  - _Acción_: SKIP cuando `py_entrada` < 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=10)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.52` → IC=-0.121 (n=159)

  - _Acción_: SKIP cuando `py_entrada` < 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=60)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.221 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.46 (IC base=+0.040)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=126)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.146 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=104)

- **FILTRO** `lag_apertura_s` > `278.55` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `lag_apertura_s` > 278.55
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=100)

- **FILTRO** `profundidad_ratio` < `30.9` → IC=-0.134 (n=99)

  - _Acción_: SKIP cuando `profundidad_ratio` < 30.9
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=51)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `restante_min` < `3.99` → IC=-0.125 (n=110)

  - _Acción_: SKIP cuando `restante_min` < 3.99
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=44)

- **FILTRO** `lag_apertura_s` > `60.71` → IC=-0.124 (n=115)

  - _Acción_: SKIP cuando `lag_apertura_s` > 60.71
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=39)

- **PATRÓN** `py_entrada` < `0.58` → IC=+0.121 (n=56)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` < 0.58 (IC base=+0.067)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `restante_min` < `12.78` → IC=-0.144 (n=102)

  - _Acción_: SKIP cuando `restante_min` < 12.78
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=103)

- **FILTRO** `lag_apertura_s` > `133.19` → IC=-0.144 (n=102)

  - _Acción_: SKIP cuando `lag_apertura_s` > 133.19
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=103)

- **FILTRO** `profundidad_ratio` < `37.6` → IC=-0.217 (n=51)

  - _Acción_: SKIP cuando `profundidad_ratio` < 37.6
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=154)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.238 (n=40)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=170)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.135 (n=168)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=96)

- **FILTRO** `restante_min` < `3.43` → IC=-0.230 (n=87)

  - _Acción_: SKIP cuando `restante_min` < 3.43
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=177)

- **FILTRO** `lag_apertura_s` > `93.56` → IC=-0.214 (n=89)

  - _Acción_: SKIP cuando `lag_apertura_s` > 93.56
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=175)

- **PATRÓN** `py_entrada` < `0.46` → IC=+0.161 (n=57)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` < 0.46 (IC base=+0.033)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.133 (n=47)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=156)

- **PATRÓN** `lag_apertura_s` < `93.77` → IC=+0.132 (n=74)

  - _Acción_: Kelly boost +0.66€ cuando `lag_apertura_s` < 93.77 (IC base=-0.013)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **PATRÓN** `py_entrada` < `0.49` → IC=+0.125 (n=78)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.49 (IC base=+0.002)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.135 (n=165)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=90)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.152 (n=90)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` > 0.5 (IC base=-0.033)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.194 (n=83)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=231)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.163 (n=4598)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=13926)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.164 (n=4770)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=14390)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.192 (n=812)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=2474)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.150 (n=798)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=2629)

- **PATRÓN** `libro_liquidez` > `1815.7196` → IC=+0.131 (n=1118)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 1815.7196 (IC base=+0.036)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.174 (n=833)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=2501)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.178 (n=867)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=2606)

- **PATRÓN** `libro_liquidez` > `1816.8776` → IC=+0.129 (n=1134)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 1816.8776 (IC base=+0.034)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.166 (n=783)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=2498)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2225)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2474)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=3214)

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
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=286)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=798)

- **FILTRO** `libro_liquidez` < `1959.6157` → IC=-0.171 (n=329)

  - _Acción_: SKIP cuando `libro_liquidez` < 1959.6157
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=670)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.131 (n=12905)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=28798)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=9792)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=31911)

- **FILTRO** `ibs_7min` < `0.2614` → IC=-0.235 (n=10422)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2614
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=31281)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.154 (n=14057)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=27646)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.236 (n=12833)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=40112)

- **FILTRO** `ibs_7min` > `0.2895` → IC=-0.180 (n=13227)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2895
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=39718)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.142 (n=2099)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=4994)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.309 (n=1691)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=5402)

- **FILTRO** `ibs_7min` < `0.7097` → IC=-0.252 (n=2340)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7097
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=4753)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.186 (n=1558)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=5535)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.267 (n=2238)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=6931)

- **FILTRO** `ibs_7min` > `0.7843` → IC=-0.211 (n=2292)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7843
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=6877)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.133 (n=1691)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=5440)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.250 (n=1747)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=5384)

- **FILTRO** `ibs_7min` < `0.7415` → IC=-0.198 (n=1780)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7415
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=5351)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.178 (n=1780)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=5351)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.267 (n=1715)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=5539)

- **FILTRO** `ibs_7min` > `0.2655` → IC=-0.194 (n=1813)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2655
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=5441)

- **FILTRO** `ballena_activa_n` > `150.0` → IC=-0.190 (n=1809)

  - _Acción_: SKIP cuando `ballena_activa_n` > 150.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=5445)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.162 (n=1911)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=4826)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.316 (n=1599)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=5138)

- **FILTRO** `ibs_7min` < `0.7038` → IC=-0.247 (n=2223)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7038
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=4514)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.216 (n=1535)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5202)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.243 (n=2228)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=7541)

- **FILTRO** `ibs_7min` > `0.7402` → IC=-0.172 (n=2442)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7402
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=7327)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=2213)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=4645)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.238 (n=2036)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=4822)

- **FILTRO** `ibs_7min` < `0.7406` → IC=-0.187 (n=1714)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7406
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=5144)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.182 (n=1707)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=5151)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.268 (n=1745)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=5315)

- **FILTRO** `ibs_7min` > `0.2759` → IC=-0.182 (n=1762)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2759
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=5298)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.185 (n=1727)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=5333)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.271 (n=1637)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=5424)

- **FILTRO** `ibs_7min` < `0.25` → IC=-0.232 (n=1736)

  - _Acción_: SKIP cuando `ibs_7min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=5325)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.182 (n=2393)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=7707)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.276 (n=1622)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=5201)

- **FILTRO** `ibs_7min` < `0.25` → IC=-0.222 (n=1693)

  - _Acción_: SKIP cuando `ibs_7min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=5130)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.200 (n=1683)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=5140)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.205 (n=2375)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=7218)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=1241)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.139 (n=164)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=499)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1156)

- **FILTRO** `libro_liquidez` < `7936.4939` → IC=-0.130 (n=347)

  - _Acción_: SKIP cuando `libro_liquidez` < 7936.4939
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=705)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=349)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.226 (n=49)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=403)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.129 (n=68)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=589)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=251)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3982` → IC=+0.135 (n=919)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.3982 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.138 (n=418)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 14.0 (IC base=+0.121)

- **PATRÓN** `total_vol_5m` < `442.4725` → IC=+0.147 (n=307)

  - _Acción_: Kelly boost +0.74€ cuando `total_vol_5m` < 442.4725 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.129 (n=788)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 53.0 (IC base=+0.121)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.438` → IC=+0.162 (n=72)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio` |x|> 0.438 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.226 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `2500.1426` → IC=+0.200 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2500.1426 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.181 (n=92)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 11.0 (IC base=+0.140)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.161 (n=57)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 8.0 (IC base=+0.105)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4139` → IC=+0.172 (n=126)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.86€ cuando `delta_ratio` |x|> 0.4139 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.197 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.110)

- **PATRÓN** `total_vol_5m` < `388.5476` → IC=+0.206 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 388.5476 (IC base=+0.110)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.182 (n=83)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 73.0 (IC base=+0.110)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3985` → IC=+0.177 (n=165)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio` |x|> 0.3985 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.188 (n=75)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 6.0 (IC base=+0.144)

- **PATRÓN** `total_vol_5m` < `8043.774` → IC=+0.167 (n=166)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 8043.774 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.173 (n=53)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 28.0 (IC base=+0.144)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `3602.5746` → IC=+0.175 (n=81)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 3602.5746 (IC base=+0.100)

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
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.192 (n=63)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=32)

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
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=244)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=333)

- **FILTRO** `streak_estiramiento` > `0.7643` → IC=-0.124 (n=99)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.7643
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=193)

- **PATRÓN** `streak_estiramiento` < `0.4493` → IC=+0.187 (n=97)

  - _Acción_: Kelly boost +0.93€ cuando `streak_estiramiento` < 0.4493 (IC base=+0.034)

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
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=53)

- **FILTRO** `volumen_racha` > `945898.4` → IC=-0.158 (n=36)

  - _Acción_: SKIP cuando `volumen_racha` > 945898.4
  - _Potencial_: sin este filtro IC_bueno=+0.141 (n=37)

- **FILTRO** `streak_estiramiento` > `0.4177` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4177
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=45)

- **PATRÓN** `streak_estiramiento` < `0.359` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `streak_estiramiento` < 0.359 (IC base=-0.007)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.126 (n=97)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 48.0 (IC base=+0.065)

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
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=557)

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
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=778)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1319)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=925)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=924)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3413)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=1776)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.211 (n=767)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.201)

- **PATRÓN** `sigma_h` > `0.011` → IC=+0.236 (n=767)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.1591` → IC=+0.207 (n=2025)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1591 (IC base=+0.201)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2208` → IC=+0.213 (n=768)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2208 (IC base=+0.201)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.129` → IC=+0.230 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.129 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.206 (n=2141)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.201)

- **PATRÓN** `ibs_15` > `0.6137` → IC=+0.279 (n=2300)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6137 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.1197` → IC=+0.202 (n=1161)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1197 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.921` → IC=+0.283 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.921 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `7427.7045` → IC=+0.207 (n=767)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7427.7045 (IC base=+0.201)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.215 (n=1354)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.201)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=990)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.228 (n=469)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.0582` → IC=+0.274 (n=157)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0582 (IC base=+0.216)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2017` → IC=+0.243 (n=212)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2017 (IC base=+0.216)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1443` → IC=+0.264 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1443 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.242 (n=436)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.216)

- **PATRÓN** `ibs_15` > `0.7112` → IC=+0.279 (n=468)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7112 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `0.1371` → IC=+0.250 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1371 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.724` → IC=+0.286 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.724 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `16193.642` → IC=+0.247 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16193.642 (IC base=+0.216)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.693` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.693
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=586)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.194 (n=171)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0034 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.0673` → IC=+0.162 (n=226)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.0673 (IC base=+0.146)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2356` → IC=+0.182 (n=171)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.91€ cuando `delta_ratio_macro` |x|> 0.2356 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1229` → IC=+0.173 (n=194)

  - _Acción_: Kelly boost +0.87€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1229 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.160 (n=368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 11.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.150 (n=238)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 6.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.5788` → IC=+0.243 (n=512)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5788 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.2696` → IC=+0.155 (n=474)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.2696 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.546` → IC=+0.230 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.546 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `3462.5082` → IC=+0.160 (n=457)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3462.5082 (IC base=+0.146)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `20.944` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 20.944
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=186)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.260 (n=102)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0087 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.1586` → IC=+0.213 (n=270)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1586 (IC base=+0.176)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0742` → IC=+0.188 (n=274)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.0742 (IC base=+0.176)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3457` → IC=+0.220 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3457 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.188 (n=219)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 11.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.179 (n=138)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 6.0 (IC base=+0.176)

- **PATRÓN** `ibs_15` > `0.5641` → IC=+0.266 (n=306)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5641 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.1308` → IC=+0.189 (n=175)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1308 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` < `0.1751` → IC=+0.178 (n=253)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.1751 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.265` → IC=+0.329 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.265 (IC base=+0.176)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.190 (n=201)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `2463.1153` → IC=+0.198 (n=306)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2463.1153 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.200 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.176)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.256` → IC=+0.154 (n=53)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 8.256 (IC base=+0.005)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.249 (n=513)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.0798` → IC=+0.215 (n=254)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0798 (IC base=+0.211)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0431` → IC=+0.215 (n=574)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0431 (IC base=+0.211)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0893` → IC=+0.272 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0893 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.240 (n=286)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.211)

- **PATRÓN** `ibs_15` > `0.5833` → IC=+0.291 (n=576)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5833 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.1345` → IC=+0.217 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1345 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` < `0.5506` → IC=+0.210 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5506 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.472` → IC=+0.239 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.472 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.39` → IC=+0.214 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.39 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.210 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2939.6834` → IC=+0.283 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2939.6834 (IC base=+0.211)

- **PATRÓN** `ibs_15` < `0.1143` → IC=+0.153 (n=626)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.76€ cuando `ibs_15` < 0.1143 (IC base=+0.065)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.370 (n=345)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.360)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.367 (n=517)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0027 (IC base=+0.360)

- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.362 (n=345)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.360)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1501` → IC=+0.382 (n=344)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1501 (IC base=+0.360)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1326` → IC=+0.391 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1326 (IC base=+0.360)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.401 (n=250)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.360)

- **PATRÓN** `ibs_15` > `0.7863` → IC=+0.398 (n=517)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7863 (IC base=+0.360)

- **PATRÓN** `dist_vwap_pct` > `0.1523` → IC=+0.378 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1523 (IC base=+0.360)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.259` → IC=+0.369 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.259 (IC base=+0.360)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.365 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.360)

- **PATRÓN** `libro_liquidez` > `3820.3005` → IC=+0.375 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3820.3005 (IC base=+0.360)

- **PATRÓN** `ballena_activa_n` < `444.0` → IC=+0.379 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 444.0 (IC base=+0.360)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.368 (n=248)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.362)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.366 (n=252)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0027 (IC base=+0.362)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.375 (n=94)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.362)

- **PATRÓN** `drift_15min` |x|≤ `0.5105` → IC=+0.363 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5105 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.370 (n=282)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.13` → IC=+0.391 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.13 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.381 (n=283)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.8038` → IC=+0.394 (n=282)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8038 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.3959` → IC=+0.406 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3959 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.997` → IC=+0.369 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.997 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` < `26.174` → IC=+0.361 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 26.174 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `16049.8465` → IC=+0.385 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16049.8465 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `500.0` → IC=+0.413 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 500.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.358 (n=104)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.354)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.381 (n=107)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.354)

- **PATRÓN** `drift_60min` |x|≤ `0.1062` → IC=+0.369 (n=158)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1062 (IC base=+0.354)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.374 (n=212)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.354)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.381 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.354)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.412 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.354)

- **PATRÓN** `ibs_15` > `0.7504` → IC=+0.403 (n=236)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7504 (IC base=+0.354)

- **PATRÓN** `dist_vwap_pct` > `0.4534` → IC=+0.377 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4534 (IC base=+0.354)

- **PATRÓN** `dist_vwap_pct` < `0.2936` → IC=+0.356 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2936 (IC base=+0.354)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.854` → IC=+0.379 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.854 (IC base=+0.354)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.77` → IC=+0.356 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.77 (IC base=+0.354)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.361 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.354)

- **PATRÓN** `libro_liquidez` > `4204.0039` → IC=+0.377 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4204.0039 (IC base=+0.354)

- **PATRÓN** `ballena_activa_n` < `148.0` → IC=+0.363 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 148.0 (IC base=+0.354)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0122` → IC=-0.223 (n=850)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0122
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=2551)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.203 (n=1241)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=2160)

- **PATRÓN** `delta_ratio_macro` |x|> `0.141` → IC=+0.182 (n=546)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.91€ cuando `delta_ratio_macro` |x|> 0.141 (IC base=-0.064)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1365` → IC=+0.246 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1365 (IC base=-0.064)

- **PATRÓN** `ibs_15` > `0.6389` → IC=+0.280 (n=819)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6389 (IC base=-0.064)

- **PATRÓN** `dist_vwap_pct` > `0.1081` → IC=+0.196 (n=475)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1081 (IC base=-0.064)

- **PATRÓN** `dist_vwap_pct` < `0.4129` → IC=+0.201 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4129 (IC base=-0.064)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1258` → IC=+0.253 (n=1742)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1258 (IC base=-0.018)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1854` → IC=+0.247 (n=1700)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1854 (IC base=-0.018)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.276 (n=2613)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.018)

- **PATRÓN** `dist_vwap_pct` > `0.8607` → IC=+0.294 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8607 (IC base=-0.018)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0467` → IC=-0.214 (n=1323)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0467
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=652)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.229 (n=493)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=1482)

- **FILTRO** `sigma_ewma_delta_pct` > `23.724` → IC=-0.264 (n=282)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.724
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=1693)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.179 (n=194)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0027 (IC base=+0.087)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2023` → IC=+0.304 (n=110)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2023 (IC base=+0.087)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1064` → IC=+0.325 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1064 (IC base=+0.087)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.121 (n=394)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 12.0 (IC base=+0.087)

- **PATRÓN** `ibs_15` > `0.7503` → IC=+0.328 (n=242)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7503 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.1012` → IC=+0.294 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1012 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.5105` → IC=+0.294 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5105 (IC base=+0.087)

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
  - _Potencial_: sin este filtro IC_bueno=+0.168 (n=519)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.164 (n=403)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0065 (IC base=+0.158)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.169 (n=360)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0038 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.0736` → IC=+0.215 (n=177)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0736 (IC base=+0.158)

- **PATRÓN** `drift_15min` |x|≤ `0.4132` → IC=+0.164 (n=135)

  - _Acción_: Kelly boost +0.82€ cuando `drift_15min` |x|≤ 0.4132 (IC base=+0.158)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0643` → IC=+0.158 (n=402)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio_macro` |x|> 0.0643 (IC base=+0.158)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.288` → IC=+0.215 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.288 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.181 (n=286)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 11.0 (IC base=+0.158)

- **PATRÓN** `ibs_15` > `0.6515` → IC=+0.265 (n=402)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6515 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` < `0.2672` → IC=+0.169 (n=373)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.2672 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.243` → IC=+0.220 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.243 (IC base=+0.158)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.168 (n=519)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `9422.8995` → IC=+0.170 (n=183)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 9422.8995 (IC base=+0.158)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.244 (n=955)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.3539` → IC=+0.240 (n=841)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3539 (IC base=+0.236)

- **PATRÓN** `drift_15min` |x|≤ `0.7675` → IC=+0.247 (n=841)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7675 (IC base=+0.236)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2094` → IC=+0.261 (n=433)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2094 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.237 (n=678)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.240 (n=845)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.236)

- **PATRÓN** `ibs_15` < `0.361` → IC=+0.268 (n=955)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.361 (IC base=+0.236)

- **PATRÓN** `dist_vwap_pct` > `0.7403` → IC=+0.308 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7403 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.315` → IC=+0.261 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.315 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.489` → IC=+0.241 (n=1004)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.489 (IC base=+0.236)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.17` → IC=-0.243 (n=270)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.17
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=527)

- **FILTRO** `drift_15min` |x|> `0.8825` → IC=-0.266 (n=199)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8825
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=598)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.216 (n=333)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=464)

- **FILTRO** `sigma_ewma_delta_pct` > `18.298` → IC=-0.140 (n=415)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.298
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=3350)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.167 (n=43)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.176)

- **PATRÓN** `ibs_15` > `0.5714` → IC=+0.233 (n=58)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5714 (IC base=-0.176)

- **PATRÓN** `dist_vwap_pct` > `0.2865` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.2865 (IC base=-0.176)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1292 (IC base=-0.176)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.214 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.176)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0786` → IC=+0.234 (n=377)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0786 (IC base=-0.039)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1879` → IC=+0.228 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1879 (IC base=-0.039)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.272 (n=423)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.6467` → IC=+0.236 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6467 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` < `0.172` → IC=+0.234 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.172 (IC base=-0.039)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.13` → IC=-0.218 (n=477)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.13
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=479)

- **FILTRO** `sigma_h` > `0.0194` → IC=-0.262 (n=477)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0194
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=479)

- **FILTRO** `drift_15min` |x|> `1.2211` → IC=-0.275 (n=238)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2211
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=718)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.202)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.202)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1476` → IC=+0.273 (n=297)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1476 (IC base=-0.030)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1704` → IC=+0.303 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1704 (IC base=-0.030)

- **PATRÓN** `ibs_15` < `0.3273` → IC=+0.293 (n=655)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3273 (IC base=-0.030)

- **PATRÓN** `dist_vwap_pct` > `0.8175` → IC=+0.356 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8175 (IC base=-0.030)

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
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.302 (n=559)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.293)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.293 (n=748)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.053` → IC=+0.330 (n=281)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.053 (IC base=+0.293)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2402` → IC=+0.304 (n=279)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2402 (IC base=+0.293)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.221` → IC=+0.319 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.221 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.313 (n=873)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.293)

- **PATRÓN** `ibs_15` > `0.8404` → IC=+0.327 (n=837)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8404 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.4333` → IC=+0.338 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4333 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.701` → IC=+0.347 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.701 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `12836.5354` → IC=+0.306 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12836.5354 (IC base=+0.293)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.296 (n=400)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.331 (n=152)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.288)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2556` → IC=+0.312 (n=152)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2556 (IC base=+0.288)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.109` → IC=+0.315 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.109 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.309 (n=479)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.288)

- **PATRÓN** `ibs_15` > `0.8305` → IC=+0.316 (n=455)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8305 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` > `0.4158` → IC=+0.347 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4158 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.360 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `16217.9862` → IC=+0.331 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16217.9862 (IC base=+0.288)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.306 (n=256)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.299)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.303 (n=383)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.299)

- **PATRÓN** `drift_60min` |x|≤ `0.0515` → IC=+0.323 (n=128)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0515 (IC base=+0.299)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3472` → IC=+0.316 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3472 (IC base=+0.299)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.325 (n=370)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.299)

- **PATRÓN** `ibs_15` > `0.8516` → IC=+0.339 (n=383)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8516 (IC base=+0.299)

- **PATRÓN** `dist_vwap_pct` > `0.4406` → IC=+0.311 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4406 (IC base=+0.299)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.266` → IC=+0.328 (n=184)

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

- **FILTRO** `ballena_activa_n` > `41.0` → IC=-0.197 (n=64)

  - _Acción_: SKIP cuando `ballena_activa_n` > 41.0
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=132)

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

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.318 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2122` → IC=-0.395 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2122
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0775` → IC=-0.292 (n=22)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0775
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `sigma_h` > `0.0046` → IC=-0.214 (n=33)
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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6137 sube el IC de +0.201 a +0.279 en UPDOWN_GBM#15min (n=2300). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7112 sube el IC de +0.216 a +0.279 en UPDOWN_GBM#BTC#15min (n=468). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5788 sube el IC de +0.146 a +0.243 en UPDOWN_GBM#ETH#15min (n=512). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.5641 sube el IC de +0.176 a +0.266 en UPDOWN_GBM#SOL#15min (n=306). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5833 sube el IC de +0.211 a +0.291 en UPDOWN_GBM#XRP#15min (n=576). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1143 sube el IC de +0.065 a +0.153 en UPDOWN_GBM#XRP#15min (n=626). Ya aplicado como kelly_boost=+0.76€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6389 sube el IC de -0.064 a +0.280 en UPDOWN_GBM_15M_TARDIO (n=819). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.018 a +0.276 en UPDOWN_GBM_15M_TARDIO (n=2613). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7503 sube el IC de +0.087 a +0.328 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=242). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.5625 sube el IC de -0.192 a +0.333 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=40). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6515 sube el IC de +0.158 a +0.265 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=402). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.361 sube el IC de +0.236 a +0.268 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=955). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5714 sube el IC de -0.176 a +0.233 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=58). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.039 a +0.272 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=423). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.202 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3273 sube el IC de -0.030 a +0.293 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=655). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8404 sube el IC de +0.293 a +0.327 en UPDOWN_GBM_IBS_ALTO (n=837). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8305 sube el IC de +0.288 a +0.316 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=455). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8516 sube el IC de +0.299 a +0.339 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=383). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7863 sube el IC de +0.360 a +0.398 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=517). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8038 sube el IC de +0.362 a +0.394 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=282). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7504 sube el IC de +0.354 a +0.403 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=236). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1534 | +0.096 | +189.64€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1534 | +0.096 | +189.64€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1166 | +0.103 | +161.22€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1166 | +0.103 | +161.22€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 265 | +0.069 | +12.71€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 265 | +0.069 | +12.71€ | 6 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 72 | +0.108 | +16.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 72 | +0.108 | +16.05€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 167 | +0.033 | +39.68€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 167 | +0.033 | +39.68€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 140 | +0.035 | +36.24€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 140 | +0.035 | +36.24€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 5 | +0.054 | +1.13€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 5 | +0.054 | +1.13€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 22 | -0.042 | +2.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 22 | -0.042 | +2.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 33643 | -0.086 | -4480.58€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1713 | -0.016 | -218.72€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 31930 | -0.090 | -4261.86€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4305 | -0.118 | -749.71€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4305 | -0.118 | -749.71€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1713 | -0.016 | -218.72€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1713 | -0.016 | -218.72€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3923 | -0.112 | -881.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3923 | -0.112 | -881.93€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 8726 | -0.001 | -823.24€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 8726 | -0.001 | -823.24€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 8452 | -0.104 | -582.94€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 8452 | -0.104 | -582.94€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 6524 | -0.157 | -1224.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 6524 | -0.157 | -1224.05€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 25502 | -0.020 | +3795.89€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 6602 | +0.002 | +1771.87€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 18900 | -0.028 | +2024.02€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 25502 | -0.020 | +3795.89€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 6602 | +0.002 | +1771.87€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 18900 | -0.028 | +2024.02€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 115258 | +0.114 | -5106.51€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 16186 | +0.183 | -483.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 489 | -0.050 | -61.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 91415 | +0.103 | -4295.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 7168 | +0.104 | -266.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 15181 | +0.103 | -1064.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 53 | -0.136 | +12.04€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 15113 | +0.104 | -1064.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 22866 | +0.130 | -351.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4858 | +0.197 | -127.71€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 15160 | +0.117 | -133.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2806 | +0.091 | -68.12€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 15228 | +0.094 | -1232.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 61 | -0.119 | -6.11€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 15152 | +0.095 | -1215.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 24481 | +0.125 | -415.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 6538 | +0.176 | -103.26€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 15328 | +0.107 | -250.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2603 | +0.100 | -52.80€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 22303 | +0.115 | -1207.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4621 | +0.189 | -267.82€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 392 | -0.013 | -7.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 15531 | +0.094 | -786.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1759 | +0.130 | -145.94€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#XRP | 15199 | +0.102 | -833.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 55 | -0.044 | +9.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 15131 | +0.102 | -843.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 18389 | +0.195 | -1146.16€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 18389 | +0.195 | -1146.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4274 | +0.175 | -394.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4274 | +0.175 | -394.12€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1964 | +0.202 | -29.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1964 | +0.202 | -29.05€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 4214 | +0.182 | -340.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 4214 | +0.182 | -340.29€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3706 | +0.242 | -128.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3706 | +0.242 | -128.53€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4152 | +0.189 | -267.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4152 | +0.189 | -267.92€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 862 | +0.431 | -22.88€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 862 | +0.431 | -22.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 341 | +0.436 | -5.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 341 | +0.436 | -5.01€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 325 | +0.436 | -4.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 325 | +0.436 | -4.30€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 184 | +0.409 | -11.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 184 | +0.409 | -11.13€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 63840 | +0.200 | -4742.49€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 63840 | +0.200 | -4742.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 10982 | +0.183 | -1164.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 10982 | +0.183 | -1164.85€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 10263 | +0.225 | -346.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 10263 | +0.225 | -346.78€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 10983 | +0.176 | -1235.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 10983 | +0.176 | -1235.46€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 10327 | +0.221 | -376.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 10327 | +0.221 | -376.99€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 10576 | +0.202 | -699.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 10576 | +0.202 | -699.91€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 10709 | +0.193 | -918.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 10709 | +0.193 | -918.50€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 24295 | +0.117 | +165.48€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 24295 | +0.117 | +165.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 12064 | +0.120 | +146.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 12064 | +0.120 | +146.24€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 12231 | +0.113 | +19.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 12231 | +0.113 | +19.24€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1736 | +0.289 | -21.74€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1736 | +0.289 | -21.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 783 | +0.280 | -16.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 783 | +0.280 | -16.81€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 836 | +0.288 | -9.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 836 | +0.288 | -9.15€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 117 | +0.349 | +4.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 117 | +0.349 | +4.22€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 779 | +0.439 | -0.58€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 779 | +0.439 | -0.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 374 | +0.436 | -2.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 374 | +0.436 | -2.83€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 359 | +0.442 | +1.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 359 | +0.442 | +1.70€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1335 | +0.070 | -61.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 482 | +0.056 | -40.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 853 | +0.078 | -20.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1046 | +0.076 | -29.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 193 | +0.069 | -8.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 853 | +0.078 | -20.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 223 | +0.029 | -33.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 223 | +0.029 | -33.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 46500 | +0.100 | -1209.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3777 | +0.092 | +51.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 42723 | +0.100 | -1261.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 25804 | +0.104 | -290.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3777 | +0.092 | +51.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 22027 | +0.106 | -342.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 9184 | +0.109 | -24.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 9184 | +0.109 | -24.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 11512 | +0.081 | -894.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 11512 | +0.081 | -894.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 867 | +0.205 | -102.15€ | 3 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 867 | +0.205 | -102.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 867 | +0.205 | -102.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 867 | +0.205 | -102.15€ | 3 | 4 |
| ✅ GBM_LATE_15M | 32603 | +0.088 | +16193.17€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 32603 | +0.088 | +16193.17€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 5486 | +0.203 | +4229.67€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 5486 | +0.203 | +4229.67€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 4827 | +0.178 | +3473.02€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 4827 | +0.178 | +3473.02€ | 0 | 26 |
| ✅ GBM_LATE_15M#DOGE | 5792 | +0.200 | +4373.96€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 5792 | +0.200 | +4373.96€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 4623 | +0.033 | +1162.71€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4623 | +0.033 | +1162.71€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 4646 | -0.031 | +1017.12€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 4646 | -0.031 | +1017.12€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 7229 | -0.036 | +1936.70€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 7229 | -0.036 | +1936.70€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 35188 | +0.087 | +18713.62€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 35188 | +0.087 | +18713.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 6795 | +0.012 | +3509.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 6795 | +0.012 | +3509.70€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 7288 | +0.014 | +1550.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 7288 | +0.014 | +1550.40€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 4972 | +0.267 | +5108.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 4972 | +0.267 | +5108.61€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 5932 | +0.010 | +1302.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 5932 | +0.010 | +1302.95€ | 1 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 5727 | +0.036 | +2296.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 5727 | +0.036 | +2296.27€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4474 | +0.286 | +4945.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4474 | +0.286 | +4945.69€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 26128 | +0.174 | +20291.70€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 26128 | +0.174 | +20291.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3943 | +0.218 | +3316.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3943 | +0.218 | +3316.32€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 4108 | +0.150 | +2987.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 4108 | +0.150 | +2987.28€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 4147 | +0.214 | +3401.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 4147 | +0.214 | +3401.54€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 4391 | +0.138 | +3232.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 4391 | +0.138 | +3232.80€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 4896 | +0.123 | +3557.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 4896 | +0.123 | +3557.54€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4643 | +0.211 | +3796.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4643 | +0.211 | +3796.22€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 7103 | +0.138 | +3379.29€ | 0 | 23 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 7103 | +0.138 | +3379.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 340 | +0.140 | +187.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 340 | +0.140 | +187.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2087 | +0.145 | +1138.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2087 | +0.145 | +1138.76€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 375 | +0.142 | +175.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 375 | +0.142 | +175.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2161 | +0.155 | +1068.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2161 | +0.155 | +1068.85€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1604 | +0.107 | +574.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1604 | +0.107 | +574.16€ | 1 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 536 | +0.134 | +234.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 536 | +0.134 | +234.64€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 32851 | +0.180 | +25317.34€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 32851 | +0.180 | +25317.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 5225 | +0.230 | +4637.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 5225 | +0.230 | +4637.36€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 5074 | +0.148 | +3328.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 5074 | +0.148 | +3328.14€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 5492 | +0.228 | +4776.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 5492 | +0.228 | +4776.45€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 5344 | +0.135 | +3706.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 5344 | +0.135 | +3706.37€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 5796 | +0.123 | +3995.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 5796 | +0.123 | +3995.86€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 5920 | +0.215 | +4873.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 5920 | +0.215 | +4873.17€ | 0 | 22 |
| ✅ GBM_LATE_5M | 8945 | +0.176 | +6025.53€ | 1 | 30 |
| ✅ GBM_LATE_5M#5min | 8945 | +0.176 | +6025.53€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 835 | +0.229 | +729.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 835 | +0.229 | +729.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2110 | +0.169 | +1522.65€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2110 | +0.169 | +1522.65€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 984 | +0.174 | +638.70€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 984 | +0.174 | +638.70€ | 0 | 17 |
| ✅ GBM_LATE_5M#ETH | 2837 | +0.180 | +1870.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2837 | +0.180 | +1870.40€ | 0 | 29 |
| ✅ GBM_LATE_5M#SOL | 1067 | +0.166 | +681.78€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1067 | +0.166 | +681.78€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1112 | +0.148 | +582.60€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1112 | +0.148 | +582.60€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2401 | +0.073 | +900.87€ | 0 | 12 |
| ✅ GBM_LATE_60M#60min | 2401 | +0.073 | +900.87€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 903 | +0.090 | +340.99€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 903 | +0.090 | +340.99€ | 0 | 12 |
| ✅ GBM_LATE_60M#ETH | 754 | +0.073 | +345.98€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 754 | +0.073 | +345.98€ | 2 | 10 |
| ✅ GBM_LATE_60M#SOL | 744 | +0.052 | +213.91€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 744 | +0.052 | +213.91€ | 2 | 12 |
| 🚫 GBM_LATE_60M_FADE | 464 | -0.236 | -9.91€ | 9 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 464 | -0.236 | -9.91€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 171 | -0.217 | -5.91€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 171 | -0.217 | -5.91€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 162 | -0.226 | +0.64€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 162 | -0.226 | +0.64€ | 5 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 131 | -0.267 | -4.64€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 131 | -0.267 | -4.64€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1030 | +0.088 | +269.46€ | 0 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1030 | +0.088 | +269.46€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 385 | +0.079 | +83.90€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 385 | +0.079 | +83.90€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 346 | +0.058 | +46.42€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 346 | +0.058 | +46.42€ | 3 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 299 | +0.135 | +139.15€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 299 | +0.135 | +139.15€ | 2 | 14 |
| ✅ LATE_WINDOW_5MIN | 126 | +0.242 | +101.52€ | 0 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 126 | +0.242 | +101.52€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 126 | +0.242 | +101.52€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 126 | +0.242 | +101.52€ | 0 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 2743 | +0.103 | +727.10€ | 0 | 3 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2743 | +0.103 | +727.10€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2743 | +0.103 | +727.10€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2743 | +0.103 | +727.10€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M | 420 | -0.071 | -32.62€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 420 | -0.071 | -32.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 114 | -0.035 | -2.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 114 | -0.035 | -2.25€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 68 | -0.086 | -7.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 68 | -0.086 | -7.96€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 157 | -0.028 | -5.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 157 | -0.028 | -5.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 2797 | +0.022 | +73.14€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2797 | +0.022 | +73.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 139 | +0.039 | +0.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 139 | +0.039 | +0.87€ | 1 | 1 |
| ✅ LIQUIDACIONES_5M#BTC | 417 | +0.027 | +31.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 417 | +0.027 | +31.78€ | 4 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 201 | -0.022 | -6.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 201 | -0.022 | -6.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1056 | +0.029 | +29.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1056 | +0.029 | +29.08€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 639 | +0.016 | +3.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 639 | +0.016 | +3.31€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 345 | +0.019 | +14.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 345 | +0.019 | +14.21€ | 1 | 2 |
| ✅ LIQUIDACIONES_60M | 1367 | -0.045 | -29.69€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1367 | -0.045 | -29.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 392 | -0.043 | -14.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 392 | -0.043 | -14.26€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 452 | -0.024 | +0.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 452 | -0.024 | +0.26€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 523 | -0.064 | -15.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 523 | -0.064 | -15.69€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 4459 | -0.015 | +134.44€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 2113 | -0.017 | +50.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 2346 | -0.012 | +83.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 124 | -0.008 | +3.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 63 | +0.054 | +11.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 61 | -0.071 | -8.20€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 1096 | -0.003 | +43.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 519 | -0.007 | +14.59€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 577 | +0.001 | +28.49€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 507 | -0.015 | +19.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 251 | -0.022 | +5.77€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 256 | -0.008 | +14.10€ | 2 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 906 | -0.032 | -13.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 415 | -0.049 | -24.48€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 491 | -0.017 | +10.98€ | 3 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 876 | -0.017 | +27.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 427 | -0.018 | +16.39€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 449 | -0.017 | +10.82€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 950 | -0.009 | +54.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 438 | -0.004 | +27.21€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 512 | -0.014 | +27.53€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 37684 | -0.004 | +1759.90€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 37684 | -0.004 | +1759.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 6713 | +0.024 | +892.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 6713 | +0.024 | +892.39€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 5635 | -0.032 | -99.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 5635 | -0.032 | -99.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 6807 | +0.019 | +668.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 6807 | +0.019 | +668.02€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 5430 | -0.052 | -163.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 5430 | -0.052 | -163.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 6351 | -0.009 | +195.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 6351 | -0.009 | +195.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 6748 | +0.012 | +266.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 6748 | +0.012 | +266.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6157 | -0.059 | -144.90€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6157 | -0.059 | -144.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1218 | +0.001 | -13.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1218 | +0.001 | -13.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1516 | -0.077 | -32.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1516 | -0.077 | -32.76€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 706 | -0.126 | -34.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 706 | -0.126 | -34.18€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1816 | -0.077 | -33.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1816 | -0.077 | -33.82€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 856 | -0.015 | -25.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 856 | -0.015 | -25.00€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3349 | +0.004 | -1.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3349 | +0.004 | -1.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 191 | +0.018 | +1.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 191 | +0.018 | +1.53€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 137 | -0.004 | -2.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 137 | -0.004 | -2.36€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1317 | +0.006 | +6.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1317 | +0.006 | +6.68€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1388 | +0.007 | +0.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1388 | +0.007 | +0.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 94648 | -0.073 | +1688.78€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 94648 | -0.073 | +1688.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 16262 | -0.073 | +901.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 16262 | -0.073 | +901.86€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 14385 | -0.098 | -772.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 14385 | -0.098 | -772.27€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 16506 | -0.066 | +914.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 16506 | -0.066 | +914.25€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 13918 | -0.095 | -416.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 13918 | -0.095 | -416.55€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 17161 | -0.052 | +349.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 17161 | -0.052 | +349.75€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 16416 | -0.063 | +711.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 16416 | -0.063 | +711.75€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8052 | -0.031 | -149.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8052 | -0.031 | -149.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1919 | -0.042 | -18.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1919 | -0.042 | -18.00€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2241 | -0.025 | -29.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2241 | -0.025 | -29.92€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1109 | -0.049 | -23.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1109 | -0.049 | -23.19€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 779 | -0.022 | -25.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 779 | -0.022 | -25.26€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1361 | +0.115 | +498.11€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1225 | +0.121 | +485.51€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 287 | +0.140 | +146.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 287 | +0.140 | +146.99€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 231 | +0.105 | +63.14€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 231 | +0.105 | +63.14€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 249 | +0.110 | +93.07€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 249 | +0.110 | +93.07€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 220 | +0.144 | +113.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 220 | +0.144 | +113.40€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 238 | +0.100 | +68.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 238 | +0.100 | +68.91€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 904 | -0.018 | -23.46€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 904 | -0.018 | -23.46€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 178 | +0.000 | +5.71€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 178 | +0.000 | +5.71€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 130 | -0.008 | -0.82€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 130 | -0.008 | -0.82€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 242 | -0.041 | -19.92€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 242 | -0.041 | -19.92€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 197 | +0.007 | +1.85€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 197 | +0.007 | +1.85€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 157 | -0.041 | -10.28€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 157 | -0.041 | -10.28€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 753 | -0.092 | -72.24€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 344 | -0.144 | -82.11€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 264 | -0.188 | -74.97€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 80 | +0.000 | -7.14€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 267 | -0.050 | -2.77€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 188 | -0.053 | -3.54€ | 2 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 79 | -0.043 | +0.77€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 142 | -0.042 | +12.63€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 113 | -0.057 | +7.23€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 29 | +0.016 | +5.41€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 565 | -0.117 | -71.28€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 188 | -0.016 | -0.96€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 895 | -0.202 | -53.85€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 372 | -0.195 | -33.02€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 317 | -0.199 | -33.81€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 55 | -0.167 | +0.79€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 302 | -0.217 | -32.10€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 258 | -0.227 | -37.67€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 44 | -0.152 | +5.58€ | 1 | 0 |
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
| ✅ STREAK_FADE_15M | 615 | +0.027 | +15.84€ | 3 | 1 |
| ✅ STREAK_FADE_15M#15min | 615 | +0.027 | +15.84€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 295 | +0.022 | +2.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 295 | +0.022 | +2.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 46 | +0.042 | -0.04€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 46 | +0.042 | -0.04€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 65 | -0.007 | -1.72€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 65 | -0.007 | -1.72€ | 2 | 0 |
| ✅ STREAK_FADE_15M#XRP | 209 | +0.040 | +15.29€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 209 | +0.040 | +15.29€ | 3 | 2 |
| ✅ STREAK_FADE_5M | 3079 | -0.021 | -121.33€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3079 | -0.021 | -121.33€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 907 | -0.020 | -31.15€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 907 | -0.020 | -31.15€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 579 | -0.027 | -25.73€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 579 | -0.027 | -25.73€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1437 | -0.017 | -50.04€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1437 | -0.017 | -50.04€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 85 | -0.052 | -8.44€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 85 | -0.052 | -8.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 47 | -0.010 | -4.00€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 47 | -0.010 | -4.00€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 9651 | +0.019 | +104.08€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 9651 | +0.019 | +104.08€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2629 | +0.021 | +27.79€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2629 | +0.021 | +27.79€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2270 | +0.026 | +46.89€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2270 | +0.026 | +46.89€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2861 | +0.010 | -0.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2861 | +0.010 | -0.81€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1891 | +0.021 | +30.22€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1891 | +0.021 | +30.22€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 8694 | +0.013 | -44.01€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 8694 | +0.013 | -44.01€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3432 | +0.017 | -9.04€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3432 | +0.017 | -9.04€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3452 | +0.012 | -22.35€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3452 | +0.012 | -22.35€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1810 | +0.008 | -12.63€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1810 | +0.008 | -12.63€ | 1 | 0 |
| ✅ UPDOWN_GBM | 55943 | +0.044 | +4259.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 13997 | +0.079 | +2953.57€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 1853 | +0.005 | +7.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 36657 | +0.037 | +1253.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 3237 | +0.006 | +46.09€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 5734 | +0.081 | +782.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1129 | +0.156 | +496.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 37 | -0.038 | -1.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 4568 | +0.064 | +288.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 10798 | +0.050 | +866.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1794 | +0.090 | +410.38€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 494 | +0.012 | +5.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 6968 | +0.053 | +406.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1468 | +0.005 | +40.82€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 74 | -0.079 | +2.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 6652 | +0.053 | +540.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1101 | +0.139 | +400.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 35 | -0.013 | -2.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 5516 | +0.036 | +142.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 12252 | +0.034 | +674.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3399 | +0.056 | +460.10€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 487 | +0.007 | +8.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 7202 | +0.032 | +201.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1099 | +0.005 | -0.03€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 65 | -0.112 | +3.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 12448 | +0.022 | +447.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 3312 | +0.032 | +285.70€ | 0 | 13 |
| ✅ UPDOWN_GBM#SOL#240min | 477 | -0.001 | -0.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 7931 | +0.022 | +161.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 670 | +0.007 | +5.30€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 58 | -0.150 | -5.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 8057 | +0.051 | +951.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3262 | +0.099 | +900.37€ | 0 | 13 |
| ✅ UPDOWN_GBM#XRP#240min | 323 | +0.005 | -1.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 4472 | +0.020 | +52.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 197 | -0.113 | +1.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 689 | +0.360 | +241.77€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 689 | +0.360 | +241.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 375 | +0.362 | +128.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 375 | +0.362 | +128.07€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 314 | +0.354 | +113.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 314 | +0.354 | +113.70€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 15603 | -0.028 | +3610.58€ | 2 | 9 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 15603 | -0.028 | +3610.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1230 | -0.056 | +398.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1230 | -0.056 | +398.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2748 | -0.113 | +122.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2748 | -0.113 | +122.18€ | 3 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 680 | +0.205 | +524.50€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 680 | +0.205 | +524.50€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1809 | +0.213 | +1152.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1809 | +0.213 | +1152.25€ | 1 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 4562 | -0.063 | +609.34€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 4562 | -0.063 | +609.34€ | 4 | 10 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 4574 | -0.066 | +803.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 4574 | -0.066 | +803.44€ | 3 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 176 | +0.028 | +6.95€ | 1 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 176 | +0.028 | +6.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 176 | +0.028 | +6.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 176 | +0.028 | +6.95€ | 1 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1116 | +0.293 | +923.74€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1116 | +0.293 | +923.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 606 | +0.288 | +465.31€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 606 | +0.288 | +465.31€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 510 | +0.299 | +458.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 510 | +0.299 | +458.44€ | 0 | 8 |
| ✅ UPDOWN_OU_5M | 758 | -0.115 | -85.64€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#5min | 758 | -0.115 | -85.64€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 224 | -0.088 | -18.30€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 224 | -0.088 | -18.30€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 73 | -0.167 | -9.78€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 73 | -0.167 | -9.78€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 82 | -0.191 | -7.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 82 | -0.191 | -7.51€ | 2 | 0 |
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
  - _Estado_: IC=+0.020 n=688 — no justifica filtro, seguir monitorizando
  - _Datos_: n=688 IC=+0.020 PNL=+31.27€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 616 celda(s) pasan gate riguroso completo de 2448 evaluadas (n>=40) y 3421 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.032 < 0.08 — monitorear
  - _Datos_: n=3305 IC=+0.032 PNL=+285.41€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.129 n=531/60 | contraria IC=+0.188 n=539 | gap=-0.059 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=375, boost estimado=+0.007. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1098/40 IC=+0.004 PNL=-0.57€ | BTC#60min: n=1466/40 IC=+0.005 PNL=+40.66€ | SOL#60min: n=669/40 IC=+0.008 PNL=+5.81€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.049 n=431155 | tras_1loss IC=+0.088 n=330933 | tras_2loss IC=+0.057 n=136226/40 | gap=-0.009 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.213 > 0.08 con n=528 PNL=+391.94€
  - _Datos_: n=528 IC=+0.213 PNL=+391.94€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.226 > 0.08 con n=49 PNL=+34.92€
  - _Datos_: n=49 IC=+0.226 PNL=+34.92€

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
  - _Estado_: n=437 IC=+0.076 PNL=+51.65€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=437 IC=+0.076 PNL=+51.65€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=65 IC=+0.172 PNL=+39.69€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=65 IC=+0.172 PNL=+39.69€

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
  - _Estado_: n=2192 IC=+0.009 PNL=+7.10€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2192 IC=+0.009 PNL=+7.10€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1041 IC=-0.001 PNL=+38.79€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1041 IC=-0.001 PNL=+38.79€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=688 IC=+0.020 PNL=+31.27€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=688 IC=+0.020 PNL=+31.27€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.201 > 0.1 con n=3059 PNL=+2152.45€
  - _Datos_: n=3059 IC=+0.201 PNL=+2152.45€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1791 IC=+0.089 PNL=+409.95€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1791 IC=+0.089 PNL=+409.95€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.242 n=126) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=126 IC=+0.242 PNL=+101.52€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.119 > 0.02 con n=781 PNL=+300.85€
  - _Datos_: n=781 IC=+0.119 PNL=+300.85€

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
  - _Estado_: n=20792 IC=+0.069 PNL=+2892.39€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=20792 IC=+0.069 PNL=+2892.39€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.146 < -0.1 con n=329 PNL=+34.28€
  - _Datos_: n=329 IC=-0.146 PNL=+34.28€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2494 IC=+0.065 PNL=+290.45€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2494 IC=+0.065 PNL=+290.45€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.119 > 0.1 con n=589 PNL=+153.93€
  - _Datos_: n=589 IC=+0.119 PNL=+153.93€

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
  - _Estado_: n=23623 IC=-0.136 PNL=+1681.78€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=23623 IC=-0.136 PNL=+1681.78€

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
  - _Estado_: n=2416 IC=+0.137 PNL=+1399.26€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2416 IC=+0.137 PNL=+1399.26€

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
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.228 < -0.1 con n=2393 PNL=-204.68€
  - _Datos_: n=2393 IC=-0.228 PNL=-204.68€

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
  - _Estado_: n=49 IC=-0.010 PNL=+3.83€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=49 IC=-0.010 PNL=+3.83€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.101 n=1397) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1397 IC=+0.101 PNL=+318.50€

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
  - _Estado_: n=10974 IC=+0.183 PNL=-1164.79€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=10974 IC=+0.183 PNL=-1164.79€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.210 > 0.1 con n=174 PNL=+108.08€
  - _Datos_: n=174 IC=+0.210 PNL=+108.08€
