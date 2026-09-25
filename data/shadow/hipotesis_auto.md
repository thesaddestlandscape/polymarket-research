# Hipótesis automáticas — 2026-09-25 06:48 UTC
_Generado por shadow_postmortem.py sobre 600756 resoluciones (PNL=+67892.64€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=493)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.122 (n=493)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.495 (IC base=+0.050)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.146 (n=176)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 94.0 (IC base=+0.050)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.134 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.258 (n=420)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=360)

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

- **PATRÓN** `ballena_activa_n` < `95.0` → IC=+0.155 (n=137)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 95.0 (IC base=+0.051)

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
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=90)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.177 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=90)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=103)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.250 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.55 (IC base=+0.110)

- **PATRÓN** `banda_hit_calibrado` > `0.6297` → IC=+0.239 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6297 (IC base=+0.110)

- **PATRÓN** `banda_z` > `8.424` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `banda_z` > 8.424 (IC base=+0.110)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.170 (n=107)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.02 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `1195.1095` → IC=+0.167 (n=67)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 1195.1095 (IC base=+0.110)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.129 (n=87)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` < 0.495 (IC base=-0.004)

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
- **FILTRO** `restante_s_al_confirmar` < `146.02` → IC=-0.231 (n=7103)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.02
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=21316)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `138.17` → IC=-0.249 (n=931)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 138.17
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=2795)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` < `500.19` → IC=-0.149 (n=366)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 500.19
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=1101)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `125.44` → IC=-0.307 (n=869)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.44
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=2610)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `165.09` → IC=-0.218 (n=1716)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 165.09
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=5149)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `126.74` → IC=-0.354 (n=1398)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 126.74
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=4196)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.204 (n=13926)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=3514)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `5649.2316` → IC=+0.177 (n=2237)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 5649.2316 (IC base=+0.101)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.138 (n=11570)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.136 (n=14069)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.231 (n=10963)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.174 (n=5688)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `7826.0587` → IC=+0.175 (n=2150)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 7826.0587 (IC base=+0.127)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.211 (n=1732)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.206 (n=1699)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.351 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=2139)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `16024.1962` → IC=+0.242 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16024.1962 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.205 (n=1528)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.207 (n=1698)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.264 (n=1548)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=2175)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `15869.986` → IC=+0.214 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15869.986 (IC base=+0.202)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.615` → IC=+0.170 (n=328)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.615 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `4624.034` → IC=+0.147 (n=236)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 4624.034 (IC base=+0.101)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.143 (n=357)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 7.0 (IC base=+0.107)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.144 (n=825)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.44 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.126 (n=557)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `5859.5725` → IC=+0.162 (n=220)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 5859.5725 (IC base=+0.107)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.154 (n=2826)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.146 (n=2412)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 15.0 (IC base=+0.145)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.338 (n=967)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.249 (n=533)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `py_entrada` < `0.26` → IC=+0.358 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.26 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.236 (n=1490)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.233)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.157 (n=462)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 11.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.139 (n=666)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 17.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.237 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.150 (n=547)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `1302.9991` → IC=+0.149 (n=662)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1302.9991 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.070)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.231 (n=709)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.207)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.433 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.162 (n=1091)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 7.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.163 (n=589)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 7.0 (IC base=+0.160)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.316 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.160)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.172 (n=729)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.160)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.173 (n=307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 7.0 (IC base=+0.162)

- **PATRÓN** `py_entrada` > `0.743` → IC=+0.356 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.743 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.163 (n=188)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.02 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `1244.5613` → IC=+0.152 (n=228)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1244.5613 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.146 (n=312)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.112)

- **PATRÓN** `py_entrada` < `0.355` → IC=+0.197 (n=387)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.355 (IC base=+0.112)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.8` → IC=-0.333 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=131)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=11545)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.199 (n=11064)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.226 (n=3819)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.339 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `8491.3442` → IC=+0.342 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8491.3442 (IC base=+0.197)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=2795)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.174 (n=2660)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 17.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.181 (n=1955)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.71 (IC base=+0.167)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.246 (n=855)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.245 (n=856)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.241)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.353 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.241)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=2754)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.184 (n=2634)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=2261)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.249 (n=2433)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.239)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.321 (n=866)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.239)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.199 (n=2667)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.193 (n=2574)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 17.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.195 (n=1984)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.71 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.192 (n=1030)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.73 (IC base=+0.191)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.441 (n=503)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.430)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.430 (n=472)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.430)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.440 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.430)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.430)

- **PATRÓN** `libro_liquidez` > `2077.5174` → IC=+0.439 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2077.5174 (IC base=+0.430)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.439 (n=212)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.438)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.438 (n=208)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.451 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

- **PATRÓN** `libro_liquidez` > `19064.2752` → IC=+0.443 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 19064.2752 (IC base=+0.438)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.450 (n=178)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.472 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.436)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.436 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.436)

- **PATRÓN** `libro_liquidez` > `3369.9988` → IC=+0.447 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3369.9988 (IC base=+0.436)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.406 (n=105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.405)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.406 (n=105)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.405)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.419 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.405)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.408 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.405)

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

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.201 (n=34306)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.236 (n=15341)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.177 (n=6977)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.180 (n=4773)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 12.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.191 (n=6421)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.225 (n=6150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.224 (n=6153)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.274 (n=2189)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.179 (n=3310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 15.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.189 (n=6256)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.172)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.233 (n=3099)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.267 (n=2120)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.210 (n=5681)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.257 (n=2291)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=6773)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=5737)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.252 (n=2176)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=5235)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.118)

- **PATRÓN** `restante_min` < `4.16` → IC=+0.127 (n=4860)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.16 (IC base=+0.118)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.139 (n=5268)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.95 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.131 (n=6445)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.118)

- **PATRÓN** `lag_apertura_s` < `2.79` → IC=+0.140 (n=4832)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.79 (IC base=+0.118)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.198 (n=2637)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.38 (IC base=+0.122)

- **PATRÓN** `restante_min` < `4.11` → IC=+0.131 (n=2397)

  - _Acción_: Kelly boost +0.65€ cuando `restante_min` < 4.11 (IC base=+0.122)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.140 (n=2616)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.94 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.140 (n=3182)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 7.0 (IC base=+0.122)

- **PATRÓN** `lag_apertura_s` < `3.37` → IC=+0.143 (n=2400)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 3.37 (IC base=+0.122)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.189 (n=2598)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.113)

- **PATRÓN** `restante_min` < `4.19` → IC=+0.126 (n=2439)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.19 (IC base=+0.113)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.135 (n=2658)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.96 (IC base=+0.113)

- **PATRÓN** `lag_apertura_s` < `2.29` → IC=+0.139 (n=2444)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.29 (IC base=+0.113)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.321 (n=791)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.290)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.381 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `4103.5959` → IC=+0.307 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4103.5959 (IC base=+0.290)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.301 (n=345)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.276)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.331 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.276)

- **PATRÓN** `libro_liquidez` > `4263.4949` → IC=+0.298 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4263.4949 (IC base=+0.276)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.333 (n=376)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.298 (n=558)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.393 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `1451.8749` → IC=+0.308 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1451.8749 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.344 (n=75)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.339)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.367 (n=73)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.339)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.384 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.339)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.344 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.339)

- **PATRÓN** `libro_liquidez` > `761.0655` → IC=+0.368 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 761.0655 (IC base=+0.339)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.443 (n=436)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.437)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.440 (n=432)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.440 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.438 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.437)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.441 (n=236)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.441 (n=236)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.440 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.447 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.435)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.451 (n=80)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.451 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.441 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.440)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.441 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.440)

- **PATRÓN** `libro_liquidez` > `1987.6172` → IC=+0.462 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1987.6172 (IC base=+0.440)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` > `13.0` → IC=+0.375 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.389)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.385 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.389)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.426 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.389)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `hora_utc` > `15.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=54)

- **FILTRO** `py_entrada` > `0.785` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.785
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=54)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.305 (n=208)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.258)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.315 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.269 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1367.6878` → IC=+0.290 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1367.6878 (IC base=+0.258)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=54)

- **FILTRO** `py_entrada` > `0.785` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.785
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=54)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.305 (n=208)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.258)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.315 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.269 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1367.6878` → IC=+0.290 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1367.6878 (IC base=+0.258)

### GBM_LATE_15M
- **PATRÓN** `drift_60min` |x|≤ `0.4859` → IC=+0.122 (n=8143)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.61€ cuando `drift_60min` |x|≤ 0.4859 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.9829` → IC=+0.244 (n=2714)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9829 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.846` → IC=+0.248 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.846 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` < `0.6359` → IC=+0.248 (n=2302)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6359 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.342` → IC=+0.186 (n=2152)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 8.342 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` < `1.2084` → IC=+0.247 (n=2209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2084 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` > `1.0443` → IC=+0.258 (n=1001)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0443 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` > `0.3037` → IC=+0.221 (n=816)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3037 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` > `1.4631` → IC=+0.202 (n=5587)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4631 (IC base=+0.105)

- **PATRÓN** `ibs_20min` < `0.5703` → IC=+0.135 (n=9812)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.5703 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.6162` → IC=+0.200 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6162 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` < `0.1546` → IC=+0.174 (n=3110)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.1546 (IC base=+0.066)

- **PATRÓN** `volumen_regimen` < `0.697` → IC=+0.184 (n=1513)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.697 (IC base=+0.066)

- **PATRÓN** `volumen_regimen` > `1.052` → IC=+0.176 (n=1559)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.052 (IC base=+0.066)

- **PATRÓN** `volumen_pendiente_norm` > `0.1673` → IC=+0.226 (n=1640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1673 (IC base=+0.066)

- **PATRÓN** `volumen_spike_ratio` > `1.5705` → IC=+0.203 (n=5177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5705 (IC base=+0.066)

- **PATRÓN** `ballena_activa_n` < `135.0` → IC=+0.212 (n=5584)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 135.0 (IC base=+0.066)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.176 (n=616)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.005 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.175 (n=614)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0082 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.3503` → IC=+0.166 (n=1837)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3503 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.168 (n=886)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 15.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.167 (n=1238)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 11.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.272 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.116` → IC=+0.269 (n=789)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.116 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.208 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `1.4361` → IC=+0.164 (n=1719)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.4361 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.249 (n=1243)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.0923` → IC=+0.275 (n=464)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0923 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.244 (n=1254)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.0549` → IC=+0.295 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0549 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.484` → IC=+0.239 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.484 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.444` → IC=+0.247 (n=1444)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.444 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` < `0.0922` → IC=+0.232 (n=1194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0922 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2782` → IC=+0.265 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2782 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.6178` → IC=+0.243 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6178 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `1807.2648` → IC=+0.236 (n=926)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1807.2648 (IC base=+0.236)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.231 (n=618)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.0846` → IC=+0.247 (n=469)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0846 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=1470)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.9037` → IC=+0.264 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9037 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `0.2069` → IC=+0.218 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2069 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` < `0.5771` → IC=+0.219 (n=1470)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5771 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.76` → IC=+0.261 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.76 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` < `1.2525` → IC=+0.219 (n=1405)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2525 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `0.6211` → IC=+0.219 (n=1404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6211 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.245 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `1.7485` → IC=+0.216 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7485 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `2.3672` → IC=+0.231 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3672 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `12494.7244` → IC=+0.218 (n=1255)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12494.7244 (IC base=+0.216)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.178 (n=488)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0026 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.077` → IC=+0.164 (n=489)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.077 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=576)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.146 (n=661)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 7.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.6944` → IC=+0.173 (n=1462)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.6944 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.1331` → IC=+0.158 (n=1303)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1331 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.254` → IC=+0.161 (n=234)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.254 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.282` → IC=+0.145 (n=1332)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.282 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.2035` → IC=+0.152 (n=1462)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.2035 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.1566` → IC=+0.178 (n=386)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1566 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.4267` → IC=+0.154 (n=1352)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4267 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.4188` → IC=+0.151 (n=1352)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.4188 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `14091.9548` → IC=+0.146 (n=975)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 14091.9548 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `410.0` → IC=+0.150 (n=1270)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 410.0 (IC base=+0.141)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.209 (n=603)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=1895)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.190 (n=1618)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.264 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.184` → IC=+0.250 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.184 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` < `0.2104` → IC=+0.186 (n=1811)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.2104 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.3587` → IC=+0.201 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3587 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `2.8331` → IC=+0.203 (n=780)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8331 (IC base=+0.185)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.193 (n=1290)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.185)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.223 (n=1368)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.6053` → IC=+0.215 (n=1554)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6053 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.248 (n=590)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.217 (n=732)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.0637` → IC=+0.248 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0637 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.635` → IC=+0.239 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.635 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.3553` → IC=+0.270 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3553 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.7663` → IC=+0.204 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7663 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.2024` → IC=+0.221 (n=949)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2024 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.217 (n=1055)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `1894.7532` → IC=+0.223 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1894.7532 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.217 (n=930)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.212)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.150 (n=101)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=2233)

- **PATRÓN** `ibs_20min` > `0.9436` → IC=+0.214 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9436 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.7929` → IC=+0.332 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7929 (IC base=+0.025)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.74` → IC=+0.160 (n=718)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.74 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `0.8561` → IC=+0.325 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8561 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `1.2004` → IC=+0.341 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2004 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.3004` → IC=+0.348 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3004 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.4081` → IC=+0.344 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4081 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` > `2.2012` → IC=+0.330 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2012 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `161.0` → IC=+0.329 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 161.0 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.68` → IC=+0.201 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.68 (IC base=+0.019)

- **PATRÓN** `volumen_regimen` < `0.8475` → IC=+0.166 (n=563)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8475 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.225 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` > `1.518` → IC=+0.177 (n=707)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.518 (IC base=+0.019)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.177 (n=60)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=328)

- **FILTRO** `ibs_20min` < `0.28` → IC=-0.207 (n=97)

  - _Acción_: SKIP cuando `ibs_20min` < 0.28
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=291)

- **FILTRO** `ibs_20min` > `0.25` → IC=-0.124 (n=2207)

  - _Acción_: SKIP cuando `ibs_20min` > 0.25
  - _Potencial_: sin este filtro IC_bueno=+0.126 (n=1088)

- **FILTRO** `sigma_ewma_delta_pct` > `8.683` → IC=-0.208 (n=354)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.683
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2941)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.184 (n=194)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.6 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` > `1.7756` → IC=+0.333 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.7756 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` < `0.5952` → IC=+0.274 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5952 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` > `0.7776` → IC=+0.297 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7776 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` < `0.0735` → IC=+0.310 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0735 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` < `1.7487` → IC=+0.297 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7487 (IC base=+0.046)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.300 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.046)

- **PATRÓN** `ibs_20min` < `0.25` → IC=+0.126 (n=1088)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.25 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.7042` → IC=+0.246 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7042 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` < `0.9446` → IC=+0.217 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9446 (IC base=-0.042)

- **PATRÓN** `volumen_regimen` < `0.7131` → IC=+0.241 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7131 (IC base=-0.042)

- **PATRÓN** `volumen_regimen` > `0.9017` → IC=+0.220 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9017 (IC base=-0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.157` → IC=+0.261 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.157 (IC base=-0.042)

- **PATRÓN** `volumen_spike_ratio` < `2.43` → IC=+0.266 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.43 (IC base=-0.042)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6576` → IC=-0.183 (n=573)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6576
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=1720)

- **FILTRO** `ibs_20min` < `0.7168` → IC=-0.154 (n=1513)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7168
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=780)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.201 (n=416)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=1877)

- **FILTRO** `ibs_20min` > `0.77` → IC=-0.203 (n=837)

  - _Acción_: SKIP cuando `ibs_20min` > 0.77
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=2528)

- **PATRÓN** `dist_vwap_pct` > `0.4581` → IC=+0.307 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4581 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` < `0.2747` → IC=+0.310 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2747 (IC base=-0.066)

- **PATRÓN** `volumen_regimen` < `0.9775` → IC=+0.285 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9775 (IC base=-0.066)

- **PATRÓN** `volumen_regimen` > `0.6166` → IC=+0.300 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6166 (IC base=-0.066)

- **PATRÓN** `volumen_pendiente_norm` < `0.1011` → IC=+0.293 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1011 (IC base=-0.066)

- **PATRÓN** `volumen_spike_ratio` < `2.1123` → IC=+0.291 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1123 (IC base=-0.066)

- **PATRÓN** `volumen_spike_ratio` > `1.7999` → IC=+0.289 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7999 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` > `0.9096` → IC=+0.272 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9096 (IC base=-0.022)

- **PATRÓN** `volumen_regimen` < `0.7351` → IC=+0.252 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7351 (IC base=-0.022)

- **PATRÓN** `volumen_regimen` > `1.2596` → IC=+0.284 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2596 (IC base=-0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.1027` → IC=+0.277 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1027 (IC base=-0.022)

- **PATRÓN** `volumen_spike_ratio` < `2.1456` → IC=+0.256 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1456 (IC base=-0.022)

- **PATRÓN** `volumen_spike_ratio` > `1.5272` → IC=+0.248 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5272 (IC base=-0.022)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.197 (n=3407)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0098 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.4762` → IC=+0.189 (n=9127)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4762 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.7682` → IC=+0.289 (n=1081)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7682 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.606` → IC=+0.157 (n=4804)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.606 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` > `0.6889` → IC=+0.248 (n=3252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6889 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.2946` → IC=+0.268 (n=866)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2946 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `1.4655` → IC=+0.239 (n=1971)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4655 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` > `2.6638` → IC=+0.242 (n=1970)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6638 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `97.0` → IC=+0.267 (n=5428)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 97.0 (IC base=+0.098)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.157 (n=3394)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0091 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.5476` → IC=+0.155 (n=8949)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.5476 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.7308` → IC=+0.241 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7308 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.2514` → IC=+0.240 (n=2839)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2514 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.7084` → IC=+0.242 (n=1321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7084 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.2035` → IC=+0.248 (n=1000)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2035 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2441` → IC=+0.303 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2441 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.6028` → IC=+0.262 (n=1744)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6028 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.3111` → IC=+0.258 (n=1796)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3111 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `84.0` → IC=+0.265 (n=3845)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 84.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `4.525` → IC=-0.157 (n=538)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.525
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1807)

- **PATRÓN** `ibs_20min` > `0.8935` → IC=+0.268 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8935 (IC base=+0.045)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.787` → IC=+0.207 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.787 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.2236` → IC=+0.268 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2236 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` < `1.433` → IC=+0.173 (n=298)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.433 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` > `2.1457` → IC=+0.198 (n=405)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.1457 (IC base=+0.045)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.179 (n=400)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 14.0 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` < `0.1845` → IC=+0.452 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1845 (IC base=-0.016)

- **PATRÓN** `volumen_spike_ratio` < `2.5496` → IC=+0.441 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5496 (IC base=-0.016)

- **PATRÓN** `volumen_spike_ratio` > `2.2378` → IC=+0.438 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2378 (IC base=-0.016)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.471 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=-0.016)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.86` → IC=+0.158 (n=683)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.86 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.3135` → IC=+0.177 (n=379)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.3135 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `0.6718` → IC=+0.168 (n=843)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 0.6718 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.2725` → IC=+0.230 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2725 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.4247` → IC=+0.197 (n=308)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4247 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `244.0` → IC=+0.194 (n=403)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 244.0 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.1614` → IC=+0.222 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1614 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` > `0.6101` → IC=+0.216 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6101 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.272` → IC=+0.309 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.272 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.4443` → IC=+0.225 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4443 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.1554` → IC=+0.240 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1554 (IC base=+0.005)

- **PATRÓN** `ballena_activa_n` < `468.0` → IC=+0.216 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 468.0 (IC base=+0.005)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.287 (n=538)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.248 (n=1691)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.248 (n=1435)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=855)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.691` → IC=+0.280 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.691 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` < `0.104` → IC=+0.258 (n=1367)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.104 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `3.4171` → IC=+0.263 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.4171 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.254 (n=1139)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `1961.8084` → IC=+0.248 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1961.8084 (IC base=+0.245)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.319 (n=585)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.6107` → IC=+0.284 (n=1288)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6107 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.330 (n=438)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.283)

- **PATRÓN** `ibs_20min` < `0.2233` → IC=+0.290 (n=1134)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2233 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.808` → IC=+0.296 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.808 (IC base=+0.283)

- **PATRÓN** `volumen_pendiente_norm` > `0.3423` → IC=+0.311 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3423 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` < `1.5928` → IC=+0.285 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5928 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` > `2.7396` → IC=+0.288 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7396 (IC base=+0.283)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.287 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `1882.9554` → IC=+0.299 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1882.9554 (IC base=+0.283)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.288 (n=767)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 28.0 (IC base=+0.283)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.2878` → IC=-0.185 (n=499)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2878
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=1500)

- **FILTRO** `ibs_20min` > `0.7745` → IC=-0.187 (n=602)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7745
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=1809)

- **PATRÓN** `ibs_20min` > `0.822` → IC=+0.158 (n=682)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.822 (IC base=+0.013)

- **PATRÓN** `dist_vwap_pct` > `0.4514` → IC=+0.224 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4514 (IC base=+0.013)

- **PATRÓN** `dist_vwap_pct` < `0.7044` → IC=+0.212 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7044 (IC base=+0.013)

- **PATRÓN** `volumen_regimen` < `0.9865` → IC=+0.238 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9865 (IC base=+0.013)

- **PATRÓN** `volumen_regimen` > `0.5875` → IC=+0.212 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5875 (IC base=+0.013)

- **PATRÓN** `volumen_pendiente_norm` > `0.1657` → IC=+0.264 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1657 (IC base=+0.013)

- **PATRÓN** `volumen_spike_ratio` < `1.5105` → IC=+0.264 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5105 (IC base=+0.013)

- **PATRÓN** `ballena_activa_n` < `149.0` → IC=+0.244 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 149.0 (IC base=+0.013)

- **PATRÓN** `dist_vwap_pct` > `0.1547` → IC=+0.211 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1547 (IC base=-0.005)

- **PATRÓN** `dist_vwap_pct` < `0.6852` → IC=+0.202 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6852 (IC base=-0.005)

- **PATRÓN** `volumen_regimen` < `1.1615` → IC=+0.212 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1615 (IC base=-0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.289 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.8248` → IC=+0.265 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8248 (IC base=-0.005)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.249 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 139.0 (IC base=-0.005)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7255` → IC=-0.196 (n=1082)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7255
  - _Potencial_: sin este filtro IC_bueno=+0.281 (n=1082)

- **FILTRO** `ibs_20min` > `0.6857` → IC=-0.232 (n=561)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6857
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=1684)

- **FILTRO** `sigma_ewma_delta_pct` > `4.705` → IC=-0.182 (n=489)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.705
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=1756)

- **PATRÓN** `ibs_20min` > `0.7255` → IC=+0.281 (n=1082)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7255 (IC base=+0.043)

- **PATRÓN** `dist_vwap_pct` > `0.8494` → IC=+0.339 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8494 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.606` → IC=+0.167 (n=343)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.606 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` < `0.8667` → IC=+0.306 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8667 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` > `0.7299` → IC=+0.295 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7299 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` < `0.1024` → IC=+0.293 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1024 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2245` → IC=+0.303 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2245 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.4185` → IC=+0.328 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4185 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.315 (n=678)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.043)

- **PATRÓN** `ibs_20min` < `0.5789` → IC=+0.121 (n=1482)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.5789 (IC base=+0.015)

- **PATRÓN** `dist_vwap_pct` < `0.2149` → IC=+0.221 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2149 (IC base=+0.015)

- **PATRÓN** `volumen_regimen` < `0.7067` → IC=+0.249 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7067 (IC base=+0.015)

- **PATRÓN** `volumen_pendiente_norm` < `0.0972` → IC=+0.212 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0972 (IC base=+0.015)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.213 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.015)

- **PATRÓN** `volumen_spike_ratio` < `2.481` → IC=+0.223 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.481 (IC base=+0.015)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.232 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=+0.015)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0168` → IC=+0.316 (n=883)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0168 (IC base=+0.276)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.284 (n=1389)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.276)

- **PATRÓN** `ibs_20min` > `0.74` → IC=+0.322 (n=1184)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.74 (IC base=+0.276)

- **PATRÓN** `dist_vwap_pct` > `0.2108` → IC=+0.316 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2108 (IC base=+0.276)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.566` → IC=+0.300 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.566 (IC base=+0.276)

- **PATRÓN** `volumen_regimen` > `0.8606` → IC=+0.300 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8606 (IC base=+0.276)

- **PATRÓN** `volumen_pendiente_norm` > `0.2809` → IC=+0.324 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2809 (IC base=+0.276)

- **PATRÓN** `volumen_spike_ratio` > `2.1481` → IC=+0.295 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1481 (IC base=+0.276)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.282 (n=1420)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.276)

- **PATRÓN** `libro_liquidez` > `2631.3944` → IC=+0.290 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2631.3944 (IC base=+0.276)

- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.301 (n=951)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.273)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.284 (n=493)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.273)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.276 (n=711)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.273)

- **PATRÓN** `ibs_20min` < `0.3925` → IC=+0.306 (n=1426)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3925 (IC base=+0.273)

- **PATRÓN** `dist_vwap_pct` > `0.3068` → IC=+0.282 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3068 (IC base=+0.273)

- **PATRÓN** `dist_vwap_pct` < `0.2261` → IC=+0.273 (n=1289)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2261 (IC base=+0.273)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.484` → IC=+0.290 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.484 (IC base=+0.273)

- **PATRÓN** `volumen_regimen` < `0.6397` → IC=+0.276 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6397 (IC base=+0.273)

- **PATRÓN** `volumen_regimen` > `1.2434` → IC=+0.307 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2434 (IC base=+0.273)

- **PATRÓN** `volumen_pendiente_norm` > `0.2377` → IC=+0.334 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2377 (IC base=+0.273)

- **PATRÓN** `volumen_spike_ratio` < `1.5347` → IC=+0.277 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5347 (IC base=+0.273)

- **PATRÓN** `volumen_spike_ratio` > `2.1456` → IC=+0.275 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1456 (IC base=+0.273)

- **PATRÓN** `libro_liquidez` > `2625.3363` → IC=+0.278 (n=951)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2625.3363 (IC base=+0.273)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.170 (n=2660)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0049 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.202 (n=2652)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.0902` → IC=+0.187 (n=2650)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0902 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=8260)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.5755` → IC=+0.218 (n=7950)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5755 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.1775` → IC=+0.195 (n=3466)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1775 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.347` → IC=+0.254 (n=1628)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.347 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `1.2107` → IC=+0.160 (n=5263)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2107 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `0.6301` → IC=+0.160 (n=5263)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6301 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.2956` → IC=+0.197 (n=1190)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2956 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.559` → IC=+0.167 (n=3356)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.559 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `2.6194` → IC=+0.177 (n=2543)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.6194 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `2403.067` → IC=+0.168 (n=5300)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2403.067 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.180 (n=6864)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 115.0 (IC base=+0.167)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.183 (n=5062)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0066 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.0812` → IC=+0.208 (n=2531)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0812 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=2934)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` < `0.4792` → IC=+0.227 (n=7593)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4792 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.9239` → IC=+0.148 (n=737)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.9239 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` < `0.2343` → IC=+0.158 (n=5508)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.2343 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.348` → IC=+0.197 (n=1287)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.348 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `1.1736` → IC=+0.152 (n=5497)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1736 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.2911` → IC=+0.220 (n=1092)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2911 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.5594` → IC=+0.166 (n=3040)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.5594 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.2529` → IC=+0.171 (n=3132)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.2529 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `116.0` → IC=+0.173 (n=6565)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 116.0 (IC base=+0.168)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.214 (n=452)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.190 (n=614)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0075 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.3426` → IC=+0.206 (n=1354)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3426 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=1422)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.192 (n=909)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.117` → IC=+0.310 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.117 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.234 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `1.4355` → IC=+0.181 (n=1254)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4355 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.240 (n=872)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.251 (n=884)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.1884` → IC=+0.290 (n=659)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1884 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.245 (n=889)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.249 (n=488)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.3437` → IC=+0.266 (n=988)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3437 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.305` → IC=+0.251 (n=1067)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.305 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` < `0.1618` → IC=+0.235 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1618 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.287` → IC=+0.253 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.287 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.4206` → IC=+0.265 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4206 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1808.46` → IC=+0.246 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1808.46 (IC base=+0.239)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.228 (n=398)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.0742` → IC=+0.195 (n=395)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.0742 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=1245)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `0.4049` → IC=+0.227 (n=1183)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4049 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.2122` → IC=+0.213 (n=701)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2122 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.501` → IC=+0.231 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.501 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `1.2593` → IC=+0.163 (n=1183)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2593 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` > `1.0736` → IC=+0.168 (n=537)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 1.0736 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.208 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `1.5024` → IC=+0.181 (n=506)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.5024 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `2.4541` → IC=+0.160 (n=383)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.4541 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `11871.8913` → IC=+0.169 (n=1057)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 11871.8913 (IC base=+0.161)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.158 (n=1291)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0057 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0597` → IC=+0.202 (n=431)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0597 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.179 (n=431)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 18.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.5665` → IC=+0.188 (n=1288)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.5665 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1345` → IC=+0.161 (n=1274)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1345 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.889` → IC=+0.203 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.889 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.2089` → IC=+0.159 (n=1288)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2089 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1558` → IC=+0.156 (n=393)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.1558 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.4411` → IC=+0.147 (n=1176)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4411 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.4202` → IC=+0.138 (n=1176)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.4202 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `215.0` → IC=+0.168 (n=368)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 215.0 (IC base=+0.138)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.222 (n=606)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.2308` → IC=+0.215 (n=889)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2308 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.220 (n=463)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.293 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.876` → IC=+0.271 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.876 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.2074` → IC=+0.201 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2074 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` < `1.6328` → IC=+0.199 (n=423)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.6328 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `2.847` → IC=+0.212 (n=575)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.847 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.207 (n=945)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `1964.9172` → IC=+0.198 (n=445)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 1964.9172 (IC base=+0.198)

- **PATRÓN** `sigma_h` < `0.0114` → IC=+0.232 (n=1108)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0114 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.0968` → IC=+0.248 (n=371)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0968 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.276 (n=387)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` < `0.2405` → IC=+0.256 (n=975)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2405 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.746` → IC=+0.263 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.746 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.3556` → IC=+0.268 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3556 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `1.7747` → IC=+0.212 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7747 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.2184` → IC=+0.228 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2184 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `1894.0152` → IC=+0.221 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1894.0152 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.209 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.218)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.211 (n=424)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.4324` → IC=+0.158 (n=1270)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4324 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=1329)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.375` → IC=+0.197 (n=1270)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.375 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.1608` → IC=+0.180 (n=843)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.1608 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.979` → IC=+0.231 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.979 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.0405` → IC=+0.145 (n=1118)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.0405 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.147 (n=1270)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.6279 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2419` → IC=+0.195 (n=270)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2419 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `1.4249` → IC=+0.155 (n=415)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4249 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `2.5103` → IC=+0.168 (n=414)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.5103 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `6271.1406` → IC=+0.182 (n=847)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 6271.1406 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `163.0` → IC=+0.147 (n=1208)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 163.0 (IC base=+0.143)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.154 (n=1336)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0072 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.3842` → IC=+0.143 (n=1336)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3842 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.179 (n=521)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.6374` → IC=+0.173 (n=1336)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.6374 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.5856` → IC=+0.133 (n=1552)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.5856 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.961` → IC=+0.168 (n=471)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 6.961 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `0.8475` → IC=+0.148 (n=891)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8475 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2919` → IC=+0.197 (n=193)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2919 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.7891` → IC=+0.138 (n=810)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.7891 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `10039.916` → IC=+0.160 (n=606)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 10039.916 (IC base=+0.124)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.158 (n=652)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0101 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=1465)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.5152` → IC=+0.205 (n=1437)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5152 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `0.8449` → IC=+0.217 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8449 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.76` → IC=+0.255 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.76 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.2184` → IC=+0.130 (n=1437)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.2184 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` > `0.6461` → IC=+0.123 (n=1437)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` > 0.6461 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.0711` → IC=+0.125 (n=603)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.0711 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4403` → IC=+0.141 (n=463)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4403 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.127 (n=1501)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2896.4901` → IC=+0.197 (n=652)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2896.4901 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.136 (n=1092)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 49.0 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.155 (n=642)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0061 (IC base=+0.113)

- **PATRÓN** `drift_60min` |x|≤ `0.1034` → IC=+0.158 (n=486)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1034 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.131 (n=1471)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.5652` → IC=+0.209 (n=1457)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5652 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `1.0109` → IC=+0.141 (n=196)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 1.0109 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.2013` → IC=+0.137 (n=1343)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.2013 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.01` → IC=+0.134 (n=233)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 9.01 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `0.6365` → IC=+0.139 (n=486)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.6365 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.2754` → IC=+0.163 (n=179)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.2754 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.4542` → IC=+0.130 (n=436)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.4542 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `2.4248` → IC=+0.130 (n=436)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.4248 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `2170.2079` → IC=+0.145 (n=971)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 2170.2079 (IC base=+0.113)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0188` → IC=+0.213 (n=916)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0188 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.2917` → IC=+0.201 (n=917)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2917 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=1422)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.204 (n=630)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `0.74` → IC=+0.259 (n=1228)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.74 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.5172` → IC=+0.221 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5172 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.578` → IC=+0.241 (n=648)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.578 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `1.2039` → IC=+0.203 (n=1375)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2039 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `0.6239` → IC=+0.211 (n=1374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6239 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.2333` → IC=+0.264 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2333 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `2.1481` → IC=+0.210 (n=1169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1481 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `1.4081` → IC=+0.207 (n=1328)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4081 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.204 (n=1464)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `2826.293` → IC=+0.209 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2826.293 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.0115` → IC=+0.228 (n=624)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0115 (IC base=+0.203)

- **PATRÓN** `sigma_h` > `0.0172` → IC=+0.206 (n=945)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0172 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.0901` → IC=+0.220 (n=473)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0901 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.221 (n=694)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.211 (n=653)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` < `0.4384` → IC=+0.245 (n=1418)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4384 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `1.2584` → IC=+0.233 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2584 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.437` → IC=+0.242 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.437 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.6303` → IC=+0.215 (n=1418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6303 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2821` → IC=+0.288 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2821 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `2.2062` → IC=+0.194 (n=1123)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.2062 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.4361` → IC=+0.199 (n=1275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4361 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2599.2247` → IC=+0.211 (n=945)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2599.2247 (IC base=+0.203)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.163 (n=641)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0039 (IC base=+0.146)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.178 (n=638)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0088 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.1369` → IC=+0.154 (n=842)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1369 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.184 (n=961)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.3875` → IC=+0.180 (n=1912)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.3875 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.8719` → IC=+0.184 (n=305)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.8719 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.703` → IC=+0.173 (n=867)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 3.703 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.8725` → IC=+0.165 (n=1123)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8725 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` > `0.6213` → IC=+0.149 (n=1683)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.6213 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1644` → IC=+0.173 (n=530)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1644 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.4413` → IC=+0.160 (n=615)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.4413 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.5338` → IC=+0.153 (n=615)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.5338 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.150 (n=2173)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.02 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `12439.6953` → IC=+0.158 (n=638)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 12439.6953 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.167 (n=1690)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 158.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.141 (n=1328)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0056 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.124 (n=2003)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 5.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` < `0.6598` → IC=+0.139 (n=1990)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.6598 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` < `0.2152` → IC=+0.122 (n=1770)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.2152 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `0.6982` → IC=+0.125 (n=790)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 0.6982 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `1.4547` → IC=+0.140 (n=639)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4547 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2760.3927` → IC=+0.124 (n=1778)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2760.3927 (IC base=+0.111)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3432` → IC=+0.121 (n=481)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.61€ cuando `drift_60min` |x|≤ 0.3432 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.148 (n=450)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 8.0 (IC base=+0.103)

- **PATRÓN** `ibs_20min` > `0.2515` → IC=+0.143 (n=480)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.2515 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` > `0.3086` → IC=+0.155 (n=169)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.3086 (IC base=+0.103)

- **PATRÓN** `volumen_regimen` < `0.6213` → IC=+0.150 (n=161)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6213 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `15024.4373` → IC=+0.143 (n=320)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 15024.4373 (IC base=+0.103)

- **PATRÓN** `ballena_activa_n` < `146.0` → IC=+0.145 (n=153)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 146.0 (IC base=+0.103)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.216 (n=216)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.3402` → IC=+0.162 (n=637)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.3402 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.151 (n=571)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.6017` → IC=+0.187 (n=560)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6017 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.4829` → IC=+0.155 (n=732)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.4829 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.406` → IC=+0.160 (n=248)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.406 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.218` → IC=+0.145 (n=637)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.218 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `1.0609` → IC=+0.170 (n=289)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.0609 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1583` → IC=+0.198 (n=170)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1583 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.1106` → IC=+0.159 (n=552)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1106 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.42` → IC=+0.153 (n=627)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.42 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `325.0` → IC=+0.158 (n=533)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 325.0 (IC base=+0.140)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.254 (n=262)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.191)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.195 (n=198)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.007 (IC base=+0.191)

- **PATRÓN** `drift_60min` |x|≤ `0.0977` → IC=+0.211 (n=199)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0977 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.206 (n=617)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `0.4056` → IC=+0.226 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4056 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` > `0.1568` → IC=+0.207 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1568 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` < `0.2278` → IC=+0.192 (n=520)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.2278 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.042` → IC=+0.226 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.042 (IC base=+0.191)

- **PATRÓN** `volumen_regimen` < `0.8342` → IC=+0.199 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8342 (IC base=+0.191)

- **PATRÓN** `volumen_regimen` > `1.1573` → IC=+0.205 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1573 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.2624` → IC=+0.273 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2624 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` < `1.3993` → IC=+0.217 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3993 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `2.4384` → IC=+0.232 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4384 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `12429.5841` → IC=+0.220 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12429.5841 (IC base=+0.191)

- **PATRÓN** `ibs_20min` < `0.0837` → IC=+0.161 (n=187)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.0837 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` < `0.6847` → IC=+0.129 (n=246)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 0.6847 (IC base=+0.093)

- **PATRÓN** `volumen_pendiente_norm` > `0.1661` → IC=+0.126 (n=129)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` > 0.1661 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `9209.6094` → IC=+0.121 (n=373)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 9209.6094 (IC base=+0.093)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `dist_vwap_pct` > `0.3434` → IC=-0.139 (n=34)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3434
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=495)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.168 (n=287)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0072 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.1156` → IC=+0.140 (n=145)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.1156 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.167 (n=400)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 8.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.261 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.939` → IC=+0.237 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.939 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.127` → IC=+0.200 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.127 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `1.069` → IC=+0.151 (n=379)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.069 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2526` → IC=+0.171 (n=86)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2526 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `2.2114` → IC=+0.170 (n=186)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.2114 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.131 (n=470)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `3108.3105` → IC=+0.185 (n=144)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 3108.3105 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.5172` → IC=+0.149 (n=397)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.5172 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` < `0.708` → IC=+0.138 (n=175)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.708 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` < `1.8403` → IC=+0.152 (n=248)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.8403 (IC base=+0.076)

- **PATRÓN** `libro_liquidez` > `2552.1243` → IC=+0.126 (n=265)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 2552.1243 (IC base=+0.076)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.126 (n=340)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 42.0 (IC base=+0.076)

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
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.206 (n=3389)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.180 (n=10580)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.47` → IC=+0.216 (n=10165)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.47 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.9764` → IC=+0.205 (n=1437)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9764 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.624` → IC=+0.226 (n=4898)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.624 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `0.8803` → IC=+0.166 (n=4533)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8803 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.2891` → IC=+0.202 (n=1403)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2891 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.5958` → IC=+0.186 (n=3259)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.5958 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `2346.0211` → IC=+0.172 (n=6777)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2346.0211 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.194 (n=7743)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 86.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.192 (n=6156)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.007 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.1487` → IC=+0.189 (n=4055)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.1487 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.207 (n=3501)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.5657` → IC=+0.238 (n=9211)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5657 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.2503` → IC=+0.162 (n=5708)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2503 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.034` → IC=+0.201 (n=1293)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.034 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.732` → IC=+0.183 (n=8909)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 3.732 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.7043` → IC=+0.162 (n=2782)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.7043 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` > `1.2024` → IC=+0.154 (n=2108)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.2024 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.288` → IC=+0.243 (n=1215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.288 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6264` → IC=+0.193 (n=2820)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6264 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.194 (n=5465)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 48.0 (IC base=+0.182)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.206 (n=576)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.224 (n=577)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.3575` → IC=+0.191 (n=1722)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.3575 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.201 (n=826)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.195 (n=1168)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.327 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.539` → IC=+0.345 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.539 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.274` → IC=+0.254 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.274 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.5691` → IC=+0.199 (n=542)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.5691 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.193 (n=1032)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.264 (n=1355)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0045 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.1282` → IC=+0.284 (n=595)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1282 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.269 (n=1219)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.3517` → IC=+0.290 (n=1191)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3517 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.563` → IC=+0.264 (n=1356)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.563 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.2267` → IC=+0.279 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2267 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` < `1.5472` → IC=+0.258 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5472 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `2.635` → IC=+0.279 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.635 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1806.42` → IC=+0.264 (n=901)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1806.42 (IC base=+0.259)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.189 (n=545)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0028 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.0846` → IC=+0.159 (n=543)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.0846 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=1698)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.3085` → IC=+0.204 (n=1629)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3085 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.1321` → IC=+0.186 (n=924)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1321 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.74` → IC=+0.168 (n=372)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.74 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.249` → IC=+0.153 (n=1467)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.249 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.6287` → IC=+0.177 (n=543)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.6287 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.2669` → IC=+0.199 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2669 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.1137` → IC=+0.160 (n=1385)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1137 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.4047` → IC=+0.155 (n=1574)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.4047 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `15748.8418` → IC=+0.159 (n=739)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 15748.8418 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `472.0` → IC=+0.158 (n=1504)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 472.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.167 (n=1411)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0057 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.26` → IC=+0.168 (n=1240)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.26 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.179 (n=471)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 18.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.155 (n=642)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.6583` → IC=+0.197 (n=1409)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.6583 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.6916` → IC=+0.157 (n=231)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.6916 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.1343` → IC=+0.168 (n=1270)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1343 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.479` → IC=+0.160 (n=236)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 11.479 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.274` → IC=+0.154 (n=1276)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.274 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `1.1888` → IC=+0.165 (n=1409)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1888 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.1513` → IC=+0.198 (n=376)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1513 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.4046` → IC=+0.162 (n=1311)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.4046 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.5117` → IC=+0.162 (n=1171)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.5117 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `421.0` → IC=+0.159 (n=1072)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 421.0 (IC base=+0.153)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.246 (n=549)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.225 (n=1721)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.222 (n=1670)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=648)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.797` → IC=+0.292 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.797 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` < `0.211` → IC=+0.220 (n=1632)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.211 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `1.6339` → IC=+0.224 (n=1571)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6339 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.228 (n=1174)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `sigma_h` < `0.0117` → IC=+0.239 (n=1538)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0117 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.1676` → IC=+0.236 (n=676)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1676 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.261 (n=584)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.238 (n=730)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.3594` → IC=+0.270 (n=1352)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3594 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.76` → IC=+0.273 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.76 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.3445` → IC=+0.308 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3445 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.7536` → IC=+0.232 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7536 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.1892` → IC=+0.237 (n=941)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1892 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.240 (n=1044)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `1892.3107` → IC=+0.242 (n=697)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1892.3107 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.231 (n=1342)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.233)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.183 (n=579)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0035 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4373` → IC=+0.145 (n=1730)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.4373 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=1802)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.877` → IC=+0.261 (n=784)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.877 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.374` → IC=+0.164 (n=683)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.374 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.435` → IC=+0.168 (n=284)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.435 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.8741` → IC=+0.157 (n=1153)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8741 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2367` → IC=+0.216 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2367 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.5221` → IC=+0.149 (n=737)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.5221 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.768` → IC=+0.151 (n=1117)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.768 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `8031.121` → IC=+0.230 (n=784)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8031.121 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.148 (n=709)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 91.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.156 (n=1410)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0076 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.4469` → IC=+0.154 (n=1410)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4469 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=528)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.141 (n=650)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.7021` → IC=+0.184 (n=1410)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.7021 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.6016` → IC=+0.143 (n=1562)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.6016 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.146` → IC=+0.179 (n=210)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 11.146 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.6958` → IC=+0.152 (n=621)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6958 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `1.1867` → IC=+0.144 (n=470)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.1867 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2894` → IC=+0.248 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2894 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.4421` → IC=+0.151 (n=1338)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.4421 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `10833.0728` → IC=+0.210 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10833.0728 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `178.0` → IC=+0.145 (n=1335)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 178.0 (IC base=+0.138)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.141 (n=1147)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0081 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.132 (n=1764)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.192 (n=1722)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.4706 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `1.0869` → IC=+0.203 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0869 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.478` → IC=+0.236 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.478 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `0.8919` → IC=+0.135 (n=1147)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8919 (IC base=+0.113)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.127 (n=1727)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `2897.5388` → IC=+0.248 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2897.5388 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.133 (n=1335)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 54.0 (IC base=+0.113)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.176 (n=557)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0058 (IC base=+0.113)

- **PATRÓN** `drift_60min` |x|≤ `0.1326` → IC=+0.162 (n=557)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1326 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.125 (n=1723)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 5.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.205 (n=1671)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.22` → IC=+0.131 (n=1364)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.22 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.474` → IC=+0.126 (n=1614)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 3.474 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `0.7164` → IC=+0.153 (n=735)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.7164 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.2227` → IC=+0.167 (n=262)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2227 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.4467` → IC=+0.144 (n=503)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4467 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `2839.872` → IC=+0.171 (n=557)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2839.872 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.121 (n=1306)

  - _Acción_: Kelly boost +0.60€ cuando `ballena_activa_n` < 51.0 (IC base=+0.113)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0192` → IC=+0.219 (n=1148)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0192 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.214 (n=1788)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.209 (n=1536)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.5141` → IC=+0.248 (n=1720)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5141 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.2054` → IC=+0.234 (n=1015)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2054 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.245` → IC=+0.272 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.245 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` < `1.2398` → IC=+0.211 (n=1720)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2398 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `0.6389` → IC=+0.215 (n=1720)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6389 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.2346` → IC=+0.245 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2346 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.505` → IC=+0.236 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.505 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.217 (n=1812)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2627.1049` → IC=+0.219 (n=1147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2627.1049 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.009` → IC=+0.226 (n=612)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.009 (IC base=+0.201)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.222 (n=612)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.209 (n=1291)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` < `0.4224` → IC=+0.267 (n=1616)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4224 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `1.2795` → IC=+0.204 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2795 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` < `0.9297` → IC=+0.204 (n=2040)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9297 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.832` → IC=+0.257 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.832 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `1.2349` → IC=+0.234 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2349 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.2826` → IC=+0.268 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2826 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `2.196` → IC=+0.198 (n=1454)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.196 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `1.4288` → IC=+0.197 (n=1652)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4288 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=1090)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.142 (n=3092)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.165 (n=2600)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0091 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.5189` → IC=+0.165 (n=2951)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.5189 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=1172)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.155)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.169 (n=1338)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 6.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.9412` → IC=+0.214 (n=985)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9412 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.1884` → IC=+0.167 (n=1088)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1884 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` < `0.4851` → IC=+0.150 (n=1822)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.4851 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.188` → IC=+0.185 (n=484)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 10.188 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` > `0.8968` → IC=+0.164 (n=1294)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.8968 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.1712` → IC=+0.188 (n=810)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1712 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `1.4564` → IC=+0.163 (n=972)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4564 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `1.879` → IC=+0.163 (n=1943)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.879 (IC base=+0.155)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=2066)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `8307.441` → IC=+0.161 (n=1338)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 8307.441 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.197 (n=777)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0038 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.4871` → IC=+0.159 (n=2332)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4871 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.174 (n=847)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.163 (n=1044)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 6.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.1802` → IC=+0.172 (n=1026)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.1802 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.6838` → IC=+0.160 (n=445)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.6838 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.281` → IC=+0.151 (n=2316)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 6.281 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.2445` → IC=+0.145 (n=2229)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.2445 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` < `0.0966` → IC=+0.143 (n=2109)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` < 0.0966 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.0724` → IC=+0.143 (n=1079)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.0724 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.4246` → IC=+0.153 (n=767)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4246 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.8143` → IC=+0.144 (n=1534)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.8143 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=3092)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `7202.6889` → IC=+0.153 (n=2082)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 7202.6889 (IC base=+0.140)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.183 (n=355)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0056 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.0064` → IC=+0.184 (n=134)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0064 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.0895` → IC=+0.201 (n=135)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0895 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.174 (n=421)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 4.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.178 (n=178)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 8.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` < `0.5452` → IC=+0.196 (n=268)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.5452 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.2197` → IC=+0.177 (n=190)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.2197 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` < `0.3749` → IC=+0.170 (n=389)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.3749 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.129` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 10.129 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.471` → IC=+0.177 (n=425)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` < 2.471 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `1.231` → IC=+0.175 (n=401)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 1.231 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` > `0.8487` → IC=+0.199 (n=267)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` > 0.8487 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.3035` → IC=+0.300 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3035 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.4485` → IC=+0.199 (n=134)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.4485 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.6405` → IC=+0.206 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6405 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `12584.8678` → IC=+0.217 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12584.8678 (IC base=+0.168)

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

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.177 (n=419)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.1382 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.6071` → IC=+0.150 (n=432)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.6071 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.6955` → IC=+0.170 (n=89)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.6955 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.2218` → IC=+0.140 (n=967)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.2218 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.377` → IC=+0.162 (n=931)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 6.377 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8794` → IC=+0.189 (n=635)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.8794 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.0682` → IC=+0.164 (n=445)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.0682 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.42` → IC=+0.146 (n=317)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.42 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.8205` → IC=+0.151 (n=632)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.8205 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `11474.1256` → IC=+0.154 (n=951)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 11474.1256 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `705.0` → IC=+0.145 (n=906)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 705.0 (IC base=+0.139)

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
- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.165 (n=836)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0073 (IC base=+0.160)

- **PATRÓN** `sigma_h` > `0.0043` → IC=+0.167 (n=948)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0043 (IC base=+0.160)

- **PATRÓN** `drift_60min` |x|≤ `0.3855` → IC=+0.165 (n=834)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3855 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=367)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.170 (n=337)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 4.0 (IC base=+0.160)

- **PATRÓN** `ibs_20min` < `0.5599` → IC=+0.164 (n=632)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.5599 (IC base=+0.160)

- **PATRÓN** `ibs_20min` > `0.8884` → IC=+0.173 (n=316)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.8884 (IC base=+0.160)

- **PATRÓN** `dist_vwap_pct` > `0.7023` → IC=+0.163 (n=271)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.7023 (IC base=+0.160)

- **PATRÓN** `dist_vwap_pct` < `0.4248` → IC=+0.170 (n=882)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.4248 (IC base=+0.160)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.12` → IC=+0.171 (n=850)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` < 4.12 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` < `0.8891` → IC=+0.161 (n=632)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8891 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` > `0.7161` → IC=+0.162 (n=847)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.7161 (IC base=+0.160)

- **PATRÓN** `volumen_pendiente_norm` < `0.1066` → IC=+0.162 (n=873)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` < 0.1066 (IC base=+0.160)

- **PATRÓN** `volumen_pendiente_norm` > `0.0781` → IC=+0.167 (n=409)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0781 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` < `1.4364` → IC=+0.176 (n=310)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.4364 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` > `1.5228` → IC=+0.161 (n=830)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.5228 (IC base=+0.160)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.166 (n=940)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.160)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.184 (n=267)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0041 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.3914` → IC=+0.175 (n=700)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3914 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=274)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.159 (n=541)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 10.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.7466` → IC=+0.148 (n=797)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.7466 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.0954` → IC=+0.151 (n=795)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.0954 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1663` → IC=+0.166 (n=375)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1663 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.3879` → IC=+0.144 (n=815)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.3879 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.388` → IC=+0.151 (n=718)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.388 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.647` → IC=+0.179 (n=266)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.647 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `0.7259` → IC=+0.145 (n=711)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.7259 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.0738` → IC=+0.163 (n=336)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.0738 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.2051` → IC=+0.155 (n=686)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.2051 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.7831` → IC=+0.149 (n=519)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.7831 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `7571.9816` → IC=+0.170 (n=795)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 7571.9816 (IC base=+0.144)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `ibs_20min` > `0.9404` → IC=+0.229 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9404 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` > `0.1887` → IC=+0.136 (n=160)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.1887 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.247` → IC=+0.188 (n=46)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 9.247 (IC base=+0.092)

- **PATRÓN** `volumen_pendiente_norm` > `0.1587` → IC=+0.208 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1587 (IC base=+0.092)

- **PATRÓN** `volumen_spike_ratio` > `1.4231` → IC=+0.125 (n=222)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 1.4231 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `3427.9609` → IC=+0.144 (n=206)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 3427.9609 (IC base=+0.092)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.149 (n=220)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0069 (IC base=+0.114)

- **PATRÓN** `drift_60min` |x|≤ `0.3998` → IC=+0.158 (n=147)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.3998 (IC base=+0.114)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.158 (n=150)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 10.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.1538` → IC=+0.210 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1538 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` > `0.5986` → IC=+0.192 (n=105)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.5986 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.689` → IC=+0.134 (n=121)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 2.689 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `0.9493` → IC=+0.131 (n=147)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 0.9493 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` < `0.092` → IC=+0.176 (n=168)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.092 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `1.8499` → IC=+0.135 (n=143)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.8499 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `3291.3893` → IC=+0.144 (n=220)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 3291.3893 (IC base=+0.114)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.158 (n=185)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 49.0 (IC base=+0.114)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.212 (n=123)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=373)

- **FILTRO** `dist_vwap_pct` > `0.1862` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1862
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=328)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.189 (n=413)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0041 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.127 (n=861)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 8.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.6731` → IC=+0.204 (n=754)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6731 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.1549` → IC=+0.156 (n=457)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1549 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.465` → IC=+0.193 (n=200)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 11.465 (IC base=+0.094)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.196 (n=110)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` < `2.0922` → IC=+0.131 (n=643)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.0922 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `2432.8034` → IC=+0.139 (n=372)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2432.8034 (IC base=+0.094)

- **PATRÓN** `ibs_20min` < `0.0667` → IC=+0.267 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0667 (IC base=+0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.189 (n=101)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` < `2.5298` → IC=+0.123 (n=237)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.5298 (IC base=+0.002)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.158 (n=320)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.006 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.122 (n=331)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.103)

- **PATRÓN** `ibs_20min` > `0.5161` → IC=+0.184 (n=289)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.5161 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` > `0.1382` → IC=+0.173 (n=151)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.1382 (IC base=+0.103)

- **PATRÓN** `volumen_regimen` < `1.0688` → IC=+0.123 (n=255)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.0688 (IC base=+0.103)

- **PATRÓN** `volumen_pendiente_norm` < `0.0759` → IC=+0.136 (n=223)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.0759 (IC base=+0.103)

- **PATRÓN** `volumen_spike_ratio` < `2.0105` → IC=+0.167 (n=220)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.0105 (IC base=+0.103)

- **PATRÓN** `ibs_20min` < `0.0889` → IC=+0.280 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0889 (IC base=+0.049)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.71` → IC=+0.143 (n=110)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.71 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` < `0.6103` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6103 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.0712` → IC=+0.214 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0712 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` < `2.3987` → IC=+0.161 (n=107)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.3987 (IC base=+0.049)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.006` → IC=-0.225 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=117)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=120)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.181 (n=139)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.004 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.136 (n=295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 7.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.6789` → IC=+0.235 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6789 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.3477` → IC=+0.172 (n=114)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.3477 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.875` → IC=+0.312 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.875 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` > `0.9419` → IC=+0.136 (n=130)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.9419 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` > `0.2766` → IC=+0.237 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2766 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` < `1.7354` → IC=+0.165 (n=156)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.7354 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.127 (n=191)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `1133.3296` → IC=+0.156 (n=251)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 1133.3296 (IC base=+0.105)

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

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.171 (n=244)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.6667 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` > `0.1982` → IC=+0.149 (n=152)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1982 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.497` → IC=+0.167 (n=109)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 5.497 (IC base=+0.071)

- **PATRÓN** `volumen_regimen` > `1.0639` → IC=+0.174 (n=90)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 1.0639 (IC base=+0.071)

- **PATRÓN** `volumen_pendiente_norm` > `0.2443` → IC=+0.185 (n=52)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2443 (IC base=+0.071)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.167 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0057 (IC base=-0.040)

- **PATRÓN** `ibs_20min` < `0.2222` → IC=+0.197 (n=64)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.2222 (IC base=-0.040)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.25` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.25 (IC base=-0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.1368` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1368 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` < `2.5569` → IC=+0.130 (n=52)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 2.5569 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` > `1.3803` → IC=+0.148 (n=52)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.3803 (IC base=-0.040)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `8.0` → IC=-0.365 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=155)

- **FILTRO** `dist_vwap_pct` > `0.2351` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2351
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=189)

- **FILTRO** `volumen_regimen` < `0.7597` → IC=-0.341 (n=67)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7597
  - _Potencial_: sin este filtro IC_bueno=-0.164 (n=138)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.367 (n=58)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=114)

- **FILTRO** `dist_vwap_pct` > `0.4139` → IC=-0.413 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4139
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=151)

- **FILTRO** `volumen_pendiente_norm` > `0.0812` → IC=-0.389 (n=16)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0812
  - _Potencial_: sin este filtro IC_bueno=-0.264 (n=70)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` < `0.0033` → IC=-0.237 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=37)

- **FILTRO** `volumen_regimen` < `0.8127` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8127
  - _Potencial_: sin este filtro IC_bueno=-0.149 (n=55)

- **FILTRO** `volumen_spike_ratio` > `3.5274` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.5274
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=34)

- **FILTRO** `drift_60min` |x|> `0.1035` → IC=-0.306 (n=34)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1035
  - _Potencial_: sin este filtro IC_bueno=-0.158 (n=36)

- **FILTRO** `volumen_regimen` > `0.9309` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9309
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
- **FILTRO** `drift_60min` |x|> `0.2367` → IC=-0.441 (n=15)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2367
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=49)

- **FILTRO** `sigma_h` < `0.0099` → IC=-0.353 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0099
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=11)

- **FILTRO** `volumen_regimen` < `1.1043` → IC=-0.433 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.1043
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=15)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.1837` → IC=-0.126 (n=121)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1837
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=236)

- **FILTRO** `dist_vwap_pct` > `0.6357` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6357
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=332)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.161 (n=119)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0058 (IC base=+0.088)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.132 (n=123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 15.0 (IC base=+0.088)

- **PATRÓN** `ibs_20min` > `0.6429` → IC=+0.162 (n=258)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.6429 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.4967` → IC=+0.182 (n=61)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.4967 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.1837` → IC=+0.143 (n=236)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.1837 (IC base=+0.051)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.0` → IC=+0.140 (n=109)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 6.0 (IC base=+0.051)

- **PATRÓN** `libro_liquidez` > `3805.194` → IC=+0.169 (n=122)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 3805.194 (IC base=+0.051)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.273 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=91)

- **FILTRO** `ibs_20min` < `0.576` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.576
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=84)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.147 (n=83)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0033 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.2293` → IC=+0.154 (n=105)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.2293 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.214 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.161 (n=54)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 7.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.2076` → IC=+0.172 (n=123)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.2076 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.2943` → IC=+0.127 (n=148)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` < 0.2943 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.645` → IC=+0.130 (n=98)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 4.645 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.0206` → IC=+0.127 (n=108)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.0206 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` < `0.1081` → IC=+0.167 (n=88)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.1081 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` > `1.4478` → IC=+0.145 (n=91)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4478 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `3787.1326` → IC=+0.152 (n=110)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3787.1326 (IC base=+0.118)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` > `0.1906` → IC=-0.150 (n=38)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1906
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=76)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.172 (n=59)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.004 (IC base=+0.044)

- **PATRÓN** `drift_60min` |x|≤ `0.1365` → IC=+0.138 (n=45)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.1365 (IC base=+0.044)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.192 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.044)

- **PATRÓN** `ibs_20min` > `0.6061` → IC=+0.162 (n=66)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.6061 (IC base=+0.044)

- **PATRÓN** `libro_liquidez` > `1545.7265` → IC=+0.123 (n=59)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1545.7265 (IC base=+0.044)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.321` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.321 (IC base=+0.017)

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

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4605 (IC base=+0.292)

- **PATRÓN** `elapsed_s` > `210.1` → IC=+0.393 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 210.1 (IC base=+0.292)

- **PATRÓN** `drift_15min` |x|≤ `1.0466` → IC=+0.447 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0466 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.8011` → IC=+0.361 (n=34)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8011 (IC base=+0.292)

- **PATRÓN** `ballena_activa_n` < `1294.0` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1294.0 (IC base=+0.292)

- **PATRÓN** `elapsed_s` > `193.3` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 193.3 (IC base=+0.214)

- **PATRÓN** `drift_15min` |x|≤ `2.5595` → IC=+0.265 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.5595 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.6484` → IC=+0.308 (n=24)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6484 (IC base=+0.214)

- **PATRÓN** `ballena_activa_n` < `1508.0` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1508.0 (IC base=+0.214)

### LATE_WINDOW_5MIN#BTC#5min
- **PATRÓN** `drift_ventana_pct` |x|> `0.4605` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4605 (IC base=+0.292)

- **PATRÓN** `elapsed_s` > `210.1` → IC=+0.393 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 210.1 (IC base=+0.292)

- **PATRÓN** `drift_15min` |x|≤ `1.0466` → IC=+0.447 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0466 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.8011` → IC=+0.361 (n=34)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8011 (IC base=+0.292)

- **PATRÓN** `ballena_activa_n` < `1294.0` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1294.0 (IC base=+0.292)

- **PATRÓN** `elapsed_s` > `193.3` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 193.3 (IC base=+0.214)

- **PATRÓN** `drift_15min` |x|≤ `2.5595` → IC=+0.265 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.5595 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.6484` → IC=+0.308 (n=24)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6484 (IC base=+0.214)

- **PATRÓN** `ballena_activa_n` < `1508.0` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1508.0 (IC base=+0.214)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `libro_liquidez` > `2923.1096` → IC=+0.167 (n=238)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2923.1096 (IC base=+0.105)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2923.1096` → IC=+0.167 (n=238)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2923.1096 (IC base=+0.105)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1801)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9583` → IC=-0.295 (n=37)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9583
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=76)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

### LIQUIDACIONES_5M#BNB#5min
- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.129 (n=33)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 26.0 (IC base=+0.040)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `35151.71` → IC=-0.141 (n=62)

  - _Acción_: SKIP cuando `liq_usd_total` < 35151.71
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=128)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=12)

- **FILTRO** `libro_liquidez` < `15405.8709` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 15405.8709
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `ballena_activa_n` > `569.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `ballena_activa_n` > 569.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **PATRÓN** `liq_n` > `18.0` → IC=+0.206 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 18.0 (IC base=+0.021)

- **PATRÓN** `liq_usd_total` > `68754.71` → IC=+0.170 (n=95)

  - _Acción_: Kelly boost +0.85€ cuando `liq_usd_total` > 68754.71 (IC base=+0.021)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=135)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=793)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=747)

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
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=431)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=168)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=630)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=630)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.143 (n=208)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=502)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=357)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=357)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.148 (n=86)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=286)

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

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=105)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=203)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=83)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=86)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=240)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=240)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=129)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.47` → IC=-0.121 (n=404)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=211)

- **PATRÓN** `py_entrada` < `0.47` → IC=+0.171 (n=162)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` < 0.47 (IC base=+0.012)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **PATRÓN** `py_entrada` < `0.55` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` < 0.55 (IC base=+0.041)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.59` → IC=+0.172 (n=65)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` < 0.59 (IC base=+0.092)

- **PATRÓN** `profundidad_ratio` > `79.6` → IC=+0.172 (n=65)

  - _Acción_: Kelly boost +0.86€ cuando `profundidad_ratio` > 79.6 (IC base=+0.092)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` > `0.44` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `py_entrada` > 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=24)

- **FILTRO** `restante_min` > `11.54` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `restante_min` > 11.54
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=23)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.262 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=25)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `restante_min` < `3.99` → IC=-0.232 (n=39)

  - _Acción_: SKIP cuando `restante_min` < 3.99
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

- **FILTRO** `lag_apertura_s` > `61.04` → IC=-0.225 (n=38)

  - _Acción_: SKIP cuando `lag_apertura_s` > 61.04
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=14)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=25)

- **FILTRO** `profundidad_ratio` < `66.8` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `profundidad_ratio` < 66.8
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=23)

- **FILTRO** `restante_min` < `13.03` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `restante_min` < 13.03
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=26)

- **FILTRO** `hora_utc` < `14.0` → IC=-0.192 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=28)

- **FILTRO** `lag_apertura_s` > `120.14` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `lag_apertura_s` > 120.14
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=27)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=44)

- **FILTRO** `restante_min` < `3.44` → IC=-0.364 (n=20)

  - _Acción_: SKIP cuando `restante_min` < 3.44
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=41)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=46)

- **FILTRO** `lag_apertura_s` > `93.56` → IC=-0.364 (n=20)

  - _Acción_: SKIP cuando `lag_apertura_s` > 93.56
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=41)

- **FILTRO** `profundidad_ratio` < `67.5` → IC=-0.188 (n=30)

  - _Acción_: SKIP cuando `profundidad_ratio` < 67.5
  - _Potencial_: sin este filtro IC_bueno=-0.106 (n=31)

- **FILTRO** `profundidad_ratio` < `46.5` → IC=-0.177 (n=29)

  - _Acción_: SKIP cuando `profundidad_ratio` < 46.5
  - _Potencial_: sin este filtro IC_bueno=+0.188 (n=30)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.44 (IC base=+0.008)

- **PATRÓN** `profundidad_ratio` > `46.5` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `profundidad_ratio` > 46.5 (IC base=+0.008)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `restante_min` < `13.49` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `restante_min` < 13.49
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=12)

- **FILTRO** `lag_apertura_s` > `90.91` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `lag_apertura_s` > 90.91
  - _Potencial_: sin este filtro IC_bueno=+0.233 (n=13)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.132 (n=36)

- **PATRÓN** `py_entrada` < `0.6` → IC=+0.132 (n=36)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.6 (IC base=+0.009)

- **PATRÓN** `restante_min` > `13.42` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` > 13.42 (IC base=+0.009)

- **PATRÓN** `lag_apertura_s` < `126.28` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `lag_apertura_s` < 126.28 (IC base=+0.009)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=60)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.167 (n=37)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=40)

- **FILTRO** `profundidad_ratio` < `21.2` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `profundidad_ratio` < 21.2
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=58)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.217 (n=44)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=51)

- **FILTRO** `restante_min` < `2.74` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `restante_min` < 2.74
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=73)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.180 (n=23)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=72)

- **FILTRO** `py_entrada` > `0.56` → IC=-0.136 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.157 (n=33)

- **PATRÓN** `py_entrada` < `0.56` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` < 0.56 (IC base=+0.015)

- **PATRÓN** `lag_apertura_s` < `68.74` → IC=+0.129 (n=33)

  - _Acción_: Kelly boost +0.64€ cuando `lag_apertura_s` < 68.74 (IC base=+0.015)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=7548)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.166 (n=3564)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=10724)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.167 (n=3676)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=11124)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.208 (n=611)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=1872)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.192 (n=625)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=1906)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.202 (n=643)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=2007)

- **FILTRO** `ibs_20min` > `0.28` → IC=-0.163 (n=662)

  - _Acción_: SKIP cuando `ibs_20min` > 0.28
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=1988)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.174 (n=608)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=1861)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.175 (n=644)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=2010)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=2786)

- **FILTRO** `py_entrada` > `0.595` → IC=-0.212 (n=709)

  - _Acción_: SKIP cuando `py_entrada` > 0.595
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2264)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=2952)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.175 (n=121)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=389)

- **FILTRO** `libro_liquidez` < `16996.7551` → IC=-0.146 (n=227)

  - _Acción_: SKIP cuando `libro_liquidez` < 16996.7551
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=681)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.405` → IC=-0.207 (n=80)

  - _Acción_: SKIP cuando `py_entrada` < 0.405
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=242)

- **FILTRO** `ibs_20min` < `0.1205` → IC=-0.232 (n=80)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1205
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=242)

- **FILTRO** `py_entrada` > `0.625` → IC=-0.279 (n=66)

  - _Acción_: SKIP cuando `py_entrada` > 0.625
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=243)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `py_entrada` < `0.415` → IC=-0.214 (n=197)

  - _Acción_: SKIP cuando `py_entrada` < 0.415
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=602)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.130 (n=10159)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=22544)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.273 (n=8027)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=24676)

- **FILTRO** `ibs_7min` < `0.2821` → IC=-0.235 (n=8175)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2821
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=24528)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.156 (n=11103)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=21600)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.230 (n=10055)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=31005)

- **FILTRO** `ibs_7min` > `0.292` → IC=-0.177 (n=10263)

  - _Acción_: SKIP cuando `ibs_7min` > 0.292
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=30797)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.137 (n=1659)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=3752)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.310 (n=1293)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=4118)

- **FILTRO** `ibs_7min` < `0.7109` → IC=-0.250 (n=1785)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7109
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=3626)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.186 (n=1229)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=4182)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.262 (n=1739)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=5322)

- **FILTRO** `drift_7min_pct` |x|> `0.1121` → IC=-0.125 (n=2398)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1121
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=4663)

- **FILTRO** `ibs_7min` > `0.7875` → IC=-0.207 (n=1765)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7875
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=5296)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.137 (n=1334)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=4308)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.251 (n=1367)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=4275)

- **FILTRO** `ibs_7min` < `0.7468` → IC=-0.191 (n=1408)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7468
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=4234)

- **FILTRO** `ballena_activa_n` > `162.0` → IC=-0.179 (n=1402)

  - _Acción_: SKIP cuando `ballena_activa_n` > 162.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=4240)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.254 (n=1432)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=4302)

- **FILTRO** `ibs_7min` > `0.2607` → IC=-0.178 (n=1432)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2607
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=4302)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.182 (n=1431)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=4303)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.165 (n=1466)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=3672)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.306 (n=1273)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=3865)

- **FILTRO** `ibs_7min` < `0.7063` → IC=-0.244 (n=1695)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7063
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=3443)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.221 (n=1184)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=3954)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.236 (n=1721)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=5825)

- **FILTRO** `ibs_7min` > `0.7436` → IC=-0.172 (n=1885)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7436
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=5661)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=1748)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=3655)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.241 (n=1332)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=4071)

- **FILTRO** `ibs_7min` < `0.74` → IC=-0.180 (n=1350)

  - _Acción_: SKIP cuando `ibs_7min` < 0.74
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=4053)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.171 (n=1320)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=4083)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.260 (n=1375)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=4127)

- **FILTRO** `ibs_7min` > `0.2744` → IC=-0.177 (n=1375)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2744
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=4127)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.184 (n=1354)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=4148)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.36` → IC=-0.253 (n=1400)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=4300)

- **FILTRO** `ibs_7min` < `0.3` → IC=-0.233 (n=1417)

  - _Acción_: SKIP cuando `ibs_7min` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4283)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.178 (n=1850)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=5963)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.38` → IC=-0.255 (n=1754)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=3655)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.229 (n=1347)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=4062)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.214 (n=1313)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=4096)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.205 (n=1765)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=5639)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=1094)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=533)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1156)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=323)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=558)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4161` → IC=+0.142 (n=498)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio` |x|> 0.4161 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.123 (n=343)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 14.0 (IC base=+0.111)

- **PATRÓN** `total_vol_5m` < `469.512` → IC=+0.141 (n=249)

  - _Acción_: Kelly boost +0.71€ cuando `total_vol_5m` < 469.512 (IC base=+0.111)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4377` → IC=+0.150 (n=58)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.75€ cuando `delta_ratio` |x|> 0.4377 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=177)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.132)

- **PATRÓN** `total_vol_5m` < `451.687` → IC=+0.136 (n=152)

  - _Acción_: Kelly boost +0.68€ cuando `total_vol_5m` < 451.687 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `2530.2591` → IC=+0.183 (n=58)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2530.2591 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.155 (n=56)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 12.0 (IC base=+0.132)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.141 (n=62)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 12.0 (IC base=+0.092)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4133` → IC=+0.173 (n=102)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio` |x|> 0.4133 (IC base=+0.090)

- **PATRÓN** `total_vol_5m` < `391.8444` → IC=+0.196 (n=67)

  - _Acción_: Kelly boost +0.98€ cuando `total_vol_5m` < 391.8444 (IC base=+0.090)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.173 (n=53)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 69.0 (IC base=+0.090)

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
- **PATRÓN** `delta_ratio` |x|> `0.3994` → IC=+0.151 (n=130)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio` |x|> 0.3994 (IC base=+0.103)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.136 (n=130)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 13.0 (IC base=+0.103)

- **PATRÓN** `total_vol_5m` < `263476.4` → IC=+0.146 (n=97)

  - _Acción_: Kelly boost +0.73€ cuando `total_vol_5m` < 263476.4 (IC base=+0.103)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.221 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `3568.9496` → IC=+0.162 (n=66)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 3568.9496 (IC base=+0.103)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.0055` → IC=-0.298 (n=191)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0055
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=192)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `63.9918` → IC=-0.405 (n=40)

  - _Acción_: SKIP cuando `T_h` > 63.9918
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=80)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.227 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.123)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0107` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0107
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=20)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0122` → IC=-0.180 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0122
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=46)

- **FILTRO** `T_h` < `39.9936` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `T_h` < 39.9936
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=52)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `pct_vs_K` |x|> `2.7344` → IC=-0.229 (n=190)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7344
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=192)

- **FILTRO** `pct_vs_K` |x|> `3.2571` → IC=-0.438 (n=111)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.2571
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=217)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.004` → IC=-0.214 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.004
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=101)

- **FILTRO** `T_h` > `75.8976` → IC=-0.148 (n=89)

  - _Acción_: SKIP cuando `T_h` > 75.8976
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=45)

- **FILTRO** `pct_vs_K` |x|> `2.9087` → IC=-0.353 (n=32)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9087
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=102)

- **FILTRO** `T_h` < `95.9199` → IC=-0.378 (n=39)

  - _Acción_: SKIP cuando `T_h` < 95.9199
  - _Potencial_: sin este filtro IC_bueno=-0.274 (n=82)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `2.4229` → IC=-0.354 (n=53)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.4229
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=55)

- **FILTRO** `sigma_h` > `0.0094` → IC=-0.321 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.228 (n=79)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.352 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=80)

- **FILTRO** `T_h` > `61.3189` → IC=-0.319 (n=70)

  - _Acción_: SKIP cuando `T_h` > 61.3189
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=35)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0126` → IC=-0.156 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0126
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=61)

- **FILTRO** `sigma_h` < `0.0083` → IC=-0.156 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=61)

- **FILTRO** `T_h` > `132.7892` → IC=-0.219 (n=30)

  - _Acción_: SKIP cuando `T_h` > 132.7892
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=61)

- **FILTRO** `pct_vs_K` |x|> `4.9556` → IC=-0.292 (n=22)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.9556
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=69)

- **FILTRO** `sigma_h` < `0.0156` → IC=-0.363 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0156
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=17)

- **FILTRO** `T_h` > `62.4283` → IC=-0.382 (n=49)

  - _Acción_: SKIP cuando `T_h` > 62.4283
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=17)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1208` → IC=+0.466 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1208 (IC base=+0.384)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.449 (n=37)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.384)

- **PATRÓN** `T_h` > `0.4742` → IC=+0.432 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4742 (IC base=+0.384)

- **PATRÓN** `dist_50` > `0.4444` → IC=+0.474 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4444 (IC base=+0.384)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.435 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.384)

- **PATRÓN** `edge` > `0.097` → IC=+0.457 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.097 (IC base=+0.419)

- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.457 (n=92)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.419)

- **PATRÓN** `T_h` < `0.6208` → IC=+0.458 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6208 (IC base=+0.419)

- **PATRÓN** `T_h` > `1.4774` → IC=+0.438 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4774 (IC base=+0.419)

- **PATRÓN** `dist_50` > `0.4027` → IC=+0.486 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4027 (IC base=+0.419)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.468 (n=93)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.419)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1134` → IC=+0.444 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1134 (IC base=+0.411)

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
- **PATRÓN** `edge` > `0.2267` → IC=+0.471 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2267 (IC base=+0.481)

- **PATRÓN** `sigma_h` < `0.0148` → IC=+0.471 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0148 (IC base=+0.481)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.471 (n=33)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.481)

- **PATRÓN** `T_h` < `1.3025` → IC=+0.471 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.3025 (IC base=+0.481)

- **PATRÓN** `T_h` > `0.8566` → IC=+0.471 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8566 (IC base=+0.481)

- **PATRÓN** `dist_50` > `0.3774` → IC=+0.471 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3774 (IC base=+0.481)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.463 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.481)

- **PATRÓN** `edge` > `0.096` → IC=+0.478 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.096 (IC base=+0.470)

- **PATRÓN** `sigma_h` < `0.0156` → IC=+0.478 (n=90)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0156 (IC base=+0.470)

- **PATRÓN** `T_h` < `0.8294` → IC=+0.469 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.8294 (IC base=+0.470)

- **PATRÓN** `T_h` > `1.2259` → IC=+0.468 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.2259 (IC base=+0.470)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.488 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.470)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.476 (n=39)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 2.0 (IC base=+0.470)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=180)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=295)

- **FILTRO** `streak_estiramiento` > `0.8486` → IC=-0.177 (n=63)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.8486
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=191)

- **PATRÓN** `streak_estiramiento` < `0.4086` → IC=+0.167 (n=46)

  - _Acción_: Kelly boost +0.83€ cuando `streak_estiramiento` < 0.4086 (IC base=+0.033)

- **PATRÓN** `streak_estiramiento` < `0.5654` → IC=+0.162 (n=128)

  - _Acción_: Kelly boost +0.81€ cuando `streak_estiramiento` < 0.5654 (IC base=+0.034)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.222 (n=16)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.015)

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
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=401)

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
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=607)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1109)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=762)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=729)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=2936)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1491)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1499)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.219 (n=742)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0087 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.0511` → IC=+0.206 (n=546)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0511 (IC base=+0.186)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2158` → IC=+0.190 (n=547)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.95€ cuando `delta_ratio_macro` |x|> 0.2158 (IC base=+0.186)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1262` → IC=+0.237 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1262 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.197 (n=1514)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 6.0 (IC base=+0.186)

- **PATRÓN** `ibs_15` > `0.6068` → IC=+0.268 (n=1637)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6068 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` > `0.3041` → IC=+0.190 (n=556)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.3041 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` < `0.6233` → IC=+0.179 (n=1559)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.6233 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.758` → IC=+0.283 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.758 (IC base=+0.186)

- **PATRÓN** `libro_liquidez` > `2967.0429` → IC=+0.195 (n=1091)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2967.0429 (IC base=+0.186)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=625)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.219 (n=368)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.0591` → IC=+0.300 (n=123)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0591 (IC base=+0.207)

- **PATRÓN** `drift_15min` |x|≤ `0.3843` → IC=+0.212 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3843 (IC base=+0.207)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2587` → IC=+0.252 (n=123)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2587 (IC base=+0.207)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1446` → IC=+0.271 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1446 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.240 (n=341)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.207)

- **PATRÓN** `ibs_15` > `0.7036` → IC=+0.276 (n=368)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7036 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.4066` → IC=+0.259 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4066 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.239` → IC=+0.272 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.239 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `16113.4131` → IC=+0.244 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16113.4131 (IC base=+0.207)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `24.513` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 24.513
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=383)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.141 (n=382)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0065 (IC base=+0.137)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.160 (n=254)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0051 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0674` → IC=+0.159 (n=168)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.0674 (IC base=+0.137)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2344` → IC=+0.174 (n=127)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio_macro` |x|> 0.2344 (IC base=+0.137)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2579` → IC=+0.164 (n=272)

  - _Acción_: Kelly boost +0.82€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2579 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.160 (n=280)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 11.0 (IC base=+0.137)

- **PATRÓN** `ibs_15` > `0.6602` → IC=+0.258 (n=341)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6602 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1631` → IC=+0.156 (n=300)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1631 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.19` → IC=+0.207 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.19 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `3422.7688` → IC=+0.147 (n=341)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3422.7688 (IC base=+0.137)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.176 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=97)

- **FILTRO** `ibs_15` > `0.2168` → IC=-0.235 (n=32)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2168
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=97)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.306 (n=65)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.1511` → IC=+0.205 (n=171)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1511 (IC base=+0.173)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0712` → IC=+0.197 (n=173)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.99€ cuando `delta_ratio_macro` |x|> 0.0712 (IC base=+0.173)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2673` → IC=+0.233 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2673 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.201 (n=135)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.173)

- **PATRÓN** `ibs_15` > `0.6111` → IC=+0.265 (n=194)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6111 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.3153` → IC=+0.203 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3153 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` < `0.5272` → IC=+0.173 (n=212)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.5272 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.389` → IC=+0.407 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.389 (IC base=+0.173)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.175 (n=149)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `3077.8574` → IC=+0.289 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3077.8574 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.226 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.173)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.5695` → IC=-0.135 (n=124)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.5695
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=906)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `15.788` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.788 (IC base=+0.004)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0235` → IC=+0.260 (n=144)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0235 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.0862` → IC=+0.213 (n=190)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0862 (IC base=+0.188)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0401` → IC=+0.191 (n=431)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.95€ cuando `delta_ratio_macro` |x|> 0.0401 (IC base=+0.188)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0898` → IC=+0.254 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0898 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.230 (n=150)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.188)

- **PATRÓN** `ibs_15` > `0.55` → IC=+0.281 (n=431)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.55 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` > `0.1332` → IC=+0.207 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1332 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` < `0.8552` → IC=+0.189 (n=496)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.8552 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.866` → IC=+0.235 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.866 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.785` → IC=+0.188 (n=431)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 10.785 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `2916.4526` → IC=+0.288 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2916.4526 (IC base=+0.188)

- **PATRÓN** `ibs_15` < `0.1176` → IC=+0.159 (n=485)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.80€ cuando `ibs_15` < 0.1176 (IC base=+0.050)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.375 (n=190)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.342)

- **PATRÓN** `drift_60min` |x|≤ `0.1082` → IC=+0.350 (n=279)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1082 (IC base=+0.342)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1435` → IC=+0.368 (n=278)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1435 (IC base=+0.342)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.13` → IC=+0.378 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.13 (IC base=+0.342)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.363 (n=420)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.342)

- **PATRÓN** `ibs_15` > `0.7873` → IC=+0.385 (n=417)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7873 (IC base=+0.342)

- **PATRÓN** `dist_vwap_pct` > `0.4335` → IC=+0.390 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4335 (IC base=+0.342)

- **PATRÓN** `dist_vwap_pct` < `0.1089` → IC=+0.343 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1089 (IC base=+0.342)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.231` → IC=+0.345 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.231 (IC base=+0.342)

- **PATRÓN** `sigma_ewma_delta_pct` < `14.018` → IC=+0.344 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 14.018 (IC base=+0.342)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.347 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.342)

- **PATRÓN** `libro_liquidez` > `3505.1277` → IC=+0.357 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3505.1277 (IC base=+0.342)

- **PATRÓN** `ballena_activa_n` < `462.0` → IC=+0.365 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 462.0 (IC base=+0.342)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.354 (n=204)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.345)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.373 (n=77)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.345)

- **PATRÓN** `drift_60min` |x|≤ `0.0569` → IC=+0.375 (n=78)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0569 (IC base=+0.345)

- **PATRÓN** `drift_15min` |x|≤ `0.4231` → IC=+0.356 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4231 (IC base=+0.345)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.354 (n=231)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=+0.345)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1231` → IC=+0.386 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1231 (IC base=+0.345)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.372 (n=216)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.345)

- **PATRÓN** `ibs_15` > `0.8166` → IC=+0.380 (n=231)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8166 (IC base=+0.345)

- **PATRÓN** `dist_vwap_pct` > `0.4066` → IC=+0.412 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4066 (IC base=+0.345)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.997` → IC=+0.350 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.997 (IC base=+0.345)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.659` → IC=+0.349 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.659 (IC base=+0.345)

- **PATRÓN** `libro_liquidez` > `11204.8499` → IC=+0.365 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11204.8499 (IC base=+0.345)

- **PATRÓN** `ballena_activa_n` < `574.0` → IC=+0.393 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 574.0 (IC base=+0.345)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.373 (n=124)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.336)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.350 (n=125)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.336)

- **PATRÓN** `delta_ratio_macro` |x|> `0.087` → IC=+0.358 (n=167)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.087 (IC base=+0.336)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2925` → IC=+0.365 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2925 (IC base=+0.336)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.398 (n=86)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.336)

- **PATRÓN** `ibs_15` > `0.7408` → IC=+0.394 (n=186)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7408 (IC base=+0.336)

- **PATRÓN** `dist_vwap_pct` > `0.4613` → IC=+0.383 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4613 (IC base=+0.336)

- **PATRÓN** `dist_vwap_pct` < `0.1227` → IC=+0.345 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1227 (IC base=+0.336)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.981` → IC=+0.348 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.981 (IC base=+0.336)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.77` → IC=+0.341 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.77 (IC base=+0.336)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.347 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.336)

- **PATRÓN** `libro_liquidez` > `3525.4286` → IC=+0.357 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3525.4286 (IC base=+0.336)

- **PATRÓN** `ballena_activa_n` < `160.0` → IC=+0.348 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 160.0 (IC base=+0.336)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0129` → IC=-0.221 (n=665)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0129
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1997)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.194 (n=904)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=1758)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1373` → IC=+0.255 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1373 (IC base=-0.062)

- **PATRÓN** `ibs_15` > `0.6371` → IC=+0.277 (n=636)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6371 (IC base=-0.062)

- **PATRÓN** `dist_vwap_pct` < `0.2815` → IC=+0.188 (n=505)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.2815 (IC base=-0.062)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1198` → IC=+0.250 (n=1193)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1198 (IC base=-0.031)

- **PATRÓN** `ibs_15` < `0.3453` → IC=+0.280 (n=1789)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3453 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` > `0.6992` → IC=+0.303 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6992 (IC base=-0.031)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.220 (n=405)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=1216)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.232 (n=405)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=1216)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.209 (n=1023)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=598)

- **FILTRO** `sigma_ewma_delta_pct` > `23.635` → IC=-0.250 (n=226)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.635
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=1395)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.162 (n=152)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0029 (IC base=+0.083)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2033` → IC=+0.293 (n=80)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2033 (IC base=+0.083)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1378` → IC=+0.327 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1378 (IC base=+0.083)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.124 (n=312)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 12.0 (IC base=+0.083)

- **PATRÓN** `ibs_15` > `0.7496` → IC=+0.331 (n=175)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7496 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` > `0.102` → IC=+0.287 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.102 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` < `0.5498` → IC=+0.285 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5498 (IC base=+0.083)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6675` → IC=-0.196 (n=100)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6675
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=301)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.166 (n=384)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.190 (n=201)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0051 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.0757` → IC=+0.218 (n=133)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0757 (IC base=+0.153)

- **PATRÓN** `drift_15min` |x|≤ `0.4223` → IC=+0.170 (n=101)

  - _Acción_: Kelly boost +0.85€ cuando `drift_15min` |x|≤ 0.4223 (IC base=+0.153)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0589` → IC=+0.157 (n=301)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.78€ cuando `delta_ratio_macro` |x|> 0.0589 (IC base=+0.153)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2902` → IC=+0.240 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2902 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.206 (n=141)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.153)

- **PATRÓN** `ibs_15` > `0.6675` → IC=+0.269 (n=301)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6675 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.4741` → IC=+0.159 (n=86)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.4741 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.1187` → IC=+0.188 (n=216)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.1187 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.857` → IC=+0.165 (n=240)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 6.857 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.166 (n=384)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `11008.7835` → IC=+0.198 (n=137)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 11008.7835 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.275 (n=234)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.4388` → IC=+0.232 (n=700)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4388 (IC base=+0.232)

- **PATRÓN** `drift_15min` |x|≤ `0.4792` → IC=+0.242 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4792 (IC base=+0.232)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2029` → IC=+0.263 (n=318)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2029 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.240 (n=275)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.244 (n=315)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.232)

- **PATRÓN** `ibs_15` < `0.3441` → IC=+0.271 (n=700)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3441 (IC base=+0.232)

- **PATRÓN** `dist_vwap_pct` > `0.7711` → IC=+0.314 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7711 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.687` → IC=+0.262 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.687 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.153` → IC=+0.238 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.153 (IC base=+0.232)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1671` → IC=-0.218 (n=214)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1671
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=416)

- **FILTRO** `drift_15min` |x|> `0.89` → IC=-0.267 (n=157)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.89
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=473)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.214 (n=246)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=384)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.350 (n=18)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=-0.169)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0761` → IC=+0.230 (n=279)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0761 (IC base=-0.042)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.268 (n=312)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.7712` → IC=+0.212 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7712 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` < `0.2005` → IC=+0.225 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2005 (IC base=-0.042)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.2002` → IC=-0.199 (n=264)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.2002
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=514)

- **FILTRO** `sigma_h` > `0.0198` → IC=-0.262 (n=388)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0198
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=390)

- **FILTRO** `drift_15min` |x|> `1.2555` → IC=-0.265 (n=194)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2555
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=584)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.263 (n=188)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=590)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1333` → IC=+0.288 (n=215)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1333 (IC base=-0.042)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.103` → IC=+0.341 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.103 (IC base=-0.042)

- **PATRÓN** `ibs_15` < `0.3429` → IC=+0.305 (n=474)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3429 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.943` → IC=+0.353 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.943 (IC base=-0.042)

### UPDOWN_GBM_ETH_15M_HORA7
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2775` → IC=-0.136 (n=20)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2775
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **FILTRO** `ibs_15` < `0.8489` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8489
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **PATRÓN** `drift_60min` |x|≤ `0.083` → IC=+0.177 (n=29)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.083 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` > `0.1565` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1565 (IC base=+0.052)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2775` → IC=-0.136 (n=20)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2775
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **FILTRO** `ibs_15` < `0.8489` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8489
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **PATRÓN** `drift_60min` |x|≤ `0.083` → IC=+0.177 (n=29)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.083 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` > `0.1565` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1565 (IC base=+0.052)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.301 (n=446)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.0563` → IC=+0.331 (n=223)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0563 (IC base=+0.295)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2402` → IC=+0.309 (n=223)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2402 (IC base=+0.295)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1077` → IC=+0.350 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1077 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.316 (n=697)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.295)

- **PATRÓN** `ibs_15` > `0.8404` → IC=+0.330 (n=668)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8404 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` > `0.2769` → IC=+0.329 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2769 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.34` → IC=+0.330 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.34 (IC base=+0.295)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.297 (n=814)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.295)

- **PATRÓN** `libro_liquidez` > `13082.2536` → IC=+0.307 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13082.2536 (IC base=+0.295)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.302 (n=246)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.287)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.287 (n=167)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.0574` → IC=+0.348 (n=123)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0574 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.262` → IC=+0.308 (n=123)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.262 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3807` → IC=+0.310 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3807 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.346 (n=173)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.8292` → IC=+0.317 (n=369)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8292 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.4454` → IC=+0.357 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4454 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.469` → IC=+0.359 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.469 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `16196.8854` → IC=+0.324 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16196.8854 (IC base=+0.287)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.315 (n=300)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.303)

- **PATRÓN** `drift_60min` |x|≤ `0.0692` → IC=+0.306 (n=132)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0692 (IC base=+0.303)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1464` → IC=+0.312 (n=200)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1464 (IC base=+0.303)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.288` → IC=+0.342 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.288 (IC base=+0.303)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.336 (n=291)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.303)

- **PATRÓN** `ibs_15` > `0.8516` → IC=+0.344 (n=300)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8516 (IC base=+0.303)

- **PATRÓN** `dist_vwap_pct` > `0.6408` → IC=+0.314 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6408 (IC base=+0.303)

- **PATRÓN** `dist_vwap_pct` < `0.167` → IC=+0.306 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.167 (IC base=+0.303)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.463` → IC=+0.324 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.463 (IC base=+0.303)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.311 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.303)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2573` → IC=-0.167 (n=70)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2573
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=212)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1143` → IC=-0.167 (n=70)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1143
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=212)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.176 (n=109)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=333)

- **FILTRO** `ballena_activa_n` > `60.0` → IC=-0.223 (n=45)

  - _Acción_: SKIP cuando `ballena_activa_n` > 60.0
  - _Potencial_: sin este filtro IC_bueno=-0.123 (n=136)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1226` → IC=-0.151 (n=41)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1226
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=124)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2312` → IC=-0.233 (n=28)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2312
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=15)

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
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `drift_15min` |x|> `0.1344` → IC=-0.241 (n=25)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.1344
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

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
- **PATRÓN** `T_h` > `87.9965` → IC=+0.222 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9965 (IC base=+0.202)

- **PATRÓN** `ratio` < `0.9775` → IC=+0.469 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9775 (IC base=+0.202)

- **PATRÓN** `T_h` > `145.7851` → IC=+0.394 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7851 (IC base=+0.332)

- **PATRÓN** `ratio` > `1.0554` → IC=+0.399 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0554 (IC base=+0.332)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `73.1081` → IC=+0.191 (n=134)

  - _Acción_: Kelly boost +0.96€ cuando `T_h` > 73.1081 (IC base=+0.178)

- **PATRÓN** `ratio` < `0.973` → IC=+0.444 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.178)

- **PATRÓN** `T_h` > `102.1277` → IC=+0.288 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 102.1277 (IC base=+0.281)

- **PATRÓN** `ratio` > `1.0455` → IC=+0.330 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0455 (IC base=+0.281)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `89.3454` → IC=+0.281 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 89.3454 (IC base=+0.244)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.417 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.244)

- **PATRÓN** `T_h` > `103.3918` → IC=+0.327 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 103.3918 (IC base=+0.309)

- **PATRÓN** `ratio` > `1.0131` → IC=+0.312 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0131 (IC base=+0.309)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1359` → IC=+0.457 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1359 (IC base=+0.403)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6068 sube el IC de +0.186 a +0.268 en UPDOWN_GBM#15min (n=1637). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7036 sube el IC de +0.207 a +0.276 en UPDOWN_GBM#BTC#15min (n=368). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6602 sube el IC de +0.137 a +0.258 en UPDOWN_GBM#ETH#15min (n=341). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6111 sube el IC de +0.173 a +0.265 en UPDOWN_GBM#SOL#15min (n=194). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.55 sube el IC de +0.188 a +0.281 en UPDOWN_GBM#XRP#15min (n=431). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1176 sube el IC de +0.050 a +0.159 en UPDOWN_GBM#XRP#15min (n=485). Ya aplicado como kelly_boost=+0.80€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6371 sube el IC de -0.062 a +0.277 en UPDOWN_GBM_15M_TARDIO (n=636). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3453 sube el IC de -0.031 a +0.280 en UPDOWN_GBM_15M_TARDIO (n=1789). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7496 sube el IC de +0.083 a +0.331 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=175). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6675 sube el IC de +0.153 a +0.269 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=301). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3441 sube el IC de +0.232 a +0.271 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=700). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.169 a +0.350 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=18). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.042 a +0.268 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=312). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3429 sube el IC de -0.042 a +0.305 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=474). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8404 sube el IC de +0.295 a +0.330 en UPDOWN_GBM_IBS_ALTO (n=668). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8292 sube el IC de +0.287 a +0.317 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=369). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8516 sube el IC de +0.303 a +0.344 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=300). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7873 sube el IC de +0.342 a +0.385 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=417). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8166 sube el IC de +0.345 a +0.380 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=231). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7408 sube el IC de +0.336 a +0.394 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=186). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1333 | +0.099 | +199.89€ | 1 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1333 | +0.099 | +199.89€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 994 | +0.108 | +171.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 994 | +0.108 | +171.76€ | 2 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 253 | +0.057 | +9.47€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 253 | +0.057 | +9.47€ | 6 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 60 | +0.145 | +20.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 60 | +0.145 | +20.16€ | 0 | 7 |
| ✅ BALLENAS_TARDIAS | 28419 | -0.090 | -3826.28€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1467 | -0.051 | -223.54€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 26952 | -0.092 | -3602.74€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3726 | -0.095 | -612.45€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3726 | -0.095 | -612.45€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1467 | -0.051 | -223.54€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1467 | -0.051 | -223.54€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3479 | -0.096 | -791.31€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3479 | -0.096 | -791.31€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 7288 | -0.022 | -678.18€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 7288 | -0.022 | -678.18€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 6865 | -0.094 | -432.14€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 6865 | -0.094 | -432.14€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 5594 | -0.177 | -1088.66€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 5594 | -0.177 | -1088.66€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 18420 | -0.028 | +4015.21€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 4805 | -0.000 | +1817.11€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 13615 | -0.037 | +2198.10€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 18420 | -0.028 | +4015.21€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 4805 | -0.000 | +1817.11€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 13615 | -0.037 | +2198.10€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 1478 | -0.103 | -191.97€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 168 | -0.053 | -21.36€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 1310 | -0.110 | -170.61€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 780 | -0.091 | -97.63€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 144 | -0.048 | -16.13€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 636 | -0.100 | -81.50€ | 1 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 491 | -0.125 | -74.32€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 24 | -0.077 | -5.22€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#5min | 467 | -0.127 | -69.10€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 66 | -0.191 | -10.49€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 66 | -0.191 | -10.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 93643 | +0.112 | -4776.53€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 14107 | +0.185 | -431.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 376 | -0.082 | -50.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 73081 | +0.099 | -4077.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 6079 | +0.107 | -217.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 12152 | +0.098 | -1034.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 45 | -0.160 | -0.32€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 12092 | +0.099 | -1022.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 18943 | +0.131 | -375.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4452 | +0.203 | -134.86€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 12117 | +0.111 | -200.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2332 | +0.104 | -17.94€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 12193 | +0.089 | -1134.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 52 | -0.093 | -6.98€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 12126 | +0.090 | -1116.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 19919 | +0.123 | -402.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 5460 | +0.175 | -81.80€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 12247 | +0.105 | -255.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2200 | +0.098 | -57.06€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 18268 | +0.113 | -1099.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4051 | +0.188 | -215.91€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 279 | -0.041 | +3.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 12391 | +0.090 | -745.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1547 | +0.125 | -142.08€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 12168 | +0.100 | -728.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 47 | -0.031 | +8.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 12108 | +0.101 | -736.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 14853 | +0.191 | -991.01€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 14853 | +0.191 | -991.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3536 | +0.167 | -374.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3536 | +0.167 | -374.09€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1247 | +0.194 | -15.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1247 | +0.194 | -15.18€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3484 | +0.179 | -303.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3484 | +0.179 | -303.47€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3089 | +0.239 | -99.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3089 | +0.239 | -99.85€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3418 | +0.191 | -212.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3418 | +0.191 | -212.17€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 698 | +0.430 | -18.91€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 698 | +0.430 | -18.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 270 | +0.438 | -2.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 270 | +0.438 | -2.69€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 262 | +0.436 | -3.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 262 | +0.436 | -3.22€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 156 | +0.405 | -10.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 156 | +0.405 | -10.50€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 51172 | +0.197 | -4020.65€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 51172 | +0.197 | -4020.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 8853 | +0.176 | -1025.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 8853 | +0.176 | -1025.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 8173 | +0.222 | -307.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 8173 | +0.222 | -307.18€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 8836 | +0.172 | -1065.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 8836 | +0.172 | -1065.35€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 8268 | +0.219 | -318.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 8268 | +0.219 | -318.80€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 8455 | +0.204 | -551.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 8455 | +0.204 | -551.61€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 8587 | +0.193 | -752.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 8587 | +0.193 | -752.32€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 19312 | +0.118 | +175.10€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 19312 | +0.118 | +175.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 9586 | +0.122 | +152.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 9586 | +0.122 | +152.44€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 9726 | +0.113 | +22.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 9726 | +0.113 | +22.65€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1481 | +0.290 | -17.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1481 | +0.290 | -17.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 660 | +0.276 | -19.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 660 | +0.276 | -19.34€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 711 | +0.292 | +0.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 711 | +0.292 | +0.51€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 110 | +0.339 | +1.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 110 | +0.339 | +1.42€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 648 | +0.437 | -1.60€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 648 | +0.437 | -1.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 306 | +0.435 | -2.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 306 | +0.435 | -2.31€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 299 | +0.440 | +0.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 299 | +0.440 | +0.48€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 43 | +0.389 | +0.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 43 | +0.389 | +0.23€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1122 | +0.076 | -41.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 390 | +0.059 | -32.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 732 | +0.085 | -9.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 61 | +0.119 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 61 | +0.119 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 885 | +0.083 | -15.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 153 | +0.074 | -5.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 732 | +0.085 | -9.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 176 | +0.022 | -30.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 176 | +0.022 | -30.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 35863 | +0.097 | -1114.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 2963 | +0.090 | +26.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 32900 | +0.097 | -1140.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 20132 | +0.101 | -329.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 2963 | +0.090 | +26.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 17169 | +0.103 | -355.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 6751 | +0.106 | -50.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 6751 | +0.106 | -50.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 8980 | +0.080 | -734.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 8980 | +0.080 | -734.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 806 | +0.215 | -97.50€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 806 | +0.215 | -97.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 806 | +0.215 | -97.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 806 | +0.215 | -97.50€ | 2 | 4 |
| ✅ GBM_LATE_15M | 25720 | +0.083 | +12209.77€ | 0 | 17 |
| ✅ GBM_LATE_15M#15min | 25720 | +0.083 | +12209.77€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 4301 | +0.193 | +3126.09€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 4301 | +0.193 | +3126.09€ | 0 | 19 |
| ✅ GBM_LATE_15M#BTC | 3821 | +0.178 | +2664.25€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 3821 | +0.178 | +2664.25€ | 0 | 27 |
| ✅ GBM_LATE_15M#DOGE | 4480 | +0.198 | +3331.78€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 4480 | +0.198 | +3331.78€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 3777 | +0.021 | +813.20€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 3777 | +0.021 | +813.20€ | 1 | 13 |
| ✅ GBM_LATE_15M#SOL | 3683 | -0.032 | +837.54€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 3683 | -0.032 | +837.54€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 5658 | -0.040 | +1436.92€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 5658 | -0.040 | +1436.92€ | 4 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 27176 | +0.086 | +14194.96€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 27176 | +0.086 | +14194.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 5158 | +0.017 | +2716.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 5158 | +0.017 | +2716.85€ | 1 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 5669 | +0.015 | +1177.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 5669 | +0.015 | +1177.17€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 3863 | +0.262 | +3889.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 3863 | +0.262 | +3889.54€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 4410 | +0.003 | +845.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 4410 | +0.003 | +845.97€ | 2 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 4409 | +0.029 | +1670.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 4409 | +0.029 | +1670.12€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 3667 | +0.275 | +3895.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 3667 | +0.275 | +3895.32€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 20721 | +0.168 | +15423.15€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 20721 | +0.168 | +15423.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3122 | +0.206 | +2480.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3122 | +0.206 | +2480.00€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3293 | +0.149 | +2413.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3293 | +0.149 | +2413.31€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3254 | +0.207 | +2580.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3254 | +0.207 | +2580.42€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 3474 | +0.133 | +2420.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 3474 | +0.133 | +2420.56€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 3856 | +0.115 | +2611.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 3856 | +0.115 | +2611.80€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 3722 | +0.202 | +2917.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 3722 | +0.202 | +2917.07€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 5202 | +0.128 | +2205.57€ | 0 | 22 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 5202 | +0.128 | +2205.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 195 | +0.119 | +84.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 195 | +0.119 | +84.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1488 | +0.124 | +676.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1488 | +0.124 | +676.50€ | 0 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 373 | +0.143 | +176.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 373 | +0.143 | +176.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1537 | +0.144 | +689.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1537 | +0.144 | +689.26€ | 0 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1103 | +0.104 | +363.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1103 | +0.104 | +363.16€ | 1 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 506 | +0.134 | +215.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 506 | +0.134 | +215.28€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 25833 | +0.175 | +19230.53€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 25833 | +0.175 | +19230.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 4097 | +0.220 | +3450.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 4097 | +0.220 | +3450.88€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 4049 | +0.151 | +2684.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 4049 | +0.151 | +2684.62€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 4244 | +0.225 | +3642.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 4244 | +0.225 | +3642.27€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 4184 | +0.137 | +2870.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 4184 | +0.137 | +2870.26€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 4519 | +0.113 | +2865.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 4519 | +0.113 | +2865.03€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 4740 | +0.205 | +3717.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 4740 | +0.205 | +3717.46€ | 0 | 24 |
| ✅ GBM_LATE_5M | 7041 | +0.148 | +4052.11€ | 1 | 28 |
| ✅ GBM_LATE_5M#5min | 7041 | +0.148 | +4052.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 594 | +0.186 | +416.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 594 | +0.186 | +416.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1802 | +0.148 | +1194.65€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1802 | +0.148 | +1194.65€ | 0 | 31 |
| ✅ GBM_LATE_5M#DOGE | 889 | +0.171 | +564.50€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 889 | +0.171 | +564.50€ | 0 | 22 |
| ✅ GBM_LATE_5M#ETH | 2323 | +0.153 | +1335.49€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2323 | +0.153 | +1335.49€ | 0 | 32 |
| ✅ GBM_LATE_5M#SOL | 600 | +0.103 | +213.75€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 600 | +0.103 | +213.75€ | 0 | 17 |
| ✅ GBM_LATE_5M#XRP | 833 | +0.117 | +327.16€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 833 | +0.117 | +327.16€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1742 | +0.068 | +736.81€ | 2 | 11 |
| ✅ GBM_LATE_60M#60min | 1742 | +0.068 | +736.81€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 630 | +0.085 | +262.55€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 630 | +0.085 | +262.55€ | 0 | 12 |
| ✅ GBM_LATE_60M#ETH | 576 | +0.071 | +286.50€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 576 | +0.071 | +286.50€ | 2 | 15 |
| ✅ GBM_LATE_60M#SOL | 536 | +0.043 | +187.76€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 536 | +0.043 | +187.76€ | 2 | 11 |
| 🚫 GBM_LATE_60M_FADE | 377 | -0.255 | -22.01€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 377 | -0.255 | -22.01€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 145 | -0.221 | -7.65€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 145 | -0.221 | -7.65€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 124 | -0.254 | -7.92€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 124 | -0.254 | -7.92€ | 4 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 108 | -0.291 | -6.44€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 108 | -0.291 | -6.44€ | 3 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 700 | +0.070 | +143.97€ | 2 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 700 | +0.070 | +143.97€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 274 | +0.058 | +44.67€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 274 | +0.058 | +44.67€ | 2 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 202 | +0.029 | +4.87€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 202 | +0.029 | +4.87€ | 1 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 224 | +0.119 | +94.43€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 224 | +0.119 | +94.43€ | 2 | 11 |
| ✅ LATE_WINDOW_5MIN | 98 | +0.260 | +81.48€ | 0 | 9 |
| ✅ LATE_WINDOW_5MIN#5min | 98 | +0.260 | +81.48€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 98 | +0.260 | +81.48€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 98 | +0.260 | +81.48€ | 0 | 9 |
| ✅ LEADLAG_BTC_XRP_15M | 1959 | +0.100 | +528.69€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1959 | +0.100 | +528.69€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1959 | +0.100 | +528.69€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1959 | +0.100 | +528.69€ | 0 | 1 |
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
| ✅ LIQUIDACIONES_5M | 1999 | +0.006 | +12.68€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1999 | +0.006 | +12.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 104 | +0.019 | -1.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 104 | +0.019 | -1.14€ | 0 | 1 |
| ✅ LIQUIDACIONES_5M#BTC | 224 | -0.009 | +9.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 224 | -0.009 | +9.00€ | 5 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 163 | -0.039 | -7.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 163 | -0.039 | -7.98€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 840 | +0.025 | +22.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 840 | +0.025 | +22.36€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 471 | -0.001 | -5.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 471 | -0.001 | -5.44€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 197 | -0.013 | -4.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 197 | -0.013 | -4.12€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M | 1082 | -0.044 | -27.41€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1082 | -0.044 | -27.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 307 | -0.044 | -13.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 307 | -0.044 | -13.45€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 361 | -0.026 | -0.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 361 | -0.026 | -0.87€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 414 | -0.060 | -13.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 414 | -0.060 | -13.09€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 1224 | -0.031 | -6.25€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 573 | -0.041 | -20.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 651 | -0.022 | +14.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 34 | +0.000 | +3.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 19 | +0.023 | +1.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 15 | -0.022 | +1.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 309 | +0.040 | +45.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 142 | +0.014 | +9.69€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 167 | +0.062 | +35.70€ | 0 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 177 | -0.075 | -18.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 83 | -0.076 | -10.23€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 94 | -0.073 | -7.92€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 217 | -0.089 | -30.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 97 | -0.106 | -15.88€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 120 | -0.074 | -14.37€ | 6 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 197 | -0.013 | +9.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 101 | -0.015 | +4.20€ | 3 | 3 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 96 | -0.010 | +5.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 290 | -0.051 | -16.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 131 | -0.056 | -10.06€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 159 | -0.047 | -6.24€ | 4 | 2 |
| ✅ MOMENTUM_IBS_15M | 14412 | -0.011 | -204.84€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14412 | -0.011 | -204.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 3129 | -0.019 | -58.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 3129 | -0.019 | -58.02€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 29088 | -0.006 | +1329.55€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 29088 | -0.006 | +1329.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 5133 | +0.018 | +632.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 5133 | +0.018 | +632.90€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 4503 | -0.028 | -46.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 4503 | -0.028 | -46.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 5181 | +0.015 | +465.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 5181 | +0.015 | +465.75€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 4282 | -0.051 | -127.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 4282 | -0.051 | -127.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 4866 | -0.010 | +185.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 4866 | -0.010 | +185.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 5123 | +0.008 | +219.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 5123 | +0.008 | +219.96€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 5839 | -0.058 | -136.42€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 5839 | -0.058 | -136.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1207 | +0.000 | -14.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1207 | +0.000 | -14.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1418 | -0.082 | -37.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1418 | -0.082 | -37.32€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 44 | -0.130 | -5.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 44 | -0.130 | -5.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 631 | -0.111 | -17.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 631 | -0.111 | -17.66€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1692 | -0.079 | -35.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1692 | -0.079 | -35.05€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 73763 | -0.072 | +1748.93€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 73763 | -0.072 | +1748.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 12472 | -0.079 | +717.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 12472 | -0.079 | +717.11€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 11376 | -0.092 | -495.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 11376 | -0.092 | -495.17€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 12684 | -0.067 | +701.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 12684 | -0.067 | +701.99€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 10905 | -0.093 | -183.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 10905 | -0.093 | -183.86€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 13513 | -0.048 | +408.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 13513 | -0.048 | +408.94€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 12813 | -0.062 | +599.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 12813 | -0.062 | +599.91€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7614 | -0.024 | -119.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7614 | -0.024 | -119.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1688 | -0.028 | -5.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1688 | -0.028 | -5.33€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1003 | -0.020 | -31.30€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2151 | -0.019 | -24.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2151 | -0.019 | -24.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1038 | -0.040 | -14.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1038 | -0.040 | -14.89€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 738 | -0.020 | -23.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 738 | -0.020 | -23.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 1131 | +0.105 | +366.67€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#5min | 995 | +0.111 | +354.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 229 | +0.132 | +109.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 229 | +0.132 | +109.02€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 194 | +0.092 | +43.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 194 | +0.092 | +43.99€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 203 | +0.090 | +63.36€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 203 | +0.090 | +63.36€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#SOL | 177 | +0.131 | +80.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 177 | +0.131 | +80.23€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 192 | +0.103 | +57.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 192 | +0.103 | +57.48€ | 0 | 5 |
| ✅ ORDER_FLOW_5M_REACTIVO | 490 | -0.065 | -62.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 490 | -0.065 | -62.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 102 | -0.010 | +2.06€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 102 | -0.010 | +2.06€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 59 | -0.139 | -18.29€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 59 | -0.139 | -18.29€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 146 | -0.088 | -30.29€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 146 | -0.088 | -30.29€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 106 | -0.009 | -0.29€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 106 | -0.009 | -0.29€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 77 | -0.108 | -15.69€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 77 | -0.108 | -15.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 568 | -0.103 | -43.94€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 261 | -0.158 | -61.43€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 213 | -0.202 | -64.12€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 48 | +0.040 | +2.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 198 | -0.075 | +0.63€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 154 | -0.083 | -7.51€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 44 | -0.043 | +8.15€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 109 | -0.022 | +16.86€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 87 | -0.039 | +10.17€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 22 | +0.042 | +6.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 454 | -0.132 | -61.46€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 114 | +0.009 | +17.52€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 710 | -0.206 | -32.61€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 292 | -0.201 | -27.02€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 255 | -0.197 | -26.63€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 37 | -0.218 | -0.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 245 | -0.221 | -22.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 213 | -0.230 | -27.06€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 32 | -0.147 | +4.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 173 | -0.191 | +16.81€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 157 | -0.192 | +12.14€ | 6 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 16 | -0.133 | +4.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 625 | -0.208 | -41.54€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 85 | -0.190 | +8.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 291 | +0.411 | +222.45€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 29 | +0.048 | -4.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 29 | +0.048 | -4.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 79 | +0.377 | +58.79€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 79 | +0.377 | +58.79€ | 0 | 6 |
| ✅ RESOLUTION_SNIPER#SOL | 183 | +0.478 | +167.90€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 183 | +0.478 | +167.90€ | 0 | 13 |
| ✅ RESOLUTION_SNIPER#sniper | 291 | +0.411 | +222.45€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 513 | +0.034 | +18.23€ | 3 | 2 |
| ✅ STREAK_FADE_15M#15min | 513 | +0.034 | +18.23€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 244 | +0.033 | +5.48€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 244 | +0.033 | +5.48€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 35 | +0.068 | +1.22€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 35 | +0.068 | +1.22€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 54 | +0.000 | -0.99€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 54 | +0.000 | -0.99€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 180 | +0.038 | +12.53€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 180 | +0.038 | +12.53€ | 1 | 3 |
| ✅ STREAK_FADE_5M | 2790 | -0.022 | -114.26€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2790 | -0.022 | -114.26€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 807 | -0.018 | -26.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 807 | -0.018 | -26.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 570 | -0.023 | -23.26€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 570 | -0.023 | -23.26€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 155 | -0.048 | -14.93€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 155 | -0.048 | -14.93€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1258 | -0.021 | -49.67€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1258 | -0.021 | -49.67€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 73 | -0.060 | -7.39€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 73 | -0.060 | -7.39€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 35 | -0.013 | -2.95€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 35 | -0.013 | -2.95€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 7803 | +0.024 | +120.60€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 7803 | +0.024 | +120.60€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2142 | +0.021 | +22.41€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2142 | +0.021 | +22.41€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1766 | +0.036 | +54.14€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1766 | +0.036 | +54.14€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2362 | +0.013 | +5.19€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2362 | +0.013 | +5.19€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1533 | +0.030 | +38.85€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1533 | +0.030 | +38.85€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 7352 | +0.013 | -34.72€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 7352 | +0.013 | -34.72€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2955 | +0.017 | -3.71€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2955 | +0.017 | -3.71€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2874 | +0.013 | -14.26€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2874 | +0.013 | -14.26€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1523 | +0.004 | -16.75€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1523 | +0.004 | -16.75€ | 2 | 0 |
| ✅ UPDOWN_GBM | 37672 | +0.031 | +2257.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 10231 | +0.069 | +1861.09€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 1389 | +0.005 | +7.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 23610 | +0.019 | +368.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2299 | +0.004 | +21.41€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 3904 | +0.067 | +429.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 696 | +0.153 | +281.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 32 | +0.000 | -0.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 3176 | +0.049 | +148.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 6992 | +0.036 | +486.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1294 | +0.083 | +291.17€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 374 | +0.019 | +7.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 4237 | +0.033 | +166.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1032 | +0.003 | +21.56€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 55 | -0.097 | +0.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 4454 | +0.040 | +274.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 651 | +0.140 | +230.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 28 | +0.000 | -1.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 3775 | +0.023 | +45.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 7950 | +0.018 | +281.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 2616 | +0.047 | +274.14€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 364 | +0.005 | +6.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 4145 | +0.005 | +4.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 779 | -0.001 | -6.77€ | 2 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 46 | -0.146 | +3.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 8862 | +0.014 | +219.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2475 | +0.028 | +174.79€ | 0 | 12 |
| ✅ UPDOWN_GBM#SOL#240min | 356 | -0.006 | -2.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 5503 | +0.011 | +42.98€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 488 | +0.014 | +6.63€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 40 | -0.167 | -2.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 5508 | +0.035 | +567.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2499 | +0.082 | +609.12€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 235 | -0.002 | -3.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 2774 | -0.004 | -38.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 141 | -0.136 | +0.93€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 556 | +0.342 | +170.22€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 556 | +0.342 | +170.22€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 308 | +0.345 | +89.86€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 308 | +0.345 | +89.86€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 248 | +0.336 | +80.36€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 248 | +0.336 | +80.36€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 12076 | -0.038 | +2562.33€ | 2 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 12076 | -0.038 | +2562.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 791 | -0.040 | +358.99€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 791 | -0.040 | +358.99€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2228 | -0.121 | +18.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2228 | -0.121 | +18.84€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 404 | +0.182 | +273.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 404 | +0.182 | +273.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1334 | +0.208 | +791.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1334 | +0.208 | +791.21€ | 2 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 3650 | -0.064 | +550.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 3650 | -0.064 | +550.27€ | 3 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 3669 | -0.075 | +569.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 3669 | -0.075 | +569.44€ | 4 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 141 | +0.038 | +8.84€ | 2 | 2 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 141 | +0.038 | +8.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 141 | +0.038 | +8.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 141 | +0.038 | +8.84€ | 2 | 2 |
| ✅ UPDOWN_GBM_IBS_ALTO | 890 | +0.295 | +722.89€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 890 | +0.295 | +722.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 491 | +0.287 | +374.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 491 | +0.287 | +374.39€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 399 | +0.303 | +348.50€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 399 | +0.303 | +348.50€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 724 | -0.110 | -83.09€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 724 | -0.110 | -83.09€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 208 | -0.076 | -14.27€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 208 | -0.076 | -14.27€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 70 | -0.167 | -9.32€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 70 | -0.167 | -9.32€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 67 | -0.196 | -9.44€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 67 | -0.196 | -9.44€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 34 | -0.194 | -7.31€ | 4 | 0 |
| ✅ WEEKLY_PRICE | 2381 | +0.300 | +1197.95€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 820 | +0.248 | +114.01€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 892 | +0.289 | +381.24€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 669 | +0.376 | +702.69€ | 0 | 1 |