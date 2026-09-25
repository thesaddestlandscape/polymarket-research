# Hipótesis automáticas — 2026-09-25 21:48 UTC
_Generado por shadow_postmortem.py sobre 610691 resoluciones (PNL=+69067.02€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=502)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.236 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.140)

- **PATRÓN** `n_total_lado` > `75.0` → IC=+0.209 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 75.0 (IC base=+0.140)

- **PATRÓN** `banda_hit_calibrado` > `0.8026` → IC=+0.257 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8026 (IC base=+0.140)

- **PATRÓN** `banda_z` > `4.083` → IC=+0.164 (n=546)

  - _Acción_: Kelly boost +0.82€ cuando `banda_z` > 4.083 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.151 (n=505)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=585)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `3000.2192` → IC=+0.150 (n=364)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3000.2192 (IC base=+0.140)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.123 (n=502)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.495 (IC base=+0.052)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.141 (n=182)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 94.0 (IC base=+0.052)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.134 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.258 (n=420)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=368)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.258 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.149)

- **PATRÓN** `n_total_lado` > `70.0` → IC=+0.210 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 70.0 (IC base=+0.149)

- **PATRÓN** `banda_hit_calibrado` > `0.624` → IC=+0.265 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.624 (IC base=+0.149)

- **PATRÓN** `banda_z` > `4.287` → IC=+0.177 (n=438)

  - _Acción_: Kelly boost +0.89€ cuando `banda_z` > 4.287 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.170 (n=313)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 11.0 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=496)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `4494.3377` → IC=+0.150 (n=198)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 4494.3377 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `11799.9463` → IC=+0.128 (n=143)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 11799.9463 (IC base=+0.054)

- **PATRÓN** `ballena_activa_n` < `95.0` → IC=+0.153 (n=142)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 95.0 (IC base=+0.054)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.214 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=+0.218 (n=101)

- **FILTRO** `banda_hit_calibrado` < `0.6297` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6297
  - _Potencial_: sin este filtro IC_bueno=+0.239 (n=90)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.170 (n=107)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.371 (n=29)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=91)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.177 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=91)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=104)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.250 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.55 (IC base=+0.110)

- **PATRÓN** `banda_hit_calibrado` > `0.6297` → IC=+0.239 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6297 (IC base=+0.110)

- **PATRÓN** `banda_z` > `8.424` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `banda_z` > 8.424 (IC base=+0.110)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.170 (n=107)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.02 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `1356.6996` → IC=+0.146 (n=46)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1356.6996 (IC base=+0.110)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.122 (n=88)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.495 (IC base=-0.008)

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
- **FILTRO** `restante_s_al_confirmar` < `146.36` → IC=-0.228 (n=7201)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.36
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=21605)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `137.45` → IC=-0.251 (n=949)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 137.45
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=2850)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` < `499.92` → IC=-0.143 (n=373)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 499.92
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=1122)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `125.44` → IC=-0.307 (n=870)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.44
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=2613)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `166.21` → IC=-0.213 (n=1748)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 166.21
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=5247)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `127.73` → IC=-0.350 (n=1415)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.73
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=4246)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.47` → IC=-0.230 (n=357)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=408)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.204 (n=174)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=539)

- **FILTRO** `py_entrada` < `0.48` → IC=-0.145 (n=150)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=563)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.205 (n=14079)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=3555)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `5661.7901` → IC=+0.179 (n=2263)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 5661.7901 (IC base=+0.101)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.138 (n=11751)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.136 (n=14118)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.231 (n=11110)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.174 (n=5754)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `7880.4556` → IC=+0.174 (n=2173)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 7880.4556 (IC base=+0.127)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.211 (n=1678)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.207 (n=1717)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.353 (n=796)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=2166)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `16028.7692` → IC=+0.240 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16028.7692 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.205 (n=1562)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.207 (n=1724)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.263 (n=1573)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=2208)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `15900.4073` → IC=+0.217 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15900.4073 (IC base=+0.202)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.615` → IC=+0.172 (n=330)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` > 0.615 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `4614.6151` → IC=+0.144 (n=237)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 4614.6151 (IC base=+0.101)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.143 (n=359)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.105)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.143 (n=829)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.44 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.124 (n=559)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `5856.6213` → IC=+0.164 (n=221)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 5856.6213 (IC base=+0.105)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.155 (n=2865)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.146 (n=2438)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 15.0 (IC base=+0.145)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.343 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.249 (n=539)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `py_entrada` < `0.26` → IC=+0.358 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.26 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.235 (n=1511)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.232)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.155 (n=471)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 11.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.139 (n=677)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 17.0 (IC base=+0.137)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.241 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.149 (n=556)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `1313.4858` → IC=+0.150 (n=672)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1313.4858 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.071)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=717)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.207)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.435 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.164 (n=558)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.165 (n=592)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 7.0 (IC base=+0.160)

- **PATRÓN** `py_entrada` < `0.315` → IC=+0.295 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.315 (IC base=+0.160)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.170 (n=735)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.160)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.174 (n=308)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 7.0 (IC base=+0.163)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.365 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.163)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.163 (n=188)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.02 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `1244.5613` → IC=+0.152 (n=228)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1244.5613 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.147 (n=315)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.111)

- **PATRÓN** `py_entrada` < `0.355` → IC=+0.197 (n=394)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.355 (IC base=+0.111)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.8` → IC=-0.333 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=131)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=11756)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.200 (n=11224)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.225 (n=3858)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.339 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `8491.3442` → IC=+0.342 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8491.3442 (IC base=+0.197)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=2837)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.173 (n=2693)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 17.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.176 (n=2687)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.73 (IC base=+0.167)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.246 (n=896)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.245 (n=886)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.242)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.351 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.242)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.185 (n=2652)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.184 (n=2669)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=2289)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.249 (n=2470)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.239)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.324 (n=782)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.321 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.239)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.199 (n=2710)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.194 (n=2607)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 17.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.197 (n=2013)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.71 (IC base=+0.192)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.434 (n=541)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.428)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.427 (n=481)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.428)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.428)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.428)

- **PATRÓN** `libro_liquidez` > `11247.6748` → IC=+0.456 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11247.6748 (IC base=+0.428)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.441 (n=218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.439 (n=212)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.452 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `14347.2058` → IC=+0.443 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14347.2058 (IC base=+0.439)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.441 (n=184)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.430)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.458 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.430)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.430)

- **PATRÓN** `libro_liquidez` > `3376.5741` → IC=+0.441 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3376.5741 (IC base=+0.430)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.407 (n=106)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.406)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.407 (n=106)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.406)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.419 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.406)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.408 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.406)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.775` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=16)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=23)

- **FILTRO** `libro_liquidez` < `7880.4556` → IC=-0.339 (n=29)

  - _Acción_: SKIP cuando `libro_liquidez` < 7880.4556
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.201 (n=35010)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.235 (n=15529)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.177 (n=6042)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 8.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.180 (n=4833)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 12.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=6524)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=6279)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.224 (n=6252)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.264 (n=3556)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.177 (n=6014)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 8.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.189 (n=6354)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.172)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=3154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=2362)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.267 (n=2152)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.220)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.210 (n=5800)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.255 (n=2321)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.196 (n=5852)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 8.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=5823)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.251 (n=2196)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=5307)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` < `4.16` → IC=+0.126 (n=4920)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.16 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.139 (n=5381)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.95 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.128 (n=7294)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 8.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.74` → IC=+0.140 (n=4908)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.74 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.198 (n=2672)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.38 (IC base=+0.121)

- **PATRÓN** `restante_min` < `4.12` → IC=+0.128 (n=2448)

  - _Acción_: Kelly boost +0.64€ cuando `restante_min` < 4.12 (IC base=+0.121)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.140 (n=2677)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.94 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.138 (n=2799)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 6.0 (IC base=+0.121)

- **PATRÓN** `lag_apertura_s` < `3.35` → IC=+0.143 (n=2445)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 3.35 (IC base=+0.121)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.189 (n=2635)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.113)

- **PATRÓN** `restante_min` < `4.19` → IC=+0.126 (n=2472)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.19 (IC base=+0.113)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.134 (n=2714)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.96 (IC base=+0.113)

- **PATRÓN** `lag_apertura_s` < `2.27` → IC=+0.139 (n=2479)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.27 (IC base=+0.113)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.317 (n=803)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.380 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `1547.5346` → IC=+0.293 (n=1125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1547.5346 (IC base=+0.288)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.296 (n=351)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.275)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.323 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.275)

- **PATRÓN** `libro_liquidez` > `4267.8515` → IC=+0.295 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4267.8515 (IC base=+0.275)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.330 (n=381)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.291)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.297 (n=566)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.291)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.394 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `1450.7635` → IC=+0.306 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1450.7635 (IC base=+0.291)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.346 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.341)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.368 (n=74)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.341)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.384 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.341)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.344 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.341)

- **PATRÓN** `libro_liquidez` > `761.0655` → IC=+0.370 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 761.0655 (IC base=+0.341)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.442 (n=445)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.439 (n=439)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.439 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.436)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.437 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.436)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.438 (n=241)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.433)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.438 (n=240)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.436 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.433)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.433)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.452 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.452 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.442 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.441 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.441)

- **PATRÓN** `libro_liquidez` > `1988.111` → IC=+0.462 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1988.111 (IC base=+0.441)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.389 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.391)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.429 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.391)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `hora_utc` > `15.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=54)

- **FILTRO** `py_entrada` > `0.785` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.785
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=54)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.306 (n=214)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.258)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.386 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.275 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `2118.5268` → IC=+0.301 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2118.5268 (IC base=+0.258)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=54)

- **FILTRO** `py_entrada` > `0.785` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.785
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=54)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.306 (n=214)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.258)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.386 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.275 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `2118.5268` → IC=+0.301 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2118.5268 (IC base=+0.258)

### GBM_LATE_15M
- **PATRÓN** `drift_60min` |x|≤ `0.4868` → IC=+0.123 (n=8275)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.4868 (IC base=+0.106)

- **PATRÓN** `ibs_20min` > `0.9829` → IC=+0.244 (n=2758)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9829 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` > `0.8396` → IC=+0.251 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8396 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` < `0.6333` → IC=+0.250 (n=2352)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6333 (IC base=+0.106)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.339` → IC=+0.188 (n=2186)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 8.339 (IC base=+0.106)

- **PATRÓN** `volumen_regimen` < `1.2062` → IC=+0.248 (n=2254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2062 (IC base=+0.106)

- **PATRÓN** `volumen_regimen` > `1.0433` → IC=+0.262 (n=1022)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0433 (IC base=+0.106)

- **PATRÓN** `volumen_pendiente_norm` > `0.3029` → IC=+0.224 (n=830)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3029 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` > `1.4617` → IC=+0.203 (n=5690)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4617 (IC base=+0.106)

- **PATRÓN** `ibs_20min` < `0.5714` → IC=+0.133 (n=9997)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5714 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.6138` → IC=+0.203 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6138 (IC base=+0.066)

- **PATRÓN** `volumen_regimen` < `0.697` → IC=+0.185 (n=1545)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.697 (IC base=+0.066)

- **PATRÓN** `volumen_regimen` > `1.0501` → IC=+0.176 (n=1592)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.0501 (IC base=+0.066)

- **PATRÓN** `volumen_pendiente_norm` > `0.167` → IC=+0.226 (n=1678)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.167 (IC base=+0.066)

- **PATRÓN** `volumen_spike_ratio` > `1.5684` → IC=+0.199 (n=5294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5684 (IC base=+0.066)

- **PATRÓN** `ballena_activa_n` < `135.0` → IC=+0.210 (n=5722)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 135.0 (IC base=+0.066)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.176 (n=624)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.005 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.177 (n=623)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0082 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.3502` → IC=+0.166 (n=1862)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3502 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.170 (n=900)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.167 (n=1248)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 11.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.271 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.137` → IC=+0.265 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.137 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.2803` → IC=+0.212 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2803 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `1.4361` → IC=+0.165 (n=1743)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.4361 (IC base=+0.161)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.176 (n=1896)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.04 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.246 (n=1272)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.093` → IC=+0.273 (n=473)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.093 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.245 (n=975)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0549` → IC=+0.293 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0549 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.551` → IC=+0.238 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.551 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.468` → IC=+0.244 (n=1472)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.468 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.276` → IC=+0.260 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.276 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.429` → IC=+0.231 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.429 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.6113` → IC=+0.240 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6113 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=1563)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.234 (n=630)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.0853` → IC=+0.243 (n=477)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0853 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.234 (n=1431)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.217 (n=1453)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` > `0.9864` → IC=+0.270 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9864 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` < `0.5685` → IC=+0.222 (n=1501)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5685 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.688` → IC=+0.261 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.688 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` < `1.2518` → IC=+0.220 (n=1430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2518 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` > `0.8707` → IC=+0.226 (n=953)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8707 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.2768` → IC=+0.249 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2768 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.3728` → IC=+0.236 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3728 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `11188.0133` → IC=+0.227 (n=1430)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11188.0133 (IC base=+0.217)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.169 (n=995)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0039 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.0773` → IC=+0.168 (n=498)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0773 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=586)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.147 (n=664)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 7.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.6975` → IC=+0.173 (n=1492)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.6975 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.1345` → IC=+0.157 (n=1334)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1345 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.236` → IC=+0.161 (n=237)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.236 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.284` → IC=+0.145 (n=1359)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 4.284 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.1967` → IC=+0.152 (n=1492)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1967 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.1556` → IC=+0.179 (n=394)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1556 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.4238` → IC=+0.154 (n=1381)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4238 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.4185` → IC=+0.149 (n=1381)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.4185 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `14134.8887` → IC=+0.146 (n=994)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 14134.8887 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `234.0` → IC=+0.169 (n=572)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 234.0 (IC base=+0.141)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.206 (n=613)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=1936)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.190 (n=1645)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.264 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.199` → IC=+0.253 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.199 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` < `0.2091` → IC=+0.187 (n=1843)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.2091 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.3578` → IC=+0.198 (n=246)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.3578 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `2.819` → IC=+0.205 (n=794)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.819 (IC base=+0.185)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.192 (n=1303)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.185)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.220 (n=1397)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.6123` → IC=+0.210 (n=1586)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6123 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=602)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.216 (n=735)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` < `0.0645` → IC=+0.244 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0645 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.717` → IC=+0.234 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.717 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.3507` → IC=+0.274 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3507 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `1.7653` → IC=+0.201 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7653 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `2.19` → IC=+0.215 (n=971)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.19 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.215 (n=1065)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `1904.2932` → IC=+0.213 (n=719)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1904.2932 (IC base=+0.209)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.213 (n=929)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.209)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.144 (n=102)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=2267)

- **PATRÓN** `ibs_20min` > `0.9436` → IC=+0.211 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9436 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.7852` → IC=+0.336 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7852 (IC base=+0.026)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.739` → IC=+0.161 (n=729)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.739 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `0.8561` → IC=+0.328 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8561 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` > `1.2014` → IC=+0.344 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2014 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.1796` → IC=+0.321 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1796 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.3004` → IC=+0.351 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3004 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.4107` → IC=+0.347 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4107 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` > `2.1967` → IC=+0.327 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1967 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `160.0` → IC=+0.332 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 160.0 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.6765` → IC=+0.207 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6765 (IC base=+0.019)

- **PATRÓN** `volumen_regimen` < `0.8471` → IC=+0.166 (n=575)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8471 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` > `0.2269` → IC=+0.221 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2269 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` > `1.5219` → IC=+0.176 (n=723)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.5219 (IC base=+0.019)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.177 (n=60)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=335)

- **FILTRO** `ibs_20min` < `0.2821` → IC=-0.200 (n=98)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2821
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=297)

- **FILTRO** `ibs_20min` > `0.25` → IC=-0.125 (n=2237)

  - _Acción_: SKIP cuando `ibs_20min` > 0.25
  - _Potencial_: sin este filtro IC_bueno=+0.124 (n=1106)

- **FILTRO** `sigma_ewma_delta_pct` > `8.692` → IC=-0.208 (n=358)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.692
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2985)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.182 (n=199)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.6 (IC base=+0.047)

- **PATRÓN** `dist_vwap_pct` > `1.9169` → IC=+0.315 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.9169 (IC base=+0.047)

- **PATRÓN** `dist_vwap_pct` < `0.6236` → IC=+0.277 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6236 (IC base=+0.047)

- **PATRÓN** `volumen_regimen` > `0.7675` → IC=+0.305 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7675 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` < `0.0729` → IC=+0.307 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0729 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` < `1.7465` → IC=+0.305 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7465 (IC base=+0.047)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.298 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.047)

- **PATRÓN** `ibs_20min` < `0.25` → IC=+0.124 (n=1106)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.25 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.7235` → IC=+0.257 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7235 (IC base=-0.042)

- **PATRÓN** `volumen_regimen` < `1.0932` → IC=+0.230 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0932 (IC base=-0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.157` → IC=+0.261 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.157 (IC base=-0.042)

- **PATRÓN** `volumen_spike_ratio` < `2.4205` → IC=+0.270 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4205 (IC base=-0.042)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6568` → IC=-0.184 (n=583)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6568
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=1751)

- **FILTRO** `ibs_20min` < `0.7193` → IC=-0.152 (n=1540)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7193
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=794)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.198 (n=428)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=1906)

- **FILTRO** `ibs_20min` > `0.77` → IC=-0.202 (n=854)

  - _Acción_: SKIP cuando `ibs_20min` > 0.77
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=2570)

- **PATRÓN** `dist_vwap_pct` > `0.4581` → IC=+0.311 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4581 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` < `0.1924` → IC=+0.310 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1924 (IC base=-0.065)

- **PATRÓN** `volumen_regimen` > `0.616` → IC=+0.303 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.616 (IC base=-0.065)

- **PATRÓN** `volumen_pendiente_norm` < `0.1011` → IC=+0.293 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1011 (IC base=-0.065)

- **PATRÓN** `volumen_pendiente_norm` > `0.1669` → IC=+0.288 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1669 (IC base=-0.065)

- **PATRÓN** `volumen_spike_ratio` < `2.1203` → IC=+0.290 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1203 (IC base=-0.065)

- **PATRÓN** `volumen_spike_ratio` > `1.8015` → IC=+0.291 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8015 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` > `0.9063` → IC=+0.273 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9063 (IC base=-0.022)

- **PATRÓN** `volumen_regimen` < `0.7331` → IC=+0.249 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7331 (IC base=-0.022)

- **PATRÓN** `volumen_regimen` > `1.2596` → IC=+0.282 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2596 (IC base=-0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.1023` → IC=+0.276 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1023 (IC base=-0.022)

- **PATRÓN** `volumen_spike_ratio` < `2.141` → IC=+0.253 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.141 (IC base=-0.022)

- **PATRÓN** `volumen_spike_ratio` > `1.5235` → IC=+0.246 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5235 (IC base=-0.022)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.197 (n=3470)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0098 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.4762` → IC=+0.187 (n=9298)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4762 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.7682` → IC=+0.285 (n=1112)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7682 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.61` → IC=+0.157 (n=4884)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.61 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` > `0.6889` → IC=+0.250 (n=3316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6889 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.2939` → IC=+0.270 (n=880)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2939 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` < `1.4647` → IC=+0.237 (n=2009)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4647 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` > `2.6541` → IC=+0.244 (n=2008)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6541 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.267 (n=5537)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 96.0 (IC base=+0.097)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.159 (n=3447)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0092 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.5493` → IC=+0.154 (n=9095)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.5493 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.7279` → IC=+0.242 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7279 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.2548` → IC=+0.241 (n=2904)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2548 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.7079` → IC=+0.242 (n=1348)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7079 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.2033` → IC=+0.249 (n=1022)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2033 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2433` → IC=+0.304 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2433 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.5994` → IC=+0.259 (n=1785)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5994 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.2989` → IC=+0.259 (n=1839)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2989 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `84.0` → IC=+0.265 (n=3933)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 84.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2583` → IC=-0.145 (n=717)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2583
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=2152)

- **FILTRO** `sigma_ewma_delta_pct` > `4.548` → IC=-0.158 (n=545)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.548
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1839)

- **PATRÓN** `ibs_20min` > `0.8935` → IC=+0.266 (n=719)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8935 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.851` → IC=+0.206 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.851 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2222` → IC=+0.272 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2222 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.433` → IC=+0.170 (n=304)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.433 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` > `2.1445` → IC=+0.200 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1445 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.182 (n=413)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 14.0 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` < `0.1673` → IC=+0.458 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1673 (IC base=-0.015)

- **PATRÓN** `volumen_spike_ratio` < `1.9827` → IC=+0.455 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9827 (IC base=-0.015)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.472 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=-0.015)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8636` → IC=+0.159 (n=696)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.8636 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.3147` → IC=+0.175 (n=380)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.3147 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `0.6718` → IC=+0.169 (n=857)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 0.6718 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.2723` → IC=+0.232 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2723 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.4226` → IC=+0.195 (n=313)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4226 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` > `2.3807` → IC=+0.157 (n=313)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.3807 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `243.0` → IC=+0.195 (n=411)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 243.0 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.1112` → IC=+0.225 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1112 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` > `0.8501` → IC=+0.229 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8501 (IC base=+0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2706` → IC=+0.317 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2706 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` < `1.4389` → IC=+0.223 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4389 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` > `2.1553` → IC=+0.243 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1553 (IC base=+0.006)

- **PATRÓN** `ballena_activa_n` < `461.0` → IC=+0.223 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 461.0 (IC base=+0.006)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.288 (n=545)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.248 (n=1640)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.248 (n=1647)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=866)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.681` → IC=+0.281 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.681 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` < `0.1037` → IC=+0.258 (n=1387)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1037 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `3.4136` → IC=+0.263 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.4136 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.253 (n=1150)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `1803.7992` → IC=+0.248 (n=1090)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1803.7992 (IC base=+0.245)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.314 (n=595)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.280)

- **PATRÓN** `drift_60min` |x|≤ `0.1738` → IC=+0.286 (n=578)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1738 (IC base=+0.280)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.323 (n=445)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.280)

- **PATRÓN** `ibs_20min` < `0.0909` → IC=+0.288 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0909 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.812` → IC=+0.294 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.812 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.754` → IC=+0.280 (n=1407)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.754 (IC base=+0.280)

- **PATRÓN** `volumen_pendiente_norm` > `0.3395` → IC=+0.301 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3395 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` < `1.7408` → IC=+0.282 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7408 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` > `2.7161` → IC=+0.289 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7161 (IC base=+0.280)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.285 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `1894.4532` → IC=+0.292 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1894.4532 (IC base=+0.280)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.283 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 28.0 (IC base=+0.280)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.294` → IC=-0.182 (n=511)

  - _Acción_: SKIP cuando `ibs_20min` < 0.294
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=1533)

- **FILTRO** `ibs_20min` > `0.7744` → IC=-0.186 (n=612)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7744
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=1837)

- **PATRÓN** `ibs_20min` > `0.9124` → IC=+0.178 (n=511)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.9124 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` > `0.4461` → IC=+0.224 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4461 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` < `0.6941` → IC=+0.217 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6941 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` < `0.9869` → IC=+0.237 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9869 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` > `0.5902` → IC=+0.216 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5902 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.0801` → IC=+0.264 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0801 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` < `1.5078` → IC=+0.262 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5078 (IC base=+0.014)

- **PATRÓN** `ballena_activa_n` < `149.0` → IC=+0.246 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 149.0 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` > `0.1577` → IC=+0.213 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1577 (IC base=-0.005)

- **PATRÓN** `dist_vwap_pct` < `0.6852` → IC=+0.199 (n=509)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.6852 (IC base=-0.005)

- **PATRÓN** `volumen_regimen` < `1.1663` → IC=+0.209 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1663 (IC base=-0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.1651` → IC=+0.280 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1651 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.8269` → IC=+0.258 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8269 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.1389` → IC=+0.238 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1389 (IC base=-0.005)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.249 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 139.0 (IC base=-0.005)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7273` → IC=-0.194 (n=1097)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7273
  - _Potencial_: sin este filtro IC_bueno=+0.277 (n=1108)

- **FILTRO** `ibs_20min` > `0.6875` → IC=-0.235 (n=564)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6875
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=1710)

- **FILTRO** `sigma_ewma_delta_pct` > `4.723` → IC=-0.184 (n=495)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.723
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=1779)

- **PATRÓN** `ibs_20min` > `0.7273` → IC=+0.277 (n=1108)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7273 (IC base=+0.042)

- **PATRÓN** `dist_vwap_pct` > `0.2166` → IC=+0.313 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2166 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.646` → IC=+0.171 (n=348)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 9.646 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` < `0.8679` → IC=+0.303 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8679 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` > `0.7298` → IC=+0.295 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7298 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.292 (n=761)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.2243` → IC=+0.301 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2243 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` < `1.4185` → IC=+0.327 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4185 (IC base=+0.042)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.314 (n=691)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.042)

- **PATRÓN** `ibs_20min` < `0.1905` → IC=+0.191 (n=751)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.1905 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` > `0.7475` → IC=+0.203 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7475 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` < `0.22` → IC=+0.221 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.22 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` < `0.7101` → IC=+0.253 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7101 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` < `0.0972` → IC=+0.212 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0972 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.069` → IC=+0.214 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.069 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` < `2.46` → IC=+0.222 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.46 (IC base=+0.014)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.240 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 51.0 (IC base=+0.014)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0168` → IC=+0.316 (n=898)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0168 (IC base=+0.276)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.284 (n=1415)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.276)

- **PATRÓN** `ibs_20min` > `0.74` → IC=+0.321 (n=1205)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.74 (IC base=+0.276)

- **PATRÓN** `dist_vwap_pct` > `0.2118` → IC=+0.315 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2118 (IC base=+0.276)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.606` → IC=+0.300 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.606 (IC base=+0.276)

- **PATRÓN** `volumen_regimen` > `0.6223` → IC=+0.289 (n=1347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6223 (IC base=+0.276)

- **PATRÓN** `volumen_pendiente_norm` > `0.2809` → IC=+0.328 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2809 (IC base=+0.276)

- **PATRÓN** `volumen_spike_ratio` > `2.1479` → IC=+0.297 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1479 (IC base=+0.276)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.282 (n=1443)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.276)

- **PATRÓN** `libro_liquidez` > `2638.7996` → IC=+0.292 (n=898)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2638.7996 (IC base=+0.276)

- **PATRÓN** `sigma_h` > `0.0154` → IC=+0.301 (n=966)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0154 (IC base=+0.273)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.285 (n=501)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.273)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.277 (n=715)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.273)

- **PATRÓN** `ibs_20min` < `0.3913` → IC=+0.306 (n=1449)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3913 (IC base=+0.273)

- **PATRÓN** `dist_vwap_pct` > `1.3638` → IC=+0.283 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.3638 (IC base=+0.273)

- **PATRÓN** `dist_vwap_pct` < `0.2281` → IC=+0.274 (n=1311)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2281 (IC base=+0.273)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.469` → IC=+0.289 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.469 (IC base=+0.273)

- **PATRÓN** `volumen_regimen` < `0.6384` → IC=+0.279 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6384 (IC base=+0.273)

- **PATRÓN** `volumen_regimen` > `1.2434` → IC=+0.308 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2434 (IC base=+0.273)

- **PATRÓN** `volumen_pendiente_norm` > `0.2372` → IC=+0.335 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2372 (IC base=+0.273)

- **PATRÓN** `volumen_spike_ratio` < `1.4247` → IC=+0.279 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4247 (IC base=+0.273)

- **PATRÓN** `volumen_spike_ratio` > `2.1415` → IC=+0.274 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1415 (IC base=+0.273)

- **PATRÓN** `libro_liquidez` > `2631.9668` → IC=+0.278 (n=966)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2631.9668 (IC base=+0.273)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.170 (n=2700)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0049 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.199 (n=2692)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0113 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.0905` → IC=+0.186 (n=2692)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.0905 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=8427)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.5745` → IC=+0.218 (n=8075)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5745 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.1784` → IC=+0.193 (n=3523)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1784 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.333` → IC=+0.256 (n=1649)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.333 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `1.2102` → IC=+0.159 (n=5350)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2102 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `0.6298` → IC=+0.160 (n=5349)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6298 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.2434` → IC=+0.194 (n=1629)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2434 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.5587` → IC=+0.167 (n=3410)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.5587 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `2.6136` → IC=+0.175 (n=2583)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.6136 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `2409.4285` → IC=+0.168 (n=5383)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2409.4285 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `114.0` → IC=+0.180 (n=6989)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 114.0 (IC base=+0.167)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.182 (n=5142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0066 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.0815` → IC=+0.208 (n=2571)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0815 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=2985)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` < `0.4806` → IC=+0.225 (n=7711)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4806 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.9233` → IC=+0.146 (n=760)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.9233 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` < `0.2362` → IC=+0.158 (n=5590)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.2362 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.336` → IC=+0.193 (n=1302)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 10.336 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `1.1727` → IC=+0.151 (n=5581)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1727 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.2904` → IC=+0.216 (n=1110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2904 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.5578` → IC=+0.164 (n=3091)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.5578 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `2.2458` → IC=+0.169 (n=3185)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.2458 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.172 (n=6674)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 115.0 (IC base=+0.167)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.210 (n=457)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.183)

- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.190 (n=621)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0075 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.3424` → IC=+0.206 (n=1370)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3424 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=499)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.192 (n=917)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.225` → IC=+0.328 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.225 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.23` → IC=+0.237 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.23 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `1.4343` → IC=+0.182 (n=1269)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.4343 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.197 (n=1396)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.238 (n=887)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.247 (n=904)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.1884` → IC=+0.288 (n=672)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1884 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.242 (n=913)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.251 (n=491)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.3443` → IC=+0.263 (n=1007)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3443 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.34` → IC=+0.249 (n=1090)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.34 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.1603` → IC=+0.233 (n=950)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1603 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.252 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.4206` → IC=+0.266 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4206 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1813.3286` → IC=+0.241 (n=671)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1813.3286 (IC base=+0.237)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.234 (n=401)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.0736` → IC=+0.195 (n=401)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.0736 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.191 (n=1080)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 8.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `0.4039` → IC=+0.227 (n=1201)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4039 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.2134` → IC=+0.213 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2134 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.479` → IC=+0.237 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.479 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `0.688` → IC=+0.167 (n=529)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.688 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` > `0.8738` → IC=+0.168 (n=801)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 0.8738 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.211 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `1.503` → IC=+0.178 (n=514)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.503 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `2.4558` → IC=+0.160 (n=389)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.4558 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `11900.8434` → IC=+0.169 (n=1073)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 11900.8434 (IC base=+0.161)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.158 (n=1306)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0057 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0594` → IC=+0.205 (n=436)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0594 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.179 (n=437)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 18.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.5665` → IC=+0.187 (n=1306)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.5665 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1357` → IC=+0.160 (n=1297)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1357 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.882` → IC=+0.202 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.882 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.204` → IC=+0.159 (n=1306)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.204 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.1543` → IC=+0.156 (n=399)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.1543 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.442` → IC=+0.146 (n=1194)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.442 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.4211` → IC=+0.136 (n=1194)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4211 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `214.0` → IC=+0.168 (n=375)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 214.0 (IC base=+0.137)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.216 (n=615)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.236` → IC=+0.218 (n=905)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.236 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=1408)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.293 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.422` → IC=+0.275 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.422 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.2066` → IC=+0.202 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2066 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` < `1.6272` → IC=+0.200 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6272 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `2.8331` → IC=+0.214 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8331 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.206 (n=953)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.198)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.234 (n=990)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0102 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.247` → IC=+0.237 (n=750)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.247 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.272 (n=392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` < `0.3478` → IC=+0.247 (n=1124)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3478 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.729` → IC=+0.260 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.729 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.3529` → IC=+0.265 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3529 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `1.766` → IC=+0.210 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.766 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `2.2024` → IC=+0.229 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2024 (IC base=+0.216)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.207 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.216)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.174 (n=1136)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0067 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.4335` → IC=+0.157 (n=1290)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4335 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=1355)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` > `0.3743` → IC=+0.196 (n=1290)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.3743 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.1599` → IC=+0.178 (n=855)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1599 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.979` → IC=+0.228 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.979 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.0379` → IC=+0.145 (n=1135)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.0379 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `0.6214` → IC=+0.147 (n=1290)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.6214 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.2913` → IC=+0.198 (n=203)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2913 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `1.4266` → IC=+0.152 (n=421)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4266 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `2.5051` → IC=+0.167 (n=421)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.5051 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `6113.3127` → IC=+0.182 (n=860)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 6113.3127 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.147 (n=1227)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 162.0 (IC base=+0.142)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.154 (n=1355)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0072 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.3848` → IC=+0.143 (n=1355)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3848 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.180 (n=529)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.644` → IC=+0.171 (n=1355)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.644 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` < `0.368` → IC=+0.135 (n=1465)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.368 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.961` → IC=+0.165 (n=478)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 6.961 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.8475` → IC=+0.149 (n=904)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8475 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2909` → IC=+0.188 (n=197)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2909 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.7906` → IC=+0.137 (n=822)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.7906 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `10007.3401` → IC=+0.158 (n=615)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 10007.3401 (IC base=+0.122)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.152 (n=664)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0102 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=1499)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.5152` → IC=+0.204 (n=1462)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5152 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `0.5228` → IC=+0.197 (n=634)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.5228 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.733` → IC=+0.258 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.733 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.2155` → IC=+0.131 (n=1462)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.2155 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.124 (n=613)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.5431` → IC=+0.139 (n=622)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.5431 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.126 (n=1527)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2898.7698` → IC=+0.193 (n=663)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2898.7698 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.134 (n=1135)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 50.0 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.156 (n=652)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0062 (IC base=+0.112)

- **PATRÓN** `drift_60min` |x|≤ `0.1048` → IC=+0.162 (n=495)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1048 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.130 (n=1503)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.112)

- **PATRÓN** `ibs_20min` < `0.5686` → IC=+0.210 (n=1480)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5686 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` > `1.0242` → IC=+0.136 (n=212)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 1.0242 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` < `0.2064` → IC=+0.136 (n=1353)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.2064 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.319` → IC=+0.128 (n=449)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 5.319 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` < `0.6379` → IC=+0.143 (n=494)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6379 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` > `0.2732` → IC=+0.156 (n=181)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.2732 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` < `1.4527` → IC=+0.128 (n=444)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.4527 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `2760.8425` → IC=+0.157 (n=671)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2760.8425 (IC base=+0.112)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0189` → IC=+0.213 (n=932)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0189 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.1343` → IC=+0.203 (n=466)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1343 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=1453)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.204 (n=634)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.7391` → IC=+0.256 (n=1249)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7391 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `0.5174` → IC=+0.219 (n=667)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5174 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.576` → IC=+0.239 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.576 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `1.2075` → IC=+0.204 (n=1398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2075 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `0.624` → IC=+0.211 (n=1398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.624 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2323` → IC=+0.268 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2323 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.1464` → IC=+0.209 (n=1189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1464 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.4081` → IC=+0.209 (n=1350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4081 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.204 (n=1487)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `2834.6035` → IC=+0.206 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2834.6035 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.0116` → IC=+0.228 (n=634)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0116 (IC base=+0.203)

- **PATRÓN** `sigma_h` > `0.0224` → IC=+0.206 (n=654)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0224 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.0902` → IC=+0.221 (n=481)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0902 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.221 (n=710)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.211 (n=656)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` < `0.438` → IC=+0.244 (n=1441)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.438 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `1.2417` → IC=+0.225 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2417 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.42` → IC=+0.234 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.42 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.6295` → IC=+0.214 (n=1441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6295 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2813` → IC=+0.286 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2813 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `2.1933` → IC=+0.193 (n=1142)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.1933 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.434` → IC=+0.198 (n=1298)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.434 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2604.9815` → IC=+0.210 (n=961)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2604.9815 (IC base=+0.203)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.167 (n=652)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0039 (IC base=+0.148)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.175 (n=654)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0089 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.1009` → IC=+0.157 (n=651)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1009 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.186 (n=980)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 15.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.5385` → IC=+0.188 (n=1746)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.5385 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.8823` → IC=+0.180 (n=320)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.8823 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.707` → IC=+0.175 (n=881)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 3.707 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.8725` → IC=+0.166 (n=1146)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8725 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` > `0.623` → IC=+0.151 (n=1719)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.623 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1641` → IC=+0.177 (n=537)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1641 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `1.4417` → IC=+0.164 (n=628)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4417 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `2.2086` → IC=+0.155 (n=854)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.2086 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.153 (n=2216)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.02 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `12451.6308` → IC=+0.160 (n=651)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 12451.6308 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `155.0` → IC=+0.168 (n=1730)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 155.0 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.136 (n=1352)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0057 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.123 (n=2046)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 5.0 (IC base=+0.110)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.137 (n=2027)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.6667 (IC base=+0.110)

- **PATRÓN** `dist_vwap_pct` < `0.2153` → IC=+0.121 (n=1798)

  - _Acción_: Kelly boost +0.60€ cuando `dist_vwap_pct` < 0.2153 (IC base=+0.110)

- **PATRÓN** `volumen_regimen` < `0.6989` → IC=+0.128 (n=802)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.6989 (IC base=+0.110)

- **PATRÓN** `volumen_pendiente_norm` > `0.1654` → IC=+0.129 (n=502)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.1654 (IC base=+0.110)

- **PATRÓN** `volumen_spike_ratio` < `1.4517` → IC=+0.143 (n=650)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4517 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `2761.0477` → IC=+0.122 (n=1807)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2761.0477 (IC base=+0.110)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.122 (n=823)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 29.0 (IC base=+0.110)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3457` → IC=+0.123 (n=484)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.3457 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.151 (n=454)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 8.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.2517` → IC=+0.147 (n=483)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.2517 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.3081` → IC=+0.157 (n=170)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.3081 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` < `0.6182` → IC=+0.152 (n=162)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6182 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `15011.8449` → IC=+0.142 (n=322)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 15011.8449 (IC base=+0.105)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.216 (n=216)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.3402` → IC=+0.159 (n=640)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.3402 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.146 (n=575)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.137 (n=444)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 11.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.6045` → IC=+0.187 (n=563)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6045 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.4828` → IC=+0.151 (n=735)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.4828 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.406` → IC=+0.157 (n=249)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 4.406 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.218` → IC=+0.142 (n=640)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.218 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `1.0609` → IC=+0.168 (n=290)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 1.0609 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.1571` → IC=+0.195 (n=172)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1571 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.1046` → IC=+0.155 (n=554)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.1046 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.4187` → IC=+0.150 (n=630)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.4187 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `325.0` → IC=+0.157 (n=534)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 325.0 (IC base=+0.137)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.260 (n=269)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.195)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.202 (n=203)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.0967` → IC=+0.218 (n=204)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0967 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=637)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `0.6969` → IC=+0.243 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6969 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` > `0.1582` → IC=+0.211 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1582 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` < `0.2301` → IC=+0.197 (n=536)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.2301 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.93` → IC=+0.226 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.93 (IC base=+0.195)

- **PATRÓN** `volumen_regimen` < `0.8363` → IC=+0.199 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8363 (IC base=+0.195)

- **PATRÓN** `volumen_regimen` > `1.1584` → IC=+0.217 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1584 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.2613` → IC=+0.278 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2613 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` < `1.3995` → IC=+0.219 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3995 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `1.7519` → IC=+0.222 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7519 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `12476.0568` → IC=+0.222 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12476.0568 (IC base=+0.195)

- **PATRÓN** `ibs_20min` < `0.084` → IC=+0.156 (n=193)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.084 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` < `0.6858` → IC=+0.137 (n=254)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.6858 (IC base=+0.093)

- **PATRÓN** `volumen_pendiente_norm` > `0.1664` → IC=+0.135 (n=135)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.1664 (IC base=+0.093)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `dist_vwap_pct` > `0.3429` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3429
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=500)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.158 (n=299)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0073 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.1188` → IC=+0.145 (n=150)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.1188 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.166 (n=423)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 8.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` > `0.8906` → IC=+0.241 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8906 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` > `1.0116` → IC=+0.230 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0116 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.239` → IC=+0.202 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.239 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `1.0699` → IC=+0.150 (n=395)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.0699 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.1823` → IC=+0.177 (n=128)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1823 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `2.2017` → IC=+0.175 (n=195)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.2017 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.135 (n=489)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.02 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `2920.0962` → IC=+0.189 (n=204)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2920.0962 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.5192` → IC=+0.148 (n=402)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.5192 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` < `0.7082` → IC=+0.137 (n=177)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.7082 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` < `1.8403` → IC=+0.156 (n=251)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.8403 (IC base=+0.077)

- **PATRÓN** `libro_liquidez` > `2554.7355` → IC=+0.122 (n=268)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2554.7355 (IC base=+0.077)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.128 (n=345)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 42.0 (IC base=+0.077)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0232` → IC=+0.161 (n=178)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0232 (IC base=+0.148)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.183 (n=178)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0068 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.2324` → IC=+0.178 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2324 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.167 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 16.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.220 (n=80)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.4` → IC=+0.191 (n=179)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.4 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.2434` → IC=+0.153 (n=93)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.2434 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `1.0655` → IC=+0.160 (n=201)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 1.0655 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.317` → IC=+0.177 (n=153)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 3.317 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.0007` → IC=+0.148 (n=157)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.0007 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` > `0.6087` → IC=+0.167 (n=178)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6087 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` < `0.2548` → IC=+0.174 (n=173)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` < 0.2548 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.222 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.176 (n=180)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.02 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `2497.2192` → IC=+0.161 (n=119)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2497.2192 (IC base=+0.148)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.152 (n=202)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0091 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.139 (n=203)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.6 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `1.1734` → IC=+0.300 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1734 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.53` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.53 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.0734` → IC=+0.122 (n=178)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.0734 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` > `0.6515` → IC=+0.132 (n=202)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 0.6515 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1181` → IC=+0.126 (n=180)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1181 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.5435` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.5435 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `2.8185` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.8185 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.142 (n=163)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 17.0 (IC base=+0.120)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.204 (n=3448)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.180 (n=10815)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.469` → IC=+0.216 (n=10342)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.469 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.9775` → IC=+0.201 (n=1477)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9775 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.857` → IC=+0.234 (n=3799)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.857 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `0.88` → IC=+0.165 (n=4617)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.88 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.2885` → IC=+0.201 (n=1424)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2885 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.5923` → IC=+0.186 (n=3317)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.5923 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `1793.6488` → IC=+0.171 (n=10341)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 1793.6488 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.195 (n=7909)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 86.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.192 (n=6253)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.007 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.1495` → IC=+0.189 (n=4126)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.1495 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=3563)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.182 (n=4320)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 7.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.5682` → IC=+0.236 (n=9375)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5682 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` < `0.2527` → IC=+0.161 (n=5806)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2527 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.031` → IC=+0.200 (n=1309)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.031 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.732` → IC=+0.182 (n=9064)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.732 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.6327` → IC=+0.163 (n=2144)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.6327 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` > `1.2018` → IC=+0.155 (n=2144)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.2018 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2874` → IC=+0.239 (n=1233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2874 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.613` → IC=+0.191 (n=2875)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.613 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.193 (n=5583)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 48.0 (IC base=+0.181)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.205 (n=582)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.225 (n=584)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.356` → IC=+0.191 (n=1746)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.356 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.203 (n=839)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.195 (n=1178)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.326 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.564` → IC=+0.342 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.564 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.2269` → IC=+0.248 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2269 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.2399` → IC=+0.196 (n=748)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.2399 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.210 (n=1763)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.256 (n=1381)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.257)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.261 (n=1380)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0045 (IC base=+0.257)

- **PATRÓN** `drift_60min` |x|≤ `0.1282` → IC=+0.280 (n=607)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1282 (IC base=+0.257)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.265 (n=1254)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.257)

- **PATRÓN** `ibs_20min` < `0.3517` → IC=+0.285 (n=1215)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3517 (IC base=+0.257)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.721` → IC=+0.260 (n=1550)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.721 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.279 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` < `1.5484` → IC=+0.254 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5484 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` > `2.6332` → IC=+0.274 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6332 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.258 (n=1522)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1809.64` → IC=+0.259 (n=919)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1809.64 (IC base=+0.257)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.192 (n=554)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0028 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.0848` → IC=+0.160 (n=554)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.0848 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=1739)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.3085` → IC=+0.203 (n=1659)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3085 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1352` → IC=+0.184 (n=931)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1352 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.699` → IC=+0.168 (n=378)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.699 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.21` → IC=+0.154 (n=1499)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.21 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.6273` → IC=+0.178 (n=554)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.6273 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2656` → IC=+0.202 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2656 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1133` → IC=+0.159 (n=1412)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1133 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.7535` → IC=+0.158 (n=1070)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.7535 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `11354.7125` → IC=+0.163 (n=1483)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 11354.7125 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `471.0` → IC=+0.158 (n=1535)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 471.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.166 (n=1438)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0058 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.0803` → IC=+0.187 (n=480)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.0803 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=564)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.157 (n=645)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.6597` → IC=+0.197 (n=1438)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.6597 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.688` → IC=+0.155 (n=233)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.688 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.1372` → IC=+0.167 (n=1303)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1372 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.446` → IC=+0.158 (n=241)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 11.446 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.511` → IC=+0.155 (n=1457)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 6.511 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `1.1856` → IC=+0.165 (n=1438)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1856 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.1508` → IC=+0.198 (n=385)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1508 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.4003` → IC=+0.162 (n=1340)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.4003 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.7535` → IC=+0.165 (n=893)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.7535 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `354.0` → IC=+0.162 (n=829)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 354.0 (IC base=+0.153)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.247 (n=559)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.225 (n=1760)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.223 (n=1699)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.293` → IC=+0.298 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.293 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` < `0.2104` → IC=+0.221 (n=1664)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2104 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.8213` → IC=+0.241 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8213 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.227 (n=1186)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.236 (n=1568)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0118 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.1693` → IC=+0.237 (n=690)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1693 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.256 (n=596)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.229)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.238 (n=732)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` < `0.0159` → IC=+0.308 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0159 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.751` → IC=+0.272 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.751 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.3433` → IC=+0.303 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3433 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` < `1.7518` → IC=+0.226 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7518 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `2.1837` → IC=+0.232 (n=961)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1837 (IC base=+0.229)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.238 (n=1052)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.229)

- **PATRÓN** `libro_liquidez` > `1902.41` → IC=+0.232 (n=710)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1902.41 (IC base=+0.229)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.227 (n=1375)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.229)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.178 (n=778)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0041 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4384` → IC=+0.145 (n=1762)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.4384 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=1845)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.8757` → IC=+0.260 (n=799)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8757 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.3708` → IC=+0.164 (n=697)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.3708 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.174` → IC=+0.159 (n=728)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 4.174 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.873` → IC=+0.155 (n=1175)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.873 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.220 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.5208` → IC=+0.151 (n=751)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.5208 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `2.1374` → IC=+0.149 (n=774)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.1374 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `8015.433` → IC=+0.234 (n=799)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8015.433 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.156 (n=547)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 78.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.161 (n=1262)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0066 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4469` → IC=+0.151 (n=1434)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.4469 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=537)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.140 (n=654)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 7.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.1434` → IC=+0.255 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1434 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.5967` → IC=+0.139 (n=1586)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.5967 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.14` → IC=+0.178 (n=212)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 11.14 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.145 (n=956)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.8616 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.1867` → IC=+0.142 (n=478)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.1867 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2886` → IC=+0.236 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2886 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.4415` → IC=+0.149 (n=1361)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.4415 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `7258.1556` → IC=+0.196 (n=650)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 7258.1556 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `177.0` → IC=+0.142 (n=1358)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 177.0 (IC base=+0.136)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.141 (n=1168)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.0082 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.132 (n=1806)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.192 (n=1753)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.4706 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` > `1.1033` → IC=+0.194 (n=370)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 1.1033 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.503` → IC=+0.237 (n=657)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.503 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `0.8929` → IC=+0.136 (n=1168)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8929 (IC base=+0.114)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.127 (n=1763)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `2897.8254` → IC=+0.249 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2897.8254 (IC base=+0.114)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.132 (n=1359)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 54.0 (IC base=+0.114)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.175 (n=565)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0058 (IC base=+0.113)

- **PATRÓN** `drift_60min` |x|≤ `0.1332` → IC=+0.163 (n=565)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1332 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.124 (n=1755)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 5.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.204 (n=1695)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.2218` → IC=+0.132 (n=1375)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.2218 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.486` → IC=+0.127 (n=1637)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 3.486 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `0.6498` → IC=+0.156 (n=565)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6498 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.2212` → IC=+0.164 (n=266)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.2212 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.442` → IC=+0.139 (n=511)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.442 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `2824.0599` → IC=+0.168 (n=565)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2824.0599 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.123 (n=1323)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 51.0 (IC base=+0.113)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0193` → IC=+0.217 (n=1166)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0193 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.214 (n=1826)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.209 (n=1562)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.5116` → IC=+0.248 (n=1749)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5116 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.208` → IC=+0.233 (n=1031)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.208 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.188` → IC=+0.271 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.188 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` < `1.2447` → IC=+0.210 (n=1749)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2447 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `0.6389` → IC=+0.216 (n=1749)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6389 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.2335` → IC=+0.248 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2335 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.5002` → IC=+0.236 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5002 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.217 (n=1838)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2635.0196` → IC=+0.219 (n=1166)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2635.0196 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.225 (n=623)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0092 (IC base=+0.201)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.222 (n=623)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.209 (n=1319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` < `0.4231` → IC=+0.265 (n=1643)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4231 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `1.2595` → IC=+0.205 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2595 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` < `0.9244` → IC=+0.203 (n=2072)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9244 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.822` → IC=+0.252 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.822 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `1.2347` → IC=+0.237 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2347 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.282` → IC=+0.268 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.282 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `2.1818` → IC=+0.197 (n=1480)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.1818 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `1.4297` → IC=+0.197 (n=1681)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4297 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=1102)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=3151)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.167 (n=2661)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0092 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.5194` → IC=+0.166 (n=3022)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.5194 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=1201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.157)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.169 (n=1345)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 6.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `0.9414` → IC=+0.214 (n=1008)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9414 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.1894` → IC=+0.171 (n=1122)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1894 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` < `0.4847` → IC=+0.153 (n=1885)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.4847 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.192` → IC=+0.191 (n=497)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 10.192 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` > `0.8944` → IC=+0.166 (n=1342)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.8944 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.1706` → IC=+0.192 (n=830)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1706 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `1.4563` → IC=+0.165 (n=996)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.4563 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `1.8746` → IC=+0.166 (n=1991)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.8746 (IC base=+0.157)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.159 (n=2144)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `8307.441` → IC=+0.165 (n=1370)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 8307.441 (IC base=+0.157)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.201 (n=793)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.4871` → IC=+0.161 (n=2375)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4871 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=868)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.164 (n=795)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 4.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.1809` → IC=+0.174 (n=1045)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.1809 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.6795` → IC=+0.169 (n=460)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.6795 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.241` → IC=+0.155 (n=2366)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 6.241 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.0974` → IC=+0.153 (n=2000)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.0974 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` < `0.0966` → IC=+0.147 (n=2154)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.0966 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.0723` → IC=+0.145 (n=1094)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.0723 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `1.4242` → IC=+0.157 (n=782)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.4242 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.8137` → IC=+0.146 (n=1563)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.8137 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=3151)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `7268.8224` → IC=+0.156 (n=2122)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 7268.8224 (IC base=+0.143)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.187 (n=356)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0056 (IC base=+0.170)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.175 (n=361)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0034 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.0894` → IC=+0.201 (n=135)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0894 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.177 (n=404)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.181 (n=180)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 8.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` < `0.5463` → IC=+0.195 (n=270)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.5463 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` > `0.2159` → IC=+0.177 (n=190)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.2159 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` < `0.1537` → IC=+0.172 (n=327)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1537 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.174` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.174 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.415` → IC=+0.178 (n=426)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 2.415 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `1.2271` → IC=+0.180 (n=404)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 1.2271 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` > `0.8476` → IC=+0.201 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8476 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.3035` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3035 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `1.4485` → IC=+0.201 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4485 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `2.6405` → IC=+0.208 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6405 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `12584.8678` → IC=+0.219 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12584.8678 (IC base=+0.170)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.217 (n=422)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.085` → IC=+0.179 (n=319)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.085 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.179 (n=366)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.175 (n=364)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.1385` → IC=+0.178 (n=420)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.1385 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.6078` → IC=+0.148 (n=433)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.6078 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.6955` → IC=+0.174 (n=90)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.6955 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.2218` → IC=+0.139 (n=969)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.2218 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.369` → IC=+0.162 (n=932)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 6.369 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8795` → IC=+0.187 (n=637)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8795 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.0682` → IC=+0.165 (n=446)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0682 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.42` → IC=+0.146 (n=317)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.42 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.8205` → IC=+0.149 (n=634)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.8205 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `11474.1256` → IC=+0.153 (n=954)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 11474.1256 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `706.0` → IC=+0.144 (n=908)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 706.0 (IC base=+0.139)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.186 (n=208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.006 (IC base=+0.165)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.181 (n=283)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0099 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.5715` → IC=+0.174 (n=623)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.5715 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.222 (n=232)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.994` → IC=+0.233 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.994 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.706` → IC=+0.225 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.706 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` < `0.3499` → IC=+0.170 (n=749)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.3499 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.2084` → IC=+0.204 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2084 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `3.3904` → IC=+0.167 (n=622)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 3.3904 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `2.2621` → IC=+0.171 (n=414)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.2621 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `2425.929` → IC=+0.198 (n=283)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2425.929 (IC base=+0.165)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.312 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.254)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.262 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.254)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.262 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.254)

- **PATRÓN** `ibs_20min` > `0.4722` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4722 (IC base=+0.254)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.213` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.213 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` < `0.1317` → IC=+0.273 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1317 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` > `0.1037` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1037 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` < `2.5115` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5115 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` > `3.6446` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6446 (IC base=+0.254)

- **PATRÓN** `libro_liquidez` > `2362.106` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2362.106 (IC base=+0.254)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.256 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.254)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.167 (n=880)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0073 (IC base=+0.163)

- **PATRÓN** `sigma_h` > `0.0043` → IC=+0.171 (n=1000)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0043 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.3872` → IC=+0.167 (n=880)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3872 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.180 (n=385)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.170 (n=337)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 4.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` < `0.5403` → IC=+0.174 (n=667)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.5403 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.886` → IC=+0.172 (n=333)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.886 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.1633` → IC=+0.164 (n=569)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1633 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` < `0.4234` → IC=+0.172 (n=933)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.4234 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.148` → IC=+0.175 (n=897)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` < 4.148 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `1.082` → IC=+0.163 (n=880)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.082 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` > `0.6398` → IC=+0.166 (n=999)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6398 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.0778` → IC=+0.174 (n=433)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.0778 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.4349` → IC=+0.175 (n=327)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.4349 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `1.5228` → IC=+0.165 (n=876)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.5228 (IC base=+0.163)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.169 (n=998)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.163)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.189 (n=278)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0041 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.3902` → IC=+0.182 (n=730)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.3902 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=289)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.156 (n=583)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 11.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.7466` → IC=+0.155 (n=831)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.7466 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.0983` → IC=+0.160 (n=830)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.0983 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.6132` → IC=+0.180 (n=179)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.6132 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.639` → IC=+0.160 (n=853)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 6.639 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.6452` → IC=+0.188 (n=277)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.6452 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` > `0.7214` → IC=+0.155 (n=742)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.7214 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` < `0.1511` → IC=+0.155 (n=860)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.1511 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.167 (n=349)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.1956` → IC=+0.166 (n=716)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.1956 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.7791` → IC=+0.154 (n=542)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.7791 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `7566.251` → IC=+0.175 (n=830)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 7566.251 (IC base=+0.152)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `ibs_20min` > `0.9583` → IC=+0.234 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9583 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.2115` → IC=+0.150 (n=175)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.2115 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.177` → IC=+0.198 (n=51)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 9.177 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` > `0.1605` → IC=+0.214 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1605 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` > `1.4296` → IC=+0.135 (n=236)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.4296 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `3433.7126` → IC=+0.150 (n=218)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3433.7126 (IC base=+0.105)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.127 (n=199)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 59.0 (IC base=+0.105)

- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.217 (n=104)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.3998` → IC=+0.162 (n=152)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.3998 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.124 (n=115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 14.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.141 (n=165)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 11.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.1508` → IC=+0.218 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1508 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.6223` → IC=+0.219 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6223 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.617` → IC=+0.135 (n=124)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 2.617 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `1.1643` → IC=+0.134 (n=200)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.1643 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` < `0.1131` → IC=+0.186 (n=183)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.1131 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.611` → IC=+0.140 (n=98)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.611 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `3291.3893` → IC=+0.157 (n=228)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 3291.3893 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.163 (n=191)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 49.0 (IC base=+0.123)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.209 (n=125)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=377)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.175 (n=118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=384)

- **FILTRO** `dist_vwap_pct` > `0.1871` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1871
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=335)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.187 (n=420)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0041 (IC base=+0.092)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.124 (n=879)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 8.0 (IC base=+0.092)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.197 (n=771)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.6667 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` > `0.1562` → IC=+0.157 (n=464)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1562 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.443` → IC=+0.191 (n=202)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 11.443 (IC base=+0.092)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.198 (n=114)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.092)

- **PATRÓN** `volumen_spike_ratio` < `2.0892` → IC=+0.129 (n=656)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 2.0892 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `2432.8034` → IC=+0.138 (n=379)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2432.8034 (IC base=+0.092)

- **PATRÓN** `ibs_20min` < `0.2737` → IC=+0.219 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2737 (IC base=+0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.192 (n=102)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` < `2.1644` → IC=+0.126 (n=212)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 2.1644 (IC base=+0.004)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.158 (n=325)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.006 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.121 (n=338)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 6.0 (IC base=+0.102)

- **PATRÓN** `ibs_20min` > `0.4919` → IC=+0.179 (n=294)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.4919 (IC base=+0.102)

- **PATRÓN** `dist_vwap_pct` > `0.14` → IC=+0.171 (n=153)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.14 (IC base=+0.102)

- **PATRÓN** `volumen_regimen` < `1.067` → IC=+0.124 (n=259)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 1.067 (IC base=+0.102)

- **PATRÓN** `volumen_pendiente_norm` < `0.1568` → IC=+0.130 (n=271)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1568 (IC base=+0.102)

- **PATRÓN** `volumen_spike_ratio` < `2.0118` → IC=+0.164 (n=224)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.0118 (IC base=+0.102)

- **PATRÓN** `ibs_20min` < `0.3241` → IC=+0.239 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3241 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.71` → IC=+0.141 (n=115)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.71 (IC base=+0.052)

- **PATRÓN** `volumen_regimen` < `0.6103` → IC=+0.138 (n=45)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.6103 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` > `0.0712` → IC=+0.220 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0712 (IC base=+0.052)

- **PATRÓN** `volumen_spike_ratio` < `2.3987` → IC=+0.158 (n=112)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.3987 (IC base=+0.052)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.006` → IC=-0.225 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=117)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=120)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.156 (n=216)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0051 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.134 (n=304)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 7.0 (IC base=+0.104)

- **PATRÓN** `ibs_20min` > `0.6741` → IC=+0.230 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6741 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` > `0.3437` → IC=+0.181 (n=117)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.3437 (IC base=+0.104)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.742` → IC=+0.312 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.742 (IC base=+0.104)

- **PATRÓN** `volumen_pendiente_norm` > `0.2716` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2716 (IC base=+0.104)

- **PATRÓN** `volumen_spike_ratio` < `1.7335` → IC=+0.173 (n=160)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.7335 (IC base=+0.104)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=196)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `1135.4629` → IC=+0.152 (n=257)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1135.4629 (IC base=+0.104)

- **PATRÓN** `ibs_20min` < `0.1674` → IC=+0.273 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1674 (IC base=-0.022)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.956` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.956 (IC base=-0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.1353` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1353 (IC base=-0.022)

- **PATRÓN** `volumen_spike_ratio` > `2.268` → IC=+0.184 (n=36)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.268 (IC base=-0.022)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.135 (n=83)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.02 (IC base=-0.022)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0105` → IC=-0.271 (n=46)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=91)

- **FILTRO** `ibs_20min` > `0.2222` → IC=-0.294 (n=32)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2222
  - _Potencial_: sin este filtro IC_bueno=+0.197 (n=64)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.165 (n=246)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.6667 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.2077` → IC=+0.135 (n=154)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.2077 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.497` → IC=+0.155 (n=111)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 5.497 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` > `1.0632` → IC=+0.170 (n=92)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.0632 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.2408` → IC=+0.185 (n=52)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2408 (IC base=+0.068)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.167 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0057 (IC base=-0.040)

- **PATRÓN** `ibs_20min` < `0.2222` → IC=+0.197 (n=64)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.2222 (IC base=-0.040)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.25` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.25 (IC base=-0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.1368` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1368 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` < `2.2847` → IC=+0.125 (n=46)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.2847 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` > `1.3803` → IC=+0.148 (n=52)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.3803 (IC base=-0.040)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `8.0` → IC=-0.365 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.169 (n=158)

- **FILTRO** `dist_vwap_pct` > `0.2381` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2381
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=193)

- **FILTRO** `volumen_regimen` < `0.7721` → IC=-0.343 (n=68)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7721
  - _Potencial_: sin este filtro IC_bueno=-0.155 (n=140)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.367 (n=58)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=115)

- **FILTRO** `dist_vwap_pct` > `0.4126` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4126
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=151)

- **FILTRO** `sigma_ewma_delta_pct` > `8.488` → IC=-0.306 (n=29)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.488
  - _Potencial_: sin este filtro IC_bueno=-0.281 (n=144)

- **FILTRO** `volumen_pendiente_norm` > `0.0765` → IC=-0.395 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0765
  - _Potencial_: sin este filtro IC_bueno=-0.264 (n=70)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` < `0.0033` → IC=-0.244 (n=37)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=38)

- **FILTRO** `volumen_regimen` < `1.2175` → IC=-0.269 (n=37)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2175
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=38)

- **FILTRO** `sigma_h` < `0.0018` → IC=-0.300 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0018
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=55)

- **FILTRO** `dist_vwap_pct` < `0.0689` → IC=-0.283 (n=44)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0689
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=29)

- **FILTRO** `sigma_ewma_delta_pct` > `2.847` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.847
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=43)

- **FILTRO** `volumen_regimen` > `0.9258` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9258
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=55)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.899` → IC=-0.413 (n=44)

  - _Acción_: SKIP cuando `ibs_20min` < 0.899
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=23)

- **FILTRO** `volumen_regimen` > `1.1069` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.1069
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=51)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.357 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=38)

- **FILTRO** `ibs_20min` > `0.6404` → IC=-0.367 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6404
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=29)

- **PATRÓN** `ibs_20min` > `0.9883` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9883 (IC base=-0.225)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_h` < `0.0073` → IC=-0.300 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0073
  - _Potencial_: sin este filtro IC_bueno=-0.157 (n=33)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=50)

- **FILTRO** `volumen_regimen` < `1.1043` → IC=-0.433 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.1043
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=15)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.1832` → IC=-0.129 (n=122)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1832
  - _Potencial_: sin este filtro IC_bueno=+0.151 (n=239)

- **FILTRO** `dist_vwap_pct` > `0.6357` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6357
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=336)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.169 (n=119)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0059 (IC base=+0.091)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.132 (n=123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 15.0 (IC base=+0.091)

- **PATRÓN** `ibs_20min` > `0.6382` → IC=+0.160 (n=263)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.6382 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `0.5013` → IC=+0.188 (n=62)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.5013 (IC base=+0.091)

- **PATRÓN** `ibs_20min` < `0.1832` → IC=+0.151 (n=239)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.1832 (IC base=+0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.944` → IC=+0.146 (n=111)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 5.944 (IC base=+0.057)

- **PATRÓN** `libro_liquidez` > `3805.194` → IC=+0.172 (n=123)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 3805.194 (IC base=+0.057)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.273 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=94)

- **FILTRO** `ibs_20min` < `0.584` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` < 0.584
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=86)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.147 (n=83)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0034 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.2293` → IC=+0.157 (n=106)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2293 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.214 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.1108` → IC=+0.203 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1108 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` < `0.3016` → IC=+0.132 (n=150)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.3016 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `0.8235` → IC=+0.135 (n=83)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8235 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` < `0.1172` → IC=+0.170 (n=89)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.1172 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `1.4478` → IC=+0.153 (n=93)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.4478 (IC base=+0.123)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` < `0.603` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `ibs_20min` < 0.603
  - _Potencial_: sin este filtro IC_bueno=+0.176 (n=69)

- **FILTRO** `ibs_20min` > `0.1832` → IC=-0.159 (n=39)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1832
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=77)

- **PATRÓN** `sigma_h` < `0.0023` → IC=+0.288 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0023 (IC base=+0.053)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.192 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.053)

- **PATRÓN** `ibs_20min` > `0.603` → IC=+0.176 (n=69)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.603 (IC base=+0.053)

- **PATRÓN** `libro_liquidez` > `1529.3843` → IC=+0.125 (n=62)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 1529.3843 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.429` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.429 (IC base=+0.025)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2` → IC=-0.167 (n=37)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=43)

- **FILTRO** `dist_vwap_pct` > `0.1432` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1432
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=55)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.226 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0073 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.207 (n=114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` < `0.7027` → IC=+0.244 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7027 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.6943` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6943 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.688` → IC=+0.242 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.688 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `0.7968` → IC=+0.287 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7968 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.081` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.081 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `1.396` → IC=+0.405 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.396 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.206 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.0808` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0808 (IC base=-0.037)

### LATE_WINDOW_5MIN
- **PATRÓN** `drift_ventana_pct` |x|> `0.4605` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4605 (IC base=+0.296)

- **PATRÓN** `elapsed_s` > `193.7` → IC=+0.365 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 193.7 (IC base=+0.296)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.296)

- **PATRÓN** `drift_60min` |x|≤ `0.8011` → IC=+0.365 (n=35)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8011 (IC base=+0.296)

- **PATRÓN** `ballena_activa_n` < `1294.0` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1294.0 (IC base=+0.296)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3676` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3676 (IC base=+0.211)

- **PATRÓN** `elapsed_s` < `214.1` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 214.1 (IC base=+0.211)

- **PATRÓN** `drift_15min` |x|≤ `2.1869` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.1869 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.7195` → IC=+0.321 (n=26)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.7195 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `1770.0` → IC=+0.278 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1770.0 (IC base=+0.211)

### LATE_WINDOW_5MIN#BTC#5min
- **PATRÓN** `drift_ventana_pct` |x|> `0.4605` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4605 (IC base=+0.296)

- **PATRÓN** `elapsed_s` > `193.7` → IC=+0.365 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 193.7 (IC base=+0.296)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.296)

- **PATRÓN** `drift_60min` |x|≤ `0.8011` → IC=+0.365 (n=35)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8011 (IC base=+0.296)

- **PATRÓN** `ballena_activa_n` < `1294.0` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1294.0 (IC base=+0.296)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3676` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3676 (IC base=+0.211)

- **PATRÓN** `elapsed_s` < `214.1` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 214.1 (IC base=+0.211)

- **PATRÓN** `drift_15min` |x|≤ `2.1869` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.1869 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.7195` → IC=+0.321 (n=26)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.7195 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `1770.0` → IC=+0.278 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1770.0 (IC base=+0.211)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `libro_liquidez` > `2925.8845` → IC=+0.169 (n=243)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2925.8845 (IC base=+0.107)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2925.8845` → IC=+0.169 (n=243)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2925.8845 (IC base=+0.107)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `10.0` → IC=-0.204 (n=69)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=80)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=133)

- **FILTRO** `libro_liquidez` < `11321.3584` → IC=-0.173 (n=111)

  - _Acción_: SKIP cuando `libro_liquidez` < 11321.3584
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=38)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=213)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=199)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=38)

- **FILTRO** `liq_n` < `4.0` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `liq_n` < 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

- **FILTRO** `libro_liquidez` < `15479.8554` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 15479.8554
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.167 (n=16)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1856)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=93)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9583` → IC=-0.295 (n=37)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9583
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=77)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=82)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=93)

### LIQUIDACIONES_5M#BNB#5min
- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 25.0 (IC base=+0.049)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `35750.18` → IC=-0.127 (n=65)

  - _Acción_: SKIP cuando `liq_usd_total` < 35750.18
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=133)

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

- **PATRÓN** `liq_n` > `18.0` → IC=+0.198 (n=51)

  - _Acción_: Kelly boost +0.99€ cuando `liq_n` > 18.0 (IC base=+0.015)

- **PATRÓN** `liq_usd_total` > `73032.76` → IC=+0.144 (n=99)

  - _Acción_: Kelly boost +0.72€ cuando `liq_usd_total` > 73032.76 (IC base=+0.015)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=136)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=814)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=768)

- **FILTRO** `liq_usd_total` < `9664.41` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `liq_usd_total` < 9664.41
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9593` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9593
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=16)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=433)

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
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=189)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.148 (n=69)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.495 (IC base=+0.007)

- **PATRÓN** `libro_liquidez` > `3983.3207` → IC=+0.185 (n=52)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 3983.3207 (IC base=+0.007)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=637)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=637)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.143 (n=208)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=509)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=370)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=370)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=172)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=172)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=107)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.136 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=73)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=87)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=111)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=208)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=89)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=92)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=242)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=242)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=130)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.47` → IC=-0.121 (n=499)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=264)

- **FILTRO** `restante_min` < `3.82` → IC=-0.126 (n=249)

  - _Acción_: SKIP cuando `restante_min` < 3.82
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=514)

- **PATRÓN** `py_entrada` < `0.47` → IC=+0.162 (n=205)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` < 0.47 (IC base=+0.023)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `profundidad_ratio` < `255.7` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `profundidad_ratio` < 255.7
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=53)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.123 (n=51)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=+0.172 (n=56)

- **PATRÓN** `py_entrada` > `0.44` → IC=+0.122 (n=35)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.44 (IC base=+0.000)

- **PATRÓN** `py_entrada` < `0.54` → IC=+0.172 (n=56)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` < 0.54 (IC base=+0.032)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.56` → IC=+0.145 (n=60)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.56 (IC base=+0.070)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.192 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=27)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=-0.114 (n=42)

- **FILTRO** `restante_min` < `3.98` → IC=-0.227 (n=42)

  - _Acción_: SKIP cuando `restante_min` < 3.98
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **FILTRO** `lag_apertura_s` > `61.04` → IC=-0.239 (n=44)

  - _Acción_: SKIP cuando `lag_apertura_s` > 61.04
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=15)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=35)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=44)

- **FILTRO** `profundidad_ratio` < `114.6` → IC=-0.159 (n=39)

  - _Acción_: SKIP cuando `profundidad_ratio` < 114.6
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=21)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=48)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.245 (n=53)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=29)

- **FILTRO** `restante_min` < `3.82` → IC=-0.333 (n=40)

  - _Acción_: SKIP cuando `restante_min` < 3.82
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=42)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.333 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=66)

- **FILTRO** `lag_apertura_s` > `70.81` → IC=-0.333 (n=40)

  - _Acción_: SKIP cuando `lag_apertura_s` > 70.81
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=42)

- **PATRÓN** `py_entrada` < `0.45` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.45 (IC base=+0.006)

- **PATRÓN** `profundidad_ratio` > `48.0` → IC=+0.143 (n=40)

  - _Acción_: Kelly boost +0.71€ cuando `profundidad_ratio` > 48.0 (IC base=+0.006)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `restante_min` < `13.48` → IC=-0.122 (n=43)

  - _Acción_: SKIP cuando `restante_min` < 13.48
  - _Potencial_: sin este filtro IC_bueno=+0.182 (n=20)

- **FILTRO** `lag_apertura_s` > `142.41` → IC=-0.136 (n=31)

  - _Acción_: SKIP cuando `lag_apertura_s` > 142.41
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=32)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.198 (n=41)

- **PATRÓN** `restante_min` > `13.48` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `restante_min` > 13.48 (IC base=-0.023)

- **PATRÓN** `lag_apertura_s` < `90.92` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 90.92 (IC base=-0.023)

- **PATRÓN** `py_entrada` < `0.58` → IC=+0.198 (n=41)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.58 (IC base=+0.033)

- **PATRÓN** `restante_min` > `13.48` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` > 13.48 (IC base=+0.033)

- **PATRÓN** `lag_apertura_s` < `90.81` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 90.81 (IC base=+0.033)

- **PATRÓN** `profundidad_ratio` > `4.6` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `profundidad_ratio` > 4.6 (IC base=+0.033)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **PATRÓN** `py_entrada` < `0.42` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.42 (IC base=+0.013)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.182 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 16.0 (IC base=+0.013)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.182 (n=64)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=33)

- **FILTRO** `profundidad_ratio` < `24.4` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `profundidad_ratio` < 24.4
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=65)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.5 (IC base=+0.033)

- **PATRÓN** `profundidad_ratio` > `12.8` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `profundidad_ratio` > 12.8 (IC base=+0.033)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.185 (n=87)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=30)

- **PATRÓN** `py_entrada` < `0.59` → IC=+0.125 (n=54)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.59 (IC base=+0.031)

- **PATRÓN** `restante_min` > `3.85` → IC=+0.167 (n=40)

  - _Acción_: Kelly boost +0.83€ cuando `restante_min` > 3.85 (IC base=+0.031)

- **PATRÓN** `lag_apertura_s` < `68.74` → IC=+0.167 (n=40)

  - _Acción_: Kelly boost +0.83€ cuando `lag_apertura_s` < 68.74 (IC base=+0.031)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=7598)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.167 (n=3614)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=10938)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.165 (n=3745)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=11325)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.209 (n=623)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=1908)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.194 (n=631)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=1949)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.203 (n=651)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=2049)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.176 (n=612)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=1906)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.176 (n=655)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=2051)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=2815)

- **FILTRO** `py_entrada` > `0.595` → IC=-0.212 (n=709)

  - _Acción_: SKIP cuando `py_entrada` > 0.595
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=2292)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=2980)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.175 (n=121)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=402)

- **FILTRO** `ibs_20min` > `0.1725` → IC=-0.144 (n=130)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1725
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=393)

- **FILTRO** `libro_liquidez` < `17011.7455` → IC=-0.143 (n=228)

  - _Acción_: SKIP cuando `libro_liquidez` < 17011.7455
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=684)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.146 (n=80)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=249)

- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=257)

- **FILTRO** `py_entrada` > `0.625` → IC=-0.279 (n=66)

  - _Acción_: SKIP cuando `py_entrada` > 0.625
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=252)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=789)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=223)

### MOMENTUM_IBS_5M#BNB#5min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=40)

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

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.179 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 15.0 (IC base=+0.032)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=10193)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=23066)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.273 (n=8172)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=25087)

- **FILTRO** `ibs_7min` < `0.28` → IC=-0.234 (n=8313)

  - _Acción_: SKIP cuando `ibs_7min` < 0.28
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=24946)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.156 (n=11295)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=21964)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.230 (n=10233)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=31537)

- **FILTRO** `ibs_7min` > `0.2924` → IC=-0.178 (n=10439)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2924
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=31331)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.136 (n=1664)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=3852)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.310 (n=1312)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4204)

- **FILTRO** `ibs_7min` < `0.7111` → IC=-0.249 (n=1820)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7111
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=3696)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.186 (n=1237)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=4279)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.259 (n=1770)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=5411)

- **FILTRO** `drift_7min_pct` |x|> `0.1118` → IC=-0.125 (n=2440)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1118
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=4741)

- **FILTRO** `ibs_7min` > `0.788` → IC=-0.207 (n=1795)

  - _Acción_: SKIP cuando `ibs_7min` > 0.788
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=5386)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.137 (n=1334)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=4402)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.250 (n=1392)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=4344)

- **FILTRO** `ibs_7min` < `0.7468` → IC=-0.192 (n=1434)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7468
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=4302)

- **FILTRO** `ballena_activa_n` > `161.0` → IC=-0.176 (n=1429)

  - _Acción_: SKIP cuando `ballena_activa_n` > 161.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=4307)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.255 (n=1454)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=4366)

- **FILTRO** `ibs_7min` > `0.2609` → IC=-0.179 (n=1453)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2609
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=4367)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.182 (n=1451)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=4369)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.166 (n=1278)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=3966)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.303 (n=1295)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=3949)

- **FILTRO** `ibs_7min` < `0.7062` → IC=-0.242 (n=1729)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7062
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=3515)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.222 (n=1196)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=4048)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.237 (n=1757)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=5925)

- **FILTRO** `ibs_7min` > `0.7465` → IC=-0.172 (n=1920)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7465
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=5762)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=1755)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=3735)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.233 (n=1625)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=3865)

- **FILTRO** `ibs_7min` < `0.7398` → IC=-0.182 (n=1372)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7398
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=4118)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.173 (n=1341)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=4149)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.260 (n=1395)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=4198)

- **FILTRO** `ibs_7min` > `0.2745` → IC=-0.178 (n=1398)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2745
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=4195)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.184 (n=1373)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=4220)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.36` → IC=-0.255 (n=1429)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=4357)

- **FILTRO** `ibs_7min` < `0.3` → IC=-0.234 (n=1444)

  - _Acción_: SKIP cuando `ibs_7min` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=4342)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.180 (n=1884)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=6067)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.38` → IC=-0.254 (n=1790)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=3697)

- **FILTRO** `ibs_7min` < `0.3` → IC=-0.225 (n=1371)

  - _Acción_: SKIP cuando `ibs_7min` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=4116)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.215 (n=1337)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=4150)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.206 (n=1790)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=5753)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1100)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=536)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1156)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=324)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=562)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3978` → IC=+0.128 (n=758)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.64€ cuando `delta_ratio` |x|> 0.3978 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.120 (n=688)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 6.0 (IC base=+0.112)

- **PATRÓN** `total_vol_5m` < `471.727` → IC=+0.143 (n=253)

  - _Acción_: Kelly boost +0.72€ cuando `total_vol_5m` < 471.727 (IC base=+0.112)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4376` → IC=+0.139 (n=59)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio` |x|> 0.4376 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=182)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `total_vol_5m` < `453.526` → IC=+0.137 (n=155)

  - _Acción_: Kelly boost +0.68€ cuando `total_vol_5m` < 453.526 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.167 (n=76)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 15.0 (IC base=+0.136)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.132 (n=55)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 10.0 (IC base=+0.089)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4133` → IC=+0.182 (n=105)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.91€ cuando `delta_ratio` |x|> 0.4133 (IC base=+0.098)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.167 (n=52)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 16.0 (IC base=+0.098)

- **PATRÓN** `total_vol_5m` < `394.3776` → IC=+0.204 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 394.3776 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.190 (n=69)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 77.0 (IC base=+0.098)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3985` → IC=+0.167 (n=133)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio` |x|> 0.3985 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.199 (n=91)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 11.0 (IC base=+0.131)

- **PATRÓN** `total_vol_5m` < `7671.127` → IC=+0.159 (n=133)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 7671.127 (IC base=+0.131)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.137 (n=133)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 13.0 (IC base=+0.098)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `3589.6144` → IC=+0.167 (n=67)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3589.6144 (IC base=+0.098)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.007` → IC=-0.324 (n=134)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=261)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `87.9866` → IC=-0.438 (n=30)

  - _Acción_: SKIP cuando `T_h` > 87.9866
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=94)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.235 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.119)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0107` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0107
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=20)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0137` → IC=-0.184 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0137
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=55)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `pct_vs_K` |x|> `2.7217` → IC=-0.225 (n=194)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7217
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=198)

- **FILTRO** `sigma_h` < `0.0044` → IC=-0.326 (n=84)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0044
  - _Potencial_: sin este filtro IC_bueno=-0.295 (n=252)

- **FILTRO** `T_h` > `62.1058` → IC=-0.330 (n=251)

  - _Acción_: SKIP cuando `T_h` > 62.1058
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=85)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.004` → IC=-0.194 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.004
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=104)

- **FILTRO** `pct_vs_K` |x|> `2.9087` → IC=-0.353 (n=32)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9087
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=106)

- **FILTRO** `T_h` < `97.7009` → IC=-0.384 (n=41)

  - _Acción_: SKIP cuando `T_h` < 97.7009
  - _Potencial_: sin este filtro IC_bueno=-0.267 (n=84)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `2.4229` → IC=-0.354 (n=53)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.4229
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=58)

- **FILTRO** `sigma_h` > `0.0094` → IC=-0.321 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=81)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.352 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=82)

- **FILTRO** `T_h` > `48.0686` → IC=-0.305 (n=80)

  - _Acción_: SKIP cuando `T_h` > 48.0686
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=27)

- **PATRÓN** `pct_vs_K` |x|≤ `1.3415` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.3415 (IC base=-0.199)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0083` → IC=-0.136 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=63)

- **FILTRO** `T_h` > `132.7892` → IC=-0.197 (n=31)

  - _Acción_: SKIP cuando `T_h` > 132.7892
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=63)

- **FILTRO** `pct_vs_K` |x|> `4.9375` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.9375
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=71)

- **FILTRO** `T_h` > `61.2269` → IC=-0.385 (n=50)

  - _Acción_: SKIP cuando `T_h` > 61.2269
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=18)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1208` → IC=+0.466 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1208 (IC base=+0.375)

- **PATRÓN** `sigma_h` < `0.0134` → IC=+0.406 (n=51)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0134 (IC base=+0.375)

- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.425 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.375)

- **PATRÓN** `T_h` > `0.4742` → IC=+0.433 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4742 (IC base=+0.375)

- **PATRÓN** `dist_50` > `0.3641` → IC=+0.462 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3641 (IC base=+0.375)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.438 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.375)

- **PATRÓN** `edge` > `0.1152` → IC=+0.452 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1152 (IC base=+0.410)

- **PATRÓN** `sigma_h` < `0.0124` → IC=+0.420 (n=123)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0124 (IC base=+0.410)

- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.437 (n=93)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.410)

- **PATRÓN** `T_h` < `0.6208` → IC=+0.420 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6208 (IC base=+0.410)

- **PATRÓN** `T_h` > `1.476` → IC=+0.439 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.476 (IC base=+0.410)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.491 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.410)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.468 (n=93)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.410)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.2492` → IC=+0.447 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2492 (IC base=+0.411)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.395 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0072 (IC base=+0.411)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.450 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.411)

- **PATRÓN** `T_h` < `0.6559` → IC=+0.429 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6559 (IC base=+0.411)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.468 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.411)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.429 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.411)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.225` → IC=+0.473 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.225 (IC base=+0.464)

- **PATRÓN** `sigma_h` < `0.0154` → IC=+0.472 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0154 (IC base=+0.464)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.446 (n=35)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.464)

- **PATRÓN** `T_h` > `0.8497` → IC=+0.473 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8497 (IC base=+0.464)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.464 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.464)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.464 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.464)

- **PATRÓN** `edge` > `0.1229` → IC=+0.464 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1229 (IC base=+0.456)

- **PATRÓN** `sigma_h` < `0.0162` → IC=+0.478 (n=91)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0162 (IC base=+0.456)

- **PATRÓN** `T_h` > `0.9178` → IC=+0.464 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.9178 (IC base=+0.456)

- **PATRÓN** `dist_50` > `0.5` → IC=+0.479 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.5 (IC base=+0.456)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.460 (n=99)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.456)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=182)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=299)

- **PATRÓN** `streak_estiramiento` < `0.4117` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `streak_estiramiento` < 0.4117 (IC base=+0.038)

- **PATRÓN** `streak_estiramiento` < `0.5654` → IC=+0.159 (n=130)

  - _Acción_: Kelly boost +0.80€ cuando `streak_estiramiento` < 0.5654 (IC base=+0.037)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.237 (n=17)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.029)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `streak_estiramiento` > `0.4152` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4152
  - _Potencial_: sin este filtro IC_bueno=+0.204 (n=25)

- **PATRÓN** `streak_estiramiento` < `0.4152` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.4152 (IC base=+0.000)

- **PATRÓN** `streak_estiramiento` < `0.5763` → IC=+0.120 (n=77)

  - _Acción_: Kelly boost +0.60€ cuando `streak_estiramiento` < 0.5763 (IC base=+0.055)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.126 (n=89)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 49.0 (IC base=+0.055)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=86)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=92)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=36)

- **FILTRO** `streak_estiramiento` > `1.1202` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_estiramiento` > 1.1202
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=31)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=24)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=797)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=803)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=409)

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
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=618)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1131)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=775)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=741)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=2970)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=1516)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=1524)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.220 (n=755)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0087 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.1607` → IC=+0.194 (n=1464)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1607 (IC base=+0.186)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2154` → IC=+0.188 (n=555)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.2154 (IC base=+0.186)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1267` → IC=+0.231 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1267 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.195 (n=1550)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 6.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.186 (n=1738)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.186)

- **PATRÓN** `ibs_15` > `0.6061` → IC=+0.267 (n=1664)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6061 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` > `0.1187` → IC=+0.185 (n=846)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1187 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` < `0.6231` → IC=+0.178 (n=1578)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.6231 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.803` → IC=+0.278 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.803 (IC base=+0.186)

- **PATRÓN** `libro_liquidez` > `8801.8341` → IC=+0.198 (n=555)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 8801.8341 (IC base=+0.186)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=648)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.221 (n=371)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.0587` → IC=+0.294 (n=124)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0587 (IC base=+0.208)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2571` → IC=+0.254 (n=124)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2571 (IC base=+0.208)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1443` → IC=+0.273 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1443 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.241 (n=345)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.208)

- **PATRÓN** `ibs_15` > `0.7036` → IC=+0.278 (n=371)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7036 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.4066` → IC=+0.259 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4066 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.607` → IC=+0.262 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.607 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `15203.8562` → IC=+0.235 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15203.8562 (IC base=+0.208)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `29.297` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 29.297
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=402)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.139 (n=388)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0065 (IC base=+0.131)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.150 (n=258)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0051 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.0678` → IC=+0.147 (n=171)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.0678 (IC base=+0.131)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2337` → IC=+0.164 (n=129)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.82€ cuando `delta_ratio_macro` |x|> 0.2337 (IC base=+0.131)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.258` → IC=+0.154 (n=278)

  - _Acción_: Kelly boost +0.77€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.258 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.148 (n=288)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.136 (n=404)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 17.0 (IC base=+0.131)

- **PATRÓN** `ibs_15` > `0.659` → IC=+0.250 (n=346)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.659 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.1604` → IC=+0.148 (n=305)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1604 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.307` → IC=+0.208 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.307 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `3422.7688` → IC=+0.141 (n=346)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3422.7688 (IC base=+0.131)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.176 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=103)

- **FILTRO** `ibs_15` > `0.2101` → IC=-0.243 (n=33)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2101
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=102)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.291 (n=65)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.1498` → IC=+0.201 (n=172)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1498 (IC base=+0.172)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0712` → IC=+0.195 (n=175)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.97€ cuando `delta_ratio_macro` |x|> 0.0712 (IC base=+0.172)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2704` → IC=+0.222 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2704 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.172)

- **PATRÓN** `ibs_15` > `0.6111` → IC=+0.267 (n=195)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6111 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.3239` → IC=+0.193 (n=73)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.3239 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` < `0.5335` → IC=+0.174 (n=213)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.5335 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.389` → IC=+0.407 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.389 (IC base=+0.172)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.178 (n=150)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `3077.8574` → IC=+0.280 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3077.8574 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.220 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.172)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.5705` → IC=-0.135 (n=124)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.5705
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=918)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.784` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 8.784 (IC base=-0.004)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0234` → IC=+0.264 (n=146)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0234 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.0851` → IC=+0.218 (n=193)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0851 (IC base=+0.188)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0393` → IC=+0.193 (n=437)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.0393 (IC base=+0.188)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0904` → IC=+0.252 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0904 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.230 (n=150)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.188)

- **PATRÓN** `ibs_15` > `0.5556` → IC=+0.281 (n=437)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5556 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` > `0.1342` → IC=+0.208 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1342 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` < `0.8342` → IC=+0.190 (n=504)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.8342 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.866` → IC=+0.235 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.866 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.591` → IC=+0.189 (n=438)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 10.591 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.189 (n=454)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.02 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `2917.3018` → IC=+0.297 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2917.3018 (IC base=+0.188)

- **PATRÓN** `ibs_15` < `0.1176` → IC=+0.158 (n=492)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.79€ cuando `ibs_15` < 0.1176 (IC base=+0.051)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.341 (n=281)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.342)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.376 (n=191)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.342)

- **PATRÓN** `drift_60min` |x|≤ `0.1078` → IC=+0.348 (n=281)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1078 (IC base=+0.342)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1435` → IC=+0.369 (n=280)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1435 (IC base=+0.342)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1316` → IC=+0.380 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1316 (IC base=+0.342)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.361 (n=424)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.342)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.384 (n=420)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.342)

- **PATRÓN** `dist_vwap_pct` > `0.4316` → IC=+0.391 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4316 (IC base=+0.342)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.247` → IC=+0.346 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.247 (IC base=+0.342)

- **PATRÓN** `sigma_ewma_delta_pct` < `14.032` → IC=+0.342 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 14.032 (IC base=+0.342)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.347 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.342)

- **PATRÓN** `libro_liquidez` > `3505.1277` → IC=+0.355 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3505.1277 (IC base=+0.342)

- **PATRÓN** `ballena_activa_n` < `462.0` → IC=+0.363 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 462.0 (IC base=+0.342)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.355 (n=205)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.346)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.375 (n=78)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.346)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.375 (n=78)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.346)

- **PATRÓN** `drift_15min` |x|≤ `0.4231` → IC=+0.357 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4231 (IC base=+0.346)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1505` → IC=+0.366 (n=155)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1505 (IC base=+0.346)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1236` → IC=+0.388 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1236 (IC base=+0.346)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.373 (n=218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.346)

- **PATRÓN** `ibs_15` > `0.8154` → IC=+0.381 (n=233)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8154 (IC base=+0.346)

- **PATRÓN** `dist_vwap_pct` > `0.4016` → IC=+0.413 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4016 (IC base=+0.346)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.152` → IC=+0.352 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.152 (IC base=+0.346)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.763` → IC=+0.351 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.763 (IC base=+0.346)

- **PATRÓN** `libro_liquidez` > `11204.8499` → IC=+0.366 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11204.8499 (IC base=+0.346)

- **PATRÓN** `ballena_activa_n` < `572.0` → IC=+0.393 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 572.0 (IC base=+0.346)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.332 (n=188)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.333)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.366 (n=125)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.333)

- **PATRÓN** `drift_60min` |x|≤ `0.1054` → IC=+0.344 (n=126)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1054 (IC base=+0.333)

- **PATRÓN** `delta_ratio_macro` |x|> `0.087` → IC=+0.359 (n=168)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.087 (IC base=+0.333)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2925` → IC=+0.359 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2925 (IC base=+0.333)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.399 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.333)

- **PATRÓN** `ibs_15` > `0.7408` → IC=+0.390 (n=188)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7408 (IC base=+0.333)

- **PATRÓN** `dist_vwap_pct` > `0.4613` → IC=+0.383 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4613 (IC base=+0.333)

- **PATRÓN** `dist_vwap_pct` < `0.1175` → IC=+0.346 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1175 (IC base=+0.333)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.031` → IC=+0.350 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.031 (IC base=+0.333)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.899` → IC=+0.337 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.899 (IC base=+0.333)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.344 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.333)

- **PATRÓN** `libro_liquidez` > `3893.6222` → IC=+0.362 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3893.6222 (IC base=+0.333)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0129` → IC=-0.222 (n=673)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0129
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=2020)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.197 (n=918)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1775)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1378` → IC=+0.252 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1378 (IC base=-0.065)

- **PATRÓN** `ibs_15` > `0.6395` → IC=+0.275 (n=642)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6395 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` < `0.5943` → IC=+0.184 (n=634)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.5943 (IC base=-0.065)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0752` → IC=+0.244 (n=1649)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0752 (IC base=-0.031)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.178` → IC=+0.236 (n=1194)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.178 (IC base=-0.031)

- **PATRÓN** `ibs_15` < `0.3469` → IC=+0.277 (n=1846)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3469 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` > `0.6957` → IC=+0.305 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6957 (IC base=-0.031)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.224 (n=411)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=1234)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.231 (n=411)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=1234)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.210 (n=1043)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=602)

- **FILTRO** `sigma_ewma_delta_pct` > `19.521` → IC=-0.251 (n=295)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.521
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=1350)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.160 (n=154)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0029 (IC base=+0.081)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2033` → IC=+0.293 (n=80)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2033 (IC base=+0.081)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1073` → IC=+0.328 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1073 (IC base=+0.081)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.123 (n=316)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 12.0 (IC base=+0.081)

- **PATRÓN** `ibs_15` > `0.7496` → IC=+0.332 (n=177)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7496 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.102` → IC=+0.287 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.102 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` < `0.3703` → IC=+0.275 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3703 (IC base=+0.081)

- **PATRÓN** `ballena_activa_n` < `441.0` → IC=+0.265 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 441.0 (IC base=+0.081)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6686` → IC=-0.189 (n=101)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6686
  - _Potencial_: sin este filtro IC_bueno=+0.261 (n=304)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.162 (n=388)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.152 (n=268)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.006 (IC base=+0.149)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.183 (n=203)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0051 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.0757` → IC=+0.213 (n=134)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0757 (IC base=+0.149)

- **PATRÓN** `drift_15min` |x|≤ `0.4193` → IC=+0.164 (n=102)

  - _Acción_: Kelly boost +0.82€ cuando `drift_15min` |x|≤ 0.4193 (IC base=+0.149)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0589` → IC=+0.154 (n=304)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio_macro` |x|> 0.0589 (IC base=+0.149)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2902` → IC=+0.230 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2902 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.203 (n=143)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.149)

- **PATRÓN** `ibs_15` > `0.6686` → IC=+0.261 (n=304)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6686 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.4741` → IC=+0.152 (n=87)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.4741 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.1135` → IC=+0.185 (n=217)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.1135 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.115` → IC=+0.155 (n=259)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 9.115 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.162 (n=388)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `11031.3332` → IC=+0.186 (n=138)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 11031.3332 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.273 (n=240)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.231)

- **PATRÓN** `drift_60min` |x|≤ `0.4447` → IC=+0.235 (n=719)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4447 (IC base=+0.231)

- **PATRÓN** `drift_15min` |x|≤ `0.4794` → IC=+0.246 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4794 (IC base=+0.231)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2029` → IC=+0.262 (n=326)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2029 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.239 (n=282)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.231)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.244 (n=268)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.231)

- **PATRÓN** `ibs_15` < `0.2691` → IC=+0.284 (n=633)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2691 (IC base=+0.231)

- **PATRÓN** `dist_vwap_pct` > `0.7631` → IC=+0.320 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7631 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.403` → IC=+0.253 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.403 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.221` → IC=+0.239 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.221 (IC base=+0.231)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1682` → IC=-0.220 (n=216)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=421)

- **FILTRO** `drift_15min` |x|> `0.89` → IC=-0.270 (n=159)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.89
  - _Potencial_: sin este filtro IC_bueno=-0.138 (n=478)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.350 (n=18)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=-0.171)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0761` → IC=+0.229 (n=282)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0761 (IC base=-0.042)

- **PATRÓN** `ibs_15` < `0.3529` → IC=+0.267 (n=316)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3529 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.4968` → IC=+0.216 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4968 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` < `0.2005` → IC=+0.224 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2005 (IC base=-0.042)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.2005` → IC=-0.199 (n=267)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.2005
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=519)

- **FILTRO** `sigma_h` > `0.0198` → IC=-0.261 (n=392)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0198
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=394)

- **FILTRO** `drift_15min` |x|> `1.2727` → IC=-0.268 (n=196)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2727
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=590)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.262 (n=191)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=595)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1333` → IC=+0.293 (n=220)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1333 (IC base=-0.042)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.103` → IC=+0.344 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.103 (IC base=-0.042)

- **PATRÓN** `ibs_15` < `0.3437` → IC=+0.307 (n=484)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3437 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.932` → IC=+0.347 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.932 (IC base=-0.042)

### UPDOWN_GBM_ETH_15M_HORA7
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2775` → IC=-0.136 (n=20)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2775
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **FILTRO** `ibs_15` < `0.8489` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8489
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **PATRÓN** `dist_vwap_pct` > `0.1645` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1645 (IC base=+0.050)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2775` → IC=-0.136 (n=20)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2775
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **FILTRO** `ibs_15` < `0.8489` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8489
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **PATRÓN** `dist_vwap_pct` > `0.1645` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1645 (IC base=+0.050)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.303 (n=449)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.0563` → IC=+0.328 (n=225)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0563 (IC base=+0.293)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2395` → IC=+0.310 (n=224)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2395 (IC base=+0.293)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1077` → IC=+0.347 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1077 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.313 (n=704)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.293)

- **PATRÓN** `ibs_15` > `0.8404` → IC=+0.328 (n=673)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8404 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.447` → IC=+0.330 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.447 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.63` → IC=+0.337 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.63 (IC base=+0.293)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.295 (n=821)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `13084.0601` → IC=+0.305 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13084.0601 (IC base=+0.293)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.304 (n=248)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.288)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.288 (n=168)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.0574` → IC=+0.349 (n=124)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0574 (IC base=+0.288)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2616` → IC=+0.309 (n=124)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2616 (IC base=+0.288)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.382` → IC=+0.312 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.382 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.309 (n=390)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.288)

- **PATRÓN** `ibs_15` > `0.8292` → IC=+0.318 (n=371)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8292 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` > `0.444` → IC=+0.357 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.444 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.359 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `16201.6469` → IC=+0.325 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16201.6469 (IC base=+0.288)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.310 (n=303)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.297)

- **PATRÓN** `drift_60min` |x|≤ `0.1126` → IC=+0.299 (n=202)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1126 (IC base=+0.297)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1466` → IC=+0.304 (n=202)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1466 (IC base=+0.297)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.288` → IC=+0.331 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.288 (IC base=+0.297)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.328 (n=271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.297)

- **PATRÓN** `ibs_15` > `0.8516` → IC=+0.339 (n=303)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8516 (IC base=+0.297)

- **PATRÓN** `dist_vwap_pct` > `0.2899` → IC=+0.303 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2899 (IC base=+0.297)

- **PATRÓN** `dist_vwap_pct` < `0.456` → IC=+0.297 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.456 (IC base=+0.297)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.564` → IC=+0.324 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.564 (IC base=+0.297)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.305 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.297)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2547` → IC=-0.158 (n=71)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2547
  - _Potencial_: sin este filtro IC_bueno=-0.116 (n=214)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1143` → IC=-0.171 (n=71)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1143
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=214)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.164 (n=111)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=333)

- **FILTRO** `ballena_activa_n` > `60.0` → IC=-0.223 (n=45)

  - _Acción_: SKIP cuando `ballena_activa_n` > 60.0
  - _Potencial_: sin este filtro IC_bueno=-0.129 (n=138)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0682` → IC=-0.155 (n=56)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0682
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=111)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1226` → IC=-0.151 (n=41)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1226
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=126)

- **FILTRO** `drift_15min` |x|> `0.2287` → IC=-0.250 (n=22)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2287
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=23)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2236` → IC=-0.133 (n=28)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2236
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2122` → IC=-0.395 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2122
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0943` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0943
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `drift_15min` |x|> `0.2657` → IC=-0.208 (n=22)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2657
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
- **PATRÓN** `T_h` > `76.962` → IC=+0.217 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 76.962 (IC base=+0.202)

- **PATRÓN** `ratio` < `0.9779` → IC=+0.465 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9779 (IC base=+0.202)

- **PATRÓN** `T_h` > `145.7851` → IC=+0.394 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7851 (IC base=+0.332)

- **PATRÓN** `ratio` > `1.01` → IC=+0.287 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.01 (IC base=+0.332)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `115.2222` → IC=+0.211 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 115.2222 (IC base=+0.176)

- **PATRÓN** `ratio` < `0.973` → IC=+0.446 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.176)

- **PATRÓN** `T_h` < `111.996` → IC=+0.295 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 111.996 (IC base=+0.282)

- **PATRÓN** `T_h` > `102.8316` → IC=+0.289 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 102.8316 (IC base=+0.282)

- **PATRÓN** `ratio` > `1.0466` → IC=+0.330 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0466 (IC base=+0.282)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `91.5869` → IC=+0.283 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 91.5869 (IC base=+0.244)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.421 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.244)

- **PATRÓN** `T_h` > `103.3918` → IC=+0.328 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 103.3918 (IC base=+0.311)

- **PATRÓN** `ratio` > `1.0131` → IC=+0.320 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0131 (IC base=+0.311)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1359` → IC=+0.457 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1359 (IC base=+0.403)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6061 sube el IC de +0.186 a +0.267 en UPDOWN_GBM#15min (n=1664). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7036 sube el IC de +0.208 a +0.278 en UPDOWN_GBM#BTC#15min (n=371). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.659 sube el IC de +0.131 a +0.250 en UPDOWN_GBM#ETH#15min (n=346). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6111 sube el IC de +0.172 a +0.267 en UPDOWN_GBM#SOL#15min (n=195). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5556 sube el IC de +0.188 a +0.281 en UPDOWN_GBM#XRP#15min (n=437). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1176 sube el IC de +0.051 a +0.158 en UPDOWN_GBM#XRP#15min (n=492). Ya aplicado como kelly_boost=+0.79€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6395 sube el IC de -0.065 a +0.275 en UPDOWN_GBM_15M_TARDIO (n=642). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3469 sube el IC de -0.031 a +0.277 en UPDOWN_GBM_15M_TARDIO (n=1846). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7496 sube el IC de +0.081 a +0.332 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=177). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6686 sube el IC de +0.149 a +0.261 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=304). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2691 sube el IC de +0.231 a +0.284 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=633). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.171 a +0.350 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=18). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3529 sube el IC de -0.042 a +0.267 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=316). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3437 sube el IC de -0.042 a +0.307 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=484). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8404 sube el IC de +0.293 a +0.328 en UPDOWN_GBM_IBS_ALTO (n=673). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8292 sube el IC de +0.288 a +0.318 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=371). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8516 sube el IC de +0.297 a +0.339 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=303). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.342 a +0.384 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=420). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8154 sube el IC de +0.346 a +0.381 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=233). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7408 sube el IC de +0.333 a +0.390 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=188). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1342 | +0.100 | +201.57€ | 1 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1342 | +0.100 | +201.57€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1002 | +0.110 | +174.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1002 | +0.110 | +174.70€ | 2 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 254 | +0.055 | +8.21€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 254 | +0.055 | +8.21€ | 6 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 60 | +0.145 | +20.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 60 | +0.145 | +20.16€ | 0 | 7 |
| ✅ BALLENAS_TARDIAS | 28806 | -0.088 | -3858.77€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1495 | -0.043 | -220.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 27311 | -0.090 | -3638.01€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3799 | -0.099 | -626.41€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3799 | -0.099 | -626.41€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1495 | -0.043 | -220.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1495 | -0.043 | -220.76€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3483 | -0.097 | -789.03€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3483 | -0.097 | -789.03€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 7373 | -0.020 | -690.02€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 7373 | -0.020 | -690.02€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 6995 | -0.090 | -443.82€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 6995 | -0.090 | -443.82€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 5661 | -0.171 | -1088.73€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 5661 | -0.171 | -1088.73€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 18856 | -0.027 | +3979.51€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 4916 | -0.000 | +1809.28€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 13940 | -0.037 | +2170.24€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 18856 | -0.027 | +3979.51€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 4916 | -0.000 | +1809.28€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 13940 | -0.037 | +2170.24€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 1478 | -0.103 | -191.97€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 168 | -0.053 | -21.36€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 1310 | -0.110 | -170.61€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 780 | -0.091 | -97.63€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 144 | -0.048 | -16.13€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 636 | -0.100 | -81.50€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 491 | -0.125 | -74.32€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 24 | -0.077 | -5.22€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#5min | 467 | -0.127 | -69.10€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 66 | -0.191 | -10.49€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 66 | -0.191 | -10.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 94975 | +0.112 | -4798.52€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 14276 | +0.185 | -428.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 382 | -0.078 | -49.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 74173 | +0.100 | -4097.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 6144 | +0.107 | -222.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 12334 | +0.097 | -1047.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 45 | -0.160 | -0.32€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 12274 | +0.099 | -1035.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 19213 | +0.132 | -368.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4514 | +0.204 | -130.16€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 12297 | +0.111 | -197.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2360 | +0.103 | -18.51€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 12373 | +0.090 | -1130.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 52 | -0.093 | -6.98€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 12306 | +0.091 | -1112.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 20188 | +0.123 | -403.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 5520 | +0.175 | -81.54€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 12430 | +0.105 | -253.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2226 | +0.097 | -59.89€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 18519 | +0.113 | -1111.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4098 | +0.188 | -217.39€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 285 | -0.037 | +4.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 12578 | +0.090 | -754.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1558 | +0.125 | -144.38€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 12348 | +0.100 | -737.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 47 | -0.031 | +8.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 12288 | +0.101 | -745.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 15064 | +0.191 | -995.63€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 15064 | +0.191 | -995.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3578 | +0.167 | -376.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3578 | +0.167 | -376.61€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1288 | +0.196 | -13.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1288 | +0.196 | -13.10€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3532 | +0.179 | -306.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3532 | +0.179 | -306.33€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3126 | +0.239 | -100.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3126 | +0.239 | -100.99€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3461 | +0.192 | -212.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3461 | +0.192 | -212.36€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 711 | +0.428 | -21.62€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 711 | +0.428 | -21.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 276 | +0.439 | -2.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 276 | +0.439 | -2.00€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 268 | +0.430 | -6.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 268 | +0.430 | -6.75€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 157 | +0.406 | -10.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 157 | +0.406 | -10.36€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 51960 | +0.197 | -4070.75€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 51960 | +0.197 | -4070.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 8981 | +0.176 | -1041.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 8981 | +0.176 | -1041.33€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 8302 | +0.223 | -302.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 8302 | +0.223 | -302.49€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 8976 | +0.172 | -1077.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 8976 | +0.172 | -1077.29€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 8396 | +0.218 | -332.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 8396 | +0.218 | -332.65€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 8589 | +0.203 | -562.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 8589 | +0.203 | -562.25€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 8716 | +0.193 | -754.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 8716 | +0.193 | -754.75€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 19604 | +0.117 | +162.82€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 19604 | +0.117 | +162.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 9736 | +0.121 | +141.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 9736 | +0.121 | +141.14€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 9868 | +0.113 | +21.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 9868 | +0.113 | +21.68€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1500 | +0.288 | -22.70€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1500 | +0.288 | -22.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 669 | +0.275 | -22.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 669 | +0.275 | -22.05€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 720 | +0.291 | -2.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 720 | +0.291 | -2.78€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 111 | +0.341 | +2.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 111 | +0.341 | +2.12€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 657 | +0.436 | -2.69€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 657 | +0.436 | -2.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 311 | +0.433 | -3.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 311 | +0.433 | -3.90€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 302 | +0.441 | +0.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 302 | +0.441 | +0.91€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 44 | +0.391 | +0.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 44 | +0.391 | +0.31€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1136 | +0.076 | -42.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 394 | +0.058 | -33.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 742 | +0.085 | -9.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 61 | +0.119 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 61 | +0.119 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 898 | +0.083 | -14.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 156 | +0.076 | -5.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 742 | +0.085 | -9.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 177 | +0.020 | -31.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 177 | +0.020 | -31.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 36508 | +0.097 | -1108.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3015 | +0.090 | +26.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 33493 | +0.098 | -1134.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 20479 | +0.101 | -330.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3015 | +0.090 | +26.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 17464 | +0.103 | -356.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 6899 | +0.107 | -42.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 6899 | +0.107 | -42.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 9130 | +0.081 | -735.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 9130 | +0.081 | -735.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 822 | +0.216 | -100.52€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 822 | +0.216 | -100.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 822 | +0.216 | -100.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 822 | +0.216 | -100.52€ | 2 | 4 |
| ✅ GBM_LATE_15M | 26159 | +0.083 | +12416.37€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 26159 | +0.083 | +12416.37€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 4371 | +0.193 | +3171.30€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 4371 | +0.193 | +3171.30€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 3894 | +0.179 | +2736.72€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 3894 | +0.179 | +2736.72€ | 0 | 26 |
| ✅ GBM_LATE_15M#DOGE | 4564 | +0.196 | +3368.85€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 4564 | +0.196 | +3368.85€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 3834 | +0.021 | +838.62€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 3834 | +0.021 | +838.62€ | 1 | 14 |
| ✅ GBM_LATE_15M#SOL | 3738 | -0.033 | +840.47€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 3738 | -0.033 | +840.47€ | 4 | 12 |
| ✅ GBM_LATE_15M#XRP | 5758 | -0.040 | +1460.41€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 5758 | -0.040 | +1460.41€ | 4 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 27656 | +0.086 | +14425.12€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 27656 | +0.086 | +14425.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 5253 | +0.017 | +2770.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 5253 | +0.017 | +2770.60€ | 2 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 5775 | +0.015 | +1199.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 5775 | +0.015 | +1199.78€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 3929 | +0.261 | +3939.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 3929 | +0.261 | +3939.05€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 4493 | +0.003 | +864.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 4493 | +0.003 | +864.11€ | 2 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 4479 | +0.028 | +1685.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 4479 | +0.028 | +1685.57€ | 3 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 3727 | +0.275 | +3966.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 3727 | +0.275 | +3966.01€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 21046 | +0.167 | +15621.41€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 21046 | +0.167 | +15621.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3168 | +0.206 | +2510.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3168 | +0.206 | +2510.28€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3341 | +0.149 | +2440.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3341 | +0.149 | +2440.18€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3306 | +0.206 | +2611.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3306 | +0.206 | +2611.20€ | 0 | 18 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 3525 | +0.132 | +2442.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 3525 | +0.132 | +2442.25€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 3922 | +0.115 | +2661.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 3922 | +0.115 | +2661.39€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 3784 | +0.202 | +2956.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 3784 | +0.202 | +2956.11€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 5299 | +0.128 | +2249.28€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 5299 | +0.128 | +2249.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 210 | +0.108 | +81.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 210 | +0.108 | +81.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1496 | +0.123 | +670.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1496 | +0.123 | +670.14€ | 0 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 373 | +0.143 | +176.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 373 | +0.143 | +176.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1581 | +0.146 | +722.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1581 | +0.146 | +722.11€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1133 | +0.106 | +383.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1133 | +0.106 | +383.89€ | 1 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 506 | +0.134 | +215.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 506 | +0.134 | +215.28€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 26287 | +0.175 | +19513.43€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#15min | 26287 | +0.175 | +19513.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 4165 | +0.220 | +3496.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 4165 | +0.220 | +3496.09€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 4129 | +0.151 | +2733.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 4129 | +0.151 | +2733.22€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 4323 | +0.223 | +3685.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 4323 | +0.223 | +3685.43€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 4259 | +0.136 | +2900.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 4259 | +0.136 | +2900.17€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 4593 | +0.113 | +2923.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 4593 | +0.113 | +2923.59€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 4818 | +0.204 | +3774.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 4818 | +0.204 | +3774.93€ | 0 | 24 |
| ✅ GBM_LATE_5M | 7195 | +0.151 | +4204.13€ | 1 | 28 |
| ✅ GBM_LATE_5M#5min | 7195 | +0.151 | +4204.13€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 594 | +0.186 | +416.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 594 | +0.186 | +416.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1809 | +0.148 | +1197.47€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1809 | +0.148 | +1197.47€ | 0 | 31 |
| ✅ GBM_LATE_5M#DOGE | 889 | +0.171 | +564.50€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 889 | +0.171 | +564.50€ | 0 | 22 |
| ✅ GBM_LATE_5M#ETH | 2438 | +0.158 | +1452.22€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2438 | +0.158 | +1452.22€ | 0 | 31 |
| ✅ GBM_LATE_5M#SOL | 628 | +0.114 | +246.46€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 628 | +0.114 | +246.46€ | 0 | 19 |
| ✅ GBM_LATE_5M#XRP | 837 | +0.116 | +326.92€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 837 | +0.116 | +326.92€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1770 | +0.067 | +746.61€ | 3 | 11 |
| ✅ GBM_LATE_60M#60min | 1770 | +0.067 | +746.61€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 643 | +0.086 | +265.67€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 643 | +0.086 | +265.67€ | 0 | 12 |
| ✅ GBM_LATE_60M#ETH | 585 | +0.071 | +293.50€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 585 | +0.071 | +293.50€ | 2 | 14 |
| ✅ GBM_LATE_60M#SOL | 542 | +0.040 | +187.44€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 542 | +0.040 | +187.44€ | 2 | 11 |
| 🚫 GBM_LATE_60M_FADE | 381 | -0.252 | -19.63€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 381 | -0.252 | -19.63€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 148 | -0.220 | -6.61€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 148 | -0.220 | -6.61€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 124 | -0.254 | -7.92€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 124 | -0.254 | -7.92€ | 4 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 109 | -0.284 | -5.10€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 109 | -0.284 | -5.10€ | 3 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 711 | +0.074 | +163.99€ | 2 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 711 | +0.074 | +163.99€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 279 | +0.062 | +52.40€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 279 | +0.062 | +52.40€ | 2 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 208 | +0.038 | +17.16€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 208 | +0.038 | +17.16€ | 2 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 224 | +0.119 | +94.43€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 224 | +0.119 | +94.43€ | 2 | 11 |
| ✅ LATE_WINDOW_5MIN | 102 | +0.260 | +85.53€ | 0 | 10 |
| ✅ LATE_WINDOW_5MIN#5min | 102 | +0.260 | +85.53€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 102 | +0.260 | +85.53€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 102 | +0.260 | +85.53€ | 0 | 10 |
| ✅ LEADLAG_BTC_XRP_15M | 2003 | +0.103 | +555.62€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2003 | +0.103 | +555.62€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2003 | +0.103 | +555.62€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2003 | +0.103 | +555.62€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 383 | -0.079 | -34.29€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 383 | -0.079 | -34.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 96 | -0.061 | -5.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 96 | -0.061 | -5.23€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 67 | -0.080 | -7.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 67 | -0.080 | -7.45€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 139 | -0.025 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 139 | -0.025 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 2055 | +0.007 | +16.15€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2055 | +0.007 | +16.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 106 | +0.028 | +0.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 106 | +0.028 | +0.43€ | 0 | 1 |
| ✅ LIQUIDACIONES_5M#BTC | 233 | -0.015 | +5.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 233 | -0.015 | +5.74€ | 5 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 164 | -0.036 | -7.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 164 | -0.036 | -7.46€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 861 | +0.025 | +22.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 861 | +0.025 | +22.83€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 473 | -0.001 | -5.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 473 | -0.001 | -5.44€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 218 | -0.004 | +0.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 218 | -0.004 | +0.04€ | 1 | 2 |
| ✅ LIQUIDACIONES_60M | 1102 | -0.043 | -26.67€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1102 | -0.043 | -26.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 313 | -0.043 | -13.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 313 | -0.043 | -13.27€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 372 | -0.027 | -1.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 372 | -0.027 | -1.05€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 417 | -0.059 | -12.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 417 | -0.059 | -12.36€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 1560 | -0.022 | +26.42€ | 2 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 739 | -0.021 | +7.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 821 | -0.022 | +18.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 41 | +0.012 | +5.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 24 | +0.000 | +1.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 17 | +0.022 | +3.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 382 | +0.039 | +55.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 177 | +0.020 | +13.05€ | 2 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 205 | +0.056 | +42.49€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 210 | -0.057 | -10.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 100 | -0.049 | -3.78€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 110 | -0.062 | -6.44€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 291 | -0.077 | -32.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 130 | -0.068 | -10.68€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 161 | -0.083 | -22.15€ | 4 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 270 | +0.004 | +20.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 138 | +0.007 | +10.59€ | 3 | 6 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 132 | +0.000 | +9.51€ | 0 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 366 | -0.043 | -11.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 170 | -0.035 | -3.14€ | 2 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 196 | -0.051 | -8.47€ | 1 | 3 |
| ✅ MOMENTUM_IBS_15M | 14462 | -0.011 | -207.10€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14462 | -0.011 | -207.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 3179 | -0.020 | -60.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 3179 | -0.020 | -60.29€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 29622 | -0.006 | +1336.94€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 29622 | -0.006 | +1336.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 5231 | +0.018 | +639.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 5231 | +0.018 | +639.72€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 4575 | -0.028 | -49.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 4575 | -0.028 | -49.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 5280 | +0.014 | +472.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 5280 | +0.014 | +472.64€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 4351 | -0.052 | -129.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 4351 | -0.052 | -129.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 4961 | -0.010 | +191.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 4961 | -0.010 | +191.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 5224 | +0.008 | +212.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 5224 | +0.008 | +212.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 5896 | -0.058 | -133.00€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 5896 | -0.058 | -133.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1212 | +0.001 | -14.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1212 | +0.001 | -14.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1435 | -0.083 | -37.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1435 | -0.083 | -37.49€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 44 | -0.130 | -5.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 44 | -0.130 | -5.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 647 | -0.112 | -19.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 647 | -0.112 | -19.11€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1711 | -0.077 | -30.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1711 | -0.077 | -30.54€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 847 | -0.016 | -25.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 847 | -0.016 | -25.72€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3345 | +0.004 | -2.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3345 | +0.004 | -2.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 189 | +0.013 | -1.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 189 | +0.013 | -1.05€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 137 | -0.004 | -2.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 137 | -0.004 | -2.36€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1315 | +0.007 | +7.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1315 | +0.007 | +7.70€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1388 | +0.007 | +0.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1388 | +0.007 | +0.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 75029 | -0.072 | +1755.42€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 75029 | -0.072 | +1755.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 12697 | -0.079 | +735.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 12697 | -0.079 | +735.87€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 11556 | -0.092 | -507.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 11556 | -0.092 | -507.68€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 12926 | -0.067 | +730.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 12926 | -0.067 | +730.36€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 11083 | -0.093 | -202.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 11083 | -0.093 | -202.59€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 13737 | -0.048 | +387.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 13737 | -0.048 | +387.61€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 13030 | -0.062 | +611.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 13030 | -0.062 | +611.85€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7634 | -0.025 | -123.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7634 | -0.025 | -123.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1697 | -0.030 | -8.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1697 | -0.030 | -8.68€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2157 | -0.019 | -25.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2157 | -0.019 | -25.07€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1043 | -0.041 | -15.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1043 | -0.041 | -15.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 738 | -0.020 | -23.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 738 | -0.020 | -23.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 1146 | +0.105 | +376.23€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#5min | 1010 | +0.112 | +363.64€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 234 | +0.136 | +114.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 234 | +0.136 | +114.86€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 195 | +0.089 | +42.34€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 195 | +0.089 | +42.34€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 207 | +0.098 | +70.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 207 | +0.098 | +70.66€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 177 | +0.131 | +80.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 177 | +0.131 | +80.23€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 197 | +0.098 | +55.55€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 197 | +0.098 | +55.55€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 513 | -0.065 | -65.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 513 | -0.065 | -65.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 111 | -0.004 | +2.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 111 | -0.004 | +2.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 62 | -0.156 | -21.51€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 62 | -0.156 | -21.51€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 152 | -0.084 | -30.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 152 | -0.084 | -30.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 106 | -0.009 | -0.29€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 106 | -0.009 | -0.29€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 82 | -0.107 | -16.21€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 82 | -0.107 | -16.21€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 580 | -0.105 | -47.18€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 266 | -0.157 | -63.24€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 218 | -0.200 | -65.93€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 48 | +0.040 | +2.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 202 | -0.073 | +0.73€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 158 | -0.081 | -7.42€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 44 | -0.043 | +8.15€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 112 | -0.035 | +15.33€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 90 | -0.054 | +8.64€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 22 | +0.042 | +6.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 466 | -0.133 | -64.70€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 114 | +0.009 | +17.52€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 728 | -0.204 | -31.94€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 300 | -0.202 | -28.59€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 263 | -0.198 | -28.19€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 37 | -0.218 | -0.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 250 | -0.218 | -22.59€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 218 | -0.227 | -27.25€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 32 | -0.147 | +4.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 178 | -0.183 | +19.24€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 162 | -0.183 | +14.57€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 16 | -0.133 | +4.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 643 | -0.205 | -40.88€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 85 | -0.190 | +8.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 295 | +0.402 | +218.00€ | 0 | 13 |
| ✅ RESOLUTION_SNIPER#BTC | 29 | +0.048 | -4.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 29 | +0.048 | -4.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 79 | +0.377 | +58.79€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 79 | +0.377 | +58.79€ | 0 | 6 |
| ✅ RESOLUTION_SNIPER#SOL | 187 | +0.463 | +163.44€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 187 | +0.463 | +163.44€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 295 | +0.402 | +218.00€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 519 | +0.037 | +20.51€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 519 | +0.037 | +20.51€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 248 | +0.036 | +6.41€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 248 | +0.036 | +6.41€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 36 | +0.079 | +2.09€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 36 | +0.079 | +2.09€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 55 | +0.009 | -0.51€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 55 | +0.009 | -0.51€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 180 | +0.038 | +12.53€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 180 | +0.038 | +12.53€ | 1 | 3 |
| ✅ STREAK_FADE_5M | 2800 | -0.022 | -114.32€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2800 | -0.022 | -114.32€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 809 | -0.017 | -25.36€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 809 | -0.017 | -25.36€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 570 | -0.023 | -23.26€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 570 | -0.023 | -23.26€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 155 | -0.048 | -14.93€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 155 | -0.048 | -14.93€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1266 | -0.022 | -50.78€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1266 | -0.022 | -50.78€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 75 | -0.058 | -7.51€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 75 | -0.058 | -7.51€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 37 | -0.013 | -3.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 37 | -0.013 | -3.07€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 7914 | +0.024 | +127.23€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 7914 | +0.024 | +127.23€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2145 | +0.022 | +23.96€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2145 | +0.022 | +23.96€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1798 | +0.037 | +56.80€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1798 | +0.037 | +56.80€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2413 | +0.014 | +9.41€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2413 | +0.014 | +9.41€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1558 | +0.028 | +37.06€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1558 | +0.028 | +37.06€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 7442 | +0.014 | -28.35€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 7442 | +0.014 | -28.35€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2989 | +0.018 | -1.38€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2989 | +0.018 | -1.38€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2905 | +0.014 | -13.31€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2905 | +0.014 | -13.31€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1548 | +0.006 | -13.66€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1548 | +0.006 | -13.66€ | 2 | 0 |
| ✅ UPDOWN_GBM | 38480 | +0.031 | +2317.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 10461 | +0.069 | +1894.39€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 1418 | +0.004 | +6.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 24096 | +0.020 | +395.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2357 | +0.004 | +22.85€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 4011 | +0.068 | +451.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 732 | +0.154 | +299.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 32 | +0.000 | -0.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 3247 | +0.049 | +152.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 7150 | +0.038 | +508.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1323 | +0.083 | +295.71€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 381 | +0.020 | +7.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 4331 | +0.036 | +179.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1058 | +0.003 | +23.94€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 57 | -0.093 | +1.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 4548 | +0.040 | +281.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 679 | +0.137 | +236.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 28 | +0.000 | -1.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 3841 | +0.023 | +46.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 8158 | +0.018 | +285.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 2666 | +0.046 | +268.60€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 372 | +0.005 | +6.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 4274 | +0.007 | +12.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 798 | +0.000 | -6.33€ | 2 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 48 | -0.140 | +3.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 8994 | +0.014 | +216.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2513 | +0.027 | +173.69€ | 0 | 12 |
| ✅ UPDOWN_GBM#SOL#240min | 364 | -0.005 | -2.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 5575 | +0.011 | +43.15€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 501 | +0.013 | +5.24€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 41 | -0.174 | -3.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 5617 | +0.035 | +576.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2548 | +0.082 | +620.32€ | 0 | 13 |
| ✅ UPDOWN_GBM#XRP#240min | 241 | -0.006 | -4.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 2828 | -0.004 | -39.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 146 | -0.135 | +0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 560 | +0.342 | +170.68€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 560 | +0.342 | +170.68€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 310 | +0.346 | +91.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 310 | +0.346 | +91.55€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 250 | +0.333 | +79.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 250 | +0.333 | +79.14€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 12291 | -0.038 | +2572.83€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 12291 | -0.038 | +2572.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 821 | -0.041 | +362.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 821 | -0.041 | +362.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2257 | -0.123 | +5.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2257 | -0.123 | +5.72€ | 4 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 428 | +0.174 | +276.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 428 | +0.174 | +276.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1363 | +0.207 | +801.90€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1363 | +0.207 | +801.90€ | 2 | 23 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 3698 | -0.064 | +546.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 3698 | -0.064 | +546.74€ | 2 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 3724 | -0.075 | +579.50€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 3724 | -0.075 | +579.50€ | 4 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 145 | +0.037 | +8.71€ | 2 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 145 | +0.037 | +8.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 145 | +0.037 | +8.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 145 | +0.037 | +8.71€ | 2 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 897 | +0.293 | +723.36€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 897 | +0.293 | +723.36€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 494 | +0.288 | +380.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 494 | +0.288 | +380.17€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 403 | +0.297 | +343.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 403 | +0.297 | +343.19€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 729 | -0.113 | -85.64€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 729 | -0.113 | -85.64€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 212 | -0.084 | -16.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 212 | -0.084 | -16.31€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 70 | -0.167 | -9.32€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 70 | -0.167 | -9.32€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 68 | -0.200 | -9.95€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 68 | -0.200 | -9.95€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 34 | -0.194 | -7.31€ | 4 | 0 |
| ✅ WEEKLY_PRICE | 2432 | +0.300 | +1226.96€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 839 | +0.249 | +117.57€ | 0 | 5 |
| ✅ WEEKLY_PRICE#ETH | 915 | +0.289 | +398.68€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 678 | +0.377 | +710.71€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.017 n=507 — no justifica filtro, seguir monitorizando
  - _Datos_: n=507 IC=+0.017 PNL=+20.68€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 533 celda(s) pasan gate riguroso completo de 2259 evaluadas (n>=40) y 3230 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.026 < 0.08 — monitorear
  - _Datos_: n=2510 IC=+0.026 PNL=+171.89€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=915/15 IC=+0.289 PNL=+398.68€ | BTC: n=839/15 IC=+0.249 PNL=+117.57€ | SOL: n=678/15 IC=+0.377 PNL=+710.71€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.111 n=335/60 | contraria IC=+0.148 n=319 | gap=-0.037 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=296, boost estimado=+0.003. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=797/40 IC=+0.001 PNL=-5.82€ | BTC#60min: n=1056/40 IC=+0.003 PNL=+24.06€ | SOL#60min: n=500/40 IC=+0.014 PNL=+5.75€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.050 n=343101 | tras_1loss IC=+0.079 n=266757 | tras_2loss IC=+0.049 n=112302/40 | gap=+0.001 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.181 > 0.08 con n=333 PNL=+210.09€
  - _Datos_: n=333 IC=+0.181 PNL=+210.09€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.214 > 0.08 con n=393 PNL=+286.36€
  - _Datos_: n=393 IC=+0.214 PNL=+286.36€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.244 > 0.08 con n=41 PNL=+31.47€
  - _Datos_: n=41 IC=+0.244 PNL=+31.47€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.328 > 0.1 con n=1991 PNL=+1118.21€
  - _Datos_: n=1991 IC=+0.328 PNL=+1118.21€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=292 IC=+0.075 PNL=+34.52€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=292 IC=+0.075 PNL=+34.52€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=51 IC=+0.198 PNL=+36.17€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=51 IC=+0.198 PNL=+36.17€

**⏳ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: 30
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 3/15 ops en el filtro definido (IC actual=+0.045 PNL=+5.14€)
  - _Datos_: n=3 IC=+0.045 PNL=+5.14€

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
  - _Estado_: n=1652 IC=+0.013 PNL=+12.13€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1652 IC=+0.013 PNL=+12.13€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=701 IC=-0.015 PNL=+11.86€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=701 IC=-0.015 PNL=+11.86€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=507 IC=+0.017 PNL=+20.68€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=507 IC=+0.017 PNL=+20.68€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.186 > 0.1 con n=2218 PNL=+1373.03€
  - _Datos_: n=2218 IC=+0.186 PNL=+1373.03€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1321 IC=+0.083 PNL=+295.67€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1321 IC=+0.083 PNL=+295.67€

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
  - _Estado_: n=552 IC=+0.018 PNL=+39.44€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=552 IC=+0.018 PNL=+39.44€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=53 IC=+0.082 PNL=+5.09€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=53 IC=+0.082 PNL=+5.09€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.260 n=102) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=102 IC=+0.260 PNL=+85.53€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.118 > 0.02 con n=645 PNL=+238.56€
  - _Datos_: n=645 IC=+0.118 PNL=+238.56€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=147 IC=-0.044 PNL=+35.89€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=147 IC=-0.044 PNL=+35.89€

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
  - _Estado_: n=13492 IC=+0.054 PNL=+1625.38€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=13492 IC=+0.054 PNL=+1625.38€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.160 < -0.1 con n=239 PNL=+21.62€
  - _Datos_: n=239 IC=-0.160 PNL=+21.62€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=1963 IC=+0.051 PNL=+210.25€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1963 IC=+0.051 PNL=+210.25€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=80 IC=-0.122 PNL=+3.66€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=80 IC=-0.122 PNL=+3.66€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.130 > 0.1 con n=428 PNL=+130.95€
  - _Datos_: n=428 IC=+0.130 PNL=+130.95€

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
  - _Estado_: n=18437 IC=-0.137 PNL=+1267.53€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=18437 IC=-0.137 PNL=+1267.53€

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
  - _Estado_: n=1986 IC=+0.141 PNL=+1091.58€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1986 IC=+0.141 PNL=+1091.58€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=4042 IC=+0.021 PNL=+140.29€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4042 IC=+0.021 PNL=+140.29€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.086 > 0.08 con n=2116 PNL=+1091.44€
  - _Datos_: n=2116 IC=+0.086 PNL=+1091.44€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.237 < -0.1 con n=1796 PNL=-200.28€
  - _Datos_: n=1796 IC=-0.237 PNL=-200.28€

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

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 37/40 ops en el filtro definido (IC actual=-0.013 PNL=+3.98€)
  - _Datos_: n=37 IC=-0.013 PNL=+3.98€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.100 n=1030) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1030 IC=+0.100 PNL=+247.72€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.411 n=446) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=446 IC=+0.411 PNL=+628.68€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=8976 IC=+0.176 PNL=-1040.42€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=8976 IC=+0.176 PNL=-1040.42€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.205 > 0.1 con n=137 PNL=+83.62€
  - _Datos_: n=137 IC=+0.205 PNL=+83.62€
